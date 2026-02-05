# /// script
# requires-python = ">=3.13"
# dependencies = [
#   'requests>=2.32.5',
#   'tqdm>=4.67.1',
#   'urllib3>=2.5.0',
#   'diskcache>=5.6.3',
#   'PyGithub==2.8.1',
#   'python-dotenv',
#   'pydantic-settings>=2.12.0'
# ]
# ///
"""
This python script screens resources linked to, and ensures that they're still alive

Environment variables to set: see the _Settings() class below

Note: the header contains all dependencies to easily run with UV
"""

import logging
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import diskcache
import requests
from dotenv import load_dotenv
from github import Auth, Github, Repository
from pydantic_settings import BaseSettings
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from urllib3.util import Retry


class _Settings(BaseSettings):
    # Note: these environment default are set for local operation, appropriate defaults
    #  for production are set in the Github actions file
    GITHUB_API_TOKEN: str
    N_MAXIMUM_CHANGES_PER_ITERATION: int = 10
    ALLOW_CACHING: bool = True
    OPEN_PR: bool = False


load_dotenv()
SETTINGS = _Settings()

github_token = Auth.Token(SETTINGS.GITHUB_API_TOKEN)
if github_token is None:
    raise EnvironmentError(
        "Missing Github token in environment (please initialise GITHUB_API_TOKEN)"
    )
N_MAXIMUM_CHANGES_PER_ITERATION = SETTINGS.N_MAXIMUM_CHANGES_PER_ITERATION
OPEN_PR = SETTINGS.OPEN_PR
ALLOW_CACHING = SETTINGS.ALLOW_CACHING


# Parameters to adjust
IGNORE_URL_PREFIXES = [
    "https://docs.google.com/",
]
TIMEOUT_DEFAULT = 5
ALLOWED_RETRIES = 4

CACHE_LIFETIME_SECONDS = 3600 * 24 * 28  # 28 days of cache lifetime


SESSION = requests.Session()

_retries = Retry(
    total=ALLOWED_RETRIES,
    backoff_factor=0.5,
    backoff_max=60,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods={"POST", "GET"},
)

SESSION = requests.Session()
SESSION.mount("https://", HTTPAdapter(max_retries=_retries))
NAVIGATOR_HEADERS = {
    "User-Agent": "Mozilla/5.0",
}

# Note: if you change the cache, make sure to gitignore the new location
_cache_folder = "maintenance-diskcache/"
os.makedirs(_cache_folder, exist_ok=True)
CACHE = diskcache.Cache(_cache_folder)

GITHUB_CLIENT = Github(auth=github_token)

# ------------------------------------------------------------------------------------
# Connects to Github
# ------------------------------------------------------------------------------------


def change_file_and_create_pull_request(
    repository: Repository,
    base_branch: str,
    file: str,
    f_change_apply: Callable,
    target_branch_name: str,
    commit_message: str,
    pr_name: str,
    pr_body: str,
) -> None:
    # Get the default branch
    base_branch_for_checkout = repository.get_branch(base_branch)
    base_sha = base_branch_for_checkout.commit.sha
    try:
        repository.create_git_ref(ref=f"refs/heads/{target_branch_name}", sha=base_sha)
    except:
        print(f"Ignoring {target_branch_name} as the branch already exists")
        return

    # Get the base file
    base_file_contents = repository.get_contents(file, ref=base_sha)

    # Update the file content
    new_file_contents = f_change_apply(
        base_file_contents.decoded_content.decode("utf-8")
    )

    repository.update_file(
        path=base_file_contents.path,
        message=commit_message,
        content=new_file_contents,
        sha=base_file_contents.sha,
        branch=target_branch_name,
    )

    # Create a pull request
    pr = repository.create_pull(
        title=pr_name,
        body=pr_body,
        head=target_branch_name,
        base=base_branch,
    )
    print(f"Created PR #{pr.number}: {pr.title}")


def change_file_locally(
    f_change_apply: Callable,
    pr_name: str | None = None,
    pr_body: str | None = None,
):
    local_file = str(Path(__file__).parent.parent.parent.parent / "README.md")

    with open(local_file, "r") as f:
        base_file_contents = f.read()

    # Update the file content
    new_file_contents = f_change_apply(base_file_contents)

    with open(local_file, "w") as f:
        f.write(new_file_contents)

    print(f"Updated local file {local_file}")
    if pr_name is not None:
        print(
            f"""

A good PR name could be: 
=======================================
{pr_name}
=======================================

"""
        )
    if pr_body is not None:
        print(
            f"""

A good PR description body could be:
=======================================
    
{pr_body}

=======================================

"""
        )


markdown_file = "README.md"

# ------------------------------------------------------------------------------------
# Reads the file
# ------------------------------------------------------------------------------------


file_io_path = str(Path(__file__).parent.parent.parent.parent / "README.md")

logging.info(f"Reading file: {file_io_path}")
with open(file_io_path, "r") as f:
    md_content = f.read()

# ------------------------------------------------------------------------------------
# Checks all links for obsolete references
# ------------------------------------------------------------------------------------


# Finding links in markdown file
def find_links_in_markdown(markdown_text: str) -> dict[str, str]:
    pattern = r"\[([^\]]+)\]\(([^\)]+)\)|\[([^\]]+)\]\s*\[([^\]]*)\]"
    out = re.findall(pattern, markdown_text)
    return {i[0]: i[1] for i in out}


logging.info("Finding all links in markdown file")
links = find_links_in_markdown(md_content)

external_links = [
    i
    for i in list(links.values())
    if i.startswith("https://") or i.startswith("http://")
]


# ------------------------------------------------------------------------------------
# Helper functions and classes
# ------------------------------------------------------------------------------------
@dataclass
class LinksToMaintain:
    dead_urls = []
    redirected_urls = {}
    forbidden_urls = []
    error_urls = []

    def __len__(self) -> int:
        return (
            len(self.dead_urls)
            + len(self.redirected_urls)
            + len(self.forbidden_urls)
            + len(self.error_urls)
        )


def _cached_session_get(
    s: requests.Session,
    url: str,
    allow_caching: bool,
) -> tuple[int | None, str | None]:
    key = f"url:{url}"
    if allow_caching:
        sc_cached = CACHE.get(key)
        if sc_cached:
            return sc_cached
    r = s.get(
        url,
        allow_redirects=False,
        headers=NAVIGATOR_HEADERS,
        timeout=TIMEOUT_DEFAULT,
    )
    status_code = r.status_code
    if (status_code is not None) and (status_code // 100) == 3:
        next_url = r.next.url
    else:
        next_url = None
    if allow_caching:
        CACHE.set(key=key, value=(status_code, next_url), expire=CACHE_LIFETIME_SECONDS)
    return status_code, next_url


def _ignore_url(url) -> bool:
    ignore = CACHE.get(f"ignore:{url}")
    if ignore:
        return True
    for i in IGNORE_URL_PREFIXES:
        if url.startswith(i):
            # Skip check of URLs that start with prefixes to ignore
            return True
    return False


def _ignore_url_in_next_iterations(url: str) -> None:
    CACHE.set(key=f"ignore:{url}", value=True, expire=CACHE_LIFETIME_SECONDS)
    logging.info(f"Marked {url} for ignoring in next iteration")


# ------------------------------------------------------------------------------------
# Execution of the maintenance itself
# ------------------------------------------------------------------------------------
ltm = LinksToMaintain()

# Identifying invalid and redirected links
logging.info("Checking all links via web requests")

try:
    for url_i in tqdm(external_links):
        try:
            if _ignore_url(url_i):
                continue
            status_code, next_url = _cached_session_get(
                SESSION,
                url_i,
                allow_caching=ALLOW_CACHING,
            )
        except requests.exceptions.ConnectionError:
            status_code = None
        if status_code is None:
            pass
        elif (status_code // 100) == 2:
            pass  # Nothing to declare
        else:
            if status_code is None:
                ltm.error_urls.append(url_i)
            elif status_code == 404:
                ltm.dead_urls.append(url_i)
                logging.warning(f"Dead URL: {url_i}")
            elif (status_code // 100) == 3:
                ltm.redirected_urls[url_i] = next_url
                logging.warning(f"Redirecting {url_i} to {next_url}")
            elif status_code == 403:
                ltm.forbidden_urls.append(url_i)
            else:
                logging.warning(f"Error on {url_i} : status={status_code}")
            _ignore_url_in_next_iterations(url_i)

        if N_MAXIMUM_CHANGES_PER_ITERATION:
            if len(ltm) >= N_MAXIMUM_CHANGES_PER_ITERATION:
                logging.info("Stopping as the maximum number of changes was reached")
                break

except BaseException as e:
    # This is a dirty way to allow for partial runs
    print(f"Interrupting the execution ({e})")

# Closing the cache after requests are made
CACHE.close()

# ------------------------------------------------------------------------------------
# Writing updates in file
# ------------------------------------------------------------------------------------

# Creating PRs for issues detected

common_kwargs = dict(
    repository=GITHUB_CLIENT.get_user("protontypes").get_repo(
        "open-sustainable-technology"
    ),
    base_branch="main",
    file="README.md",
)


# First, fix the redirections
open_prs = common_kwargs.get("repository").get_pulls(state="open", head="main")


def _f_repo_id(url: str) -> str:
    x = url.split("/")
    return f"{x[-2]}/{x[-1]}"


def chunk_dict(x: dict[str, str], chunk_size: int = 3) -> list[dict[str, str]]:
    out = []
    x_keys = list(x.keys())
    for i in range(0, len(x_keys), chunk_size):
        out.append({i: x[i] for i in x_keys[i : i + chunk_size]})
    return out


_relevant_prs_titles = [i.title for i in open_prs]


def _hasnt_yet_been_processed(url: str) -> bool:
    id_short = _f_repo_id(url)
    for i in _relevant_prs_titles:
        if id_short in i:
            return False
    return True


unprocessed_urls = {
    i: v for i, v in ltm.redirected_urls.items() if _hasnt_yet_been_processed(i)
}
if len(unprocessed_urls) < 1:
    print("No REDIRECT updates to carry out")
for redirects in chunk_dict(unprocessed_urls, chunk_size=3):

    def f_fix_redirect(md_content: str) -> str:
        logging.info("Replacing links")
        for old_url, new_url in redirects.items():
            md_content = md_content.replace(old_url, new_url)
        return md_content

    print(redirects)
    sources = list(redirects.keys())
    targets = list(redirects.values())
    branch_name = f"fix-redirects{'-'.join([_f_repo_id(i) for i in sources])}"
    pr_name = f"Redirect {', '.join([_f_repo_id(i) for i in sources])}"
    pr_body = "This PR carries out redirection of the following links:\n" + "\n".join(
        [f"- [{k}]({k}) to [{v}]({v})" for k, v in redirects.items()]
    )
    if OPEN_PR:
        change_file_and_create_pull_request(
            **common_kwargs,
            f_change_apply=f_fix_redirect,
            target_branch_name=branch_name,
            commit_message="Fixing targets",
            pr_name=pr_name,
            pr_body=pr_body,
        )
    else:
        change_file_locally(
            f_change_apply=f_fix_redirect,
        )


# Second: removing the lines with URL issues
def remove_lines_containing(markdown_str, url):
    lines = markdown_str.splitlines()
    filtered_lines = [line for line in lines if url not in line]
    return "\n".join(filtered_lines)


def chunk_list(x: list[str], chunk_size: int = 3) -> list[list[str]]:
    return [x[i : i + chunk_size] for i in range(0, len(x), chunk_size)]


unprocessed_urls = [
    i for i in ltm.dead_urls if _hasnt_yet_been_processed(i)
]  # TODO: add processing of ltm.error_urls
if len(unprocessed_urls) < 1:
    print("No ISSUES updates to carry out")
for urls_issues in chunk_list(unprocessed_urls, chunk_size=1):

    def f_remove_issues(md_content: str) -> str:
        logging.info("Removing links")
        for i in urls_issues:
            md_content = remove_lines_containing(md_content, i)
        return md_content

    print(urls_issues)
    sources = urls_issues
    branch_name = f"remove-dead-{'-'.join([_f_repo_id(i) for i in sources])}"
    pr_name = f"Removing dead {', '.join([_f_repo_id(i) for i in sources])}"
    pr_body = (
        "This PR deletes the links where the target is dead (HTTP 404):\n"
        + "\n".join([f"- [{k}]({k})" for k in sources])
    )
    if OPEN_PR:
        change_file_and_create_pull_request(
            **common_kwargs,
            f_change_apply=f_remove_issues,
            target_branch_name=branch_name,
            commit_message="Removing dead target",
            pr_name=pr_name,
            pr_body=pr_body,
        )
    else:
        change_file_locally(
            f_change_apply=f_fix_redirect,
            pr_name=pr_name,
            pr_body=pr_body,
        )

logging.info("Completed")

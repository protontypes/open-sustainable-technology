"""
This python script screens resources linked to, and ensures that they're still alive
"""

import logging
import os
import re
from dataclasses import dataclass

import diskcache
import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from urllib3.util import Retry

# Parameters to adjust
IGNORE_URL_PREFIXES = [
    "https://docs.google.com/",
]
TIMEOUT_DEFAULT = 5
ALLOWED_RETRIES = 4
N_MAXIMUM_CHANGES_PER_ITERATION: int | None = 5  # None ignores the feature
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

markdown_file = "README.md"

# ------------------------------------------------------------------------------------
# Reads the file
# ------------------------------------------------------------------------------------
if os.path.exists(markdown_file):
    file_io_path = markdown_file
elif os.path.exists(f"../{markdown_file}"):
    file_io_path = f"../{markdown_file}"
else:
    raise FileNotFoundError("Unable to find readme file")

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
    invalid_urls = []
    redirected_urls = {}
    forbidden_urls = []
    error_urls = []

    def __len__(self) -> int:
        return (
            len(self.invalid_urls)
            + len(self.redirected_urls)
            + len(self.forbidden_urls)
            + len(self.error_urls)
        )


def _cached_session_get(s: requests.Session, url: str) -> tuple[int | None, str | None]:
    key = f"url:{url}"
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
    if (status_code // 100) == 3:
        next_url = r.next.url
    else:
        next_url = None
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
            status_code, next_url = _cached_session_get(SESSION, url_i)
        except requests.exceptions.ConnectionError:
            status_code = None
        if (status_code // 100) == 2:
            pass  # Nothing to declare
        else:
            if status_code is None:
                ltm.error_urls.append(url_i)
            elif status_code == 404:
                ltm.invalid_urls.append(url_i)
                logging.warning(f"Invalid URL: {url_i}")
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
logging.info("Replacing links")
for i in ltm.invalid_urls:
    md_content = md_content.replace(i, "DEAD_URL")
for i in ltm.error_urls:
    md_content = md_content.replace(i, "ERROR_URL")
for old_url, new_url in ltm.redirected_urls.items():
    md_content = md_content.replace(old_url, new_url)
# and do nothing about the forbidden ones

logging.info(f"Exporting updated file: {file_io_path}")
with open(file_io_path, "w") as f:
    f.write(md_content)

logging.info("Completed")

"""
This python script screens resources linked to, and ensures that they're still alive
"""

import logging
import os
import re

import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from urllib3.util import Retry

SESSION = requests.Session()
TIMEOUT_DEFAULT = 5

_retries = Retry(
    total=4,
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

# Identifying invalid and redirected links
logging.info("Checking all links via web requests")
invalid_urls = []
redirected_urls = {}
forbidden_urls = []
error_urls = []

for url_i in tqdm(external_links):
    try:
        r = SESSION.get(
            url_i,
            allow_redirects=False,
            headers=NAVIGATOR_HEADERS,
            timeout=TIMEOUT_DEFAULT,
        )
        status_code = r.status_code
    except requests.exceptions.ConnectionError:
        status_code = None
    if status_code is None:
        error_urls.append(url_i)
    elif (status_code // 100) == 2:
        pass  # Nothing to declare
    elif status_code == 404:
        invalid_urls.append(url_i)
        logging.warning(f"Invalid URL: {url_i}")
    elif (status_code // 100) == 3:
        next_url = r.next.url
        redirected_urls[url_i] = next_url
        logging.warning(f"Redirecting {url_i} to {next_url}")
    elif status_code == 403:
        forbidden_urls.append(url_i)
    else:
        logging.warning(f"Error on {url_i} : status={status_code}")


# ------------------------------------------------------------------------------------
# Writing updates in file
# ------------------------------------------------------------------------------------
logging.info("Replacing links")
for i in invalid_urls:
    md_content = md_content.replace(i, "DEAD_URL")
for i in error_urls:
    md_content = md_content.replace(i, "ERROR_URL")
for old_url, new_url in redirected_urls.items():
    md_content = md_content.replace(old_url, new_url)
# and do nothing about the forbidden ones

logging.info(f"Exporting updated file: {file_io_path}")
with open(file_io_path, "w") as f:
    f.write(md_content)

logging.info("Completed")

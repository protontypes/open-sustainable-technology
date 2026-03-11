# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///

import os
import re
import sys
from pathlib import Path

import requests

ECOSYSTEMS_TIMEOUT = 30

KNOWN_OSS_LICENSES = {
    "MIT", "Apache-2.0", "GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0",
    "BSD-2-Clause", "BSD-3-Clause", "MPL-2.0", "AGPL-3.0", "ISC", "Unlicense",
    "0BSD", "Artistic-2.0", "BSL-1.0", "CC0-1.0", "ECL-2.0", "EPL-1.0",
    "EPL-2.0", "EUPL-1.1", "EUPL-1.2", "NCSA", "OSL-3.0", "PostgreSQL",
    "Zlib", "MIT-0",
}


def extract_project_url(pr_body):
    if not pr_body or not pr_body.strip():
        return None
    match = re.search(r"https?://\S+", pr_body)
    if not match:
        return None
    return match.group(0).rstrip(").,;")


def fetch_json(url, params=None):
    try:
        resp = requests.get(url, params=params, timeout=ECOSYSTEMS_TIMEOUT, allow_redirects=True)
        if resp.status_code != 200:
            return None
        return resp.json()
    except Exception:
        return None


def fetch_repos_data(url):
    return fetch_json(
        "https://repos.ecosyste.ms/api/v1/repositories/lookup", {"url": url}
    )


def fetch_packages_data(url):
    data = fetch_json(
        "https://packages.ecosyste.ms/api/v1/packages/lookup", {"repository_url": url}
    )
    if isinstance(data, list):
        return data
    return []


def fetch_commits_data(url):
    return fetch_json(
        "https://commits.ecosyste.ms/api/v1/repositories/lookup", {"url": url}
    )


def fetch_issues_data(url):
    return fetch_json(
        "https://issues.ecosyste.ms/api/v1/repositories/lookup", {"url": url}
    )


def trigger_ost_sync(url):
    try:
        requests.get(
            "https://ost.ecosyste.ms/api/v1/projects/lookup",
            params={"url": url},
            timeout=10,
        )
    except Exception:
        pass


def format_date(iso_string):
    if not iso_string:
        return "N/A"
    return iso_string.split("T")[0]


def format_days(seconds):
    if seconds is None:
        return "N/A"
    days = int(seconds / 86400)
    if days == 0:
        hours = int(seconds / 3600)
        return f"{hours}h"
    if days > 365:
        years = days / 365
        return f"{years:.1f} years"
    return f"{days} days"


def check_active(repo, commits):
    signals = []
    archived = repo.get("archived", False)
    if archived:
        return "no", ["Repository is archived"]

    pushed = repo.get("pushed_at")
    if pushed:
        signals.append(f"Last push: {format_date(pushed)}")

    commits = commits or {}
    past_year_commits = commits.get("past_year_total_commits", 0)
    past_year_committers = commits.get("past_year_total_committers", 0)
    total_commits = commits.get("total_commits", 0)
    total_committers = commits.get("total_committers", 0)
    signals.append(f"{past_year_commits} commits in past year ({total_commits} total)")
    signals.append(f"{past_year_committers} committers in past year ({total_committers} total)")

    if past_year_commits == 0:
        return "no", signals
    if past_year_commits < 5 or past_year_committers < 1:
        return "maybe", signals
    return "yes", signals


def check_documented(repo, packages):
    signals = []
    metadata = repo.get("metadata") or {}
    files = metadata.get("files") or {}

    has_readme = bool(files.get("readme"))
    has_description = bool(repo.get("description"))
    has_homepage = bool(repo.get("homepage"))

    if has_readme:
        signals.append("Has README")
    else:
        signals.append("No README found")

    if has_description:
        signals.append("Has description")

    if has_homepage:
        signals.append(f"Homepage: {repo['homepage']}")

    for pkg in (packages or []):
        doc_url = pkg.get("documentation_url")
        if doc_url:
            signals.append(f"Docs: {doc_url}")
            break

    if not has_readme:
        return "no", signals
    if has_readme and (has_description or has_homepage):
        return "yes", signals
    return "maybe", signals


def check_licensed(repo):
    signals = []
    license_name = repo.get("license")
    metadata = repo.get("metadata") or {}
    files = metadata.get("files") or {}
    has_license_file = bool(files.get("license"))

    if not license_name and not has_license_file:
        signals.append("No license detected")
        return "no", signals

    if license_name:
        signals.append(f"License: {license_name}")
    if has_license_file:
        signals.append("Has LICENSE file")

    if license_name and license_name.lower() in {"other", "none"}:
        return "maybe", signals
    normalized = {l.lower() for l in KNOWN_OSS_LICENSES}
    if license_name and license_name.lower() in normalized:
        return "yes", signals
    if license_name:
        return "maybe", signals
    return "maybe", signals


def check_usage(repo, packages, issues):
    signals = []
    stars = repo.get("stargazers_count", 0)
    forks = repo.get("forks_count", 0)
    signals.append(f"{stars} stars, {forks} forks")

    issues = issues or {}
    issue_authors = issues.get("issue_authors_count", 0)
    pr_authors = issues.get("pull_request_authors_count", 0)
    signals.append(f"{issue_authors} issue authors, {pr_authors} PR authors")

    total_downloads = 0
    total_dep_repos = 0
    total_dep_pkgs = 0
    for pkg in (packages or []):
        downloads = pkg.get("downloads") or 0
        dep_repos = pkg.get("dependent_repos_count") or 0
        dep_pkgs = pkg.get("dependent_packages_count") or 0
        total_downloads += downloads
        total_dep_repos += dep_repos
        total_dep_pkgs += dep_pkgs

    if packages:
        signals.append(f"{total_downloads} downloads, {total_dep_repos} dependent repos, {total_dep_pkgs} dependent packages")

    has_external = (
        stars >= 5
        or forks >= 2
        or issue_authors >= 3
        or pr_authors >= 2
        or total_downloads >= 100
        or total_dep_repos >= 1
    )

    if has_external:
        return "yes", signals
    return "maybe", signals


def verdict_icon(result):
    if result == "yes":
        return "pass"
    if result == "no":
        return "fail"
    return "unclear"


def build_comment(project_url, repos, packages, commits, issues):
    repo = repos or {}
    description = repo.get("description") or "No description"
    language = repo.get("language") or "N/A"

    active_result, active_signals = check_active(repo, commits)
    documented_result, documented_signals = check_documented(repo, packages)
    licensed_result, licensed_signals = check_licensed(repo)
    usage_result, usage_signals = check_usage(repo, packages, issues)

    checks = [
        ("Active", active_result, active_signals),
        ("Documented", documented_result, documented_signals),
        ("Open source license", licensed_result, licensed_signals),
        ("Usage from external parties", usage_result, usage_signals),
    ]

    warnings = ""
    if repo.get("archived"):
        warnings += "> **Warning:** This repository is archived.\n\n"
    if repo.get("fork"):
        warnings += "> **Note:** This repository is a fork.\n\n"

    comment = f"### Project Review: {project_url}\n\n"
    comment += warnings
    comment += f"**{description}** ({language})\n\n"

    for name, result, signals in checks:
        icon = verdict_icon(result)
        comment += f"**{name}:** {icon}\n"
        for signal in signals:
            comment += f"- {signal}\n"
        comment += "\n"

    comment += "---\n\n"

    commits_data = commits or {}
    dds = commits_data.get("dds")
    if dds is not None:
        comment += f"**Dev Distribution Score:** {float(dds) * 100:.1f}%\n\n"

    committers_list = commits_data.get("committers") or []
    if committers_list:
        top = committers_list[:5]
        parts = [f"{c['name']} ({c['count']})" for c in top]
        comment += f"**Top committers:** {', '.join(parts)}\n\n"

    metadata = repo.get("metadata") or {}
    files = metadata.get("files") or {}
    community_files = [
        name.upper()
        for name in ["readme", "license", "contributing", "code_of_conduct", "citation", "funding"]
        if files.get(name)
    ]
    if community_files:
        comment += f"**Community files:** {' | '.join(community_files)}\n\n"

    issues_data = issues or {}
    avg_close_issue = format_days(issues_data.get("avg_time_to_close_issue"))
    avg_close_pr = format_days(issues_data.get("avg_time_to_close_pull_request"))
    if avg_close_issue != "N/A" or avg_close_pr != "N/A":
        comment += f"**Avg time to close:** Issues: {avg_close_issue}, PRs: {avg_close_pr}\n\n"

    scorecard = repo.get("scorecard") or {}
    scorecard_data = scorecard.get("data") or {}
    scorecard_score = scorecard_data.get("score")
    if scorecard_score is not None:
        comment += f"**OpenSSF Scorecard:** {scorecard_score} / 10\n\n"

    if packages:
        comment += "**Packages:**\n\n"
        comment += "| Registry | Name | Version | Downloads | Dependent Repos | Dependent Packages |\n"
        comment += "|---|---|---|---|---|---|\n"
        for pkg in packages:
            ecosystem = pkg.get("ecosystem", "")
            name = pkg.get("name", "")
            version = pkg.get("latest_release_number", "N/A")
            downloads = pkg.get("downloads", "N/A")
            dep_repos = pkg.get("dependent_repos_count", "N/A")
            dep_pkgs = pkg.get("dependent_packages_count", "N/A")
            registry_url = pkg.get("registry_url", "")
            if registry_url:
                name_link = f"[{name}]({registry_url})"
            else:
                name_link = name
            comment += f"| {ecosystem} | {name_link} | {version} | {downloads} | {dep_repos} | {dep_pkgs} |\n"
        comment += "\n"

    comment += "*Data from [ecosyste.ms](https://ecosyste.ms)*\n"

    return comment


def main():
    pr_body = os.environ.get("PR_BODY", "")

    out = Path("pr-review")
    out.mkdir(exist_ok=True)

    project_url = extract_project_url(pr_body)
    if not project_url:
        print("Could not extract a project URL from the PR body.")
        sys.exit(0)

    print(f"Looking up: {project_url}")

    repos = fetch_repos_data(project_url)
    packages = fetch_packages_data(project_url)
    commits = fetch_commits_data(project_url)
    issues = fetch_issues_data(project_url)

    trigger_ost_sync(project_url)

    if not repos and not packages and not commits and not issues:
        comment = f"Could not fetch project data from [ecosyste.ms](https://ecosyste.ms) for: {project_url}"
    else:
        comment = build_comment(project_url, repos, packages, commits, issues)

    (out / "comment.md").write_text(comment)
    print("Data written to pr-review/")


if __name__ == "__main__":
    main()

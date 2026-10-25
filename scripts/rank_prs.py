"""Find every repo you've contributed PRs to, rank by merged PRs, and rewrite the README section."""
import json
import os
import re
import urllib.parse
import urllib.request

USER = "anmol0b"

# A repo shows up once you have at least this many merged PRs in it...
MIN_MERGED = 1
# ...and it has at least this many stars (keeps small personal repos out).
MIN_STARS = 20

# Never show these. Use "owner" to hide a whole org, or "owner/repo" for one repo.
EXCLUDE = {
    "Elyndor-Labs",        # your own team, already shown under Solana
    "Sanjay8602/AutoGPT",  # a fork, not the real AutoGPT
}

STATES = [
    ("open", "is:open", "2ea043"),
    ("merged", "is:merged", "8957e5"),
    ("closed", "is:closed is:unmerged", "cf222e"),
]

START, END = "<!-- OSS:START -->", "<!-- OSS:END -->"


def api(path):
    req = urllib.request.Request("https://api.github.com" + path,
                                 headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def all_prs():
    """Every PR you authored in repos you don't own (search API caps at 1000)."""
    q = urllib.parse.quote(f"author:{USER} type:pr -user:{USER}")
    items, page = [], 1
    while page <= 10:
        data = api(f"/search/issues?q={q}&per_page=100&page={page}")
        items += data["items"]
        if len(data["items"]) < 100:
            break
        page += 1
    return items


def excluded(repo):
    return repo in EXCLUDE or repo.split("/")[0] in EXCLUDE


def line(repo):
    badges = []
    for label, query, color in STATES:
        q = f"repo:{repo} author:{USER} is:pr {query}"
        img = ("https://img.shields.io/github/issues-search?query=" + urllib.parse.quote(q)
               + f"&label={label}&color={color}&style=flat-square")
        link = f"https://github.com/{repo}/pulls?q=" + urllib.parse.quote_plus(f"is:pr author:{USER} {query}")
        badges.append(f"[![{label}]({img})]({link})")
    name = repo.split("/")[1]
    return f"- **[{name}](https://github.com/{repo})** &nbsp; " + " ".join(badges)


def main():
    merged, total = {}, {}
    for pr in all_prs():
        repo = pr["repository_url"].split("/repos/")[1]
        if excluded(repo):
            continue
        total[repo] = total.get(repo, 0) + 1
        if pr.get("pull_request", {}).get("merged_at"):
            merged[repo] = merged.get(repo, 0) + 1

    shown = []
    for repo, m in merged.items():
        if m < MIN_MERGED:
            continue
        if api(f"/repos/{repo}")["stargazers_count"] < MIN_STARS:
            continue
        shown.append(repo)

    shown.sort(key=lambda r: (-merged[r], -total[r], r.lower()))
    body = "\n".join(line(r) for r in shown)

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    readme = re.sub(re.escape(START) + r".*?" + re.escape(END),
                    lambda _: f"{START}\n{body}\n{END}", readme, flags=re.S)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    for r in shown:
        print(f"{merged[r]:>3} merged  {r}")


if __name__ == "__main__":
    main()
"""Rank open source repos by merged PR count and rewrite the README section."""
import json
import os
import re
import urllib.parse
import urllib.request

USER = "anmol0b"

# Repos to show. Add or remove entries here; order only matters for ties.
REPOS = [
    ("openclaw", "openclaw/openclaw"),
    ("agent-orchestrator", "OrchestratorInc/agent-orchestrator"),
    ("networking", "cb7chaitanya/networking"),
    ("orca", "stablyai/orca"),
    ("opencode", "anomalyco/opencode"),
]

STATES = [
    ("open", "is:open", "2ea043"),
    ("merged", "is:merged", "8957e5"),
    ("closed", "is:closed is:unmerged", "cf222e"),
]

START, END = "<!-- OSS:START -->", "<!-- OSS:END -->"


def merged_count(repo):
    q = f"repo:{repo} author:{USER} is:pr is:merged"
    url = "https://api.github.com/search/issues?per_page=1&q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)["total_count"]


def line(name, repo):
    badges = []
    for label, query, color in STATES:
        q = f"repo:{repo} author:{USER} is:pr {query}"
        img = (
            "https://img.shields.io/github/issues-search?query="
            + urllib.parse.quote(q)
            + f"&label={label}&color={color}&style=flat-square"
        )
        link = f"https://github.com/{repo}/pulls?q=" + urllib.parse.quote_plus(f"is:pr author:{USER} {query}")
        badges.append(f"[![{label}]({img})]({link})")
    return f"- **[{name}](https://github.com/{repo})** &nbsp; " + " ".join(badges)


def main():
    counts = {repo: merged_count(repo) for _, repo in REPOS}
    ranked = sorted(REPOS, key=lambda r: -counts[r[1]])  # stable: ties keep list order
    body = "\n".join(line(n, r) for n, r in ranked)

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{body}\n{END}",
        readme,
        flags=re.S,
    )
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new)

    for n, r in ranked:
        print(f"{counts[r]:>3}  {n}")


if __name__ == "__main__":
    main()

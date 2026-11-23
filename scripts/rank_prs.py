"""Find every repo you've contributed PRs to, rank by merged PRs, and rewrite the README section.

Counts come from the GraphQL `user.pullRequests` connection, not the search API:
GitHub search silently misses some PRs (e.g. every PR in stablyai/orca), which made
repos vanish from the list and their search-backed badges read 0.
"""
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

# (label, GraphQL state, badge color)
STATES = [
    ("open", "OPEN", "2ea043"),
    ("merged", "MERGED", "8957e5"),
    ("closed", "CLOSED", "cf222e"),
]

START, END = "<!-- OSS:START -->", "<!-- OSS:END -->"

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    pullRequests(first: 100, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes {
        state
        repository { nameWithOwner stargazerCount isPrivate owner { login } }
      }
    }
  }
}
"""


def graphql(variables):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required (GraphQL API needs auth)")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    return data["data"]


def all_prs():
    """Every PR you authored, across all pages."""
    prs, after = [], None
    while True:
        conn = graphql({"login": USER, "after": after})["user"]["pullRequests"]
        prs += conn["nodes"]
        if not conn["pageInfo"]["hasNextPage"]:
            return prs
        after = conn["pageInfo"]["endCursor"]


def excluded(repo):
    return repo in EXCLUDE or repo.split("/")[0] in EXCLUDE


def line(repo, counts):
    badges = []
    for label, state, color in STATES:
        img = f"https://img.shields.io/badge/{label}-{counts.get(state, 0)}-{color}?style=flat-square"
        query = {"OPEN": "is:open", "MERGED": "is:merged", "CLOSED": "is:closed is:unmerged"}[state]
        link = f"https://github.com/{repo}/pulls?q=" + urllib.parse.quote_plus(f"is:pr author:{USER} {query}")
        badges.append(f"[![{label}]({img})]({link})")
    name = repo.split("/")[1]
    return f"- **[{name}](https://github.com/{repo})** &nbsp; " + " ".join(badges)


def main():
    counts, stars = {}, {}
    for pr in all_prs():
        r = pr["repository"]
        repo = r["nameWithOwner"]
        if r["isPrivate"] or r["owner"]["login"].lower() == USER.lower() or excluded(repo):
            continue
        stars[repo] = r["stargazerCount"]
        c = counts.setdefault(repo, {})
        c[pr["state"]] = c.get(pr["state"], 0) + 1

    shown = [r for r, c in counts.items()
             if c.get("MERGED", 0) >= MIN_MERGED and stars[r] >= MIN_STARS]
    shown.sort(key=lambda r: (-counts[r].get("MERGED", 0), -sum(counts[r].values()), r.lower()))
    body = "\n".join(line(r, counts[r]) for r in shown)

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    readme = re.sub(re.escape(START) + r".*?" + re.escape(END),
                    lambda _: f"{START}\n{body}\n{END}", readme, flags=re.S)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    for r in shown:
        print(f"{counts[r].get('MERGED', 0):>3} merged  {r}")


if __name__ == "__main__":
    main()

"""Fetch the PyPhi commit history — the v8 real recorded series.

The v8 question takes the recurrence instrument off the lab's synthetic trajectories and onto a real
recorded series the lab did not generate. The series is the commit history of PyPhi
(github.com/wmayner/pyphi), the open-source library the lab computes Φ with. Open-source contributors
coordinate through a shared repository and a maintainer who reviews and merges: a real mediated
coordination, with the maintainer the gatekeeper the others reach the codebase through.

This pulls every commit's author and date through the GitHub API and writes `commits_raw.csv`, the
frozen provenance the rest of the study reads. The committed CSV is the snapshot the analysis
reproduces from; re-running this updates it to the current history, which drifts as PyPhi develops.

Run from the repo root (needs an authenticated `gh`):
    python org_frontier/recurrence/real_series/fetch_commits.py
"""

import csv
import json
import os
import re
import subprocess

REPO = "wmayner/pyphi"
OUT = os.path.join(os.path.dirname(__file__), "commits_raw.csv")


def fetch():
    raw = subprocess.run(
        ["gh", "api", "--paginate", f"repos/{REPO}/commits?per_page=100"],
        capture_output=True, text=True, check=True).stdout
    # gh --paginate concatenates JSON arrays; join them into one
    commits = json.loads(re.sub(r"\]\s*\[", ",", raw.strip()))
    rows = []
    for c in commits:
        login = (c.get("author") or {}).get("login")
        name = (c["commit"]["author"] or {}).get("name", "?")
        author = login or name
        date = c["commit"]["author"]["date"][:10]
        rows.append((date, author))
    rows.sort()
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "author"])
        w.writerows(rows)
    print(f"wrote {len(rows)} commits to {OUT}")


if __name__ == "__main__":
    fetch()

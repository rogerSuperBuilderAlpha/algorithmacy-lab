"""Fetch event-level PR and review data — the v9 recorded series.

v8 found that weekly commit activity is too coarse: it records co-presence, not the review-and-merge
causal structure where a maintainer's gatekeeping lives. v9 reads that structure directly. For each
pull request on PyPhi (github.com/wmayner/pyphi), this pulls the author, the merge actor, the open and
merge timestamps, and the review events. The merge actor is observed, so who commits the determination
that a change enters the codebase is a recorded fact here, not a fitted guess.

Writes `prs.csv` (one row per PR) and `reviews.csv` (one row per review event), the frozen provenance
the analysis reads. Re-running updates them to the current state, which drifts as PyPhi develops.

Run from the repo root (needs an authenticated `gh`):
    python org_frontier/recurrence/event_series/fetch_events.py
"""

import csv
import json
import os
import re
import subprocess

REPO = "wmayner/pyphi"
HERE = os.path.dirname(__file__)


def api(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)


def fetch():
    raw = subprocess.run(
        ["gh", "api", "--paginate", f"repos/{REPO}/pulls?state=all&per_page=100"],
        capture_output=True, text=True, check=True).stdout
    prs = json.loads(re.sub(r"\]\s*\[", ",", raw.strip()))

    pr_rows, review_rows = [], []
    for p in prs:
        n = p["number"]
        author = (p.get("user") or {}).get("login", "?")
        created = (p.get("created_at") or "")[:10]
        merged_at = (p.get("merged_at") or "")[:10]
        state = "merged" if p.get("merged_at") else p.get("state", "?")
        merged_by = ""
        if p.get("merged_at"):
            detail = api(f"repos/{REPO}/pulls/{n}")
            if detail:
                merged_by = (detail.get("merged_by") or {}).get("login", "")
        pr_rows.append((n, author, state, created, merged_at, merged_by))
        reviews = api(f"repos/{REPO}/pulls/{n}/reviews") or []
        for r in reviews:
            review_rows.append((n, (r.get("user") or {}).get("login", "?"),
                                r.get("state", "?"), (r.get("submitted_at") or "")[:10]))

    with open(os.path.join(HERE, "prs.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["number", "author", "state", "created", "merged_at", "merged_by"])
        w.writerows(sorted(pr_rows))
    with open(os.path.join(HERE, "reviews.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pr_number", "reviewer", "state", "submitted_at"])
        w.writerows(sorted(review_rows))
    print(f"wrote {len(pr_rows)} PRs and {len(review_rows)} review events")


if __name__ == "__main__":
    fetch()

"""Fetch event-level PR and review data for a review-heavy project — the v10 recorded series.

v9 read PyPhi's merge graph and found a light review culture: a single maintainer the gate, few
reviews. v10 reads a project with a heavy review process, scikit-learn, where two approving reviews are
required before a merge and the core team reviews and merges each other's work. Comparing the two
projects with the same instrument is the governance contrast: where the veto sits, and how shared it
is, under a light review culture against a heavy one.

scikit-learn has tens of thousands of pull requests, so this samples a bounded recent window: the most
recent closed pull requests, up to MAX_MERGED merged ones, a window comparable to PyPhi's full history
and stated rather than silent. Writes `prs.csv` and `reviews.csv`, the frozen provenance.

Run from the repo root (needs an authenticated `gh`):
    python org_frontier/recurrence/review_heavy/fetch_events.py
"""

import csv
import json
import os
import subprocess

REPO = "scikit-learn/scikit-learn"
MAX_MERGED = 150
HERE = os.path.dirname(__file__)


def api(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    return json.loads(out.stdout) if out.returncode == 0 else None


def fetch():
    merged_prs = []
    page = 1
    while len(merged_prs) < MAX_MERGED and page <= 8:
        batch = api(f"repos/{REPO}/pulls?state=closed&per_page=100&page={page}"
                    f"&sort=created&direction=desc")
        if not batch:
            break
        merged_prs += [p for p in batch if p.get("merged_at")]
        page += 1
    merged_prs = merged_prs[:MAX_MERGED]

    pr_rows, review_rows = [], []
    for p in merged_prs:
        n = p["number"]
        author = (p.get("user") or {}).get("login", "?")
        created = (p.get("created_at") or "")[:10]
        merged_at = (p.get("merged_at") or "")[:10]
        detail = api(f"repos/{REPO}/pulls/{n}")
        merged_by = (detail.get("merged_by") or {}).get("login", "") if detail else ""
        pr_rows.append((n, author, "merged", created, merged_at, merged_by))
        for r in api(f"repos/{REPO}/pulls/{n}/reviews") or []:
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
    print(f"wrote {len(pr_rows)} merged PRs and {len(review_rows)} review events from {REPO}")


if __name__ == "__main__":
    fetch()

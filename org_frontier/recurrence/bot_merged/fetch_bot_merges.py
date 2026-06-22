"""Fetch event-level PR data from a bot-merged project — the v11 recorded series.

v9 and v10 read projects where a human merges. v11 reads one where a machine does: Kubernetes, whose
Prow/Tide bot merges a pull request mechanically once a reviewer has approved, an OWNER has approved,
and CI has passed. The merge actor is a bot, so the determination it commits is documented and
institutional: the bot merges if and only if the human approvals and the checks are in place. That makes
the merge a model-bound field case, where the rule is elicited from the platform's documented process
rather than from interviews, and a test of whether the bot is a member of the coordination or a conduit.

This pulls a bounded recent window of merged pull requests with the author, the merge actor (the bot),
the open and merge dates, and the human reviewers who approved. Writes `prs.csv` and `approvals.csv`,
the frozen provenance. The window is stated, not silent.

Run from the repo root (needs an authenticated `gh`):
    python org_frontier/recurrence/bot_merged/fetch_bot_merges.py
"""

import csv
import json
import os
import subprocess

REPO = "kubernetes/kubernetes"
MAX_MERGED = 150
HERE = os.path.dirname(__file__)


def api(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    return json.loads(out.stdout) if out.returncode == 0 else None


def fetch():
    merged = []
    page = 1
    while len(merged) < MAX_MERGED and page <= 10:
        batch = api(f"repos/{REPO}/pulls?state=closed&per_page=100&page={page}"
                    f"&sort=created&direction=desc")
        if not batch:
            break
        merged += [p for p in batch if p.get("merged_at")]
        page += 1
    merged = merged[:MAX_MERGED]

    pr_rows, app_rows = [], []
    for p in merged:
        n = p["number"]
        author = (p.get("user") or {}).get("login", "?")
        created = (p.get("created_at") or "")[:10]
        merged_at = (p.get("merged_at") or "")[:10]
        detail = api(f"repos/{REPO}/pulls/{n}")
        merged_by = (detail.get("merged_by") or {}).get("login", "") if detail else ""
        pr_rows.append((n, author, created, merged_at, merged_by))
        for r in api(f"repos/{REPO}/pulls/{n}/reviews") or []:
            if r.get("state") == "APPROVED":
                app_rows.append((n, (r.get("user") or {}).get("login", "?"),
                                 (r.get("submitted_at") or "")[:10]))

    with open(os.path.join(HERE, "prs.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["number", "author", "created", "merged_at", "merged_by"])
        w.writerows(sorted(pr_rows))
    with open(os.path.join(HERE, "approvals.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pr_number", "approver", "approved_at"])
        w.writerows(sorted(app_rows))
    print(f"wrote {len(pr_rows)} merged PRs and {len(app_rows)} human approvals from {REPO}")


if __name__ == "__main__":
    fetch()

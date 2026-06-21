"""Read scikit-learn's event-level series and contrast its governance with PyPhi's (v9).

The same measures as v9 — the merge gate, the reviewer set, the lifecycle, the elicited-model Φ — run
on a review-heavy project, and each is set beside PyPhi's light-review number. The four-role elicited
model adds the reviewer approval as a gate of its own. Tests the predictions in HYPOTHESES.md.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/review_heavy/analyze.py
"""

import collections
import csv
import datetime as dt
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states

HERE = os.path.dirname(__file__)

# PyPhi v9 numbers, for the light-review comparison (from event_series/FINDINGS.md)
PYPHI = {"reviews_per_pr": 0.32, "top_merger_share": 59, "self_merge": 37,
         "authors": 22, "mergers": 4, "latency_median": 0}


def load():
    with open(os.path.join(HERE, "prs.csv")) as f:
        prs = list(csv.DictReader(f))
    with open(os.path.join(HERE, "reviews.csv")) as f:
        reviews = list(csv.DictReader(f))
    return prs, reviews


def contrast(prs, reviews):
    merged = [p for p in prs if p["merged_by"]]
    mergers = collections.Counter(p["merged_by"] for p in merged)
    authors = collections.Counter(p["author"] for p in prs)
    reviewers = collections.Counter(r["reviewer"] for r in reviews)
    self_merge = sum(1 for p in merged if p["merged_by"] == p["author"])
    top_share = round(100 * mergers.most_common(1)[0][1] / len(merged))
    rpp = round(len(reviews) / len(prs), 1)
    lat = sorted((dt.date.fromisoformat(p["merged_at"]) - dt.date.fromisoformat(p["created"])).days
                 for p in prs if p["merged_at"] and p["created"])
    med = lat[len(lat) // 2]

    print("=== the governance contrast (scikit-learn vs PyPhi v9) ===")
    print(f"  {'metric':<34}{'scikit-learn':>14}{'PyPhi':>10}")
    print(f"  {'reviews per PR (H1)':<34}{rpp:>14}{PYPHI['reviews_per_pr']:>10}")
    print(f"  {'top merger share % (H2)':<34}{top_share:>14}{PYPHI['top_merger_share']:>10}")
    print(f"  {'self-merge %':<34}{round(100*self_merge/len(merged)):>14}{PYPHI['self_merge']:>10}")
    print(f"  {'distinct reviewers (H3)':<34}{len(reviewers):>14}{'-':>10}")
    print(f"  {'distinct authors':<34}{len(authors):>14}{PYPHI['authors']:>10}")
    print(f"  {'distinct mergers (H3)':<34}{len(mergers):>14}{PYPHI['mergers']:>10}")
    print(f"  {'open->merge latency median days (H5)':<34}{med:>14}{PYPHI['latency_median']:>10}")
    print(f"  top mergers: {dict(mergers.most_common(5))}")
    return merged, reviews


def lifecycle(prs, reviews):
    rev_by_pr = collections.defaultdict(list)
    for r in reviews:
        rev_by_pr[r["pr_number"]].append(r["submitted_at"])
    between = total = 0
    for p in prs:
        rs = rev_by_pr.get(p["number"])
        if not rs or not (p["created"] and p["merged_at"]):
            continue
        c = dt.date.fromisoformat(p["created"]); m = dt.date.fromisoformat(p["merged_at"])
        for rd in rs:
            if not rd:
                continue
            total += 1
            between += int(c <= dt.date.fromisoformat(rd) <= m)
    print(f"\n=== H5 reviews falling between open and merge: {between}/{total} ===")


def elicited_phi():
    print("\n=== H4 the four-role review-and-merge model, exact Φ ===")
    # W(0) author, R(1) reviewer-approval, S(2) merger, C(3) codebase. A change enters iff opened,
    # approved, and merged: W reads C, R reads W and C, S reads R and W, C reads S.
    rules = [lambda x: x[3], lambda x: x[0] & x[3], lambda x: x[1] & x[0], lambda x: x[2]]
    labels = ("W", "R", "S", "C")
    v = classify_rules(rules, labels)
    net, tpm = network(rules, labels)
    _, core, phi = complex_over_states(net, tpm, 4)
    members = "".join(labels[i] for i in sorted(core)) if core else "-"
    both = core is not None and 1 in core and 2 in core
    print(f"  elicited four-role model: {v.structure}, whole-system Φ={v.max_phi:.3f}, "
          f"major complex={members} (Φ={phi:.3f})")
    print(f"  both approval (R) and merge (S) gates in the core: {both}")
    print(f"  PyPhi v9 three-role gate was triadic Φ=2.0, core WSC")


if __name__ == "__main__":
    prs, reviews = load()
    contrast(prs, reviews)
    lifecycle(prs, reviews)
    elicited_phi()

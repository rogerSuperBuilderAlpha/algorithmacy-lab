"""Read the event-level PR and review series: the merge gate, the elicited-model Φ, the lifecycle.

The merge actor is observed, so the structural questions the lab usually models can be measured. Who
merges (the veto-player test), how concentrated the gate is, how the open-to-merge order runs, and how
the gate shifts over time. The role triad is then taken through exact Φ under the institutional merge
rule, an elicited model rather than a fitted one. Tests the predictions in HYPOTHESES.md.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/event_series/analyze.py
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


def load():
    with open(os.path.join(HERE, "prs.csv")) as f:
        prs = list(csv.DictReader(f))
    with open(os.path.join(HERE, "reviews.csv")) as f:
        reviews = list(csv.DictReader(f))
    return prs, reviews


def merge_gate(prs):
    merged = [p for p in prs if p["state"] == "merged" and p["merged_by"]]
    mergers = collections.Counter(p["merged_by"] for p in merged)
    authors = collections.Counter(p["author"] for p in prs)
    self_merged = sum(1 for p in merged if p["merged_by"] == p["author"])
    top_merger, top_n = mergers.most_common(1)[0]
    print(f"=== H1/H5 the merge gate ({len(merged)} merged PRs with a recorded merger) ===")
    print(f"  mergers: {dict(mergers.most_common())}")
    print(f"  top merger {top_merger}: {top_n}/{len(merged)} = {100*top_n/len(merged):.0f}% of merges")
    print(f"  self-merged (author == merger): {self_merged}/{len(merged)} = {100*self_merged/len(merged):.0f}%")
    print(f"  distinct authors {len(authors)} vs distinct mergers {len(mergers)}")
    return merged


def disintermediation(merged):
    print("=== H4 does the gate disintermediate over time (self-merge share by year) ===")
    by_year = collections.defaultdict(lambda: [0, 0])   # year -> [self, total]
    for p in merged:
        y = (p["merged_at"] or p["created"])[:4]
        by_year[y][1] += 1
        if p["merged_by"] == p["author"]:
            by_year[y][0] += 1
    for y in sorted(by_year):
        s, t = by_year[y]
        print(f"  {y}: self-merged {s}/{t} = {100*s/t:.0f}%")


def lifecycle(prs, reviews):
    print("=== H3 the open-to-merge lifecycle ===")
    lat = []
    for p in prs:
        if p["state"] == "merged" and p["merged_at"] and p["created"]:
            d = (dt.date.fromisoformat(p["merged_at"]) - dt.date.fromisoformat(p["created"])).days
            lat.append(d)
    lat.sort()
    med = lat[len(lat) // 2]
    print(f"  open->merge latency (days): median {med}, min {lat[0]}, max {lat[-1]}, "
          f"non-negative {sum(1 for d in lat if d >= 0)}/{len(lat)}")
    # review position within the lifecycle, where reviews exist
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
            total += 1
            if c <= dt.date.fromisoformat(rd) <= m:
                between += 1
    print(f"  reviews falling between open and merge: {between}/{total}")


def elicited_phi():
    print("=== H2 the elicited merge triad, exact Φ ===")
    # author W(0), merge gate S(1), codebase C(2). Institutional merge rule:
    # the codebase changes iff a PR (W) is merged by the gate (S); the gate reads the PR and the
    # proposed change (C); the author acts on the merged state. This is the strict bottleneck.
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = classify_rules(rules, labels)
    net, tpm = network(rules, labels)
    _, core, phi = complex_over_states(net, tpm, 3)
    members = "".join(labels[i] for i in sorted(core)) if core else "-"
    print(f"  elicited model (strict bottleneck): {v.structure}, whole-system Φ={v.max_phi:.3f}, "
          f"major complex={members} (Φ={phi:.3f})")
    print(f"  the gate S is the merge actor the data identifies (see H1); the model is institutional,")
    print(f"  not fit to activity.")


if __name__ == "__main__":
    prs, reviews = load()
    merged = merge_gate(prs)
    print()
    disintermediation(merged)
    print()
    lifecycle(prs, reviews)
    print()
    elicited_phi()

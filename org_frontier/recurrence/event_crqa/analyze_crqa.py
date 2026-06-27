"""event_crqa — behavioral cross-recurrence on the v9 PyPhi PR/review history.

v9 read this data structurally: the merge gate is a veto player and sits in the elicited triad's major
complex. This runs the behavioral instrument (CRQA) on the same frozen series and asks whether the gate
the structure names is also the behaviorally most-coupled role.

Series (monthly bins over the project span): author opens (PR created), reviews (submitted), merges
(merged). Each month's count is quantized to three levels (none / at-or-below median positive / above), so
the categorical cross-recurrence matches activity levels across roles. Hypotheses are fixed in
HYPOTHESES.md before this ran.

Run (from the repo root):  python org_frontier/recurrence/event_crqa/analyze_crqa.py
"""

import csv
import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.recurrence.crqa import coupling_matrix, coupling_centrality, peak, crqa  # noqa: E402

EVENT = os.path.join(_REPO_ROOT, "org_frontier", "recurrence", "event_series")
ROLES = ("author", "review", "merge")
MAX_LAG, N_SHUFFLE, SEED = 6, 2000, 0


def _month(date_str):
    return date_str[:7]  # YYYY-MM


def load_monthly():
    """Monthly event counts for the three roles, aligned over the full span."""
    opens, reviews, merges = [], [], []
    with open(os.path.join(EVENT, "prs.csv")) as f:
        for r in csv.DictReader(f):
            if r["created"]:
                opens.append(_month(r["created"]))
            if r["merged_at"]:
                merges.append(_month(r["merged_at"]))
    with open(os.path.join(EVENT, "reviews.csv")) as f:
        for r in csv.DictReader(f):
            if r["submitted_at"]:
                reviews.append(_month(r["submitted_at"]))

    all_months = sorted(set(opens + reviews + merges))
    lo, hi = all_months[0], all_months[-1]
    span = []
    y, m = int(lo[:4]), int(lo[5:7])
    while f"{y:04d}-{m:02d}" <= hi:
        span.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            y, m = y + 1, 1

    idx = {mo: i for i, mo in enumerate(span)}
    counts = np.zeros((len(span), 3), dtype=int)
    for mo in opens:
        counts[idx[mo], 0] += 1
    for mo in reviews:
        counts[idx[mo], 1] += 1
    for mo in merges:
        counts[idx[mo], 2] += 1
    return span, counts


def quantize(col):
    """Three levels: 0 none, 1 at-or-below the median positive month, 2 above it."""
    pos = col[col > 0]
    if pos.size == 0:
        return np.zeros_like(col)
    med = np.median(pos)
    out = np.zeros_like(col)
    out[(col > 0) & (col <= med)] = 1
    out[col > med] = 2
    return out


def main():
    print("EVENT_CRQA — behavioral cross-recurrence on the v9 PR/review history")
    print("=" * 84)
    span, counts = load_monthly()
    traj = np.column_stack([quantize(counts[:, j]) for j in range(3)])
    print(f"  span: {span[0]} .. {span[-1]}  ({len(span)} months)")
    print(f"  totals: author opens {counts[:,0].sum()}, reviews {counts[:,1].sum()}, "
          f"merges {counts[:,2].sum()}")

    # ---- bH1: coupling centrality, merge as hub, vs time-shuffle null ----
    cent = coupling_centrality(traj, max_lag=MAX_LAG)
    order = np.argsort(cent)[::-1]
    print("  coupling centrality: " + ", ".join(f"{ROLES[i]}={cent[i]:.3f}" for i in order))
    top = int(np.argmax(cent))
    rng = np.random.default_rng(SEED)
    null = np.empty(N_SHUFFLE)
    for b in range(N_SHUFFLE):
        sh = np.column_stack([rng.permutation(traj[:, j]) for j in range(3)])
        null[b] = coupling_centrality(sh, max_lag=MAX_LAG)[2]  # merge column
    p = (np.sum(null >= cent[2]) + 1) / (N_SHUFFLE + 1)
    print(f"  merge centrality {cent[2]:.3f} vs shuffle null mean {null.mean():.3f}  p={p:.4f}")

    # ---- bH2: lead-lag into the gate ----
    lag_am, prom_am = peak(traj[:, 0], traj[:, 2], MAX_LAG)
    lag_rm, prom_rm = peak(traj[:, 1], traj[:, 2], MAX_LAG)
    print(f"  peak lag author->merge: {lag_am:+d} months (prom {prom_am:.3f}); "
          f"review->merge: {lag_rm:+d} (prom {prom_rm:.3f})")

    # ---- bH3: determinism per pair ----
    det_am = crqa(traj[:, 0], traj[:, 2])["det"]
    det_ar = crqa(traj[:, 0], traj[:, 1])["det"]
    det_rm = crqa(traj[:, 1], traj[:, 2])["det"]
    dets = {"author-merge": det_am, "author-review": det_ar, "review-merge": det_rm}
    spine = max(dets, key=dets.get)
    print("  determinism: " + ", ".join(f"{k}={v:.3f}" for k, v in dets.items())
          + f"  (highest: {spine})")

    print("=" * 84)
    bH1 = top == 2 and p < 0.05
    bH2 = lag_am >= 0 and lag_rm >= 0
    bH3 = spine == "author-merge"
    bH4 = ROLES[top] == "merge"
    print(f"  bH1 (merge is the behavioral hub, beats shuffle null): "
          f"{'SUPPORTED' if bH1 else 'REFUTED'}")
    print(f"  bH2 (the gate does not lead: author/review lags >= 0): "
          f"{'SUPPORTED' if bH2 else 'REFUTED'}")
    print(f"  bH3 (author-merge is the highest-determinism pair): "
          f"{'SUPPORTED' if bH3 else 'REFUTED'}")
    print(f"  bH4 (the behaviorally-central role is the structural gate, merge): "
          f"{'SUPPORTED' if bH4 else 'REFUTED'}")
    print("=" * 84)
    print("  Reading: whether the merge gate v9 names structurally also reads as the behavioral hub, and "
          "whether the monthly grain can resolve the lead-lag the time-compressed lifecycle hides.")
    print("=" * 84)


if __name__ == "__main__":
    main()

"""bot_crqa — behavioral cross-recurrence on the v11 bot-merged history (Kubernetes/Prow).

v11 read this data structurally: the Tide bot merges all 150 PRs and sits in the elicited triad's major
complex, with the author excluded. This runs the behavioral instrument (CRQA) on the same frozen series and
asks whether the machine merger reads as a transparent conduit — its merge timing driven by upstream events
— in contrast to v9, where a human merge gate was the behavioral hub.

Series (daily bins over 2026-06-01..2026-06-22): author opens (created), human approvals (approved_at,
a partial view), bot merges (merged_at). Each day's count is quantized to three levels. Hypotheses are
fixed in HYPOTHESES.md before this ran.

Run (from the repo root):  python org_frontier/recurrence/bot_crqa/analyze_crqa.py
"""

import csv
import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.recurrence.crqa import coupling_centrality, peak, crqa  # noqa: E402

BOT = os.path.join(_REPO_ROOT, "org_frontier", "recurrence", "bot_merged")
ROLES = ("author", "approval", "merge")
MAX_LAG, N_SHUFFLE, SEED = 4, 2000, 0


def _days(lo, hi):
    """Inclusive list of YYYY-MM-DD strings from lo to hi (same month span here)."""
    import datetime as dt
    a = dt.date.fromisoformat(lo)
    b = dt.date.fromisoformat(hi)
    out = []
    while a <= b:
        out.append(a.isoformat())
        a = a + dt.timedelta(days=1)
    return out


def load_daily():
    opens, approvals, merges = [], [], []
    with open(os.path.join(BOT, "prs.csv")) as f:
        for r in csv.DictReader(f):
            if r["created"]:
                opens.append(r["created"])
            if r["merged_at"]:
                merges.append(r["merged_at"])
    with open(os.path.join(BOT, "approvals.csv")) as f:
        for r in csv.DictReader(f):
            if r["approved_at"]:
                approvals.append(r["approved_at"])
    alld = sorted(set(opens + approvals + merges))
    span = _days(alld[0], alld[-1])
    idx = {d: i for i, d in enumerate(span)}
    counts = np.zeros((len(span), 3), dtype=int)
    for d in opens:
        counts[idx[d], 0] += 1
    for d in approvals:
        counts[idx[d], 1] += 1
    for d in merges:
        counts[idx[d], 2] += 1
    return span, counts


def quantize(col):
    pos = col[col > 0]
    if pos.size == 0:
        return np.zeros_like(col)
    med = np.median(pos)
    out = np.zeros_like(col)
    out[(col > 0) & (col <= med)] = 1
    out[col > med] = 2
    return out


def main():
    print("BOT_CRQA — behavioral cross-recurrence on the v11 bot-merged history")
    print("=" * 84)
    span, counts = load_daily()
    traj = np.column_stack([quantize(counts[:, j]) for j in range(3)])
    print("  span: %s .. %s  (%d days)" % (span[0], span[-1], len(span)))
    print("  totals: author opens %d, approvals %d (partial), bot merges %d"
          % (counts[:, 0].sum(), counts[:, 1].sum(), counts[:, 2].sum()))

    # ---- bH2: coupling centrality, merge as hub, vs time-shuffle null ----
    cent = coupling_centrality(traj, max_lag=MAX_LAG)
    order = np.argsort(cent)[::-1]
    print("  coupling centrality: " + ", ".join("%s=%.3f" % (ROLES[i], cent[i]) for i in order))
    top = int(np.argmax(cent))
    least = int(np.argmin(cent))
    rng = np.random.default_rng(SEED)
    null = np.empty(N_SHUFFLE)
    for b in range(N_SHUFFLE):
        sh = np.column_stack([rng.permutation(traj[:, j]) for j in range(3)])
        null[b] = coupling_centrality(sh, max_lag=MAX_LAG)[2]
    p = (np.sum(null >= cent[2]) + 1) / (N_SHUFFLE + 1)
    print("  merge centrality %.3f vs shuffle null mean %.3f  p=%.4f" % (cent[2], null.mean(), p))

    # ---- bH1: lead-lag into the merge ----
    lag_am, prom_am = peak(traj[:, 0], traj[:, 2], MAX_LAG)   # open -> merge
    lag_hm, prom_hm = peak(traj[:, 1], traj[:, 2], MAX_LAG)   # approval -> merge
    print("  peak lag open->merge: %+d d (prom %.3f); approval->merge: %+d d (prom %.3f)"
          % (lag_am, prom_am, lag_hm, prom_hm))

    # ---- bH3: determinism per pair ----
    det_am = crqa(traj[:, 0], traj[:, 2])["det"]
    det_ah = crqa(traj[:, 0], traj[:, 1])["det"]
    det_hm = crqa(traj[:, 1], traj[:, 2])["det"]
    dets = {"approval-merge": det_hm, "author-approval": det_ah, "author-merge": det_am}
    spine = max(dets, key=dets.get)
    print("  determinism: " + ", ".join("%s=%.3f" % (k, v) for k, v in dets.items())
          + "  (highest: %s)" % spine)

    print("=" * 84)
    bH1 = lag_am >= 0 and lag_hm >= 0
    bH2 = top == 2 and p < 0.05
    bH3 = spine == "approval-merge"
    bH4 = least == 0
    print("  bH1 (the conduit fires downstream: upstream->merge lags >= 0): %s"
          % ("SUPPORTED" if bH1 else "REFUTED"))
    print("  bH2 (the bot merge is the behavioral hub, beats shuffle null): %s"
          % ("SUPPORTED" if bH2 else "REFUTED"))
    print("  bH3 (approval-merge is the highest-determinism pair): %s"
          % ("SUPPORTED" if bH3 else "REFUTED"))
    print("  bH4 (the author is the least central role): %s"
          % ("SUPPORTED" if bH4 else "REFUTED"))
    print("=" * 84)
    print("  Reading: whether the machine merger reads behaviorally as a transparent conduit driven by "
          "upstream events, against v9's human gate that was the behavioral hub.")
    print("=" * 84)


if __name__ == "__main__":
    main()

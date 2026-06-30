"""Rank contingent gates by predicted fall-risk and backtest the forecast against 1995-2025 outcomes.

Run:  python org_frontier/studies/constraint_durability/analyze_durability.py
"""

import math
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.studies.constraint_durability.durability import ROWS, OBS_SCORE, predicted_risk  # noqa: E402


def main():
    print("CONSTRAINT DURABILITY — how soon does a contingent gate fall?")
    print("=" * 84)
    print("  the formal class says IF a gate is contingent; durability says HOW SOON it falls.")
    print("  predicted fall-risk: reducible=4 (already), necessary=0 (never), else 3 - durability")
    print("  " + "-" * 80)

    scored = []
    for name, klass, family, dur, obs in ROWS:
        pred = predicted_risk(klass, dur)
        scored.append((pred, name, klass, family, dur, obs))
    # deterministic ranking: fall-risk desc, then name
    scored.sort(key=lambda r: (-r[0], r[1]))
    print("  %-26s %-11s %-10s dur risk  observed" % ("name", "class", "family"))
    for pred, name, klass, family, dur, obs in scored:
        print("  %-26s %-11s %-10s  %d   %d    %s" % (name, klass, family[:10], dur, pred, obs))

    # ---- backtest ----
    pts = [(predicted_risk(k, d), OBS_SCORE[o]) for _n, k, _f, d, o in ROWS]
    n = len(pts)
    tp = sum(1 for p, o in pts if p >= 2 and o >= 2)
    fp = sum(1 for p, o in pts if p >= 2 and o < 2)
    tn = sum(1 for p, o in pts if p < 2 and o < 2)
    fn = sum(1 for p, o in pts if p < 2 and o >= 2)
    acc = (tp + tn) / n
    xs = [p for p, _ in pts]
    ys = [o for _, o in pts]
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in pts)
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    r = cov / (sx * sy)

    print("  " + "-" * 80)
    print("  backtest vs 1995-2025 outcomes (n=%d)" % n)
    print("  predicted-vs-observed correlation r=%.3f" % r)
    print("  binary erode forecast (risk>=2 vs observed>=pressured): accuracy=%.2f  TP=%d FP=%d TN=%d FN=%d"
          % (acc, tp, fp, tn, fn))
    print("  false positives (predicted fall, actually held): %d" % fp)
    print("=" * 84)
    assert fp == 0, "the forecast wrongly predicted a fall for a gate that held"
    assert r > 0.85, "predicted/observed correlation below 0.85"


if __name__ == "__main__":
    main()

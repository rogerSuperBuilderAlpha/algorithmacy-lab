"""Blind inter-coder validation of the durability forecast.

Three coders scored constraint durability blind to outcomes. This computes inter-coder reliability, the
median consensus, and re-runs the backtest with the consensus scores — testing whether the durability->fall
forecast survives when someone other than the outcome-aware author does the coding.

Run:  python org_frontier/studies/constraint_durability/analyze_intercoder.py
"""

import itertools
import math
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.studies.constraint_durability.durability import ROWS, OBS_SCORE, predicted_risk  # noqa: E402
from org_frontier.studies.constraint_durability.intercoder import CODERS, RELIABILITY_FLOOR  # noqa: E402


def _median(xs):
    s = sorted(xs)
    return s[len(s) // 2]


def _pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    sa = math.sqrt(sum((x - ma) ** 2 for x in a))
    sb = math.sqrt(sum((y - mb) ** 2 for y in b))
    return cov / (sa * sb)


def _backtest(durability_of):
    pts = [(predicted_risk(k, durability_of(name, dur)), OBS_SCORE[obs])
           for name, k, _f, dur, obs in ROWS]
    n = len(pts)
    tp = sum(1 for p, o in pts if p >= 2 and o >= 2)
    fp = sum(1 for p, o in pts if p >= 2 and o < 2)
    tn = sum(1 for p, o in pts if p < 2 and o < 2)
    fn = sum(1 for p, o in pts if p < 2 and o >= 2)
    xs = [p for p, _ in pts]
    ys = [o for _, o in pts]
    return _pearson(xs, ys), (tp + tn) / n, tp, fp, tn, fn


def main():
    print("DURABILITY — blind inter-coder validation")
    print("=" * 80)
    items = sorted(CODERS["coder_1"].keys())
    coders = sorted(CODERS.keys())

    # ---- inter-coder reliability: mean pairwise Pearson over the scored items ----
    vecs = {c: [CODERS[c][i] for i in items] for c in coders}
    cors = [_pearson(vecs[a], vecs[b]) for a, b in itertools.combinations(coders, 2)]
    rel = sum(cors) / len(cors)
    print("  coders: %d   items: %d   pairwise r: %s" % (len(coders), len(items),
          " ".join("%.3f" % c for c in cors)))
    print("  GATE inter-coder reliability: mean pairwise r=%.3f (floor %.2f): %s"
          % (rel, RELIABILITY_FLOOR, "PASS" if rel >= RELIABILITY_FLOOR else "FAIL"))
    assert rel >= RELIABILITY_FLOOR, "blind coders did not agree above the floor"

    # ---- consensus (median) and disagreement with the single-coder original ----
    consensus = {i: _median([CODERS[c][i] for c in coders]) for i in items}
    orig = {name: dur for name, _k, _f, dur, _o in ROWS}
    diffs = [i for i in items if orig[i] != consensus[i]]
    print("  consensus differs from the single-coder durability on %d of %d items: %s"
          % (len(diffs), len(items), ", ".join(diffs)))

    # ---- backtests: single-coder baseline vs blind consensus ----
    r_base, acc_base, _, fp_base, _, _ = _backtest(lambda name, dur: dur)
    r_cons, acc_cons, tp, fp, tn, fn = _backtest(lambda name, dur: consensus.get(name, dur))
    print("  " + "-" * 76)
    print("  single-coder baseline : r=%.3f  acc=%.2f  FP=%d" % (r_base, acc_base, fp_base))
    print("  blind-consensus       : r=%.3f  acc=%.2f  TP=%d FP=%d TN=%d FN=%d"
          % (r_cons, acc_cons, tp, fp, tn, fn))
    print("  the forecast survives blind coding: %s" % (r_cons > 0.80))
    print("=" * 80)
    assert r_cons > 0.80, "the forecast did not survive blind coding (consensus r <= 0.80)"


if __name__ == "__main__":
    main()

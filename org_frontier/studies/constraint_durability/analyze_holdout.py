"""Out-of-sample validation: blind-coded durability on twelve held-out intermediaries, fixed predictor.

Run:  python org_frontier/studies/constraint_durability/analyze_holdout.py
"""

import itertools
import math
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.studies.constraint_durability.durability import OBS_SCORE, predicted_risk  # noqa: E402
from org_frontier.studies.constraint_durability.holdout import CODERS, CLASS, OBSERVED  # noqa: E402


def _median(xs):
    return sorted(xs)[len(xs) // 2]


def _pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    sa = math.sqrt(sum((x - ma) ** 2 for x in a))
    sb = math.sqrt(sum((y - mb) ** 2 for y in b))
    return cov / (sa * sb)


def main():
    print("DURABILITY — out-of-sample holdout (blind-coded, fixed predictor)")
    print("=" * 82)
    items = sorted(CODERS["coder_1"].keys())
    coders = sorted(CODERS.keys())

    vecs = {c: [CODERS[c][i] for i in items] for c in coders}
    cors = [_pearson(vecs[a], vecs[b]) for a, b in itertools.combinations(coders, 2)]
    rel = sum(cors) / len(cors)
    print("  held-out items: %d   coders: %d   inter-coder reliability r=%.3f"
          % (len(CLASS), len(coders), rel))

    consensus = {i: _median([CODERS[c][i] for c in coders]) for i in items}

    def pred(name):
        k = CLASS[name]
        if k == "reducible":
            return 4
        if k == "necessary":
            return 0
        return predicted_risk(k, consensus[name])

    names = sorted(CLASS.keys())
    print("  %-26s %-11s dur risk  observed" % ("name", "class"))
    pts = []
    for name in names:
        p = pred(name)
        o = OBS_SCORE[OBSERVED[name]]
        pts.append((p, o))
        d = consensus.get(name, "-")
        print("  %-26s %-11s  %s   %d    %s" % (name, CLASS[name], str(d), p, OBSERVED[name]))

    n = len(pts)
    tp = sum(1 for p, o in pts if p >= 2 and o >= 2)
    fp = sum(1 for p, o in pts if p >= 2 and o < 2)
    tn = sum(1 for p, o in pts if p < 2 and o < 2)
    fn = sum(1 for p, o in pts if p < 2 and o >= 2)
    r = _pearson([p for p, _ in pts], [o for _, o in pts])
    print("  " + "-" * 78)
    print("  OUT-OF-SAMPLE backtest (n=%d): r=%.3f  acc=%.2f  TP=%d FP=%d TN=%d FN=%d"
          % (n, r, (tp + tn) / n, tp, fp, tn, fn))
    print("  in-sample r=0.925 -> blind in-sample r=0.859 -> out-of-sample r=%.3f (graceful degradation)" % r)
    print("  false positives out-of-sample: %d" % fp)
    print("=" * 82)
    assert fp == 0, "out-of-sample forecast wrongly predicted a fall for a gate that held"
    assert r > 0.60, "out-of-sample correlation collapsed below 0.60"


if __name__ == "__main__":
    main()

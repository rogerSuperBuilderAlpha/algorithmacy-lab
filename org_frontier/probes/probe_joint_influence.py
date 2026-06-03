"""Probe 13 — context-sensitive (joint) influence vs isolated influence.

Probe 12 predicted core membership from each node's influence averaged per-function in isolation
(AUC 0.695 on the full family). The gap to the controlled 0.89 was attributed to higher-order joint
effects. Test a context-sensitive influence measure that captures them:

  total_influence(X) = fraction of the 8 full system states in which flipping X changes the NEXT
  state of ANY node (evaluated in the real joint context, not per-function-averaged).

H13: total_influence predicts core membership better than the isolated per-function influence — its
AUC is higher, narrowing the gap.

Same family sample as Probe 12 (seed 11, N=800) for a paired comparison. Nodes 0,1,2 = A,B,C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_joint_influence [N] [seed]
"""

import csv
import os
import sys

import numpy as np

from .lib import major_complex

LABELS = ("A", "B", "C")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _f(t):
    return lambda a, b: t[(a & 1) | ((b & 1) << 1)]


def _sens(t, bit):
    return sum(t[c] != t[c ^ (1 << bit)] for c in range(4)) / 4.0


def _auc(pos, neg):
    if not pos or not neg:
        return float("nan")
    return (sum(p > n for p in pos for n in neg) + 0.5 * sum(p == n for p in pos for n in neg)) / (len(pos) * len(neg))


def main(N=800, seed=11):
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(N):
        t = [tuple(int(b) for b in rng.integers(0, 2, 4)) for _ in range(3)]
        f0, f1, f2 = _f(t[0]), _f(t[1]), _f(t[2])

        def succ(s):
            a, b, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
            return (f0(b, c), f1(a, c), f2(a, b))   # node0 reads(1,2); node1 reads(0,2); node2 reads(0,1)

        # isolated influence (Probe 12 measure)
        iso = {"A": np.mean([_sens(t[1], 0), _sens(t[2], 0)]),
               "B": np.mean([_sens(t[0], 0), _sens(t[2], 1)]),
               "C": np.mean([_sens(t[0], 1), _sens(t[1], 1)])}
        reads = {"A": any(_sens(t[0], b) for b in (0, 1)),
                 "B": any(_sens(t[1], b) for b in (0, 1)),
                 "C": any(_sens(t[2], b) for b in (0, 1))}
        # context-sensitive total influence: flip node X in each of 8 states, does successor change?
        tot = {}
        for X, bit in (("A", 0), ("B", 1), ("C", 2)):
            cnt = sum(succ(s) != succ(s ^ (1 << bit)) for s in range(8))
            tot[X] = cnt / 8.0

        rules = [lambda x: f0(x[1], x[2]), lambda x: f1(x[0], x[2]), lambda x: f2(x[0], x[1])]
        core, _ = major_complex(rules, LABELS)
        core = core or ()
        for X in ("A", "B", "C"):
            bidir = bool(reads[X] and iso[X] > 0)
            rows.append({"node": X, "bidirectional": bidir, "iso_influence": round(iso[X], 3),
                         "total_influence": round(tot[X], 3), "in_core": X in core})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "joint_influence.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    bidir = [r for r in rows if r["bidirectional"]]
    iso_auc = _auc([r["iso_influence"] for r in bidir if r["in_core"]],
                   [r["iso_influence"] for r in bidir if not r["in_core"]])
    tot_auc = _auc([r["total_influence"] for r in bidir if r["in_core"]],
                   [r["total_influence"] for r in bidir if not r["in_core"]])
    print(f"PROBE 13 — joint vs isolated influence (N={N}, {len(bidir)} bidirectional node-obs)")
    print("=" * 78)
    print(f"  AUC, isolated per-function influence (Probe 12) : {iso_auc:.3f}")
    print(f"  AUC, context-sensitive total influence          : {tot_auc:.3f}")
    print(f"  improvement                                     : {tot_auc - iso_auc:+.3f}")
    print("  P(in core) by total_influence:")
    for lv in sorted({r["total_influence"] for r in bidir}):
        grp = [r for r in bidir if r["total_influence"] == lv]
        print(f"    {lv:.3f}  n={len(grp):>4}  {100*sum(r['in_core'] for r in grp)/len(grp):5.1f}%")
    print("=" * 78)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    main(N, seed)

"""Probe 12 — validate the two-condition account on the full 3-node family.

The two conditions (bidirectional coupling + pivotality) were found in mediated structures. This
tests them on the complete model family: every node's update is an arbitrary Boolean function of the
other two (node i reads the other two), so a wiring = (f0, f1, f2), 16^3 = 4096 total. Sample N and,
for each node X, compute:
  - bidirectional: X reads someone (fX non-constant) AND someone reads X (X influences another fn).
  - out_influence(X): mean Boolean sensitivity of the other nodes' updates to X.
and whether X is in the major complex.

H12: across arbitrary wirings, (a) a non-bidirectional node is essentially never in the core, and
(b) among bidirectional nodes P(in core) rises with influence.

Labels A,B,C for nodes 0,1,2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_family_validation [N] [seed]
"""

import csv
import os
import sys

import numpy as np

from .lib import major_complex

LABELS = ("A", "B", "C")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _f(table):
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def _sens(table, bit):
    return sum(table[c] != table[c ^ (1 << bit)] for c in range(4)) / 4.0


def main(N=800, seed=11):
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(N):
        t = [tuple(int(b) for b in rng.integers(0, 2, 4)) for _ in range(3)]  # f0,f1,f2
        f0, f1, f2 = _f(t[0]), _f(t[1]), _f(t[2])
        # node0 reads (1,2); node1 reads (0,2); node2 reads (0,1)
        rules = [lambda x: f0(x[1], x[2]), lambda x: f1(x[0], x[2]), lambda x: f2(x[0], x[1])]
        core, _ = major_complex(rules, LABELS)
        core = core or ()
        # influence of each node on the others (which input position it occupies in each fn)
        out_infl = {
            "A": np.mean([_sens(t[1], 0), _sens(t[2], 0)]),   # A is input0 of f1 and f2
            "B": np.mean([_sens(t[0], 0), _sens(t[2], 1)]),   # B is input0 of f0, input1 of f2
            "C": np.mean([_sens(t[0], 1), _sens(t[1], 1)]),   # C is input1 of f0 and f1
        }
        reads_someone = {"A": any(_sens(t[0], b) for b in (0, 1)),
                         "B": any(_sens(t[1], b) for b in (0, 1)),
                         "C": any(_sens(t[2], b) for b in (0, 1))}
        for X in ("A", "B", "C"):
            bidir = bool(reads_someone[X] and out_infl[X] > 0)
            rows.append({"node": X, "bidirectional": bidir,
                         "out_influence": round(float(out_infl[X]), 3),
                         "in_core": X in core})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "family_validation.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    nonbidir = [r for r in rows if not r["bidirectional"]]
    bidir = [r for r in rows if r["bidirectional"]]
    nb_in = sum(r["in_core"] for r in nonbidir)
    print(f"PROBE 12 — two-condition account on the 3-node family (N={N}, {len(rows)} node-obs)")
    print("=" * 78)
    print(f"  non-bidirectional nodes in core : {nb_in}/{len(nonbidir)} "
          f"({100*nb_in/max(len(nonbidir),1):.1f}%) — coupling is necessary")
    print("  among bidirectional nodes, P(in core) by influence:")
    for lv in sorted({r["out_influence"] for r in bidir}):
        grp = [r for r in bidir if r["out_influence"] == lv]
        print(f"    influence {lv:.3f}   n={len(grp):>4}   P(in core)={100*sum(r['in_core'] for r in grp)/len(grp):5.1f}%")
    pos = [r["out_influence"] for r in bidir if r["in_core"]]
    neg = [r["out_influence"] for r in bidir if not r["in_core"]]
    if pos and neg:
        auc = (sum(p > n for p in pos for n in neg) + 0.5 * sum(p == n for p in pos for n in neg)) / (len(pos) * len(neg))
        print(f"  rank-AUC (influence predicts in-core, among bidirectional): {auc:.3f}")
    print("=" * 78)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    main(N, seed)

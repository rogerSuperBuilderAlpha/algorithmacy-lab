"""Scaling the triadic rate: sample strict-mediation families at n = 5 (and optionally n = 4).

Completes the trend 9.4% (n=3, full census) -> ~2.3% (n=4, sample) -> ? (n=5). A strict-mediation
n-party form: one mediator S reads all (n-1) outer parties via a random Boolean function; each outer
party reads S via a random function. We sample, compute exact IIT-4.0 max Φ over reachable states,
and report the triadic rate and the P(triadic | S reads all outer) conditional.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.scaling [n] [n_sample] [seed]
"""

import csv
import os
import sys
import time

import numpy as np

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from .run import _rand_table, _fn

_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def sample_form(n, rng):
    """One strict-mediation n-party form. Node 0=W, 1=S, 2..n-1 = counterparts.
    S (index 1) reads all outer indices; each outer party reads S only."""
    outer = [0] + list(range(2, n))          # W and the counterparts
    ts = _rand_table(rng, len(outer))         # S reads all outer parties
    rules = [None] * n
    rules[1] = _fn(ts, tuple(outer))          # S'
    for i in outer:
        ti = _rand_table(rng, 1)
        rules[i] = _fn(ti, (1,))              # party' = f(S)
    return rules


def main(n=5, n_sample=400, seed=7):
    rng = np.random.default_rng(seed)
    labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)])
    rows = []
    start = time.time()
    print(f"SCALING — strict-mediation n={n} family (n_sample={n_sample}, seed={seed})")
    for k in range(n_sample):
        rules = sample_form(n, rng)
        v = classify_rules(rules, labels=labels)
        cm = cm_from_rules(rules)
        s_reads_all = bool(all(cm[i, 1] for i in [0] + list(range(2, n))))
        rows.append({"idx": k, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "s_reads_all": s_reads_all, "n_states": v.n_states_evaluated})
        if (k + 1) % 50 == 0:
            print(f"  {k+1}/{n_sample}  ({time.time()-start:.0f}s)")

    path = os.path.join(_RESULTS, f"population_n{n}.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {path}")

    tri = [r for r in rows if r["structure"] == "triadic"]
    reads_all = [r for r in rows if r["s_reads_all"]]
    reads_all_tri = [r for r in reads_all if r["structure"] == "triadic"]
    print("=" * 80)
    print(f"  n={n}: triadic {len(tri)}/{len(rows)} ({100*len(tri)/len(rows):.1f}%)")
    if reads_all:
        print(f"  P(triadic | S reads all outer) = {100*len(reads_all_tri)/len(reads_all):.1f}% "
              f"({len(reads_all_tri)}/{len(reads_all)})")
    print(f"  trend: n=3 9.4% (census) -> n=4 ~2.3% (sample) -> n={n} {100*len(tri)/len(rows):.1f}% (sample)")
    print("=" * 80)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    n_sample = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    main(n, n_sample, seed)

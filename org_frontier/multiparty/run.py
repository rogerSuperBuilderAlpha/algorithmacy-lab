"""Multi-party experiment: named four-party forms + a sampled strict-mediation n=4 population.

Two parts:
  1. Named forms (forms.py): does adding a counterpart keep the form triadic? Compute each.
  2. Population scaling: sample the strict-mediation n=4 family (mediator S reads all three outer
     parties via a random Boolean function; each outer party reads S via a random function) and
     report P(triadic), compared to the n=3 strict-mediation result (9.4%). Tests whether the
     n=3 rule (mediator must read all sources, parties must stay live to it) generalizes, and
     whether irreducibility gets rarer as parties are added.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.run [n_sample] [seed]
"""

import csv
import os
import sys
import time

import numpy as np

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from . import forms as mp

_HERE = os.path.dirname(__file__)
_RESULTS = os.path.join(_HERE, "results")
LABELS4 = ("W", "S", "C1", "C2")


def run_named():
    print("=" * 92)
    print("NAMED FOUR-PARTY FORMS")
    print("=" * 92)
    rows = []
    for f in mp.FORMS:
        v = classify_rules(f.rules, labels=f.labels)
        check = "ok" if (f.expected == "?" or v.structure == f.expected) else "MISMATCH"
        flag = "" if check == "ok" else "  <-- " + check
        print(f"  {f.key:<28} {v.structure:<8} {v.competence:<12} maxΦ={v.max_phi:.4f} "
              f"states={v.n_states_evaluated:<3} expected={f.expected}{flag}")
        rows.append({"key": f.key, "structure": v.structure, "competence": v.competence,
                     "max_phi": f"{v.max_phi:.6f}", "n_states": v.n_states_evaluated,
                     "expected": f.expected})
    _write("named.csv", rows)
    return rows


def _rand_table(rng, n_inputs):
    """A random Boolean truth table over n_inputs inputs, as a tuple of 2^n_inputs bits."""
    return tuple(int(b) for b in rng.integers(0, 2, size=2 ** n_inputs))


def _fn(table, idx_inputs):
    """Build a function of the state tuple x reading the given input indices (little-endian)."""
    def f(x, table=table, idx_inputs=idx_inputs):
        key = 0
        for k, i in enumerate(idx_inputs):
            key |= (x[i] & 1) << k
        return table[key]
    return f


def sample_population(n_sample, seed):
    """Sample strict-mediation n=4 forms: S reads (W,C1,C2); each outer reads S only."""
    rng = np.random.default_rng(seed)
    print("\n" + "=" * 92)
    print(f"POPULATION SCALING — sampled strict-mediation n=4 family (n_sample={n_sample}, seed={seed})")
    print("=" * 92)
    rows = []
    start = time.time()
    for k in range(n_sample):
        ts = _rand_table(rng, 3)            # S reads W,C1,C2
        tw = _rand_table(rng, 1)            # W reads S
        t1 = _rand_table(rng, 1)            # C1 reads S
        t2 = _rand_table(rng, 1)            # C2 reads S
        rules = [
            _fn(tw, (1,)),                  # W' = f(S)
            _fn(ts, (0, 2, 3)),             # S' = f(W, C1, C2)
            _fn(t1, (1,)),                  # C1' = f(S)
            _fn(t2, (1,)),                  # C2' = f(S)
        ]
        v = classify_rules(rules, labels=LABELS4)
        cm = cm_from_rules(rules)
        s_reads_all = bool(cm[0, 1] and cm[2, 1] and cm[3, 1])
        rows.append({"idx": k, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "s_reads_all_three": s_reads_all, "n_states": v.n_states_evaluated})
        if (k + 1) % 300 == 0:
            print(f"  {k+1}/{n_sample}  ({time.time()-start:.0f}s)")
    _write("population_n4.csv", rows)
    _report_population(rows)
    return rows


def _report_population(rows):
    n = len(rows)
    tri = [r for r in rows if r["structure"] == "triadic"]
    reads_all = [r for r in rows if r["s_reads_all_three"]]
    reads_all_tri = [r for r in reads_all if r["structure"] == "triadic"]
    not_all = [r for r in rows if not r["s_reads_all_three"]]
    not_all_tri = [r for r in not_all if r["structure"] == "triadic"]

    def pct(a, b):
        return f"{100.0*len(a)/len(b):.1f}%" if b else "n/a"

    print("\n" + "-" * 92)
    print("POPULATION RESULT (n=4) — and the n=3 comparison")
    print(f"  sampled forms                          : {n}")
    print(f"  triadic (Φ > 0)                        : {len(tri)}  ({pct(tri, rows)})   "
          f"[n=3 strict-mediation was 9.4%]")
    print(f"  P(triadic | S reads all three outer)   : {pct(reads_all_tri, reads_all)} "
          f"({len(reads_all_tri)}/{len(reads_all)})")
    print(f"  P(triadic | S does NOT read all three) : {pct(not_all_tri, not_all)} "
          f"({len(not_all_tri)}/{len(not_all)})")
    print(f"  -> the mediator reading ALL parties is the n=4 analogue of 'reads both' — necessary,")
    print(f"     and irreducibility is rarer than at n=3 (harder to keep more parties jointly live).")
    print("-" * 92)


def _write(name, rows):
    os.makedirs(_RESULTS, exist_ok=True)
    path = os.path.join(_RESULTS, name)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path}")


def main(n_sample=1500, seed=7):
    run_named()
    sample_population(n_sample, seed)


if __name__ == "__main__":
    n_sample = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    main(n_sample, seed)

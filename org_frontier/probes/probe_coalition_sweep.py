"""Probe 8 — coalition displacement as a population rate.

Probe 1 found (on three forms) that a counterpart coalition ejects the worker from the core. This
makes it a rate. Fix W' = S and S' = W ∧ C1 ∧ C2 (all-required pool). Sweep every Boolean coupling
of the two counterparts: C1' = f1(S, C2), C2' = f2(S, C1) — 16 × 16 = 256 forms. A "coalition" is
present when C1 reads C2 or C2 reads C1. Measure how often the worker is in the major complex.

H8: the worker is in the core far less often when a coalition channel is present.

Nodes: 0=W, 1=S, 2=C1, 3=C2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_coalition_sweep
"""

import csv
import itertools
import os

from .lib import major_complex

LABELS = ("W", "S", "C1", "C2")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _fn2(table):
    # inputs (a, b) -> table[a | b<<1]
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def _depends_on_second(table):
    # does f(a,b) depend on b? compare b=0 vs b=1 across a.
    return any(table[a] != table[a | 2] for a in (0, 1))


def main():
    tables = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]
    rows = []
    for t1, t2 in itertools.product(tables, tables):
        f1, f2 = _fn2(t1), _fn2(t2)
        # C1' = f1(S, C2);  C2' = f2(S, C1)
        rules = [lambda x: x[1],
                 lambda x: x[0] & x[2] & x[3],
                 lambda x, f1=f1: f1(x[1], x[3]),
                 lambda x, f2=f2: f2(x[1], x[2])]
        core, phi = major_complex(rules, LABELS)
        w_in = core is not None and "W" in core
        coalition = _depends_on_second(t1) or _depends_on_second(t2)  # C1 reads C2 or C2 reads C1
        rows.append({"w_in_core": w_in, "coalition": coalition,
                     "core_size": len(core) if core else 0, "phi": f"{phi:.4f}"})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "coalition_sweep.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    coal = [r for r in rows if r["coalition"]]
    nocoal = [r for r in rows if not r["coalition"]]

    def rate(rs):
        return f"{100*sum(r['w_in_core'] for r in rs)/len(rs):.1f}%" if rs else "n/a"

    print("PROBE 8 — coalition displacement as a rate (256 forms)")
    print("=" * 78)
    print(f"  worker in core, overall                 : {rate(rows)}")
    print(f"  worker in core, coalition PRESENT       : {rate(coal)}  (n={len(coal)})")
    print(f"  worker in core, coalition ABSENT        : {rate(nocoal)}  (n={len(nocoal)})")
    print("=" * 78)


if __name__ == "__main__":
    main()

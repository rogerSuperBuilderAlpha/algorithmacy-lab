"""Probe 9 — inference displacement as a population rate.

Probe 4 showed (on named forms) that a blended internal model M can take the counterpart C's place
in the core. This rates it. Fix S' = W ∧ C and C' = S. Sweep how the worker uses signal and model
(W' = f1(S, M), 16 functions) and how the model updates from the determination (M' = f2(S), 4
functions): 64 forms. Record whether C and M are each in the major complex.

H9: M and C trade off — C is in the core less often when M is, i.e. the inferred model displaces the
counterpart rather than adding to it.

Nodes: 0=W, 1=S, 2=C, 3=M.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_inference_sweep
"""

import csv
import itertools
import os

from .lib import major_complex

LABELS = ("W", "S", "C", "M")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _fn2(t):   # inputs (a,b) -> t[a | b<<1]
    return lambda a, b: t[(a & 1) | ((b & 1) << 1)]


def _fn1(t):   # input a -> t[a]
    return lambda a: t[a & 1]


def main():
    t2 = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]
    t1 = [(o0, o1) for o0 in (0, 1) for o1 in (0, 1)]
    rows = []
    for wt, mt in itertools.product(t2, t1):
        fW, fM = _fn2(wt), _fn1(mt)
        rules = [lambda x, fW=fW: fW(x[1], x[3]),     # W' = f1(S, M)
                 lambda x: x[0] & x[2],                # S' = W AND C
                 lambda x: x[1],                       # C' = S
                 lambda x, fM=fM: fM(x[1])]            # M' = f2(S)
        core, phi = major_complex(rules, LABELS)
        rows.append({"C_in": bool(core and "C" in core),
                     "M_in": bool(core and "M" in core),
                     "core_size": len(core) if core else 0})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "inference_sweep.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    m_in = [r for r in rows if r["M_in"]]
    m_out = [r for r in rows if not r["M_in"]]

    def c_rate(rs):
        return f"{100*sum(r['C_in'] for r in rs)/len(rs):.1f}%" if rs else "n/a"

    print("PROBE 9 — inference displacement as a rate (64 forms)")
    print("=" * 78)
    print(f"  P(C in core), overall          : {c_rate(rows)}")
    print(f"  P(C in core | M in core)       : {c_rate(m_in)}  (n={len(m_in)})")
    print(f"  P(C in core | M NOT in core)   : {c_rate(m_out)}  (n={len(m_out)})")
    both = sum(r["C_in"] and r["M_in"] for r in rows)
    print(f"  forms where C and M coexist in core: {both}")
    print("=" * 78)


if __name__ == "__main__":
    main()

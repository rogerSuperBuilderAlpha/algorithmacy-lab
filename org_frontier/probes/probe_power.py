"""Probe 16 — power asymmetry: does balanced influence make the triad?

Operationalize "the system commits determinations neither party controls" as a continuous knob: the
ASYMMETRY of the two parties' influence on the determination. Over all 16 two-input determinations
S' = f(W, C) (parties track S), compute influence_W and influence_C (Boolean sensitivity), the
asymmetry |inf_W - inf_C|, and the verdict.

H16: triadic forms cluster at LOW asymmetry (balanced influence — neither controls); as one party's
influence dominates (high asymmetry, up to unilateral control), the form goes dyadic.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_power
"""

import csv
import os

from .lib import verdict

LABELS = ("W", "S", "C")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _f(t):
    return lambda a, b: t[(a & 1) | ((b & 1) << 1)]


def _sens(t, bit):
    return sum(t[c] != t[c ^ (1 << bit)] for c in range(4)) / 4.0


def main():
    rows = []
    for m in range(16):
        t = tuple((m >> k) & 1 for k in range(4))   # f(W,C): index W | C<<1
        s = _f(t)
        rules = [lambda x: x[1], lambda x, s=s: s(x[0], x[2]), lambda x: x[1]]
        v = verdict(rules, LABELS)
        inf_w, inf_c = _sens(t, 0), _sens(t, 1)
        rows.append({"fn": m, "inf_W": inf_w, "inf_C": inf_c,
                     "asymmetry": round(abs(inf_w - inf_c), 3),
                     "structure": v.structure, "phi": round(v.max_phi, 3)})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "power.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    print("PROBE 16 — power asymmetry vs the triad (16 determinations)")
    print("=" * 72)
    print("  asymmetry   n    triadic   mean Φ")
    for lv in sorted({r["asymmetry"] for r in rows}):
        grp = [r for r in rows if r["asymmetry"] == lv]
        tri = sum(r["structure"] == "triadic" for r in grp)
        mphi = sum(r["phi"] for r in grp) / len(grp)
        print(f"   {lv:.2f}       {len(grp):>2}    {tri}/{len(grp)}      {mphi:.3f}")
    tri = [r for r in rows if r["structure"] == "triadic"]
    dya = [r for r in rows if r["structure"] == "dyadic"]
    ma = lambda rs: sum(r["asymmetry"] for r in rs) / len(rs) if rs else float("nan")
    print("=" * 72)
    print(f"  mean asymmetry of triadic forms: {ma(tri):.3f}  (n={len(tri)})")
    print(f"  mean asymmetry of dyadic  forms: {ma(dya):.3f}  (n={len(dya)})")
    print("=" * 72)


if __name__ == "__main__":
    main()

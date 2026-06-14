"""Probe Q95 (H1-H4) — does composing two triads unify, fragment, or add?

Composes two read-recipient triads through a shared node (recipient of triad 1 = sender of triad 2) and
reads the verdict, the major complex, and the disjoint-complex tiling, against a single triad and two
disjoint triads.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q95_composition_of_triads.probe_composition_of_triads
"""

import csv
import os

from org_frontier.questions.q95_composition_of_triads import forms as F


def main():
    print("PROBE Q95 (H1-H4) — composition of two read-recipient triads")
    print("=" * 80)
    rows = {}
    for name, (rules, lab) in [("single_triad", F.single_triad()),
                               ("two_disjoint_triads", F.two_disjoint_triads()),
                               ("composed", F.composed())]:
        st, sphi, core, cphi, tiling = F.summary(rules, lab)
        rows[name] = {"structure": st, "sys_phi": sphi, "core": core, "core_phi": cphi, "tiling": tiling}
        print(f"  {name:<20} {st:<8} sysΦ={sphi:<5} major={core} (φ={cphi})")
        print(f"  {'':20} complexes: {tiling}")

    comp = rows["composed"]
    core = set(comp["core"])
    spans_both = bool(core & {"E1", "M1"}) and bool(core & {"M2", "R2"})
    h1 = comp["structure"] == "triadic"
    h2 = len(comp["tiling"]) == 1 and spans_both
    h3 = comp["core_phi"] > 2.0
    h4 = "S" in core

    print("=" * 80)
    print(f"  H1 the composition is triadic:                              {h1} (sysΦ={comp['sys_phi']})")
    print(f"  H2 it unifies into one spanning complex (both triads):      {h2} (n_complexes={len(comp['tiling'])})")
    print(f"  H3 composed core Φ exceeds a single triad (>2.0):           {h3} ({comp['core_phi']})")
    print(f"  H4 the shared bridge node S is in the core:                 {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "composition_of_triads.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["config", "structure", "sys_phi", "major_complex", "core_phi", "n_complexes"])
        for name, r in rows.items():
            w.writerow([name, r["structure"], r["sys_phi"], "|".join(r["core"]), r["core_phi"], len(r["tiling"])])


if __name__ == "__main__":
    main()

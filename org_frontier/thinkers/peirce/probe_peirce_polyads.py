"""Probe — Peirce H5: polyadic reducibility (the positive clause of the reduction thesis).

Question.  Peirce (CP 1.363): tetrads and higher are compounds of triads — "A sells C to B for the price D"
           resolves into two triads sharing a hypostatic term. Among four-element forms built from two-input
           rules only, does any contain an irreducible distinction of adicity 4?
Hypothesis. H5 (Peirce): at least one does (triads compose upward), while no one-input four-element form
           reaches adicity 3 (H1).
Method.    Random sample (default 60, seed 0) of four-element forms, each node reading exactly two others with
           a gate from {AND, OR, XOR, NAND, NOR, XNOR}; genuine_adicity, whole Φ, and core for each.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_polyads [n_forms] [seed]
"""

import sys

from org_frontier.thinkers.peirce import forms as F


def main():
    n_forms = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    print("Peirce H5 — polyadic reducibility: %d two-input four-element forms (seed %d)" % (n_forms, seed))
    control = F.run_control()
    recs = []
    for name, form, spec in F.two_input_sample(n_forms, seed):
        recs.append(F.evaluate(name, form, spec))
    counts = {}
    for r in recs:
        counts[r["genuine_adicity"]] = counts.get(r["genuine_adicity"], 0) + 1
    n4 = counts.get(4, 0)
    n3 = counts.get(3, 0)
    print("  adicity counts=%s  adicity-4 forms=%d/%d  adicity>=3 forms=%d/%d"
          % (dict(sorted(counts.items())), n4, len(recs), n4 + n3, len(recs)))
    for r in recs:
        if r["genuine_adicity"] == 4:
            print("    adicity-4 exemplar: %s  %s" % (r["spec"], r["max_distinction"]))
            break
    status = "CONFIRMED" if n4 > 0 else "REFUTED"
    print("H5 (two-input rules compose into an adicity-4 fact): %s" % status)
    out = "probe_peirce_polyads" if (n_forms, seed) == (60, 0) else "probe_peirce_polyads_n%d_s%d" % (n_forms, seed)
    F.save(out, {"control": control, "forms": recs, "adicity_counts": counts,
                 "n_forms": n_forms, "seed": seed, "H5": status})


if __name__ == "__main__":
    main()

"""Probe Q110 (H1-H4) — is the dyad/triad boundary symmetric?

Compares the fragility-margin distribution (edits to break a triad) with the construction-distance
distribution (edits to build one) over the 256-form family.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q110_reversibility.probe_reversibility
"""

import csv
import os
from collections import Counter

from org_frontier.questions.q110_reversibility import forms as F


def main():
    print("PROBE Q110 (H1-H4) — reversibility of the dyad/triad boundary")
    print("=" * 74)
    frag, cons = F.both_distributions()
    frag_hist = dict(sorted(Counter(frag).items()))
    cons_hist = dict(sorted(Counter(cons).items()))
    mfrag = sum(frag) / len(frag)
    mcons = sum(cons) / len(cons)
    print(f"  fragility margin (break a triad), {len(frag)} triadic forms: {frag_hist} mean={mfrag:.2f}")
    print(f"  construction distance (build a triad), {len(cons)} dyadic forms: {cons_hist} mean={mcons:.2f}")

    h1 = all(d == 1 for d in frag)
    h2 = max(cons) > 1
    h3 = frag_hist != cons_hist
    h4 = mcons > mfrag
    print("=" * 74)
    print(f"  H1 every triad is one edit from a dyad (fragility all 1):   {h1}")
    print(f"  H2 not every dyad is one edit from a triad:                 {h2} (max {max(cons)})")
    print(f"  H3 the boundary is asymmetric (distributions differ):       {h3}")
    print(f"  H4 building costs more edits than breaking (mean):          {h4} ({mcons:.2f} > {mfrag:.2f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "reversibility.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["direction", "distance", "n_forms"])
        for d, n in frag_hist.items():
            w.writerow(["break_triad_fragility", d, n])
        for d, n in cons_hist.items():
            w.writerow(["build_triad_construction", d, n])


if __name__ == "__main__":
    main()

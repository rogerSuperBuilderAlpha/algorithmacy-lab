"""Probe Q105 (H1-H4) — the minimal edit that builds a triad from a dyad.

Computes the construction distance (minimal Hamming distance to a triadic form) for every dyadic form in
the 256-form family, and reads where the building edits sit.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q105_construction_distance.probe_construction_distance
"""

import csv
import os
from collections import Counter

from org_frontier.questions.q105_construction_distance import forms as F


def main():
    print("PROBE Q105 (H1-H4) — construction distance from dyadic to triadic")
    print("=" * 74)
    dyadic, triadic = F.classify_family()
    dists = {}
    one_step_mediator = 0
    one_step_total = 0
    for bits in dyadic:
        d, steps = F.construction_distance(bits, triadic)
        dists[bits] = (d, steps)
        if d == 1:
            one_step_total += 1
            if steps & set(F.MEDIATOR_BITS):
                one_step_mediator += 1

    hist = Counter(d for d, _ in dists.values())
    bb = F.broadcast_bits()
    bd, bsteps = dists[bb]
    within2 = sum(1 for d, _ in dists.values() if d <= 2) / len(dyadic)
    med_frac = one_step_mediator / max(one_step_total, 1)

    print(f"  {len(dyadic)} dyadic forms | distance histogram: {dict(sorted(hist.items()))}")
    print(f"  broadcast: construction distance {bd} via bits {sorted(bsteps)} "
          f"(mediator bits = {sorted(F.MEDIATOR_BITS)})")
    print(f"  within distance 2: {within2:.2f} | distance-1 builds at a mediator bit: {med_frac:.2f}")

    h1 = bd == 1 and bool(bsteps & set(F.MEDIATOR_BITS))
    h2 = within2 > 0.5
    h3 = len(hist) >= 2
    h4 = med_frac > 0.5
    print("=" * 74)
    print(f"  H1 the broadcast is one mediator-bit edit from triadic:    {h1}")
    print(f"  H2 most dyadic forms are within construction distance 2:   {h2} ({within2:.2f})")
    print(f"  H3 the construction distance varies across dyadic forms:   {h3} ({dict(sorted(hist.items()))})")
    print(f"  H4 distance-1 builds happen at a mediator bit (>0.5):      {h4} ({med_frac:.2f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "construction_distance.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["construction_distance", "n_dyadic_forms"])
        for d in sorted(hist):
            w.writerow([d, hist[d]])


if __name__ == "__main__":
    main()

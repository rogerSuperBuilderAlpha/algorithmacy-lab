"""Probe Q108 (H1-H4) — which party steers the verdict, and how finely?

Varies each party's function of the read-recipient triad and counts the triadic settings, to locate the
control nodes and their granularity.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q108_controllability.probe_controllability
"""

import csv
import os

from org_frontier.questions.q108_controllability import forms as F


def main():
    print("PROBE Q108 (H1-H4) — controllability of the verdict from a single party")
    print("=" * 74)
    counts = {}
    for party, pos in F.PARTY_BITS.items():
        sweep = F.control_sweep(F.READ_RECIPIENT, pos)
        tri = sum(1 for _, t in sweep if t)
        counts[party] = (tri, len(sweep))
        both = 0 < tri < len(sweep)
        print(f"  {party:<12} {tri}/{len(sweep)} settings triadic | control node (both verdicts): {both}")

    def both(p):
        t, n = counts[p]
        return 0 < t < n

    h1 = both("mediator")
    h2 = both("worker") and both("counterpart")
    h3 = counts["mediator"][0] > counts["worker"][0] and counts["mediator"][0] > counts["counterpart"][0]
    h4 = counts["worker"][0] == 1 and counts["counterpart"][0] == 1
    print("=" * 74)
    print(f"  H1 the mediator is a control node:                          {h1}")
    print(f"  H2 each outer party is a control node:                      {h2}")
    print(f"  H3 the mediator is the dominant control node (most triadic):{h3} "
          f"(med {counts['mediator'][0]} vs W {counts['worker'][0]}, C {counts['counterpart'][0]})")
    print(f"  H4 the outer parties are knife-edge (exactly one triadic):  {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "controllability.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["party", "triadic_settings", "total_settings"])
        for party, (tri, n) in counts.items():
            w.writerow([party, tri, n])


if __name__ == "__main__":
    main()

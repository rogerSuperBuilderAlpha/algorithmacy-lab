"""Probe Q63-H2 — substitutable recipients collapse the triad.

Question: does mass outreach to interchangeable recipients factor even when personalized on the surface?
Hypothesis (H2): all_required (M'=E&R1&R2) is triadic; substitutable (M'=E&(R1|R2)) is dyadic.
Method: classify both n=4 forms with exact IIT-4.0 Φ over the MIP. Instrument control as in H1.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q63_outreach_coordination.probe_substitutable
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.questions.q63_outreach_coordination.forms import (
    LABELS4, ALL_REQUIRED, SUBSTITUTABLE, check_controls,
)


def main():
    print("PROBE Q63-H2 — substitutable recipients")
    print("=" * 64)
    print(check_controls(verdict))
    res, rows = {}, []
    for name, rules in (("all_required", ALL_REQUIRED), ("substitutable", SUBSTITUTABLE)):
        v = verdict(rules, LABELS4)
        res[name] = v
        print(f"  {name:<16} {v.structure:<8} Φ_MIP={v.max_phi:.4f}")
        rows.append((name, v.structure, f"{v.max_phi:.6f}"))
    confirmed = res["all_required"].structure == "triadic" and res["substitutable"].structure == "dyadic"
    print("=" * 64)
    print(f"  all_required triadic: {res['all_required'].structure == 'triadic'} | "
          f"substitutable dyadic: {res['substitutable'].structure == 'dyadic'}")
    print(f"  H2 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")

    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "substitutable.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "structure", "max_phi"])
        w.writerows(rows)


if __name__ == "__main__":
    main()

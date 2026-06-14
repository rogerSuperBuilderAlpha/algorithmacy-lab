"""Probe Q114 (H1-H4) — does a principal extract rent or create value?

Compares the Shapley values of the base triad with a triad joined by a bidirectionally-coupled principal,
and with a monitor-only principal, to ask whether the principal's value comes at the parties' expense.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q114_principal_rent.probe_principal_rent
"""

import csv
import os

from org_frontier.questions.q114_principal_rent import forms as F


def main():
    print("PROBE Q114 (H1-H4) — the principal's value capture")
    print("=" * 74)
    base = F.base_triad_shapley()
    bidir, phi_b = F.shapley_for(F.BIDIRECTIONAL)
    mon, phi_m = F.shapley_for(F.MONITOR_ONLY)
    print(f"  base triad (no principal): {base}  Φ=2.0")
    print(f"  bidirectional principal:   {bidir}  Φ={phi_b}")
    print(f"  monitor-only principal:    {mon}  Φ={phi_m}")

    parties_rise = all(bidir[p] >= base[p] - 1e-9 for p in ("E", "M", "R"))
    h1 = bidir["P"] > 0
    h2 = mon["P"] <= 0
    h3 = parties_rise
    h4 = phi_b > 2.0
    print("=" * 74)
    print(f"  H1 a bidirectional principal captures positive value:      {h1} ({bidir['P']:+.3f})")
    print(f"  H2 a monitor-only principal captures non-positive value:   {h2} ({mon['P']:+.3f})")
    print(f"  H3 the principal's value is added, not extracted:          {h3} "
          f"(parties E,M,R do not fall)")
    print(f"  H4 the principal grows the total value (Φ > 2):            {h4} ({phi_b})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "principal_rent.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "party", "shapley_value"])
        for p, val in base.items():
            w.writerow(["base_triad", p, val])
        for p, val in bidir.items():
            w.writerow(["bidirectional_principal", p, val])
        for p, val in mon.items():
            w.writerow(["monitor_only_principal", p, val])


if __name__ == "__main__":
    main()

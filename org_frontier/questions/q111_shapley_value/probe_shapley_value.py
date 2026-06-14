"""Probe Q111 (H1-H4) — the Shapley value of integration.

Distributes the read-recipient triad's Φ among its parties by their marginal contribution to the
coordination's integration, and checks the mediator's share and a non-core party's value.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q111_shapley_value.probe_shapley_value
"""

import csv
import os

from org_frontier.questions.q111_shapley_value import forms as F


def main():
    print("PROBE Q111 (H1-H4) — the Shapley value of integration")
    print("=" * 72)
    sv, phi = F.shapley(*F.read_recipient())
    n = len(sv)
    print(f"  read-recipient triad: Φ = {phi}")
    for party, val in sv.items():
        print(f"    {party}: Shapley value {val:+.3f}  (share {val / phi:.0%})" if phi else f"    {party}: {val}")
    sv_sp, phi_sp = F.shapley(*F.with_spectator())
    print(f"  with a read-only spectator X: whole-system Φ = {phi_sp}")
    print(f"    Shapley values: {sv_sp}")

    h1 = sv["M"] > sv["E"] and sv["M"] > sv["R"]
    h2 = abs(sum(sv.values()) - phi) < 1e-2
    h3 = sv["M"] > phi / n
    h4 = sv_sp["X"] <= 0
    print("=" * 72)
    print(f"  H1 the mediator's value exceeds each outer party's:        {h1}")
    print(f"  H2 the Shapley values sum to the system Φ (efficiency):    {h2}")
    print(f"  H3 the mediator captures a super-egalitarian share (>Φ/n): {h3} ({sv['M']:.3f} > {phi/n:.3f})")
    print(f"  H4 a non-core spectator captures non-positive value:       {h4} ({sv_sp['X']:+.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "shapley_value.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "party", "shapley_value"])
        for party, val in sv.items():
            w.writerow(["read_recipient", party, val])
        for party, val in sv_sp.items():
            w.writerow(["with_spectator", party, val])


if __name__ == "__main__":
    main()

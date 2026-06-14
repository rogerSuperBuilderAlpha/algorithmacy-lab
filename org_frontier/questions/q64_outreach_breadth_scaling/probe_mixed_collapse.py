"""Probe Q64-H4 — one substitutable recipient collapses an otherwise all-required campaign.

Hypothesis (H4): at k=3, mixed (M'=E&R1&(R2|R3)) is dyadic while all_required (M'=E&R1&R2&R3) is triadic.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q64_outreach_breadth_scaling.probe_mixed_collapse
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.questions.q64_outreach_breadth_scaling.forms import all_required, mixed_k3, labels, check_controls


def main():
    print("PROBE Q64-H4 — one substitutable recipient")
    print("=" * 64)
    print(check_controls(verdict))
    vm = verdict(mixed_k3(), labels(3))
    va = verdict(all_required(3), labels(3))
    print(f"  mixed (E&R1&(R2|R3))   {vm.structure:<8} Φ_MIP={vm.max_phi:.4f}")
    print(f"  all_required (E&R1&R2&R3) {va.structure:<8} Φ_MIP={va.max_phi:.4f}")
    confirmed = vm.structure == "dyadic" and va.structure == "triadic"
    print("=" * 64)
    print(f"  mixed dyadic: {vm.structure == 'dyadic'} | all_required triadic: {va.structure == 'triadic'}")
    print(f"  H4 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")
    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "mixed_collapse.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "structure", "max_phi"])
        w.writerow(["mixed", vm.structure, f"{vm.max_phi:.6f}"])
        w.writerow(["all_required", va.structure, f"{va.max_phi:.6f}"])


if __name__ == "__main__":
    main()

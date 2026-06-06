"""Probe Q64-H5 — every recipient sits in the core of an all-required campaign.

Hypothesis (H5): the major complex of all_required is the full party set at k=2 (n=4) and k=3 (n=5).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q64_outreach_breadth_scaling.probe_core_membership
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q64_outreach_breadth_scaling.forms import all_required, labels, check_controls


def main():
    print("PROBE Q64-H5 — core membership of the all-required campaign")
    print("=" * 64)
    print(check_controls(verdict))
    rows, all_full = [], True
    for k in (2, 3):
        lab = labels(k)
        core, phi = major_complex(all_required(k), lab)
        full = set(core or ()) == set(lab)
        all_full = all_full and full
        print(f"  k={k}  core={core}  Φ={phi:.4f}  full_set={full}")
        rows.append((k, "|".join(core or ()), f"{phi:.6f}", full))
    print("=" * 64)
    print(f"  every recipient in core (k=2,3): {all_full}")
    print(f"  H5 VERDICT: {'CONFIRMED' if all_full else 'REFUTED'}")
    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "core_membership.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["k", "core", "phi", "full_set"]); w.writerows(rows)


if __name__ == "__main__":
    main()

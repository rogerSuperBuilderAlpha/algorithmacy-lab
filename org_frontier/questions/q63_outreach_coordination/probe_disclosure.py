"""Probe Q63-H3 — disclosure is a label, not a read.

Question: does the agent announcing itself change the structure of the coordination?
Hypothesis (H3): adding a disclosure node D (D'=M) that no commit reads leaves the read-recipient triad's
major complex {E,M,R} and its Φ unchanged, with D excluded.
Method: read the major complex of the disclosed n=4 form and compare its core and Φ to the read-recipient
n=3 triad. Instrument control as in H1.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q63_outreach_coordination.probe_disclosure
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q63_outreach_coordination.forms import (
    LABELS3, LABELS_D, READ_RECIPIENT, DISCLOSED, check_controls,
)


def main():
    print("PROBE Q63-H3 — disclosure is a label, not a read")
    print("=" * 64)
    print(check_controls(verdict))

    base_core, base_phi = major_complex(READ_RECIPIENT, LABELS3)
    disc_core, disc_phi = major_complex(DISCLOSED, LABELS_D)
    print(f"  read_recipient triad core={base_core} Φ={base_phi:.4f}")
    print(f"  disclosed form     core={disc_core} Φ={disc_phi:.4f}")

    core_unchanged = set(disc_core or ()) == {"E", "M", "R"}
    d_excluded = "D" not in (disc_core or ())
    phi_equal = abs((disc_phi or -1) - (base_phi or -2)) < 1e-6
    confirmed = core_unchanged and d_excluded and phi_equal
    print("=" * 64)
    print(f"  core == {{E,M,R}}: {core_unchanged} | D excluded: {d_excluded} | Φ equal: {phi_equal}")
    print(f"  H3 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")

    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "disclosure.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "core", "phi"])
        w.writerow(["read_recipient", "|".join(base_core or ()), f"{base_phi:.6f}"])
        w.writerow(["disclosed", "|".join(disc_core or ()), f"{disc_phi:.6f}"])


if __name__ == "__main__":
    main()

"""Probe Q64-H2 — substitutable campaign is dyadic at every breadth.

Hypothesis (H2): substitutable (M'=E&(R1|...|Rk)) is dyadic for k=2,3,4. Instrument control first.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q64_outreach_breadth_scaling.probe_substitutable_scaling
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.questions.q64_outreach_breadth_scaling.forms import substitutable, labels, check_controls


def main():
    print("PROBE Q64-H2 — substitutable campaign scaling")
    print("=" * 64)
    print(check_controls(verdict))
    rows, all_dyadic = [], True
    for k in (2, 3, 4):
        n = k + 2
        v = verdict(substitutable(k), labels(k))
        dy = v.structure == "dyadic"
        all_dyadic = all_dyadic and dy
        print(f"  k={k} n={n}  {v.structure:<8} Φ_MIP={v.max_phi:.4f}")
        rows.append((k, n, v.structure, f"{v.max_phi:.6f}"))
    print("=" * 64)
    print(f"  all k dyadic: {all_dyadic}")
    print(f"  H2 VERDICT: {'CONFIRMED' if all_dyadic else 'REFUTED'}")
    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "substitutable_scaling.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["k", "n", "structure", "max_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()

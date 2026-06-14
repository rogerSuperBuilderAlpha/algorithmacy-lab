"""Probe Q64-H1 — all-required campaign stays triadic at Φ = n−1 at every breadth.

Question: does an all-binding multi-recipient campaign stay triadic as recipients are added?
Hypothesis (H1): all_required (M'=E&R1&...&Rk) is triadic for k=1..4 (n=3..6) with Φ_MIP = n−1.
Method: classify each k with exact IIT-4.0 Φ over the MIP. Instrument control first.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q64_outreach_breadth_scaling.probe_all_required_scaling
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.questions.q64_outreach_breadth_scaling.forms import all_required, labels, check_controls


def main():
    print("PROBE Q64-H1 — all-required campaign scaling")
    print("=" * 64)
    print(check_controls(verdict))
    rows, all_ok = [], True
    for k in (1, 2, 3, 4):
        n = k + 2
        v = verdict(all_required(k), labels(k))
        law = abs(v.max_phi - (n - 1)) < 1e-6
        ok = v.structure == "triadic" and law
        all_ok = all_ok and ok
        print(f"  k={k} n={n}  {v.structure:<8} Φ_MIP={v.max_phi:.4f}  (n-1={n-1}) law_holds={law}")
        rows.append((k, n, v.structure, f"{v.max_phi:.6f}", n - 1, law))
    print("=" * 64)
    print(f"  all k triadic at Φ=n-1: {all_ok}")
    print(f"  H1 VERDICT: {'CONFIRMED' if all_ok else 'REFUTED'}")

    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "all_required_scaling.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["k", "n", "structure", "max_phi", "n_minus_1", "law_holds"])
        w.writerows(rows)


if __name__ == "__main__":
    main()

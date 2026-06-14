"""Probe Q103 (H1-H4) — does the cause-effect structure follow the operations?

Reads the integrated structure of the read-recipient triad under substitution, a tracking memory, and
delegation, and tests whether substitution collapses it and the others restructure it.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q103_structure_under_operations.probe_structure_under_operations
"""

import csv
import os

from org_frontier.questions.q103_structure_under_operations import forms as F


def main():
    print("PROBE Q103 (H1-H4) — the cause-effect structure under the operations")
    print("=" * 78)
    rows = {}
    for name, (rules, labels) in F.OPERATIONS.items():
        phi, dtype, jp = F.joint_parties(rules, labels)
        rows[name] = {"phi": phi, "dtype": dtype, "joint": tuple(sorted(jp))}
        print(f"  {name:<24} Φ={phi:<5} type={dtype:<11} joint_mechanism_parties={tuple(sorted(jp))}")

    sub = rows["substitution"]
    mem = rows["tracking_memory"]
    dele = rows["delegation_triage"]
    h1 = sub["phi"] == 0.0 and not sub["joint"]
    h2 = mem["phi"] > 0 and "Mem" in mem["joint"]
    h3 = dele["phi"] > 0 and "T" in dele["joint"]
    h4 = all((r["phi"] > 0) == bool(r["joint"]) for r in rows.values())
    print("=" * 78)
    print(f"  H1 substitution collapses the integrated structure:        {h1}")
    print(f"  H2 a tracking memory restructures it (Mem enters):         {h2} ({mem['joint']})")
    print(f"  H3 delegation restructures it (T enters):                  {h3} ({dele['joint']})")
    print(f"  H4 the joint mechanism is present iff the form is triadic: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "structure_under_operations.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["operation", "phi", "dual_type", "joint_mechanism_parties"])
        for name, r in rows.items():
            w.writerow([name, r["phi"], r["dtype"], "|".join(r["joint"])])


if __name__ == "__main__":
    main()

"""Probe Q63-H1 — read-the-recipient versus broadcast outreach.

Question: does an agent that reads the recipient produce triadic coordination where a broadcast does not?
Hypothesis (H1): read_recipient (E'=M, M'=E&R, R'=M) is triadic; broadcast (E'=M, M'=E, R'=M) is dyadic.
Method: classify both with exact IIT-4.0 Φ over the MIP. Instrument control: a dyadic relay reads dyadic
and a fully-coupled triad reads triadic before the comparison.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q63_outreach_coordination.probe_read_recipient
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.questions.q63_outreach_coordination.forms import (
    LABELS3, READ_RECIPIENT, BROADCAST, check_controls,
)


def main():
    print("PROBE Q63-H1 — read-the-recipient vs broadcast")
    print("=" * 64)
    print(check_controls(verdict))
    res, rows = {}, []
    for name, rules in (("read_recipient", READ_RECIPIENT), ("broadcast", BROADCAST)):
        v = verdict(rules, LABELS3)
        res[name] = v
        print(f"  {name:<16} {v.structure:<8} Φ_MIP={v.max_phi:.4f}")
        rows.append((name, v.structure, f"{v.max_phi:.6f}"))
    confirmed = res["read_recipient"].structure == "triadic" and res["broadcast"].structure == "dyadic"
    print("=" * 64)
    print(f"  read_recipient triadic: {res['read_recipient'].structure == 'triadic'} | "
          f"broadcast dyadic: {res['broadcast'].structure == 'dyadic'}")
    print(f"  H1 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")

    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "read_recipient.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "structure", "max_phi"])
        w.writerows(rows)


if __name__ == "__main__":
    main()

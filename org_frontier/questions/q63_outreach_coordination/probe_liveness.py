"""Probe Q63-H5 — liveness, not the mediator reading both, carries the verdict.

Question: is one-shot outreach triadic, or does irreducibility need the recipient's response to stay live?
Hypothesis (H5): conversation (E'=M, M'=E&R, R'=M) is triadic; one_shot (E'=M, M'=E&R, R'=R, recipient
frozen) is dyadic, even though M reads both E and R in both forms.
Method: classify both n=3 forms with exact IIT-4.0 Φ over the MIP. Instrument control as in H1.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q63_outreach_coordination.probe_liveness
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.questions.q63_outreach_coordination.forms import (
    LABELS3, CONVERSATION, ONE_SHOT, check_controls,
)


def main():
    print("PROBE Q63-H5 — liveness vs one-shot")
    print("=" * 64)
    print(check_controls(verdict))
    res, rows = {}, []
    for name, rules in (("conversation", CONVERSATION), ("one_shot", ONE_SHOT)):
        v = verdict(rules, LABELS3)
        res[name] = v
        print(f"  {name:<16} {v.structure:<8} Φ_MIP={v.max_phi:.4f}")
        rows.append((name, v.structure, f"{v.max_phi:.6f}"))
    confirmed = res["conversation"].structure == "triadic" and res["one_shot"].structure == "dyadic"
    print("=" * 64)
    print(f"  conversation triadic: {res['conversation'].structure == 'triadic'} | "
          f"one_shot dyadic: {res['one_shot'].structure == 'dyadic'}")
    print(f"  H5 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")

    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "liveness.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "structure", "max_phi"])
        w.writerows(rows)


if __name__ == "__main__":
    main()

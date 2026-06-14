"""Probe Q63-H4 — a cost proxy does not recover the verdict.

Question: can a cheap cost proxy stand in for the structural verdict?
Hypothesis (H4): the mediator's in-degree (number of sources M's commit reads), a stand-in for tailoring
cost, fails to separate dyadic from triadic - at least one dyadic form has in-degree >= a triadic form's.
Method: compute mediator in-degree from the connectivity matrix for the four forms and pair it with each
form's verdict. Instrument control as in H1.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q63_outreach_coordination.probe_cost_proxy
"""

import csv
import os

from org_frontier.probes.lib import verdict
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.questions.q63_outreach_coordination.forms import (
    LABELS3, LABELS4, READ_RECIPIENT, BROADCAST, ALL_REQUIRED, SUBSTITUTABLE, check_controls,
)

M_INDEX = 1  # the mediator is element 1 in every form


def main():
    print("PROBE Q63-H4 — cost proxy (mediator in-degree) vs verdict")
    print("=" * 64)
    print(check_controls(verdict))
    forms = [
        ("read_recipient", READ_RECIPIENT, LABELS3),
        ("broadcast", BROADCAST, LABELS3),
        ("all_required", ALL_REQUIRED, LABELS4),
        ("substitutable", SUBSTITUTABLE, LABELS4),
    ]
    rows, recs = [], []
    for name, rules, labels in forms:
        v = verdict(rules, labels)
        cm = cm_from_rules(rules)
        cost = int(cm[:, M_INDEX].sum())  # sources the mediator's commit reads
        recs.append((name, v.structure, cost))
        print(f"  {name:<16} {v.structure:<8} mediator_in_degree(cost)={cost}")
        rows.append((name, v.structure, cost))

    triadic_costs = [c for _, s, c in recs if s == "triadic"]
    dyadic_costs = [c for _, s, c in recs if s == "dyadic"]
    # H4 confirmed if the proxy is non-monotone: some dyadic form's cost >= some triadic form's cost.
    non_monotone = any(dc >= tc for dc in dyadic_costs for tc in triadic_costs)
    print("=" * 64)
    print(f"  triadic costs={sorted(triadic_costs)} | dyadic costs={sorted(dyadic_costs)}")
    print(f"  cost proxy non-monotone (a dyadic form >= a triadic form): {non_monotone}")
    print(f"  H4 VERDICT: {'CONFIRMED' if non_monotone else 'REFUTED'}")

    d = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "cost_proxy.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "structure", "mediator_in_degree"])
        w.writerows(rows)


if __name__ == "__main__":
    main()

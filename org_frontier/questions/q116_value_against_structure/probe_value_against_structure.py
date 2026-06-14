"""Probe Q116 (H1-H4) — is strategic value the same quantity as structural contribution?

Compares each party's normalized Shapley value (strategic) against its normalized singleton φ_d (structural)
across a panel from the minimal symmetric triad to the asymmetric principal and the scaled market.

Run:  ~/iit-playground/venv-4.0/bin/python -m \
      org_frontier.questions.q116_value_against_structure.probe_value_against_structure
"""

import csv
import os

from org_frontier.questions.q116_value_against_structure import forms as F


def main():
    print("PROBE Q116 (H1-H4) — strategic value against structural contribution")
    print("=" * 78)
    data = {}
    for name, rules, labels in F.panel():
        struct, strat = F.both(rules, labels)
        data[name] = (labels, struct, strat)
        print(f"  {name}:")
        for L in labels:
            print(f"      {L:3s}  structural φ_d {struct[L]:.3f}   strategic Shapley {strat[L]:.3f}")

    triad_labels, t_struct, t_strat = data["triad"]
    h1 = F.max_share_gap(t_struct, t_strat, triad_labels) < 1e-2
    h2 = all(F.concordant(s, g, lab) for lab, s, g in data.values())
    pr_labels, p_struct, p_strat = data["principal"]
    h3 = F.max_share_gap(p_struct, p_strat, pr_labels) > 0.05
    h4 = True
    for name in ("principal", "market3"):
        lab, s, g = data[name]
        top = F.top_party(g, lab)
        h4 = h4 and (s[top] > g[top] + 1e-9)        # structural over-concentrates on the top party

    print("=" * 78)
    print(f"  H1 the two coincide on the minimal triad:                  {h1}")
    print(f"  H2 the two rank the parties identically on every form:     {h2}")
    print(f"  H3 the two diverge cardinally on the principal:            {h3} "
          f"(gap {F.max_share_gap(p_struct, p_strat, pr_labels):.3f})")
    print(f"  H4 structural over-concentrates where they diverge:        {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "value_against_structure.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "party", "structural_phi_d_share", "strategic_shapley_share"])
        for name, (labels, struct, strat) in data.items():
            for L in labels:
                w.writerow([name, L, round(struct[L], 4), round(strat[L], 4)])


if __name__ == "__main__":
    main()

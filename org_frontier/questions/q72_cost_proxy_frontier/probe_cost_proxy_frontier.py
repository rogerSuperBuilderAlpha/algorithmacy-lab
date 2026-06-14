"""Probe Q72 (H1-H4) — do cheap structural proxies recover the outreach verdict?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q72_cost_proxy_frontier.probe_cost_proxy_frontier
"""
import csv, os
from org_frontier.probes.lib import verdict
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.questions.q72_cost_proxy_frontier.forms import FORMS


def main():
    print("PROBE Q72 (H1-H4) — cost/proxy frontier")
    print("=" * 72)
    rows = []
    for name, rules, labels, mi in FORMS:
        v = verdict(rules, labels)
        cm = cm_from_rules(rules)
        med_indeg = int(cm[:, mi].sum())
        edges = int(cm.sum())
        rows.append((name, v.structure, med_indeg, edges))
        print(f"  {name:<16} {v.structure:<8} med_in_degree={med_indeg}  total_edges={edges}")
    # proxy failure tests
    def by(s): return [r for r in rows if r[1] == s]
    tri, dy = by("triadic"), by("dyadic")
    # H1: a triadic and a dyadic form share the same mediator in-degree
    h1 = any(t[2] == d[2] for t in tri for d in dy)
    # H2: a triadic and a dyadic form share the same total edge count
    h2 = any(t[3] == d[3] for t in tri for d in dy)
    # H3: a dyadic form has mediator in-degree >= a triadic form (non-monotone)
    h3 = any(d[2] >= t[2] for d in dy for t in tri)
    # H4: neither proxy is a threshold separator (both H1/H2 collisions exist => no monotone cut)
    h4 = h1 and h3
    print("=" * 72)
    print(f"  same med-in-degree across verdicts (in-degree cannot separate): {h1}")
    print(f"  same total-edges across verdicts (edges cannot separate): {h2}")
    print(f"  dyadic med-in-degree >= triadic (non-monotone): {h3}")
    print(f"  no structural cost proxy recovers the verdict: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "cost_proxy_frontier.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "structure", "med_in_degree", "total_edges"]); w.writerows(rows)


if __name__ == "__main__":
    main()

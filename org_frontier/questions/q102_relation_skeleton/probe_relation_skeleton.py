"""Probe Q102 (H1-H4) — over which purviews do a coordination's relations concentrate?

Reads the relation skeleton of mediated and symmetric triads and tests the hub motif, the combinatorial
growth of relations, and the spread in symmetric forms.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q102_relation_skeleton.probe_relation_skeleton
"""

import csv
import os

from org_frontier.questions.q102_relation_skeleton import forms as F


def main():
    print("PROBE Q102 (H1-H4) — the relation skeleton of coordination")
    print("=" * 78)
    rows = {}
    for group, forms in (("mediated", F.MEDIATED), ("symmetric", F.SYMMETRIC)):
        for name, (rules, labels) in forms.items():
            s = F.relation_skeleton(rules, labels)
            s["group"] = group
            rows[name] = s
            density = s["n_relations"] / max(s["n_distinctions"], 1)
            print(f"  {name:<18} [{group:<9}] {s['n_relations']:>3} rels over "
                  f"hub {s['hub']} share={s['hub_share']:.2f} max_order={s['max_order']} "
                  f"density={density:.1f}")

    rr, ar = rows["read_recipient"], rows["all_required_k2"]
    ring, mkt = rows["ring_d2"], rows["market_N2"]
    dens = lambda r: r["n_relations"] / max(r["n_distinctions"], 1)

    h1 = rr["hub_share"] > 0.5 and ar["hub_share"] > 0.5
    h2 = dens(ar) > dens(rr)
    h3 = ring["hub_share"] < 0.5 and mkt["hub_share"] < 0.5
    h4 = ar["hub_share"] > 0.9 and ar["max_order"] >= 5
    print("=" * 78)
    print(f"  H1 mediated triads concentrate relations on a hub (>50%):     {h1}")
    print(f"  H2 the breadth market is denser in relations than the triad:  {h2} "
          f"({dens(ar):.1f} vs {dens(rr):.1f})")
    print(f"  H3 symmetric triads spread relations (no hub >50%):           {h3}")
    print(f"  H4 the breadth hub is combinatorial (>90% share, order>=5):   {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "relation_skeleton.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "group", "n_distinctions", "n_relations", "hub", "hub_share", "max_order"])
        for name, s in rows.items():
            w.writerow([name, s["group"], s["n_distinctions"], s["n_relations"],
                        "|".join(s["hub"]), s["hub_share"], s["max_order"]])


if __name__ == "__main__":
    main()

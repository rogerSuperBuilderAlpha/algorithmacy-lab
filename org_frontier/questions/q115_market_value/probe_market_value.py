"""Probe Q115 (H1-H4) — how a required market's value scales.

Computes the Shapley value distribution of the all-required market at N = 2, 3, 4 and reads how the outer
parties' and the agents' value scale.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q115_market_value.probe_market_value
"""

import csv
import os

from org_frontier.questions.q115_market_value import forms as F


def main():
    print("PROBE Q115 (H1-H4) — the value distribution of a required market at scale")
    print("=" * 76)
    rows = {N: F.market_shapley(N) for N in F.SIZES}
    for N, r in rows.items():
        print(f"  N={N} (Φ={r['phi']}): outer party {r['outer']:.3f}, each agent {r['agent']:.3f}, "
              f"total {r['total']:.3f}")

    h1 = all(abs(rows[N]["total"] - rows[N]["phi"]) < 1e-2 for N in F.SIZES)
    h2 = all(rows[N]["outer"] > rows[N]["agent"] for N in (3, 4))
    h3 = rows[2]["outer"] < rows[3]["outer"] < rows[4]["outer"]
    h4 = rows[4]["agent"] <= rows[2]["agent"] + 1e-9
    print("=" * 76)
    print(f"  H1 the market distributes its full Φ at every N:           {h1}")
    print(f"  H2 the unique outer parties out-earn each agent (N>=3):    {h2}")
    print(f"  H3 the outer parties' value grows with N:                  {h3} "
          f"({rows[2]['outer']:.2f} < {rows[3]['outer']:.2f} < {rows[4]['outer']:.2f})")
    print(f"  H4 each agent's value does not grow with N (commoditized): {h4} "
          f"({rows[2]['agent']:.2f} -> {rows[4]['agent']:.2f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "market_value.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["N", "phi", "outer_party_value", "agent_value", "total"])
        for N, r in rows.items():
            w.writerow([N, r["phi"], r["outer"], r["agent"], r["total"]])


if __name__ == "__main__":
    main()

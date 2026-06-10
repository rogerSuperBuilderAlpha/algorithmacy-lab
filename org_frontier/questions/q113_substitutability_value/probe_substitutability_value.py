"""Probe Q113 (H1-H4) — does substitutability erode value or destroy it?

Compares the Shapley value distribution of an all-required market with a substitutable one.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q113_substitutability_value.probe_substitutability_value
"""

import csv
import os

from org_frontier.questions.q113_substitutability_value import forms as F


def main():
    print("PROBE Q113 (H1-H4) — substitutability and value")
    print("=" * 72)
    sv_req, phi_req = F.shapley_for(F.ALL_REQUIRED)
    sv_sub, phi_sub = F.shapley_for(F.SUBSTITUTABLE)
    tot_req = sum(sv_req.values())
    tot_sub = sum(sv_sub.values())
    print(f"  all-required market:  Φ={phi_req}  Shapley={sv_req}  total={tot_req:.2f}")
    print(f"  substitutable market: Φ={phi_sub}  Shapley={sv_sub}  total={tot_sub:.2f}")

    spread = max(sv_req.values()) - min(sv_req.values())
    h1 = tot_req > 0
    h2 = abs(tot_sub) < 1e-9
    h3 = spread < 1e-2
    h4 = abs((tot_req - tot_sub) - phi_req) < 1e-2
    print("=" * 72)
    print(f"  H1 the all-required market captures positive value:        {h1} ({tot_req:.2f})")
    print(f"  H2 the substitutable market captures zero value:           {h2} ({tot_sub:.2f})")
    print(f"  H3 the required parties share value equally:               {h3} (spread {spread:.3f})")
    print(f"  H4 substitutability destroys the whole value (= Φ):        {h4} ({tot_req - tot_sub:.2f} = {phi_req})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "substitutability_value.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["market", "party", "shapley_value"])
        for p, v in sv_req.items():
            w.writerow(["all_required", p, v])
        for p, v in sv_sub.items():
            w.writerow(["substitutable", p, v])


if __name__ == "__main__":
    main()

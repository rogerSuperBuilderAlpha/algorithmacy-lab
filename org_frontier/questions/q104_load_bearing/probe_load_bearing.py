"""Probe Q104 (H1-H4) — which element of the structure carries the integration?

Ranks the read-recipient triad's distinctions by φ_d and recomputes the verdict after knocking out each of
its edges, to locate the load-bearing distinction and test whether every read is load-bearing.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q104_load_bearing.probe_load_bearing
"""

import csv
import os

from org_frontier.questions.q104_load_bearing import forms as F


def main():
    print("PROBE Q104 (H1-H4) — the load-bearing distinction of the read-recipient triad")
    print("=" * 78)
    phi, dists = F.distinctions_by_phi(*F.read_recipient())
    print(f"  system Φ = {phi}")
    for mech, purv, pd in dists:
        print(f"    distinction {mech} -> {purv}  φ_d={pd}")
    ko = F.knockout_verdicts()
    print("  edge knockouts:")
    for name, (struct, kphi) in ko.items():
        print(f"    drop {name:<10} -> {struct} Φ={kphi}")

    top = dists[0]
    binding_top = len(top[0]) >= 2 or len(top[1]) >= 2
    singles = [pd for m, p, pd in dists if len(m) == 1 and len(p) == 1]
    h1 = binding_top and abs(top[2] - phi) < 1e-9
    h2 = all(pd < phi - 1e-9 for pd in singles) if singles else False
    h3 = ko["M_reads_R"][0] == "dyadic"
    h4 = all(struct == "dyadic" for struct, _ in ko.values())
    print("=" * 78)
    print(f"  H1 the load-bearing distinction is binding, with φ_d = Φ:    {h1}")
    print(f"  H2 the singleton distinctions carry less than Φ:             {h2}")
    print(f"  H3 knocking the mediator's read collapses the verdict:       {h3}")
    print(f"  H4 every edge is load-bearing (no redundancy):              {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "load_bearing.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["element", "type", "value"])
        for mech, purv, pd in dists:
            w.writerow(["|".join(mech) + "->" + "|".join(purv), "distinction_phi", pd])
        for name, (struct, kphi) in ko.items():
            w.writerow([name, "knockout_verdict", f"{struct}:{kphi}"])


if __name__ == "__main__":
    main()

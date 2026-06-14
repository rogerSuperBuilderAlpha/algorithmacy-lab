"""Probe Q89 (H1-H4) — which heterogeneous agents enter the core of a market?

Q85 showed a market of interchangeable agents collapses all-or-nothing. This asks what happens when the
agents differ: a passive (read-only) agent, a full agent reading both outer parties, and partial agents
reading only one. The major complex is read for each configuration.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q89_heterogeneous_market.probe_heterogeneous_market
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q89_heterogeneous_market import forms as F


def read(name, types, active, combine):
    rules, lab = F.market(types, active, combine)
    v = verdict(rules, lab)
    core, phi = major_complex(rules, lab)
    core = tuple(core or ())
    print(f"  {name:<22} {v.structure:<8} Φ={v.max_phi:.2f}  core={core}")
    return {"name": name, "structure": v.structure, "phi": round(float(v.max_phi), 3), "core": core}


def main():
    print("PROBE Q89 (H1-H4) — heterogeneous agent market")
    print("=" * 78)
    # baseline (validation): full pair, all-required -> reproduces Q85 (triadic, full core)
    base = read("full_pair_required", ["full", "full"], [1, 2], "and")
    # H1: one full agent passive (reads E,C but not read forward) -> excluded from core
    passive = read("one_passive", ["full", "full"], [1], "and")
    # H2: a required agent reading only the sender -> in core?
    sender = read("sender_only_req", ["full", "sender"], [1, 2], "and")
    # H3: a required agent reading only the recipient; and a mixed required market
    recip = read("recipient_only_req", ["full", "recipient"], [1, 2], "and")
    mixed = read("mixed3_required", ["full", "sender", "recipient"], [1, 2, 3], "and")
    # H4: substitutable heterogeneous market -> dyadic
    subst = read("hetero_substitutable", ["full", "sender"], [1, 2], "or")

    h1 = ("M2" not in passive["core"]) and (set(passive["core"]) == {"E", "M1", "C"})
    h2 = ("M2" in sender["core"]) and sender["structure"] == "triadic"
    h3 = (mixed["structure"] == "triadic"
          and set(mixed["core"]) == {"E", "M1", "M2", "M3", "C"}
          and "M2" in recip["core"])
    h4 = subst["structure"] == "dyadic"

    print("=" * 78)
    print(f"  baseline full_pair_required: {base['structure']} Φ={base['phi']} core={base['core']}")
    print(f"  H1 passive (read-only) agent excluded, core={{E,M1,C}}:        {h1}")
    print(f"  H2 sender-only required agent enters the core:                {h2}")
    print(f"  H3 mixed required market: one stable core of all agents+E+C:  {h3}")
    print(f"  H4 substitutable heterogeneous market is dyadic:              {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "heterogeneous_market.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["config", "structure", "phi", "core"])
        for r in (base, passive, sender, recip, mixed, subst):
            w.writerow([r["name"], r["structure"], r["phi"], "|".join(r["core"])])


if __name__ == "__main__":
    main()

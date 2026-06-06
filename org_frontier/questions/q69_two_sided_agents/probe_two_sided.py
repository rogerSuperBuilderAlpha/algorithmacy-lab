"""Probe Q69 (H1-H4) — two-sided agent exchange: where is the core?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q69_two_sided_agents.probe_two_sided
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q69_two_sided_agents.forms import CONFIGS, LABELS, check_controls


def main():
    print("PROBE Q69 (H1-H4) — two-sided agent exchange")
    print("=" * 64)
    print(check_controls(verdict))
    data, rows = {}, []
    for name, rules in CONFIGS:
        core, phi = major_complex(rules, LABELS)
        cs = set(core or ())
        data[name] = (core, phi, cs)
        print(f"  {name:<12} core={core} Φ={phi:.4f} size={len(core or ())}")
        rows.append((name, "|".join(core or ()), f"{phi:.6f}", len(core or ())))
    lc, _, lcs = data["live_chain"]
    dg, dgphi, dgs = data["delegated"]
    cr, crphi, crs = data["closed_ring"]
    h1 = len(lc or ()) == 2 and ({"E"} & lcs or {"R"} & lcs)
    h2 = dgs == {"As", "Ar"}
    h3 = dgphi > 1e-9
    h4 = crs == {"E", "As", "Ar", "R"} and crphi > 2.0 + 1e-9
    print("=" * 64)
    print(f"  live_chain core human-agent pair: {bool(h1)} | delegated core == {{As,Ar}}: {h2}")
    print(f"  agent core triadic: {h3} | ring binds all four Φ>2: {h4}")
    print(f"  H1 VERDICT: {'CONFIRMED' if h1 else 'REFUTED'}")
    print(f"  H2 VERDICT: {'CONFIRMED' if h2 else 'REFUTED'}")
    print(f"  H3 VERDICT: {'CONFIRMED' if h3 else 'REFUTED'}")
    print(f"  H4 VERDICT: {'CONFIRMED' if h4 else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "two_sided.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["config", "core", "phi", "size"]); w.writerows(rows)


if __name__ == "__main__":
    main()

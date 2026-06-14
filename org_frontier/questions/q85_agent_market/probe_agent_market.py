"""Probe Q85 (H1-H4) — does interchangeability collapse a market of worker-side agents at every N?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q85_agent_market.probe_agent_market
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q85_agent_market import forms as F


def main():
    print("PROBE Q85 (H1-H4) — agent market: substitutable vs all-required at N=2,3,4")
    print("=" * 70)
    sub, req = {}, {}
    rows = []
    for N in (2, 3, 4):
        lab = F.labels(N)
        vs = verdict(F.substitutable(N), lab)
        vr = verdict(F.all_required(N), lab)
        sub[N] = vs.structure; req[N] = (vr.structure, vr.max_phi)
        print(f"  N={N} (n={N+2})  substitutable={vs.structure:<8}Φ={vs.max_phi:.3f} | all_required={vr.structure:<8}Φ={vr.max_phi:.3f}")
        rows.append((N, "substitutable", vs.structure, f"{vs.max_phi:.4f}"))
        rows.append((N, "all_required", vr.structure, f"{vr.max_phi:.4f}"))
    # H3: all-required core contains all N agents + E + C (use N=3)
    core3, phi3 = major_complex(F.all_required(3), F.labels(3))
    full3 = set(core3 or ()) == set(F.labels(3))
    print(f"  all_required N=3 core={core3} Φ={phi3:.3f} full_set={full3}")
    # H4: mixed (one substitutable pair) at N=3 factors
    vm = verdict(F.mixed_one_substitutable(3), F.labels(3))
    print(f"  mixed (one substitutable pair, N=3): {vm.structure} Φ={vm.max_phi:.3f}")

    h1 = all(sub[N] == "dyadic" for N in (2, 3, 4))
    h2 = all(req[N][0] == "triadic" for N in (2, 3, 4)) and req[2][1] < req[3][1] < req[4][1] + 1e-9
    h3 = full3
    h4 = vm.structure == "dyadic"
    print("=" * 70)
    print(f"  substitutable dyadic at every N: {h1}")
    print(f"  all-required triadic at every N, Φ grows: {h2}")
    print(f"  all-required core contains all agents + E + C: {h3}")
    print(f"  one substitutable pair among required still factors: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "agent_market.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["N", "form", "structure", "max_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()

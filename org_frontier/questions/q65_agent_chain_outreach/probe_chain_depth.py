"""Probe Q65-H1/H2 — agent chain stays triadic at every depth, Φ constant at 2.0.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q65_agent_chain_outreach.probe_chain_depth
"""
import csv, os
from org_frontier.probes.lib import verdict
from org_frontier.questions.q65_agent_chain_outreach.forms import agent_chain, chain_labels, check_controls


def main():
    print("PROBE Q65-H1/H2 — agent chain depth")
    print("=" * 64)
    print(check_controls(verdict))
    rows, all_tri, all_phi2 = [], True, True
    for d in (1, 2, 3, 4):
        n = d + 2
        v = verdict(agent_chain(d), chain_labels(d))
        tri = v.structure == "triadic"
        phi2 = abs(v.max_phi - 2.0) < 1e-6
        all_tri &= tri; all_phi2 &= phi2
        print(f"  d={d} agents (n={n})  {v.structure:<8} Φ_MIP={v.max_phi:.4f}")
        rows.append((d, n, v.structure, f"{v.max_phi:.6f}"))
    print("=" * 64)
    print(f"  all depths triadic: {all_tri} | Φ constant at 2.0: {all_phi2}")
    print(f"  H1 VERDICT: {'CONFIRMED' if all_tri else 'REFUTED'}")
    print(f"  H2 VERDICT: {'CONFIRMED' if all_phi2 else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "chain_depth.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["d", "n", "structure", "max_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()

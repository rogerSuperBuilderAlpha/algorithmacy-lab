"""Probe Q65-H3 — a relay-gap agent collapses the chain.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q65_agent_chain_outreach.probe_relay_gap
"""
import csv, os
from org_frontier.probes.lib import verdict
from org_frontier.questions.q65_agent_chain_outreach.forms import agent_chain, relay_gap, chain_labels, check_controls


def main():
    print("PROBE Q65-H3 — relay-gap agent")
    print("=" * 64)
    print(check_controls(verdict))
    vi = verdict(agent_chain(2), chain_labels(2))
    vg = verdict(relay_gap(), chain_labels(2))
    print(f"  intact chain     {vi.structure:<8} Φ_MIP={vi.max_phi:.4f}")
    print(f"  relay_gap chain  {vg.structure:<8} Φ_MIP={vg.max_phi:.4f}")
    confirmed = vg.structure == "dyadic" and vi.structure == "triadic"
    print("=" * 64)
    print(f"  relay_gap dyadic: {vg.structure == 'dyadic'} | intact triadic: {vi.structure == 'triadic'}")
    print(f"  H3 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "relay_gap.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "structure", "max_phi"])
        w.writerow(["intact", vi.structure, f"{vi.max_phi:.6f}"])
        w.writerow(["relay_gap", vg.structure, f"{vg.max_phi:.6f}"])


if __name__ == "__main__":
    main()

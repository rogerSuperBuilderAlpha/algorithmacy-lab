"""Probe Q65-H4 — the whole agent chain is the irreducible core.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q65_agent_chain_outreach.probe_chain_core
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q65_agent_chain_outreach.forms import agent_chain, chain_labels, check_controls


def main():
    print("PROBE Q65-H4 — chain core membership")
    print("=" * 64)
    print(check_controls(verdict))
    lab = chain_labels(2)
    core, phi = major_complex(agent_chain(2), lab)
    full = set(core or ()) == set(lab)
    print(f"  d=2 chain core={core} Φ={phi:.4f} full_set={full}")
    print("=" * 64)
    print(f"  whole chain is core: {full}")
    print(f"  H4 VERDICT: {'CONFIRMED' if full else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "chain_core.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["core", "phi", "full_set"]); w.writerow(["|".join(core or ()), f"{phi:.6f}", full])


if __name__ == "__main__":
    main()

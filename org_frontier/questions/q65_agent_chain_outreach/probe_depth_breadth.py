"""Probe Q65-H5 — depth does not undo breadth.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q65_agent_chain_outreach.probe_depth_breadth
"""
import csv, os
from org_frontier.probes.lib import verdict
from org_frontier.questions.q65_agent_chain_outreach.forms import depth_breadth, check_controls


def main():
    print("PROBE Q65-H5 — depth atop breadth")
    print("=" * 64)
    print(check_controls(verdict))
    lab = ("E", "A1", "M", "R1", "R2")
    v = verdict(depth_breadth(), lab)
    confirmed = v.structure == "triadic"
    print(f"  depth+breadth form  {v.structure:<8} Φ_MIP={v.max_phi:.4f}")
    print("=" * 64)
    print(f"  depth+breadth triadic: {confirmed}")
    print(f"  H5 VERDICT: {'CONFIRMED' if confirmed else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "depth_breadth.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "structure", "max_phi"]); w.writerow(["depth_breadth", v.structure, f"{v.max_phi:.6f}"])


if __name__ == "__main__":
    main()

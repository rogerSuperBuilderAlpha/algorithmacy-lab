"""Probe Q70 (H1-H4) — does multi-homing across interchangeable agents collapse the triad?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q70_agent_substitutability.probe_agent_substitutability
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q70_agent_substitutability import forms as F


def main():
    print("PROBE Q70 (H1-H4) — agent substitutability")
    print("=" * 64)
    print(F.check_controls(verdict))
    vs = verdict(F.SINGLE, F.LABELS3)
    vu = verdict(F.SUBST, F.LABELS4)
    vr = verdict(F.REQUIRED, F.LABELS4); cr, prc = major_complex(F.REQUIRED, F.LABELS4)
    print(f"  single agent      {vs.structure:<8} Φ_MIP={vs.max_phi:.4f}")
    print(f"  substitutable     {vu.structure:<8} Φ_MIP={vu.max_phi:.4f}")
    print(f"  required-both     {vr.structure:<8} Φ_MIP={vr.max_phi:.4f}  core={cr}")
    both_in = {"M1", "M2"} <= set(cr or ())
    h1 = vs.structure == "triadic"
    h2 = vu.structure == "dyadic"
    h3 = vr.structure == "triadic"
    h4 = both_in
    print("=" * 64)
    print(f"  single triadic: {h1} | substitutable dyadic: {h2} | required triadic: {h3} | both agents in core: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "agent_substitutability.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "structure", "max_phi"])
        w.writerow(["single", vs.structure, f"{vs.max_phi:.6f}"])
        w.writerow(["substitutable", vu.structure, f"{vu.max_phi:.6f}"])
        w.writerow(["required_both", vr.structure, f"{vr.max_phi:.6f}"])


if __name__ == "__main__":
    main()

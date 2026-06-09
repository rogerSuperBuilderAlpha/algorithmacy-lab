"""Probe Q83 (H1-H4) — do two gating agents enter the core only when jointly required?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q83_agent_coalition.probe_agent_coalition
"""
import csv, os
from org_frontier.probes.lib import major_complex
from org_frontier.questions.q83_agent_coalition import forms as F


def main():
    print("PROBE Q83 (H1-H4) — recipient-side gating coalition")
    print("=" * 66)
    br_core, br_phi = major_complex(F.BOTH_REQUIRED, F.LABELS5)
    es_core, es_phi = major_complex(F.EITHER_SUFFICES, F.LABELS5)
    sg_core, sg_phi = major_complex(F.SINGLE_BIDIR, F.LABELS4)
    print(f"  both_required    core={br_core} Φ={br_phi:.3f}")
    print(f"  either_suffices  core={es_core} Φ={es_phi:.3f}")
    print(f"  single_bidir     core={sg_core} Φ={sg_phi:.3f}")
    brs, ess, sgs = set(br_core or ()), set(es_core or ()), set(sg_core or ())
    h1 = {"T1", "T2"} <= brs                       # both agents in the core when jointly required
    h2 = not ({"T1", "T2"} <= ess)                 # not both in when either suffices (substitutable)
    h3 = "T" in sgs                                # single bidirectional gating agent enters (Q68)
    h4 = br_phi > 1e-9 and es_phi > 1e-9 and sg_phi > 1e-9   # base triad present (triadic core) in all
    print("=" * 66)
    print(f"  both-required: T1 and T2 in core: {h1}")
    print(f"  either-suffices: NOT both agents in core: {h2}")
    print(f"  single bidirectional agent enters core: {h3}")
    print(f"  triadic core present in all configs: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "agent_coalition.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["config", "core", "phi"])
        w.writerow(["both_required", "|".join(br_core or ()), f"{br_phi:.4f}"])
        w.writerow(["either_suffices", "|".join(es_core or ()), f"{es_phi:.4f}"])
        w.writerow(["single_bidir", "|".join(sg_core or ()), f"{sg_phi:.4f}"])


if __name__ == "__main__":
    main()

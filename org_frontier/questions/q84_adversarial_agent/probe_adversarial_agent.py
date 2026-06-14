"""Probe Q84 (H1-H4) — can a non-core agent flip the verdict from outside?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q84_adversarial_agent.probe_adversarial_agent
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q84_adversarial_agent import forms as F

BASE_CORE = {"E", "M", "R"}


def main():
    print("PROBE Q84 (H1-H4) — adversarial agent: influence vs membership")
    print("=" * 70)
    out = {}
    for name, rules in (("read_only", F.READ_ONLY), ("emit_only", F.EMIT_ONLY), ("bidir_pivotal", F.BIDIR_PIVOTAL)):
        v = verdict(rules, F.LABELS)
        core, cphi = major_complex(rules, F.LABELS)
        out[name] = (v.structure, v.max_phi, set(core or ()), cphi)
        print(f"  {name:<14} whole={v.structure:<8}Φ={v.max_phi:.3f} | core={core} Φ={cphi:.3f}")
    # core verdict = triadic iff core Phi>0
    def core_triadic(n): return out[n][3] > 1e-9
    h1 = out["read_only"][2] == BASE_CORE and core_triadic("read_only")          # X out, core unchanged & triadic
    h2 = out["emit_only"][2] == BASE_CORE and core_triadic("emit_only")
    h3 = out["bidir_pivotal"][2] != BASE_CORE                                    # pivotal X changes the core
    h4 = core_triadic("read_only") and core_triadic("emit_only")                 # no non-core coupling flips the core verdict to dyadic
    print("=" * 70)
    print(f"  read-only X: core {{E,M,R}} unchanged & triadic: {h1}")
    print(f"  emit-only X: core {{E,M,R}} unchanged & triadic: {h2}")
    print(f"  bidirectional-pivotal X changes the core: {h3}")
    print(f"  no non-core coupling flips the core verdict: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "adversarial_agent.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["coupling", "whole", "whole_phi", "core", "core_phi"])
        for name in ("read_only", "emit_only", "bidir_pivotal"):
            s, wp, c, cp = out[name]; w.writerow([name, s, f"{wp:.4f}", "|".join(sorted(c)), f"{cp:.4f}"])


if __name__ == "__main__":
    main()

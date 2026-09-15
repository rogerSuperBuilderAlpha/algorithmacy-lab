"""Probe — Simmel H1: the superindividual triad.

Question.  Does the mutual triad have the "superindividual energy" Simmel (1902, I: 45) denies the dyad —
           an irreducible whole that is the full triple, and a pair that stays bound through the third
           when its direct tie is removed?
Hypothesis. H1 (Simmel): triad_mutual core = {A,B,C}; Φ(triad) > Φ(dyad); triad_broken_line triadic with A
           and B in the core; dyad_cut Φ = 0.
Method.    Exact IIT-4.0 Φ_MIP and major complex on the four forms in methods.md (H1).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_superindividual
"""

from org_frontier.thinkers.simmel import forms as F


def main():
    print("Simmel H1 — the superindividual triad")
    control = F.run_control()
    recs = {name: F.evaluate(name, form) for name, form in [
        ("dyad_mutual", F.DYAD_MUTUAL), ("dyad_cut", F.DYAD_CUT),
        ("triad_mutual", F.TRIAD_MUTUAL), ("triad_broken_line", F.TRIAD_BROKEN_LINE)]}

    c1 = set(recs["triad_mutual"]["core"]) == {"A", "B", "C"}
    c2 = recs["triad_mutual"]["phi_mip"] > recs["dyad_mutual"]["phi_mip"]
    c3 = recs["triad_broken_line"]["verdict"] == "triadic" and {"A", "B"} <= set(recs["triad_broken_line"]["core"])
    c4 = recs["dyad_cut"]["phi_mip"] == 0.0
    checks = {"triad core is the full triple": c1, "Φ(triad) > Φ(dyad)": c2,
              "broken line keeps A and B bound": c3, "cut dyad has nothing left": c4}
    for k, ok in checks.items():
        print("  %-36s %s" % (k, "yes" if ok else "no"))
    n_ok = sum(checks.values())
    status = "CONFIRMED" if n_ok == 4 else ("PARTIAL" if n_ok >= 2 else "REFUTED")
    print("H1 (superindividual triad): %s" % status)
    F.save("probe_simmel_superindividual", {"control": control, "forms": recs, "checks": checks, "H1": status})


if __name__ == "__main__":
    main()

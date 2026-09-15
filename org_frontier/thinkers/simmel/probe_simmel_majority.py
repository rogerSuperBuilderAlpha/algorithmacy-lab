"""Probe — Simmel H3: the majority that overrides the individual.

Question.  Simmel (1902, II): in a dyad "there is no majority which can override the individual," and
           the occasion for one "is given so soon as a single unit is added." Is a triad in which each
           member follows the majority of the three an irreducible whole with all three in the core?
Hypothesis. H3 (Simmel): majority_triad triadic, core {A,B,C}. Lab prior (probe 10): a majority factors.
Method.    Exact Φ_MIP and major complex on majority_triad; unanimity_triad and unanimity_dyad for contrast.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_majority
"""

from org_frontier.thinkers.simmel import forms as F


def main():
    print("Simmel H3 — the majority that overrides the individual")
    control = F.run_control()
    recs = {name: F.evaluate(name, form) for name, form in [
        ("majority_triad", F.MAJORITY_TRIAD), ("unanimity_triad", F.UNANIMITY_TRIAD),
        ("unanimity_dyad", F.UNANIMITY_DYAD)]}
    m = recs["majority_triad"]
    ok = m["verdict"] == "triadic" and set(m["core"]) == {"A", "B", "C"}
    status = "CONFIRMED" if ok else "REFUTED"
    print("H3 (majority triad binds all three): %s" % status)
    F.save("probe_simmel_majority", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()

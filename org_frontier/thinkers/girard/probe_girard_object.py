"""Probe — Girard H3: the object is a means of reaching the mediator.

Question.  Girard (1965: 10, 99): "the impulse toward the object is ultimately an impulse toward the
           mediator"; in double mediation each copies "the copy of his own desire" and the object is
           forgotten. Is O in the complex, and does its presence change Φ at all?
Hypothesis. H3: double core = {S, M}; Φ(double core) = Φ(bare S ⇄ M dyad).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_object
"""

from org_frontier.thinkers.girard import forms as F


def main():
    print("Girard H3 — double mediation with the object, and the rivals alone")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("double", "dyad")}
    core_ok = set(recs["double"]["core"]) == {"S", "M"}
    same = abs(recs["double"]["core_phi"] - recs["dyad"]["core_phi"]) < 1e-6
    print("  double core is {S,M}=%s   Φ(double core)=%.3f = Φ(dyad)=%.3f: %s" % (
        core_ok, recs["double"]["core_phi"], recs["dyad"]["core_phi"], same))
    if core_ok and same:
        status = "CONFIRMED"
    elif core_ok:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H3 (the object is outside the structure and adds nothing to it): %s" % status)
    F.save("probe_girard_object", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()

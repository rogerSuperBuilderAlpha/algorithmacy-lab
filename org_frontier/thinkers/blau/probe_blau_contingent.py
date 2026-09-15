"""Probe — Blau H1: power is a relation when service is contingent on compliance.

Question.  Blau (1964: 22): the superior "attains power over others by making the satisfaction of their need
           contingent on their compliance." The Serres paper found a constant producer's arrow binds
           nothing. Does the contingent supplier bind where the independent one does not?
Hypothesis. H1: contingent core = {S, B}, Φ > 0; independent has no complex containing B.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_contingent
"""

from org_frontier.thinkers.blau import forms as F


def main():
    print("Blau H1 — the independent and the contingent supplier")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("independent", "contingent")}
    c_ok = set(recs["contingent"]["core"]) == {"S", "B"} and recs["contingent"]["core_phi"] > 1e-9
    i_ok = "B" not in recs["independent"]["core"]
    print("  contingent binds both=%s   independent leaves B unbound=%s" % (c_ok, i_ok))
    status = "CONFIRMED" if c_ok and i_ok else ("PARTIAL" if c_ok else "REFUTED")
    print("H1 (power is a relation when the service is contingent on compliance): %s" % status)
    F.save("probe_blau_contingent", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()

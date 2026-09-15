"""Probe — Serres H1: the one-way arrow is the atom of relation.

Question.  Serres (1982: 7–8): "it always goes in the same direction. The same one is the host; the same
           one takes and eats" — "the simple, irreversible arrow" — "the atomic form of our relations."
           A parasite reads a producer who does not read back. Is the pair a whole?
Hypothesis. H1: the arrow has a complex containing both with Φ > 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_arrow
"""

from org_frontier.thinkers.serres import forms as F


def main():
    print("Serres H1 — the arrow and the exchange")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("arrow", "exchange")}
    a = recs["arrow"]
    ok = {"F", "P"} <= set(a["core"]) and a["core_phi"] > 1e-9
    print("  arrow is a complex of host and parasite=%s   exchange Φ=%.3f" % (ok, recs["exchange"]["core_phi"]))
    status = "CONFIRMED" if ok else "REFUTED"
    print("H1 (the one-way arrow is a relation): %s" % status)
    F.save("probe_serres_arrow", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()

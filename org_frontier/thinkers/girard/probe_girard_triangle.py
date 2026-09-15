"""Probe — Girard H1: desire is triangular; the straight line is not essential.

Question.  Girard (1965: 2): "The straight line is present in the desire of Don Quixote, but it is not
           essential. The mediator is there, above that line, radiating toward both the subject and the
           object." In the internal triangle, are S and O one whole though S never reads O — and does
           deleting M dissolve it?
Hypothesis. H1: internal core ⊇ {S, O}; with M deleted, no complex contains both.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_triangle
"""

from org_frontier.thinkers.girard import forms as F


def main():
    print("Girard H1 — the internal triangle, and the triangle without its mediator")
    control = F.run_control()
    recs = {"spontaneous": F.evaluate("spontaneous"), "internal": F.evaluate("internal"),
            "internal_minus_M": F.evaluate("internal_minus_M", F.delete(F.SPECS["internal"], "M"))}
    together = {"S", "O"} <= set(recs["internal"]["core"])
    apart = not ({"S", "O"} <= set(recs["internal_minus_M"]["core"]))
    print("  S and O in one complex (internal)=%s   S and O apart once M is deleted=%s" % (together, apart))
    status = "CONFIRMED" if (together and apart) else "REFUTED"
    print("H1 (subject and object are one only through the mediator): %s" % status)
    F.save("probe_girard_triangle", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()

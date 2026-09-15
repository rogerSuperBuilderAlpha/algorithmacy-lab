"""Probe — Granovetter H1: strength is graded.

Question.  Granovetter (1973: 1361): strength is "a (probably linear) combination of the amount of time ..."
           A symmetric dyad read with probability p per step: is Φ strictly increasing in p?
Hypothesis. H1: Φ(dyad) strictly increasing over p = 0.25, 0.5, 0.75, 1.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_strength
"""

from org_frontier.thinkers.granovetter import forms as F

fs = frozenset


def main():
    print("Granovetter H1 — the dyad at four tie strengths")
    control = F.run_control()
    ps = (0.25, 0.5, 0.75, 1.0)
    recs = {}
    for p in ps:
        lab, ties = F.graph(("a", "b"), {fs("ab"): p})
        recs["p%.2f" % p] = F.evaluate("p%.2f" % p, lab, ties)
    phis = [recs["p%.2f" % p]["phi_mip"] for p in ps]
    strict = all(phis[i] < phis[i + 1] - 1e-9 for i in range(3))
    print("  Φ over p: %s  strictly increasing=%s" % (", ".join("%.3f" % x for x in phis), strict))
    status = "CONFIRMED" if strict else "REFUTED"
    print("H1 (Φ of a dyad rises strictly with tie strength): %s" % status)
    F.save("probe_granovetter_strength", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()

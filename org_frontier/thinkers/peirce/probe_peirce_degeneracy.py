"""Probe — Peirce H2: grades of degeneracy.

Question.  Peirce (CP 1.473): "Every triad is either monadically degenerate, dyadically degenerate, or
           genuine." Do his exemplars — three independent monads; "A father of B, B father of C"; the
           genuine triad — order strictly by genuine adicity 1 < 2 < 3?
Hypothesis. H2 (Peirce): they do, and neither degenerate form has a three-member complex.
Method.    genuine_adicity, whole Φ, and major complex on the three forms in methods.md (H2).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_degeneracy
"""

from org_frontier.thinkers.peirce import forms as F


def main():
    print("Peirce H2 — grades of degeneracy")
    control = F.run_control()
    recs = {name: F.evaluate(name, form) for name, form in [
        ("monadic_degenerate", F.MONADIC_DEGENERATE), ("dyadic_degenerate", F.DYADIC_DEGENERATE)]}
    recs["genuine"] = control
    a1, a2, a3 = (recs[k]["genuine_adicity"] for k in ("monadic_degenerate", "dyadic_degenerate", "genuine"))
    ordered = a1 <= 1 and a2 == 2 and a3 == 3
    no_triple = all(len(recs[k]["core"]) < 3 for k in ("monadic_degenerate", "dyadic_degenerate"))
    print("  adicity: monadic=%d dyadic=%d genuine=%d  degenerate forms without a 3-member complex: %s"
          % (a1, a2, a3, no_triple))
    status = "CONFIRMED" if (ordered and no_triple) else ("PARTIAL" if ordered or no_triple else "REFUTED")
    print("H2 (monadic < dyadic < genuine by adicity 1 < 2 < 3): %s" % status)
    F.save("probe_peirce_degeneracy", {"control": control, "forms": recs, "ordered": ordered,
                                        "no_triple": no_triple, "H2": status})


if __name__ == "__main__":
    main()

"""Probe — Peirce H3: giving.

Question.  Peirce (CP 1.345, 8.331): "A gives B to C" is a genuine triad — "A's making C the possessor
           according to Law" — while "A's putting B away from him and C's subsequently taking B up" is
           "merely one dyadic relation followed by another." Does the joint rule R'=G∧T carry a three-term
           fact that the two-step chain T'=G, R'=T lacks?
Hypothesis. H3 (Peirce): genuine giving has adicity 3 with G, T, R in one complex; the degenerate
           imitation has adicity ≤ 2.
Method.    genuine_adicity, whole Φ, and major complex on the two forms in methods.md (H3); giver rule shared.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_giving
"""

from org_frontier.thinkers.peirce import forms as F


def main():
    print("Peirce H3 — giving: genuine vs degenerate")
    control = F.run_control()
    recs = {name: F.evaluate(name, form) for name, form in [
        ("giving_genuine", F.GIVING_GENUINE), ("giving_degenerate", F.GIVING_DEGENERATE)]}
    g, d = recs["giving_genuine"], recs["giving_degenerate"]
    genuine_ok = g["genuine_adicity"] == 3 and {"G", "T", "R"} <= set(g["core"])
    degenerate_ok = d["genuine_adicity"] <= 2
    print("  genuine: adicity=%d core=%s Φ=%.3f | degenerate: adicity=%d core=%s Φ=%.3f"
          % (g["genuine_adicity"], tuple(g["core"]), g["phi_mip"],
             d["genuine_adicity"], tuple(d["core"]), d["phi_mip"]))
    status = "CONFIRMED" if (genuine_ok and degenerate_ok) else ("PARTIAL" if genuine_ok or degenerate_ok else "REFUTED")
    print("H3 (genuine giving adicity 3, degenerate ≤ 2): %s" % status)
    F.save("probe_peirce_giving", {"control": control, "forms": recs, "genuine_ok": genuine_ok,
                                    "degenerate_ok": degenerate_ok, "H3": status})


if __name__ == "__main__":
    main()

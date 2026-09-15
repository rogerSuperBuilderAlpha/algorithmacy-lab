"""Probe — Blau H2: an alternative supplier removes the superior's power.

Question.  Blau (1964: 118): the dependent "may obtain the needed service elsewhere, assuming that there are
           alternative suppliers." Does a second supplier lower the first's advantage and value added?
Hypothesis. H2: advantage(S1) and V(S1) in alternatives are below advantage(S) and V(S) in single.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_alternatives
"""

from org_frontier.thinkers.blau import forms as F


def main():
    print("Blau H2 — one supplier, and an alternative")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("single", "alternatives")}
    a0, a1 = F.advantage(recs["single"], "S"), F.advantage(recs["alternatives"], "S1")
    v0, v1 = recs["single"]["value_added"]["S"], recs["alternatives"]["value_added"]["S1"]
    adv_down, v_down = a1 < a0 - 1e-6, v1 < v0 - 1e-6
    print("  supplier's advantage %.3f -> %.3f (falls: %s)   value added %.3f -> %.3f (falls: %s)" % (
        a0, a1, adv_down, v0, v1, v_down))
    status = "CONFIRMED" if adv_down and v_down else ("PARTIAL" if adv_down or v_down else "REFUTED")
    print("H2 (an alternative supplier removes the superior's power): %s" % status)
    F.save("probe_blau_alternatives", {"control": control, "forms": recs, "advantage": [a0, a1],
                                       "value_added": [v0, v1], "H2": status})


if __name__ == "__main__":
    main()

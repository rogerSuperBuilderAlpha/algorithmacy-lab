"""Probe — Blau H3: organizing the dependent shifts power.

Question.  Blau (1964: 119): the dependent "can coerce him to furnish the service, provided they are capable
           of doing so." Two subordinates who comply only together, against two who comply each alone.
Hypothesis. H3: S's advantage falls and each subordinate's value added rises from unorganized to organized.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_organized
"""

from org_frontier.thinkers.blau import forms as F


def main():
    print("Blau H3 — subordinates alone, and organized")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("unorganized", "organized")}
    a0, a1 = F.advantage(recs["unorganized"], "S"), F.advantage(recs["organized"], "S")
    adv_down = a1 < a0 - 1e-6
    v_up = all(recs["organized"]["value_added"][b] > recs["unorganized"]["value_added"][b] + 1e-6 for b in ("B1", "B2"))
    print("  S's advantage %.3f -> %.3f (falls: %s)   subordinates' V %s -> %s (rise: %s)" % (
        a0, a1, adv_down, [recs["unorganized"]["value_added"][b] for b in ("B1", "B2")],
        [recs["organized"]["value_added"][b] for b in ("B1", "B2")], v_up))
    status = "CONFIRMED" if adv_down and v_up else ("PARTIAL" if adv_down or v_up else "REFUTED")
    print("H3 (organizing the dependent shifts power toward them): %s" % status)
    F.save("probe_blau_organized", {"control": control, "forms": recs, "advantage_S": [a0, a1], "H3": status})


if __name__ == "__main__":
    main()

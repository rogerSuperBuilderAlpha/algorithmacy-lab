"""Probe — Blau H5: opposition mirrors legitimation.

Question.  Blau (1964: 23): "Collective approval of power legitimates that power ... Collective disapproval
           of power engenders opposition." The same shape with the superior's sign reversed. Do the two
           forms have the same structure, and does shared opposition bring the superior to rest where the
           isolated subordinate's does not?
Hypothesis. H5: |core| and core Φ equal for opposition_shared and authority; opposition_shared has a fixed
           point with S yielding (111) and opposition_isolated has none.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_opposition
"""

from org_frontier.thinkers.blau import forms as F


def main():
    print("Blau H5 — legitimation and opposition")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("authority", "opposition_isolated", "opposition_shared")}
    a, o = recs["authority"], recs["opposition_shared"]
    mirror = len(a["core"]) == len(o["core"]) and abs(a["core_phi"] - o["core_phi"]) < 1e-6
    rest = "111" in o["fixed_points"] and not recs["opposition_isolated"]["fixed_points"]
    print("  mirror (same core size and Φ)=%s   shared opposition rests, isolated does not=%s" % (mirror, rest))
    status = "CONFIRMED" if mirror and rest else ("PARTIAL" if mirror or rest else "REFUTED")
    print("H5 (opposition mirrors legitimation; only shared opposition brings the superior to rest): %s" % status)
    F.save("probe_blau_opposition", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()

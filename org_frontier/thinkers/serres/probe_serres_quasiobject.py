"""Probe — Serres H5: the quasi-object weaves the "we".

Question.  Serres (1982: 225): "The quasi-object, when being passed, makes the collective, if it stops, it
           makes the individual." Three players; the token passes round the ring, or it stops.
Hypothesis. H5: passing core = {A, B, C} with Φ > 0; stopped has no complex.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_quasiobject
"""

from org_frontier.thinkers.serres import forms as F


def main():
    print("Serres H5 — the token passing, and the token stopped")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("passing", "stopped")}
    a = set(recs["passing"]["core"]) == {"A", "B", "C"} and recs["passing"]["core_phi"] > 1e-9
    b = not recs["stopped"]["core"]
    print("  passing: all three one complex=%s (Φ=%.3f)   stopped: no complex=%s" % (
        a, recs["passing"]["core_phi"], b))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H5 (the moving token weaves the we; stopped, it marks the I): %s" % status)
    F.save("probe_serres_quasiobject", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()

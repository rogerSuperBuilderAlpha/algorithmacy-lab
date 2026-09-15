"""Probe — Bowen H2: the calm twosome and the outsider; tension involves the third.

Question.  Bowen (1978: 373): "In periods of calm, the triangle is made up of a comfortably close twosome and
           a less comfortable outsider ... The outsider seeks to form a togetherness with one of the twosome."
           Under tension "it 'triangles' a third person" (174). Who is in the major complex, calm and
           triangled?
Hypothesis. H2: calm core = {A, B}; triangled core = {A, B, C}.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_twosome
"""

from org_frontier.thinkers.bowen import forms as F


def main():
    print("Bowen H2 — the calm triangle and the triangled one, no anxiety")
    control = F.run_control()
    recs = {name: F.evaluate(name, 0.0) for name in ("calm", "triangled")}
    calm_ok = set(recs["calm"]["core"]) == {"A", "B"}
    tri_ok = set(recs["triangled"]["core"]) == {"A", "B", "C"}
    print("  calm core is the twosome=%s   triangled core is the triad=%s" % (calm_ok, tri_ok))
    status = "CONFIRMED" if (calm_ok and tri_ok) else "REFUTED"
    print("H2 (calm: twosome with the outsider out; tension: the third is in): %s" % status)
    F.save("probe_bowen_twosome", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()

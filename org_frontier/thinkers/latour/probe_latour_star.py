"""Probe — Latour H5: the actor-network — attachments first, actors second.

Question.  Latour (2005: 217): "an actor-network is what is made to act by a large star-shaped web of
           mediators flowing in and out of it." A center attached to three mediators against the same
           center attached to three intermediaries: is the mediator star a whole of four with higher Φ,
           and where does the intermediary star's core fall?
Hypothesis. H5 (Latour): star_mediators core = all four and Φ(star_mediators) > Φ(star_intermediaries).
Method.    Two forms on (A, M1, M2, M3).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_star
"""

from org_frontier.thinkers.latour import forms as F


def main():
    print("Latour H5 — the star of mediators against the star of intermediaries")
    control = F.run_control()
    recs = {name: F.evaluate(name, rules, F.STAR_LABELS) for name, rules in F.STAR.items()}
    med, inter = recs["star_mediators"], recs["star_intermediaries"]
    all_four = set(med["core"]) == set(F.STAR_LABELS)
    higher = med["phi_mip"] > inter["phi_mip"] + 1e-9
    print("  mediator star binds all four=%s  Φ(mediators) > Φ(intermediaries)=%s  intermediary-star core=%s"
          % (all_four, higher, tuple(inter["core"])))
    if all_four and higher:
        status = "CONFIRMED"
    elif all_four or higher:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H5 (the mediator star is a whole of four and out-integrates the intermediary star): %s" % status)
    F.save("probe_latour_star", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()

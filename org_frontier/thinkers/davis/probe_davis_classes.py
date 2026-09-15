"""Probe — Davis H2: the structural classes follow clusterability, not balance.

Question.  At k = 4, does the instrument sort the four triangles as Davis does — the forbidden ppm alone,
           the three clusterable patterns together?
Hypothesis. H2: ppm has all three persons in its core; ppp, pmm, mmm each fewer than three.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_classes   (~30 min)
"""

from org_frontier.thinkers.davis import forms as F


def main():
    print("Davis H2 — Φ of the four triangles at k = 4")
    control = F.run_control()
    recs = {name: F.evaluate_phi(name, 3, F.TRIAD_EDGES, signs, 4) for name, signs in F.NAMED.items()}
    ppm3 = len(recs["ppm"]["core_persons"]) == 3
    clus = {n: len(recs[n]["core_persons"]) < 3 for n in ("ppp", "pmm", "mmm")}
    print("  ppm all three in core=%s   clusterable patterns fewer than three: %s" % (
        ppm3, " ".join("%s=%s" % kv for kv in clus.items())))
    if ppm3 and all(clus.values()):
        status = "CONFIRMED"
    elif ppm3 or all(clus.values()):
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (the classes follow clusterability): %s" % status)
    F.save("probe_davis_classes", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()

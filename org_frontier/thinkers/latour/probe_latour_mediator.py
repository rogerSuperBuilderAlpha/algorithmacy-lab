"""Probe — Latour H2: the mediator transforms and therefore counts.

Question.  Latour (2005: 39): mediators "transform, translate, distort, and modify"; "their input is never
           a good predictor of their output." Between the same A and B, is a mediator (joint rule, or a
           rule that reads its own state) in the core, and an intermediary (copy) out?
Hypothesis. H2 (Latour): M in both mediator cores; M out of the intermediary core.
Method.    intermediary, mediator_joint, mediator_specific on (A, M, B).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_mediator
"""

from org_frontier.thinkers.latour import forms as F


def main():
    print("Latour H2 — intermediary against two mediators between A and B")
    control = F.run_control()
    recs = {name: F.evaluate(name, rules, F.THIRD_LABELS) for name, rules in F.THIRD.items()}
    med_in = all("M" in recs[n]["core"] for n in ("mediator_joint", "mediator_specific"))
    int_out = "M" not in recs["intermediary"]["core"]
    print("  M in both mediator cores=%s  M out of the intermediary core=%s" % (med_in, int_out))
    if med_in and int_out:
        status = "CONFIRMED"
    elif med_in:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (mediators count, the intermediary does not): %s" % status)
    F.save("probe_latour_mediator", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()

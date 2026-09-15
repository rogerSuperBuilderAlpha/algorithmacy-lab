"""Probe — Girard H4: distance.

Question.  Girard (1965: 9): "we have only to vary the distance, in the triangle, separating the mediator
           from the desiring subject." The mediator reads the subject with probability p per step and
           otherwise holds his own desire. Does the core's Φ rise as he draws near, and does the object
           ever enter?
Hypothesis. H4: core Φ strictly increasing over p = 0.25, 0.5, 0.75, 1; O in the core at no p > 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_distance
"""

from org_frontier.thinkers.girard import forms as F


def main():
    print("Girard H4 — the mediator draws nearer")
    control = F.run_control(stochastic=True)
    recs = [F.evaluate_distance(p) for p in F.PS]
    pos = recs[1:]
    phis = [r["core_phi"] if "M" in r["core"] and "S" in r["core"] else 0.0 for r in pos]
    rising = all(phis[i] < phis[i + 1] - 1e-9 for i in range(len(phis) - 1))
    o_never = all("O" not in r["core"] for r in pos)
    print("  core Φ over p>0: %s  strictly rising=%s   O in core at any p>0: %s" % (
        ", ".join("%.3f" % x for x in phis), rising, not o_never))
    n = int(rising) + int(o_never)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H4 (the nearer the mediator, the tighter the pair; the object never enters): %s" % status)
    F.save("probe_girard_distance", {"control": control, "sweep": recs, "H4": status})


if __name__ == "__main__":
    main()

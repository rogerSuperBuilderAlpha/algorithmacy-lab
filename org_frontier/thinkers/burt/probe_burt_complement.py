"""Probe — Burt H5: closure within, brokerage beyond.

Question.  Burt (2000; 2001: 31; 2005): "brokerage across structural holes is the source of value added, but
           closure can be critical to realizing the value buried in structural holes" — social capital is
           "closure within a group and brokerage beyond the group." Broker E in {E, A1, A2} with outsider O:
           is V(E) highest with the group closed and the hole to O open?
Hypothesis. H5 (Burt): V(E | within) > V(E | open), V(E | across), V(E | everywhere).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_complement
"""

from org_frontier.thinkers.burt import forms as F


def main():
    print("Burt H5 — where the broker adds most: open, closure within, closure across, closure everywhere")
    control = F.run_control()
    recs = {name: F.evaluate(name, sp) for name, sp in F.h5_forms().items()}
    V = {k: r["value_added"] for k, r in recs.items()}
    others = [V[k] for k in ("open", "across", "everywhere")]
    strict = all(V["within"] > o + 1e-9 for o in others)
    tied = (not strict) and all(V["within"] >= o - 1e-9 for o in others)
    print("  V(E): " + "  ".join("%s=%.3f" % (k, v) for k, v in V.items()))
    status = "CONFIRMED" if strict else ("PARTIAL" if tied else "REFUTED")
    print("H5 (closure within the group and a hole beyond it maximizes the broker's value added): %s" % status)
    F.save("probe_burt_complement", {"control": control, "forms": recs, "V": V, "H5": status})


if __name__ == "__main__":
    main()

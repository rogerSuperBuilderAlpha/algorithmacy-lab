"""Probe — Granovetter H3: the bridge.

Question.  Granovetter (1973: 1364): a bridge is "the only path between two points" and "all bridges are weak
           ties." Two strong dyads joined by one tie: does a weak bridge do what a strong one does — same
           transmission, and a major complex spanning both dyads?
Hypothesis. H3: transmission equal (12 pairs) and the core spans both dyads under both bridges.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_bridge
"""

from org_frontier.thinkers.granovetter import forms as F

fs = frozenset
LABELS = ("a1", "a2", "b1", "b2")


def bridge(p):
    return F.graph(LABELS, {fs({"a1", "a2"}): F.STRONG, fs({"b1", "b2"}): F.STRONG, fs({"a2", "b1"}): p})


def spans(core):
    c = set(core)
    return bool(c & {"a1", "a2"}) and bool(c & {"b1", "b2"})


def main():
    print("Granovetter H3 — two strong dyads joined by a weak bridge, then by a strong one")
    control = F.run_control()
    recs = {}
    for name, p in (("bridge_weak", F.WEAK), ("bridge_strong", F.STRONG)):
        lab, ties = bridge(p)
        recs[name] = F.evaluate(name, lab, ties)
    same_reach = recs["bridge_weak"]["reach_pairs"] == recs["bridge_strong"]["reach_pairs"] == 12
    sw, ss = spans(recs["bridge_weak"]["core"]), spans(recs["bridge_strong"]["core"])
    print("  transmission equal at 12=%s  core spans both dyads: weak=%s strong=%s" % (same_reach, sw, ss))
    if same_reach and sw and ss:
        status = "CONFIRMED"
    elif ss:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H3 (a weak bridge joins the two dyads as a strong one does): %s" % status)
    F.save("probe_granovetter_bridge", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()

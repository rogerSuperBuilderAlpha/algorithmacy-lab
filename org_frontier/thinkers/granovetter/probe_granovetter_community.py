"""Probe — Granovetter H5: local cohesion, overall fragmentation.

Question.  Granovetter (1973: 1373–1378): a community "completely partitioned into cliques" is fragmented
           at the macro level though cohesive locally; weak ties between cliques integrate it. Three strong
           dyads: isolated, joined by weak ties in a chain, in a ring, and by strong ties in a ring — where
           is the major complex?
Hypothesis. H5: chain and ring both have a major complex spanning all three dyads.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_community
"""

from org_frontier.thinkers.granovetter import forms as F

fs = frozenset
LABELS = ("a1", "a2", "b1", "b2", "c1", "c2")
DYADS = {fs({"a1", "a2"}): F.STRONG, fs({"b1", "b2"}): F.STRONG, fs({"c1", "c2"}): F.STRONG}


def spans_all(core):
    c = set(core)
    return all(bool(c & d) for d in ({"a1", "a2"}, {"b1", "b2"}, {"c1", "c2"}))


def main():
    print("Granovetter H5 — three strong dyads: isolated, weak chain, weak ring, strong ring")
    control = F.run_control()
    forms = {
        "isolated": dict(DYADS),
        "chain": {**DYADS, fs({"a2", "b1"}): F.WEAK, fs({"b2", "c1"}): F.WEAK},
        "ring": {**DYADS, fs({"a2", "b1"}): F.WEAK, fs({"b2", "c1"}): F.WEAK, fs({"c2", "a1"}): F.WEAK},
        "strong_ring": {**DYADS, fs({"a2", "b1"}): F.STRONG, fs({"b2", "c1"}): F.STRONG, fs({"c2", "a1"}): F.STRONG},
    }
    recs = {}
    for name, t in forms.items():
        lab, ties = F.graph(LABELS, t)
        recs[name] = F.evaluate(name, lab, ties)
    sc, sr = spans_all(recs["chain"]["core"]), spans_all(recs["ring"]["core"])
    print("  core spans all three dyads: chain=%s ring=%s strong_ring=%s" % (sc, sr, spans_all(recs["strong_ring"]["core"])))
    status = "CONFIRMED" if (sc and sr) else ("PARTIAL" if sr else "REFUTED")
    print("H5 (weak ties between cliques make the community one whole): %s" % status)
    F.save("probe_granovetter_community", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()

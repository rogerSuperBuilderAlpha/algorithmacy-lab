"""Probe — Latour H3: the actor is whatever makes a difference.

Question.  Latour (2005: 71): "any thing that does modify a state of affairs by making a difference is an
           actor ... Does it make a difference in the course of some other agent's action or not?" Is the
           set of nodes that make a difference to another node's next state the same as the major complex?
Hypothesis. H3 (Latour): membership = difference-making.
Method.    source (S' = S; M' = S∧A; A' = M), spectator (S' = M; M' = A; A' = M), control. Boolean influence
           > 0 on some other rule = makes a difference.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_difference
"""

from org_frontier.thinkers.latour import forms as F


def main():
    print("Latour H3 — making a difference against membership in the core")
    control = F.run_control()
    recs = {name: F.evaluate(name, rules, F.DIFF_LABELS) for name, rules in F.DIFF.items()}
    differ_not_in, in_not_differ = [], []
    for name, r in recs.items():
        d, c = set(r["makes_difference"]), set(r["core"])
        differ_not_in += ["%s:%s" % (name, x) for x in sorted(d - c)]
        in_not_differ += ["%s:%s" % (name, x) for x in sorted(c - d)]
    print("  make a difference but out of the core: %s | in the core but make no difference: %s"
          % (",".join(differ_not_in) or "none", ",".join(in_not_differ) or "none"))
    status = "CONFIRMED" if not differ_not_in and not in_not_differ else "REFUTED"
    print("H3 (a node is in the core iff it makes a difference to another): %s" % status)
    F.save("probe_latour_difference", {"control": control, "forms": recs, "differ_not_in": differ_not_in,
                                        "in_not_differ": in_not_differ, "H3": status})


if __name__ == "__main__":
    main()

"""Probe — Burt H2: structural equivalence is redundancy without a tie.

Question.  Burt (1992: 19): contacts with the same contacts "lead to the same sources of information and so
           are redundant" — "one nonredundant contact at a cost of maintaining three." Two contacts reading
           one source Z against two contacts reading different sources: are the equivalent contacts one
           member or two, and does E add more than it adds with a single contact?
Hypothesis. H2 (Burt): equivalent -> at most one of X, Y in the core and V(E) <= V(E | single);
           nonredundant -> both in the core.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_equivalence
"""

from org_frontier.thinkers.burt import forms as F


def main():
    print("Burt H2 — structurally equivalent contacts against nonredundant contacts")
    control = F.run_control()
    recs = {name: F.evaluate(name, sp) for name, sp in F.h2_forms().items()}
    eq_core = set(recs["equivalent"]["core"])
    evicted = len(eq_core & {"X", "Y"}) <= 1
    at_single = recs["equivalent"]["value_added"] <= recs["single"]["value_added"] + 1e-6
    both_nonred = {"X", "Y"} <= set(recs["nonredundant"]["core"])
    print("  equivalent: at most one of X,Y in core=%s  V(E) at single-contact value=%s | nonredundant: both in core=%s"
          % (evicted, at_single, both_nonred))
    if evicted and at_single and both_nonred:
        status = "CONFIRMED"
    elif (evicted or at_single) and both_nonred:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (structurally equivalent contacts count as one; nonredundant contacts as two): %s" % status)
    F.save("probe_burt_equivalence", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()

"""Probe — Coleman H4: the rotating-credit association is one unit.

Question.  Coleman (1988: S102–S103): each of n members contributes and in turn receives; "a person who
           receives a payout early ... could abscond and leave the others with a loss." A ring of four who
           each pay when paid, against two bilateral credit pairs.
Hypothesis. H4: ring4 is one complex of four, all V equal and positive; two_dyads has no complex of more
           than two.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_credit
"""

from org_frontier.thinkers.coleman import forms as F


def main():
    print("Coleman H4 — the ring of credit, and bilateral credit")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("ring4", "two_dyads")}
    r = recs["ring4"]
    vals = list(r["value_added"].values())
    ring_ok = set(r["core"]) == {"A", "B", "C", "D"} and r["core_phi"] > 1e-9 \
        and all(abs(v - vals[0]) < 1e-9 for v in vals) and vals[0] > 1e-9
    dyads_ok = len(recs["two_dyads"]["core"]) <= 2
    print("  ring: complex of four with equal positive V=%s   dyads: no complex above two=%s" % (ring_ok, dyads_ok))
    if ring_ok and dyads_ok:
        status = "CONFIRMED"
    elif ring_ok:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H4 (the association is one unit and every member is necessary to it): %s" % status)
    F.save("probe_coleman_credit", {"control": control, "forms": recs, "H4": status})


if __name__ == "__main__":
    main()

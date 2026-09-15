"""Probe — Burt H4: a hole at your own end — the rival broker.

Question.  Burt (1992: 45): autonomy needs "numerous structural holes around your contacts and none attached
           to yourself"; a contact's "secondary structural holes ... others outside the network who could
           replace the contact." A second broker R reading the same two contacts and read by them: does E's
           value added fall, and are E and R both in the core?
Hypothesis. H4 (Burt): V(E | rival) < V(E | alone) and not both E and R in the core.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_rival
"""

from org_frontier.thinkers.burt import forms as F


def main():
    print("Burt H4 — the broker alone against the broker with a rival spanning the same hole")
    control = F.run_control()
    forms = F.h4_forms()
    recs = {name: F.evaluate(name, sp) for name, sp in forms.items()}
    recs["rival_R"] = F.evaluate("rival_R", forms["rival"], party="R")
    drop = recs["rival"]["value_added"] < recs["alone"]["value_added"] - 1e-9
    not_both = not ({"E", "R"} <= set(recs["rival"]["core"]))
    print("  V(E) falls with the rival=%s  not both brokers in the core=%s  (rival core=%s)"
          % (drop, not_both, tuple(recs["rival"]["core"])))
    n = int(drop) + int(not_both)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H4 (a rival spanning the same hole erodes the broker's autonomy): %s" % status)
    F.save("probe_burt_rival", {"control": control, "forms": recs, "H4": status})


if __name__ == "__main__":
    main()

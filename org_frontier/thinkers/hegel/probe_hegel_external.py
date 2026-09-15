"""Probe — Hegel H2: the external middle connects without uniting.

Question.  Hegel: the formal syllogism's middle is "only the abstract particularity," "rational but
           non-conceptual" (EL §182); communication passes a determinateness "without transition into the
           opposite" (SL 635), spreading "like a scent" (635–636). Relay (A→M→B) and broadcast (A→M, A→B),
           A staying what it was: connected, and one?
Hypothesis. H2: both have Φ = 0 and no complex containing M, with B reachable from A.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_external
"""

from org_frontier.thinkers.hegel import forms as F


def main():
    print("Hegel H2 — communication and scent: the middle that relays")
    control = F.run_control()
    recs, ok = {}, []
    for name in ("communication", "scent"):
        recs[name] = F.evaluate(name)
        reach = F.reachable_from(F.SPECS[name], "A")
        recs[name]["reachable_from_A"] = reach
        cond = recs[name]["phi_mip"] < 1e-9 and "M" not in recs[name]["core"] and "B" in reach
        ok.append(cond)
        print("    %s: reachable from A=%s  Φ=0 and M in no complex=%s" % (name, reach, cond))
    status = "CONFIRMED" if all(ok) else "REFUTED"
    print("H2 (the relaying middle connects the terms and unites none of them): %s" % status)
    F.save("probe_hegel_external", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()

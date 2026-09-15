"""Probe — Hegel H5: the process of alternating middle terms.

Question.  Hegel's "runs through the determination of the middle term and the extreme" (SL 642–643), read
           as process (Moss 2013): each term is middle in turn, by a three-phase clock. Is the rotating
           triad a whole of three with the clock outside, and does its Φ reach the simultaneous system's?
Hypothesis. H5: core = {A, B, C}; Φ(rotating) = Φ(system).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_rotating
"""

from org_frontier.thinkers.hegel import forms as F


def main():
    print("Hegel H5 — the rotating middle against the fixed middle and the simultaneous system")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("syllogism", "system")}
    recs["rotating"] = F.evaluate_rules("rotating", F.ROT_LABELS, F.ROT_RULES)
    core_ok = set(recs["rotating"]["core"]) == {"A", "B", "C"}
    pr, ps, py = recs["rotating"]["phi_mip"], recs["system"]["phi_mip"], recs["syllogism"]["phi_mip"]
    eq_system = abs(pr - ps) < 1e-6
    print("  rotating core is {A,B,C}=%s   Φ rotating=%.3f  system=%.3f  syllogism=%.3f  rotating=system:%s" % (
        core_ok, pr, ps, py, eq_system))
    if core_ok and eq_system:
        status = "CONFIRMED"
    elif core_ok:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H5 (the alternation of middles is the totality): %s" % status)
    F.save("probe_hegel_rotating", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()

"""Probe — Serres H2: noise gives rise to a new system.

Question.  Serres (1982: 14): "Theorem: noise gives rise to a new system, an order that is more complex than
           the simple chain." Farmer → tax farmer → rat, then the noise the feast provokes and that stops
           the feast. Does a complex appear, and who is in it?
Hypothesis. H2: chain has no complex; chain_noise has one containing N and excluding F and T.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_theorem
"""

from org_frontier.thinkers.serres import forms as F


def main():
    print("Serres H2 — the chain, and the chain interrupted")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("chain", "chain_noise")}
    none_before = not recs["chain"]["core"]
    core = set(recs["chain_noise"]["core"])
    with_n = "N" in core and recs["chain_noise"]["core_phi"] > 1e-9
    upper_out = not (core & {"F", "T"})
    print("  chain has no complex=%s   noise in the new complex=%s   F and T outside it=%s" % (
        none_before, with_n, upper_out))
    if none_before and with_n and upper_out:
        status = "CONFIRMED"
    elif none_before and with_n:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (noise gives rise to a new system): %s" % status)
    F.save("probe_serres_theorem", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()

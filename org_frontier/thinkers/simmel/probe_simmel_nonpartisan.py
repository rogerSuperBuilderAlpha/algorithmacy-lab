"""Probe — Simmel H4: the nonpartisan as mediator or arbitrator.

Question.  Simmel (1902, II) splits the nonpartisan third into the mediator, who conveys objectified
           claims while the parties keep the decision and "seeks to eliminate himself," and the arbitrator, in
           whom the decision "has become a person." Does the scale arbitrator → mediator → self-eliminated
           mediator read as in, in (weaker), out?
Hypothesis. H4 (Simmel): M ∈ core(arbitrator), M ∈ core(mediator), M ∉ core(mediator_eliminated), and
           Φ_arb > Φ_med > 0.
Method.    Exact Φ_MIP and major complex on the three forms in methods.md (H4).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_nonpartisan
"""

from org_frontier.thinkers.simmel import forms as F


def main():
    print("Simmel H4 — the nonpartisan scale")
    control = F.run_control()
    recs = {name: F.evaluate(name, form) for name, form in [
        ("arbitrator", F.ARBITRATOR), ("mediator", F.MEDIATOR),
        ("mediator_eliminated", F.MEDIATOR_ELIMINATED)]}
    m_in = {k: "M" in v["core"] for k, v in recs.items()}
    membership_ok = m_in["arbitrator"] and m_in["mediator"] and not m_in["mediator_eliminated"]
    ordering_ok = recs["arbitrator"]["phi_mip"] > recs["mediator"]["phi_mip"] > 0
    for k, v in m_in.items():
        print("  M in core of %-20s %s" % (k, v))
    if membership_ok and ordering_ok:
        status = "CONFIRMED"
    elif membership_ok or (m_in["arbitrator"] and not m_in["mediator_eliminated"]):
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H4 (arbitrator in, mediator in but weaker, eliminated mediator out): %s" % status)
    F.save("probe_simmel_nonpartisan", {"control": control, "forms": recs, "M_in_core": m_in,
                                        "membership_ok": membership_ok, "ordering_ok": ordering_ok, "H4": status})


if __name__ == "__main__":
    main()

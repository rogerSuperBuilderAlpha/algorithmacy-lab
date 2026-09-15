"""Probe — Hegel H1: the middle founds the connection.

Question.  Hegel: "everything rational is a syllogism" (SL 588); the syllogism is "the essential ground of
           everything true" (EL §181R). Is the middle in the core and necessary, and is the syllogism more
           integrated than the judgment (two terms, no middle)?
Hypothesis. H1: (a) M in core; delete M → Φ = 0. (b) Φ(syllogism) > Φ(judgment).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_middle
"""

from org_frontier.thinkers.hegel import forms as F


def main():
    print("Hegel H1 — the judgment, the syllogism, and the syllogism without its middle")
    control = F.run_control()
    recs = {"judgment": F.evaluate("judgment"), "syllogism": F.evaluate("syllogism")}
    recs["syllogism_minus_M"] = F.evaluate("syllogism_minus_M", F.delete(F.SPECS["syllogism"], "M"))
    m_in = "M" in recs["syllogism"]["core"]
    m_needed = recs["syllogism_minus_M"]["phi_mip"] < 1e-9 and not recs["syllogism_minus_M"]["core"]
    more = recs["syllogism"]["phi_mip"] > recs["judgment"]["phi_mip"] + 1e-9
    equal = abs(recs["syllogism"]["phi_mip"] - recs["judgment"]["phi_mip"]) < 1e-9
    print("  M in core=%s  M necessary=%s  Φ(syllogism)=%.3f vs Φ(judgment)=%.3f  syllogism more=%s" % (
        m_in, m_needed, recs["syllogism"]["phi_mip"], recs["judgment"]["phi_mip"], more))
    if m_in and m_needed and more:
        status = "CONFIRMED"
    elif m_in and m_needed and equal:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H1 (the middle is necessary, and the syllogism outbinds the judgment): %s" % status)
    F.save("probe_hegel_middle", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()

"""Probe — Hegel H4: the system of three syllogisms has no distinguished binder.

Question.  Hegel: free mechanism is the totality of "the syllogisms in which each of the three different
           objects runs through the determination of the middle term and the extreme" (SL 642–643); "the
           state is a system of three syllogisms" (EL §198R). Shares — what each term's removal costs — in
           the single syllogism and in the system where every term is middle to the other two.
Hypothesis. H4: syllogism shares (A 0, M 2, B 0); system shares equal and positive.
           Descriptive: Φ(system) against the sum of three syllogisms' Φ.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_system
"""

from org_frontier.thinkers.hegel import forms as F


def main():
    print("Hegel H4 — the single syllogism and the system of three")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("syllogism", "system")}
    sh = {name: F.shares(name) for name in ("syllogism", "system")}
    s_syl = sh["syllogism"]
    a = abs(s_syl["A"]) < 1e-9 and abs(s_syl["B"]) < 1e-9 and abs(s_syl["M"] - 2.0) < 1e-9
    vals = list(sh["system"].values())
    b = max(vals) - min(vals) < 1e-9 and min(vals) > 1e-9
    three = 3 * recs["syllogism"]["phi_mip"]
    additive = abs(recs["system"]["phi_mip"] - three) < 1e-9
    print("  syllogism shares (0,2,0)=%s   system shares equal & positive=%s   Φ(system)=%.3f vs 3×Φ(syllogism)=%.3f (equal=%s)" % (
        a, b, recs["system"]["phi_mip"], three, additive))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H4 (the fixed middle bears the whole; in the system every term bears an equal share): %s" % status)
    F.save("probe_hegel_system", {"control": control, "forms": recs, "shares": sh,
                                  "descriptive_additive": additive, "H4": status})


if __name__ == "__main__":
    main()

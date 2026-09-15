"""Probe — Simmel H5: the tertius gaudens and the balance of forces.

Question.  Simmel (1902, II): the third's leverage is "determined exclusively by the relationship
           which the energies of the parties exhibit toward each other"; when they are equal "a minimum of
           addition often suffices." Holding every rule fixed but the weights, does the third's core
           membership track the contestants' balance?
Hypothesis. H5 (Simmel): T ∈ core(balanced), T ∉ core(dictator); T's influence and membership are monotone
           non-increasing from balanced to intermediate to dictator.
Method.    Four nodes A, B, T, O; O' = [w_A·A + w_T·T > w_B·B + w_T·(1−T)]; A'=B'=T'=O. Weights per
           methods.md (H5). Exact Φ_MIP, major complex, and T's Boolean influence on O'.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_gaudens
"""

from org_frontier.thinkers.simmel import forms as F


def main():
    print("Simmel H5 — the tertius gaudens and the balance of forces")
    control = F.run_control()
    recs = {}
    for regime, w in F.GAUDENS_REGIMES.items():
        labels, rules = F.gaudens(*w)
        rec = F.evaluate("gaudens_" + regime, (labels, rules))
        rec["weights"] = list(w)
        rec["influence_T_on_O"] = F.influence(rules[3], 4, 2)
        rec["influence_A_on_O"] = F.influence(rules[3], 4, 0)
        rec["influence_B_on_O"] = F.influence(rules[3], 4, 1)
        rec["T_in_core"] = "T" in rec["core"]
        print("    weights=%s  infl(T)=%.3f infl(A)=%.3f infl(B)=%.3f  T in core: %s"
              % (w, rec["influence_T_on_O"], rec["influence_A_on_O"], rec["influence_B_on_O"], rec["T_in_core"]))
        recs[regime] = rec
    order = ["balanced", "intermediate", "dictator"]
    infl = [recs[r]["influence_T_on_O"] for r in order]
    memb = [int(recs[r]["T_in_core"]) for r in order]
    ends_ok = recs["balanced"]["T_in_core"] and not recs["dictator"]["T_in_core"]
    mono_ok = all(a >= b for a, b in zip(infl, infl[1:])) and all(a >= b for a, b in zip(memb, memb[1:]))
    status = "CONFIRMED" if (ends_ok and mono_ok) else ("PARTIAL" if ends_ok else "REFUTED")
    print("H5 (third's membership tracks the contestants' balance): %s" % status)
    F.save("probe_simmel_gaudens", {"control": control, "forms": recs, "ends_ok": ends_ok, "mono_ok": mono_ok,
                                    "H5": status})


if __name__ == "__main__":
    main()

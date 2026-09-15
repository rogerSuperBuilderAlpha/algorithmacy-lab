"""Probe — Bowen H5: detriangling.

Question.  Bowen (1978: 174–175): a tense twosome in contact with a third who stays emotionally detached yet
           in good contact finds its tension resolving. A third read by both insiders and reading both:
           reactive (C' = A ∧ B) or neutral (C' = C). Is the neutral third outside the complex, and does its
           presence let the twosome hold more of its Φ under anxiety than the bare dyad?
Hypothesis. H5: (a) neutral C is outside the core, reactive C inside; (b) with a neutral third the insiders'
           complex retains a larger fraction than the dyad at every ε > 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_detriangle
"""

from org_frontier.thinkers.bowen import forms as F


def main():
    print("Bowen H5 — reactive third, neutral third, bare dyad, under uniform anxiety")
    control = F.run_control()
    r0 = {name: F.evaluate(name, 0.0) for name in ("reactive_third", "neutral_third")}
    a = ("C" not in r0["neutral_third"]["core"]) and ("C" in r0["reactive_third"]["core"])
    print("  reactive core=%s  neutral core=%s  neutral out & reactive in=%s" % (
        tuple(r0["reactive_third"]["core"]), tuple(r0["neutral_third"]["core"]), a))
    sweep = {"dyad": [], "neutral_third": []}
    base = {}
    for name in sweep:
        base[name] = r0[name]["core_phi"] if name in r0 else F.evaluate(name, 0.0)["core_phi"]
        for e in F.EPS:
            r = F.evaluate(name, e)
            r["core_fraction"] = round(r["core_phi"] / base[name], 6) if base[name] else None
            sweep[name].append(r)
    b_each = [sweep["neutral_third"][i]["core_fraction"] > sweep["dyad"][i]["core_fraction"] + 1e-9 for i in range(1, len(F.EPS))]
    b = all(b_each)
    print("  insiders' complex retains more with a neutral third than the bare dyad at ε>0: %s   (core fractions neutral: %s | dyad: %s)" % (
        "".join("Y" if x else "n" for x in b_each),
        " ".join("%.3f" % r["core_fraction"] for r in sweep["neutral_third"][1:]),
        " ".join("%.3f" % r["core_fraction"] for r in sweep["dyad"][1:])))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H5 (the neutral third is out of the unit and its presence steadies the twosome): %s" % status)
    F.save("probe_bowen_detriangle", {"control": control, "membership": r0, "base_core_phi": base,
                                      "sweep": sweep, "H5": status})


if __name__ == "__main__":
    main()

"""Probe — Peirce H4: the sign relation.

Question.  Peirce (CP 2.274, 5.484): sign, object, and interpretant are "bound together" in a genuine
           triadic relation, a "tri-relative influence not being in any way resolvable into actions
           between pairs." With the dynamical object exogenous (O'=O), S'=O, I'=(S↔O): is there an
           adicity-3 distinction, and are all three in one complex?
Hypothesis. H4 (Peirce): yes and yes. Lab prior: the exogenous object is never in the core (probe 5); the
           pragmatic-feedback form O'=I is run as the comparison.
Method.    genuine_adicity, whole Φ, and major complex on the two forms in methods.md (H4).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_sign
"""

from org_frontier.thinkers.peirce import forms as F


def main():
    print("Peirce H4 — the sign relation")
    control = F.run_control()
    recs = {name: F.evaluate(name, form) for name, form in [
        ("sign_exogenous", F.SIGN_EXOGENOUS), ("sign_pragmatic", F.SIGN_PRAGMATIC)]}
    ex, pr = recs["sign_exogenous"], recs["sign_pragmatic"]
    ex_full = ex["genuine_adicity"] == 3 and set(ex["core"]) == {"O", "S", "I"}
    pr_full = pr["genuine_adicity"] == 3 and set(pr["core"]) == {"O", "S", "I"}
    print("  exogenous: adicity=%d core=%s Φ=%.3f | pragmatic: adicity=%d core=%s Φ=%.3f"
          % (ex["genuine_adicity"], tuple(ex["core"]), ex["phi_mip"],
             pr["genuine_adicity"], tuple(pr["core"]), pr["phi_mip"]))
    if ex_full:
        status = "CONFIRMED"
    elif ex["genuine_adicity"] == 3 or pr_full:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H4 (sign relation binds O, S, I at adicity 3 with the object exogenous): %s" % status)
    F.save("probe_peirce_sign", {"control": control, "forms": recs, "exogenous_full": ex_full,
                                  "pragmatic_full": pr_full, "H4": status})


if __name__ == "__main__":
    main()

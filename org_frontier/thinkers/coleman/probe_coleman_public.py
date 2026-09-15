"""Probe — Coleman H5: the public good.

Question.  Coleman (1988: S119): "the actor or actors who generate social capital ordinarily capture only a
           small part of its benefits." B closes the B–C tie. How much of the core's gain does B capture?
Hypothesis. H5: gain = coreΦ_closed − coreΦ_open > 0 and (V_B,closed − V_B,open) / gain < 1.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_public
"""

from org_frontier.thinkers.coleman import forms as F


def main():
    print("Coleman H5 — who captures the gain from closure")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("norm_open", "norm_closed")}
    o, c = recs["norm_open"], recs["norm_closed"]
    gain = round(c["core_phi"] - o["core_phi"], 6)
    dB = round(c["value_added"]["B"] - o["value_added"]["B"], 6)
    frac = round(dB / gain, 6) if abs(gain) > 1e-9 else None
    print("  core Φ gain from closure=%.3f   ΔV(B)=%.3f   B's captured fraction=%s" % (
        gain, dB, "%.3f" % frac if frac is not None else "undefined"))
    if gain > 1e-6 and frac is not None and frac < 1 - 1e-6:
        status = "CONFIRMED"
    elif gain > 1e-6:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H5 (the closer captures less than the whole gains): %s" % status)
    F.save("probe_coleman_public", {"control": control, "forms": recs, "gain": gain, "dV_B": dB,
                                    "captured_fraction": frac, "H5": status})


if __name__ == "__main__":
    main()

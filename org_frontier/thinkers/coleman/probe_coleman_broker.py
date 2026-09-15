"""Probe — Coleman H2: closure is the collective's gain, not the broker's (against Burt H1).

Question.  The Burt paper found closure removes the broker's value added. Coleman (1988: S119): social
           capital is a public good — "the actor or actors who generate social capital ordinarily capture
           only a small part of its benefits." On Burt's own forms, does closure raise the core's Φ while
           lowering the broker's positional advantage?
Hypothesis. H2: for both brokers coreΦ_closed ≥ coreΦ_open and advantage_closed < advantage_open.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_broker
"""

from org_frontier.thinkers.burt import forms as B
from org_frontier.thinkers.coleman import forms as F


def main():
    print("Coleman H2 — Burt's brokers, read for the collective")
    control = F.run_control()
    forms = B.h1_forms()
    recs = {name: B.evaluate(name, sp) for name, sp in forms.items()}
    checks = {}
    for broker in ("info", "control"):
        o, c = recs["%s_open" % broker], recs["%s_closed" % broker]
        checks[broker] = {"phi_up": c["core_phi"] >= o["core_phi"] - 1e-6,
                          "adv_down": c["advantage"] < o["advantage"] - 1e-6,
                          "core_phi": [o["core_phi"], c["core_phi"]], "advantage": [o["advantage"], c["advantage"]]}
        print("  %-8s coreΦ open→closed %.3f→%.3f (≥: %s)   advantage of E %.3f→%.3f (<: %s)" % (
            broker, o["core_phi"], c["core_phi"], checks[broker]["phi_up"],
            o["advantage"], c["advantage"], checks[broker]["adv_down"]))
    full = [b for b in checks if checks[b]["phi_up"] and checks[b]["adv_down"]]
    if len(full) == 2:
        status = "CONFIRMED"
    elif len(full) == 1 or all(checks[b]["adv_down"] for b in checks) or all(checks[b]["phi_up"] for b in checks):
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (closure raises the whole and lowers the broker): %s" % status)
    F.save("probe_coleman_broker", {"control": control, "forms": recs, "checks": checks, "H2": status})


if __name__ == "__main__":
    main()

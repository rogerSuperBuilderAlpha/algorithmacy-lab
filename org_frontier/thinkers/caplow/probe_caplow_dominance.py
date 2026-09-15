"""Probe — Caplow H3: when A ≥ B + C, no coalition against A.

Question.  Caplow (1956 on Types 4, 6; 1959 on Types 7, 8): "true coalition is impossible" when A exceeds
           B and C combined; at equality BC "can block the dominance of A" but "is not sufficient to control
           the situation." Does BC ever bind in Types 4, 6, 7, 8, and is A in every core?
Hypothesis. H3 (Caplow): BC never binds; A is in the core of every coalition form and every precoalition form.
Method.    Types 4, 6, 7, 8: three coalition forms and the precoalition form each.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_dominance
"""

from org_frontier.thinkers.caplow import forms as F

TYPES = [4, 6, 7, 8]


def main():
    print("Caplow H3 — A ≥ B + C: Types 4, 6, 7, 8")
    control = F.run_control()
    recs = F.evaluate_types(TYPES)
    bc_binds = [k for k in TYPES if recs["t%d_BC" % k]["binds"]]
    a_out = [name for name, r in recs.items() if "A" not in r["core"]]
    print("  BC binds in types: %s   forms with A out of the core: %s"
          % (",".join(map(str, bc_binds)) or "none", ",".join(a_out) or "none"))
    if not bc_binds and not a_out:
        status = "CONFIRMED"
    elif not bc_binds:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H3 (BC never binds and A holds every core when A ≥ B + C): %s" % status)
    F.save("probe_caplow_dominance", {"control": control, "forms": recs, "bc_binds": bc_binds,
                                       "a_out": a_out, "H3": status})


if __name__ == "__main__":
    main()

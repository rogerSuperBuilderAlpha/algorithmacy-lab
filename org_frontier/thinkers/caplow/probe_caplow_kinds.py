"""Probe — Caplow H4: conservative, revolutionary, improper (Type 5).

Question.  Caplow (1968): in Type 5 (A > B > C, A < B + C) every pair wins; AB is conservative, BC
           revolutionary, AC improper. Under A.2 both partners gain control over the isolate. Are both
           partners in the core in each, and does BC alone remove A from the core?
Hypothesis. H4 (Caplow): all three bind; A out under BC, in under AB and AC.
Method.    Type 5 forms (4, 3, 2) plus the precoalition form.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_kinds
"""

from org_frontier.thinkers.caplow import forms as F

KIND = {"AB": "conservative", "BC": "revolutionary", "AC": "improper"}


def main():
    print("Caplow H4 — Type 5: conservative AB, revolutionary BC, improper AC")
    control = F.run_control()
    recs = F.evaluate_types([5])
    for p in F.PAIRS:
        r = recs["t5_%s" % p]
        print("  %-13s %s: core=%s  A in core: %s  partners both in core: %s"
              % (KIND[p], p, tuple(r["core"]), "A" in r["core"], r["binds"]))
    all_bind = all(recs["t5_%s" % p]["binds"] for p in F.PAIRS)
    a_pattern = ("A" not in recs["t5_BC"]["core"] and "A" in recs["t5_AB"]["core"] and "A" in recs["t5_AC"]["core"])
    if all_bind and a_pattern:
        status = "CONFIRMED"
    elif a_pattern:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H4 (all three Type 5 coalitions bind; only BC removes A from the core): %s" % status)
    F.save("probe_caplow_kinds", {"control": control, "forms": recs, "all_bind": all_bind,
                                   "a_pattern": a_pattern, "H4": status})


if __name__ == "__main__":
    main()

"""Probe — Caplow H1: power predicts the coalition.

Question.  Caplow (1956, 1959): the initial distribution of power predicts which pair coalesces, across
           eight types. Rendered by his own assumptions (stronger controls weaker within the bloc; strength
           additive; members read the outcome), is the set of coalitions that BIND — both partners in the
           major complex — the set Caplow predicts, type by type?
Hypothesis. H1 (Caplow): yes in all eight. Lab prior: no where the prediction rests on the weaker member's
           wish to control the isolate (Types 3, 5, 7, 8), since the controlled partner is unread.
Method.    24 coalition forms + 8 precoalition forms; verdict, major complex, binds.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_types
"""

from org_frontier.thinkers.caplow import forms as F


def main():
    print("Caplow H1 — power predicts the coalition: eight types, three coalitions each")
    control = F.run_control()
    recs = F.evaluate_types()
    matches = {}
    for k, (w, predicted) in F.TYPES.items():
        binding = {p for p in F.PAIRS if recs["t%d_%s" % (k, p)]["binds"]}
        matches[k] = {"predicted": sorted(predicted), "binding": sorted(binding), "match": binding == predicted}
        print("  type %d w=%-9s Caplow predicts %-14s binding %-14s %s"
              % (k, tuple(w), ",".join(sorted(predicted)) or "none", ",".join(sorted(binding)) or "none",
                 "MATCH" if binding == predicted else "differs"))
    n_match = sum(1 for m in matches.values() if m["match"])
    no_complex_pre = [k for k in F.TYPES if not recs["t%d_pre" % k]["core"]]
    print("  types matching Caplow: %d/8  (differ: %s)  precoalition forms with no complex: %s"
          % (n_match, ",".join(str(k) for k, m in matches.items() if not m["match"]) or "none",
             ",".join(str(k) for k in no_complex_pre) or "none"))
    status = "CONFIRMED" if n_match == 8 else ("PARTIAL" if n_match >= 4 else "REFUTED")
    print("H1 (binding coalitions = Caplow's predicted coalitions in every type): %s" % status)
    F.save("probe_caplow_types", {"control": control, "forms": recs, "matches": matches,
                                   "n_match": n_match, "H1": status})


if __name__ == "__main__":
    main()

"""Probe — Caplow H5: strength is additive.

Question.  Caplow (1956, A.3): "The strength of a coalition is equal to the sum of the strengths of its two
           members." If the sum is what matters, every winning coalition stands in the same relation to the
           isolate. Do all winning coalitions bind, or does binding track how the strength is divided?
Hypothesis. H5 (Caplow): every winning coalition binds.
Method.    The 24 coalition forms; winning = bloc weight > isolate weight; binding vs equal partner weights.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_additivity
"""

from org_frontier.thinkers.caplow import forms as F


def main():
    print("Caplow H5 — strength is additive: do all winning coalitions bind?")
    control = F.run_control()
    recs = F.evaluate_types(pre=False)
    winning = [r for r in recs.values() if r["wins"]]
    n_bind = sum(1 for r in winning if r["binds"])
    equal_bind = sum(1 for r in winning if r["equal_partners"] and r["binds"])
    equal_total = sum(1 for r in winning if r["equal_partners"])
    unequal_bind = sum(1 for r in winning if not r["equal_partners"] and r["binds"])
    unequal_total = sum(1 for r in winning if not r["equal_partners"])
    print("  winning coalitions=%d  binding=%d  equal-partner winners binding %d/%d  unequal-partner winners binding %d/%d"
          % (len(winning), n_bind, equal_bind, equal_total, unequal_bind, unequal_total))
    tracks_equality = (equal_bind == equal_total and unequal_bind == 0)
    status = "CONFIRMED" if n_bind == len(winning) else "REFUTED"
    print("  binding coincides with equal partner weights: %s" % tracks_equality)
    print("H5 (every winning coalition binds regardless of the division of strength): %s" % status)
    F.save("probe_caplow_additivity", {"control": control, "forms": recs, "n_winning": len(winning),
                                        "n_binding": n_bind, "tracks_equality": tracks_equality, "H5": status})


if __name__ == "__main__":
    main()

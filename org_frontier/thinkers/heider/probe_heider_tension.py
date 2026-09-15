"""Probe — Heider H2: forces toward balance; imbalance is tension.

Question.  Heider (1946: 107–108): "If no balanced state exists, then forces towards this state will arise
           ... If a change is not possible, the state of imbalance will produce tension." Do balanced
           triads rest — every attractor a state satisfying every relation — and do unbalanced triads have
           no rest state, ending in cycles or in frozen unsatisfied states?
Hypothesis. H2: balanced → rest states only; unbalanced → no rest state.
Method.    The four named patterns; attractors from the TPM; rest = fixed point satisfying all relations.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_tension
"""

from org_frontier.thinkers.heider import forms as F


def main():
    print("Heider H2 — rest and tension: attractors of the four signed triads")
    control = F.run_control()
    recs = {}
    for name, signs in F.NAMED.items():
        recs[name] = F.evaluate(name, F.triad(signs), F.TRIAD_LABELS, F.TRIAD_EDGES, signs)
        print(F.line(recs[name]))
    balanced = [r for r in recs.values() if r["product"] == 1]
    unbalanced = [r for r in recs.values() if r["product"] == -1]
    bal_ok = all(r["rest_states"] and r["attractors_are_rest"] for r in balanced)
    bal_rest = all(r["rest_states"] for r in balanced)
    unb_no_rest = all(not r["rest_states"] for r in unbalanced)
    unb_fixed = sum(r["n_fixed"] for r in unbalanced)
    unb_cycles = sum(r["n_cycles"] for r in unbalanced)
    print("  balanced: rest states in all=%s, all attractors rest=%s | unbalanced: no rest state in all=%s, "
          "attractors = %d frozen unsatisfied fixed points + %d cycles"
          % (bal_rest, bal_ok, unb_no_rest, unb_fixed, unb_cycles))
    if bal_ok and unb_no_rest:
        status = "CONFIRMED"
    elif bal_rest and unb_no_rest:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (balanced triads rest at satisfied states; unbalanced have none): %s" % status)
    F.save("probe_heider_tension", {"control": control, "forms": recs, "unbalanced_fixed": unb_fixed,
                                     "unbalanced_cycles": unb_cycles, "H2": status})


if __name__ == "__main__":
    main()

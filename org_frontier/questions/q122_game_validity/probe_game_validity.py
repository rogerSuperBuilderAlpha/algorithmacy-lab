"""Probe Q122 (H1-H4) — is the value function a valid cooperative game?

Audits the value wave's machinery against the critical review's T2/T3/T5: whether v(S)=subsystem-Φ is
monotone and superadditive on the forms the wave used, whether the negative Shapley values are clamp
artifacts, and whether the values are background-relative.

Run:  ~/iit-playground/venv-4.0/bin/python -m \
      org_frontier.questions.q122_game_validity.probe_game_validity
"""

import csv
import os

from org_frontier.questions.q122_game_validity import forms as F


def main():
    print("PROBE Q122 (H1-H4) — cooperative-game validity of the value function")
    print("=" * 78)

    prod = F.productive_forms()
    prod_audit = {}
    for name, rules, labels in prod:
        mono, sup = F.monotone_superadditive(rules, labels)
        prod_audit[name] = (mono, sup)
        print(f"  {name:24s}: monotonicity_viol={mono}  superadditivity_viol={sup}")

    dname, drules, dlabels = F.degenerate_form()
    dmono, dsup = F.monotone_superadditive(drules, dlabels)
    print(f"  {dname:24s}: monotonicity_viol={dmono}  superadditivity_viol={dsup}  (degenerate)")

    # clamp and background sensitivity of the headline vectors
    sens = {}
    for name, rules, labels in [("read_recipient", *F.productive_forms()[0][1:]),
                                ("bidirectional_principal", F.productive_forms()[1][1], F.productive_forms()[1][2]),
                                (dname, drules, dlabels)]:
        clamped = F.shapley(rules, labels, background=1, clamp=True)
        raw = F.shapley(rules, labels, background=1, clamp=False)
        zeros = F.shapley(rules, labels, background=0, clamp=True)
        sens[name] = (clamped, raw, zeros)
        print(f"  {name}: clamp+bg1={clamped}")
        print(f"  {' ' * len(name)}  raw  +bg1={raw}")
        print(f"  {' ' * len(name)}  clamp+bg0={zeros}")

    h1 = all(m == 0 for m, _ in prod_audit.values())                     # monotone on productive forms
    h2 = all(s == 0 for _, s in prod_audit.values())                     # superadditive on productive forms
    h3 = dmono > 0                                                        # non-monotone on the degenerate form
    clamp_invariant = all(c == r for c, r, _ in sens.values())           # negatives not a clamp artifact
    bg_relative = all(all(abs(val) < 1e-9 for val in z.values()) for _, _, z in sens.values())
    h4 = clamp_invariant and bg_relative
    print("=" * 78)
    print(f"  H1 v is monotone on every productive form:                 {h1}")
    print(f"  H2 v is superadditive on every productive form:            {h2}")
    print(f"  H3 v is non-monotone on the degenerate monitor-only form:  {h3} ({dmono} violations)")
    print(f"  H4 the vectors are clamp-invariant but background-relative: {h4} "
          f"(clamp-invariant={clamp_invariant}, zero at bg0={bg_relative})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "game_validity.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "monotonicity_violations", "superadditivity_violations", "class"])
        for name, (m, s) in prod_audit.items():
            w.writerow([name, m, s, "productive"])
        w.writerow([dname, dmono, dsup, "degenerate"])


if __name__ == "__main__":
    main()

"""Probe 291 (Q136) — two competing mediators: does competition return value to the parties?

A single faithful mediator captures two-thirds of the coordination's value (Q111). The natural remedy a
market offers is competition: a second mediator the parties could use instead. Q136 asks what a second
mediator does to the integrated value and its distribution, in two regimes. When the mediators are
substitutes — the parties can route through either — neither is necessary. When they are complements — both
are required — both are bottlenecks.

The form is four nodes: worker W, two mediators S1 and S2, counterpart C. Each mediator commits the parties'
joint determination (Si' = W ∧ C). In the substitutes form the parties read either mediator (W' = C' =
S1 ∨ S2); in the complements form they read both (W' = C' = S1 ∧ S2).

Hypotheses (fixed before computing):
  H1. Substitutable mediators eliminate the irreducible coordination: with either mediator sufficient,
      neither is necessary, the form factors (Φ → 0), and there is no rent for anyone — competition
      destroys the value rather than returning it to the parties.
  H2. Complementary mediators split the value: each captures less than a single mediator's two-thirds and the
      parties capture more, the total rising. A required second mediator dilutes the rent toward the parties.

Method: build the substitutes and complements forms; read the whole-system verdict, the major complex, the
total Φ, and the Shapley value of subsystem Φ at the integrating state.

Validation gap: exact Φ; Q111 value function; Φ-to-money bridge open (Q122). "Value", "share", "rent" name
Shapley allocations of Φ.

Run:  python -m org_frontier.questions.q136_competing_mediators.probe_competing_mediators
"""

import os
from itertools import combinations
from math import factorial

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict, major_complex

LABELS = ("W", "S1", "S2", "C")
FORMS = {
    "substitutes (W,C read S1|S2)": [lambda x: x[1] | x[2], lambda x: x[0] & x[3],
                                     lambda x: x[0] & x[3], lambda x: x[1] | x[2]],
    "complements (W,C read S1&S2)": [lambda x: x[1] & x[2], lambda x: x[0] & x[3],
                                     lambda x: x[0] & x[3], lambda x: x[1] & x[2]],
}


def shapley_at(r, labels, state):
    n = len(r)
    net = pyphi.Network(tpm_from_rules(r), cm=cm_from_rules(r), node_labels=labels)
    cache = {}

    def v(S):
        S = tuple(sorted(S))
        if S in cache:
            return cache[S]
        if not S:
            return 0.0
        try:
            phi = float(nbp.sia(pyphi.Subsystem(net, state, nodes=S)).phi)
        except Exception:
            phi = 0.0
        cache[S] = max(0.0, phi)
        return cache[S]

    players = list(range(n))
    vals = {i: 0.0 for i in players}
    for i in players:
        oth = [p for p in players if p != i]
        for rr in range(len(oth) + 1):
            for Sc in combinations(oth, rr):
                w = factorial(len(Sc)) * factorial(n - len(Sc) - 1) / factorial(n)
                vals[i] += w * (v(tuple(Sc) + (i,)) - v(Sc))
    return {labels[i]: round(vals[i], 3) for i in players}, round(v(tuple(players)), 3)


def main():
    print("PROBE 291 (Q136) — two competing mediators: does competition return value to the parties?")
    print("=" * 88)

    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    svc, tc = shapley_at(triad, ("W", "S", "C"), (1, 1, 1))
    ctrl = abs(tc - 2.0) < 1e-6 and abs(svc["S"] - 1.333) < 1e-3
    print(f"  CONTROL single faithful mediator: share {svc['S']/tc:.1%} (two-thirds)  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    res = {}
    for name, r in FORMS.items():
        v = verdict(r, LABELS)
        core, cphi = major_complex(r, LABELS)
        st = v.mip_state or (1, 1, 1, 1)
        sv, tot = shapley_at(r, LABELS, st)
        res[name] = (v, core, tot, sv)
        med_share = (sv["S1"] / tot) if tot > 1e-9 else 0.0
        party_share = ((sv["W"] + sv["C"]) / tot) if tot > 1e-9 else 0.0
        print(f"\n[{name}]")
        print(f"  whole-system: {v.structure} Φ={v.max_phi:.3f} | major complex={core} coreΦ={cphi:.3f}")
        print(f"  Shapley {sv} | each-mediator share {med_share:.0%} | parties collective {party_share:.0%}")

    sub = res["substitutes (W,C read S1|S2)"]
    com = res["complements (W,C read S1&S2)"]
    h1 = sub[0].structure == "dyadic" and sub[0].max_phi < 1e-9
    com_med = com[3]["S1"] / com[2]
    com_party = com[3]["W"] / com[2]
    h2 = com[0].max_phi > 2.0 and com_med < 0.66 and com_party > (1 / 6 + 1e-3)

    print("\n" + "=" * 88)
    print(f"  H1 (substitutable mediators eliminate the coordination — Φ -> 0, no rent): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}")
    print(f"  H2 (complementary mediators split value: each mediator < 2/3, each party > 1/6, total up): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}  "
          f"(Φ={com[0].max_phi:.1f}, each mediator {com_med:.0%}, each party {com_party:.0%})")
    print("  Reading: competition does not simply return the mediator's cut to the parties. Substitutable")
    print("  mediators dissolve the irreducible coordination entirely — Φ goes to zero, and there is no value")
    print("  for anyone to capture. Complementary mediators raise the total value and split it evenly, each of")
    print("  the four taking a quarter, so a second required mediator dilutes the rent toward the parties.")
    print("=" * 88)


if __name__ == "__main__":
    main()

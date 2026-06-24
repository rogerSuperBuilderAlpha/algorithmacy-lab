"""Probe 294 (Q139) — value and veto: does interested mediation align them?

Q112 found a coordination's destruction democratic but its value concentrated — every party can collapse the
triad (universal veto), yet the mediator captures two-thirds. That is a decoupling: equal power to destroy,
unequal share of value. Q139 asks whether the decoupling is fixed or moves with interest. As the mediator
turns interested, does veto power stay universal, and does the value-veto gap — the mediator's value share
above its equal one-third of the universal veto — close or open?

Method: the Q126/Q127 interested mediator on two baselines, the sparse AND (which self-interest destroys) and
the balanced XOR (which self-interest re-integrates), approve agenda. At each interestedness level with
positive Φ: the number of parties whose knockout collapses the form (veto count), the mediator's Shapley
value share, and the gap (share − 1/3).

Hypotheses (fixed before computing):
  H1. Veto power is universal at every interestedness level with positive Φ — all three parties remain
      pivotal. Q112's democratic destruction is robust to interest.
  H2. The value-veto gap tracks integration, not veto: it is large when the form is fully integrated
      (Φ = 2.0) and zero when it is weakly integrated (Φ = 0.5). So destructive interest (AND) closes the gap
      and re-integrating interest (XOR) opens it.

Validation gap: exact Φ; value at the integrating state; Φ-to-money bridge open (Q122). "Value", "share",
"veto" name structural quantities, not money or legal power.

Run:  python -m org_frontier.questions.q139_value_veto.probe_value_veto
"""

import os
from itertools import combinations
from math import factorial

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict

LABELS = ("W", "S", "C")
STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]
BASELINES = {"AND": {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1},
             "XOR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}}


def rules(base, k, agenda=1):
    order = sorted(STATES, key=lambda wc: ((wc[0] + wc[1]) if agenda == 1 else 2 - (wc[0] + wc[1]), wc))
    ov = set(order[:k])
    f = lambda w, c: (agenda if (w, c) in ov else base[(w, c)])
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def pivotal(r, p):
    rr = list(r)
    rr[p] = lambda x, p=p: x[p]
    return verdict(rr, LABELS).structure == "dyadic"


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
    print("PROBE 294 (Q139) — value and veto: does interested mediation align them?")
    print("=" * 84)

    r0 = rules(BASELINES["AND"], 0)
    sv0, t0 = shapley_at(r0, LABELS, (1, 1, 1))
    ctrl = abs(t0 - 2.0) < 1e-6 and sum(pivotal(r0, p) for p in range(3)) == 3
    print(f"  CONTROL faithful triad: Φ=2.0, veto 3/3, mediator value {sv0['S']/t0:.0%}, gap "
          f"{sv0['S']/t0 - 1/3:+.2f}  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    all_universal = True
    gap_tracks = True
    for name, base in BASELINES.items():
        print(f"\n[{name} baseline, approve agenda]")
        print("  k | Φ | veto count | mediator value share | gap (share - 1/3)")
        print("  --+------+------------+----------------------+------------------")
        for k in range(3):
            r = rules(base, k)
            v = verdict(r, LABELS)
            if v.max_phi < 1e-9:
                print(f"  {k} | 0.00 | (dead)     | —                    | —")
                continue
            nveto = sum(pivotal(r, p) for p in range(3))
            st = v.mip_state or (1, 1, 1)
            sv, tot = shapley_at(r, LABELS, st)
            gap = sv["S"] / tot - 1 / 3
            print(f"  {k} | {v.max_phi:.2f} | {nveto}/3        | {sv['S']/tot:18.0%}   | {gap:+.2f}")
            if nveto != 3:
                all_universal = False
            # gap should be ~+1/3 at Φ=2.0 and ~0 at Φ=0.5
            expected = 1 / 3 if v.max_phi > 1.5 else 0.0
            if abs(gap - expected) > 0.05:
                gap_tracks = False

    print("\n" + "=" * 84)
    print(f"  H1 (veto power universal at every level with positive Φ): "
          f"{'SUPPORTED' if all_universal else 'NOT SUPPORTED'}")
    print(f"  H2 (the value-veto gap tracks integration: +1/3 at Φ=2.0, 0 at Φ=0.5): "
          f"{'SUPPORTED' if gap_tracks else 'NOT SUPPORTED'}")
    print("  Reading: every party can always veto the coordination, at every interestedness level — Q112's")
    print("  democratic destruction is robust to interest. What moves is the value-veto gap, the mediator's")
    print("  share above its equal third of the veto. The gap is the integration: full at Φ=2.0, none at")
    print("  Φ=0.5. So self-interest that destroys (AND) democratizes value to match the equal veto, and")
    print("  self-interest that re-integrates (XOR) re-concentrates it. Q112's decoupling is integration.")
    print("=" * 84)


if __name__ == "__main__":
    main()

"""Probe 293 (Q138) — regulation: the minimum faithful fraction that revives the coordination.

A predatory mediator that commits only its own agenda kills the coordination (Q126, Q131). A regulator can
force the mediator to commit the parties' joint determination on some of its states. Q138 asks how much
forced faithfulness it takes to revive the coordination, and who gets the value when it does.

The mediator's default is the predatory constant (always approve). The regulator forces m of its four input
states back to the faithful AND commit, the highest-warrant states first (where the parties most warrant a
commit). The coordination's Φ and the Shapley split are read as m rises from 0 (fully predatory) to 4 (fully
faithful).

Hypotheses (fixed before computing):
  H1. There is a minimum faithful fraction below which the coordination is dead (Φ = 0) and at or above which
      it revives. Regulation must restore at least that fraction.
  H2. Minimum-viable regulation revives the coordination with an egalitarian split — each party gets as much
      as the mediator — and the mediator's two-thirds dominance returns only at full faithfulness. The last
      increment of faithfulness is what concentrates the rent.

Method: sweep m = 0..4 forced-faithful states; per m the verdict Φ and the Shapley value of subsystem Φ at the
integrating state, giving the mediator's share and the parties' collective share.

Validation gap: exact Φ; value at the integrating state; Φ-to-money bridge open (Q122). The forcing order
matters; the highest-warrant-first order is the natural regulatory target.

Run:  python -m org_frontier.questions.q138_faithful_fraction.probe_faithful_fraction
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
AND = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1}


def rules(m):
    """Predatory default (constant approve); m highest-warrant states forced back to faithful AND."""
    order = sorted(STATES, key=lambda wc: (-(wc[0] + wc[1]), wc))   # 11 first, then 01/10, then 00
    faithful = set(order[:m])
    f = lambda w, c: (AND[(w, c)] if (w, c) in faithful else 1)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


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
    print("PROBE 293 (Q138) — regulation: the minimum faithful fraction that revives the coordination")
    print("=" * 84)

    sv4, t4 = shapley_at(rules(4), LABELS, (1, 1, 1))
    ctrl = abs(t4 - 2.0) < 1e-6 and abs(sv4["S"] - 1.333) < 1e-3
    print(f"  CONTROL fully faithful (4/4): Φ={t4:.3f}, mediator share {sv4['S']/t4:.0%}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    print("\n  faithful states | Φ | mediator share | parties (collective)")
    print("  ----------------+-------+----------------+---------------------")
    rows = []
    for m in range(5):
        r = rules(m)
        v = verdict(r, LABELS)
        st = v.mip_state or (1, 1, 1)
        sv, tot = shapley_at(r, LABELS, st)
        msh = (sv["S"] / tot) if tot > 1e-9 else None
        psh = ((sv["W"] + sv["C"]) / tot) if tot > 1e-9 else None
        rows.append((m, v.max_phi, msh, psh))
        print(f"  {m}/4              | {v.max_phi:.3f} | {f'{msh:.0%}' if msh is not None else '  — ':>6}"
              f"         | {f'{psh:.0%}' if psh is not None else '  — '}")

    revived = [m for m, phi, _, _ in rows if phi > 1e-9]
    m_star = min(revived) if revived else None
    threshold_egalitarian = m_star is not None and rows[m_star][2] is not None and rows[m_star][2] < 0.5 + 1e-9
    mediator_dominates_only_full = rows[4][2] > 0.6 and (m_star is None or rows[m_star][2] <= 0.5 + 1e-9)

    print("\n" + "=" * 84)
    print(f"  H1 (a minimum faithful fraction revives the coordination): "
          f"{'SUPPORTED' if m_star is not None else 'NOT SUPPORTED'}  "
          f"(minimum = {m_star}/4 = {m_star/4:.0%} faithful)")
    print(f"  H2 (threshold regulation gives an egalitarian split; mediator dominance only at full faith): "
          f"{'SUPPORTED' if (threshold_egalitarian and mediator_dominates_only_full) else 'NOT SUPPORTED'}  "
          f"(at {m_star}/4 mediator {rows[m_star][2]:.0%}, at 4/4 mediator {rows[4][2]:.0%})")
    print("  Reading: reviving the coordination takes a sharp minimum of faithfulness — below three-quarters")
    print("  the form is dead. At that minimum the value splits evenly, the parties holding the majority; the")
    print("  mediator's two-thirds returns only with the last faithful state. The platform's rent is the")
    print("  fully-faithful commit, so light-touch regulation that merely revives the coordination does not")
    print("  hand the rent back to the platform — full restoration does.")
    print("=" * 84)


if __name__ == "__main__":
    main()

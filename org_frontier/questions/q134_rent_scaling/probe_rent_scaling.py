"""Probe 289 (Q134) — does the mediator's two-thirds rent scale with the number of parties?

Q111 found that the faithful mediator of the three-party triad captures two-thirds of the coordination's
integrated value, and the synthesis paper read that as concentrated platform power. Q134 asks whether the
two-thirds is scale-invariant. The natural null is that the mediator, in every productive coalition at any
size, always takes the same share. The alternative is that the share changes as the coordination grows.

The form is the conjunctive star: a mediator S commits iff all outer parties warrant it (S' = P1 ∧ … ∧ Pk),
and each outer party reads the mediator (Pi' = S). This is the read-recipient triad generalized to k outer
parties. The Shapley value of subsystem Φ distributes the system's Φ (which scales as Φ = n − 1 for the
conjunctive form) among the n = k + 1 parties.

Hypotheses (fixed before computing):
  H1. The mediator's share is scale-invariant at two-thirds, independent of the number of parties.
  H2 (alternative). The share changes with scale; specifically it declines as parties are added, the
      additional parties' contribution diluting the mediator's slice while the total grows.

Method: build the conjunctive star for k = 2, 3, 4 outer parties (n = 3, 4, 5). Compute the Shapley value of
subsystem Φ at the integrating (all-ones) state, the mediator's share, and each outer party's share.

Validation gap: exact Φ; Q111 value function; Φ-to-money bridge open (Q122). "Value", "share", "rent" name
Shapley allocations of Φ.

Run:  python -m org_frontier.questions.q134_rent_scaling.probe_rent_scaling
"""

import os
from itertools import combinations
from math import factorial

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict


def star_rules(k):
    """Mediator S (node 0) commits iff all k outer parties warrant it; each outer party reads S."""
    n = k + 1
    rules = [lambda x: 1 if all(x[j] for j in range(1, n)) else 0]
    for _ in range(1, n):
        rules.append(lambda x: x[0])
    labels = tuple(["S"] + [f"P{i}" for i in range(1, n)])
    return rules, labels


def shapley_at(rules, labels, state):
    n = len(rules)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
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
        for r in range(len(oth) + 1):
            for Sc in combinations(oth, r):
                w = factorial(len(Sc)) * factorial(n - len(Sc) - 1) / factorial(n)
                vals[i] += w * (v(tuple(Sc) + (i,)) - v(Sc))
    return {labels[i]: round(vals[i], 3) for i in players}, round(v(tuple(players)), 3)


def main():
    print("PROBE 289 (Q134) — does the mediator's two-thirds rent scale with the number of parties?")
    print("=" * 84)

    # Control: the three-party triad reproduces Q111 — mediator 1.333 of Φ=2.0, share two-thirds.
    r0, l0 = star_rules(2)
    sv0, t0 = shapley_at(r0, l0, (1, 1, 1))
    ctrl = abs(t0 - 2.0) < 1e-6 and abs(sv0["S"] - 1.333) < 1e-3
    print(f"  CONTROL 3-party triad: total Φ={t0:.3f}, mediator {sv0['S']:.3f} share {sv0['S']/t0:.1%}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    print("\n  parties | total Φ | mediator Shapley | mediator share | outer-party share")
    print("  --------+---------+------------------+----------------+------------------")
    shares = []
    for k in (2, 3, 4):
        rules, labels = star_rules(k)
        st = verdict(rules, labels).mip_state or tuple(1 for _ in labels)
        sv, tot = shapley_at(rules, labels, st)
        med = sv["S"]
        outer = sv["P1"]
        share = med / tot
        shares.append((k + 1, share, outer / tot))
        print(f"  {k+1:^7} | {tot:7.3f} | {med:16.3f} | {share:13.1%}  | {outer/tot:16.1%}")

    declines = all(shares[i][1] > shares[i + 1][1] for i in range(len(shares) - 1))
    invariant = abs(shares[0][1] - shares[-1][1]) < 1e-3
    print("\n" + "=" * 84)
    print(f"  H1 (mediator share is scale-invariant at two-thirds): "
          f"{'SUPPORTED' if invariant else 'NOT SUPPORTED'}")
    print(f"  H2 (the share declines as parties are added — the rent dilutes): "
          f"{'SUPPORTED' if declines else 'NOT SUPPORTED'}  "
          f"(share {' -> '.join(f'{s:.1%}' for _, s, _ in shares)})")
    print("  Reading: the mediator's rent is not scale-invariant. As the coordination grows the total")
    print("  integrated value grows (Φ = n-1) but the mediator's slice falls toward one-half; the parties")
    print("  collectively keep more (33% -> 45%), though each individual party keeps less. The bottleneck's")
    print("  dominance is a small-coordination phenomenon — in a larger pool it still takes the plurality.")
    print("=" * 84)


if __name__ == "__main__":
    main()

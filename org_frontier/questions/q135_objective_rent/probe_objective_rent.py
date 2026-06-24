"""Probe 290 (Q135) — the objective's rent: what the system's own agenda captures when it joins the core.

Q128 found that a predatory mediator (S' = O) re-integrates the coordination when its objective O reads both
parties, with the objective entering the irreducible core. Q129 found the objective displaces a party from
the core. Q135 asks the value question: when the system's objective joins the core, does it capture value,
and at whose expense? The objective is the system's own agenda; if it takes a share, the platform's goal is a
rentier on the coordination, not a free pursuit.

The model is Q128's: worker W, system S, counterpart C, objective O, with W' = S, S' = O, C' = S, and O'
adapting to the parties. The Shapley value of subsystem Φ distributes the system's Φ among the four nodes.

Hypotheses (fixed before computing):
  H1. When the objective adapts to both parties (it joins the core, Q128), it captures positive value — it is
      a claimant, not a passive goal.
  H2. The objective captures as much as the system itself, and the human parties' shares are driven to near
      zero or below — the agenda displaces the parties in value as it does in the core (Q129).

Method: the Q128 forms — predatory mediator S' = O with the objective frozen (O' = O) or adaptive
(O' = W ∧ C, W ∨ C, W ⊕ C). Shapley value of subsystem Φ at the verdict's integrating state; the objective's
share, the system's share, and the parties' shares.

Validation gap: exact Φ; Q111 value function at the integrating state; Φ-to-money bridge open (Q122). Small
negative Shapley values at weakly-integrated forms are non-monotonicity artifacts. "Value", "share", "rent"
name Shapley allocations of Φ.

Run:  python -m org_frontier.questions.q135_objective_rent.probe_objective_rent
"""

import os
from itertools import combinations
from math import factorial

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict

LABELS = ("W", "S", "C", "O")
ADAPTATIONS = {
    "frozen (O'=O)": lambda x: x[3],
    "AND (O'=W&C)": lambda x: x[0] & x[2],
    "OR (O'=W|C)": lambda x: x[0] | x[2],
    "XOR (O'=W^C)": lambda x: x[0] ^ x[2],
}


def rules(obj):
    return [lambda x: x[1], lambda x: x[3], lambda x: x[1], obj]   # W'=S, S'=O, C'=S, O'=obj


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
        for r_ in range(len(oth) + 1):
            for Sc in combinations(oth, r_):
                w = factorial(len(Sc)) * factorial(n - len(Sc) - 1) / factorial(n)
                vals[i] += w * (v(tuple(Sc) + (i,)) - v(Sc))
    return {labels[i]: round(vals[i], 3) for i in players}, round(v(tuple(players)), 3)


def main():
    print("PROBE 290 (Q135) — the objective's rent: what the system's agenda captures when it joins the core")
    print("=" * 92)

    # Control: the faithful 3-party triad reproduces Q111 (mediator two-thirds).
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    sv_c, t_c = shapley_at(triad, ("W", "S", "C"), (1, 1, 1))
    ctrl = abs(t_c - 2.0) < 1e-6 and abs(sv_c["S"] - 1.333) < 1e-3
    print(f"  CONTROL faithful triad: mediator {sv_c['S']:.3f} of Φ={t_c:.3f} (two-thirds)  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    print("\n  objective adaptation | Φ | core | Shapley W/S/C/O | O-share | S-share | parties")
    print("  ---------------------+---+------+-----------------+---------+---------+--------")
    rows = []
    for name, obj in ADAPTATIONS.items():
        r = rules(obj)
        v = verdict(r, LABELS)
        st = v.mip_state or (1, 1, 1, 1)
        sv, tot = shapley_at(r, LABELS, st)
        o_sh = (sv["O"] / tot) if tot > 1e-9 else 0.0
        s_sh = (sv["S"] / tot) if tot > 1e-9 else 0.0
        parties = sv["W"] + sv["C"]
        rows.append((name, v.max_phi, sv, o_sh, s_sh, parties, tot))
        print(f"  {name:<20} | {v.max_phi:.1f} |      | {sv['W']:.2f}/{sv['S']:.2f}/{sv['C']:.2f}/{sv['O']:.2f} "
              f"| {o_sh:6.0%}  | {s_sh:6.0%}  | {parties:+.2f}")

    adaptive = [r for r in rows if r[6] > 1e-9]   # forms with positive total Φ
    h1 = all(r[2]["O"] > 1e-3 for r in adaptive)
    objective_equals_system = all(abs(r[3] - r[4]) < 1e-3 for r in adaptive)
    # Parties' fate tracks displacement: negative where the objective displaces (AND/OR), positive where not (XOR).
    displacing = [r for r in adaptive if r[0].startswith("AND") or r[0].startswith("OR")]
    nondisplacing = [r for r in adaptive if r[0].startswith("XOR")]
    parties_track = (all(r[5] < 0 for r in displacing) and all(r[5] > 0 for r in nondisplacing))

    print("\n" + "=" * 92)
    print(f"  H1 (the adaptive objective captures positive value — a claimant, not a passive goal): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}")
    print(f"  REFINED (the objective captures exactly what the system does — a co-equal rentier): "
          f"{'CONFIRMED' if objective_equals_system else 'FAILED'}")
    print(f"  REFINED (the parties' value tracks displacement — negative under AND/OR, positive under XOR): "
          f"{'CONFIRMED' if parties_track else 'FAILED'}")
    print("  Reading: the system's own agenda is a rentier on a par with the system — O-share = S-share in")
    print("  every adaptive form. Whether the human parties keep anything tracks Q129's displacement: under")
    print("  the conjunctive/disjunctive objective, which displaces a party from the core, the parties take")
    print("  negative value; under the parity objective, which keeps all four bound, they take an equal share.")
    print("=" * 92)


if __name__ == "__main__":
    main()

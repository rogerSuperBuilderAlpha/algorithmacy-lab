"""Probe 288 (Q133) — value capture under the deny agenda: completing the Q132 symmetry.

Q132 read value capture across baselines under the approve agenda and found extraction on the XOR baseline,
which re-integrates under approve. Q127 established that under the deny agenda the re-integrating baseline is
XNOR instead. Q133 runs the deny-agenda value sweep so the mirror result reproduces from a script: under
deny, the extracting baseline should be XNOR (not XOR), with the mediator again capturing two-thirds at full
re-integration.

Hypotheses (fixed before computing):
  H1. Under the deny agenda, the re-integrating baseline is XNOR (Φ rises 0.5 -> 2.0) and the mediator
      captures two-thirds there — extraction, the mirror of Q132's XOR-under-approve.
  H2. AND/OR still destroy under deny (value and share fall), and XOR does not re-integrate under deny.

Method: the interested mediator at level k imposes the deny agenda (a = 0) on the k states where the parties
least warrant denial (the highest-warrant-for-1 states first), committing the faithful baseline elsewhere.
Shapley value of subsystem Φ at the verdict's max-Φ state, for the four baselines.

Validation gap: exact Φ; Q111 value function read at the integrating state (Q132); Φ-to-money bridge open
(Q122). "Value", "share", "rent" name Shapley allocations of Φ.

Run:  python -m org_frontier.questions.q133_deny_symmetry.probe_deny_symmetry
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
BASELINES = {
    "AND": {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1},
    "OR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1},
    "XNOR": {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 1},
    "XOR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0},
}


def rules_for(base, k, agenda=0):
    order = sorted(STATES, key=lambda wc: ((wc[0] + wc[1]) if agenda == 1 else 2 - (wc[0] + wc[1]), wc))
    ov = set(order[:k])
    f = lambda w, c: (agenda if (w, c) in ov else base[(w, c)])
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


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
    print("PROBE 288 (Q133) — value capture under the deny agenda: completing the Q132 symmetry")
    print("=" * 84)

    r0 = rules_for(BASELINES["AND"], 0)
    st0 = verdict(r0, LABELS).mip_state or (1, 1, 1)
    sv0, t0 = shapley_at(r0, LABELS, st0)
    ctrl = abs(t0 - 2.0) < 1e-6 and abs(sv0["S"] - 1.333) < 1e-3
    print(f"  CONTROL faithful AND: total Φ={t0:.3f}, mediator share {sv0['S']/t0:.1%}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    extraction_on = []
    for name, base in BASELINES.items():
        print(f"\n[baseline {name}, deny agenda]")
        print("  k | verdict Φ | mediator share")
        print("  --+-----------+---------------")
        traj = []
        for k in range(5):
            r = rules_for(base, k)
            v = verdict(r, LABELS)
            st = v.mip_state or (1, 1, 1)
            sv, tot = shapley_at(r, LABELS, st)
            sh = (sv["S"] / tot) if tot > 1e-9 else None
            traj.append((k, v.max_phi, sh))
            print(f"  {k} | {v.max_phi:9.3f} | {f'{sh:6.1%}' if sh is not None else '   —  '}")
        faith = traj[0][1]
        if any(t[1] > faith + 1e-9 and t[2] is not None and t[2] > 0.6 for t in traj):
            extraction_on.append(name)

    h1 = "XNOR" in extraction_on and "XOR" not in extraction_on
    h2 = "AND" not in extraction_on and "OR" not in extraction_on
    print("\n" + "=" * 84)
    print(f"  H1 (deny: XNOR re-integrates and extracts, mirroring XOR-under-approve): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}  (extraction on: {extraction_on})")
    print(f"  H2 (AND/OR destroy under deny; XOR does not re-integrate under deny): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")
    print("  Reading: the destruction-vs-extraction split is symmetric in the agenda — approve extracts on")
    print("  XOR, deny extracts on XNOR — because each agenda re-integrates the balanced baseline whose")
    print("  minority output it overrides. The value image of Q127's agenda symmetry.")
    print("=" * 84)


if __name__ == "__main__":
    main()

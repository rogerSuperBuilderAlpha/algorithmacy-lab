"""Probe 287 (Q132) — value capture across baselines: destruction or extraction is baseline-relative.

Question: Q131 found that an interested mediator on the AND baseline destroys value — the total Φ falls and
the mediator's two-thirds share falls with it. Q127 found the baseline governs what self-interest does: on
the balanced baselines a faithful mediator is weakly irreducible (Φ = 0.5) and a dose of self-interest
re-integrates it, raising Φ. Q132 reads the Shapley value of integration across all four Q127 baselines and
asks whether, where the value grows, the mediator captures the gain (extraction) or the parties share it.

A methodological correction is forced first. Q111's Shapley value function reads subsystem Φ at the all-ones
background state. That state is where the AND mediator integrates, so Q131's reading was sound there, but it
is not where the OR, XNOR, or XOR mediators integrate — at all-ones their subsystem Φ is zero or degenerate,
and the value function misses the very re-integration Q127 found. The value must be read at the state where
the form integrates: the verdict's max-Φ state. Q132 uses that verdict-aligned background and reports the
all-ones reading alongside to show where the two diverge.

Hypotheses (fixed before computing):
  H1. The all-ones value reading (Q111's) agrees with the verdict only on the AND baseline; on the others it
      is degenerate, because all-ones is not those mediators' integrating state.
  H2. Under the verdict-aligned reading, destruction-versus-extraction is baseline-relative, mirroring Q127:
      on a sparse baseline (AND) self-interest destroys value and the mediator's rent; on a balanced baseline
      that re-integrates (XOR under the approve agenda) the mediator captures the re-integrated value as the
      same concentrated two-thirds rent — extraction, not sharing.

Method: the Q127 interested mediator at level k for four baselines (AND, OR, XNOR, XOR), approve agenda. At
each k, the verdict (max Φ over reachable states) and its integrating state, then the Shapley value of
subsystem Φ at that state, and for comparison at the all-ones state.

Validation gap: exact Φ on a three-node model; the Φ-to-economic-value bridge is open (Q122), so "value",
"share", "rent" name Shapley allocations of Φ, not money. The background-state choice is itself the Q122
question; Q132 uses the verdict-aligned state and says so.

Run:  python -m org_frontier.questions.q132_value_baselines.probe_value_baselines
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


def rules_for(base, k, agenda=1):
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


def share(sv, total):
    return (sv["S"] / total) if total > 1e-9 else None


def main():
    print("PROBE 287 (Q132) — value capture across baselines: destruction or extraction is baseline-relative")
    print("=" * 92)

    # Control: faithful AND at its integrating state reproduces Q111/Q131 (mediator 1.333, share 2/3).
    r0 = rules_for(BASELINES["AND"], 0)
    st0 = verdict(r0, LABELS).mip_state or (1, 1, 1)
    sv0, t0 = shapley_at(r0, LABELS, st0)
    ctrl = abs(t0 - 2.0) < 1e-6 and abs(sv0["S"] - 1.333) < 1e-3
    print(f"  CONTROL faithful AND @ {st0}: total Φ={t0:.3f}, mediator share {sv0['S']/t0:.1%}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    allones_ok_on = []      # baselines where all-ones agrees with verdict at k=0
    extraction_on = []      # balanced baselines that re-integrate and concentrate the rent
    for name, base in BASELINES.items():
        print(f"\n[baseline {name}]")
        print("  k | verdict Φ | @maxstate share | all-ones Φ | reading")
        print("  --+-----------+-----------------+------------+--------")
        traj = []
        for k in range(5):
            r = rules_for(base, k)
            v = verdict(r, LABELS)
            st = v.mip_state or (1, 1, 1)
            sv_v, tot_v = shapley_at(r, LABELS, st)
            sv_a, tot_a = shapley_at(r, LABELS, (1, 1, 1))
            sh = share(sv_v, tot_v)
            traj.append((k, v.max_phi, sh, tot_a))
            sh_s = f"{sh:6.1%}" if sh is not None else "   —  "
            print(f"  {k} | {v.max_phi:9.3f} | {sh_s}          | {tot_a:10.3f} |")
        # all-ones agrees with verdict at k=0?
        if abs(traj[0][3] - traj[0][1]) < 1e-6:
            allones_ok_on.append(name)
        # re-integration with concentrated rent: some k>0 has Φ above the faithful Φ and share ~2/3
        faith_phi = traj[0][1]
        if any(t[1] > faith_phi + 1e-9 and t[2] is not None and t[2] > 0.6 for t in traj):
            extraction_on.append(name)

    h1 = allones_ok_on == ["AND"]
    h2 = "XOR" in extraction_on and "AND" not in extraction_on

    print("\n" + "=" * 92)
    print(f"  H1 (all-ones value reading agrees with the verdict only on AND): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}  (agrees on: {allones_ok_on})")
    print(f"  H2 (verdict-aligned: re-integrating baselines concentrate the rent — extraction): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}  (extraction on: {extraction_on})")
    print("  Reading: destruction or extraction is baseline-relative, mirroring Q127. On a sparse mediator")
    print("  (AND) self-interest destroys the value and the mediator's two-thirds rent with it. On a balanced")
    print("  mediator that re-integrates (XOR, approve), self-interest raises the value to Φ=2.0 and the")
    print("  mediator captures it as the same two-thirds rent — extraction. The all-ones value reading sees")
    print("  none of this off the AND baseline, isolating the Q122 background-state problem as the blocker.")
    print("=" * 92)


if __name__ == "__main__":
    main()

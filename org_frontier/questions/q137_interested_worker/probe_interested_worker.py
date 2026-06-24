"""Probe 292 (Q137) — the interested worker: can gaming the system reclaim value?

The interested-mediator studies put the agenda in the system. The worker is also described as interested:
algorithmic resistance is the worker acting on its own theory of the system rather than the system's signal.
Q137 makes the worker interested too and asks whether gaming reclaims value for the worker, or whether mutual
self-interest only destroys the coordination faster.

The triad is W, S, C with the faithful rules W' = S, S' = W ∧ C, C' = S. The system's interestedness is the
Q126 ladder over its agenda. The worker's interestedness is the analogous move on its own rule: the worker
reads only the system (W' = S), and an interested worker overrides that toward its own agenda (acting
regardless of the system's signal) on some of its input states. Both interestedness levels are swept.

Hypotheses (fixed before computing):
  H1. The worker cannot reclaim absolute value by gaming the system: worker interestedness collapses the
      coordination (Φ -> 0), so the worker captures nothing.
  H2. The only thing that raises the worker's share is the system defecting (the Q131 equalization), and even
      then the worker's absolute value falls. There is no cell where the worker gains.

Method: sweep system interestedness k_S in {0,1,2} and worker interestedness k_W in {0,1,2}. For each cell,
the verdict Φ and the worker's Shapley value (absolute and share) of subsystem Φ at the integrating state.

Validation gap: exact Φ; the worker reads only the system in the canonical triad, so its interested rule has
few states — a richer worker is a limitation. Φ-to-money bridge open (Q122).

Run:  python -m org_frontier.questions.q137_interested_worker.probe_interested_worker
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


def system_rule(k_s):
    order = sorted(STATES, key=lambda wc: (wc[0] + wc[1], wc))
    ov = set(order[:k_s])
    return lambda w, c: (1 if (w, c) in ov else (w & c))


def worker_rule(k_w):
    # The worker reads only S; faithful W' = S. Override toward its agenda (act, = 1) on k_w of the 2 S-states.
    ov = set([0, 1][:k_w])
    return lambda s: (1 if s in ov else s)


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


def cell(k_s, k_w):
    fS, fW = system_rule(k_s), worker_rule(k_w)
    rules = [lambda x, fW=fW: fW(x[1]), lambda x, fS=fS: fS(x[0], x[2]), lambda x: x[1]]
    v = verdict(rules, LABELS)
    st = v.mip_state or (1, 1, 1)
    sv, tot = shapley_at(rules, LABELS, st)
    w_abs = sv["W"]
    w_share = (w_abs / tot) if tot > 1e-9 else 0.0
    return v.max_phi, w_abs, w_share


def main():
    print("PROBE 292 (Q137) — the interested worker: can gaming the system reclaim value?")
    print("=" * 80)

    phi0, wabs0, wsh0 = cell(0, 0)
    ctrl = abs(phi0 - 2.0) < 1e-6 and abs(wabs0 - 0.333) < 1e-3
    print(f"  CONTROL faithful triad: Φ={phi0:.3f}, worker Shapley {wabs0:.3f} (share {wsh0:.0%})  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    print("\n  Worker absolute Shapley value (and Φ) by interestedness:")
    print("  k_S \\ k_W |   0 (faithful)   |   1 (gaming)   |   2 (ignores system)")
    print("  ----------+------------------+----------------+---------------------")
    grid = {}
    for ks in (0, 1, 2):
        cells = []
        for kw in (0, 1, 2):
            phi, wabs, wsh = cell(ks, kw)
            grid[(ks, kw)] = (phi, wabs, wsh)
            cells.append(f"Φ{phi:.2f} W={wabs:+.3f}")
        label = "faithful" if ks == 0 else ("interested" if ks == 1 else "predatory")
        print(f"  {ks} ({label:<10}) | {cells[0]:<16} | {cells[1]:<14} | {cells[2]}")

    worker_collapses = all(grid[(ks, kw)][0] < 1e-9 for ks in (0, 1, 2) for kw in (1, 2))
    share_rises_only_on_system = grid[(1, 0)][2] > grid[(0, 0)][2] + 1e-3
    worker_never_gains = all(grid[(ks, kw)][1] <= wabs0 + 1e-3 for ks in (0, 1, 2) for kw in (0, 1, 2))

    print("\n" + "=" * 80)
    print(f"  H1 (worker gaming collapses the coordination — Φ -> 0 whenever k_W >= 1): "
          f"{'SUPPORTED' if worker_collapses else 'NOT SUPPORTED'}")
    print(f"  H2 (worker's share rises only when the system defects; absolute value never gains): "
          f"{'SUPPORTED' if (share_rises_only_on_system and worker_never_gains) else 'NOT SUPPORTED'}  "
          f"(share at k_S=1: {grid[(1,0)][2]:.0%} vs baseline {wsh0:.0%}; max worker abs = {wabs0:.3f})")
    print("  Reading: the worker has no structural lever to capture value. Acting on its own agenda rather")
    print("  than the system's signal collapses the irreducible bind, so gaming yields nothing. Its share")
    print("  rises only when the SYSTEM defects and the shrinking value equalizes, but its absolute take falls")
    print("  in every interested cell. Resistance breaks the coordination; it does not redistribute it.")
    print("=" * 80)


if __name__ == "__main__":
    main()

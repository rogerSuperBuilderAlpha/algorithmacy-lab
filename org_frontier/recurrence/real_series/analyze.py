"""Read the real recorded series with the recurrence instrument, and fit a model for a first Φ.

Cross-recurrence runs directly on the weekly party-activity series: the coupling matrix and its lead-
lag, each party's coupling centrality, the pairwise measures, and the whole-system multidimensional
recurrence. For the three-party core era a Boolean model is fit to the series and its exact Φ
computed, a first structural pass labeled as model-fit. Tests the predictions in HYPOTHESES.md.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/real_series/analyze.py
"""

import csv
import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import (
    coupling_matrix, coupling_centrality, md_recurrence, crqa, peak)
from org_frontier.classifier.classifier import classify_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states

HERE = os.path.dirname(__file__)
PROM = 0.05


def load(name):
    path = os.path.join(HERE, f"activity_{name}.csv")
    with open(path) as f:
        r = csv.reader(f)
        header = next(r)[1:]
        data = np.array([[int(x) for x in row[1:]] for row in r], dtype=int)
    return header, data


def behavioral(name, parties, traj):
    print(f"\n=== {name}: cross-recurrence on the real series ({traj.shape[0]} weeks, "
          f"{len(parties)} parties) ===")
    cen = coupling_centrality(traj)
    order = np.argsort(-cen)
    print("  coupling centrality (high = behavioral hub):")
    for i in order:
        print(f"    {parties[i]:<18} {cen[i]:.3f}")
    lag, prom = coupling_matrix(traj, max_lag=8)
    print("  pairwise coupling (RR, DET, Lmax, lag):")
    sync = led = 0
    best = (-1, None)
    for a, b in itertools.combinations(range(len(parties)), 2):
        m = crqa(traj[:, a], traj[:, b])
        pl, pr = peak(traj[:, a], traj[:, b], max_lag=8)
        tag = (f"lag {pl:+d}" if pr > PROM else "no lead")
        if pr > PROM:
            if abs(pl) <= 1:
                sync += 1
            else:
                led += 1
        score = m["det"] * m["lmax"]
        if score > best[0]:
            best = (score, (parties[a], parties[b]))
        # share of recurrence that is co-ACTIVE (1-1) rather than co-inactive (0-0)
        x, y = traj[:, a], traj[:, b]
        R = (x[:, None] == y[None, :])
        both = (x[:, None] == 1) & (y[None, :] == 1)
        active_share = both.sum() / max(R.sum(), 1)
        print(f"    {parties[a]:<14}-{parties[b]:<14} RR {m['rr']:.3f} DET {m['det']:.3f} "
              f"Lmax {m['lmax']:>3d}  {tag} (prom {pr:.2f})  co-active share {active_share:.2f}")
    md = md_recurrence(traj)
    print(f"  whole-system md-recurrence: RR {md['rr']:.3f} DET {md['det']:.2f}")
    print(f"  strongest sustained pair: {best[1]}")
    print(f"  prominent pairs near lag 0: {sync}; with a directed lead: {led}")
    return cen, order, best


def fit_rules(traj):
    """Fit each node's next-state as the majority next value over weeks at each global state."""
    n = traj.shape[1]
    tables = []
    for j in range(n):
        counts = {}
        for t in range(len(traj) - 1):
            s = tuple(traj[t])
            counts.setdefault(s, []).append(int(traj[t + 1, j]))
        table = {}
        for s in itertools.product((0, 1), repeat=n):
            vals = counts.get(s, [])
            table[s] = 1 if vals and sum(vals) * 2 >= len(vals) else 0
        tables.append(table)

    def make(j):
        return lambda state, j=j: tables[j][tuple(int(x) for x in state)]
    rules = [make(j) for j in range(n)]
    # in-sample accuracy
    correct = total = 0
    for t in range(len(traj) - 1):
        s = tuple(traj[t])
        for j in range(n):
            total += 1
            correct += int(rules[j](s) == traj[t + 1, j])
    return rules, correct / total


def structural_core(parties, traj):
    print(f"\n=== core: a Boolean model FIT to the series, then exact Φ (first pass, model-fit) ===")
    rules, acc = fit_rules(traj)
    labels = tuple(p[0].upper() for p in parties)   # W, R, W -> disambiguate
    labels = ("W", "R", "M")
    v = classify_rules(rules, labels)
    net, tpm = network(rules, labels)
    _, core, phi = complex_over_states(net, tpm, len(parties))
    coremembers = "".join(labels[i] for i in sorted(core)) if core else "-"
    print(f"  fit in-sample accuracy: {acc:.2f}")
    print(f"  fitted-model verdict: {v.structure}, whole-system Φ={v.max_phi:.3f}, "
          f"major complex={coremembers} (Φ={phi:.3f})")
    print(f"  labels: W={parties[0]}, R={parties[1]}, M={parties[2]}")


if __name__ == "__main__":
    for name in ("core", "recent"):
        parties, traj = load(name)
        behavioral(name, parties, traj)
    parties, traj = load("core")
    structural_core(parties, traj)

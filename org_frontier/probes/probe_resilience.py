"""Probe 108 (D2) — does Φ track resilience even though it does not track success?

Question: Φ is orthogonal to match-success (Probes 48, 80). Is it orthogonal to everything behavioral, or
does it track resilience — how fast a form recovers from a perturbation? Hypothesis: triadic forms
recover differently from a knocked node than dyadic forms, so the verdict tracks recovery time even
though it does not track success. Method: for each corpus form, find its attractor from a fixed start,
flip each node in each attractor state, count deterministic steps to return to the attractor (recovery
time), and correlate the mean recovery time with the verdict.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_resilience
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family
from .probe_phi_ar import _auc

N = 3
MAX = 30


def step(rules, s):
    return tuple(int(rules[i](s)) for i in range(N))


def attractor(rules, start):
    seen, s = [], start
    while s not in seen:
        seen.append(s)
        s = step(rules, s)
    return set(seen[seen.index(s):])


def recovery(rules):
    attr = attractor(rules, (1,) * N)
    times = []
    for a in attr:
        for j in range(N):
            p = list(a)
            p[j] ^= 1
            s, t = tuple(p), 0
            while s not in attr and t < MAX:
                s = step(rules, s)
                t += 1
            times.append(t)
    return float(np.mean(times)) if times else 0.0


def main():
    print("PROBE 108 (D2) — recovery time from perturbation vs the verdict")
    print("=" * 64)
    rec, y = [], []
    for _, rules in enumerate_family():
        rec.append(recovery(rules))
        y.append(int(classify_rules(rules, labels=("W", "S", "C")).structure == "triadic"))
    rec = np.array(rec)
    y = np.array(y)
    auc = _auc(rec, y)
    print(f"  {len(y)} forms, {int(y.sum())} triadic")
    print(f"  triadic mean recovery time = {rec[y==1].mean():.3f} steps")
    print(f"  dyadic  mean recovery time = {rec[y==0].mean():.3f} steps")
    print(f"  rank-AUC (recovery time predicts triadic) = {auc:.3f}")
    print("=" * 64)
    if abs(auc - 0.5) >= 0.15:
        direction = "longer" if rec[y == 1].mean() > rec[y == 0].mean() else "shorter"
        print(f"  Reading: triadic forms take {direction} to recover from a perturbation, so the verdict")
        print("  tracks resilience even though it does not track success — Φ is about the kind of")
        print("  coordination, and that kind has a behavioral signature in how the form absorbs a shock.")
    else:
        print("  Reading: recovery time does not track the verdict either. Φ is orthogonal to this")
        print("  behavioral measure as well — the structural kind leaves no recovery-time signature here.")
    print("=" * 64)


if __name__ == "__main__":
    main()

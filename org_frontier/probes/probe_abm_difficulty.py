"""Probe 98 (#40) — does the verdict track an agent-based coordination-difficulty measure?

Question: the construct says triadic coordination is harder than dyadic. Does an independent learning
measure agree? When two agents must hit a platform's commit by choosing outputs, how hard is it for
independent Q-learners to coordinate, and does that difficulty track the exact verdict? Hypothesis:
triadic forms are harder to learn — the commit depends jointly on both agents, so independent learners
take longer to converge than on a dyadic commit one agent alone can drive. Method: for each corpus form,
read its commit function S(W,C); run two independent epsilon-greedy Q-learning bandits whose reward is
the commit value; record episodes-to-stable-success (difficulty); correlate difficulty with the verdict.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_abm_difficulty
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

LABELS = ("W", "S", "C")
EPISODES = 300
SEEDS = 6


def difficulty(ts, rng):
    """Episodes for two independent Q-bandits to reach stable commit=1; EPISODES if commit unreachable."""
    if max(ts) == 0:
        return EPISODES
    qw = np.zeros(2)
    qc = np.zeros(2)
    alpha, streak, need = 0.2, 0, 10
    for ep in range(EPISODES):
        eps = max(0.05, 1.0 - ep / 100.0)
        aw = rng.integers(2) if rng.random() < eps else int(np.argmax(qw))
        ac = rng.integers(2) if rng.random() < eps else int(np.argmax(qc))
        r = float(ts[aw | (ac << 1)])
        qw[aw] += alpha * (r - qw[aw])
        qc[ac] += alpha * (r - qc[ac])
        streak = streak + 1 if r == 1.0 else 0
        if streak >= need:
            return ep
    return EPISODES


def commit_table(rules):
    """Recover the 4-entry commit truth table S(W,C) from a corpus form."""
    return tuple(int(rules[1]([w, 0, c])) for c in (0, 1) for w in (0, 1))


def main():
    print("PROBE 98 (#40) — agent-based coordination difficulty vs the verdict")
    print("=" * 64)
    rng = np.random.default_rng(40)
    diffs, y = [], []
    for _, rules in enumerate_family():
        ts = commit_table(rules)
        d = np.mean([difficulty(ts, rng) for _ in range(SEEDS)])
        diffs.append(d)
        y.append(int(classify_rules(rules, labels=LABELS).structure == "triadic"))
    diffs = np.array(diffs)
    y = np.array(y)
    print(f"  {len(y)} forms, {int(y.sum())} triadic; difficulty = mean episodes-to-coordinate")
    print(f"  triadic mean difficulty = {diffs[y==1].mean():.1f}")
    print(f"  dyadic  mean difficulty = {diffs[y==0].mean():.1f}")
    auc = _auc(diffs, y)
    print(f"  rank-AUC (difficulty predicts triadic) = {auc:.3f}")
    print("=" * 64)
    if auc >= 0.65:
        print("  Reading: triadic forms take longer for independent agents to coordinate, so the exact")
        print("  verdict tracks behavioral coordination difficulty — structure and difficulty agree.")
    else:
        print("  Reading: the independent-learner difficulty does not track the verdict (AUC near 0.5),")
        print("  and triadic forms are not the harder ones here. The commit-function difficulty an")
        print("  independent-bandit measure sees is not what the structural verdict measures; coordination")
        print("  hardness for selfish learners and irreducibility of the form are different things.")
    print("=" * 64)


if __name__ == "__main__":
    main()

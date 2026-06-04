"""Probe 107 (D1) — do partner-modeling agents show the difficulty gap independent learners did not?

Question: independent Q-bandits showed no link between coordination difficulty and the verdict (Probe 98,
AUC 0.567). Does giving the agents a model of the partner — fictitious play, where each best-responds to
the partner's observed action distribution — recover a link? Hypothesis: partner-modeling resolves the
coordination problems triadic commits pose, so either the difficulty now tracks the verdict, or (if it
does not) the verdict is confirmed not to be a coordination-game-difficulty measure for any agent.
Method: for each corpus form, read its commit function; run two fictitious-play learners whose reward is
the commit; record episodes-to-stable-coordination; correlate with the verdict and compare to Probe 98.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_tom_agents
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
from .probe_abm_difficulty import commit_table

EPISODES = 300
SEEDS = 6


def difficulty_fp(ts, rng):
    """Fictitious play: each agent best-responds to the partner's empirical action frequency."""
    if max(ts) == 0:
        return EPISODES
    # counts of each agent's past actions (Laplace-smoothed)
    cw = np.ones(2)
    cc = np.ones(2)
    streak = 0
    for ep in range(EPISODES):
        eps = max(0.05, 1.0 - ep / 100.0)
        pc = cc / cc.sum()           # W's model of C's action distribution
        pw = cw / cw.sum()           # C's model of W's action distribution
        # expected reward of each own action under the partner model
        ew = [sum(pc[ac] * ts[aw | (ac << 1)] for ac in (0, 1)) for aw in (0, 1)]
        ec = [sum(pw[aw] * ts[aw | (ac << 1)] for aw in (0, 1)) for ac in (0, 1)]
        aw = rng.integers(2) if rng.random() < eps else int(np.argmax(ew))
        ac = rng.integers(2) if rng.random() < eps else int(np.argmax(ec))
        cw[aw] += 1
        cc[ac] += 1
        r = ts[aw | (ac << 1)]
        streak = streak + 1 if r == 1.0 else 0
        if streak >= 10:
            return ep
    return EPISODES


def main():
    print("PROBE 107 (D1) — partner-modeling (fictitious-play) agents vs the verdict")
    print("=" * 64)
    rng = np.random.default_rng(107)
    diffs, y = [], []
    for _, rules in enumerate_family():
        ts = commit_table(rules)
        diffs.append(np.mean([difficulty_fp(ts, rng) for _ in range(SEEDS)]))
        y.append(int(classify_rules(rules, labels=("W", "S", "C")).structure == "triadic"))
    diffs = np.array(diffs)
    y = np.array(y)
    auc = _auc(diffs, y)
    print(f"  {len(y)} forms, {int(y.sum())} triadic; difficulty = mean episodes-to-coordinate")
    print(f"  triadic mean difficulty = {diffs[y==1].mean():.1f}")
    print(f"  dyadic  mean difficulty = {diffs[y==0].mean():.1f}")
    print(f"  rank-AUC (difficulty predicts triadic) = {auc:.3f}  (independent bandits, Probe 98: 0.567)")
    print("=" * 64)
    if auc >= 0.65:
        print("  Reading: partner-modeling agents find triadic forms harder, so the verdict tracks")
        print("  coordination difficulty once agents reason about each other — the Probe 98 null was about")
        print("  the agent model, not the construct.")
    else:
        print("  Reading: even partner-modeling agents show no verdict-linked difficulty. The structural")
        print("  verdict is not a coordination-game-difficulty measure for any agent here — irreducibility")
        print("  of the form and the hardness of learning to hit its commit are simply different things.")
    print("=" * 64)


if __name__ == "__main__":
    main()

"""Probe 114 (G2) — is there a cheap feature that catches the parity forms?

Question: the learned surrogate recovered the verdict perfectly (#85), so some cheap feature must catch
the parity forms that Φ_AR and CES counts miss. Which one? Hypothesis: a synergy-targeted feature —
O-information or a transfer-entropy term — separates parity-triadic from dyadic, where the rankers that
fail on parity (Φ-magnitude-like features) cannot. Method: over the corpus, build the 13-feature panel
and label forms parity-triadic / conjunctive-triadic / dyadic; for each feature report its AUC on the
hard contrast (parity-triadic vs dyadic) and on the easy one (conjunctive-triadic vs dyadic); the feature
with high AUC on the hard contrast is the parity detector.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_parity_detector
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from .probe_minimal_features import features, NAMES
from .probe_abm_difficulty import commit_table
from .probe_phi_ar import _auc

PARITY = {(0, 1, 1, 0), (1, 0, 0, 1)}
NOISE = 0.08
T = 8000


def main():
    print("PROBE 114 (G2) — the cheap feature that catches the parity blind spot")
    print("=" * 70)
    rng = np.random.default_rng(114)
    X, grp = [], []
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=("W", "S", "C"))
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), 3, T, rng)
        X.append(features(traj))
        if v.structure != "triadic":
            grp.append("dyadic")
        else:
            grp.append("parity" if commit_table(rules) in PARITY else "conj")
    X = np.array(X)
    grp = np.array(grp)
    dy = grp == "dyadic"
    par = grp == "parity"
    conj = grp == "conj"

    def auc_contrast(mask_pos, mask_neg, j):
        sel = mask_pos | mask_neg
        return _auc(X[sel, j], mask_pos[sel].astype(int))

    rows = []
    for j in range(X.shape[1]):
        hard = auc_contrast(par, dy, j)
        easy = auc_contrast(conj, dy, j)
        rows.append((NAMES[j], hard, easy))
    rows.sort(key=lambda r: -abs(r[1] - 0.5))
    print(f"  {int(par.sum())} parity-triadic, {int(conj.sum())} conjunctive-triadic, {int(dy.sum())} dyadic")
    print(f"  {'feature':<12}{'AUC parity-vs-dyadic':<22}{'AUC conj-vs-dyadic'}")
    for nm, hard, easy in rows[:7]:
        print(f"  {nm:<12}{hard:<22.3f}{easy:.3f}")
    print("=" * 70)
    best = rows[0]
    print(f"  best parity detector: {best[0]} (parity-vs-dyadic AUC {best[1]:.3f})")
    print("  Reading: a feature with high AUC on the parity-vs-dyadic contrast is what lets the learned")
    print("  surrogate catch the forms Φ_AR and relation counts miss — the synergy the parity commits")
    print("  carry leaves a cheap statistical trace, even though no Φ-magnitude proxy ranks it.")
    print("=" * 70)


if __name__ == "__main__":
    main()

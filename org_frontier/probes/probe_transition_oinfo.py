"""Probe 83 (#38) — does O-information on the transition structure separate forms better?

Question: Probe 46 found O-information on the present-state joint weakly separates triadic from dyadic
forms. Does computing it on the transition structure — the joint of present and next states — do
better? Hypothesis: it does not improve the separation, because the state-by-node TPM makes the
next-state variables conditionally independent given the present, so the transition's synergy reduces
to the present-state joint already measured. Method: across the 256-form strict-mediation corpus,
classify each, sample triadic and dyadic forms, simulate noisy trajectories, and for each compute
O-information on the present-state triple and on the six-variable (present ⊕ next) joint. Compare the
triadic-vs-dyadic group separation under each measure.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_transition_oinfo
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
from ._info import o_information

LABELS = ("W", "S", "C")
NOISE = 0.08
T = 20000
PER_GROUP = 16


def measures(rules, rng):
    tpm = add_noise(tpm_from_rules(rules), NOISE)
    traj = exact_phi.simulate_trajectory(tpm, 3, T, rng)
    present = o_information(traj[:-1], [0, 1, 2])
    stacked = np.hstack([traj[:-1], traj[1:]])
    transition = o_information(stacked, [0, 1, 2, 3, 4, 5])
    return present, transition


def main():
    print("PROBE 83 (#38) — O-information: present-state joint vs present⊕next transition joint")
    print("=" * 78)
    tri, dya = [], []
    for label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        (tri if v.structure == "triadic" else dya).append(rules)
    rng = np.random.default_rng(5)
    tri_s = [tri[i] for i in rng.choice(len(tri), min(PER_GROUP, len(tri)), replace=False)]
    dya_s = [dya[i] for i in rng.choice(len(dya), min(PER_GROUP, len(dya)), replace=False)]

    def summarize(forms):
        p = np.array([measures(r, rng) for r in forms])
        return p[:, 0], p[:, 1]

    tp, tt = summarize(tri_s)
    dp, dt = summarize(dya_s)
    print(f"  groups: {len(tri_s)} triadic, {len(dya_s)} dyadic   (noise={NOISE}, T={T})")
    print(f"  {'measure':<22}{'triadic mean':<16}{'dyadic mean':<16}{'|gap|'}")
    print(f"  {'present joint':<22}{tp.mean():<16.4f}{dp.mean():<16.4f}{abs(tp.mean()-dp.mean()):.4f}")
    print(f"  {'present⊕next joint':<22}{tt.mean():<16.4f}{dt.mean():<16.4f}{abs(tt.mean()-dt.mean()):.4f}")
    print("=" * 78)
    gp, gt = abs(tp.mean() - dp.mean()), abs(tt.mean() - dt.mean())
    better = gt > gp + 0.02
    print(f"  transition opens a wider group gap than present: {better} ({gt:.4f} vs {gp:.4f})")
    if better:
        print("  Reading: the present⊕next joint separates the groups more than the present-state joint.")
        print("  The transition structure carries discriminating synergy that the static joint misses,")
        print("  though the gap stays modest — a partial gain over Probe 46, not a clean separator.")
    else:
        print("  Reading: the transition joint does not open a wider gap than the present-state joint.")
        print("  Going from present to present⊕next does not rescue O-information as a discriminator.")
    print("=" * 78)


if __name__ == "__main__":
    main()

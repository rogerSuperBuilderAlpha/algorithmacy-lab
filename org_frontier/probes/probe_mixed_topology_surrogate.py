"""Probe 129 (N2) — does mixed-topology training fix the surrogate's family-specificity?

Question: the surrogate trained on strict mediation fails across topology (#123, 40% on new families). Is
that a training-distribution limit a more diverse training set fixes? Hypothesis: training on a mix —
strict mediation plus random arbitrary wirings at n=3 and n=4 — generalizes to the held-out topology
archetypes where strict-mediation-only training did not. Method: build two training sets (strict-mediation
only; strict-mediation plus random arbitrary wirings), score each against the same held-out archetype
forms (single-hub, OR-hub, chain, pool, parity, majority, two-hub).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_mixed_topology_surrogate
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.ensemble import RandomForestClassifier

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from proxy_audit import exact_phi
from .probe_surrogate_transfer import feats
from .probe_ood_surrogate import ood_forms

NOISE = 0.08
T = 4000


def random_wiring(n, rng):
    """Each node an arbitrary Boolean function of all the others — a topologically diverse family."""
    rules = [None] * n
    for i in range(n):
        ins = tuple(j for j in range(n) if j != i)
        table = rng.integers(0, 2, 2 ** len(ins))
        rules[i] = (lambda x, ins=ins, t=table: int(t[sum((x[ins[k]] & 1) << k for k in range(len(ins)))]))
    return rules


def featurize(forms_n, rng):
    X, y = [], []
    for n, rules in forms_n:
        labels = tuple(f"x{i}" for i in range(n))
        v = classify_rules(rules, labels=labels)
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), n, T, rng)
        X.append(feats(traj, n))
        y.append(int(v.structure == "triadic"))
    return np.array(X), np.array(y)


def main():
    print("PROBE 129 (N2) — mixed-topology training vs strict-mediation-only")
    print("=" * 64)
    rng = np.random.default_rng(129)
    Xsm, ysm = featurize([(3, r) for _, r in enumerate_family()], rng)
    rand = [(3, random_wiring(3, rng)) for _ in range(300)] + [(4, random_wiring(4, rng)) for _ in range(300)]
    Xr, yr = featurize(rand, rng)
    Xmix = np.vstack([Xsm, Xr])
    ymix = np.concatenate([ysm, yr])

    test = [(rules, n) for _, rules, n in ood_forms()]
    Xte, yte = [], []
    for rules, n in test:
        labels = tuple(f"x{i}" for i in range(n))
        yte.append(int(classify_rules(rules, labels=labels).structure == "triadic"))
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), n, T, rng)
        Xte.append(feats(traj, n))
    Xte, yte = np.array(Xte), np.array(yte)

    def score(X, y, tag):
        clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1).fit(X, y)
        acc = (clf.predict(Xte) == yte).mean()
        print(f"  {tag:<42}{int((clf.predict(Xte)==yte).sum())}/{len(yte)} ({100*acc:.0f}%)")
        return acc

    baseline = max(yte.mean(), 1 - yte.mean())
    print(f"  held-out archetype forms: {len(yte)} ({int(yte.sum())} triadic); majority baseline = {baseline:.0%}")
    a = score(Xsm, ysm, "trained on strict-mediation only")
    b = score(Xmix, ymix, "trained on strict-mediation + random wirings")
    print("=" * 64)
    if b > a + 0.05 and b > baseline:
        print(f"  Reading: diverse training lifts archetype accuracy from {a:.0%} to {b:.0%}, above the")
        print(f"  {baseline:.0%} majority baseline. The family-specificity of #123 is a training-distribution")
        print("  limit a varied training set fixes.")
    elif b > a + 0.05:
        print(f"  Reading: diverse training lifts accuracy from {a:.0%} to {b:.0%}, yet both sit below the")
        print(f"  {baseline:.0%} majority baseline. Mixing topologies broadens the signal but does not reach")
        print("  cross-topology generalization — the cheap features carry a family-specific verdict signal")
        print("  that diverse data only partly widens. The screen stays family-bound.")
    else:
        print(f"  Reading: diverse training does not close the gap ({a:.0%} to {b:.0%}); the screen stays")
        print("  family-specific.")
    print("=" * 64)


if __name__ == "__main__":
    main()

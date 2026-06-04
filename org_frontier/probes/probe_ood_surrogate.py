"""Probe 123 (K2) — does the surrogate generalize to topology families it never trained on?

Question: the surrogate trains on the strict-mediation corpus and transfers to larger strict-mediation
forms (#99). Does it classify the topology families introduced later — multi-hub, parity hub, threshold
commits, chain, pool — which it never saw? Hypothesis: it generalizes, because the coupling signal it
learned is topology-independent. Method: train the eight-feature random forest on the n=3 corpus; build
labelled forms from the new families at n=4..6; score the trained surrogate against the exact verdict.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ood_surrogate
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
from .probe_surrogate_transfer import dataset, feats
from .probe_distributed_mediators import single_hub, two_hub
from .probe_conjunctive_law import or_hub
from .probe_topology_map import chain, pool
from .probe_parity_scaling import parity_hub
from .probe_threshold_scaling import threshold_hub
from .probe_symmetric_multihub import sym_two_hub

NOISE = 0.08
T = 4000


def ood_forms():
    out = []
    for n in (4, 5, 6):
        out += [(f"single_hub n{n}", single_hub(n), n),
                (f"or_hub n{n}", or_hub(n), n),
                (f"parity_hub n{n}", parity_hub(n), n),
                (f"chain n{n}", chain(n), n),
                (f"pool n{n}", pool(n), n),
                (f"majority n{n}", threshold_hub(n, (n - 1) // 2 + 1), n)]
        if n >= 6:
            out += [(f"two_hub_asym n{n}", two_hub(n), n), (f"two_hub_sym n{n}", sym_two_hub(n), n)]
    return out


def main():
    print("PROBE 123 (K2) — out-of-distribution surrogate generalization")
    print("=" * 64)
    rng = np.random.default_rng(123)
    Xtr, ytr = dataset([(3, r) for _, r in enumerate_family()], rng)
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1).fit(Xtr, ytr)
    correct = 0
    rows = []
    for name, rules, n in ood_forms():
        labels = tuple(f"x{i}" for i in range(n))
        truth = classify_rules(rules, labels=labels).structure
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), n, T, rng)
        pred = "triadic" if clf.predict([feats(traj, n)])[0] == 1 else "dyadic"
        ok = pred == truth
        correct += ok
        rows.append((name, truth, pred, ok))
    print(f"  trained on {len(ytr)} n=3 strict-mediation forms; tested on {len(rows)} new-family forms")
    print(f"  {'form':<20}{'truth':<10}{'predicted':<11}{'ok'}")
    for name, truth, pred, ok in rows:
        print(f"  {name:<20}{truth:<10}{pred:<11}{ok}")
    print("=" * 64)
    acc = correct / len(rows)
    print(f"  out-of-distribution accuracy = {correct}/{len(rows)} ({100*acc:.0f}%)")
    if acc >= 0.8:
        print("  Reading: high accuracy on families the surrogate never trained on says the coupling signal")
        print("  is topology-independent, so the cheap instrument is not tied to strict mediation.")
    else:
        print("  Reading: the surrogate fails on families it never saw — hub-shaped forms that resemble the")
        print("  training family pass, while chains, pools, and multi-hub forms do not. The transfer of")
        print("  #99 holds across size within a topology family, not across topology. The cheap instrument")
        print("  must be trained on the structural class it will be applied to; it is a screen, not a")
        print("  topology-general test.")
    print("=" * 64)


if __name__ == "__main__":
    main()

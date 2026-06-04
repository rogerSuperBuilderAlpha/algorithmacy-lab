"""Probe 64 (#14) — predicting the major complex from the coupling graph alone.

Question: can the irreducible core be predicted from connectivity without computing Φ? Hypothesis: the
bidirectional-coupling rule (a node is in the core iff it both reads and is read within the
determination) predicts the core well but not perfectly, leaving the holistic residual (cf. #13, #44).
Method: sample strict-mediation n=4 forms, predict the core as {S} ∪ {outer parties bidirectionally
coupled to S}, and compare with the actual major complex. Report exact-set match and node-level
precision/recall.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_team_core_rule [N] [seed]
"""

import sys

import numpy as np

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.multiparty.scaling import sample_form
from .lib import major_complex

LABELS = ("W", "S", "C1", "C2")


def predicted_core(cm, labels):
    # S is index 1; outer indices are the rest. Bidirectional = S reads i AND i reads S.
    core = set()
    s = 1
    bidir = [i for i in range(len(labels)) if i != s and cm[i, s] and cm[s, i]]
    if bidir:
        core = {labels[s]} | {labels[i] for i in bidir}
    return core


def main(N=300, seed=7):
    rng = np.random.default_rng(seed)
    exact = node_tp = node_fp = node_fn = total_nodes = 0
    for _ in range(N):
        rules = sample_form(4, rng)
        cm = cm_from_rules(rules)
        actual, _ = major_complex(rules, LABELS)
        actual = set(actual or ())
        pred = predicted_core(cm, LABELS)
        exact += (pred == actual)
        for lab in LABELS:
            total_nodes += 1
            inp, ina = lab in pred, lab in actual
            node_tp += inp and ina
            node_fp += inp and not ina
            node_fn += (not inp) and ina
    prec = node_tp / (node_tp + node_fp) if node_tp + node_fp else float("nan")
    rec = node_tp / (node_tp + node_fn) if node_tp + node_fn else float("nan")
    print("PROBE 64 (#14) — graph-only prediction of the major complex (n=4 sample)")
    print("=" * 72)
    print(f"  forms: {N}")
    print(f"  exact core-set match: {100*exact/N:.1f}%")
    print(f"  node-level precision={prec:.3f}  recall={rec:.3f}  (FP={node_fp} FN={node_fn})")
    print("=" * 72)
    print("  Reading: the bidirectional-coupling rule recovers the core graph-only to this accuracy;")
    print("  the shortfall is the holistic residual Φ captures and connectivity cannot.")
    print("=" * 72)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    main(N, seed)

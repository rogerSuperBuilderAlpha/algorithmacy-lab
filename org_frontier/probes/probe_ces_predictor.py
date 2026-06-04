"""Probe 93 (#2) — do cause-effect-structure counts predict the verdict?

Question: per-node influence does not by itself predict triadicity on the full family. Does the
cause-effect structure (CES) — the count of distinctions and relations PyPhi's phi_structure returns —
predict it? Hypothesis: relation and distinction counts separate triadic from dyadic forms well, because
an irreducible third party shows up as higher-order relations a per-node feature cannot see. Method:
over the 256-form corpus, compute the Φ-structure suite on a reachable state of each form, and report
the rank-AUC of each CES count against the exact verdict, plus a combined logistic model.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ces_predictor
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_auc_score

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family
from proxy_audit.exact_phi import reachable_states
from structure_suite.suite import extract_suite
from .probe_phi_ar import _auc

LABELS = ("W", "S", "C")
FEATURES = ("n_distinctions", "n_relations", "frac_higher_order", "mean_order")


def main():
    print("PROBE 93 (#2) — CES distinction/relation counts vs the verdict")
    print("=" * 64)
    X, y, skipped = [], [], 0
    for _, rules in enumerate_family():
        sbn = tpm_from_rules(rules)
        rs = reachable_states(sbn, 3)
        if not rs:
            skipped += 1
            continue
        state = [(rs[0] >> i) & 1 for i in range(3)]
        suite = extract_suite(sbn, cm_from_rules(rules), 3, state)
        if suite is None:
            skipped += 1
            continue
        v = classify_rules(rules, labels=LABELS)
        X.append([suite[k] for k in FEATURES])
        y.append(int(v.structure == "triadic"))
    X = np.array(X, float)
    y = np.array(y)
    print(f"  {len(y)} forms scored ({int(y.sum())} triadic), {skipped} skipped (unreachable)")
    print(f"  {'CES feature':<20}{'rank-AUC'}")
    for j, name in enumerate(FEATURES):
        print(f"  {name:<20}{_auc(X[:, j], y):.3f}")
    clf = LogisticRegression(max_iter=1000)
    p = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    print("=" * 64)
    print(f"  combined CES logistic CV-AUC = {roc_auc_score(y, p):.3f}")
    print("  Reading: high AUC for relation/distinction counts says the cause-effect structure carries")
    print("  the verdict where per-node influence does not — an irreducible third party appears as")
    print("  higher-order structure. A low AUC would say even CES counts miss it.")
    print("=" * 64)


if __name__ == "__main__":
    main()

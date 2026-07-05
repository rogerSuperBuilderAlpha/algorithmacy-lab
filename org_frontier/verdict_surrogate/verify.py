"""Deterministic reproduce check for CI.

Re-derives the arm's headline numbers from the committed dataset.csv and prints PASS/FAIL against the
pre-registered lines, plus a landmark exact-Φ verdict as a determinism anchor. Threshold comparisons
(not exact-string matches) keep the check robust to small numerical drift across environments while
still failing if a claim breaks. See hypotheses.md for the pre-registered lines.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.verify
"""

import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

from .forms import FEATURE_KEYS, DYNAMICAL_KEYS, chain, all_required
from org_frontier.classifier.classifier import classify_rules

_DATASET = os.path.join(os.path.dirname(__file__), "results", "dataset.csv")
SEED = 0


def _rf():
    return RandomForestClassifier(n_estimators=400, min_samples_leaf=2,
                                  class_weight="balanced", random_state=SEED, n_jobs=-1)


def main():
    # Landmark exact verdicts (deterministic; anchors the oracle the surrogate is judged against).
    v4 = classify_rules(chain(2)[0])
    va = classify_rules(all_required(4)[0])
    print(f"landmark: chain n=4 {v4.structure} Φ={v4.max_phi:.3f}; "
          f"all_required n=4 {va.structure} Φ={va.max_phi:.3f}")
    ok_landmark = (v4.structure == "triadic" and abs(v4.max_phi - 2.0) < 1e-3
                   and va.structure == "triadic" and abs(va.max_phi - 3.0) < 1e-3)
    print(f"  landmark exact verdicts hold: {'PASS' if ok_landmark else 'FAIL'}")

    df = pd.read_csv(_DATASET)
    train = df[df["split"] == "train"].reset_index(drop=True)
    y = train["triadic"].to_numpy()

    # H1: learned all-features CV AUC vs best single dynamical proxy.
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    proba = cross_val_predict(_rf(), train[FEATURE_KEYS].to_numpy(), y, cv=skf,
                              method="predict_proba", n_jobs=-1)[:, 1]
    auc_learned = roc_auc_score(y, proba)
    proxy_auc = max(max(roc_auc_score(y, train[k]), 1 - roc_auc_score(y, train[k]))
                    for k in DYNAMICAL_KEYS)
    print(f"H1: learned AUC {auc_learned:.3f}  vs best single proxy {proxy_auc:.3f}")
    ok_h1 = auc_learned >= 0.85 and auc_learned > proxy_auc
    print(f"  H1 learned AUC >= 0.85 and beats single proxy: {'PASS' if ok_h1 else 'FAIL'}")

    # H1 back-channel discount.
    bc = (train["has_backchannel"] == 1).to_numpy()
    proxy_key = max(DYNAMICAL_KEYS,
                    key=lambda k: max(roc_auc_score(y, train[k]), 1 - roc_auc_score(y, train[k])))
    pv = train[proxy_key].to_numpy()
    orient = 1 if roc_auc_score(y, pv) >= 0.5 else -1
    proxy_call = ((orient * pv) > (orient * np.median(pv))).astype(int)
    learned_call = (proba > 0.5).astype(int)
    la = (learned_call[bc] == y[bc]).mean()
    pa = (proxy_call[bc] == y[bc]).mean()
    print(f"H1: back-channel forms learned acc {la:.3f} vs single-proxy acc {pa:.3f}")
    ok_bc = la > pa
    print(f"  H1 back-channel discount (learned > single proxy): {'PASS' if ok_bc else 'FAIL'}")

    # H2: train n<=5, pooled held-out AUC on n>=6.
    test = df[df["split"] == "test"].reset_index(drop=True)
    if len(test) and test["triadic"].nunique() > 1:
        rf = _rf().fit(train[FEATURE_KEYS].to_numpy(), y)
        tp = rf.predict_proba(test[FEATURE_KEYS].to_numpy())[:, 1]
        auc_test = roc_auc_score(test["triadic"].to_numpy(), tp)
        print(f"H2: pooled held-out (n>=6) AUC {auc_test:.3f} on {len(test)} forms "
              f"({int(test['triadic'].sum())} triadic)")
        ok_h2 = auc_test > 0.75
        print(f"  H2 pooled held-out AUC > 0.75: {'PASS' if ok_h2 else 'FAIL'}")
    else:
        print("H2: no held-out test forms with both classes in dataset.csv (build with --max-n 8)")


if __name__ == "__main__":
    main()

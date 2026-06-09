"""Probe Q81 (H1-H4) — a learned surrogate for the outreach verdict, and whether it crosses sizes.

Trains a random forest over the 10 size-invariant cheap features (intensive trajectory statistics) on
the 256-form n=3 outreach family, labelled by exact IIT-4.0 Φ. Measures in-distribution recovery
(5-fold CV ROC-AUC and accuracy), then trains on the full n=3 family and tests on held-out outreach
forms at n = 4, 5, 6 that the surrogate never saw — the generalization-past-the-size-ceiling test.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q81_learned_surrogate.probe_learned_surrogate
"""

import csv
import os

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score

from org_frontier.questions.q81_learned_surrogate import forms as F

TRAIN_SEED = 7
EVAL_SEEDS = (1, 2, 3)


def _rf():
    return RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)


def main():
    print("PROBE Q81 (H1-H4) — learned surrogate for the outreach verdict")
    print("=" * 78)

    # In-distribution: the n=3 outreach family.
    X3, y3, _ = F.build_n3_matrix(np.random.default_rng(TRAIN_SEED))
    base = float(max(y3.mean(), 1 - y3.mean()))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    proba = cross_val_predict(_rf(), X3, y3, cv=cv, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    cv_acc = accuracy_score(y3, pred)
    cv_auc = roc_auc_score(y3, proba)
    print(f"  n=3 family: {len(y3)} forms ({int(y3.sum())} triadic, {len(y3) - int(y3.sum())} dyadic), "
          f"{X3.shape[1]} intensive features")
    print(f"  majority-class baseline accuracy : {base:.3f}")
    print(f"  surrogate 5-fold CV accuracy      : {cv_acc:.3f}")
    print(f"  surrogate 5-fold CV ROC-AUC       : {cv_auc:.3f}")

    # Generalization: train on full n=3, test on held-out n = 4, 5, 6 forms.
    clf = _rf().fit(X3, y3)
    larger_base = None
    accs, recalls = [], []
    print("  --- generalization to held-out larger forms (n = 4, 5, 6) ---")
    for s in EVAL_SEEDS:
        Xl, yl, _ = F.build_larger_matrix(np.random.default_rng(s))
        if larger_base is None:
            larger_base = float(max(yl.mean(), 1 - yl.mean()))
        p = clf.predict(Xl)
        a = accuracy_score(yl, p)
        r = recall_score(yl, p, pos_label=0)         # dyadic recall: not just predicting triadic
        accs.append(a)
        recalls.append(r)
        print(f"    seed {s}: {len(yl)} forms, accuracy={a:.3f}, dyadic recall={r:.3f}")
    gen_acc = float(np.mean(accs))
    gen_recall = float(np.mean(recalls))
    print(f"  held-out majority baseline        : {larger_base:.3f}")
    print(f"  mean generalization accuracy      : {gen_acc:.3f}")
    print(f"  mean held-out dyadic recall       : {gen_recall:.3f}")

    h1 = cv_auc >= 0.85
    h2 = cv_acc >= base + 0.10
    h3 = gen_acc >= 0.75
    h4 = gen_recall >= 0.50
    print("=" * 78)
    print(f"  H1 in-distribution CV ROC-AUC >= 0.85: {h1} ({cv_auc:.3f})")
    print(f"  H2 CV accuracy >= majority + 0.10:     {h2} ({cv_acc:.3f} vs {base + 0.10:.3f})")
    print(f"  H3 mean generalization accuracy >= 0.75: {h3} ({gen_acc:.3f})")
    print(f"  H4 mean held-out dyadic recall >= 0.50:  {h4} ({gen_recall:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "learned_surrogate.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["metric", "value"])
        w.writerow(["n3_majority_baseline", f"{base:.4f}"])
        w.writerow(["cv_accuracy", f"{cv_acc:.4f}"])
        w.writerow(["cv_roc_auc", f"{cv_auc:.4f}"])
        w.writerow(["larger_majority_baseline", f"{larger_base:.4f}"])
        for s, a, r in zip(EVAL_SEEDS, accs, recalls):
            w.writerow([f"gen_accuracy_seed{s}", f"{a:.4f}"])
            w.writerow([f"gen_dyadic_recall_seed{s}", f"{r:.4f}"])
        w.writerow(["gen_accuracy_mean", f"{gen_acc:.4f}"])
        w.writerow(["gen_dyadic_recall_mean", f"{gen_recall:.4f}"])


if __name__ == "__main__":
    main()

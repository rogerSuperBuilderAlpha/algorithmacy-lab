"""Does the surrogate generalize to LARGER systems than it was trained on?

The central worry for any cheap Φ surrogate (e.g. Hosaka et al.'s GNN) is
extrapolation: it is trained where exact Φ is computable (small systems) but
must be used where it is not (large systems). We probe this directly:

  - within-data size step: train on n=3 networks, test on n=4 (and vice versa);
  - genuine out-of-size: train on all n∈{3,4}, test on a fresh n=5 set.

We report how much the surrogate degrades out-of-size relative to its
in-distribution cross-validated performance.

Usage:
    python -m learned_surrogate.extrapolate
"""

import csv

import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

from .build_dataset import FEATURE_KEYS

TRAIN_PATH = "learned_surrogate/results/dataset.csv"
TEST_N5_PATH = "learned_surrogate/results/test_n5.csv"
SUMMARY_PATH = "learned_surrogate/results/extrapolation_summary.csv"


def _spearman(x, y):
    def rank(a):
        a = np.asarray(a, float)
        u, inv, c = np.unique(a, return_inverse=True, return_counts=True)
        avg, s = {}, 0
        for k, cc in enumerate(c):
            avg[k] = (2 * s + cc - 1) / 2.0
            s += cc
        return np.array([avg[i] for i in inv])
    rx, ry = rank(x), rank(y)
    if rx.std() < 1e-12 or ry.std() < 1e-12:
        return 0.0
    return float(np.corrcoef(rx, ry)[0, 1])


def _auc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, bool)
    npos, nneg = labels.sum(), (~labels).sum()
    if npos == 0 or nneg == 0:
        return float("nan")
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(len(scores), float)
    ranks[order] = np.arange(1, len(scores) + 1)
    u, inv = np.unique(scores, return_inverse=True)
    for k in range(len(u)):
        m = inv == k
        ranks[m] = ranks[m].mean()
    return float((ranks[labels].sum() - npos * (npos + 1) / 2) / (npos * nneg))


def _load(path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    X = np.array([[float(r[k]) for k in FEATURE_KEYS] for r in rows])
    phi = np.array([float(r["phi_mean"]) for r in rows])
    n = np.array([int(float(r["n"])) for r in rows])
    return X, phi, n


def _evaluate(Xtr, ytr, Xte, yte, label):
    """Train on (Xtr, ytr), evaluate regression ρ and detection AUC on test."""
    pos_tr = (ytr > 1e-6).astype(int)
    pos_te = yte > 1e-6
    reg = RandomForestRegressor(n_estimators=300, random_state=0, n_jobs=-1).fit(Xtr, ytr)
    rho = _spearman(reg.predict(Xte), yte)
    auc = float("nan")
    if pos_tr.sum() > 0 and pos_tr.sum() < len(pos_tr) and pos_te.sum() and (~pos_te).sum():
        clf = RandomForestClassifier(n_estimators=300, random_state=0, n_jobs=-1).fit(Xtr, pos_tr)
        auc = _auc(clf.predict_proba(Xte)[:, 1], pos_te)
    print(f"  {label:<34} ρ={rho:+.3f}   AUC(Φ>0)={auc:.3f}   "
          f"(test n={len(yte)}, Φ>0: {int(pos_te.sum())})")
    return {"setting": label, "spearman": rho, "auc_phi_positive": auc,
            "n_test": len(yte), "n_test_positive": int(pos_te.sum())}


def main():
    X, phi, n = _load(TRAIN_PATH)
    rows = []
    print("\nSize extrapolation of the learned surrogate (train -> test):\n")

    # Within-data: n=3 <-> n=4.
    m3, m4 = n == 3, n == 4
    rows.append(_evaluate(X[m3], phi[m3], X[m4], phi[m4], "train n=3  ->  test n=4"))
    rows.append(_evaluate(X[m4], phi[m4], X[m3], phi[m3], "train n=4  ->  test n=3"))

    # Genuine out-of-size: train on all n in {3,4}, test on fresh n=5.
    try:
        X5, phi5, _ = _load(TEST_N5_PATH)
        rows.append(_evaluate(X, phi, X5, phi5, "train n=3,4  ->  test n=5 (unseen)"))
    except FileNotFoundError:
        print("  (n=5 test set not found; run build_test_set first.)")

    print("\nReference (in-distribution, 5-fold CV from train.py): ρ≈0.54, AUC≈0.90")

    with open(SUMMARY_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["setting", "spearman", "auc_phi_positive",
                                          "n_test", "n_test_positive"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {SUMMARY_PATH}")


if __name__ == "__main__":
    main()

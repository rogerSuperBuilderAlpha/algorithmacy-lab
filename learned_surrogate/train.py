"""Train and cross-validate surrogate models that predict exact IIT-4.0 Φ from
cheap features, and compare them to the best single feature.

Two tasks:
  - regression: predict Φ (mean over reachable states);
  - detection:  classify Φ > 0.

All scores are honest out-of-fold (cross_val_predict, 5-fold), so they reflect
generalization, not fit. We compare a linear model (Ridge) and a random forest
to the best single feature, to see whether *combining* cheap features recovers
what no single one captured.

Usage:
    python -m learned_surrogate.train
"""

import csv

import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_predict, KFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from .build_dataset import FEATURE_KEYS

DATA_PATH = "learned_surrogate/results/dataset.csv"
SUMMARY_PATH = "learned_surrogate/results/surrogate_summary.csv"
PLOT_PATH = "learned_surrogate/results/surrogate.png"


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


def load():
    with open(DATA_PATH) as f:
        rows = list(csv.DictReader(f))
    X = np.array([[float(r[k]) for k in FEATURE_KEYS] for r in rows])
    phi = np.array([float(r["phi_mean"]) for r in rows])
    return X, phi


def main():
    X, phi = load()
    pos = (phi > 1e-6).astype(int)
    n = len(phi)
    print(f"\nLearned surrogate: {n} networks, {int(pos.sum())} with Φ>0, "
          f"{len(FEATURE_KEYS)} features\n")

    kf = KFold(n_splits=5, shuffle=True, random_state=0)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

    # ---- regression: predict Φ ----
    print("REGRESSION (predict Φ) — out-of-fold Spearman ρ vs true Φ:")
    best_feat_rho = max(abs(_spearman(X[:, i], phi)) for i in range(len(FEATURE_KEYS)))
    best_feat_name = FEATURE_KEYS[int(np.argmax([abs(_spearman(X[:, i], phi))
                                                 for i in range(len(FEATURE_KEYS))]))]
    ridge = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    rf = RandomForestRegressor(n_estimators=300, random_state=0, n_jobs=-1)
    pred_ridge = cross_val_predict(ridge, X, phi, cv=kf)
    pred_rf = cross_val_predict(rf, X, phi, cv=kf)
    rho_ridge, rho_rf = _spearman(pred_ridge, phi), _spearman(pred_rf, phi)
    print(f"  best single feature ({best_feat_name}): {best_feat_rho:.3f}")
    print(f"  Ridge (linear combo):                   {rho_ridge:.3f}")
    print(f"  Random forest:                          {rho_rf:.3f}")

    # ---- detection: classify Φ>0 ----
    print("\nDETECTION (classify Φ>0) — out-of-fold AUC:")
    best_feat_auc = max(max(_auc(X[:, i], pos), 1 - _auc(X[:, i], pos))
                        for i in range(len(FEATURE_KEYS)))
    rfc = RandomForestClassifier(n_estimators=300, random_state=0, n_jobs=-1)
    proba = cross_val_predict(rfc, X, pos, cv=skf, method="predict_proba")[:, 1]
    auc_rf = _auc(proba, pos)
    print(f"  best single feature: {best_feat_auc:.3f}")
    print(f"  Random forest:       {auc_rf:.3f}")

    # ---- feature importances (fit on all data, for inspection) ----
    rf.fit(X, phi)
    imp = sorted(zip(FEATURE_KEYS, rf.feature_importances_), key=lambda t: -t[1])
    print("\nRandom-forest feature importances (regression):")
    for k, v in imp:
        print(f"  {k:<24} {v:.3f}")

    with open(SUMMARY_PATH, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["task", "model", "score"])
        w.writerow(["regression_spearman", "best_single_feature", best_feat_rho])
        w.writerow(["regression_spearman", "ridge", rho_ridge])
        w.writerow(["regression_spearman", "random_forest", rho_rf])
        w.writerow(["detection_auc", "best_single_feature", best_feat_auc])
        w.writerow(["detection_auc", "random_forest", auc_rf])
        w.writerow([])
        w.writerow(["feature_importance", "feature", "importance"])
        for k, v in imp:
            w.writerow(["", k, v])
    print(f"\nWrote {SUMMARY_PATH}")
    _plot(phi, pred_rf, imp)


def _plot(phi, pred_rf, imp):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plot.")
        return
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    axes[0].scatter(pred_rf, phi, s=14, alpha=0.5, edgecolors="none")
    lim = [min(pred_rf.min(), phi.min()), max(pred_rf.max(), phi.max())]
    axes[0].plot(lim, lim, "k--", lw=1, alpha=0.6)
    axes[0].set_xlabel("predicted Φ (random forest, out-of-fold)")
    axes[0].set_ylabel("exact IIT-4.0 Φ")
    axes[0].set_title(f"Learned surrogate (ρ = {_spearman(pred_rf, phi):.2f})")
    names = [k for k, _ in imp][::-1]
    vals = [v for _, v in imp][::-1]
    axes[1].barh(names, vals)
    axes[1].set_xlabel("RF feature importance")
    axes[1].set_title("Which cheap features matter")
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=120, bbox_inches="tight")
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()

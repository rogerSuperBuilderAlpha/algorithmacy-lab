"""H1 -- rescue: does a learned combination of cheap features recover the coordination verdict
within the n <= 5 training pool, beating the single-proxy ceiling and the structural-only heuristic?

Reports, all cross-validated (stratified 5-fold, out-of-fold predictions) inside the training pool:
  * learned model (random forest) on all cheap features -> AUC for triadic vs dyadic;
  * the best single dynamical proxy at its rank threshold -> AUC (the proxy_bridge comparator);
  * the structural-only heuristic (strict mediation AND mediator reads >= 2 parties);
  * an ablation: structural-only vs dynamical-only vs both feature blocks;
  * the back-channel discount: on forms with a real back-channel, does the learned model call the
    verdict where the single proxy fails?
Writes results/train.json and results/train.png.
"""

import json
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

from .forms import FEATURE_KEYS, STRUCTURAL_KEYS, DYNAMICAL_KEYS

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
_DATASET = os.path.join(_RESULTS, "dataset.csv")
SEED = 0
N_SPLITS = 5


def _rf():
    return RandomForestClassifier(n_estimators=400, min_samples_leaf=2,
                                  class_weight="balanced", random_state=SEED, n_jobs=-1)


def _cv_auc(X, y, model):
    """Out-of-fold AUC via cross_val_predict probabilities."""
    skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    proba = cross_val_predict(model, X, y, cv=skf, method="predict_proba", n_jobs=-1)[:, 1]
    return roc_auc_score(y, proba), proba


def _single_proxy_auc(df, y):
    """Best single dynamical proxy by rank-AUC (matches proxy_bridge's comparator)."""
    best = None
    for key in DYNAMICAL_KEYS:
        v = df[key].to_numpy()
        auc = roc_auc_score(y, v)
        auc = max(auc, 1 - auc)              # a proxy may point either way; take its best orientation
        if best is None or auc > best[1]:
            best = (key, auc)
    return best


def _structural_heuristic(df):
    """The corpus arm's rule: strict mediation (no bypassing edge) AND mediator reads >= 2 parties.
    In feature terms: is_strict_star AND hub_fanin >= 2."""
    return ((df["is_strict_star"] == 1) & (df["hub_fanin"] >= 2)).astype(int).to_numpy()


def main():
    df = pd.read_csv(_DATASET)
    train = df[df["split"] == "train"].reset_index(drop=True)
    y = train["triadic"].to_numpy()
    print(f"Training pool: {len(train)} forms, {y.sum()} triadic ({100*y.mean():.1f}%).")
    if y.sum() < 5 or (len(y) - y.sum()) < 5:
        print("WARNING: too few of one class for a stable AUC.")

    X_all = train[FEATURE_KEYS].to_numpy()
    X_struct = train[STRUCTURAL_KEYS].to_numpy()
    X_dyn = train[DYNAMICAL_KEYS].to_numpy()

    auc_all, proba_all = _cv_auc(X_all, y, _rf())
    auc_struct, _ = _cv_auc(X_struct, y, _rf())
    auc_dyn, _ = _cv_auc(X_dyn, y, _rf())
    proxy_key, proxy_auc = _single_proxy_auc(train, y)

    heur = _structural_heuristic(train)
    heur_auc = roc_auc_score(y, heur)
    heur_bacc = balanced_accuracy_score(y, heur)

    # Back-channel discount: forms with a real back-channel edge.
    bc = train["has_backchannel"] == 1
    proxy_vals = train[proxy_key].to_numpy()
    thr = np.median(proxy_vals)             # a nominal proxy threshold
    orient = 1 if roc_auc_score(y, proxy_vals) >= 0.5 else -1
    proxy_call = ((orient * proxy_vals) > (orient * thr)).astype(int)
    learned_call = (proba_all > 0.5).astype(int)
    bc_report = {}
    if bc.sum() > 0:
        ybc = y[bc.to_numpy()]
        bc_report = {
            "n_backchannel_forms": int(bc.sum()),
            "learned_balanced_acc": float(balanced_accuracy_score(ybc, learned_call[bc.to_numpy()]))
            if len(set(ybc)) > 1 else None,
            "single_proxy_balanced_acc": float(balanced_accuracy_score(ybc, proxy_call[bc.to_numpy()]))
            if len(set(ybc)) > 1 else None,
            "learned_acc": float((learned_call[bc.to_numpy()] == ybc).mean()),
            "single_proxy_acc": float((proxy_call[bc.to_numpy()] == ybc).mean()),
        }

    # Feature importances on a full-data fit (reporting only).
    rf = _rf().fit(X_all, y)
    imp = sorted(zip(FEATURE_KEYS, rf.feature_importances_), key=lambda t: -t[1])[:10]

    results = {
        "n_train": int(len(train)),
        "n_triadic": int(y.sum()),
        "auc_learned_all": round(auc_all, 4),
        "auc_learned_structural_only": round(auc_struct, 4),
        "auc_learned_dynamical_only": round(auc_dyn, 4),
        "best_single_proxy": proxy_key,
        "auc_best_single_proxy": round(proxy_auc, 4),
        "proxy_bridge_reference_auc": 0.629,
        "structural_heuristic_auc": round(heur_auc, 4),
        "structural_heuristic_balanced_acc": round(heur_bacc, 4),
        "backchannel_discount": bc_report,
        "top_importances": [(k, round(float(v), 4)) for k, v in imp],
    }
    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "train.json"), "w") as fh:
        json.dump(results, fh, indent=2)

    print("=" * 78)
    print("H1 -- RESCUE (cross-validated within n<=5 pool)")
    print("=" * 78)
    print(f"  learned model, all features      AUC = {auc_all:.3f}")
    print(f"  learned model, structural only   AUC = {auc_struct:.3f}")
    print(f"  learned model, dynamical only    AUC = {auc_dyn:.3f}")
    print(f"  best single proxy ({proxy_key})  AUC = {proxy_auc:.3f}   "
          f"[proxy_bridge ref 0.629]")
    print(f"  structural heuristic             AUC = {heur_auc:.3f}  bacc = {heur_bacc:.3f}")
    if bc_report:
        print(f"  back-channel forms ({bc_report['n_backchannel_forms']}): "
              f"learned acc {bc_report['learned_acc']:.3f} vs "
              f"single-proxy acc {bc_report['single_proxy_acc']:.3f}")
    print("  top features:", ", ".join(f"{k}={v:.2f}" for k, v in imp[:6]))
    print(f"  wrote {os.path.join(_RESULTS, 'train.json')}")

    _plot(results)


def _plot(results):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return
    labels = ["single proxy\n(proxy_bridge)", "structural\nheuristic",
              "learned\ndynamical", "learned\nstructural", "learned\nall"]
    vals = [results["auc_best_single_proxy"], results["structural_heuristic_auc"],
            results["auc_learned_dynamical_only"], results["auc_learned_structural_only"],
            results["auc_learned_all"]]
    fig, ax = plt.subplots(figsize=(7, 4))
    colors = ["#b0b0b0", "#b0b0b0", "#7aa6c2", "#7aa6c2", "#2a6f97"]
    ax.bar(labels, vals, color=colors)
    ax.axhline(0.5, ls=":", c="k", lw=0.8)
    ax.axhline(0.85, ls="--", c="#c1121f", lw=0.8, label="pre-registered H1 line (0.85)")
    ax.set_ylabel("AUC (triadic vs dyadic)")
    ax.set_ylim(0.4, 1.0)
    ax.set_title("Recovering the coordination verdict within n<=5")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(_RESULTS, "train.png"), dpi=130)


if __name__ == "__main__":
    main()

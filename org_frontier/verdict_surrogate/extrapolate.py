"""H2 -- extrapolation: trained only on n <= 5, does the learned verdict recover at the held-out
sizes n in {6,7,8}, where exact Φ is too expensive to label a population?

Trains a random forest on the whole n <= 5 pool and predicts on the held-out large-n forms. Reports
per size: AUC (when both classes are present), balanced accuracy, recall on the rare triadic class,
and the screen recall -- the fraction of true triads a top-k% screen catches, the operative number
for using the surrogate as a pre-filter for exact Φ. Repeats with a size-robust feature subset
(ratios and flags only, no raw size-growing counts) to test whether extrapolation leans on n itself.

Writes results/extrapolate.json and results/extrapolate.png.
"""

import json
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, balanced_accuracy_score, recall_score

from .forms import FEATURE_KEYS, DYNAMICAL_KEYS

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
_DATASET = os.path.join(_RESULTS, "dataset.csv")
SEED = 0

# Size-robust subset: ratios and flags that do not grow mechanically with n, plus the dynamical
# block. Excludes n, n_edges, degrees, fan-in/out, longest_path (raw counts that scale with size).
ROBUST_KEYS = ["density", "frac_edges_through_hub", "is_strict_star", "n_reciprocal_nonhub",
               "hub_bias", "hub_all_required", "hub_or_like"] + DYNAMICAL_KEYS


def _rf():
    return RandomForestClassifier(n_estimators=400, min_samples_leaf=2,
                                  class_weight="balanced", random_state=SEED, n_jobs=-1)


def _screen_recall(y, proba, frac):
    """Fraction of true positives whose predicted probability is in the top `frac` of the batch."""
    if y.sum() == 0:
        return None
    k = max(1, int(np.ceil(frac * len(y))))
    top = set(np.argsort(-proba)[:k])
    caught = sum(1 for i in np.where(y == 1)[0] if i in top)
    return caught / int(y.sum())


def _evaluate(train, test, keys):
    rf = _rf().fit(train[keys].to_numpy(), train["triadic"].to_numpy())
    per_n = {}
    for n in sorted(test["n"].unique()):
        sub = test[test["n"] == n]
        y = sub["triadic"].to_numpy()
        proba = rf.predict_proba(sub[keys].to_numpy())[:, 1]
        pred = (proba > 0.5).astype(int)
        entry = {
            "n_forms": int(len(sub)),
            "n_triadic": int(y.sum()),
            "auc": round(float(roc_auc_score(y, proba)), 4) if len(set(y)) > 1 else None,
            "balanced_acc": round(float(balanced_accuracy_score(y, pred)), 4)
            if len(set(y)) > 1 else None,
            "triadic_recall": round(float(recall_score(y, pred, zero_division=0)), 4),
            "screen_recall_top10pct": _screen_recall(y, proba, 0.10),
            "screen_recall_top20pct": _screen_recall(y, proba, 0.20),
        }
        per_n[int(n)] = entry
    # pooled over all held-out sizes
    y = test["triadic"].to_numpy()
    proba = rf.predict_proba(test[keys].to_numpy())[:, 1]
    pooled = {
        "n_forms": int(len(test)),
        "n_triadic": int(y.sum()),
        "auc": round(float(roc_auc_score(y, proba)), 4) if len(set(y)) > 1 else None,
        "balanced_acc": round(float(balanced_accuracy_score(y, (proba > 0.5).astype(int))), 4)
        if len(set(y)) > 1 else None,
    }
    return per_n, pooled, rf, proba


def main():
    df = pd.read_csv(_DATASET)
    train = df[df["split"] == "train"].reset_index(drop=True)
    test = df[df["split"] == "test"].reset_index(drop=True)
    if len(test) == 0:
        print("No held-out (n>=6) forms in the dataset yet. Build with --max-n 8 first.")
        return

    per_n_full, pooled_full, rf_full, proba_full = _evaluate(train, test, FEATURE_KEYS)
    per_n_rob, pooled_rob, _, _ = _evaluate(train, test, ROBUST_KEYS)

    # attach per-form predictions for the boundary analysis
    test = test.copy()
    test["proba"] = proba_full
    test["pred"] = (proba_full > 0.5).astype(int)
    test["correct"] = (test["pred"] == test["triadic"]).astype(int)
    test.to_csv(os.path.join(_RESULTS, "test_predictions.csv"), index=False)

    results = {
        "n_train": int(len(train)), "n_test": int(len(test)),
        "full_features": {"per_n": per_n_full, "pooled": pooled_full},
        "size_robust_features": {"per_n": per_n_rob, "pooled": pooled_rob},
    }
    with open(os.path.join(_RESULTS, "extrapolate.json"), "w") as fh:
        json.dump(results, fh, indent=2)

    print("=" * 78)
    print("H2 -- EXTRAPOLATION (train n<=5, test held-out n)")
    print("=" * 78)
    print(f"{'n':>3} {'forms':>6} {'triadic':>8} {'AUC':>7} {'bal.acc':>8} "
          f"{'tri.recall':>11} {'top10%':>7} {'top20%':>7}")
    for n, e in per_n_full.items():
        auc = f"{e['auc']:.3f}" if e["auc"] is not None else "  -  "
        bacc = f"{e['balanced_acc']:.3f}" if e["balanced_acc"] is not None else "  -  "
        s10 = f"{e['screen_recall_top10pct']:.2f}" if e["screen_recall_top10pct"] is not None else " - "
        s20 = f"{e['screen_recall_top20pct']:.2f}" if e["screen_recall_top20pct"] is not None else " - "
        print(f"{n:>3} {e['n_forms']:>6} {e['n_triadic']:>8} {auc:>7} {bacc:>8} "
              f"{e['triadic_recall']:>11.3f} {s10:>7} {s20:>7}")
    pa = pooled_full["auc"]
    print(f"  pooled held-out AUC (full features)     = {pa if pa is not None else 'n/a'}")
    pr = pooled_rob["auc"]
    print(f"  pooled held-out AUC (size-robust subset)= {pr if pr is not None else 'n/a'}")
    print(f"  wrote {os.path.join(_RESULTS, 'extrapolate.json')}")

    _plot(per_n_full)


def _plot(per_n):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return
    ns = list(per_n.keys())
    aucs = [per_n[n]["auc"] for n in ns]
    recs = [per_n[n]["triadic_recall"] for n in ns]
    fig, ax = plt.subplots(figsize=(6.5, 4))
    xs = [n for n, a in zip(ns, aucs) if a is not None]
    ys = [a for a in aucs if a is not None]
    if xs:
        ax.plot(xs, ys, "o-", color="#2a6f97", label="held-out AUC")
    ax.plot(ns, recs, "s--", color="#e07a5f", label="triadic recall")
    ax.axhline(0.75, ls="--", c="#c1121f", lw=0.8, label="pre-registered n=6 line (0.75)")
    ax.axhline(0.5, ls=":", c="k", lw=0.8)
    ax.set_xlabel("party count n (held-out; trained only on n<=5)")
    ax.set_ylabel("score")
    ax.set_ylim(0, 1.05)
    ax.set_title("Does the verdict extrapolate past the exact-Φ ceiling?")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(_RESULTS, "extrapolate.png"), dpi=130)


if __name__ == "__main__":
    main()

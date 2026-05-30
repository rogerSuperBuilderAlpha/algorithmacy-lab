"""Analyze how micro EI and causal emergence relate to exact IIT-4.0 Φ.

Usage:
    python -m emergence_vs_phi.analyze
"""

import csv

import numpy as np

RESULTS_PATH = "emergence_vs_phi/results/emergence.csv"
SUMMARY_PATH = "emergence_vs_phi/results/summary.csv"
PLOT_PATH = "emergence_vs_phi/results/emergence_vs_phi.png"

MEASURES = ["ei_micro", "ei_macro_best", "causal_emergence"]
LABELS = {
    "ei_micro": "micro effective information",
    "ei_macro_best": "best macro EI",
    "causal_emergence": "causal emergence (macro − micro)",
}


def _rank(a):
    a = np.asarray(a, float)
    u, inv, c = np.unique(a, return_inverse=True, return_counts=True)
    avg, s = {}, 0
    for k, cc in enumerate(c):
        avg[k] = (2 * s + cc - 1) / 2.0
        s += cc
    return np.array([avg[i] for i in inv])


def _pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.std() < 1e-12 or y.std() < 1e-12:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def _spearman(x, y):
    return _pearson(_rank(x), _rank(y))


def _auc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, bool)
    npos, nneg = labels.sum(), (~labels).sum()
    if npos == 0 or nneg == 0:
        return float("nan")
    r = _rank(scores) + 1
    return float((r[labels].sum() - npos * (npos + 1) / 2) / (npos * nneg))


def load():
    with open(RESULTS_PATH) as f:
        rows = list(csv.DictReader(f))
    data = {k: np.array([float(r[k]) for r in rows])
            for k in MEASURES + ["phi_mean", "phi_max", "noise"]}
    return data, len(rows)


def main():
    data, n = load()
    phi = data["phi_mean"]
    pos = phi > 1e-6
    ce = data["causal_emergence"]
    emergent = ce > 1e-6
    print(f"\nEmergence vs Φ: {n} n=3 networks, {int(pos.sum())} with Φ>0, "
          f"{int(emergent.sum())} causally emergent (CE>0)\n")

    print(f"{'measure':<34}{'Spearman ρ(Φ)':>14}{'Pearson r':>12}{'AUC(Φ>0)':>12}")
    print("-" * 72)
    summary = []
    for k in MEASURES:
        rho, r, auc = _spearman(data[k], phi), _pearson(data[k], phi), _auc(data[k], pos)
        print(f"{LABELS[k]:<34}{rho:>14.3f}{r:>12.3f}{auc:>12.3f}")
        summary.append({"measure": k, "spearman_phi": rho, "pearson_phi": r, "auc_phi": auc})

    # Do emergence and integration co-occur, or trade off?
    print("\nCo-occurrence of causal emergence and integration:")
    print(f"  mean Φ  | emergent (CE>0): {phi[emergent].mean():.3f}   "
          f"| non-emergent: {phi[~emergent].mean():.3f}")
    print(f"  mean CE | integrated (Φ>0): {ce[pos].mean():.4f}  "
          f"| non-integrated: {ce[~pos].mean():.4f}")
    both = int((emergent & pos).sum())
    print(f"  both emergent AND integrated: {both} / {n}")
    print(f"  micro EI vs Φ: full ρ = {_spearman(data['ei_micro'], phi):+.3f}, "
          f"but among Φ>0 only ρ = {_spearman(data['ei_micro'][pos], phi[pos]):+.3f} "
          f"(EI tracks Φ once integrated — it is Φ's precursor — but does not "
          f"predict whether integration occurs)")
    print(f"  causal emergence among Φ>0 only: ρ = "
          f"{_spearman(ce[pos], phi[pos]):+.3f}; "
          f"top-Φ systems' mean CE = {ce[np.argsort(-phi)[:10]].mean():.4f} "
          f"(the most integrated systems show ~no emergence)")

    with open(SUMMARY_PATH, "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["measure", "spearman_phi", "pearson_phi", "auc_phi"])
        wr.writeheader(); wr.writerows(summary)
    print(f"\nWrote {SUMMARY_PATH}")
    _plot(data, phi)


def _plot(data, phi):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plot.")
        return
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))
    for ax, k in zip(axes, MEASURES):
        ax.scatter(data[k], phi, s=18, alpha=0.5, edgecolors="none")
        ax.set_xlabel(LABELS[k]); ax.set_ylabel("exact IIT-4.0 Φ (mean)")
        ax.set_title(f"ρ = {_spearman(data[k], phi):.2f}")
    fig.suptitle("Effective information / causal emergence vs exact IIT-4.0 Φ (n=3)", y=1.03)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=120, bbox_inches="tight")
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()

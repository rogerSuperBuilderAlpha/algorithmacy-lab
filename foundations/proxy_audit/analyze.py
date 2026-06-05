"""Analyze the proxy audit: how well does each proxy track exact IIT-4.0 Φ?

Produces:
- a printed table of rank (Spearman) and linear (Pearson) correlations of each
  proxy with exact Φ, plus each proxy's ability to detect Φ > 0 (AUC);
- a scatter-plot grid (each proxy vs Φ) saved to results/;
- a correlation summary saved to results/summary.csv.

Usage:
    python -m foundations.proxy_audit.analyze
"""

import csv

import numpy as np

RESULTS_PATH = "proxy_audit/results/audit.csv"
SUMMARY_PATH = "proxy_audit/results/summary.csv"
PLOT_PATH = "proxy_audit/results/proxy_vs_phi.png"

PROXY_KEYS = [
    "total_correlation",
    "stochastic_interaction",
    "lz_complexity",
    "mean_abs_corr",
    "n_edges",
]
PROXY_LABELS = {
    "total_correlation": "Total correlation",
    "stochastic_interaction": "Stochastic interaction",
    "lz_complexity": "LZ complexity",
    "mean_abs_corr": "Mean |pairwise corr|",
    "n_edges": "Number of edges",
}


def _spearman(x, y):
    """Spearman rank correlation (ties via average rank)."""
    def rank(a):
        order = np.argsort(a, kind="mergesort")
        ranks = np.empty(len(a), dtype=float)
        ranks[order] = np.arange(len(a))
        # average ties
        _, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
        cum = np.cumsum(counts)
        avg = {}
        start = 0
        for k, c in enumerate(counts):
            avg[k] = (start + start + c - 1) / 2.0
            start += c
        return np.array([avg[i] for i in inv])

    rx, ry = rank(np.asarray(x, float)), rank(np.asarray(y, float))
    return _pearson(rx, ry)


def _pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.std() < 1e-12 or y.std() < 1e-12:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def _auc(scores, labels):
    """AUC of ``scores`` ranking the binary ``labels`` (prob. a positive
    outranks a negative). Robust to ties via the rank-sum formula."""
    scores = np.asarray(scores, float)
    labels = np.asarray(labels, bool)
    n_pos, n_neg = labels.sum(), (~labels).sum()
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(len(scores), float)
    ranks[order] = np.arange(1, len(scores) + 1)
    # average ranks for ties
    uniq, inv = np.unique(scores, return_inverse=True)
    for u in range(len(uniq)):
        mask = inv == u
        ranks[mask] = ranks[mask].mean()
    return float((ranks[labels].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg))


def load():
    with open(RESULTS_PATH) as f:
        rows = list(csv.DictReader(f))
    data = {k: np.array([float(r[k]) for r in rows]) for k in
            ["phi_mean", "phi_max"] + PROXY_KEYS}
    return data, len(rows)


def main():
    data, n_rows = load()
    phi = data["phi_mean"]
    phi_positive = phi > 1e-6

    print(f"\nProxy audit: {n_rows} networks, "
          f"{int(phi_positive.sum())} with Φ>0 "
          f"(Φ range {phi.min():.3f}–{phi.max():.3f})\n")

    header = f"{'proxy':<24}{'Spearman ρ':>12}{'Pearson r':>12}{'AUC(Φ>0)':>12}"
    print(header)
    print("-" * len(header))
    summary = []
    for key in PROXY_KEYS:
        rho = _spearman(data[key], phi)
        r = _pearson(data[key], phi)
        auc = _auc(data[key], phi_positive)
        print(f"{PROXY_LABELS[key]:<24}{rho:>12.3f}{r:>12.3f}{auc:>12.3f}")
        summary.append({"proxy": key, "spearman": rho, "pearson": r, "auc_phi_positive": auc})

    with open(SUMMARY_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["proxy", "spearman", "pearson", "auc_phi_positive"])
        writer.writeheader()
        writer.writerows(summary)
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

    fig, axes = plt.subplots(1, len(PROXY_KEYS), figsize=(4 * len(PROXY_KEYS), 4))
    for ax, key in zip(axes, PROXY_KEYS):
        ax.scatter(data[key], phi, s=14, alpha=0.5, edgecolors="none")
        ax.set_xlabel(PROXY_LABELS[key])
        ax.set_ylabel("exact IIT-4.0 Φ (mean)")
        rho = _spearman(data[key], phi)
        ax.set_title(f"ρ = {rho:.2f}")
    fig.suptitle("Cheap proxies vs exact IIT-4.0 integrated information", y=1.02)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, bbox_inches="tight", dpi=120)
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()

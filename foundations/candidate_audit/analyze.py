"""Analyze the candidate-measure audit against exact IIT-4.0 Φ.

Usage:
    python -m foundations.candidate_audit.analyze
"""

import csv

import numpy as np

from .measures import MEASURE_KEYS

RESULTS_PATH = "candidate_audit/results/audit.csv"
SUMMARY_PATH = "candidate_audit/results/summary.csv"
PLOT_PATH = "candidate_audit/results/candidate_vs_phi.png"

LABELS = {
    "tdmi": "Time-delayed MI",
    "phi_wms": "Φ whole-minus-sum",
    "stochastic_interaction": "Stochastic interaction",
    "causal_density": "Causal density",
    "integrated_synergy": "Integrated synergy",
    "total_correlation": "Total correlation",
}


def _pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.std() < 1e-12 or y.std() < 1e-12:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def _rank(a):
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    r = np.empty(len(a), float)
    r[order] = np.arange(len(a))
    uniq, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
    avg, start = {}, 0
    for k, c in enumerate(counts):
        avg[k] = (2 * start + c - 1) / 2.0
        start += c
    return np.array([avg[i] for i in inv])


def _spearman(x, y):
    return _pearson(_rank(x), _rank(y))


def _auc(scores, labels):
    scores = np.asarray(scores, float)
    labels = np.asarray(labels, bool)
    n_pos, n_neg = labels.sum(), (~labels).sum()
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = _rank(scores) + 1
    return float((ranks[labels].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg))


def load():
    with open(RESULTS_PATH) as f:
        rows = list(csv.DictReader(f))
    data = {k: np.array([float(r[k]) for r in rows]) for k in ["phi_mean"] + MEASURE_KEYS}
    return data, len(rows)


def main():
    data, n_rows = load()
    phi = data["phi_mean"]
    pos = phi > 1e-6
    print(f"\nCandidate-measure audit: {n_rows} networks, {int(pos.sum())} with Φ>0 "
          f"(Φ range {phi.min():.3f}–{phi.max():.3f})\n")

    header = f"{'candidate measure':<26}{'Spearman ρ':>12}{'Pearson r':>12}{'AUC(Φ>0)':>12}"
    print(header)
    print("-" * len(header))
    summary = []
    # rank by |Spearman| descending for readability
    scored = [(k, _spearman(data[k], phi), _pearson(data[k], phi), _auc(data[k], pos))
              for k in MEASURE_KEYS]
    for k, rho, r, auc in sorted(scored, key=lambda t: -abs(t[1])):
        print(f"{LABELS[k]:<26}{rho:>12.3f}{r:>12.3f}{auc:>12.3f}")
        summary.append({"measure": k, "spearman": rho, "pearson": r, "auc_phi_positive": auc})

    with open(SUMMARY_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["measure", "spearman", "pearson", "auc_phi_positive"])
        w.writeheader()
        w.writerows(summary)
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
    keys = MEASURE_KEYS
    fig, axes = plt.subplots(1, len(keys), figsize=(3.6 * len(keys), 3.6))
    for ax, k in zip(axes, keys):
        ax.scatter(data[k], phi, s=12, alpha=0.5, edgecolors="none")
        ax.set_xlabel(LABELS[k])
        ax.set_ylabel("exact IIT-4.0 Φ (mean)")
        ax.set_title(f"ρ = {_spearman(data[k], phi):.2f}")
    fig.suptitle("Candidate integrated-information measures vs exact IIT-4.0 Φ", y=1.03)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, bbox_inches="tight", dpi=120)
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()

"""Analyze ΦID-based Φ_R (CCS, time-series-estimated) vs exact IIT-4.0 Φ.

Usage:
    python -m phiid_vs_phi.analyze
"""

import csv

import numpy as np

RESULTS_PATH = "phiid_vs_phi/results/phiid.csv"
SUMMARY_PATH = "phiid_vs_phi/results/summary.csv"
PLOT_PATH = "phiid_vs_phi/results/phiid_vs_phi.png"

MEASURES = {"phi_r_ccs": "Φ_R (ΦID, CCS)", "phi_wms_min": "Φ_WMS (uncorrected)"}


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


def main():
    with open(RESULTS_PATH) as f:
        rows = list(csv.DictReader(f))
    col = lambda k: np.array([float(r[k]) for r in rows])
    phi = col("phi_mean")
    pos = phi > 1e-6
    print(f"\nΦID Φ_R (CCS) vs exact Φ: {len(rows)} networks, {int(pos.sum())} with Φ>0\n")
    print(f"{'measure':<26}{'Spearman ρ(Φ)':>14}{'Pearson r':>12}{'AUC(Φ>0)':>12}")
    print("-" * 64)
    summary = []
    for k, label in MEASURES.items():
        x = col(k)
        rho, r, auc = _spearman(x, phi), _pearson(x, phi), _auc(x, pos)
        print(f"{label:<26}{rho:>14.3f}{r:>12.3f}{auc:>12.3f}")
        summary.append({"measure": k, "spearman": rho, "pearson": r, "auc": auc})
    # among Φ>0
    pr = col("phi_r_ccs")
    print(f"\namong Φ>0 only: Φ_R(CCS) vs Φ  ρ = {_spearman(pr[pos], phi[pos]):+.3f}")
    print("note: on these same networks the *exact* Φ_WMS tracks Φ at ρ≈0.28 "
          "(AUC≈0.67); the time-series estimate roughly halves that — see FINDINGS.")

    with open(SUMMARY_PATH, "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["measure", "spearman", "pearson", "auc"])
        wr.writeheader(); wr.writerows(summary)
    print(f"\nWrote {SUMMARY_PATH}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2))
        for ax, k in zip(axes, MEASURES):
            ax.scatter(col(k), phi, s=16, alpha=0.5, edgecolors="none")
            ax.set_xlabel(MEASURES[k]); ax.set_ylabel("exact IIT-4.0 Φ (mean)")
            ax.set_title(f"ρ = {_spearman(col(k), phi):.2f}")
        fig.suptitle("ΦID-based integrated information (time-series, CCS) vs exact Φ", y=1.02)
        fig.tight_layout(); fig.savefig(PLOT_PATH, dpi=120, bbox_inches="tight")
        print(f"Wrote {PLOT_PATH}")
    except ImportError:
        pass


if __name__ == "__main__":
    main()

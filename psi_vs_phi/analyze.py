"""Analyze ψ (and i) vs exact IIT-4.0 Φ, and rank ψ against the candidate measures.

Usage:
    python -m psi_vs_phi.analyze
"""

import csv

import numpy as np

RESULTS_PATH = "psi_vs_phi/results/psi_audit.csv"
SUMMARY_PATH = "psi_vs_phi/results/summary.csv"
PLOT_PATH = "psi_vs_phi/results/psi_vs_phi.png"

# measures to rank against Φ (ψ and i first, then the candidate-audit measures)
LEADERBOARD = {
    "psi": "ψ (MaxCal information)",
    "i": "i(π) = H − h",
    "phi_wms": "Φ whole-minus-sum",
    "integrated_synergy": "integrated synergy",
    "stochastic_interaction": "stochastic interaction",
    "total_correlation": "total correlation",
    "causal_density": "causal density",
    "tdmi": "time-delayed MI",
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


def _boot_ci(x, y, fn=_spearman, n=2000, seed=0):
    rng = np.random.default_rng(seed)
    x, y = np.asarray(x, float), np.asarray(y, float)
    vals = []
    idx = np.arange(len(x))
    for _ in range(n):
        b = rng.choice(idx, len(idx), replace=True)
        vals.append(fn(x[b], y[b]))
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def main():
    with open(RESULTS_PATH) as f:
        rows = list(csv.DictReader(f))
    col = lambda k, rs: np.array([float(r[k]) for r in rs])

    erg = [r for r in rows if int(r["ergodic"]) == 1]
    print(f"\nψ vs exact IIT-4.0 Φ: {len(rows)} networks total, "
          f"{len(erg)} ergodic (ψ well-defined) — primary analysis on the ergodic subset.\n")
    if len(erg) < 10:
        print("Too few ergodic networks; widen the ensemble."); return

    phi = col("phi_mean", erg)
    pos = phi > 1e-6
    print(f"  {int(pos.sum())}/{len(erg)} ergodic networks have Φ>0  (Φ range {phi.min():.3f}–{phi.max():.3f})\n")

    # Leaderboard: each measure vs Φ on the ergodic subset.
    header = f"{'measure':<26}{'Spearman ρ':>12}{'Pearson r':>12}{'AUC(Φ>0)':>12}"
    print(header); print("-" * len(header))
    summary, scored = [], []
    for k, label in LEADERBOARD.items():
        x = col(k, erg)
        rho, r, auc = _spearman(x, phi), _pearson(x, phi), _auc(x, pos)
        scored.append((label, rho, r, auc, k))
    for label, rho, r, auc, k in sorted(scored, key=lambda t: -abs(t[1])):
        star = "  ←ψ" if k == "psi" else ("  ←i" if k == "i" else "")
        print(f"{label:<26}{rho:>12.3f}{r:>12.3f}{auc:>12.3f}{star}")
        summary.append({"measure": k, "spearman": rho, "pearson": r, "auc_phi_positive": auc})

    # ψ focus: CI, Φ>0-conditional, ablation.
    psi_x = col("psi", erg)
    lo, hi = _boot_ci(psi_x, phi)
    print(f"\nψ vs Φ:  Spearman ρ = {_spearman(psi_x, phi):+.3f}  (95% CI [{lo:+.2f}, {hi:+.2f}])")
    print(f"  among Φ>0 only:  ρ = {_spearman(psi_x[pos], phi[pos]):+.3f}")
    print(f"  i(π) vs Φ:  ρ = {_spearman(col('i', erg), phi):+.3f}   "
          f"(ablation: is the signal in ψ or in i?)")
    # per-size
    for n in (3, 4):
        m = [r for r in erg if int(r["n"]) == n]
        if len(m) > 5:
            pm = col("phi_mean", m)
            print(f"  n={n} ({len(m)} nets): ψ ρ = {_spearman(col('psi', m), pm):+.3f}")

    with open(SUMMARY_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["measure", "spearman", "pearson", "auc_phi_positive"])
        w.writeheader(); w.writerows(summary)
    print(f"\nWrote {SUMMARY_PATH}")
    _plot(psi_x, col("i", erg), phi)


def _plot(psi_x, i_x, phi):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plot."); return
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax, x, lab in [(axes[0], psi_x, "ψ (MaxCal information)"),
                       (axes[1], i_x, "i(π) = H(π) − h(π)")]:
        ax.scatter(x, phi, s=18, alpha=0.5, edgecolors="none")
        ax.set_xlabel(lab); ax.set_ylabel("exact IIT-4.0 Φ (mean)")
        ax.set_title(f"ρ = {_spearman(x, phi):.2f}")
    fig.suptitle("Does maximum-caliber information track exact IIT-4.0 Φ? (ergodic networks)", y=1.02)
    fig.tight_layout(); fig.savefig(PLOT_PATH, dpi=120, bbox_inches="tight")
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()

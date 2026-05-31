"""Publication figures for the ψ-vs-Φ study.

Produces two figures in results/:
  psi_vs_phi.png        — main result: ψ-vs-Φ scatter, the Φ_WMS positive control,
                          the partitioned ϕ_ψ scatter, and the leaderboard.
  psi_vs_phi_supp.png   — distributions, the IIT-3.0 comparator, and the analytic
                          dissociation cases.

Usage:  python -m psi_vs_phi.figures
"""

import csv
import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from .analyze import _spearman, _load, _col, _load_phi3, LEADERBOARD

RESULTS = "psi_vs_phi/results/psi_audit.csv"
MAIN = "psi_vs_phi/results/psi_vs_phi.png"
SUPP = "psi_vs_phi/results/psi_vs_phi_supp.png"


def _mpl():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    return plt


def main():
    plt = _mpl()
    rows = _load(RESULTS)
    erg = [r for r in rows if int(r["ergodic"]) == 1]
    n_arr = _col("n", erg)
    phi = _col("phi_mean", erg)
    psi_x = _col("psi", erg)
    phipsi = _col("phi_psi", erg)
    wms = _col("phi_wms", erg)
    pos = phi > 1e-6

    # ---------------- Figure 1: main result ---------------- #
    fig, ax = plt.subplots(2, 2, figsize=(11, 9))

    def scatter(a, x, y, xlab, ylab, title):
        for nn, c, m in [(3, "#1f77b4", "o"), (4, "#d62728", "^")]:
            sel = n_arr == nn
            a.scatter(x[sel], y[sel], s=26, alpha=0.55, c=c, marker=m,
                      edgecolors="none", label=f"n={nn}")
        a.set_xlabel(xlab); a.set_ylabel(ylab); a.set_title(title)
        a.legend(frameon=False, fontsize=8, loc="best")

    scatter(ax[0, 0], psi_x, phi, "ψ  (maximum-caliber information)",
            "exact IIT-4.0 Φ (mean)",
            f"(a) ψ does not track Φ   ρ = {_spearman(psi_x, phi):+.2f}")
    scatter(ax[0, 1], wms, phi, "Φ whole-minus-sum (partition-based proxy)",
            "exact IIT-4.0 Φ (mean)",
            f"(b) positive control: a partition-based proxy DOES   ρ = {_spearman(wms, phi):+.2f}")
    scatter(ax[1, 0], phipsi, phi, "ϕ_ψ  (ψ + partition step)",
            "exact IIT-4.0 Φ (mean)",
            f"(c) adding a partition does not rescue ψ   ρ = {_spearman(phipsi, phi):+.2f}")

    # leaderboard bar
    a = ax[1, 1]
    scored = [(LEADERBOARD[k], _spearman(_col(k, erg), phi), k) for k in LEADERBOARD]
    scored.sort(key=lambda t: t[1])
    labels = [s[0] for s in scored]
    vals = [s[1] for s in scored]
    colors = ["#d62728" if s[2] in ("psi", "phi_psi", "i") else "#1f77b4" for s in scored]
    a.barh(range(len(vals)), vals, color=colors)
    a.set_yticks(range(len(vals))); a.set_yticklabels(labels, fontsize=8)
    a.axvline(0, color="k", lw=0.8)
    a.set_xlabel("Spearman ρ with exact Φ")
    a.set_title("(d) leaderboard (red = MaxCal / complexity)")

    fig.suptitle("Does maximum-caliber information ψ track exact IIT-4.0 Φ?  "
                 "(181 ergodic Boolean networks, seed 1)", y=1.0, fontsize=12)
    fig.tight_layout()
    fig.savefig(MAIN, dpi=130, bbox_inches="tight")
    print(f"Wrote {MAIN}")

    # ---------------- Figure 2: supplementary ---------------- #
    fig2, ax2 = plt.subplots(1, 3, figsize=(14, 4.4))

    # distributions
    a = ax2[0]
    a.hist(psi_x, bins=20, alpha=0.6, label="ψ", color="#d62728")
    a.hist(phi, bins=20, alpha=0.6, label="Φ (mean)", color="#1f77b4")
    a.set_xlabel("value (bits)"); a.set_ylabel("count")
    a.set_title("(a) distributions of ψ and Φ"); a.legend(frameon=False)

    # IIT 3.0 comparator
    phi3 = _load_phi3(1)
    a = ax2[1]
    if phi3:
        n3 = [r for r in erg if int(r["n"]) == 3 and int(r["idx"]) in phi3]
        p3 = np.array([phi3[int(r["idx"])] for r in n3])
        p4 = _col("phi_mean", n3)
        ps = _col("psi", n3)
        a.scatter(ps, p3, s=28, alpha=0.6, c="#2ca02c", marker="o", edgecolors="none",
                  label=f"ψ vs Φ₃  ρ={_spearman(ps, p3):+.2f}")
        a.set_xlabel("ψ"); a.set_ylabel("exact IIT-3.0 Φ (mean), n=3")
        a.set_title(f"(b) ψ misses 3.0 too\n(3.0 vs 4.0 agree: ρ={_spearman(p3, p4):+.2f})")
        a.legend(frameon=False, fontsize=8)

    # dissociation cases
    a = ax2[2]
    cases = ["(A) segregated\nbiased", "(B) parity\ncoupled"]
    psi_vals = [1.749, 0.428]
    phi_vals = [0.000, 0.689]
    xpos = np.arange(2)
    a.bar(xpos - 0.2, psi_vals, 0.4, label="ψ", color="#d62728")
    a.bar(xpos + 0.2, phi_vals, 0.4, label="Φ (mean)", color="#1f77b4")
    a.set_xticks(xpos); a.set_xticklabels(cases, fontsize=9)
    a.set_ylabel("bits")
    a.set_title("(c) analytic dissociation:\nψ ranks them backwards")
    a.legend(frameon=False)

    fig2.tight_layout()
    fig2.savefig(SUPP, dpi=130, bbox_inches="tight")
    print(f"Wrote {SUPP}")


if __name__ == "__main__":
    main()

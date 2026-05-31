"""Figures for the Complex Brain Hypothesis study. Usage: python -m cbh_complexity.figures"""

import csv
import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

RES = "cbh_complexity/results"


def _load(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def _col(rows, k):
    return np.array([float(r[k]) for r in rows])


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    A = _load(f"{RES}/ising_exact.csv")
    Cc = _load(f"{RES}/phi_noise.csv")
    B = _load(f"{RES}/ising_grain.csv")

    fig, ax = plt.subplots(2, 2, figsize=(11, 8.6))

    # (a) exact Ising: entropy monotone, complexity peaks at Tc and collapses
    T, H, Cn = _col(A, "T"), _col(A, "H"), _col(A, "Cn")
    a = ax[0, 0]
    a.plot(T, H / H.max(), "o-", color="#1f77b4", label="entropy H (norm.)")
    a.plot(T, Cn / Cn.max(), "s-", color="#d62728", label="TSE complexity Cₙ (norm.)")
    a.axvline(2.27, ls=":", color="gray", lw=1); a.text(2.3, 0.05, "Tc", color="gray")
    a.set_xlabel("temperature T"); a.set_ylabel("normalised value")
    a.set_title("(a) exact 4×4 Ising: H monotone, Cₙ peaks at Tc then collapses")
    a.legend(frameon=False, fontsize=9)

    # (b) parity ring: H, Cn, Phi vs noise
    noise = _col(Cc, "noise"); Hs = _col(Cc, "H_stationary")
    Cns = _col(Cc, "Cn_stationary"); phix = _col(Cc, "phi_max")
    a = ax[0, 1]
    a.plot(noise, Hs / Hs.max(), "o-", color="#1f77b4", label="entropy H (norm.)")
    a.plot(noise, Cns / Cns.max(), "s-", color="#d62728", label="TSE complexity Cₙ (norm.)")
    a.plot(noise, phix / phix.max(), "^-", color="#2ca02c", label="exact Φ_max (norm.)")
    a.set_xlabel("per-node noise (order → disorder)"); a.set_ylabel("normalised value")
    a.set_title("(b) parity ring, exact Φ: entropy↑, Cₙ peaks, Φ↓")
    a.legend(frameon=False, fontsize=9)

    # (c) grain sweep: apparent complexity vs grain at three temperatures
    a = ax[1, 0]
    grains = [1, 2, 4, 8]
    styles = {1.0: ("#2ca02c", "ordered T=1.0"), 2.27: ("#ff7f0e", "critical T=2.27"),
              6.0: ("#1f77b4", "disordered T=6.0")}
    for r in B:
        Tv = float(r["T"])
        c, lab = styles.get(round(Tv, 2), ("k", f"T={Tv}"))
        vals = [float(r[f"AC_grain{g}"]) for g in grains]
        a.plot(grains, vals, "o-", color=c, label=lab)
    a.set_xlabel("coarse-graining grain (block size)"); a.set_ylabel("apparent complexity (bits)")
    a.set_title("(c) grain-dependence: disordered state collapses when coarsened")
    a.set_xticks(grains); a.legend(frameon=False, fontsize=9)

    # (d) matched-entropy dissociation
    a = ax[1, 1]
    labels = ["contentless\n(independent)", "rich\n(parity ring)"]
    Hv = [3.169, 3.169]; Cnv = [0.0, 0.251]; Phiv = [0.0, 0.388]
    x = np.arange(2)
    a.bar(x - 0.25, Hv, 0.25, label="entropy H", color="#1f77b4")
    a.bar(x, Cnv, 0.25, label="TSE Cₙ", color="#d62728")
    a.bar(x + 0.25, Phiv, 0.25, label="exact Φ_max", color="#2ca02c")
    a.set_xticks(x); a.set_xticklabels(labels)
    a.set_ylabel("bits"); a.set_title("(d) matched entropy, dissociated complexity/Φ")
    a.legend(frameon=False, fontsize=9)

    fig.suptitle("Resolving the entropy–content conundrum on exactly-computable systems", y=1.0,
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(f"{RES}/cbh_complexity.png", dpi=130, bbox_inches="tight")
    print(f"Wrote {RES}/cbh_complexity.png")


if __name__ == "__main__":
    main()

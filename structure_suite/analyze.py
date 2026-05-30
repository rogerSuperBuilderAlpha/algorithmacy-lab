"""Analyze the Φ-structure suite: what does the suite capture beyond scalar Φ?

Usage:
    python -m structure_suite.analyze
"""

import csv

import numpy as np

from .suite import SUITE_KEYS

RESULTS_PATH = "structure_suite/results/suite.csv"
SUMMARY_PATH = "structure_suite/results/summary.csv"
HEATMAP_PATH = "structure_suite/results/suite_corr.png"
SCATTER_PATH = "structure_suite/results/phi_vs_structure.png"

LABELS = {
    "phi": "Φ",
    "n_distinctions": "# distinctions",
    "sum_phi_distinctions": "Σφ distinctions",
    "n_relations": "# relations",
    "sum_phi_relations": "Σφ relations",
    "mean_order": "mean order",
    "frac_higher_order": "frac order≥2",
    "max_order": "max order",
}


def _rank(a):
    a = np.asarray(a, float)
    uniq, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
    avg, start = {}, 0
    for k, c in enumerate(counts):
        avg[k] = (2 * start + c - 1) / 2.0
        start += c
    return np.array([avg[i] for i in inv])


def _pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.std() < 1e-12 or y.std() < 1e-12:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def _spearman(x, y):
    return _pearson(_rank(x), _rank(y))


def load():
    with open(RESULTS_PATH) as f:
        rows = list(csv.DictReader(f))
    data = {k: np.array([float(r[k]) for r in rows]) for k in SUITE_KEYS}
    return data, len(rows)


def main():
    data, n_rows = load()
    phi = data["phi"]
    pos = phi > 1e-6
    print(f"\nΦ-structure suite: {n_rows} (network,state) points, "
          f"{int(pos.sum())} with Φ>0\n")

    # 1) How redundant is each structural dimension with scalar Φ?
    print("Rank correlation of each structural dimension with scalar Φ:")
    struct_keys = [k for k in SUITE_KEYS if k != "phi"]
    summary = []
    for k in struct_keys:
        rho = _spearman(data[k], phi)
        print(f"  {LABELS[k]:<22} ρ(Φ) = {rho:+.3f}")
        summary.append({"dimension": k, "spearman_with_phi": rho})
    print("  -> dimensions with |ρ| well below 1 carry structure Φ alone misses.\n")

    # 2) Φ = 0 systems still have rich structure.
    z = ~pos
    if z.sum():
        print(f"Among the {int(z.sum())} Φ=0 (reducible) systems:")
        print(f"  # distinctions: mean {data['n_distinctions'][z].mean():.1f}, "
              f"max {int(data['n_distinctions'][z].max())}")
        print(f"  # relations:    mean {data['n_relations'][z].mean():.1f}, "
              f"max {int(data['n_relations'][z].max())}")
        frac_struct = np.mean(data["n_distinctions"][z] > 0)
        print(f"  fraction with >0 distinctions: {frac_struct:.2f}")
        print("  -> scalar Φ reports '0', yet the cause-effect structure is non-empty.\n")

    # 3) Structural spread at (nearly) fixed Φ.
    print("Structural spread within narrow Φ bands (same Φ, different structure):")
    bands = [(0.0, 1e-6), (1e-6, 0.2), (0.2, 0.5), (0.5, 10)]
    for lo, hi in bands:
        m = (phi >= lo) & (phi < hi)
        if m.sum() < 3:
            continue
        nd, nr = data["n_distinctions"][m], data["n_relations"][m]
        tag = "Φ=0" if hi <= 1e-6 else f"{lo:g}≤Φ<{hi:g}"
        print(f"  {tag:<10} (n={int(m.sum())}): "
              f"# distinctions {int(nd.min())}–{int(nd.max())}, "
              f"# relations {int(nr.min())}–{int(nr.max())}")
    print()

    with open(SUMMARY_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["dimension", "spearman_with_phi"])
        w.writeheader()
        w.writerows(summary)
    print(f"Wrote {SUMMARY_PATH}")
    _plots(data)


def _plots(data):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plots.")
        return

    keys = SUITE_KEYS
    # Correlation heatmap.
    M = np.array([[_spearman(data[a], data[b]) for b in keys] for a in keys])
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(M, vmin=-1, vmax=1, cmap="RdBu_r")
    ax.set_xticks(range(len(keys)))
    ax.set_yticks(range(len(keys)))
    ax.set_xticklabels([LABELS[k] for k in keys], rotation=45, ha="right")
    ax.set_yticklabels([LABELS[k] for k in keys])
    for i in range(len(keys)):
        for j in range(len(keys)):
            ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=7)
    fig.colorbar(im, label="Spearman ρ")
    ax.set_title("Φ-structure suite: rank-correlation among dimensions")
    fig.tight_layout()
    fig.savefig(HEATMAP_PATH, dpi=120, bbox_inches="tight")
    print(f"Wrote {HEATMAP_PATH}")

    # Φ vs structure scatters.
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, k in zip(axes, ["n_distinctions", "n_relations"]):
        ax.scatter(data["phi"], data[k], s=14, alpha=0.45, edgecolors="none")
        ax.set_xlabel("scalar Φ")
        ax.set_ylabel(LABELS[k])
        ax.set_title(f"Φ vs {LABELS[k]}  (ρ={_spearman(data['phi'], data[k]):.2f})")
    fig.suptitle("Same Φ, different structure: the vertical spread (esp. at Φ=0)", y=1.02)
    fig.tight_layout()
    fig.savefig(SCATTER_PATH, dpi=120, bbox_inches="tight")
    print(f"Wrote {SCATTER_PATH}")


if __name__ == "__main__":
    main()

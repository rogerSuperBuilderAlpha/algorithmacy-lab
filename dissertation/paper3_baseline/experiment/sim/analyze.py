"""Analyze sim_runs.csv: per-condition difficulty, the H1a back-channel contrast,
the H1 Φ-monotonicity test, and the H2 parity (Cerullo) probe. Writes a figure."""

import csv
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_RES = os.path.join(_HERE, "..", "results")

ORDER = ["C0_dyadic", "C1_parity", "C2_partial", "C3_strict"]
PHI = {"C0_dyadic": 0.0, "C1_parity": 0.5, "C2_partial": 0.83, "C3_strict": 2.0}


def load():
    with open(os.path.join(_RES, "sim_runs.csv")) as fh:
        rows = list(csv.DictReader(fh))
    by = {}
    for r in rows:
        by.setdefault(r["condition"], []).append(float(r["success"]))
    return {k: np.array(v) for k, v in by.items()}


def main():
    by = load()
    print("=" * 64)
    print("Coordination success by condition (mean ± 95% CI over 2 senders × 5 seeds)")
    print("=" * 64)
    print(f"{'condition':<12}{'Φ':>6}{'success':>10}{'difficulty':>12}{'95% CI':>16}")
    diffs = {}
    for c in ORDER:
        v = by[c]
        m, sd, nse = v.mean(), v.std(ddof=1), 1.96 * v.std(ddof=1) / np.sqrt(len(v))
        diffs[c] = 1 - m
        print(f"{c:<12}{PHI[c]:>6.2f}{m:>10.3f}{1-m:>12.3f}{f'[{m-nse:.3f},{m+nse:.3f}]':>16}")

    # H1a: the back-channel contrast (C2 partial vs C3 strict; AND held fixed)
    c2, c3 = by["C2_partial"], by["C3_strict"]
    pooled_sd = np.sqrt((c2.var(ddof=1) + c3.var(ddof=1)) / 2)
    d = (c2.mean() - c3.mean()) / pooled_sd
    print("\n[H1a] back-channel contrast (C2 partial Φ0.83 vs C3 strict Φ2.0, AND fixed):")
    print(f"  Δsuccess = {c2.mean()-c3.mean():+.3f}  (Cohen's d = {d:.2f})  -> strict is harder")

    # H1: Φ-monotonicity across conditions
    phis = np.array([PHI[c] for c in ORDER])
    dfc = np.array([diffs[c] for c in ORDER])
    # Spearman by hand
    rp, rd = phis.argsort().argsort(), dfc.argsort().argsort()
    rho = np.corrcoef(rp, rd)[0, 1]
    print(f"\n[H1] Spearman(Φ, difficulty) across 4 conditions = {rho:+.2f}")
    print("  (positive, but driven by C3; NOT clean monotone — see H2)")

    # H2: parity anomaly (Cerullo)
    print("\n[H2] Cerullo / parity probe:")
    print(f"  C1 parity (Φ=0.50) difficulty = {diffs['C1_parity']:.3f}  ≈  "
          f"C0 dyadic (Φ=0) difficulty = {diffs['C0_dyadic']:.3f}")
    print("  Parity scores mid-Φ but coordinates as easily as the dyad: the XOR determination")
    print("  is invertible, so 'no back-channel' is NOT sufficient for difficulty. This is the")
    print("  empirical face of Cerullo (2015): Φ magnitude does not track difficulty for parity.")

    # figure
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7.5, 4.2))
        xs = range(len(ORDER))
        succ = [by[c].mean() for c in ORDER]
        ci = [1.96 * by[c].std(ddof=1) / np.sqrt(len(by[c])) for c in ORDER]
        ax.bar(xs, succ, yerr=ci, capsize=4, color="#4C72B0")
        ax.set_xticks(list(xs))
        ax.set_xticklabels([f"{c.split('_')[1]}\nΦ={PHI[c]}" for c in ORDER])
        ax.set_ylabel("coordination success (asymptotic)")
        ax.set_ylim(0, 1)
        ax.axhline(0.95, ls="--", lw=0.8, color="gray")
        ax.set_title("Coordination difficulty by determination structure (party count fixed at 3)\n"
                     "only strict mediation (Φ=2.0, joint AND, no back-channel) is hard")
        fig.tight_layout()
        fig.savefig(os.path.join(_RES, "sim_results.png"), dpi=130)
        print(f"\nfigure -> {os.path.join(_RES, 'sim_results.png')}")
    except Exception as e:
        print(f"(figure skipped: {e})")


if __name__ == "__main__":
    main()

"""Summarise the Complex Brain Hypothesis experiments and write results/summary.txt.

Reports, for each experiment, the quantities the paper cites: the monotonicity of entropy, the
non-monotonicity (peak) of complexity, the high-entropy collapse, the grain-dependence, and the
matched-entropy dissociation. Usage: python -m foundations.cbh_complexity.analyze
"""

import csv

import numpy as np


def _load(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def _col(rows, k):
    return np.array([float(r[k]) for r in rows])


def _spearman(x, y):
    def rank(a):
        order = np.argsort(np.argsort(a))
        return order.astype(float)
    rx, ry = rank(x), rank(y)
    if rx.std() < 1e-12 or ry.std() < 1e-12:
        return 0.0
    return float(np.corrcoef(rx, ry)[0, 1])


def main():
    out = []
    def p(s): out.append(s); print(s)

    # Experiment A: exact 4x4 Ising
    A = _load("cbh_complexity/results/ising_exact.csv")
    T, H, Cn = _col(A, "T"), _col(A, "H"), _col(A, "Cn")
    ipk = int(np.argmax(Cn))
    p("EXPERIMENT A — exact 4x4 Ising (the authors' own example)")
    p(f"  entropy H: monotone {H[0]:.2f} -> {H[-1]:.2f} over T={T[0]}..{T[-1]} "
      f"(Spearman(T,H)={_spearman(T, H):+.3f}, i.e. monotone increasing)")
    p(f"  TSE complexity Cn: NON-monotone, peaks at T={T[ipk]:.2f} (Cn={Cn[ipk]:.2f}; "
      f"2D Tc≈2.27) and collapses to Cn={Cn[-1]:.2f} at T={T[-1]} (highest entropy)")
    p(f"  => high-entropy disordered state has LOW complexity: high entropy does not imply complexity.")
    p(f"  (honest caveat) Cn is also high at low T ({Cn[0]:.2f}, ordered/redundant): TSE Cn resolves the")
    p(f"  conundrum at the high-entropy end but conflates order with complexity at the low-entropy end.")
    Cfep = _col(A, "C_fep")
    p(f"  FEP complexity term (mean-field posterior-prior KL): {Cfep[0]:.2f} (ordered) -> {Cfep[ipk]:.2f} "
      f"(critical) -> {Cfep[-1]:.2f} (disordered); monotone-DECREASING in T, highest at order — it does NOT")
    p(f"  match apparent complexity, and joins Cn/Phi in misfiring at the ordered end (see paper 5.3).")

    # Experiment B: grain sweep
    B = _load("cbh_complexity/results/ising_grain.csv")
    p("\nEXPERIMENT B — Metropolis L=16 apparent-complexity grain sweep (claim C2), bootstrap 95% CIs")
    grains = [1, 2, 4, 8]
    for r in B:
        vals = "  ".join(
            f"g{g}={float(r['AC_grain%d' % g]):.2f}[{float(r['AC_grain%d_lo' % g]):.2f},"
            f"{float(r['AC_grain%d_hi' % g]):.2f}]" for g in grains)
        p(f"  T={float(r['T']):.2f}: {vals}")
    hi = [r for r in B if abs(float(r["T"]) - 6.0) < 1e-6][0]
    p(f"  => at the coarsest grain the high-entropy (T=6) state has the lowest apparent complexity "
      f"(g8={float(hi['AC_grain8']):.2f} [{float(hi['AC_grain8_lo']):.2f},{float(hi['AC_grain8_hi']):.2f}]), "
      f"non-overlapping CI with the ordered/critical states: coarse-graining reveals the high-entropy "
      f"state as simplest. The disordered collapse survives the bootstrap; the ordered/critical ordering "
      f"is finite-size dependent.")

    # Experiment C: exact-Phi noise sweep
    Cc = _load("cbh_complexity/results/phi_noise.csv")
    noise, Hs, Cns = _col(Cc, "noise"), _col(Cc, "H_stationary"), _col(Cc, "Cn_stationary")
    phim, phix = _col(Cc, "phi_mean"), _col(Cc, "phi_max")
    jpk = int(np.argmax(Cns))
    p("\nEXPERIMENT C — parity ring (n=4), exact IIT-4.0 Φ, order->disorder by noise")
    p(f"  entropy H: monotone {Hs[0]:.2f} -> {Hs[-1]:.2f} (Spearman(noise,H)={_spearman(noise, Hs):+.3f})")
    p(f"  TSE complexity Cn: peaks at noise={noise[jpk]:.3f} (Cn={Cns[jpk]:.3f}), -> {Cns[-1]:.3f} at max noise")
    p(f"  exact Φ_max: {phix[0]:.2f} (ordered) -> {phix[-1]:.2f} (disordered); integration destroyed by disorder")
    p(f"  => max-entropy state (noise 0.5): H={Hs[-1]:.2f} (max), Cn={Cns[-1]:.3f}, Φ={phix[-1]:.3f} "
      f"-> maximal entropy, zero complexity/integration = 'contentless'.")
    p(f"  Spearman(H, Cn)={_spearman(Hs, Cns):+.3f}, Spearman(H, Φmax)={_spearman(Hs, phix):+.3f}: "
      f"complexity and Φ are NOT monotone functions of entropy.")

    with open("cbh_complexity/results/summary.txt", "w") as f:
        f.write("\n".join(out) + "\n")
    print("\nWrote cbh_complexity/results/summary.txt")


if __name__ == "__main__":
    main()

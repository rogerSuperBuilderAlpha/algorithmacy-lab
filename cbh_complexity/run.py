"""Generate the Complex Brain Hypothesis datasets.

Three experiments, all written to results/:
  A. ising_exact.csv  -- exact 4x4 Ising temperature sweep: entropy H, apparent complexity at grains,
     and TSE neural complexity Cn. The authors' own example, made exact. (claim C1)
  B. ising_grain.csv  -- Metropolis L=16 grain sweep: apparent complexity vs grain at low/critical/high
     temperature. (claim C2: grain-dependence / the two high-entropy regimes)
  C. phi_noise.csv    -- a small structured dynamical system swept from order to disorder by noise, with
     exact IIT-4.0 Phi, TSE Cn and entropy of the stationary distribution. Connects CBH "complexity" to
     IIT integration on a system where Phi is exact.

Usage:  python -m cbh_complexity.run
"""

import csv
import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from . import ising
from . import complexity as C
from proxy_audit import networks, exact_phi
from candidate_audit import measures as candmeas

RES = "cbh_complexity/results"


def exp_A_ising_exact():
    rows = ising.sweep(L=4, grains=(1, 2), compute_tse=True)
    path = f"{RES}/ising_exact.csv"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["T", "H", "h_per_spin", "AC_grain1", "AC_grain2", "Cn"])
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {path} ({len(rows)} temperatures)")


def exp_B_ising_grain(seed=1):
    rng = np.random.default_rng(seed)
    rows = ising.grain_sweep(L=16, temps=(1.0, 2.27, 6.0), grains=(1, 2, 4, 8),
                             n_samples=400, rng=rng)
    path = f"{RES}/ising_grain.csv"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["T", "AC_grain1", "AC_grain2", "AC_grain4", "AC_grain8"])
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {path}")


def _structured_network(n=4, rng=None):
    """A structured, integrated network: a parity ring — each node is the PARITY (XOR) of its two
    ring-neighbours. Parity is maximally integrative (a node's next value depends irreducibly on its
    inputs jointly), so the deterministic system has positive exact Φ. Increasing the per-node noise
    carries it from order (noise 0) to disorder (noise 0.5, uniform), the order parameter analogous to
    Ising temperature."""
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        cm[(j - 1) % n, j] = 1
        cm[(j + 1) % n, j] = 1
    gate = [networks._gate_parity] * n
    return cm, gate


def exp_C_phi_noise(n=4, seed=1):
    rng = np.random.default_rng(seed)
    cm, gate = _structured_network(n)
    noises = np.round(np.linspace(0.0, 0.5, 21), 3)
    path = f"{RES}/phi_noise.csv"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["noise", "H_stationary", "Cn_stationary",
                                          "total_correlation", "phi_mean", "phi_max"])
        w.writeheader()
        for noise in noises:
            tpm = networks.network_from_assignment(n, cm, gate, float(noise), rng)
            pi = candmeas.stationary_distribution(tpm)
            H = C.entropy_bits(pi)
            Cn = C.tse_complexity(pi, n, max_subsets=64)
            tc = candmeas.total_correlation(tpm, n)
            phi_mean, phi_max, _, _ = exact_phi.network_phi_aggregations(tpm, cm, n, rng)
            w.writerow({"noise": float(noise), "H_stationary": H, "Cn_stationary": Cn,
                        "total_correlation": tc, "phi_mean": phi_mean, "phi_max": phi_max})
    print(f"Wrote {path}")


def main():
    os.makedirs(RES, exist_ok=True)
    print("Experiment A: exact 4x4 Ising sweep ...")
    exp_A_ising_exact()
    print("Experiment B: Metropolis L=16 grain sweep ...")
    exp_B_ising_grain()
    print("Experiment C: exact-Phi order->disorder sweep ...")
    exp_C_phi_noise()
    print("done.")


if __name__ == "__main__":
    main()

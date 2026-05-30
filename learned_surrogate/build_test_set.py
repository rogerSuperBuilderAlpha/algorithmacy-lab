"""Build an out-of-size test set (default n=5) for the extrapolation analysis.

Same columns as build_dataset.py, so a surrogate trained on the n∈{3,4} dataset
can be evaluated directly on larger systems it never saw. We cap states at 16
(as the training set does) so the exact-Φ target is estimated comparably.

Usage:
    python -m learned_surrogate.build_test_set [size] [n_networks] [seed]
"""

import csv
import sys
import time

import numpy as np

from proxy_audit import networks, exact_phi, proxies
from candidate_audit import measures
from .build_dataset import FEATURE_KEYS

DENSITIES = [0.3, 0.5, 0.8]
NOISES = [0.0, 0.05, 0.2]


def main(size=5, n_networks=300, seed=7):
    rng = np.random.default_rng(seed)
    path = f"learned_surrogate/results/test_n{size}.csv"
    print(f"Building n={size} test set: {n_networks} networks (seed={seed})...")
    fieldnames = ["idx", "gates", "phi_mean", "phi_max", "n_states_evaluated"] + FEATURE_KEYS
    start = time.time()
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for idx in range(n_networks):
            density = DENSITIES[idx % len(DENSITIES)]
            noise = NOISES[(idx // len(DENSITIES)) % len(NOISES)]
            tpm, cm, meta = networks.generate_network(size, density, noise, rng)
            traj = exact_phi.simulate_trajectory(tpm, size, 500, rng)
            phi_mean, phi_max, n_eval = exact_phi.network_phi(tpm, cm, size, rng)
            px = proxies.all_proxies(tpm, cm, size, traj)
            mv = measures.all_measures(tpm, size)
            writer.writerow({
                "idx": idx, "gates": "|".join(meta["gates"]),
                "phi_mean": phi_mean, "phi_max": phi_max, "n_states_evaluated": n_eval,
                "n": size, "density": density, "noise": noise, "n_edges": meta["n_edges"],
                "total_correlation": px["total_correlation"],
                "stochastic_interaction": px["stochastic_interaction"],
                "lz_complexity": px["lz_complexity"], "mean_abs_corr": px["mean_abs_corr"],
                "tdmi": mv["tdmi"], "phi_wms": mv["phi_wms"],
                "causal_density": mv["causal_density"],
                "integrated_synergy": mv["integrated_synergy"],
            })
            if (idx + 1) % 50 == 0 or idx + 1 == n_networks:
                print(f"  {idx + 1}/{n_networks}  ({time.time() - start:.0f}s)")
    print(f"Wrote {path}")


if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    n_networks = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    main(size, n_networks, seed)

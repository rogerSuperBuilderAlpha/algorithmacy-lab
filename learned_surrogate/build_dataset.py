"""Build the exact-IIT-4.0 feature dataset.

Each row is one network: its exact IIT-4.0 Φ (mean and max over reachable
states) plus every cheap feature from the proxy and candidate audits. This CSV
is both the training data for the surrogate and a reusable benchmark.

Usage:
    python -m learned_surrogate.build_dataset [per_cell] [seed]
"""

import csv
import sys
import time

import numpy as np

from proxy_audit import networks, exact_phi, proxies
from candidate_audit import measures

SIZES = [3, 4]
RESULTS_PATH = "learned_surrogate/results/dataset.csv"

# Union of features from both audits (de-duplicated). These are the predictors.
FEATURE_KEYS = [
    # structural / meta
    "n", "density", "noise", "n_edges",
    # proxy-audit features
    "total_correlation", "stochastic_interaction", "lz_complexity", "mean_abs_corr",
    # candidate-audit measures (excluding the two already listed above)
    "tdmi", "phi_wms", "causal_density", "integrated_synergy",
]


def main(per_cell=40, seed=2):
    rng = np.random.default_rng(seed)
    ensemble = list(networks.generate_ensemble(SIZES, per_cell, rng))
    total = len(ensemble)
    print(f"Building dataset on {total} networks (per_cell={per_cell}, seed={seed})...")

    fieldnames = ["idx", "gates", "phi_mean", "phi_max", "n_states_evaluated"] + FEATURE_KEYS
    start = time.time()
    with open(RESULTS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for idx, (tpm, cm, meta) in enumerate(ensemble):
            n = meta["n"]
            traj = exact_phi.simulate_trajectory(tpm, n, 500, rng)
            phi_mean, phi_max, n_eval = exact_phi.network_phi(tpm, cm, n, rng)
            px = proxies.all_proxies(tpm, cm, n, traj)
            mv = measures.all_measures(tpm, n)
            row = {
                "idx": idx, "gates": "|".join(meta["gates"]),
                "phi_mean": phi_mean, "phi_max": phi_max, "n_states_evaluated": n_eval,
                "n": n, "density": meta["density"], "noise": meta["noise"],
                "n_edges": meta["n_edges"],
                "total_correlation": px["total_correlation"],
                "stochastic_interaction": px["stochastic_interaction"],
                "lz_complexity": px["lz_complexity"],
                "mean_abs_corr": px["mean_abs_corr"],
                "tdmi": mv["tdmi"], "phi_wms": mv["phi_wms"],
                "causal_density": mv["causal_density"],
                "integrated_synergy": mv["integrated_synergy"],
            }
            writer.writerow(row)
            if (idx + 1) % 50 == 0 or idx + 1 == total:
                print(f"  {idx + 1}/{total}  ({time.time() - start:.0f}s)")
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    per_cell = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    main(per_cell, seed)

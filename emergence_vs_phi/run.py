"""Compute micro EI, causal emergence, and exact IIT-4.0 Φ for an ensemble.

Restricted to n=3 networks, where the causal-emergence search over all state
coarse-grainings (Bell(8) = 4140 partitions) is exact and tractable. We sweep
noise levels (including higher noise) because causal emergence requires
indeterminism to appear.

Usage:
    python -m emergence_vs_phi.run [per_cell] [seed]
"""

import csv
import sys
import time

import numpy as np
from pyphi import convert

from proxy_audit import networks, exact_phi
from . import emergence

RESULTS_PATH = "emergence_vs_phi/results/emergence.csv"
DENSITIES = [0.3, 0.5, 0.8]
NOISES = [0.0, 0.1, 0.2, 0.35]


def main(per_cell=10, seed=1):
    rng = np.random.default_rng(seed)
    jobs = []
    for density in DENSITIES:
        for noise in NOISES:
            for _ in range(per_cell):
                jobs.append(networks.generate_network(3, density, noise, rng))
    total = len(jobs)
    print(f"Emergence vs Φ on {total} n=3 networks (per_cell={per_cell}, seed={seed})...")

    fields = ["idx", "density", "noise", "n_edges", "gates",
              "ei_micro", "ei_macro_best", "causal_emergence", "macro_n_states",
              "phi_mean", "phi_max"]
    start = time.time()
    with open(RESULTS_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for idx, (tpm, cm, meta) in enumerate(jobs):
            P = convert.state_by_node2state_by_state(tpm)
            ce, ei_micro, ei_macro, best_part = emergence.causal_emergence(P)
            phi_mean, phi_max, _ = exact_phi.network_phi(tpm, cm, 3, rng)
            w.writerow({
                "idx": idx, "density": meta["density"], "noise": meta["noise"],
                "n_edges": meta["n_edges"], "gates": "|".join(meta["gates"]),
                "ei_micro": ei_micro, "ei_macro_best": ei_macro,
                "causal_emergence": ce, "macro_n_states": len(best_part),
                "phi_mean": phi_mean, "phi_max": phi_max,
            })
            if (idx + 1) % 20 == 0 or idx + 1 == total:
                print(f"  {idx + 1}/{total}  ({time.time() - start:.0f}s)")
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    per_cell = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    main(per_cell, seed)

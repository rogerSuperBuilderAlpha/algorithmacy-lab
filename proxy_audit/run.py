"""Run the proxy audit over an ensemble and write a results CSV.

Usage:
    python -m proxy_audit.run [per_cell] [seed]

For every network we record its exact IIT-4.0 Φ (mean and max over reachable
states) alongside every cheap proxy, plus metadata. The output CSV is the
substrate for ``analyze.py``.
"""

import csv
import sys
import time

import numpy as np

from . import networks, proxies, exact_phi

SIZES = [3, 4]
RESULTS_PATH = "proxy_audit/results/audit.csv"

PROXY_KEYS = [
    "total_correlation",
    "stochastic_interaction",
    "lz_complexity",
    "mean_abs_corr",
    "n_edges",
]


def main(per_cell=12, seed=0):
    rng = np.random.default_rng(seed)
    ensemble = list(networks.generate_ensemble(SIZES, per_cell, rng))
    total = len(ensemble)
    print(f"Running proxy audit on {total} networks (sizes={SIZES}, "
          f"per_cell={per_cell}, seed={seed})...")

    fieldnames = (
        ["idx", "n", "density", "noise", "n_edges", "gates",
         "phi_mean", "phi_max", "n_states_evaluated"]
        + PROXY_KEYS
    )
    start = time.time()
    with open(RESULTS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for idx, (tpm, cm, meta) in enumerate(ensemble):
            res = exact_phi.evaluate_network(tpm, cm, meta["n"], rng)
            px = proxies.all_proxies(tpm, cm, meta["n"], res["trajectory"])
            row = {
                "idx": idx,
                "n": meta["n"],
                "density": meta["density"],
                "noise": meta["noise"],
                "n_edges": meta["n_edges"],
                "gates": "|".join(meta["gates"]),
                "phi_mean": res["phi_mean"],
                "phi_max": res["phi_max"],
                "n_states_evaluated": res["n_states_evaluated"],
                **px,
            }
            writer.writerow(row)
            if (idx + 1) % 20 == 0 or idx + 1 == total:
                elapsed = time.time() - start
                print(f"  {idx + 1}/{total}  ({elapsed:.0f}s)")
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    per_cell = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    main(per_cell, seed)

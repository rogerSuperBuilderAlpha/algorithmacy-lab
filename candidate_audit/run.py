"""Run the candidate-measure audit and write a results CSV.

Reuses the verified exact-Φ oracle and network ensemble from the proxy_audit
package, so the ground truth is identical to that experiment.

Usage:
    python -m candidate_audit.run [per_cell] [seed]
"""

import csv
import sys
import time

import numpy as np

from proxy_audit import networks, exact_phi
from . import measures

SIZES = [3, 4]
RESULTS_PATH = "candidate_audit/results/audit.csv"


def main(per_cell=15, seed=1):
    rng = np.random.default_rng(seed)
    ensemble = list(networks.generate_ensemble(SIZES, per_cell, rng))
    total = len(ensemble)
    print(f"Running candidate-measure audit on {total} networks "
          f"(sizes={SIZES}, per_cell={per_cell}, seed={seed})...")

    fieldnames = (
        ["idx", "n", "density", "noise", "n_edges", "gates",
         "phi_mean", "phi_max", "n_states_evaluated"]
        + measures.MEASURE_KEYS
    )
    start = time.time()
    with open(RESULTS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for idx, (tpm, cm, meta) in enumerate(ensemble):
            n = meta["n"]
            phi_mean, phi_max, n_eval = exact_phi.network_phi(tpm, cm, n, rng)
            mvals = measures.all_measures(tpm, n)
            row = {
                "idx": idx, "n": n, "density": meta["density"],
                "noise": meta["noise"], "n_edges": meta["n_edges"],
                "gates": "|".join(meta["gates"]),
                "phi_mean": phi_mean, "phi_max": phi_max,
                "n_states_evaluated": n_eval,
                **mvals,
            }
            writer.writerow(row)
            if (idx + 1) % 20 == 0 or idx + 1 == total:
                print(f"  {idx + 1}/{total}  ({time.time() - start:.0f}s)")
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    per_cell = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    main(per_cell, seed)

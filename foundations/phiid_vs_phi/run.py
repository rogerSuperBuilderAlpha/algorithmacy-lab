"""Compute ΦID-based Φ_R (CCS, from time series) and exact Φ for an ensemble.

Usage:
    python -m foundations.phiid_vs_phi.run [per_cell] [seed]
"""

import csv
import sys
import time

import numpy as np

from foundations.proxy_audit import networks, exact_phi
from . import phiid_measure

SIZES = [3, 4]
RESULTS_PATH = "phiid_vs_phi/results/phiid.csv"


def main(per_cell=12, seed=3):
    rng = np.random.default_rng(seed)
    ensemble = list(networks.generate_ensemble(SIZES, per_cell, rng))
    total = len(ensemble)
    print(f"ΦID Φ_R (CCS) vs exact Φ on {total} networks (seed={seed})...")
    fields = ["idx", "n", "density", "noise", "phi_r_ccs", "phi_wms_min",
              "phi_mean", "phi_max"]
    start = time.time()
    with open(RESULTS_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for idx, (tpm, cm, meta) in enumerate(ensemble):
            n = meta["n"]
            phi_r, phi_wms = phiid_measure.phi_r_integration(tpm, n, rng)
            phi_mean, phi_max, _ = exact_phi.network_phi(tpm, cm, n, rng)
            w.writerow({"idx": idx, "n": n, "density": meta["density"],
                        "noise": meta["noise"], "phi_r_ccs": phi_r,
                        "phi_wms_min": phi_wms, "phi_mean": phi_mean,
                        "phi_max": phi_max})
            if (idx + 1) % 20 == 0 or idx + 1 == total:
                print(f"  {idx + 1}/{total}  ({time.time() - start:.0f}s)")
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    per_cell = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    main(per_cell, seed)

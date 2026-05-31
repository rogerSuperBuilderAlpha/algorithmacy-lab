"""Generate the ψ-vs-Φ dataset.

For each network in the ensemble, record the maximum-caliber information ψ and its companion
i(π), exact IIT-4.0 Φ (mean over reachable states), and — on the *same* networks — the
candidate-audit measures, so ψ can be ranked against them on identical systems.

Uses seed 1 by default (the ensemble candidate_audit used), so ψ slots directly into that
leaderboard.

Usage:
    python -m psi_vs_phi.run [per_cell] [seed]
"""

import csv
import sys
import time

import numpy as np

from proxy_audit import networks, exact_phi
from candidate_audit import measures as candmeas
from . import psi as psimod

SIZES = [3, 4]


def main(per_cell=15, seed=1):
    rng = np.random.default_rng(seed)
    ensemble = list(networks.generate_ensemble(SIZES, per_cell, rng))
    total = len(ensemble)
    # seed 1 is the canonical file (psi_audit.csv); all seeds also get a per-seed file.
    results_path = ("psi_vs_phi/results/psi_audit.csv" if seed == 1
                    else f"psi_vs_phi/results/psi_audit_seed{seed}.csv")
    global RESULTS_PATH
    RESULTS_PATH = results_path
    print(f"ψ vs exact IIT-4.0 Φ on {total} networks (seed={seed}) → {results_path}...")

    fields = ["idx", "n", "density", "noise", "ergodic",
              "psi", "i", "log2_kappa", "H_pi", "h_pi", "phi_psi",
              "phi_mean", "phi_max", "phi_piw", "gates",
              # candidate-audit measures on the same nets (for the leaderboard)
              "phi_wms", "stochastic_interaction", "total_correlation",
              "causal_density", "integrated_synergy", "tdmi"]
    start = time.time()
    with open(RESULTS_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for idx, (tpm, cm, meta) in enumerate(ensemble):
            n = meta["n"]
            p = psimod.psi(tpm)
            phi_psi = psimod.psi_partitioned(tpm, n)
            cand = candmeas.all_measures(tpm, n)
            phi_mean, phi_max, phi_piw, _ = exact_phi.network_phi_aggregations(tpm, cm, n, rng)
            w.writerow({
                "idx": idx, "n": n, "density": meta["density"], "noise": meta["noise"],
                "ergodic": int(p["ergodic"]),
                "psi": p["psi"], "i": p["i"], "log2_kappa": p["log2_kappa"],
                "H_pi": p["H_pi"], "h_pi": p["h_pi"], "phi_psi": phi_psi,
                "phi_mean": phi_mean, "phi_max": phi_max, "phi_piw": phi_piw,
                "gates": "|".join(meta["gates"]),
                "phi_wms": cand["phi_wms"], "stochastic_interaction": cand["stochastic_interaction"],
                "total_correlation": cand["total_correlation"], "causal_density": cand["causal_density"],
                "integrated_synergy": cand["integrated_synergy"], "tdmi": cand["tdmi"],
            })
            if (idx + 1) % 20 == 0 or idx + 1 == total:
                print(f"  {idx + 1}/{total}  ({time.time() - start:.0f}s)")
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    per_cell = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    main(per_cell, seed)

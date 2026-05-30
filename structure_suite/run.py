"""Collect the Φ-structure suite over many (network, state) pairs.

Unlike the proxy/candidate audits (which summarize each network by a single Φ),
this experiment is about *structural variation across states*, so each row is a
single (network, state). To keep relation computation tractable we cap the
number of states sampled per network.

Usage:
    python -m structure_suite.run [seed]
"""

import csv
import sys
import time

import numpy as np

from proxy_audit import networks, exact_phi
from . import suite

RESULTS_PATH = "structure_suite/results/suite.csv"

# Networks per (density, noise) cell, and states sampled per network.
SETTINGS = [
    # (n, per_cell, states_per_net)  -- n=4 relations are costly, so sample less.
    (3, 6, 6),
    (4, 3, 3),
]
DENSITIES = [0.3, 0.5, 0.8]
NOISES = [0.0, 0.05, 0.2]


def main(seed=1):
    rng = np.random.default_rng(seed)
    jobs = []
    for n, per_cell, n_states in SETTINGS:
        for density in DENSITIES:
            for noise in NOISES:
                for _ in range(per_cell):
                    tpm, cm, meta = networks.generate_network(n, density, noise, rng)
                    states = exact_phi.reachable_states(tpm, n)
                    if len(states) > n_states:
                        pick = rng.choice(len(states), size=n_states, replace=False)
                        states = [states[i] for i in pick]
                    jobs.append((tpm, cm, meta, states))

    fieldnames = ["net_idx", "n", "density", "noise", "n_edges", "state"] + suite.SUITE_KEYS
    start = time.time()
    n_rows = 0
    with open(RESULTS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for net_idx, (tpm, cm, meta, states) in enumerate(jobs):
            n = meta["n"]
            for s in states:
                state = tuple((s >> i) & 1 for i in range(n))
                row_suite = suite.extract_suite(tpm, cm, n, state)
                if row_suite is None:
                    continue
                writer.writerow({
                    "net_idx": net_idx, "n": n, "density": meta["density"],
                    "noise": meta["noise"], "n_edges": meta["n_edges"],
                    "state": "".join(map(str, state)),
                    **row_suite,
                })
                n_rows += 1
            if (net_idx + 1) % 20 == 0 or net_idx + 1 == len(jobs):
                print(f"  net {net_idx + 1}/{len(jobs)}, {n_rows} rows "
                      f"({time.time() - start:.0f}s)")
    print(f"Wrote {RESULTS_PATH} ({n_rows} rows)")


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    main(seed)

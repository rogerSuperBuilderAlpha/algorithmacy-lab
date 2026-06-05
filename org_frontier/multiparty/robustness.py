"""Reachability robustness: recompute the n=4 triadic rate with noise (full reachability).

Diagnostic from population_n4.csv: every deterministic strict-mediation n=4 form collapses to <=4
of 16 reachable states, so the deterministic triadic rate (2.3%) is measured in a degenerate
regime. This script adds output noise (independent per node, so it adds no coupling) to make all
states reachable, then recomputes exact IIT-4.0 max Φ over all states. Independent noise cannot
manufacture integration in a form that factors, so dyadic forms stay ~0 and only genuinely
irreducible forms score Φ > 0 — now without the attractor-collapse confound.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.robustness [n_sample] [noise] [seed]
"""

import csv
import os
import sys
import time

import numpy as np

from org_frontier.classifier.classifier import cm_from_rules, classify_rules
from org_frontier.proxy_bridge.bridge import add_noise
from org_frontier.multiparty.run import _rand_table, _fn, LABELS4
from foundations.proxy_audit import exact_phi

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
EPS = 1e-3


def main(n_sample=300, noise=0.1, seed=7):
    rng = np.random.default_rng(seed)
    sim_rng = np.random.default_rng(seed + 100)
    rows = []
    start = time.time()
    print(f"REACHABILITY ROBUSTNESS — noisy n=4 (n_sample={n_sample}, noise={noise}, seed={seed})")
    for k in range(n_sample):
        ts, tw, t1, t2 = (_rand_table(rng, 3), _rand_table(rng, 1),
                          _rand_table(rng, 1), _rand_table(rng, 1))
        rules = [_fn(tw, (1,)), _fn(ts, (0, 2, 3)), _fn(t1, (1,)), _fn(t2, (1,))]
        det = classify_rules(rules, labels=LABELS4)               # collapsed, deterministic
        from org_frontier.classifier.classifier import tpm_from_rules
        tpm = tpm_from_rules(rules)
        cm = cm_from_rules(rules)
        _, max_phi_noisy, _ = exact_phi.network_phi(add_noise(tpm, noise), cm, 4, sim_rng)
        rows.append({"idx": k, "det_structure": det.structure,
                     "det_states": det.n_states_evaluated,
                     "noisy_max_phi": f"{max_phi_noisy:.6f}",
                     "noisy_triadic": max_phi_noisy > EPS})
        if (k + 1) % 50 == 0:
            print(f"  {k+1}/{n_sample}  ({time.time()-start:.0f}s)")

    path = os.path.join(_RESULTS, "robustness_n4_noisy.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {path}")

    det_tri = sum(r["det_structure"] == "triadic" for r in rows)
    noisy_tri = sum(r["noisy_triadic"] for r in rows)
    print("=" * 78)
    print(f"  deterministic (collapsed) triadic rate : {det_tri}/{len(rows)} ({100*det_tri/len(rows):.1f}%)")
    print(f"  noisy (full reachability) triadic rate : {noisy_tri}/{len(rows)} ({100*noisy_tri/len(rows):.1f}%)")
    print(f"  (n=3 strict-mediation deterministic was 9.4%)")
    print("=" * 78)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    noise = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    main(n, noise, seed)

"""IIT-3.0 system Φ oracle (secondary comparator).

Kearney (2026) re-derives the *IIT 3.0* cause/effect repertoires (earth-mover's
distance), not the IIT 4.0 intrinsic-difference structure that our primary oracle
(`proxy_audit.exact_phi`) uses. A natural reviewer objection is therefore "maybe
ψ tracks 3.0 Φ even though it misses 4.0 Φ." This module computes whole-system
IIT-3.0 big-Φ on the *same* networks so we can rule that out.

Practical notes (this is run on a PyPhi checkout configured for 4.0):
- The 3.0 concept-evaluation path routes through PyPhi's parallel MapReduce, which
  requires the optional `pyphi[parallel]` (ray) dependency. We force sequential
  evaluation with a thin MapReduce monkeypatch (parallel=False) so no extra
  dependency is needed; results are identical, only slower.
- We set the 3.0 configuration explicitly: IIT_VERSION=3.0, DIRECTED_BI system
  partitions, EMD repertoire distance.
- The EMD code in this checkout raises a histogram-length error on some n=4
  repertoire shapes, so the 3.0 comparator is computed on the **n=3 subset only**
  (where every evaluation is stable). This limitation is reported, not hidden.

Whole-system Φ is mean-aggregated over reachable states exactly as the 4.0 oracle
aggregates, so the 3.0 and 4.0 network-level values are directly comparable.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import exceptions

import pyphi.parallel as _parallel

# Force sequential MapReduce so the 3.0 path needs no `ray`/`pyphi[parallel]`.
_orig_mapreduce_init = _parallel.MapReduce.__init__


def _sequential_init(self, *args, **kwargs):
    kwargs["parallel"] = False
    return _orig_mapreduce_init(self, *args, **kwargs)


_parallel.MapReduce.__init__ = _sequential_init

# IIT 3.0 configuration.
pyphi.config.PROGRESS_BARS = False
pyphi.config.IIT_VERSION = 3.0
pyphi.config.PARTITION_TYPE = "BI"
pyphi.config.SYSTEM_PARTITION_TYPE = "DIRECTED_BI"
pyphi.config.REPERTOIRE_DISTANCE = "EMD"

from proxy_audit.exact_phi import reachable_states  # noqa: E402


def network_phi3(tpm_sbn, cm, n, max_states=16):
    """Whole-system IIT-3.0 Φ, mean (and max) over reachable states.

    Returns (mean_phi3, max_phi3, n_evaluated, n_errors). Per-state EMD failures
    are caught and counted rather than aborting the network."""
    network = pyphi.Network(tpm_sbn, cm=cm)
    states = reachable_states(tpm_sbn, n)[:max_states]
    phis, errs = [], 0
    for s in states:
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            subsystem = pyphi.Subsystem(network, state)
            phi = float(pyphi.compute.phi(subsystem))
            phis.append(max(0.0, phi))
        except exceptions.StateUnreachableError:
            continue
        except Exception:
            errs += 1
    if not phis:
        return 0.0, 0.0, 0, errs
    return float(np.mean(phis)), float(np.max(phis)), len(phis), errs


def build(per_cell=15, seed=1):
    """Compute IIT-3.0 Φ on the n=3 subset of the seed ensemble and write
    results/phi3_n3_seed{seed}.csv keyed by the same network idx as run.py."""
    import csv
    import time
    from proxy_audit import networks

    rng = np.random.default_rng(seed)
    ensemble = list(networks.generate_ensemble([3, 4], per_cell, rng))
    out_path = f"psi_vs_phi/results/phi3_n3_seed{seed}.csv"
    start = time.time()
    total_err = 0
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["idx", "n", "phi3_mean", "phi3_max", "n_eval", "n_err"])
        w.writeheader()
        for idx, (tpm, cm, meta) in enumerate(ensemble):
            if meta["n"] != 3:
                continue  # n=4 EMD path is unstable in this checkout
            m, mx, ne, er = network_phi3(tpm, cm, 3)
            total_err += er
            w.writerow({"idx": idx, "n": 3, "phi3_mean": m, "phi3_max": mx,
                        "n_eval": ne, "n_err": er})
    print(f"Wrote {out_path}  ({time.time() - start:.0f}s, {total_err} per-state EMD errors)")


if __name__ == "__main__":
    import sys
    pc = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    sd = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    build(pc, sd)

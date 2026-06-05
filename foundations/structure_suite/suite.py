"""Extract the IIT-4.0 Φ-structure suite for a system in a state.

The suite is a multi-dimensional characterization of the cause-effect structure,
in the spirit of Barrett et al. (2026)'s proposal to replace scalar Φ:

- ``phi``                  -- system integrated information (the usual scalar).
- ``n_distinctions``       -- number of irreducible cause-effect distinctions.
- ``sum_phi_distinctions`` -- total small-φ of the distinctions.
- ``n_relations``          -- number of relations among distinctions.
- ``sum_phi_relations``    -- total φ of the relations.
- ``mean_order``           -- mean mechanism order (1 = single-unit, 2 = pair…);
  a measure of how higher-order the structure is.
- ``frac_higher_order``    -- fraction of distinctions with mechanism order ≥ 2.
- ``max_order``            -- largest mechanism order present.

All come from a single ``pyphi.new_big_phi.phi_structure`` call, so correctness
rests on PyPhi, not on us.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi
from pyphi import exceptions

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

SUITE_KEYS = [
    "phi",
    "n_distinctions",
    "sum_phi_distinctions",
    "n_relations",
    "sum_phi_relations",
    "mean_order",
    "frac_higher_order",
    "max_order",
]


def extract_suite(tpm_sbn, cm, n, state):
    """Return the Φ-structure suite dict for ``state``, or ``None`` if the state
    is unreachable."""
    network = pyphi.Network(tpm_sbn, cm=cm)
    try:
        subsystem = pyphi.Subsystem(network, tuple(state))
    except exceptions.StateUnreachableError:
        return None

    ps = new_big_phi.phi_structure(subsystem)
    orders = [len(d.mechanism) for d in ps.distinctions]
    return {
        "phi": max(0.0, float(ps.phi)),
        "n_distinctions": len(ps.distinctions),
        "sum_phi_distinctions": float(ps.sum_phi_distinctions),
        "n_relations": len(ps.relations),
        "sum_phi_relations": float(ps.sum_phi_relations),
        "mean_order": float(np.mean(orders)) if orders else 0.0,
        "frac_higher_order": float(np.mean([o >= 2 for o in orders])) if orders else 0.0,
        "max_order": max(orders) if orders else 0,
    }

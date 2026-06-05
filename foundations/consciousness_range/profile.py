"""Compute a full Φ-structure 'phenomenological profile' for a creature.

Under the IIT-is-true assumption, these quantities characterize *what it is like*
to be the system in its state:

- ``phi``                  -- integrated information ("level of consciousness").
- ``n_distinctions``       -- number of irreducible cause-effect distinctions
  (the "concepts" the experience is composed of).
- ``order_hist``           -- how many distinctions of each mechanism order
  (1 = single-unit, 2 = pair, …): the *composition* of the experience.
- ``sum_phi_distinctions`` -- total small-φ of the distinctions.
- ``n_relations``          -- number of relations binding the distinctions
  (the "richness"/integration of the structure).
- ``sum_phi_relations``    -- total φ of the relations.
- ``mean_order`` / ``max_order`` -- summary of compositional depth.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def profile(creature):
    """Return the Φ-structure profile dict for a bestiary creature."""
    network = pyphi.Network(creature["tpm"], cm=creature["cm"])
    try:
        subsystem = pyphi.Subsystem(network, creature["state"])
    except exceptions.StateUnreachableError:
        return None
    ps = new_big_phi.phi_structure(subsystem)
    orders = [len(d.mechanism) for d in ps.distinctions]
    hist = {o: int(np.sum(np.array(orders) == o)) for o in sorted(set(orders))} if orders else {}
    return {
        "name": creature["name"],
        "desc": creature["desc"],
        "n_nodes": creature["n"],
        "state": "".join(map(str, creature["state"])),
        "phi": max(0.0, float(ps.phi)),
        "n_distinctions": len(ps.distinctions),
        "order_hist": hist,
        "sum_phi_distinctions": float(ps.sum_phi_distinctions),
        "n_relations": len(ps.relations),
        "sum_phi_relations": float(ps.sum_phi_relations),
        "mean_order": float(np.mean(orders)) if orders else 0.0,
        "max_order": max(orders) if orders else 0,
    }

"""Random small-network generator for the proxy audit.

We need an ensemble of small discrete dynamical systems that span a wide range
of integrated information, so that any correlation between a cheap proxy and the
exact Φ is exercised across the whole range rather than a narrow band.

Each network is a set of ``n`` binary nodes. Every node updates as a (possibly
noisy) Boolean function of the nodes that connect to it. We return PyPhi's
state-by-node TPM together with the connectivity matrix.
"""

import numpy as np

# Boolean gate functions of a node's inputs (operate on the 1-D array of the
# input nodes' current states). Chosen to give a spread of dynamics from highly
# integrative (XOR/parity) to nearly independent (COPY/constant).
def _gate_or(inputs):
    return float(np.any(inputs))


def _gate_and(inputs):
    return float(np.all(inputs))


def _gate_parity(inputs):
    return float(np.sum(inputs) % 2)


def _gate_majority(inputs):
    if len(inputs) == 0:
        return 0.0
    return float(np.sum(inputs) > len(inputs) / 2)


def _gate_copy(inputs):
    # Copy the first input (or stay off if no inputs).
    return float(inputs[0]) if len(inputs) else 0.0


GATES = [_gate_or, _gate_and, _gate_parity, _gate_majority, _gate_copy]


def random_connectivity(n, density, rng):
    """Return an ``n x n`` connectivity matrix.

    ``cm[i, j] == 1`` means node ``i`` is an input to node ``j``. Self-loops are
    allowed. We guarantee every node has at least one input so the dynamics are
    well defined.
    """
    cm = (rng.random((n, n)) < density).astype(int)
    for j in range(n):
        if cm[:, j].sum() == 0:
            cm[rng.integers(n), j] = 1
    return cm


def network_from_assignment(n, cm, gate_choice, noise, rng):
    """Build a state-by-node TPM from a per-node gate assignment.

    Args:
        cm: connectivity matrix (inputs along axis 0).
        gate_choice: list of gate functions, one per node.
        noise: probability of flipping a node's deterministic output, applied
            independently per node. ``0`` gives a deterministic system.

    Returns:
        tpm: state-by-node TPM of shape ``(2**n, n)`` giving P(node on next).
    """
    n_states = 2 ** n
    tpm = np.zeros((n_states, n))
    for state_index in range(n_states):
        # PyPhi uses little-endian state indexing.
        state = np.array([(state_index >> i) & 1 for i in range(n)])
        for j in range(n):
            input_nodes = np.where(cm[:, j])[0]
            out = gate_choice[j](state[input_nodes])
            # Mix the deterministic output toward 0.5 by the noise level.
            tpm[state_index, j] = out * (1 - noise) + (1 - out) * noise
    return tpm


def generate_network(n, density, noise, rng):
    """Generate one random network: returns (tpm, cm, meta)."""
    cm = random_connectivity(n, density, rng)
    gate_choice = [GATES[rng.integers(len(GATES))] for _ in range(n)]
    tpm = network_from_assignment(n, cm, gate_choice, noise, rng)
    meta = {
        "n": n,
        "density": density,
        "noise": noise,
        "n_edges": int(cm.sum()),
        "gates": [g.__name__.replace("_gate_", "") for g in gate_choice],
    }
    return tpm, cm, meta


def generate_ensemble(sizes, per_cell, rng):
    """Yield a diverse ensemble of networks.

    For each network size we sweep a grid of connectivity densities and noise
    levels, generating ``per_cell`` random networks per (size, density, noise)
    cell. This deliberately spans sparse/dense and deterministic/noisy regimes
    to cover a broad range of Φ.
    """
    densities = [0.3, 0.5, 0.8]
    noises = [0.0, 0.05, 0.2]
    for n in sizes:
        for density in densities:
            for noise in noises:
                for _ in range(per_cell):
                    yield generate_network(n, density, noise, rng)

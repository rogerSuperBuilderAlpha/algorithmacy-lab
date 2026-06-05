"""Exact IIT-4.0 system integrated information -- the ground-truth oracle.

This is the only part of the pipeline that uses PyPhi's expensive machinery. We
compute big-Φ for the whole system in a reachable current state, using the
IIT-4.0 formalism (`pyphi.new_big_phi.sia`).
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import convert, new_big_phi, tpm as tpmmod
from pyphi import exceptions

# Quiet PyPhi: no progress bars, single-threaded (these are tiny systems).
pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def simulate_trajectory(tpm_sbn, n, timesteps, rng):
    """Simulate a binary trajectory of length ``timesteps`` from a random
    initial state. Returns a (timesteps, n) int array of node states.

    ``pyphi.tpm.simulate`` works on the state-by-state TPM and returns decimal
    state indices, which we expand back into per-node binary states (little
    endian, matching PyPhi's convention).
    """
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    initial = int(rng.integers(0, 2 ** n))
    path = tpmmod.simulate(sbs, initial, timesteps, rng)
    traj = np.array([[(idx >> i) & 1 for i in range(n)] for idx in path])
    return traj.astype(int)


def exact_big_phi(tpm_sbn, cm, state):
    """Exact IIT-4.0 big-Φ of the whole system in ``state``.

    Returns ``None`` if the state is unreachable under the network's dynamics
    (PyPhi refuses to analyze such states)."""
    network = pyphi.Network(tpm_sbn, cm=cm)
    try:
        subsystem = pyphi.Subsystem(network, tuple(state))
    except exceptions.StateUnreachableError:
        return None
    return float(new_big_phi.sia(subsystem).phi)


def reachable_states(tpm_sbn, n):
    """Return the decimal indices of states that have at least one predecessor
    under the dynamics (i.e. states PyPhi will agree to analyze)."""
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    # A state j is reachable if some state i transitions into it with prob > 0.
    incoming = sbs.sum(axis=0)
    return [j for j in range(2 ** n) if incoming[j] > 1e-12]


def network_phi(tpm_sbn, cm, n, rng, max_states=16):
    """Network-level exact IIT-4.0 Φ: the mean (and max) of big-Φ over the
    system's reachable states.

    Φ is state-dependent, but the proxies we audit are system-level properties
    of the dynamics. Averaging exact Φ over the reachable states gives a single
    system-level integration value to correlate against them, and avoids the
    bias of only ever scoring a low-Φ attractor.

    Returns (mean_phi, max_phi, n_evaluated).
    """
    network = pyphi.Network(tpm_sbn, cm=cm)
    states = reachable_states(tpm_sbn, n)
    if len(states) > max_states:
        idx = rng.choice(len(states), size=max_states, replace=False)
        states = [states[i] for i in idx]
    phis = []
    for s in states:
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            subsystem = pyphi.Subsystem(network, state)
        except exceptions.StateUnreachableError:
            continue
        phi = float(new_big_phi.sia(subsystem).phi)
        # A negative system Φ means the system in this state is *reducible*
        # (not an integrated complex), which carries zero integrated
        # information. Clamp to 0, matching IIT's treatment of complexes.
        phis.append(max(0.0, phi))
    if not phis:
        return 0.0, 0.0, 0
    return float(np.mean(phis)), float(np.max(phis)), len(phis)


def network_phi_aggregations(tpm_sbn, cm, n, rng, max_states=16):
    """Exact IIT-4.0 Φ aggregated over reachable states three ways: uniform mean,
    max, and stationary-π-weighted mean.

    The π-weighted aggregation is the most defensible comparator for a stationary
    quantity like ψ, since it weights each state by how often the system actually
    occupies it. For n ∈ {3,4} every reachable state is evaluated (≤16), so the
    three aggregations are computed on the same exact per-state Φ values.

    Returns (mean_phi, max_phi, piw_phi, n_evaluated)."""
    from foundations.candidate_audit.measures import stationary_distribution
    network = pyphi.Network(tpm_sbn, cm=cm)
    states = reachable_states(tpm_sbn, n)
    if len(states) > max_states:
        idx = rng.choice(len(states), size=max_states, replace=False)
        states = sorted(states[i] for i in idx)
    pi = stationary_distribution(tpm_sbn)
    phis, weights = [], []
    for s in states:
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            subsystem = pyphi.Subsystem(network, state)
        except exceptions.StateUnreachableError:
            continue
        phi = max(0.0, float(new_big_phi.sia(subsystem).phi))
        phis.append(phi)
        weights.append(pi[s])
    if not phis:
        return 0.0, 0.0, 0.0, 0
    phis = np.array(phis)
    w = np.array(weights)
    w = w / w.sum() if w.sum() > 1e-12 else np.full(len(phis), 1.0 / len(phis))
    return float(phis.mean()), float(phis.max()), float((w * phis).sum()), len(phis)


def evaluate_network(tpm_sbn, cm, n, rng, trajectory_len=500, max_states=16):
    """Full evaluation of one network.

    Returns a dict with network-level mean/max exact Φ and the simulated
    trajectory (used by the dynamical proxies).
    """
    trajectory = simulate_trajectory(tpm_sbn, n, trajectory_len, rng)
    mean_phi, max_phi, n_eval = network_phi(tpm_sbn, cm, n, rng, max_states)
    return {
        "phi_mean": mean_phi,
        "phi_max": max_phi,
        "n_states_evaluated": n_eval,
        "trajectory": trajectory,
    }

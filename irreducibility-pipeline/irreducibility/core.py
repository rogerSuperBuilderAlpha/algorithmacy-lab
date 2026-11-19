"""Exact irreducibility of a coordinative structure, computed with PyPhi (IIT 4.0).

A coordinative structure is modelled as a small deterministic Boolean network. Each node is a
party (a worker, a platform, a counterpart, an agent, a manager). Each party's next state is a
fixed Boolean function of the current states of the parties it reads.

From those rules this module builds the state-by-node transition probability matrix (TPM) and the
connectivity matrix, and asks PyPhi's IIT-4.0 implementation (``pyphi.new_big_phi``) two questions:

1. **Is the structure irreducible?** For every reachable state, ``new_big_phi.sia`` returns system
   integrated information Φ over the minimum-information partition (MIP), the directional cut that
   damages the cause-effect structure least. If Φ_MIP = 0 in every reachable state, some cut along
   party lines leaves the structure intact: it is **dyadic** (it factors). If Φ_MIP > 0 in at least
   one reachable state, no cut does: it is **triadic** (irreducible).
2. **Who is bound?** ``new_big_phi.maximal_complex`` returns the major complex, the subset of
   parties that forms the maximally irreducible core.

Only the binary verdict and the core membership are interpreted. Φ magnitude depends on the
encoding and is read as at most an ordinal hint.

Run the instrument controls before trusting any verdict:  ``python -m irreducibility.validate``

Provenance: consolidated from the lab's classifier (``classifier.py``), exact-Φ oracle
(``exact_phi.py``) and probe helpers (``lib.py``); behaviour unchanged.
"""

import os
from dataclasses import dataclass, field
from typing import Callable, Optional, Sequence

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import convert, exceptions, new_big_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

# Φ below this is treated as zero (floating-point and PyPhi numerical noise).
PHI_EPS = 1e-9

DEFAULT_LABELS = ("W", "S", "C")  # worker, system/mediator, counterpart


# ---------------------------------------------------------------------------------------------
# Rules -> transition matrix and connectivity matrix
# ---------------------------------------------------------------------------------------------

def tpm_from_rules(rules: Sequence[Callable], n: Optional[int] = None) -> np.ndarray:
    """Deterministic state-by-node TPM of shape (2^n, n) from per-node Boolean rules.

    ``rules[j]`` maps the current state tuple (little-endian: index 0 = first party) to node j's
    next value in {0, 1}. Little-endian indexing matches PyPhi.
    """
    n = len(rules) if n is None else n
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(rules[j](cur))
    return tpm


def cm_from_rules(rules: Sequence[Callable], n: Optional[int] = None) -> np.ndarray:
    """Connectivity matrix: cm[i, j] = 1 iff node j's rule depends on node i (flip test)."""
    n = len(rules) if n is None else n
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            for s in range(2 ** n):
                cur = list((s >> k) & 1 for k in range(n))
                flipped = cur.copy()
                flipped[i] ^= 1
                if rules[j](tuple(cur)) != rules[j](tuple(flipped)):
                    cm[i, j] = 1
                    break
    return cm


def reachable_states(tpm_sbn: np.ndarray, n: int):
    """Decimal indices of states with at least one predecessor (the states PyPhi will analyze)."""
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    incoming = sbs.sum(axis=0)
    return [j for j in range(2 ** n) if incoming[j] > 1e-12]


def simulate_trajectory(tpm_sbn, n, timesteps, rng):
    """Simulate a binary trajectory (timesteps x n) from a random initial state. Used by the proxy study."""
    from pyphi import tpm as tpmmod
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    initial = int(rng.integers(0, 2 ** n))
    path = tpmmod.simulate(sbs, initial, timesteps, rng)
    return np.array([[(idx >> i) & 1 for i in range(n)] for idx in path]).astype(int)


def exact_big_phi(tpm_sbn: np.ndarray, cm: np.ndarray, state) -> Optional[float]:
    """Exact IIT-4.0 system Φ over the MIP in ``state``; None if the state is unreachable."""
    network = pyphi.Network(tpm_sbn, cm=cm)
    try:
        subsystem = pyphi.Subsystem(network, tuple(state))
    except exceptions.StateUnreachableError:
        return None
    return float(new_big_phi.sia(subsystem).phi)


def network_phi(tpm_sbn, cm, n, rng, max_states=16):
    """Mean and max of exact Φ over reachable states (negative values clamped to 0).

    Returns (mean_phi, max_phi, n_evaluated). Used by the proxy study.
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
        phis.append(max(0.0, float(new_big_phi.sia(subsystem).phi)))
    if not phis:
        return 0.0, 0.0, 0
    return float(np.mean(phis)), float(np.max(phis)), len(phis)


# ---------------------------------------------------------------------------------------------
# The verdict
# ---------------------------------------------------------------------------------------------

@dataclass
class Verdict:
    """The verdict for one encoding of a coordinative structure."""
    structure: str                # "dyadic" or "triadic"
    max_phi: float                # max Φ_MIP over reachable states
    mip_state: Optional[tuple]    # the state achieving max_phi (triadic only)
    mip_partition: str            # the minimum-information partition at that state
    n_states_evaluated: int
    n_states_irreducible: int     # reachable states with Φ_MIP > PHI_EPS
    phi_profile: list = field(default_factory=list)  # [(state, phi), ...]
    labels: tuple = DEFAULT_LABELS

    @property
    def competence(self) -> str:
        """The competence the structure demands: literacy (dyadic) or algorithmacy (triadic)."""
        return "algorithmacy" if self.structure == "triadic" else "literacy"

    def __str__(self) -> str:
        head = (f"{self.structure.upper():>9}  (max Φ_MIP = {self.max_phi:.6f} over "
                f"{self.n_states_evaluated} reachable states; {self.n_states_irreducible} irreducible)")
        if self.mip_state is not None:
            head += f"\n           max-Φ state {self.mip_state}, MIP cut: {self.mip_partition}"
        return head


def phi_profile(tpm_sbn: np.ndarray, cm: np.ndarray, n: Optional[int] = None):
    """Exact IIT-4.0 Φ_MIP for each reachable state: [(state_tuple, phi), ...]."""
    n = cm.shape[0] if n is None else n
    out = []
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        phi = exact_big_phi(tpm_sbn, cm, state)
        if phi is not None:
            out.append((state, float(phi)))
    return out


def _mip_partition_repr(tpm_sbn, cm, state, labels) -> str:
    try:
        net = pyphi.Network(tpm_sbn, cm=cm, node_labels=labels[:cm.shape[0]])
        sub = pyphi.Subsystem(net, tuple(state))
        return str(new_big_phi.sia(sub).partition).splitlines()[0].strip()
    except Exception as e:  # informational only
        return f"(unavailable: {e})"


def classify(tpm_sbn: np.ndarray, cm: np.ndarray,
             labels: Sequence[str] = DEFAULT_LABELS, eps: float = PHI_EPS) -> Verdict:
    """Triadic iff Φ_MIP > eps in at least one reachable state; read at the most-integrated state."""
    n = cm.shape[0]
    profile = phi_profile(tpm_sbn, cm, n)
    if not profile:
        return Verdict("dyadic", 0.0, None, "(no reachable states)", 0, 0, [], tuple(labels[:n]))
    max_state, max_phi = max(profile, key=lambda r: r[1])
    n_irreducible = sum(1 for _, p in profile if p > eps)
    triadic = max_phi > eps
    mip = _mip_partition_repr(tpm_sbn, cm, max_state, tuple(labels)) if triadic else "(factors)"
    return Verdict(
        structure="triadic" if triadic else "dyadic",
        max_phi=max_phi,
        mip_state=max_state if triadic else None,
        mip_partition=mip,
        n_states_evaluated=len(profile),
        n_states_irreducible=n_irreducible,
        phi_profile=profile,
        labels=tuple(labels[:n]),
    )


def classify_rules(rules: Sequence[Callable], labels: Sequence[str] = DEFAULT_LABELS,
                   eps: float = PHI_EPS) -> Verdict:
    """Classify a structure given per-party Boolean rules."""
    return classify(tpm_from_rules(rules), cm_from_rules(rules), labels=labels, eps=eps)


def verdict(rules, labels):
    """Whole-system verdict (alias used throughout the studies)."""
    return classify_rules(rules, labels=labels)


def major_complex(rules, labels):
    """(core_label_tuple, phi) of the major complex, maximised over reachable states.

    Returns (None, -1.0) if no state has an irreducible complex.
    """
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=tuple(labels))
    best = (None, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in mc.node_indices), float(mc.phi))
    return best

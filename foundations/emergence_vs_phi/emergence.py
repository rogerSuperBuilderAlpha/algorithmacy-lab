"""Effective information and causal emergence (Hoel), computed exactly.

All quantities are derived from the state-by-state transition probability matrix
``P`` (rows = current micro state, columns = next micro state, rows sum to 1),
obtained from a PyPhi network's state-by-node TPM. Entropies are in bits.

- **Effective information** ``EI`` = the mutual information between a *uniform
  intervention* on the current state and the resulting next state:

      EI = H(E_bar) - (1/N) Σ_s H(P[s, :])

  where ``E_bar`` is the average ("effect") output distribution. EI is maximal
  (``log2 N`` bits) for a deterministic, non-degenerate system and 0 for a fully
  degenerate one.

- **Causal emergence** = ``max_φ EI_macro(φ) - EI_micro`` over coarse-grainings
  ``φ`` of the micro state space. The macro TPM for a state grouping assumes a
  uniform distribution over micro states within each macro state (Hoel 2013).
  Causal emergence is ≥ 0 (the micro grouping is always available) and > 0 when
  some coarse description has stronger effective information than the micro one.
"""

import numpy as np

_EPS = 1e-12


def _entropy(p):
    p = np.asarray(p, float)
    p = p[p > _EPS]
    return float(-(p * np.log2(p)).sum())


def effective_information(P):
    """EI (bits) of a state-by-state TPM under a uniform intervention."""
    P = np.asarray(P, float)
    N = P.shape[0]
    effect = P.mean(axis=0)                      # average output distribution
    cond_H = np.mean([_entropy(P[s]) for s in range(N)])
    return max(0.0, _entropy(effect) - cond_H)


def macro_tpm(P, groups):
    """Macro state-by-state TPM for a partition ``groups`` of micro states.

    Assumes a uniform distribution over the micro states within each macro
    state (Hoel 2013): for macro states I, J,

        P_macro[I, J] = (1/|I|) Σ_{s∈I} Σ_{s'∈J} P[s, s'].
    """
    P = np.asarray(P, float)
    m = len(groups)
    M = np.zeros((m, m))
    for i, gi in enumerate(groups):
        for j, gj in enumerate(groups):
            M[i, j] = P[np.ix_(gi, gj)].sum() / len(gi)
    return M


def _set_partitions(elements):
    """Yield all set partitions of a list (each partition = list of lists)."""
    elements = list(elements)
    if len(elements) == 0:
        yield []
        return
    first = elements[0]
    for rest in _set_partitions(elements[1:]):
        # insert `first` into each existing block...
        for i in range(len(rest)):
            yield rest[:i] + [[first] + rest[i]] + rest[i + 1:]
        # ...or as its own new block.
        yield [[first]] + rest


def causal_emergence(P, max_states_for_full_search=8):
    """Causal emergence of a state-by-state TPM.

    Searches coarse-grainings of the micro state space and returns
    ``(ce, ei_micro, ei_macro_best, best_partition)`` where
    ``ce = ei_macro_best - ei_micro``.

    For ``N <= max_states_for_full_search`` micro states this enumerates *all*
    set partitions (exact). Larger systems are not supported here (the number of
    partitions explodes); callers should restrict to small ``n``.
    """
    P = np.asarray(P, float)
    N = P.shape[0]
    ei_micro = effective_information(P)
    if N > max_states_for_full_search:
        raise ValueError(
            f"{N} micro states exceeds the exhaustive-search limit "
            f"({max_states_for_full_search}); restrict to smaller systems."
        )
    best_ei, best_part = ei_micro, [[s] for s in range(N)]
    for part in _set_partitions(range(N)):
        if len(part) == N or len(part) == 1:
            continue  # micro (== ei_micro) and the trivial 1-state macro (EI 0)
        groups = [np.array(b) for b in part]
        ei = effective_information(macro_tpm(P, groups))
        if ei > best_ei:
            best_ei, best_part = ei, part
    return best_ei - ei_micro, ei_micro, best_ei, best_part

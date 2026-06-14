"""Candidate measures of integrated information.

These are the practical, polynomial‑time measures from the
Barrett–Seth / Mediano–Rosas–Seth lineage that people compute on data. All are
defined here for a discrete, binary network whose dynamics are given by a
state‑by‑node TPM, and are evaluated exactly from the time‑lagged joint
distribution `J[s, s'] = π(s)·P(s'|s)` under the stationary distribution π.

Measures implemented (all in bits):

- ``tdmi``                 -- time‑delayed mutual information I(Xₜ₋₁; Xₜ); the
  whole‑system temporal integration, and an upper bound for the partition terms.
- ``phi_wms``              -- whole‑minus‑sum integrated information over the
  minimum information bipartition (Balduzzi & Tononi 2008; Barrett & Seth 2011).
- ``stochastic_interaction`` -- Ay (2001).
- ``causal_density``       -- mean pairwise transfer entropy (Seth 2008).
- ``integrated_synergy``   -- the synergy (about the system's own future) of the
  minimum information bipartition, via the MMI redundancy of the partial
  information decomposition (Williams & Beer 2010; Mediano et al. ΦID lineage).
- ``total_correlation``    -- instantaneous multi‑information (baseline).

Geometric Φ, Φ*, decoding‑Φ and the full ΦID / M‑information require numerical
optimisation or external packages and are deferred; see FINDINGS.md.
"""

import numpy as np
from pyphi import convert

_EPS = 1e-12


# --------------------------------------------------------------------------- #
# Distributions
# --------------------------------------------------------------------------- #

def stationary_distribution(tpm_sbn):
    """Stationary distribution over states (power iteration).

    Canonical state-by-node implementation; ``foundations.proxy_audit.proxies``
    re-exports this so every measure converges with the same parameters.
    """
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    n_states = sbs.shape[0]
    pi = np.full(n_states, 1.0 / n_states)
    for _ in range(5000):
        nxt = pi @ sbs
        if np.abs(nxt - pi).sum() < 1e-13:
            pi = nxt
            break
        pi = nxt
    return pi / pi.sum()


def lagged_joint(tpm_sbn):
    """Joint distribution J[s, s'] = π(s)·P(s'|s) over consecutive states."""
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    pi = stationary_distribution(tpm_sbn)
    return pi[:, None] * sbs


def _onehot(indices, n_cols):
    m = np.zeros((len(indices), n_cols))
    m[np.arange(len(indices)), indices] = 1.0
    return m


def _subset_indices(n, nodes):
    """For every full state s (0..2**n-1), the little‑endian index of its bits
    restricted to ``nodes``."""
    nodes = list(nodes)
    idx = np.zeros(2 ** n, dtype=int)
    for s in range(2 ** n):
        v = 0
        for bit, node in enumerate(nodes):
            v |= ((s >> node) & 1) << bit
        idx[s] = v
    return idx


def marginal_lagged(J, n, prev_nodes, next_nodes):
    """Marginal of the lagged joint onto (prev bits of ``prev_nodes``, next bits
    of ``next_nodes``). Returns an array of shape (2**|prev|, 2**|next|)."""
    p_idx = _subset_indices(n, prev_nodes)
    q_idx = _subset_indices(n, next_nodes)
    G_prev = _onehot(p_idx, 2 ** len(list(prev_nodes)))
    G_next = _onehot(q_idx, 2 ** len(list(next_nodes)))
    # out[p, q] = sum_{s,s'} [prev(s)=p] J[s,s'] [next(s')=q]
    return G_prev.T @ J @ G_next


# --------------------------------------------------------------------------- #
# Information-theoretic primitives (bits)
# --------------------------------------------------------------------------- #

def _entropy(p):
    p = np.asarray(p, float).ravel()
    p = p[p > _EPS]
    return float(-(p * np.log2(p)).sum())


def mutual_info(joint2d):
    """I(X;Y) from a 2‑D joint distribution."""
    p = np.asarray(joint2d, float)
    px = p.sum(1, keepdims=True)
    py = p.sum(0, keepdims=True)
    denom = px * py
    mask = p > _EPS
    return float((p[mask] * np.log2(p[mask] / denom[mask])).sum())


def cond_mutual_info(P):
    """I(A;C|B) from a 3‑D joint P[A, B, C]."""
    P = np.asarray(P, float)
    P_B = P.sum(axis=(0, 2))            # P(b)
    P_AB = P.sum(axis=2)                # P(a,b)
    P_BC = P.sum(axis=0)               # P(b,c)
    total = 0.0
    A, B, C = P.shape
    for a in range(A):
        for b in range(B):
            for c in range(C):
                pabc = P[a, b, c]
                if pabc <= _EPS:
                    continue
                num = pabc * P_B[b]
                den = P_AB[a, b] * P_BC[b, c]
                if den <= _EPS:
                    continue
                total += pabc * np.log2(num / den)
    return float(total)


# --------------------------------------------------------------------------- #
# Bipartitions
# --------------------------------------------------------------------------- #

def _bipartitions(n):
    for mask in range(1, 2 ** (n - 1)):
        a = tuple(i for i in range(n) if (mask >> i) & 1)
        b = tuple(i for i in range(n) if not ((mask >> i) & 1))
        if a and b:
            yield a, b


# --------------------------------------------------------------------------- #
# Candidate measures
# --------------------------------------------------------------------------- #

def tdmi(J, n):
    """Time‑delayed mutual information of the whole system, I(Xₜ₋₁; Xₜ)."""
    return mutual_info(J)


def phi_wms(J, n):
    """Whole‑minus‑sum integrated information over the minimum information
    bipartition.

        φ(partition) = I(Xₜ₋₁;Xₜ) − Σ_k I(M^k_{t-1}; M^k_t)

    minimised (normalised by the smaller part) over bipartitions. The reported
    value is the un‑normalised φ at that bipartition. May be negative — a known
    property of whole‑minus‑sum measures.
    """
    whole = mutual_info(J)
    best, best_norm = None, np.inf
    for a, b in _bipartitions(n):
        ia = mutual_info(marginal_lagged(J, n, a, a))
        ib = mutual_info(marginal_lagged(J, n, b, b))
        phi = whole - ia - ib
        norm = phi / min(len(a), len(b))
        if norm < best_norm:
            best_norm, best = norm, phi
    return best if best is not None else 0.0


def stochastic_interaction(tpm_sbn, n):
    """Ay (2001): Σ_i H(X^i_t | X^i_{t-1}) − H(Xₜ | Xₜ₋₁), under π."""
    pi = stationary_distribution(tpm_sbn)
    n_states = len(pi)
    states = np.array([[(s >> i) & 1 for i in range(n)] for s in range(n_states)])

    def _hb(p):
        p = np.clip(p, _EPS, 1 - _EPS)
        return float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))

    cond_h_whole = sum(
        pi[s] * sum(_hb(tpm_sbn[s, j]) for j in range(n)) for s in range(n_states)
    )
    sum_nodes = 0.0
    for i in range(n):
        prev = states[:, i]
        for a in (0, 1):
            mask = prev == a
            p_prev = pi[mask].sum()
            if p_prev < _EPS:
                continue
            p_next_on = (pi[mask] * tpm_sbn[mask, i]).sum() / p_prev
            sum_nodes += p_prev * _hb(p_next_on)
    return max(0.0, sum_nodes - cond_h_whole)


def causal_density(J, n):
    """Mean pairwise transfer entropy TE(i→j) = I(X^i_{t-1}; X^j_t | X^j_{t-1}),
    averaged over ordered pairs i≠j (Seth's causal density, discrete form)."""
    if n < 2:
        return 0.0
    vals = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # joint over ((i,j)_{t-1}, j_t): shape (4, 2). The prev index is
            # little-endian over (i, j), so reshape(2,2,2) yields axes
            # [j_prev, i_prev, j_next]; transpose to [i_prev, j_prev, j_next].
            m = marginal_lagged(J, n, (i, j), (j,))   # (4, 2)
            P = m.reshape(2, 2, 2).transpose(1, 0, 2)  # [i_prev, j_prev, j_next]
            vals.append(cond_mutual_info(P))           # I(i_prev; j_next | j_prev)
    return float(np.mean(vals))


def integrated_synergy(J, n):
    """Net synergy (negative interaction information / co‑information) about the
    system's own future, for the minimum information bipartition.

    For a bipartition (A, B), with the whole next state X_t as the shared target,
        S(A,B) = I(Xₜ₋₁; Xₜ) − I(A_{t-1}; Xₜ) − I(B_{t-1}; Xₜ)
    which is the co‑information of (A_{t-1}, B_{t-1}, X_t) up to sign: positive
    when the parts' pasts jointly carry information about the future that neither
    carries alone (synergy‑dominated), negative when their information is
    redundant. It is zero for independent parts, avoiding the spurious‑synergy
    pathology of MMI‑based decompositions. We report the minimum across
    bipartitions (the integrated synergy). May be negative.
    """
    whole = mutual_info(J)
    best = np.inf
    for a, b in _bipartitions(n):
        ia = mutual_info(marginal_lagged(J, n, a, range(n)))  # I(A_{t-1}; X_t)
        ib = mutual_info(marginal_lagged(J, n, b, range(n)))  # I(B_{t-1}; X_t)
        best = min(best, whole - ia - ib)
    return best if np.isfinite(best) else 0.0


def total_correlation(tpm_sbn, n):
    """Instantaneous multi‑information of the stationary distribution."""
    pi = stationary_distribution(tpm_sbn)
    n_states = len(pi)
    states = np.array([[(s >> i) & 1 for i in range(n)] for s in range(n_states)])
    marg_on = (states * pi[:, None]).sum(axis=0)

    def _hb(p):
        p = np.clip(p, _EPS, 1 - _EPS)
        return float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))

    return max(0.0, sum(_hb(p) for p in marg_on) - _entropy(pi))


MEASURE_KEYS = [
    "tdmi",
    "phi_wms",
    "stochastic_interaction",
    "causal_density",
    "integrated_synergy",
    "total_correlation",
]


def all_measures(tpm_sbn, n):
    """Compute every candidate measure for a network. Returns a dict."""
    J = lagged_joint(tpm_sbn)
    return {
        "tdmi": tdmi(J, n),
        "phi_wms": phi_wms(J, n),
        "stochastic_interaction": stochastic_interaction(tpm_sbn, n),
        "causal_density": causal_density(J, n),
        "integrated_synergy": integrated_synergy(J, n),
        "total_correlation": total_correlation(tpm_sbn, n),
    }

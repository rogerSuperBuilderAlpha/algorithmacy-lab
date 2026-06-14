"""Cheap, polynomial-time proxies for integrated information.

The point of the audit is to ask, empirically: how well do measures that people
*can* compute on real data track the exact Φ that IIT actually defines? We
implement a representative spread:

- ``total_correlation``      -- a static, distributional integration measure
  (multi-information of the stationary distribution).
- ``stochastic_interaction`` -- the dynamical integration of Ay (2001): how much
  better the whole system predicts its own future than its nodes predict their
  own futures in isolation. A well-defined, non-negative cheap surrogate for
  integrated information.
- ``lz_complexity``      -- normalized Lempel-Ziv (LZ76) complexity of a
  simulated binary trajectory: the empirical "neural complexity"/PCI-style
  proxy used in consciousness studies.
- ``mean_abs_corr``      -- mean absolute pairwise correlation of node activity
  in the trajectory: a trivial coupling baseline.
- ``n_edges``            -- number of connections: a purely structural baseline.

All proxies take the state-by-node TPM (and connectivity / state where needed)
and return a single float. They use only the network itself -- no call to
PyPhi's exact machinery -- so they are cheap by construction.

Entropies are in bits.
"""

import numpy as np

from foundations.candidate_audit.measures import stationary_distribution

_EPS = 1e-12


def _binary_entropy(p):
    """Entropy (bits) of a Bernoulli(p)."""
    p = np.clip(p, _EPS, 1 - _EPS)
    return float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))


def _entropy(dist):
    """Shannon entropy (bits) of a probability vector."""
    dist = np.asarray(dist, dtype=float)
    dist = dist[dist > _EPS]
    return float(-(dist * np.log2(dist)).sum())


def total_correlation(tpm_sbn, n):
    """Multi-information of the stationary distribution.

    TC = sum_i H(X_i) - H(X). Zero iff the nodes are statistically independent
    at stationarity; grows with statistical interdependence.
    """
    pi = stationary_distribution(tpm_sbn)
    n_states = len(pi)
    states = np.array([[(s >> i) & 1 for i in range(n)] for s in range(n_states)])
    # Marginal on-probability of each node under pi.
    marg_on = (states * pi[:, None]).sum(axis=0)
    sum_marginal_h = sum(_binary_entropy(p) for p in marg_on)
    joint_h = _entropy(pi)
    return max(0.0, sum_marginal_h - joint_h)


def stochastic_interaction(tpm_sbn, n):
    """Stochastic interaction (Ay 2001): a non-negative dynamical integration
    measure.

        Φ_SI = sum_i H(X_{i,t} | X_{i,t-1}) - H(X_t | X_{t-1})

    The whole system's one-step uncertainty is subtracted from the summed
    one-step uncertainty of its nodes taken in isolation. It is zero iff the
    nodes evolve independently and positive when the joint dynamics are more
    predictable than the marginal node dynamics, i.e. when the parts are
    dynamically coupled. All terms are evaluated under the stationary
    distribution.
    """
    pi = stationary_distribution(tpm_sbn)
    n_states = len(pi)
    states = np.array([[(s >> i) & 1 for i in range(n)] for s in range(n_states)])

    # H(X_t | X_{t-1}) under stationary inputs. Nodes are conditionally
    # independent given the previous state, so the per-state conditional entropy
    # is the sum of per-node binary entropies.
    cond_h_whole = 0.0
    for s in range(n_states):
        cond_h_whole += pi[s] * sum(_binary_entropy(tpm_sbn[s, j]) for j in range(n))

    # sum_i H(X_{i,t} | X_{i,t-1}).
    sum_cond_h_nodes = 0.0
    for i in range(n):
        prev_on = states[:, i]  # value of node i in each previous state
        for a in (0, 1):
            mask = prev_on == a
            p_prev = pi[mask].sum()
            if p_prev < _EPS:
                continue
            # P(next_i = 1 | prev_i = a), averaged over states with prev_i = a.
            p_next_on = (pi[mask] * tpm_sbn[mask, i]).sum() / p_prev
            sum_cond_h_nodes += p_prev * _binary_entropy(p_next_on)

    return max(0.0, sum_cond_h_nodes - cond_h_whole)


def _lz76(s):
    """Lempel-Ziv (1976) complexity: the number of distinct phrases in the
    left-to-right exhaustive-history parse (Kaspar & Schuster 1987 formulation).
    This is the standard LZc used in neural-complexity / PCI work."""
    n = len(s)
    if n == 0:
        return 0
    i, c, l = 0, 1, 1
    k, k_max = 1, 1
    while True:
        if s[i + k - 1] == s[l + k - 1]:
            k += 1
            if l + k > n:
                c += 1
                break
        else:
            if k > k_max:
                k_max = k
            i += 1
            if i == l:
                c += 1
                l += k_max
                if l + 1 > n:
                    break
                i = 0
                k = 1
                k_max = 1
            else:
                k = 1
    return c


def lz_complexity(trajectory):
    """Normalized LZ76 complexity of a binary trajectory.

    ``trajectory`` is a (timesteps, n) array of 0/1. We concatenate it in
    row-major (time-major) order into one bit string, as is standard for
    multichannel LZc, and normalize by the asymptotic random-sequence value
    ``L / log2(L)`` so values are comparable across lengths.
    """
    flat = np.asarray(trajectory).astype(int).flatten()
    bits = "".join(str(b) for b in flat)
    length = len(bits)
    if length < 2:
        return 0.0
    raw = _lz76(bits)
    norm = length / np.log2(length)
    return float(raw / norm)


def mean_abs_corr(trajectory):
    """Mean absolute pairwise Pearson correlation of node activity over time."""
    traj = np.asarray(trajectory, dtype=float)
    n = traj.shape[1]
    if n < 2:
        return 0.0
    vals = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = traj[:, i], traj[:, j]
            if a.std() < _EPS or b.std() < _EPS:
                vals.append(0.0)
            else:
                vals.append(abs(np.corrcoef(a, b)[0, 1]))
    return float(np.mean(vals)) if vals else 0.0


def all_proxies(tpm_sbn, cm, n, trajectory):
    """Compute every proxy and return a dict."""
    return {
        "total_correlation": total_correlation(tpm_sbn, n),
        "stochastic_interaction": stochastic_interaction(tpm_sbn, n),
        "lz_complexity": lz_complexity(trajectory),
        "mean_abs_corr": mean_abs_corr(trajectory),
        "n_edges": float(cm.sum()),
    }

"""q221 identifiability check: exact (enumerated, no sampling) pairwise categorical match profiles of
small Boolean forms in the q220 family, plus their exact IIT-4.0 bottleneck targets.

Family (q220 / q161 / crqa.trajectory): synchronous update, node j's next value = rule_j(state), then each
node is flipped independently with probability `flip` (q220 FLIP = 0.08). The exact-Φ target is computed
from the *deterministic* rules (tpm_from_rules ignores flip), exactly as q161/q220 do.

Everything here is exact linear algebra on the 2^n-state Markov chain; there is no randomness.
Imports from q161/q220/recurrence are read-only.
"""

import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

FLIP = 0.08
MAX_LAG = 20
WARMUP = 20


def bits(s, n):
    return tuple((s >> i) & 1 for i in range(n))  # little-endian, as tpm_from_rules / crqa


def noisy_sbs(rules, flip=FLIP):
    """State-by-state transition matrix of the q220 generator: deterministic rule then independent flips."""
    n = len(rules)
    N = 2 ** n
    P = np.zeros((N, N))
    for s in range(N):
        nxt = [int(r(bits(s, n))) for r in rules]
        for s2 in range(N):
            b = bits(s2, n)
            p = 1.0
            for j in range(n):
                p *= (1 - flip) if b[j] == nxt[j] else flip
            P[s, s2] = p
    return P


def stationary(P):
    w, v = np.linalg.eig(P.T)
    i = int(np.argmin(np.abs(w - 1)))
    pi = np.real(v[:, i])
    pi = pi / pi.sum()
    assert np.allclose(pi @ P, pi, atol=1e-12)
    return pi


def node_indicator(n, j):
    return np.array([bits(s, n)[j] for s in range(2 ** n)], dtype=float)


def match_profile(P, dist, i, j, max_lag=MAX_LAG):
    """P(x_i(t) == x_j(t+k)) for k = -max_lag..max_lag, with x(t) ~ dist (stationary if dist = pi).
    Negative k means x_j leads: P(x_i(t) == x_j(t+k)) = P(x_j(t') == x_i(t'+|k|)) under stationarity;
    for a non-stationary `dist` the negative lags are computed with the row at time t' = t."""
    n = int(round(np.log2(P.shape[0])))
    a, b = node_indicator(n, i), node_indicator(n, j)
    out = []
    Pk = {0: np.eye(P.shape[0])}
    for k in range(1, max_lag + 1):
        Pk[k] = Pk[k - 1] @ P
    for k in range(-max_lag, max_lag + 1):
        if k >= 0:
            J11 = dist @ (a[:, None] * Pk[k] * b[None, :]).sum(1)
            J00 = dist @ ((1 - a)[:, None] * Pk[k] * (1 - b)[None, :]).sum(1)
        else:
            m = -k
            J11 = dist @ (b[:, None] * Pk[m] * a[None, :]).sum(1)
            J00 = dist @ ((1 - b)[:, None] * Pk[m] * (1 - a)[None, :]).sum(1)
        out.append(J11 + J00)
    return np.array(out)


def all_profiles(rules, flip=FLIP, dist=None, max_lag=MAX_LAG):
    """dict (i, j) -> match profile over lags -max_lag..max_lag, for all ordered pairs incl. i == j (auto)."""
    P = noisy_sbs(rules, flip)
    pi = stationary(P) if dist is None else dist
    n = len(rules)
    return {(i, j): match_profile(P, pi, i, j, max_lag) for i in range(n) for j in range(n)}


def xor_triplet_prob(rules, flip=FLIP):
    """P(x_2(t+1) == x_0(t) XOR x_1(t)) under the stationary law."""
    P = noisy_sbs(rules, flip)
    pi = stationary(P)
    n = len(rules)
    tot = 0.0
    for s in range(2 ** n):
        b = bits(s, n)
        for s2 in range(2 ** n):
            if bits(s2, n)[2] == (b[0] ^ b[1]):
                tot += pi[s] * P[s, s2]
    return tot


def phi_targets(rules, labels):
    """(major-complex core indices, mc Φ, bottleneck set, leave-one-out drops) with the lab's own code."""
    from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
        core_indices, bottleneck_set)
    ci, phi = core_indices(rules, labels)
    bset, base, drops = bottleneck_set(rules, labels)
    return ci, phi, bset, base, drops


# ----------------------------------------------------------------------------- affine GF(2) rule space

def affine_rule(mask, c):
    """x -> c XOR (XOR of x[k] for k in mask) on 3 nodes."""
    return lambda x, m=mask, c=c: c ^ (sum(x[k] for k in range(3) if (m >> k) & 1) & 1)


def affine_systems():
    """All 16^3 = 4096 three-node systems whose rules are affine over GF(2): (mask, const) per node."""
    opts = [(m, c) for m in range(8) for c in (0, 1)]
    for combo in itertools.product(opts, repeat=3):
        yield combo, [affine_rule(m, c) for (m, c) in combo]

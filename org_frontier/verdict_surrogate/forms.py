"""Coordination-form generators and cheap features for the verdict surrogate.

Every generator returns ``(rules, meta)`` where ``rules`` is a list of per-party Boolean rules in
the classifier's convention (little-endian state tuple -> next bit) and ``meta`` records the
construction and whether a worker<->counterpart back-channel was added. Node 1 is the mediator S
in every construction; node 0 is the worker W; nodes 2.. are counterparts.

The features are the predictors the surrogate is allowed to use. None of them computes exact Φ:

* structural features come from the connectivity matrix (a flip-test, O(n * 2^n)) and from the
  mediator's truth table -- both cheap and available on a form far past the exact-Φ ceiling;
* dynamical features come from the repo's proxy and candidate audits, read off the TPM and a short
  simulated trajectory.
"""

import numpy as np

from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules
from org_frontier.multiparty.run import _rand_table, _fn
from foundations.proxy_audit.exact_phi import simulate_trajectory
from foundations.proxy_audit import proxies
from foundations.candidate_audit import measures


# --------------------------------------------------------------------------------------
# Generators.  n = number of parties; node 0 = W, node 1 = S (mediator), 2.. = counterparts.
# --------------------------------------------------------------------------------------

def _outer(n):
    """Indices of the non-mediator parties: worker (0) and counterparts (2..n-1)."""
    return [0] + list(range(2, n))


def random_strict_mediation(n, rng):
    """S reads all outer parties via a random function; each outer party reads S only."""
    outer = _outer(n)
    rules = [None] * n
    rules[1] = _fn(_rand_table(rng, len(outer)), tuple(outer))
    for i in outer:
        rules[i] = _fn(_rand_table(rng, 1), (1,))
    return rules, {"construction": "random_strict", "has_backchannel": False}


def random_with_backchannel(n, rng):
    """A random strict-mediation form plus one random direct edge between two outer parties.

    This is the adversarial family: a direct worker<->counterpart channel injects statistical
    dependence that a single dynamical proxy misreads as integration (the proxy_bridge failure).
    """
    rules, meta = random_strict_mediation(n, rng)
    outer = _outer(n)
    a, b = rng.choice(outer, size=2, replace=False)
    # b now also reads a directly, in addition to S.
    tb = _rand_table(rng, 2)
    rules[b] = _fn(tb, (1, int(a)))            # b' = f(S, a)
    meta = {"construction": "random_backchannel", "has_backchannel": True}
    return rules, meta


def chain(k):
    """Mediator chain W -> S1 -> ... -> Sk -> C.  n = k + 2.  Triadic (Φ = 2.0) at every depth."""
    rules = [lambda x: x[1]]
    for j in range(1, k + 1):
        lo, hi = j - 1, j + 1
        rules.append(lambda x, lo=lo, hi=hi: x[lo] & x[hi])
    rules.append(lambda x, k=k: x[k])
    return rules, {"construction": "chain", "has_backchannel": False}


def all_required(n):
    """S commits iff every outer party is present: S' = W AND C1 AND ... AND C_{n-2}.

    The canonical multi-party triad: no proper subset satisfies S, so no party-respecting cut
    factors the form."""
    outer = _outer(n)
    rules = [None] * n

    def s_rule(x, outer=tuple(outer)):
        v = 1
        for i in outer:
            v &= x[i]
        return v

    rules[1] = s_rule
    for i in outer:
        rules[i] = _fn((0, 1), (1,))          # outer' = S (identity read of the mediator)
    return rules, {"construction": "all_required", "has_backchannel": False}


def substitutable(n):
    """S commits if ANY outer party is present: S' = W OR C1 OR ...  Dyadic (substitutability
    collapses irreducibility -- the multiparty arm's finding)."""
    outer = _outer(n)
    rules = [None] * n

    def s_rule(x, outer=tuple(outer)):
        v = 0
        for i in outer:
            v |= x[i]
        return v

    rules[1] = s_rule
    for i in outer:
        rules[i] = _fn((0, 1), (1,))
    return rules, {"construction": "substitutable", "has_backchannel": False}


def add_backchannel(rules, n, rng):
    """Add a direct reciprocal edge between the worker and the last counterpart to a constructed
    form. On a triadic construction this should collapse the triad (the hierarchy_backchannel
    mechanism); the surrogate must learn to discount it from the structural feature alone."""
    rules = list(rules)
    a, b = 0, n - 1
    base_b = rules[b]
    rules[b] = lambda x, base_b=base_b, a=a: base_b(x) & x[a]   # b also reads the worker directly
    base_a = rules[a]
    rules[a] = lambda x, base_a=base_a, b=b: base_a(x) | x[b]   # worker also reads b directly
    return rules


# --------------------------------------------------------------------------------------
# Cheap features.  None of these computes exact Φ.
# --------------------------------------------------------------------------------------

def _longest_path(cm):
    """Longest simple directed path length (edges), ignoring self-loops. Cheap for small n."""
    n = cm.shape[0]
    adj = [[j for j in range(n) if i != j and cm[i, j]] for i in range(n)]
    best = 0

    def dfs(u, seen, length):
        nonlocal best
        best = max(best, length)
        for v in adj[u]:
            if v not in seen:
                dfs(v, seen | {v}, length + 1)

    for s in range(n):
        dfs(s, {s}, 0)
    return best


def structural_features(rules, n):
    """Features read from the connectivity matrix and the hub's truth table. No Φ."""
    cm = cm_from_rules(rules, n)
    off = cm.copy()
    np.fill_diagonal(off, 0)
    in_deg = off.sum(axis=0)          # in_deg[j] = how many parties j reads
    out_deg = off.sum(axis=1)         # out_deg[i] = how many parties read i
    hub = int(np.argmax(in_deg + out_deg))
    n_edges = int(off.sum())
    # reciprocal (mutual) edges
    recip = [(i, j) for i in range(n) for j in range(i + 1, n) if off[i, j] and off[j, i]]
    recip_nonhub = [(i, j) for (i, j) in recip if hub not in (i, j)]
    # edges not touching the hub -> candidate back-channels between outer parties
    nonhub_edges = int(sum(off[i, j] for i in range(n) for j in range(n)
                           if i != j and hub not in (i, j)))
    edges_through_hub = int(sum(off[i, j] for i in range(n) for j in range(n)
                                if i != j and hub in (i, j)))
    is_strict_star = int(nonhub_edges == 0 and n_edges > 0)

    # hub truth-table shape (cheap: enumerate the hub's own inputs only)
    hub_inputs = [i for i in range(n) if off[i, hub]]
    fanin = len(hub_inputs)
    all_required_hub = 0
    or_like_hub = 0
    bias = 0.0
    if fanin > 0:
        ones = 0
        all_ones_out = None
        any_zero_all_out_zero = True
        for m in range(2 ** fanin):
            state = [0] * n
            for b, i in enumerate(hub_inputs):
                state[i] = (m >> b) & 1
            out = int(rules[hub](tuple(state)))
            ones += out
            if m == (2 ** fanin - 1):
                all_ones_out = out
            if m != (2 ** fanin - 1) and out == 1:
                any_zero_all_out_zero = False   # fired without all inputs present
        bias = ones / (2 ** fanin)
        # all-required: fires only when every input is present
        all_required_hub = int(all_ones_out == 1 and any_zero_all_out_zero)
        # or-like / substitutable: fires whenever any input is present (bias high, fires at singletons)
        fires_at_singletons = 0
        for b in range(fanin):
            state = [0] * n
            state[hub_inputs[b]] = 1
            fires_at_singletons += int(rules[hub](tuple(state)) == 1)
        or_like_hub = int(fanin >= 2 and fires_at_singletons == fanin)

    return {
        "n": n,
        "n_edges": n_edges,
        "density": n_edges / (n * (n - 1)) if n > 1 else 0.0,
        "max_in_degree": int(in_deg.max()),
        "max_out_degree": int(out_deg.max()),
        "hub_fanin": int(in_deg[hub]),
        "hub_fanout": int(out_deg[hub]),
        "n_reciprocal": len(recip),
        "n_reciprocal_nonhub": len(recip_nonhub),   # the back-channel signal
        "n_nonhub_edges": nonhub_edges,
        "frac_edges_through_hub": edges_through_hub / n_edges if n_edges else 0.0,
        "is_strict_star": is_strict_star,
        "longest_path": _longest_path(cm),
        "hub_bias": bias,
        "hub_all_required": all_required_hub,
        "hub_or_like": or_like_hub,
    }


def dynamical_features(rules, n, rng, traj_len=500):
    """Features from the TPM and a short simulated trajectory (proxy + candidate audits)."""
    tpm = tpm_from_rules(rules, n)
    cm = cm_from_rules(rules, n)
    traj = simulate_trajectory(tpm, n, traj_len, rng)
    px = proxies.all_proxies(tpm, cm, n, traj)
    mv = measures.all_measures(tpm, n)
    return {
        "total_correlation": px["total_correlation"],
        "stochastic_interaction": px["stochastic_interaction"],
        "lz_complexity": px["lz_complexity"],
        "mean_abs_corr": px["mean_abs_corr"],
        "tdmi": mv["tdmi"],
        "phi_wms": mv["phi_wms"],
        "causal_density": mv["causal_density"],
        "integrated_synergy": mv["integrated_synergy"],
    }


STRUCTURAL_KEYS = [
    "n", "n_edges", "density", "max_in_degree", "max_out_degree", "hub_fanin", "hub_fanout",
    "n_reciprocal", "n_reciprocal_nonhub", "n_nonhub_edges", "frac_edges_through_hub",
    "is_strict_star", "longest_path", "hub_bias", "hub_all_required", "hub_or_like",
]
DYNAMICAL_KEYS = [
    "total_correlation", "stochastic_interaction", "lz_complexity", "mean_abs_corr",
    "tdmi", "phi_wms", "causal_density", "integrated_synergy",
]
FEATURE_KEYS = STRUCTURAL_KEYS + DYNAMICAL_KEYS


def cheap_features(rules, n, rng, traj_len=500):
    """All predictors for one form (structural + dynamical). No exact Φ."""
    f = structural_features(rules, n)
    f.update(dynamical_features(rules, n, rng, traj_len))
    return f

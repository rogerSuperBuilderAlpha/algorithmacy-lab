"""Information-theoretic measures for the Complex Brain Hypothesis test.

The Complex Brain Hypothesis (Mago et al. 2026) distinguishes the *entropy* of a system's states from
its *complexity*, and claims complexity (not entropy) indexes phenomenal richness. We make both
computable on small systems where they (and exact IIT-4.0 Φ) can be evaluated exactly.

Quantities (all in bits):

- ``entropy_bits``        -- Shannon entropy H of a distribution (the EBH "signal diversity" marker).
- ``integration``         -- total correlation I(X) = Σ_i H(x_i) − H(X) of a joint over n binary units.
- ``tse_complexity``      -- Tononi-Sporns-Edelman neural complexity (Tononi, Sporns & Edelman 1994;
  the construct the CBH cites as "neural complexity"): the integration-based complexity that is 0 for
  independent units and is meant to peak for systems that are both differentiated and integrated.
- ``apparent_complexity`` -- the Aaronson/Gell-Mann "apparent complexity": the structure of a
  *coarse-grained* representation, operationalised as the entropy of the distribution of coarse-grained
  block values. Low for uniform (ordered) and for washed-out (disordered) coarse representations, high
  for structured ones; grain-dependent. This is the measure the CBH's coffee/Ising picture is about.

Validate with ``python -m foundations.cbh_complexity.complexity`` before trusting any sweep.
"""

import numpy as np

_EPS = 1e-12


def entropy_bits(p):
    """Shannon entropy of a probability vector, in bits."""
    p = np.asarray(p, float).ravel()
    p = p[p > _EPS]
    return float(-(p * np.log2(p)).sum())


# --------------------------------------------------------------------------- #
# Joint-distribution measures over n binary units (distribution = length-2^n vector)
# --------------------------------------------------------------------------- #

def _as_tensor(dist, n):
    """Reshape a length-2^n probability vector into an n-dimensional (2,)*n tensor.
    Bit i is axis i (little-endian: state index s has bit i = (s>>i)&1)."""
    d = np.asarray(dist, float).reshape((2,) * n)
    return d


def _marginal_entropy(tensor, n, subset):
    """Entropy of the marginal distribution over the bits in ``subset``."""
    keep = tuple(subset)
    drop = tuple(i for i in range(n) if i not in keep)
    marg = tensor.sum(axis=drop) if drop else tensor
    return entropy_bits(marg)


def integration(dist, n):
    """Total correlation I(X) = Σ_i H(x_i) − H(X) over the joint distribution."""
    t = _as_tensor(dist, n)
    h_whole = entropy_bits(t)
    h_marg = sum(_marginal_entropy(t, n, (i,)) for i in range(n))
    return float(h_marg - h_whole)


def tse_complexity(dist, n, max_subsets=64, rng=None):
    """Tononi-Sporns-Edelman neural complexity (integration-based form):

        C(X) = Σ_{k=1}^{n} [ (k/n)·I(X) − ⟨I(X_k)⟩ ]

    where I is total correlation and ⟨I(X_k)⟩ is the average integration over subsets of size k. For
    subset sizes with more than ``max_subsets`` subsets, ⟨I(X_k)⟩ is estimated by random sampling.
    C(X) = 0 for independent units; it is meant to be larger for systems that are both differentiated
    and integrated. (We report its behaviour across regimes honestly, including the ordered/redundant
    end, rather than assuming it.)"""
    if rng is None:
        rng = np.random.default_rng(0)
    t = _as_tensor(dist, n)
    h_whole = entropy_bits(t)
    h_singles = [_marginal_entropy(t, n, (i,)) for i in range(n)]
    I_whole = sum(h_singles) - h_whole

    def avg_integration_size_k(k):
        if k == 1:
            return 0.0  # single-unit integration is 0 by definition
        if k == n:
            return I_whole
        from math import comb
        total = comb(n, k)
        if total <= max_subsets:
            from itertools import combinations
            subsets = list(combinations(range(n), k))
        else:
            subsets = set()
            while len(subsets) < max_subsets:
                subsets.add(tuple(sorted(rng.choice(n, size=k, replace=False))))
            subsets = list(subsets)
        vals = []
        for s in subsets:
            h_s = _marginal_entropy(t, n, s)
            vals.append(sum(h_singles[i] for i in s) - h_s)
        return float(np.mean(vals))

    C = 0.0
    for k in range(1, n + 1):
        C += (k / n) * I_whole - avg_integration_size_k(k)
    return float(C)


# --------------------------------------------------------------------------- #
# Apparent complexity under coarse-graining (Aaronson / Gell-Mann)
# --------------------------------------------------------------------------- #

def block_magnetizations(config, L, block):
    """Coarse-grain an L×L ±1 spin configuration into block-average magnetizations.
    Returns a flat array of block means in [-1, 1]."""
    g = config.reshape(L, L)
    nb = L // block
    out = np.empty((nb, nb))
    for bi in range(nb):
        for bj in range(nb):
            out[bi, bj] = g[bi * block:(bi + 1) * block, bj * block:(bj + 1) * block].mean()
    return out.ravel()


def apparent_complexity(configs, weights, L, block, n_bins=9):
    """Apparent complexity at a given grain: the Shannon entropy (bits) of the distribution of
    coarse-grained block-magnetization values, pooled over an ensemble of configurations.

    Operationalises the Aaronson (2014) "complexity of a coarse-grained representation": a uniform
    coarse field (ordered, all +1/−1; or disordered washed-out to ~0) needs few distinct values and
    scores low; a structured field spanning many block values scores high. ``configs`` is an array of
    ±1 configurations (rows), ``weights`` their probabilities (e.g. Boltzmann), summing to 1."""
    bins = np.linspace(-1.0, 1.0, n_bins + 1)
    hist = np.zeros(n_bins)
    for cfg, w in zip(configs, weights):
        bm = block_magnetizations(cfg, L, block)
        h, _ = np.histogram(bm, bins=bins)
        hist += w * h
    if hist.sum() <= _EPS:
        return 0.0
    return entropy_bits(hist / hist.sum())


# --------------------------------------------------------------------------- #
# Free-energy complexity term (posterior-prior KL) under a mean-field model
# --------------------------------------------------------------------------- #

def meanfield_kl_table(N, ngrid=400):
    """KL(posterior(m | k up-spins) || prior(m)) in bits, for each k in 0..N, under a mean-field
    generative model: given a global magnetization latent m, each of N spins is +1 with probability
    (1+m)/2 independently; prior p(m) uniform on a grid of ``ngrid`` points in (-1,1). The likelihood
    depends on the configuration only through k, so the posterior does too. With a uniform prior,
    KL = log2(ngrid) - H(posterior). This is the free-energy 'complexity' term (degrees of freedom the
    data forces into the latent) for the mean-field model."""
    mgrid = np.linspace(-0.999, 0.999, ngrid)
    out = np.empty(N + 1)
    for k in range(N + 1):
        ll = k * np.log((1 + mgrid) / 2) + (N - k) * np.log((1 - mgrid) / 2)
        ll -= ll.max()
        w = np.exp(ll)
        post = w / w.sum()
        out[k] = np.log2(ngrid) - entropy_bits(post)
    return out


def fep_complexity_meanfield(p_k, ngrid=400):
    """Free-energy complexity term averaged over a distribution p_k over the up-spin count k
    (length N+1): E_k[ KL(posterior(m|k) || prior(m)) ]. p_k is e.g. the Boltzmann distribution over k
    at a given temperature."""
    p_k = np.asarray(p_k, float)
    N = len(p_k) - 1
    return float((p_k * meanfield_kl_table(N, ngrid)).sum())


# --------------------------------------------------------------------------- #
# Validation controls
# --------------------------------------------------------------------------- #

def _independent_dist(n, p_on=0.5):
    """Joint of n independent bits each ON with prob p_on -> length-2^n vector."""
    d = np.ones(2 ** n)
    for s in range(2 ** n):
        for i in range(n):
            bit = (s >> i) & 1
            d[s] *= p_on if bit else (1 - p_on)
    return d / d.sum()


def _perfectly_correlated_dist(n):
    """All bits equal: mass split between all-0 and all-1."""
    d = np.zeros(2 ** n)
    d[0] = 0.5
    d[-1] = 0.5
    return d


def _controls():
    print("complexity.py validation controls\n" + "-" * 50)
    n = 6
    indep = _independent_dist(n, 0.5)
    corr = _perfectly_correlated_dist(n)

    print(f"independent {n} fair bits:  H={entropy_bits(indep):.3f} (expect {n})  "
          f"I={integration(indep, n):.4f} (expect 0)  Cn={tse_complexity(indep, n):.4f} (expect ~0)")
    print(f"perfectly correlated:       H={entropy_bits(corr):.3f} (expect 1)  "
          f"I={integration(corr, n):.4f} (expect {n-1})  Cn={tse_complexity(corr, n):.4f}")

    # A structured/intermediate system: pairs correlated, pairs independent of each other.
    # bits (0,1),(2,3),(4,5) each perfectly correlated internally, pairs independent.
    d = np.ones(2 ** n)
    for s in range(2 ** n):
        bits = [(s >> i) & 1 for i in range(n)]
        ok = (bits[0] == bits[1]) and (bits[2] == bits[3]) and (bits[4] == bits[5])
        d[s] = 1.0 if ok else 0.0
    d = d / d.sum()
    print(f"3 correlated pairs (mid):   H={entropy_bits(d):.3f}  I={integration(d, n):.4f}  "
          f"Cn={tse_complexity(d, n):.4f} (expect > independent and > 0)")

    # Apparent complexity controls on 4x4 fields.
    L = 4
    up = np.ones(L * L)                      # ordered: all +1
    rng = np.random.default_rng(0)
    structured = np.array([1 if (i // L) < L / 2 else -1 for i in range(L * L)], float)  # two domains
    ac_up = apparent_complexity([up], [1.0], L, 2)
    ac_struct = apparent_complexity([structured], [1.0], L, 2)
    print(f"apparent complexity (grain 2): ordered/uniform={ac_up:.3f} (expect ~0)  "
          f"two-domain={ac_struct:.3f} (expect > 0)")

    # FEP complexity term (mean-field): KL(k) U-shaped in k, symmetric, max at the extremes.
    kl = meanfield_kl_table(16)
    print(f"FEP complexity KL(k): k=0 {kl[0]:.3f}, k=8 {kl[8]:.3f}, k=16 {kl[16]:.3f} "
          f"(expect symmetric, extremes > middle, all >= 0)")

    ok = (abs(integration(indep, n)) < 1e-9 and abs(tse_complexity(indep, n)) < 1e-9
          and tse_complexity(d, n) > 0 and ac_up < 1e-9 and ac_struct > ac_up
          and abs(kl[0] - kl[16]) < 1e-9 and kl[0] > kl[8] and kl.min() > -1e-9)
    print("-" * 50)
    print("ALL CONTROLS PASSED ✓" if ok else "CONTROLS FAILED ✗")
    return ok


if __name__ == "__main__":
    _controls()

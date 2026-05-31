"""Exact 2D Ising model on a small periodic lattice — the Complex Brain Hypothesis's own example.

The CBH (Mago et al. 2026, citing Aaronson et al. 2014) illustrates the entropy–content conundrum with
the Ising model across temperature: ordered (low T → low entropy, low apparent complexity), critical
(intermediate entropy, maximal apparent complexity from cross-scale structure), and disordered (high T
→ high entropy, but a coarse-grained description washes out to homogeneity → low apparent complexity).

We make this exact. For an L×L lattice with periodic boundaries we enumerate all 2^(L²) configurations,
compute the Boltzmann distribution P(config) ∝ exp(−E/T) at each temperature, and from it the exact
Shannon entropy of the configuration distribution and the exact (Boltzmann-weighted) apparent
complexity at any grain. L = 4 (2^16 = 65536 configurations) is the default: small enough to enumerate
exactly, large enough to show the finite-size crossover near the 2D critical temperature T_c ≈ 2.27 J.
"""

import numpy as np

from .complexity import entropy_bits, apparent_complexity, tse_complexity, block_magnetizations


def _all_configs(L):
    """All 2^(L²) spin configurations as a (2^N, N) array of ±1, indexed so that state s has
    spin i = +1 iff bit i of s is set (little-endian) — matching the bit convention in complexity.py."""
    N = L * L
    idx = np.arange(2 ** N)
    bits = ((idx[:, None] >> np.arange(N)[None, :]) & 1).astype(np.int8)  # (2^N, N) in {0,1}
    return (2 * bits - 1).astype(np.int8), bits


def _energies(configs_pm, L):
    """Energy E = −Σ_{<ij>} s_i s_j over nearest-neighbour bonds with periodic boundaries (J=1)."""
    N = L * L
    g = configs_pm.reshape(-1, L, L)
    right = (g * np.roll(g, -1, axis=2)).sum(axis=(1, 2))
    down = (g * np.roll(g, -1, axis=1)).sum(axis=(1, 2))
    return -(right + down).astype(float)


def boltzmann_weights(energies, T):
    """Boltzmann distribution over configurations at temperature T (k_B = 1)."""
    e = energies - energies.min()
    w = np.exp(-e / T)
    return w / w.sum()


def sweep(L=4, temps=None, grains=(1, 2), compute_tse=True):
    """Exact temperature sweep. Returns a list of dicts with, per temperature:
    T, entropy H (bits) and per-spin entropy of the configuration distribution, apparent complexity at
    each grain, and (optionally) TSE neural complexity of the spin joint distribution."""
    if temps is None:
        temps = np.round(np.linspace(0.5, 6.0, 23), 3)
    N = L * L
    configs_pm, _ = _all_configs(L)
    energies = _energies(configs_pm, L)

    # Precompute block magnetizations per grain once (configs are fixed).
    from .complexity import block_magnetizations
    bm_cache = {b: np.array([block_magnetizations(c, L, b) for c in configs_pm]) for b in grains}
    bins = np.linspace(-1.0, 1.0, 10)

    rows = []
    for T in temps:
        w = boltzmann_weights(energies, T)
        H = entropy_bits(w)
        row = {"T": float(T), "H": H, "h_per_spin": H / N}
        for b in grains:
            # weighted histogram of block magnetizations across the ensemble
            hist = np.zeros(len(bins) - 1)
            bmv = bm_cache[b]
            digit = np.clip(np.digitize(bmv, bins) - 1, 0, len(bins) - 2)  # (2^N, nblocks)
            for col in range(bmv.shape[1]):
                np.add.at(hist, digit[:, col], w)
            hist = hist / hist.sum()
            row[f"AC_grain{b}"] = entropy_bits(hist)
        if compute_tse:
            row["Cn"] = tse_complexity(w, N, max_subsets=48)
        rows.append(row)
    return rows


def metropolis_samples(L, T, n_samples=400, burn=2000, thin=20, rng=None):
    """Metropolis-sampled equilibrium configurations for a larger lattice (where exact enumeration is
    infeasible), used only for the grain-dependence demonstration. Returns a (n_samples, L*L) ±1 array."""
    if rng is None:
        rng = np.random.default_rng(0)
    g = rng.choice([-1, 1], size=(L, L)).astype(np.int8)
    out = []
    steps = burn + n_samples * thin
    for step in range(steps):
        i, j = rng.integers(L), rng.integers(L)
        nb = g[(i + 1) % L, j] + g[(i - 1) % L, j] + g[i, (j + 1) % L] + g[i, (j - 1) % L]
        dE = 2 * g[i, j] * nb
        if dE <= 0 or rng.random() < np.exp(-dE / T):
            g[i, j] = -g[i, j]
        if step >= burn and (step - burn) % thin == 0:
            out.append(g.ravel().copy())
    return np.array(out, dtype=np.int8)


def grain_sweep(L=16, temps=(1.0, 2.27, 6.0), grains=(1, 2, 4, 8), n_samples=400,
                n_boot=400, rng=None):
    """Apparent complexity vs grain at several temperatures, on a sampled L×L lattice, with bootstrap
    95% CIs over the sampled configurations. Demonstrates the grain-dependence (CBH claim C2): a high-T
    disordered state's apparent complexity collapses under coarse-graining. CIs are reported because
    this is the one non-exact experiment; the ordered/critical ordering is not expected to survive
    them, while the disordered-state collapse should."""
    if rng is None:
        rng = np.random.default_rng(0)
    bins = np.linspace(-1.0, 1.0, 10)

    def ac_from_blockmags(bm_matrix, idx):
        # entropy of the pooled block-magnetization histogram over the configs in idx
        sub = bm_matrix[idx].ravel()
        hist, _ = np.histogram(sub, bins=bins)
        if hist.sum() == 0:
            return 0.0
        return entropy_bits(hist / hist.sum())

    rows = []
    for T in temps:
        configs = metropolis_samples(L, T, n_samples=n_samples, rng=rng)
        m = len(configs)
        row = {"T": float(T)}
        for b in grains:
            if b > L:
                continue
            # precompute block magnetizations once: (n_samples, n_blocks)
            bm = np.array([block_magnetizations(c, L, b) for c in configs])
            idx_all = np.arange(m)
            row[f"AC_grain{b}"] = ac_from_blockmags(bm, idx_all)
            boots = [ac_from_blockmags(bm, rng.choice(idx_all, m, replace=True))
                     for _ in range(n_boot)]
            row[f"AC_grain{b}_lo"] = float(np.percentile(boots, 2.5))
            row[f"AC_grain{b}_hi"] = float(np.percentile(boots, 97.5))
        rows.append(row)
    return rows


if __name__ == "__main__":
    import sys
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    for r in sweep(L=L):
        print(f"T={r['T']:.2f}  H={r['H']:.2f}  h/spin={r['h_per_spin']:.3f}  "
              f"AC(g1)={r.get('AC_grain1', 0):.3f}  AC(g2)={r.get('AC_grain2', 0):.3f}  "
              f"Cn={r.get('Cn', 0):.3f}")

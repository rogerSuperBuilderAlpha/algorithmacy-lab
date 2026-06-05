"""Analytic dissociation cases: tiny hand-built systems where ψ and Φ disagree.

The bulk result (ψ is uncorrelated with Φ across the ensemble) is a statistical
claim. These hand-crafted minimal systems make the *mechanism* concrete: they
exhibit, in two or three nodes, both directions of dissociation —

  (A) high ψ, zero Φ   — a segregated/biased system that deviates strongly from
      its MaxCal reference (so ψ is large) yet is reducible (Φ = 0);
  (B) low ψ, high Φ    — an integrated system (e.g. parity/XOR coupling) whose
      stationary occupancy is near the MaxCal reference (so ψ is small) yet whose
      cause–effect structure is irreducible (Φ > 0).

Each case prints ψ, the companion mutual information i(π), the partitioned
ϕ_ψ, and exact IIT-4.0 Φ, so the structural mismatch is visible analytically
rather than only in aggregate statistics.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from psi_vs_phi import psi as M
from foundations.proxy_audit import exact_phi
from foundations.proxy_audit import networks


def _phi(tpm, cm, n):
    rng = np.random.default_rng(0)
    mean, mx, piw, ne = exact_phi.network_phi_aggregations(tpm, cm, n, rng)
    return mean, mx


def case_segregated_biased(noise=0.05):
    """(A) Three independent COPY nodes, each strongly biased toward staying ON.

    No node influences any other → the system is reducible → Φ = 0. But the
    stationary distribution piles up on a corner of state space, far from the
    MaxCal marginal, so ψ is large. High ψ, zero Φ. Built at n = 3 to match the
    integrated case (B), so the comparison is at equal state-space size."""
    n = 3
    cm = np.eye(n, dtype=int)  # each node feeds only itself
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        st = [(s >> i) & 1 for i in range(n)]
        for j in range(n):
            # node copies itself, but with a low flip-to-off rate -> drifts ON
            out = 1.0 if st[j] == 1 else 0.85   # asymmetric: sticky ON
            tpm[s, j] = out * (1 - noise) + (1 - out) * noise
    return tpm, cm, n


def case_parity_coupled(noise=0.05):
    """(B) Three nodes each updating to the PARITY of the other two — a maximally
    integrative coupling (every node depends on the rest). Irreducible → Φ > 0.
    The dynamics spread occupancy broadly, keeping the stationary distribution
    close to the MaxCal marginal, so ψ is modest. Low(er) ψ, high Φ."""
    n = 3
    cm = (1 - np.eye(n)).astype(int)  # all-to-all except self
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        st = np.array([(s >> i) & 1 for i in range(n)])
        for j in range(n):
            others = np.array([st[k] for k in range(n) if k != j])
            out = float(others.sum() % 2)
            tpm[s, j] = out * (1 - noise) + (1 - out) * noise
    return tpm, cm, n


def report():
    print("Analytic dissociation cases (ψ vs exact IIT-4.0 Φ)")
    print("=" * 66)
    print(f"{'case':<34}{'ψ':>7}{'i(π)':>7}{'ϕ_ψ':>8}{'Φ_mean':>8}{'Φ_max':>7}")
    print("-" * 66)
    for name, builder in [
        ("(A) segregated, biased (Φ=0)", case_segregated_biased),
        ("(B) parity-coupled (integrated)", case_parity_coupled),
    ]:
        tpm, cm, n = builder()
        p = M.psi(tpm)
        phi_psi = M.psi_partitioned(tpm, n)
        phi_mean, phi_max = _phi(tpm, cm, n)
        print(f"{name:<34}{p['psi']:>7.3f}{p['i']:>7.3f}{phi_psi:>8.3f}"
              f"{phi_mean:>8.3f}{phi_max:>7.3f}")
    print("-" * 66)
    print("Expect: (A) ψ large, Φ=0;  (B) ψ modest, Φ>0  →  ψ and Φ dissociate.")


if __name__ == "__main__":
    report()

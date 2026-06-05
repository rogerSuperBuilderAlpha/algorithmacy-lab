"""Analytic dissociation: two systems at matched high entropy that complexity separates.

The entropy–content conundrum (Mago et al. 2026) is the claim that two states can share elevated
entropy yet differ in phenomenal richness. We exhibit it exactly on small systems. At *maximal* entropy
every system is uniform and hence independent, so complexity must vanish; the interesting comparison is
therefore at high-but-submaximal entropy, where two systems can match on entropy and differ on
complexity and integration.

  - "Contentless" (coarse-grained/underfitting analogue): n independent biased bits. High entropy, zero
    integration, zero TSE complexity, zero exact Φ.
  - "Rich" (fine-grained/structured analogue): the parity-ring dynamical system at a noise level chosen
    to match the contentless system's stationary entropy. Same entropy, but positive complexity and Φ.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from . import complexity as C
from .run import _structured_network
from foundations.proxy_audit import networks, exact_phi
from foundations.candidate_audit import measures as candmeas


def _independent_bits_dist(n, p_on):
    d = np.ones(2 ** n)
    for s in range(2 ** n):
        for i in range(n):
            d[s] *= p_on if ((s >> i) & 1) else (1 - p_on)
    return d / d.sum()


def report(n=4, rich_noise=0.125):
    rng = np.random.default_rng(0)

    # Rich: parity ring at chosen noise.
    cm, gate = _structured_network(n)
    tpm = networks.network_from_assignment(n, cm, gate, rich_noise, rng)
    pi = candmeas.stationary_distribution(tpm)
    H_rich = C.entropy_bits(pi)
    Cn_rich = C.tse_complexity(pi, n, max_subsets=64)
    phi_rich, phimax_rich, _, _ = exact_phi.network_phi_aggregations(tpm, cm, n, rng)

    # Contentless: independent biased bits matched to H_rich. Solve 4*Hb(p) = H_rich.
    from scipy.optimize import brentq

    def hb(p):
        p = min(max(p, 1e-9), 1 - 1e-9)
        return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
    target = H_rich / n
    p_on = brentq(lambda p: hb(p) - target, 1e-6, 0.5)
    dist = _independent_bits_dist(n, p_on)
    H_cont = C.entropy_bits(dist)
    Cn_cont = C.tse_complexity(dist, n, max_subsets=64)
    # exact Phi of independent bits is 0 by construction (no connections); report 0.

    print("Matched-entropy dissociation (n=%d)" % n)
    print("=" * 64)
    print(f"{'system':<34}{'H':>7}{'Cn':>8}{'Phi_max':>9}")
    print("-" * 64)
    print(f"{'contentless (independent bits)':<34}{H_cont:>7.3f}{Cn_cont:>8.3f}{0.0:>9.3f}")
    print(f"{'rich (parity ring, noise=%.3f)' % rich_noise:<34}{H_rich:>7.3f}{Cn_rich:>8.3f}{phimax_rich:>9.3f}")
    print("-" * 64)
    print("Same (high) entropy; complexity and Φ separate the rich from the contentless system.")
    return {"H_cont": H_cont, "H_rich": H_rich, "Cn_cont": Cn_cont, "Cn_rich": Cn_rich,
            "phimax_rich": phimax_rich, "p_on": p_on}


if __name__ == "__main__":
    report()

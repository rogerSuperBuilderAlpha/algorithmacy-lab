"""Maximum-caliber information ψ (Kearney 2026), for stationary Markov chains.

Definitions (transcribed from Kearney 2026, §5.1–5.2 / §6.2; all entropies in bits):

- Per-state conditional entropy of the dynamics:  Hc(x) = H(P(x, ·)).
- Per-state perplexity ("effective number of out-paths"):  PP(x) = 2^{Hc(x)}.
- MaxCal path-ensemble partition constant:  κ = Σ_x PP(x).
- MaxCal input marginal:  µ(x) = PP(x) / κ.
- Stationary distribution π of the chain.
- Entropy rate:  h(π) = Σ_x π(x) Hc(x).
- **Information:**  ψ(π) = log₂κ − H(π) − h(π)  =  D_KL(π ‖ µ)   (Kearney eq. 5.10).
  The KL form guarantees ψ ≥ 0; ψ = 0 iff π = µ (e.g. circulant / uniform chains).
- Related mutual information:  i(π) = H(π) − h(π).

Verified against the paper's worked cases: permutative TPM ⇒ κ = N·e^{h}, ψ = log N − H(π);
circulant TPM ⇒ π = µ ⇒ ψ = 0. Run `python -m psi_vs_phi.psi` to execute the controls.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from pyphi import convert

_EPS = 1e-12


def _entropy_bits(p):
    p = np.asarray(p, float)
    p = p[p > _EPS]
    return float(-(p * np.log2(p)).sum())


def stationary_distribution(P, start=None, iters=20000, tol=1e-14):
    """Stationary distribution of a state-by-state TPM by power iteration."""
    n = P.shape[0]
    pi = np.full(n, 1.0 / n) if start is None else np.asarray(start, float)
    pi = pi / pi.sum()
    for _ in range(iters):
        nxt = pi @ P
        if np.abs(nxt - pi).sum() < tol:
            pi = nxt
            break
        pi = nxt
    return pi / pi.sum()


def is_ergodic(P, tol=1e-6):
    """Practical ergodicity test for ψ to be well-defined: power iteration from a
    uniform start and from a one-hot start must converge to the *same* stationary
    distribution (a unique stationary dist that does not depend on the start).
    Catches reducible chains (multiple recurrent classes) and gross periodicity."""
    n = P.shape[0]
    pi_u = stationary_distribution(P)
    pi_1 = stationary_distribution(P, start=np.eye(n)[0])
    return float(np.abs(pi_u - pi_1).sum()) < tol


def conditional_entropies(P):
    """Per-state conditional entropy Hc(x) = H(P(x,·)) in bits, for each row."""
    return np.array([_entropy_bits(P[x]) for x in range(P.shape[0])])


def maxcal_marginal(P):
    """Return (mu, log2_kappa): the MaxCal input marginal µ(x)=PP(x)/κ and log₂κ,
    where PP(x)=2^{Hc(x)} and κ=Σ PP(x)."""
    Hc = conditional_entropies(P)
    PP = np.exp2(Hc)
    kappa = PP.sum()
    return PP / kappa, float(np.log2(kappa)), Hc


def psi(tpm_sbn):
    """Maximum-caliber information ψ(π) of a state-by-node TPM.

    Returns dict with psi (= log2κ − H(π) − h(π)), psi_kl (= D_KL(π‖µ); must match),
    i (= H(π) − h(π)), log2_kappa, H_pi, h_pi, and ergodic (bool)."""
    P = convert.state_by_node2state_by_state(np.asarray(tpm_sbn, float))
    mu, log2_kappa, Hc = maxcal_marginal(P)
    pi = stationary_distribution(P)
    H_pi = _entropy_bits(pi)
    h_pi = float((pi * Hc).sum())
    psi_val = log2_kappa - H_pi - h_pi
    # KL form (Kearney eq. 5.10): D_KL(pi || mu)
    m = pi > _EPS
    psi_kl = float((pi[m] * np.log2(pi[m] / np.clip(mu[m], _EPS, None))).sum())
    return {
        "psi": psi_val,
        "psi_kl": psi_kl,
        "i": H_pi - h_pi,
        "log2_kappa": log2_kappa,
        "H_pi": H_pi,
        "h_pi": h_pi,
        "ergodic": is_ergodic(P),
    }


# --------------------------------------------------------------------------- #
# Validation controls — run BEFORE trusting any ψ–Φ analysis.
# --------------------------------------------------------------------------- #

def _controls():
    rng = np.random.default_rng(0)
    print("ψ validation controls\n" + "-" * 40)

    def from_sbs(P):  # build psi-quantities directly from a state-by-state TPM
        mu, log2_kappa, Hc = maxcal_marginal(P)
        pi = stationary_distribution(P)
        H_pi, h_pi = _entropy_bits(pi), float((pi * Hc).sum())
        psi_v = log2_kappa - H_pi - h_pi
        mm = pi > _EPS
        kl = float((pi[mm] * np.log2(pi[mm] / np.clip(mu[mm], _EPS, None))).sum())
        return psi_v, kl, H_pi, log2_kappa, pi

    N = 6
    # 1) Uniform-rows (circulant-like null): every row uniform -> pi=mu -> psi=0.
    P_unif = np.full((N, N), 1.0 / N)
    p, kl, H, lk, _ = from_sbs(P_unif)
    print(f"uniform-rows:   psi={p:+.4f}  kl={kl:+.4f}  (expect ~0)")

    # 2) Deterministic single cycle (circulant permutation): pi uniform, Hc=0 -> psi=0.
    P_cyc = np.roll(np.eye(N), 1, axis=1)
    p, kl, H, lk, _ = from_sbs(P_cyc)
    print(f"single cycle:   psi={p:+.4f}  kl={kl:+.4f}  (expect ~0)")

    # 3) Biased-occupancy chain: strong drift to state 0 -> H(pi) << log2 N -> psi>0.
    P_bias = np.full((N, N), 0.02 / (N - 1))
    P_bias[:, 0] = 0.98
    P_bias = P_bias / P_bias.sum(1, keepdims=True)
    p, kl, H, lk, _ = from_sbs(P_bias)
    print(f"biased->state0: psi={p:+.4f}  kl={kl:+.4f}  H(pi)={H:.3f} (log2 N={np.log2(N):.3f}); expect psi>0")

    # 4) psi == psi_kl and psi >= 0 across random ergodic chains.
    maxdiff, minpsi = 0.0, np.inf
    for _ in range(200):
        R = rng.random((N, N)) ** 3 + 1e-3
        R = R / R.sum(1, keepdims=True)
        p, kl, *_ = from_sbs(R)
        maxdiff = max(maxdiff, abs(p - kl)); minpsi = min(minpsi, p)
    print(f"random chains:  max|psi - psi_kl| = {maxdiff:.2e} (expect ~0);  min psi = {minpsi:+.4f} (expect >= 0)")

    ok = abs(from_sbs(P_unif)[0]) < 1e-9 and abs(from_sbs(P_cyc)[0]) < 1e-9 and \
        from_sbs(P_bias)[0] > 0.1 and maxdiff < 1e-9 and minpsi > -1e-9
    print("-" * 40)
    print("ALL CONTROLS PASSED ✓" if ok else "CONTROLS FAILED ✗")
    return ok


if __name__ == "__main__":
    _controls()

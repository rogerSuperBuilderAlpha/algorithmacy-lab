# Findings: maximum-caliber information ψ does not track exact IIT-4.0 Φ

**TL;DR.** On networks where exact IIT-4.0 Φ is computable, the maximum-caliber information ψ of
Kearney (2026) — the system-level scalar ψ(π) = log₂κ − H(π) − h(π) — is **essentially
uncorrelated with Φ** (Spearman ρ ≈ 0.05–0.09, 95% CI including zero; detection AUC ≈ chance),
stable across two seeds. ψ behaves like an order/disorder *complexity* measure, not an
*integration* measure — outcome **H0**, as theory anticipated. This is, to our knowledge, the first
direct numerical test of the question Kearney explicitly posed but did not answer.

## Result (seed 1; primary analysis on the ergodic subset)

270 random Boolean‑gate networks (n ∈ {3,4}); 181 are ergodic, so ψ — defined only for ergodic,
homogeneous Markov chains — is well‑defined on those. 55/181 have Φ > 0.

Measures vs exact Φ, ranked by |Spearman ρ|:

| measure | Spearman ρ | Pearson r | AUC(Φ>0) |
|---------|-----:|-----:|-----:|
| Φ whole‑minus‑sum | **0.580** | 0.700 | 0.860 |
| integrated synergy | 0.479 | 0.183 | 0.784 |
| total correlation | −0.373 | −0.158 | 0.261 |
| stochastic interaction | 0.136 | 0.283 | 0.573 |
| i(π) = H − h | −0.135 | 0.211 | 0.393 |
| time‑delayed MI | −0.135 | 0.211 | 0.394 |
| **ψ (MaxCal information)** | **0.085** | −0.116 | **0.524** |
| causal density | −0.011 | 0.237 | 0.513 |

- **ψ vs Φ:** ρ = +0.085, **95% CI [−0.08, +0.24]** (includes 0); AUC 0.524 (chance); Pearson −0.116.
- **Among Φ>0 only:** ρ = −0.318 (if anything, slightly negative).
- **By size:** n=3 ρ = 0.096, n=4 ρ = 0.028.
- **Seed 2 replication** (181 ergodic nets): ρ = 0.052, AUC 0.516, among Φ>0 ρ = −0.266. Stable null.
- **ψ's companion i(π)** (mutual information) also fails (ρ = −0.135) — the signal is not hiding in i.

## Verdict: H0

ψ ranks **near the bottom** of the leaderboard, far below the whole‑minus‑sum family. Crucially, the
*same* framework on the *same* networks shows Φ whole‑minus‑sum tracks Φ well (ρ = 0.58, AUC 0.86)
— so this is not a dead detector. **ψ specifically does not track integration.** It is a
complexity‑type quantity, clustering with the dependence/complexity proxies (total correlation,
i(π)) that our `proxy_audit` already found do not track Φ.

## Why (theory matches the data)

ψ is built entirely from **whole‑system entropies** — the stationary distribution's marginal
entropy and entropy rate against a maximum‑caliber reference. It has **no partition or exclusion
step.** Exact IIT Φ is, by definition, irreducibility *across the minimum information partition*.
The proven FEP↔constrained‑MaxEnt duality (Ramstead et al. 2023) that underwrites Kearney's bridge
operates at the *system* level and has **no analogue of Φ's partition/exclusion/maximisation
structure** — so there was no a‑priori reason ψ should track Φ, and it does not. The measures that
*do* track Φ here (whole‑minus‑sum, integrated synergy) are precisely the ones that *do* contain a
whole‑minus‑parts operation.

## What this does and does not say

- It **answers the specific empirical question Kearney raised** — does the MaxCal information ψ
  connect to IIT's Φ? On these systems, no.
- It does **not** refute Kearney's *repertoire‑level* derivation (that the IIT 3.0 cause/effect
  repertoire machinery can be re‑expressed via constrained MaxEnt). That is a structural claim
  about the construction, distinct from whether the system‑level scalar ψ proxies Φ. Testing the
  repertoire‑level derivation is Tier B.
- It is consistent with the FEP↔IIT link being real at the level Ramstead et al. prove (free
  energy ↔ constrained entropy) while **not** descending to a ψ≈Φ relationship.

## Caveats

- ψ is only defined for ergodic chains; the primary analysis is the 181/270 ergodic networks
  (non‑ergodic ones flagged and excluded). Small systems (n ∈ {3,4}); a specific Boolean‑gate
  ensemble.
- **3.0/4.0 mismatch:** Kearney re‑derives IIT **3.0** repertoires (earth‑mover's distance); we
  test against canonical **4.0** Φ (intrinsic difference). The near‑zero ψ–Φ correlation is,
  however, not a subtle-measure-choice effect — ψ is near‑orthogonal to Φ and to the broad
  integration signal regardless.
- We tested the **system‑level stationary ψ** (the cheap scalar the paper gives), not the full
  CMEP repertoire construction.

## Reproduce
`python -m psi_vs_phi.run 15 1 && python -m psi_vs_phi.analyze`. ψ is validated on controls first
(`python -m psi_vs_phi.psi`): ψ=0 for circulant/uniform chains, ψ=log₂N−H(π) for permutative,
ψ≥0 and ψ==KL(π‖µ) across random chains.

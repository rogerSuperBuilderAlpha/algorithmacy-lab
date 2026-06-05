# Findings: maximum-caliber information ψ does not track exact IIT-4.0 Φ

**TL;DR.** On networks where exact IIT-4.0 Φ is computable, the maximum-caliber information ψ of
Kearney (2026) — the system-level scalar ψ(π) = log₂κ − H(π) − h(π) — is **essentially uncorrelated
with Φ** (Spearman ρ ≈ 0.09, 95% CI includes zero; detection AUC ≈ chance), robust to aggregation and
stable across five seeds. Crucially, **giving ψ a partition step does not rescue it**: the partitioned
MaxCal measure ϕ_ψ *anti*-correlates with Φ (ρ = −0.28) while the identical partition on a mutual
information (Φ_WMS) tracks Φ at ρ = 0.58. ψ behaves like an order/disorder *complexity* measure, not
an *integration* measure — outcome **H0**, as theory anticipated, and now shown to be structural
rather than a measure-choice artefact.

## Result (seed 1; primary analysis on the ergodic subset)

270 random Boolean-gate networks (n ∈ {3,4}); 181 ergodic (ψ well-defined); 55/181 have Φ > 0.

Measures vs exact Φ (mean aggregation), ranked by |Spearman ρ|:

| measure | Spearman ρ | 95% CI | AUC(Φ>0) |
|---------|-----:|:---:|-----:|
| Φ whole-minus-sum (partition-based) | **+0.580** | [+0.46,+0.67] | 0.860 |
| integrated synergy (partition-based) | +0.479 | [+0.37,+0.58] | 0.784 |
| total correlation (complexity) | −0.373 | [−0.50,−0.24] | 0.261 |
| **ϕ_ψ (partitioned MaxCal)** | **−0.276** | [−0.42,−0.13] | 0.359 |
| stochastic interaction | +0.136 | [−0.02,+0.28] | 0.573 |
| i(π) = H − h (MaxCal companion) | −0.135 | [−0.28,+0.01] | 0.393 |
| time-delayed MI | −0.135 | [−0.28,+0.01] | 0.394 |
| **ψ (MaxCal information)** | **+0.085** | [−0.08,+0.24] | **0.524** |
| causal density | −0.011 | [−0.16,+0.13] | 0.513 |

- **ψ vs Φ:** ρ = +0.085, p = 0.25, AUC 0.524 (chance), Pearson −0.116.
- **Aggregation robustness:** π-weighted Φ ρ = +0.018 (p = 0.81); max Φ ρ = +0.125 (p = 0.09). Null
  under all three aggregations.
- **Among Φ>0 only:** ρ = −0.318 (if anything, slightly negative).
- **Power:** min detectable |ρ| ≈ 0.146 at n = 181; ψ sits below it, Φ_WMS (0.58) far above.
- **Within-regime (Simpson's check):** per-size ρ = 0.096 (n=3), 0.028 (n=4); per-cell ρ ∈ [−0.17,
  +0.16]; per-gate ρ ∈ [+0.02, +0.15]. No stratum shows tracking.
- **Five-seed stability:** ρ = 0.085, 0.052, 0.083, 0.122, 0.137. Pooled (906 nets) ρ = +0.096,
  CI [+0.02,+0.17], p = 0.004 — statistically nonzero at large n but **negligible** (~1% of rank
  variance vs Φ_WMS's ~34%), and of inconsistent sign across subsets.

## The partition step does not rescue ψ (the decisive new result)

ϕ_ψ = ψ(whole) − min-partition[ψ(A)+ψ(B)] is ψ given IIT's MIP logic, built on the *same*
marginalisation Φ_WMS uses. It gives ρ = **−0.276** (p < 0.001, AUC 0.359): a significant *negative*
association. The identical partition operation on a mutual information (Φ_WMS) gives ρ = +0.58. The
partition is therefore not the missing ingredient — the **kind of quantity being partitioned** is. ψ
is a KL self-divergence (one distribution vs a reference derived from the same dynamics); a mutual
information is a joint-vs-factorised comparison. Cutting the latter exposes irreducibility; cutting
the former does not.

## IIT 3.0 vs 4.0 (version objection closed)

n=3 subset (90 ergodic nets, 37 with Φ₃>0): ψ vs IIT-3.0 Φ ρ = +0.113; ψ vs IIT-4.0 Φ (same nets)
ρ = +0.096; **3.0 vs 4.0 ρ = +0.858**. ψ misses both, and the two IIT versions agree, so the oracle
choice is not the confound. (n=4 3.0 omitted: EMD path unstable in this 4.0 checkout.)

## Analytic dissociation (`python -m foundations.psi_vs_phi.dissociation`)

| case | ψ | i(π) | ϕ_ψ | Φ_mean | Φ_max |
|---|---:|---:|---:|---:|---:|
| (A) segregated, biased COPY nodes, n=3 (Φ=0) | 2.623 | 0.027 | 0.000 | 0.000 | 0.000 |
| (B) parity-coupled, integrated, n=3 | 0.428 | 1.713 | 0.428 | 0.689 | 1.378 |

ψ ranks the *un*integrated system (A) about 6× above the maximally integrated one (B), which has zero
Φ. A clean sign-inversion of the ranking at equal state-space size (both n=3).

## Verdict: H0 (structural)

ψ (and ϕ_ψ) cluster with the complexity quantities at the bottom of the leaderboard, far below the
whole-minus-sum family — and the *same* framework on the *same* networks shows Φ_WMS tracks Φ well
(ρ = 0.58, AUC 0.86), so this is not a dead detector. ψ is built entirely from whole-system entropies
with **no partition or exclusion step**; exact IIT Φ *is* irreducibility across the MIP after an
exclusion maximisation. The proven FEP↔constrained-MaxEnt duality (Ramstead et al. 2023) is
system-level and has **no analogue of Φ's partition/exclusion structure** — so ψ was never licensed to
track Φ, and bolting a partition onto the wrong kind of scalar (ϕ_ψ) makes it worse, not better.

## What this does and does not say

- It answers, negatively, the specific empirical question Kearney raised about the system-level
  scalar ψ — and forecloses the partition-rescue and the 3.0-vs-4.0 escape hatches.
- It does **not** refute Kearney's *repertoire-level* derivation (re-expressing IIT's repertoire
  calculus via constrained MaxEnt) — a structural claim about the construction, distinct from whether
  the scalar proxies Φ. That is Tier B.
- It is consistent with the FEP↔IIT link being real at the level Ramstead et al. prove (free energy
  ↔ constrained entropy) while **not** descending to ψ ≈ Φ. The credible remaining route is
  *learning dynamics* (dΦ/dt vs surprise), not the static scalar.

## Caveats

- ψ defined only for ergodic chains (181/270); the screen is a practical reducibility/periodicity
  filter. Small systems (n ∈ {3,4}); a specific Boolean-gate ensemble — the only regime with exact-Φ
  ground truth. The structural argument does not depend on the slice.
- 3.0 comparator is n=3 only (EMD instability at n=4 in this checkout).
- Tested the system-level scalar ψ and its partitioned extension ϕ_ψ; compared against scalar system
  Φ, not the full Φ-structure (distinctions + relations).

## Reproduce
`python -m foundations.psi_vs_phi.psi` (controls) → `python -m foundations.psi_vs_phi.run 15 1` (… seeds 1–5) →
`python -m foundations.psi_vs_phi.exact_phi3 15 1` (3.0, n=3) → `python -m foundations.psi_vs_phi.analyze` →
`python -m foundations.psi_vs_phi.figures`.

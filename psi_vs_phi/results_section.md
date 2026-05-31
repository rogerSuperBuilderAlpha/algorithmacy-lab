# Results (draft prose — superseded by the assembled `paper_draft.md` §4)

## 3.1 ψ is well-defined and behaves as specified

Before relating ψ to Φ we validated the implementation against Kearney's own predictions
(`psi.py`). For circulant and uniform-row transition matrices the stationary distribution equals
the maximum-caliber marginal (π = µ) and ψ = 0; for deterministic permutations ψ = log₂N − H(π);
across random chains ψ ≥ 0 and the two equivalent forms — ψ = log₂κ − H(π) − h(π) and the
Kullback–Leibler form ψ = D_KL(π ‖ µ) — agreed to machine precision (max difference 1.3×10⁻¹⁵).
ψ is therefore computed exactly and as defined.

## 3.2 ψ does not track exact IIT-4.0 Φ, robustly

For 270 random Boolean-gate networks (n ∈ {3,4}), 181 were ergodic (the set on which ψ is defined),
55 with Φ > 0. Across these, **ψ is essentially uncorrelated with exact Φ**: Spearman ρ = 0.085 (95%
CI [−0.08, +0.24]; exact p = 0.25), Pearson r = −0.116, detection AUC = 0.524 (chance). The result is
robust to how Φ is aggregated (π-weighted mean ρ = 0.018; max ρ = 0.125), stable across five seeds
(ρ = 0.085, 0.052, 0.083, 0.122, 0.137), and absent in every density/noise/gate stratum (per-cell
ρ ∈ [−0.17, +0.16]). Pooled over five seeds (906 nets) the tiny association becomes statistically
nonzero (ρ = 0.096, p = 0.004) but remains negligible — ~1% of rank variance, an order of magnitude
below a genuine proxy, and of inconsistent sign. Restricting to Φ > 0 gives ρ = −0.318. With n = 181
the minimum detectable |ρ| is ≈ 0.146; ψ sits below it. The companion i(π) also fails (ρ = −0.135),
so the signal is not hiding in the mutual-information term.

## 3.3 The failure is specific to ψ, not the test, and the partition step does not rescue it

On the identical ergodic networks, the whole-minus-sum Φ correlates strongly with exact Φ (ρ = 0.580,
AUC = 0.860) and integrated synergy moderately (ρ = 0.479) — the apparatus detects integration when
present. The decisive new test: a **partitioned MaxCal measure ϕ_ψ**, ψ given IIT's
minimum-information-partition step on the *same* marginalisation Φ_WMS uses, does *not* recover the
signal; it **anti-correlates** (ρ = −0.276, p < 0.001, AUC = 0.359). The identical partition applied
to a mutual information (Φ_WMS) tracks Φ; applied to ψ it does not. The missing ingredient is not the
partition but the kind of quantity being partitioned: ψ is a KL self-divergence, not a
joint-vs-factorised mutual information.

**Table 1.** Association with exact IIT-4.0 Φ across the 181 ergodic networks (seed 1).

| measure | Spearman ρ | 95% CI | AUC(Φ>0) |
|---|---:|:---:|---:|
| Φ whole-minus-sum | +0.580 | [+0.46,+0.67] | 0.860 |
| integrated synergy | +0.479 | [+0.37,+0.58] | 0.784 |
| total correlation | −0.373 | [−0.50,−0.24] | 0.261 |
| **ϕ_ψ (partitioned MaxCal)** | **−0.276** | [−0.42,−0.13] | 0.359 |
| stochastic interaction | +0.136 | [−0.02,+0.28] | 0.573 |
| i(π) = H − h | −0.135 | [−0.28,+0.01] | 0.393 |
| **ψ (maximum-caliber information)** | **+0.085** | [−0.08,+0.24] | 0.524 |
| causal density | −0.011 | [−0.16,+0.13] | 0.513 |

## 3.4 ψ misses IIT 3.0 and 4.0 alike

On the n=3 subset (90 ergodic nets), ψ vs IIT-3.0 Φ ρ = 0.113 and ψ vs IIT-4.0 Φ ρ = 0.096, while 3.0
and 4.0 Φ agree (ρ = 0.858). The version of IIT Kearney re-derives (3.0) is not the issue.

## 3.5 Analytic dissociation

Two hand-built systems make the mechanism concrete: a segregated, biased system scores ψ = 1.749 with
Φ = 0, while a parity-coupled integrated system scores ψ = 0.428 with Φ_max = 1.378. ψ ranks the
unintegrated system above the integrated one — the aggregate null in its purest analytic form.

## 3.6 Interpretation

On these systems the maximum-caliber information ψ is a complexity-type quantity that does not proxy
integrated information, and no partition step converts it into one. This matches the theoretical
expectation: the duality underwriting the MaxCal–FEP bridge (Ramstead et al. 2023) is system-level
and contains no analogue of Φ's partition/exclusion/maximisation structure. It bounds the bridge to
the level at which it is proven and does not extend it to ψ ≈ Φ. It does not bear on Kearney's
repertoire-level derivation (Tier B). The credible remaining route to an empirical IIT–FEP link is
learning dynamics, not a static scalar.

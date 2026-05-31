# Results (draft)

## 3.1 ψ is well-defined and behaves as specified

Before relating ψ to Φ we validated the implementation against Kearney's own predictions
(`psi.py`). For circulant and uniform-row transition matrices the stationary distribution equals
the maximum-caliber marginal (π = µ) and ψ = 0; for deterministic permutations ψ = log₂N − H(π);
across random chains ψ ≥ 0 and the two equivalent forms — ψ = log₂κ − H(π) − h(π) and the
Kullback–Leibler form ψ = D_KL(π ‖ µ) — agreed to machine precision (max difference 1.3×10⁻¹⁵).
ψ is therefore computed exactly and as defined.

## 3.2 ψ does not track exact IIT-4.0 Φ

We computed ψ and exact IIT-4.0 Φ for 270 random Boolean-gate networks (n ∈ {3,4}). ψ is defined
only for ergodic, homogeneous Markov chains; 181 of the 270 networks were ergodic, and these form
the primary analysis set (55 with Φ > 0).

Across these networks, **ψ is essentially uncorrelated with exact Φ**: Spearman ρ = 0.085 (95%
bootstrap CI [−0.08, +0.24], i.e. not distinguishable from zero), Pearson r = −0.116, and the area
under the ROC curve for detecting Φ > 0 from ψ is 0.524 — chance. Restricting to integrated systems
(Φ > 0) gives ρ = −0.318, if anything slightly negative. The result is stable: an independent
second ensemble (seed 2) gave ρ = 0.052 and AUC = 0.516. ψ's companion quantity i(π) = H(π) − h(π)
likewise fails to track Φ (ρ = −0.135), so the absent signal is not hidden in the
mutual-information term. Figure 1 shows the scatter: a structureless cloud, with the highest-Φ
networks sitting at low ψ.

## 3.3 The failure is specific to ψ, not the test

To confirm that the framework can detect a measure that *does* track Φ, we ranked ψ against the
candidate integrated-information measures on the identical ergodic networks (Table 1). The
whole-minus-sum Φ correlates strongly (ρ = 0.580, AUC = 0.860) and the co-information "integrated
synergy" moderately (ρ = 0.479); ψ ranks near the bottom (ρ = 0.085), clustering with the
dependence/complexity measures — total correlation (ρ = −0.373) and i(π) (ρ = −0.135) — that are
known not to track Φ. The measures that succeed are precisely those built on a whole-minus-parts
(partition) operation; ψ, which is built from whole-system entropies with no partition step, is not
among them.

**Table 1.** Association with exact IIT-4.0 Φ across the 181 ergodic networks (seed 1).

| measure | Spearman ρ | AUC(Φ>0) |
|---|---:|---:|
| Φ whole-minus-sum | 0.580 | 0.860 |
| integrated synergy | 0.479 | 0.784 |
| total correlation | −0.373 | 0.261 |
| stochastic interaction | 0.136 | 0.573 |
| i(π) = H − h | −0.135 | 0.393 |
| **ψ (maximum-caliber information)** | **0.085** | **0.524** |
| causal density | −0.011 | 0.513 |

## 3.4 Interpretation

On these systems the maximum-caliber information ψ is a complexity-type quantity that does not
proxy integrated information. This matches the theoretical expectation: the duality that
underwrites the MaxCal–FEP bridge (Ramstead et al. 2023) relates free energy to constrained entropy
at the *system* level and contains no analogue of Φ's partition, exclusion, and maximisation
structure, so there is no a-priori reason for the system-level ψ to track Φ — and empirically it
does not. This is a direct, negative answer to the question Kearney poses; it bounds the
MaxCal–IIT bridge to the level at which it is proven (free energy ↔ constrained entropy) and does
not extend it to a ψ ≈ Φ relationship. It does not bear on Kearney's separate repertoire-level
derivation, which remains for future work (Tier B).

---
citekey: mayner2025intrinsic
title: Intrinsic Cause--Effect Power: The Tradeoff Between Differentiation and Specification
authors: Mayner, William G. P. and Marshall, William and Tononi, Giulio
year: 2026
doi: 10.3390/e28040410
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2510.03881
sha256: 4374aeddbaf4076e67ff1eff6ccddc0f43518b43b0bf9417f2162f11ee6cb1de
pdf_path: literature/pdfs/mayner2025intrinsic.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Integrated information theory (IIT) operationalizes the existence of consciousness in terms of the intrinsic, specific cause-effect power of a substrate of units. This paper argues that for a substrate in its actual state to have intrinsic, specific cause-effect power, its units must satisfy two complementary requirements: (i) they must provide themselves with a repertoire of alternative cause-effect states (intrinsic availability), and (ii) they must increase the probability of one specific cause-effect state. Prior work captured only requirement (ii) (renamed here "intrinsic specification," assessed as the intrinsic difference from maximal differentiation); the new contribution is "intrinsic differentiation," which captures requirement (i) and is assessed as the intrinsic difference from a maximally specific (deterministic) distribution. Intrinsic information is defined as the minimum of differentiation and specification, and this is folded into the system integrated information measure φ_s. Through worked examples (single-unit "monads," small micro-unit systems/complexes, and macro units), the authors show that a tradeoff between differentiation and specification—equivalently between determinism and indeterminism—is a necessary condition for positive intrinsic existence, since purely deterministic systems have zero differentiation and purely random systems have zero specification. They argue this requirement of some intrinsic indeterminism resonates with ideas about criticality and metastability in brain dynamics.

## Key facts it relies on
- The paper builds directly on the IIT 4.0 formulation of φ_s from Albantakis et al. 2023 (PLOS Comp Biol, ref [1]); the framework is "the same as the IIT 4.0 definition of φ_s from [1], until Eq. (23)," when intrinsic differentiation is incorporated.
- The intrinsic difference (ID) between two probability distributions p and q is ID(p,q) = max_s p(s) log(p(s)/q(s)); it is asymmetric (not a metric), and decomposes into a selectivity term p(s) and an informativeness term log(p(s)/q(s)).
- Intrinsic effect differentiation is defined as i^e_diff(s,s') = ID(p_s'(s̄), p_e(s̄|s)) = −log(p_e(s'|s)), i.e., the ID between a maximally specific (deterministic) distribution for s' and the conditional effect distribution; intrinsic cause differentiation is defined analogously.
- Intrinsic specification is the previously defined intrinsic-information quantity (renamed), e.g. i^e_spec(s,s̄) = p_e(s̄|s) log(p_e(s̄|s)/p_e(s̄)), the ID between the conditional effect distribution and the unconditional effect distribution.
- Intrinsic information is the minimum of intrinsic differentiation and intrinsic specification: ii(s) = min{ii_c(s), ii_e(s)} with ii_{c/e}(s) = min{i^{c/e}_diff(s), i^{c/e}_spec(s)}, justified by IIT's "principle of minimal existence."
- For a single-unit system (a "monad"), φ_s(s) = ii(s); intrinsic differentiation is maximized when past/future states are equally likely (specification then zero) and specification is maximized when the monad is deterministic (differentiation then zero), so φ_s is maximized at intermediate determinism.
- In the monad (imperfect COPY gate, stays in state with probability p), φ_s(s) = ii(s) = min{p log(2p), −log(p)}; numerically the maximum value φ_s(s) = 0.427 occurs at p = 0.744 (Figure 2C).
- A fully deterministic system has i_diff(s) = 0 and thus ii(s) = 0; a uniformly random system has i_spec(s) = 0 and thus ii(s) = 0; only a balanced system achieves positive intrinsic information ii(s) > 0 (Figure 1).
- For a 6-unit example system from [1] with temperature parameter K (originally K = 4 made the full 6-unit system the complex), the full 6-unit system is a complex for K ≳ 0.775 and breaks into two-unit complexes for K ≲ 0.775; intrinsic differentiation only affects φ_s when K ≳ 2.839 (Figure 3F).
- In the macro-unit (Example 3) imperfect-AND two-unit system from Marshall et al. [7], the macro monad α = {A,B} has greater φ_s than the corresponding micro system for p ∈ (0.096, 0.5) (Figure 4C); at p = 0.05 (the value used in [7]) α satisfies maximally-irreducible-within and outperforms the micro system, but whether macro outperforms micro depends on intrinsic differentiation (via p).
- Calculations were performed with the PyPhi toolbox for IIT (ref [10]); the formalism assumes a discrete-time finite-state system governed by a transition-probability matrix (TPM) and the do(·) causal-intervention operator (Pearl, ref [9]).

## Critical notes from the literature
- The paper acknowledges its central motivation is conceptual—aligning the mathematical formulation with IIT's postulates (notably the postulate of intrinsicality, that existence must be defined from the system's own perspective, not an outside observer's)—rather than empirical.
- The authors note intrinsic differentiation essentially captures indeterminism, but without the standard "noise" interpretation; they treat indeterminism as intrinsic to the system and a requirement for its existence, and acknowledge that the ontological status of quantum indeterminism "remains subject to debate."
- Scope is limited to simple/illustrative systems: an isolated binary unit, small systems of micro units, and macro units; the authors note that whether macro systems outperform their micro constituents depends on the level of determinism, and macro-level differentiation may prevent the macro system from outperforming the micro system.
- The framework is presented as a refinement that changes the IIT 4.0 measure only from Eq. (23) onward; the authors flag that in the analyzed 6-unit example the change in which subset is the complex is "not due to the introduction of intrinsic differentiation" (which only affects φ_s for K ≳ 2.839).

## Key topics covered
Integrated information theory (IIT 4.0); intrinsic cause-effect power; intrinsic differentiation; intrinsic specification; intrinsic information; intrinsic difference (ID) measure; system integrated information φ_s; determinism vs. indeterminism tradeoff; monads (single-unit systems); complexes; macro units / causal grains; maximally-irreducible-within condition; directed partitions; principle of maximal/minimal existence; transition-probability matrices; do-operator / causal marginalization; PyPhi toolbox; criticality and metastability in brain dynamics; collapse models and quantum indeterminism.

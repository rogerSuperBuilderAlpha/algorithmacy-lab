---
citekey: mediano2022integrated
title: Integrated information as a common signature of dynamical and information-processing complexity
authors: Mediano, Pedro A. M. and Rosas, Fernando E. and Farah, Juan Carlos and Shanahan, Murray and Bor, Daniel and Barrett, Adam B.
year: 2022
doi: 10.1063/5.0063384
arxiv: null
journal: Chaos: An Interdisciplinary Journal of Nonlinear Science
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2106.10211
sha256: 8432b116c09404be78dbfcc8d6d6c65fed710fc2a294e198942f28d75a22ceb4
pdf_path: literature/pdfs/mediano2022integrated.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper argues that Integrated Information Theory (IIT), stripped of its contentious claims about consciousness, can serve as a pragmatic, domain-agnostic framework for studying complexity that bridges the historically divided information-processing and dynamical-systems approaches to complexity science. The authors use a redundancy-corrected measure of integrated information, Φ^R (derived from the Integrated Information Decomposition, ΦID, framework), and apply it to two paradigmatic systems: networks of coupled Kuramoto oscillators and cellular automata (CA). For coupled oscillators, they show that Φ^R peaks sharply within the critical phase-transition region between desynchronisation and hypersynchronisation, coinciding with high metastability, and that it is more discriminating than coalition entropy or metastability alone. For cellular automata, they show Φ^R grows monotonically with Wolfram complexity class, peaks at intermediate values of Langton's λ ("edge of chaos"), and locally detects coherent emergent structures (gliders, blinkers, collisions). They conclude that integrated information is a common signature capturing heterogeneous markers of complexity — metastability, criticality, and distributed computation — without relying on idiosyncratic, ad-hoc criteria.

## Key facts it relies on
- The effective information φ for a bipartition B = {M¹, M²} is defined as φ[X;τ,B] = I(X_{t−τ};X_t) − Σ_{k=1}^{2} I(M^k_{t−τ};M^k_t), where I is Shannon mutual information and τ is the integration timescale (Eq. 1).
- Φ is computed by exhaustively searching all bipartitions and selecting the Minimum Information Bipartition (MIB), with a normalisation factor K(B) = min{H(M¹),H(M²)} introduced to avoid biasing toward unbalanced bipartitions (Eqs. 2a–2c).
- Standard Φ can take negative values because it includes a negative redundancy component (the parts containing the same predictive information), so Φ < 0 when redundancy-dominated; the revised Φ^R adds back redundancy via the Minimum Mutual Information (MMI) function: φ^R[X;τ,B] = φ[X;τ,B] + min_{i,j} I(M^i_{t−τ};M^j_t) (Eq. 3).
- The coupled-oscillator model is a community-structured network of N=8 communities of m=32 Kuramoto oscillators each (256 total), with intra-community coupling a=0.6, inter-community coupling b=0.4, inter-community connection probability q=1/8, natural frequency ω=1, normalisation constant κ=64, parametrised by phase lag β = π/2 − α (Eqs. 4–5).
- For oscillators they ran 1500 simulations with β uniform in [0,2π], using a 4th-order Runge-Kutta integrator with step 0.05, each run 5×10⁶ timesteps, discarding the first 10⁴ as transient, thinning by factor 5, coalition threshold γ=0.8; Φ^R is zero for desynchronised systems and peaks in the transition region (Fig. 4), more narrowly than coalition entropy H_c.
- Φ^R grows with integration timescale τ while time-delayed mutual information (TDMI) I(X_{t−τ};X_t) decreases with higher τ — at short timescales the system is redundancy-dominated (predictable from parts), at longer timescales prediction is enabled by interactions between parts (Fig. 5).
- Measurement noise: flipping each bit with probability p, Φ^R decays exponentially as η = exp(−p/ℓ) with ℓ ≈ 0.04; a 5% measurement noise can wipe out 70% of the observed integrated information (Fig. 6).
- For cellular automata, following Lizier's simulation parameters, they initialise a tape of length 10⁴ with i.i.d. random values, discard the first 100 steps, and run 600 more steps to estimate probability distributions; Φ^R grows monotonically with Wolfram complexity class (I→IV), being higher and positive for complex classes IV and III and lower (often negative) for classes I and II (Fig. 7).
- Using a 6-colour, range-2 CA, Φ^R peaks at intermediate values of Langton's λ ("edge of chaos"), and when plotted against Δλ (distance from the transition event) runs from different automata align onto a consistent universal profile (Fig. 8).
- Local/pointwise Φ is high in all coherent structures of ECA rules 54 and 110 — gliders, blinkers, and collisions — indicating it detects storage, transfer, and modification of information without being explicitly designed to (Fig. 9); the paper builds on Lizier's local information dynamics (excess entropy/storage e_k, transfer entropy TE).

## Critical notes from the literature
- The authors explicitly dissociate their work from IIT's original consciousness claims, noting those "audacious claims" caused "heated debate" and drove scientists away; they adopt a "pragmatic IIT" based on Balduzzi & Tononi's IIT 2.0 rather than more recent consciousness-focused accounts that have "hindered its reach and made the theory applicable only in small discrete systems."
- The standard Φ measure has a drawback that it can take negative values, hindering interpretation as a measure of system-wide integration; this motivates the redundancy-corrected Φ^R used throughout, though Φ^R itself is sensitive and "vanishes quickly" if the specific spatio-temporal patterns are disrupted.
- The authors caution that the relationship between integrated information, metastability, criticality, and distributed computation "is not an identity" — their agreement is an important empirical finding conveyed by Φ, not a definitional equivalence.
- They suggest that the capacity to integrate information is "a necessary, but not sufficient, condition for universal computation," and note that whether a CA rule belongs to class III or IV is formally undecidable.
- The pointwise/local Φ used in the CA coherent-structure analysis (Fig. 9) has NOT been ΦID-revised, because the simpler redundancy in Eq. 3 does not naturally translate to a pointwise setting; pointwise ΦID metrics remain an open problem deferred to future work.

## Key topics covered
Integrated Information Theory (IIT), Integrated Information Decomposition (ΦID), effective information φ, redundancy-corrected Φ^R, Minimum Information Bipartition (MIB), Minimum Mutual Information (MMI) redundancy, coupled Kuramoto oscillators, community-structured networks, chimera states, metastability, instantaneous synchronisation, coalition entropy, criticality and phase transitions, integration timescale τ, time-delayed mutual information, measurement-noise robustness, cellular automata, Wolfram complexity classes, Langton's λ / edge of chaos, distributed computation, local/pointwise information dynamics (storage/transfer/modification), gliders and blinkers, complexity science unification.

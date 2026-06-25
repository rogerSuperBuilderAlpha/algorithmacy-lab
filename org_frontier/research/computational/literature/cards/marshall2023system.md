---
citekey: marshall2023system
title: System Integrated Information
authors: Marshall, William and Grasso, Matteo and Mayner, William G. P. and Zaeemzadeh, Alireza and Barbosa, Leonardo S. and Chastain, Erick and Findlay, Graham and Sasai, Shuntaro and Albantakis, Larissa and Tononi, Giulio
year: 2023
doi: 10.3390/e25020334
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://vtechworks.lib.vt.edu/bitstreams/918fdd25-c1b3-4197-b2af-15796d7a970d/download
sha256: 231b19ce5aa2409be610cffe460b8fa3c28dc5a8ac706913f3228d2a10c8f2ff
pdf_path: literature/pdfs/marshall2023system.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This paper introduces a definition of system integrated information (φ_s) for Integrated Information Theory (IIT) that is aligned with the postulates of IIT 4.0. IIT starts from five axioms of experience (intrinsicality, information, integration, exclusion, composition) and translates them into postulates about the physical substrate of consciousness (a "complex"). The authors build a mathematical framework based on the first four postulates—existence, intrinsicality, information, integration—plus exclusion, to define φ_s and use it to identify complexes. The measure is grounded in a recently introduced measure of intrinsic information that uniquely satisfies the existence, intrinsicality, and information postulates. Using small example systems computed with the PyPhi package, the paper demonstrates how determinism, degeneracy, and "fault lines" in connectivity affect system integrated information. It shows that a complex is identified as the system S* that maximizes φ_s, and that any overlapping candidate systems have lower φ_s. The work also presents a theorem bounding the maximum possible integrated information for a given partition and a recursive algorithm for carving a universe into non-overlapping complexes.

## Key facts it relies on
- IIT identifies five axioms of experience—intrinsicality, information, integration, exclusion, composition—plus the zeroth axiom Existence; these are translated into postulates about the substrate of consciousness (a "complex").
- The starting point is a stochastic system U with a transition probability function T_U ≡ p(s̄ | do(u)), defined via interventions (do-operator) and measurements, assuming units are independent given the current state.
- Intrinsic information is defined as the product of two terms, informativeness and selectivity; the intrinsic effect information is ii_e(s,s̄) = p_e(s̄|s) log( p_e(s̄|s) / p_e(s̄) ), and cause information is defined analogously using the cause repertoire (Bayes' Theorem inversion).
- System integrated information for a partition is the minimum of integrated cause and effect information: φ_s(s,θ) = min{ φ_c(s,θ), φ_e(s,θ) }; the system's φ_s is taken relative to its minimum partition (the "fault line").
- The minimum partition θ' minimizes relative integrated information φ_s(s,θ) / max φ_s(s,θ), and partitions must cut into K ≥ 2 parts using directional partitions (cutting inputs ←, outputs →, or both ↔).
- Theorem 1: the maximum possible value of φ_s(s,θ) equals Σ_{i=1}^K |S^(i)||X^(i)|, the total number of potential connections cut by the partition (proof in Appendix B).
- A complex is the maximally irreducible system S* = argmax φ_s(s); overlapping systems are excluded, and the process is applied recursively (Appendix C algorithm) to carve the universe into non-overlapping complexes.
- Example 1 (information): a deterministic four-unit system had ii_c = ii_e = 4; adding noise to unit D (effect-state probability 0.6 vs opposite 0.4) reduced these to ii_c = ii_e = 1.95; making D's input–output function identical to A (degeneracy) gave ii_c = 1.5, ii_e = 3.
- Example 2 (integration): a symmetric four-unit system with no fault lines had φ_s = 0.3393 (48.1% of intrinsic information); a system with a fault line between {A,B,C} and {D} had φ_s = 0.0628 (10.0%); two strongly connected pairs with a fault line gave φ_s = 0.1477 (21.2%).
- Example 3 (exclusion): an eight-unit universe condensed into three non-overlapping complexes—{F} with φ_s = 0.49, {A,B,C,D,E} with φ_s = 0.12, and {G,H} with φ_s = 0.06; units used sigmoidal activation (Equation 2) with noise levels k = 2 and k = 0.2.

## Critical notes from the literature
- The authors state IIT "must still be considered a work in progress" and that the mathematical formulation has been refined over time; this paper aligns φ_s with recent updates (IIT 4.0) but does not claim a final formulation.
- The examples focus only on φ_s and identifying complexes, not on the resulting Φ-structures (which require the composition postulate to unfold the cause–effect structure); composition is deferred to other work (IIT 4.0 / ref [3]).
- The work restricts consideration to the grain at which the universe is defined; in principle the search for complexes should include systems of units with different spatiotemporal grains, which is left aside "for simplicity."
- The authors note high determinism and low degeneracy are necessary but not sufficient conditions for high φ_s; how environmental constraints facilitate evolution of high φ_s is named as future research.
- Examples are minimalistic small causal models (four to eight units); the paper states future work must investigate more realistic networks before testing IIT's prediction that the maximum of system integrated information in the human brain corresponds to the substrate of consciousness.

## Key topics covered
Integrated information theory (IIT 4.0); system integrated information (φ_s); axioms and postulates of consciousness; intrinsic information (informativeness, selectivity); cause and effect repertoires; do-operator / causal interventions; directional partitions and minimum partition (fault lines); determinism and degeneracy; exclusion and complexes; recursive complex-identification algorithm; principle of maximal/minimal existence; PyPhi computation; sigmoidal threshold units.

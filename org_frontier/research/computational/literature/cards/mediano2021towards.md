---
citekey: mediano2021towards
title: Towards an extended taxonomy of information dynamics via Integrated Information Decomposition
authors: Mediano, Pedro A. M. and Rosas, Fernando E. and Luppi, Andrea I. and Carhart-Harris, Robin L. and Bor, Daniel and Seth, Anil K. and Barrett, Adam B.
year: 2021
doi: 10.48550/arXiv.2109.13186
arxiv: 2109.13186
journal: arXiv preprint
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2109.13186
sha256: 98b0e23fa2dca89fcd8ac73a901c9e09d27561cb51aa8dbd625bfe4291a6270a
pdf_path: literature/pdfs/mediano2021towards.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to characterise and quantify the higher-order dynamical interactions in complex multivariate systems that go beyond simple information transfer and storage, which standard cause-effect ("causal arrow") and one-dimensional complexity metrics fail to capture. The authors combine Partial Information Decomposition (PID) with Integrated Information Theory (IIT) into a new framework they call Integrated Information Decomposition (ΦID), which overcomes PID's limitation of admitting only a single (multivariate) target by decomposing the time-delayed mutual information (TDMI) across multiple sources and multiple targets simultaneously. For a bipartite system of two time series, ΦID yields 16 information atoms (each a pair of forward/backward PID atoms tracking how information evolves from past to future), structured in a lattice and computed via a "double-redundancy" function. From this they build an extended taxonomy of six disjoint information-dynamic phenomena (storage, copy, transfer, erasure, downward causation, upward causation) and show that established measures—transfer entropy (TE), causal density (CD), and various integrated-information measures (Φ)—are aggregates of several distinct ΦID atoms. They demonstrate practical consequences in three settings: a whole-brain Dynamic Mean Field (DMF) simulation, a noisy autoregressive system, and empirical heart-rate/respiration data (Fantasia database), showing for example that whole-minus-sum Φ can go negative because of a negative redundancy-to-redundancy atom, and that the TE effect from breath to heart is driven by a synergistic (Syn→Un) rather than a genuine transfer atom.

## Key facts it relies on
- ΦID decomposes the time-delayed mutual information TDMI = I(X_t; X_{t+1}); for a two-element system this is decomposed by PID into redundant (Red), unique (Un), and synergistic (Syn) "information atoms" (the standard 4-atom bivariate PID lattice from Williams and Beer [21]).
- For a system of two time series, ΦID yields 16 distinct information atoms, each corresponding to a pair of the four original PID atoms evolving from past to future (e.g., Red→Syn, Syn→Un¹), structured in a lattice (Fig. 1c).
- Standard Shannon theory and PID together specify a system of 15 equations for the 16 ΦID atoms, yielding an underdetermined system; one extra constraint—a "double-redundancy" function (a multi-target extension of PID's redundancy)—is needed to compute the atoms.
- Proposition 1 ("15-for-free"): Axioms 1 (compatibility) and 2 (partial ordering) provide unique values for the 16 atoms once one defines a single-target redundancy function Red(·) and an expression for the double-redundancy atom I_∂^{{1}{2}→{1}{2}}.
- The proposed six-mode taxonomy (Fig. 2): Storage (Red→Red, Un¹→Un¹, Un²→Un², Syn→Syn), Copy (Un¹→Red, Un²→Red), Transfer (Un¹→Un², Un²→Un¹), Erasure (Red→Un¹, Red→Un²), Downward causation (Syn→Un¹, Syn→Un², Syn→Red), and Upward causation (Un¹→Syn, Un²→Syn, Red→Syn); upward causation and synergistic storage (Syn→Syn) had not been previously reported.
- For three 2-binary-variable example systems (copy transfer, downward XOR, parity-preserving random) Φ^WMS = 1 for all three, yet ΦID shows each has only one non-zero atom: Un¹→Un² = 1 (copy), Syn→Un¹ = 1 (downward XOR), and Syn→Syn = 1 (PPR) (Fig. 4).
- Transfer entropy TE(1→2) := I(X¹_t; X²_{t+1} | X²_t) decomposes via ΦID as TE(1→2) = Syn→Red + Syn→Un² + Un¹→Red + Un¹→Un² (Eq. 4), of which only Un¹→Un² is the "genuine" transfer term; the atom Syn→Red is counted in both TE(1→2) and TE(2→1), so unnormalised causal density (uCD) double-counts it.
- Φ^WMS = I(X_t; X_{t+1}) − Σ_i I(X^i_t; X^i_{t+1}) (Eq. 3) accounts for all synergies, the unique transferred information, and the negative of the Red→Red atom; this negative double-redundancy term explains why Φ^WMS can go negative in highly redundant systems, motivating a revised measure Φ^R that adds the double-redundancy back.
- Empirical demonstration uses the Fantasia database [56], 40 healthy subjects watching the Disney movie "Fantasia"; following the pipeline of Ref. [53], the TE from breath to heart was significantly higher than heart to breath, and ΦID revealed this effect is dominated by the Syn→Un atom while the genuine transfer atom Un→Un showed no significant difference, with Un→Red showing a significant effect in the opposite direction.
- Whole-brain simulation uses the Dynamic Mean Field (DMF) model [43] with a DTI-based connectome from the Human Connectome Project [51] (Lausanne-83 parcellation); at global coupling G ≈ 2 (a phase transition) Φ^WMS drops below zero while the revised Φ^R strongly increases and peaks, consistent with G = 2 being the optimal fit to awake subjects.
- All numerical examples use a multi-target extension of Ince's Common Change in Surprisal (CCS) redundancy measure [39], with results shown to replicate using a multi-target extension of Barrett's Minimum Mutual Information (MMI) measure [40].

## Critical notes from the literature
- The authors state ΦID does not prescribe a particular functional form for the (double-)redundancy function; multiple double-redundancy functions can be formulated, they may differ across scenarios, and there is "not yet a consensus on one that is universally preferable" — a thorough comparison is left as future work.
- The framework as presented decomposes mutual information between only two time points, which captures all past-to-future information in Markovian systems but "might miss relevant phenomena in systems with non-Markovian dynamics" that typically arise when many variables are unobservable; handling unobserved variables (e.g., via Taken's embedding theorem) is flagged as future work.
- Interpretation of ΦID results depends on how the joint distribution p(X_t, X_{t+1}) is constructed: observational data yields a Granger/predictive reading, while interventional (do()) distributions satisfying faithfulness and causal Markov conditions yield a counterfactual causal (Pearl-sense) reading.
- The paper argues, in line with Feldman and Crutchfield [57], that there are fundamental limitations to any purported all-encompassing scalar measure of dynamical complexity, and that existing integrated-information measures (Φ^WMS, Φ_G, ψ, CD) capture intrinsically different combinations of ΦID atoms rather than approximating a single concept — echoing the prior conclusion of Ref. [19] that such measures differ not only in practice but in principle.
- The choice to analyse pairs of brain regions in the DMF example is noted as "only for convenience," and the physiological implications of the heart/breath findings are deferred to a separate publication.

## Key topics covered
Integrated Information Decomposition (ΦID); Partial Information Decomposition (PID); redundant/unique/synergistic information atoms; time-delayed mutual information (TDMI); double-redundancy function and product lattice; Moebius inversion / lattice atoms; taxonomy of information dynamics (storage, copy, transfer, erasure, upward/downward causation); transfer entropy decomposition; causal density and unnormalised causal density; whole-minus-sum integrated information (Φ^WMS) and revised Φ^R; negative integrated information; active information storage (AIS); Integrated Information Theory (IIT); Dynamic Mean Field whole-brain model; Human Connectome Project / DTI connectome; noisy autoregressive systems; heart rate / respiration coupling (Fantasia database); CCS and MMI redundancy measures.

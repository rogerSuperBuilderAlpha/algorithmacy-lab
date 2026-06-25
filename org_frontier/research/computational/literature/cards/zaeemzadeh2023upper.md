---
citekey: zaeemzadeh2023upper
title: Upper bounds for integrated information
authors: Zaeemzadeh, Alireza and Tononi, Giulio
year: 2023
doi: 10.48550/arXiv.2305.09826
arxiv: 2305.09826
journal: arXiv preprint
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2305.09826
sha256: 66249859c2269f7198020fa7cb4e60fe0f3bc14370d967306328df338b8433c0
pdf_path: literature/pdfs/zaeemzadeh2023upper.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how large the integrated information measures of Integrated Information Theory (IIT) can get, and how those maxima are achieved. Working from the IIT formalism (mechanism integrated information φ for distinctions, and relation integrated information φ_r), the authors derive analytical upper bounds for a single mechanism, for groups of overlapping mechanisms, and for relations among mechanisms, under the working assumption that the system is realizable by a TPM that is a product of unit TPMs (conditional independence). Their first main result (Theorem 1) shows the integrated effect (cause) information of a mechanism M over a purview Z cannot exceed |M||Z|, i.e. the total number of potential causal connections between mechanism and purview; equivalently, mechanism integrated information counts the number of causal connections that must be severed to disintegrate the mechanism. They then prove (Theorem 2, Theorem 3, Corollary 1) that because mechanisms that share parts (are subsets/supersets, or share purview units) cannot simultaneously reach their individual maxima, not all distinctions in a system of more than one unit can be maximally integrated. They introduce constructive TPM designs that maximize integrated information of a chosen subset of distinctions or relations, exploit symmetries to reduce the minimum-information-partition search from exponential to linear (K/2 + 1 partitions) in mechanism size, and verify the bounds numerically using the PyPhi toolbox. The sums of distinction and relation integrated information are shown to grow hyper-exponentially with the number of units N.

## Key facts it relies on
- Theorem 1: for a mechanism M in state m, candidate cause purview C and candidate effect purview E, φ_e(m,E) ≤ |M||E| and φ_c(m,C) ≤ |M||C|; this bound is achievable, and to disintegrate a maximally integrated mechanism all causal connections between the mechanism and the purview must be severed.
- Lemma 2 bounds the (positive part of the) log-ratio of unpartitioned to partitioned effect repertoire by N(θ), the total number of connections cut by partition θ; mechanism integrated information thus counts the causal connections that must be severed to split the mechanism into causally independent parts.
- The sum of distinction integrated information over all mechanisms is bounded by Σ_{M⊆S} φ(m) ≤ Σ |M| N = (N²/2) 2^N (Eq. 6); over unique purviews the bound is N(N+1)/4 · 2^N (Eq. 7). Each bound has a quadratic term (connections grow quadratically) and an exponential term (number of subsets grows exponentially) in N.
- Lemma 4: achieving φ_e(m,Z) = |M||Z| requires selectivity π_e(Z=z|m) = 1; high selectivity (close to 1) is necessary for large integrated information, and selectivity of 1 requires TPM entries to be 0 or 1 (Lemma 7 / Lemma 3 on deterministic mechanisms).
- Theorem 2 / Corollary 1: any subset or superset of M that shares purview units with M cannot also reach the maximum if φ_e(m,Z)=|M||Z|; consequently all distinctions in a system composed of more than one unit cannot all be maximally integrated.
- Theorem 3: in a system of N units, for a mechanism size 1 < K < N where all size-K mechanisms specify themselves with probability 1 (Z=M), none of those mechanisms can achieve the maximum |M||Z| = |M|² of integrated effect information (exceptions only at K=N or K=1).
- The minimum information partition (MIP) for the special grid-like / reflexive system can be found by evaluating only K/2 + 1 partitions (proved in S3 Appendix), reducing MIP search from more-than-exponential to linear in mechanism size, making computation feasible in larger networks.
- A system of N units can contain as many as 2^N − 1 distinctions and 2^(2^N − 1) − 1 causal relations; the derived bound on Σ φ_r(d) grows as O(N² 2^(2^N)) (Eq. 16), i.e. hyper-exponentially.
- Numerical experiments were performed with the freely available PyPhi toolbox; for system size N = 12 the maximum (N choose K) φ_e*(K) is achieved at K = 7, illustrating the trade-off between achievable φ_e per mechanism and the number of mechanisms.
- Tested TPM constructions include High selectivity (the Theorem-3 construction, 0/1 entries), Random deterministic, Random, and Hamming (decoding of the (7,4) Hamming code, suggested by Tegmark [15] as a candidate high-integration system); deterministic TPMs achieve higher sums of integrated information than nondeterministic ones.

## Critical notes from the literature
- The authors state their results are state-dependent: a system or mechanism optimal in one state is not necessarily optimal in others, and finding conditions for high integrated information across more than one state is left open.
- The working assumption is conditional independence (TPM as a product of unit TPMs) and binary units; the authors say results generalize to non-binary units and that S2 Appendix shows robustness to other difference measures (point-wise mutual information, KL divergence), but the core derivations are made under these assumptions.
- The authors note exact calculation of Φ for realistic systems is not feasible (difficulty of obtaining a TPM at the right grain, nested combinatorial explosions over unit grains, candidate complexes, distinctions and relations), which motivates the bounds as a step toward approximations/heuristics rather than exact values.
- Several bounds are explicitly stated to be not tight or not achievable: Bounds I and II (Eqs. 6, 7) are labeled "not achievable" because inter- and intra-order constraints prevent all distinctions from reaching their maxima; the authors note the numerical Bound III (Σ_K (N choose K) φ_e*(K)) "might be a general upper bound for any system" but "the generality of this upper bound remains to be investigated."
- Deriving a tighter general closed-form bound for S(o) (and hence for Σ φ_r(d)), and finding closed-form bounds for arbitrary subsets of distinctions, are stated as open problems.

## Key topics covered
Integrated Information Theory (IIT 4.0); mechanism integrated information (φ, φ_e, φ_c); causal distinctions and relations; upper bounds on integrated information; cause/effect repertoires and causal marginalization; minimum information partition (MIP) and number of connections cut; selectivity vs informativeness decomposition; inter-order and intra-order constraints among overlapping mechanisms; deterministic TPMs and 0/1 entries; constructive TPM design to maximize integrated information; symmetry exploitation to reduce MIP search to linear time; hyper-exponential growth of distinction and relation sums in N; numerical validation with PyPhi; Hamming (7,4) code, random, and high-selectivity TPM constructions; implications for connectivity profiles (grid-like vs random), the brain, and panpsychism.

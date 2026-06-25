---
citekey: zaeemzadeh2024upperbounds
title: Upper Bounds for Integrated Information
authors: Zaeemzadeh, Alireza and Tononi, Giulio
year: 2024
doi: 10.1371/journal.pcbi.1012323
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: plos-template
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pcbi.1012323&type=printable
sha256: f3a8af380eca898308e553d6dd39e7f7781def62175ee9427ff98ac6a71a1a0b
pdf_path: literature/pdfs/zaeemzadeh2024upperbounds.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Within Integrated Information Theory (IIT 4.0), the paper studies the upper bounds on integrated information measures and the conditions under which those bounds can be achieved. It asks how large the mechanism integrated information (φ) of a single distinction can get, why the distinctions of a system cannot all simultaneously reach their maxima, and how the integrated information of causal relations is bounded. The central method connects integrated information to the number of causal connections that must be severed to disintegrate a mechanism-purview pair, derived through a chain of lemmas about causal marginalization and informativeness. The main results are: a single distinction's integrated cause/effect information is bounded by the product of mechanism and purview sizes (Theorem 1, φ_e(m,E) ≤ |M||E|); mechanisms that share parts cannot all reach their maximum simultaneously (Theorem 2, inter-order constraints), so the sum bounds in Eqs (6) and (7) are not achievable; and even mechanisms of the same size with full self-selectivity cannot all maximize their integrated information (Theorem 3, intra-order constraints). The authors also derive a linear-programming-based bound for the sum of relations' integrated information, give a linear-time numerical bound for "reflexive" systems, and validate the bounds numerically with the PyPhi toolbox, finding densely connected grid-like and deterministic systems achieve the highest values.

## Key facts it relies on
- Theorem 1: for a mechanism M in state m, a candidate cause purview C, and a candidate effect purview E, φ_e(m,E) ≤ |M||E| and φ_c(m,C) ≤ |M||C|, where |E|, |C| are purview sizes; this bound is achievable and equals the total number of causal connections between mechanism and purview.
- Lemma 2 establishes that the informativeness term |log_2(π_z(Z=z|m)/π_z^θ(Z=z|m))|_+ is bounded above by N(θ), the total number of connections cut by partition θ; Lemma 1 is the single-unit special case bounding it by |M|−|M̄|.
- The sum of integrated information over all subsets (mechanisms) of a system is bounded by Σφ(m) ≤ Σ|M|N = N Σ_{|M|=1}^N |M| (N choose |M|) = (N²/2)2^N (Eq 6); over unique purviews the bound is N(N+1)/4 · 2^N (Eq 7).
- Theorem 2 (inter-order constraints): if φ_e(m,Z)=|M||Z| for one mechanism-purview pair, then any subset (M̄⊂M) or superset (M̄⊃M) of M that shares purview units with M (Z∩Z̄≠∅) satisfies φ_e(m̄,Z̄) < |M̄||Z̄|, so the bounds in Eqs (6) and (7) are not achievable. Corollary 1: all distinctions in a system cannot be maximally integrated if the system has more than one unit.
- Lemma 4: φ_e(m,Z)=|M||Z| only if the selectivity term π_e(Z=z|m)=1; achieving the maximum requires selectivity of 1.
- Theorem 3 (intra-order constraints): in a system of N units, for a fixed mechanism size 1 < K < N where all size-K mechanisms fully specify themselves (π_e(Z=z'|m)=1, Z=M), none can achieve its maximum integrated effect information |M||Z|=|M|² (exceptions are K=N, single such mechanism, or K=1).
- The system can have as many as 2^(2^(N−1)) − 1 causal relations; the maximum number of relations is 2^(2^(N−1))−1 and the maximum value for distinction integrated information is N², giving Σφ_r(d) a growth rate of O(N²2^(2^N)) (Eq 16).
- For a self-relation (|d|=1), φ_r(d) = |z_c*∩z_e*| · φ_d/|z_c*∪z_e*| (Eq 9); the relation integrated information of any subset of distinctions cannot exceed the smallest distinction's integrated information, φ_r(d) ≤ min φ_d.
- The MIP for the reflexive/self-specifying system can be found by evaluating only K/2 + 1 partitions, reducing computation from exponential to quadratic in N (linear-time numerical bound).
- Numerical experiments use the PyPhi toolbox [14]; Fig 1B shows that for N=12 the maximum (N choose K)φ_e*(K) is achieved at K=7; Bound III (the Section 2.1.3 numerical bound) grows as O(2^N) and is shown tight for the proposed construction.

## Critical notes from the literature
- The authors state that exact computation of Φ for realistic systems is not feasible due to difficulty of obtaining a TPM at the right grain and combinatorial explosions; bounds and heuristics are needed as in statistical physics and quantum mechanics, and this work is explicitly framed as a first step toward "well-grounded estimates."
- Bounds I and II (Eqs 6, 7) are explicitly labeled "not achievable" because of inter- and intra-order constraints; the achievable maximum is strictly below these absolute bounds.
- Results are state-dependent: the bounds and optimal TPM constructions hold only for a specific state, and a system optimal in one state is not necessarily optimal in others (acknowledged open problem).
- Whether the linear-time numerical bound (Bound III) is a general upper bound for any system, not just the high-selectivity regime, "remains to be investigated"; finding a closed-form bound for S(o) / arbitrary distinction subsets remains an open problem.
- The working assumption is a TPM that is a product of unit TPMs (conditional independence, no instantaneous causation) and binary units; derivations focus on integrated effect information, with results shown applicable to cause information in S1 Appendix and to other difference measures (KL divergence, pointwise mutual information) in S2 Appendix.

## Key topics covered
Integrated Information Theory (IIT 4.0); mechanism integrated information (φ); integrated cause/effect information (φ_c, φ_e); causal distinctions and relations; purviews and cause-effect repertoires; causal marginalization; minimum information partition (MIP); upper bounds and achievability conditions; inter-order and intra-order constraints; selectivity vs informativeness decomposition; transition probability matrix (TPM) construction; linear programming bound for relations; PyPhi numerical experiments; grid-like / densely connected / deterministic connectivity profiles; Hamming-code candidate systems; computational complexity reduction.

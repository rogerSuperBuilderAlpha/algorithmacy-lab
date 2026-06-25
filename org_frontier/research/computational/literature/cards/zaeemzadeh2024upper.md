---
citekey: zaeemzadeh2024upper
title: Upper bounds for integrated information
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
pdf_path: literature/pdfs/zaeemzadeh2024upper.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Within the IIT 4.0 framework, this paper asks how large the integrated information of mechanisms (distinctions) and of causal relations among them can possibly be, and under what conditions the maximum is achievable. The authors derive analytic upper bounds for mechanism integrated information φ, showing it is bounded by the number of causal connections between a mechanism and its purview, and prove that mechanisms sharing parts cannot all simultaneously reach their individual maxima. They establish bounds on the sum of distinctions' integrated information (quadratic times exponential in N) and on the sum of relations' integrated information (which can grow hyper-exponentially, on the order of O(N²·2^(2^N))). A central result is that intrinsic integrated information is fundamentally different from Shannon information, which for N binary units is at most N. The paper also provides constructive TPM designs that maximize integrated information for special classes of systems, and uses symmetries to reduce partition searches from exponential to linear in mechanism size. Numerical experiments with the PyPhi toolbox illustrate that the bounds are tight for the proposed constructions and that deterministic TPMs outperform nondeterministic ones.

## Key facts it relies on
- The work is built on the IIT 4.0 formalism of Albantakis et al. (ref [1], PLOS Comput Biol 2023) and the intrinsic-information difference measure of Barbosa et al. (refs [11], [12]); mechanism integrated information is φ(m) = min{φ_c(m), φ_e(m)}.
- Theorem 1: for a mechanism M in state m, candidate cause purview C, and candidate effect purview E, φ_e(m, E) ≤ |M||E| and φ_c(m, C) ≤ |M||C|; the bound equals the total number of causal connections between mechanism and purview, and is achievable.
- The sum of distinctions' integrated information is bounded by Σ φ(m) ≤ (N²/2)·2^N (Eq 6), and over unique purviews by Σ φ(m) ≤ (N(N+1)/4)·2^N (Eq 7); both consist of a quadratic term times an exponential term.
- Lemma 1 / Lemma 2: the informativeness term |log₂(π_e(Z|m)/π_e^θ(Z|m))|₊ is bounded by the number of causal connections cut — by |M| − |M̄| for nested mechanisms (Lemma 1) and by N(θ), the total number of connections cut by partition θ (Lemma 2).
- Theorem 2: any subset or superset of M that shares purview units with M cannot achieve its maximum if φ_e(m,Z) = |M||Z|; Corollary 1 states all distinctions in a system cannot be maximally integrated if the system has more than one unit.
- Theorem 3 (intra-order constraint): in a system of N units, for mechanism size 1 < K < N, if all mechanisms of size K fully specify themselves with selectivity 1 (Z = M), none can achieve their maximum integrated effect information |M||Z| = |M|²; the proof is constructive (yields a TPM).
- A system of N units can contain up to 2^(2^(N−1)) − 1 causal relations; the sum of relations' integrated information has growth rate O(N²·2^(2^N)) (Eq 16), and maximum distinction integrated information is N².
- Intrinsic integrated information differs fundamentally from Shannon information, which for a system of N binary units is at most N.
- The MIP search can be reduced to evaluating only K/2 + 1 partitions, making the computational complexity of the reflexive-system numerical bound quadratic in N (reduced from more than exponential to linear in mechanism size).
- Numerical experiments used the PyPhi toolbox (ref [14]); for system size N = 12, the maximum (N choose K)·φ_e*(K) is achieved at K = 7; deterministic (0/1) TPMs outperform nondeterministic TPMs, and a Hamming (7,4) decoding TPM was tested as a candidate high-Φ system.

## Critical notes from the literature
- The authors state the bounds in Eqs (6) and (7) (Bound I and Bound II) are "not achievable" because of inter-order and intra-order constraints; achieving φ_e = |M||z_e| for all distinctions simultaneously is impossible, so Eq (16) is "not tight."
- Results are explicitly state-dependent: bounds and optimal TPM constructions hold only in one state of the system/mechanism; finding conditions for high integrated information across multiple states is left open.
- The derivations mainly focus on integrated effect information (a bound for φ_e bounds φ_d); the authors note results extend to cause information (S1 Appendix) but that cause-effect dependencies could potentially tighten the bounds further.
- The working assumption is that systems are realizable by a TPM that is a product of unit TPMs (conditional independence, no instantaneous causation), and the analysis treats binary units (stated to generalize to non-binary).
- Whether the numerical reflexive-system upper bound (Σ (N choose K)·φ_e*(K), Section 2.1.3) is a general upper bound for any system, not just the high-selectivity regime, remains conjectural / to be investigated; deriving a tighter general closed-form bound for S(o) is an open problem.

## Key topics covered
Integrated Information Theory (IIT 4.0); mechanism integrated information (φ); cause/effect repertoires; causal marginalization; purviews and minimum information partition (MIP); causal distinctions and relations; cause-effect structure; upper bounds on φ; inter-order and intra-order constraints; selectivity vs informativeness; transition probability matrix (TPM) construction; computational reduction via symmetries; Shannon vs intrinsic information; growth rates of Φ with system size; PyPhi numerical experiments; deterministic vs random TPMs; Hamming code TPM.

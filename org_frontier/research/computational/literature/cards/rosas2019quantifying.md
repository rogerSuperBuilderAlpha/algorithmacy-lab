---
citekey: rosas2019quantifying
title: Quantifying high-order interdependencies via multivariate extensions of the mutual information
authors: Rosas, Fernando E. and Mediano, Pedro A. M. and Gastpar, Michael and Jensen, Henrik J.
year: 2019
doi: 10.1103/physreve.100.032305
arxiv: null
journal: Physical Review E
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1902.11239
sha256: 592364820feb12e94ff87d32ac8c09a751f445d6bf26653f340985919f6cc91d
pdf_path: literature/pdfs/rosas2019quantifying.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to quantify high-order interdependencies (statistical synergy vs. redundancy) in multivariate systems in a model-agnostic, symmetric way, without splitting variables into predictors and targets. It builds on a decomposition of the total information storable in a system into collective constraints (total correlation, C) and shared randomness (binding entropy / dual total correlation, B), and defines the O-information as their difference, Ω(X^n) = C(X^n) − B(X^n). Ω(X^n) > 0 marks redundancy-dominated systems and Ω(X^n) < 0 marks synergy-dominated systems; it equals the interaction (co-)information for n=3 but provides a more meaningful extension for larger n, and its computational cost scales gracefully with system size. The authors prove Ω is permutation-invariant, vanishes for two variables, is maximised by the n-bit copy (Ω = n−2) and minimised by the n-bit xor (Ω = 2−n), can be decomposed as a sum of triple interaction-information terms via partition-lattice "assembly paths," and imposes scale-dependent bounds on subsystem correlations. They show the TSE (Tononi–Sporns–Edelman) complexity tracks C+B (correlation above 0.97) rather than synergy, so TSE and Ω are complementary. As a proof of concept they analyse four-voice Baroque scores and find Bach's chorales are synergy-dominated while Corelli's pieces are redundancy-dominated.

## Key facts it relies on
- The O-information is defined as Ω(X^n) := C(X^n) − B(X^n) = (n−2)H(X^n) + Σ_j [H(X_j) − H(X^n_{−j})], where C is the total correlation (multi-information) and B is the binding entropy (dual total correlation / excess entropy); it was originally introduced as "enigmatic information" by James et al. (Ref. [27]).
- Lemma 1: Ω is independent of variable order (A); Ω(X_1,X_2)=0 for any p (B); Ω(X_1,X_2,X_3)=I(X_1;X_2;X_3), the interaction information, for n=3 (C); for n>3, Ω generally differs from the full interaction information I(X_1;…;X_n).
- For n=3, redundancy dominates when I(X_1;X_2;X_3) ≥ 0 (e.g. X_1=X_2=X_3 a fair coin gives I=1) and synergy dominates when ≤ 0 (e.g. xor gate Y_3=Y_1+Y_2 mod 2 gives I=−1); for n≥4 the co-information no longer reflects the redundancy/synergy balance.
- Proposition 2: for a binary vector with n≥3, Ω(X^n)=n−2 iff X^n is an "n-bit copy" (all equal to a fair coin), and Ω(X^n)=2−n iff X^n is an "n-bit xor" (n−1 i.i.d. fair coins, X_n = sum mod 2). Corollary 2 generalises to alphabet size m: Ω = (n−2)log m and (2−n)log m respectively.
- Lemma 3 (tight bounds): (n−1)log|X| ≥ C(X^n) ≥ 0; (n−1)log|X| ≥ B(X^n) ≥ 0; n log|X| ≥ C+B ≥ 0; (n−2)log|X| ≥ Ω(X^n) ≥ (2−n)log|X|.
- Proposition 1 / Corollary 1: Ω can be written as a sum of triple interaction-information terms along any partition-lattice "assembly path"; e.g. Ω(X^n) = Σ_{k=2}^{n−1} I(X_k; X^{k−1}; X^n_{k+1}); the decompositions are valid for any relabelling of variables, but the partition lattice grows super-exponentially with n.
- TSE complexity: the authors show TSE(X^n) ∝ C(X^n)+B(X^n); Monte Carlo over distributions sampled uniformly from the probability simplex gives correlation consistently above 0.97, outperforming other proposed TSE approximations, and TSE assigns equal values to a 3-bit copy and a 3-bit xor (conflating redundancy and synergy). Hence Ω = C−B and TSE ∝ C+B are complementary.
- Statistical-mechanics test: for ensembles of n=5 spins with random Hamiltonians (couplings J_γ i.i.d. standard normal, β=0.1), Ω is near zero for max interaction order k=2 and becomes negative (more synergistic) as k grows.
- Music case study: four-voice scores (J. S. Bach chorales, ~4×10^4 four-note chords; Corelli Op. 1, 3–6, ~8×10^4 chords), with each voice a time series of 13 values (notes plus silence), computed in "muts" (log base 13). Bach's chorales have negative Ω with all local ω_ij negative (synergy-dominated); Corelli's pieces have positive Ω with all local ω_ij positive except between the two violins, strongest redundancy between viola and cello (ω_ij = 0.17), attributed to a shared basso continuo bass line.

## Critical notes from the literature
- The authors note Ω = 0 is ambiguous: it can arise either from a system with only disjoint pairwise interactions or from "destructive interference" where redundant (Ω>0) and synergistic (Ω<0) subsystems cancel; redundancy and synergy can coexist within the same variables, which Ω alone cannot disentangle (resolving this may require inspecting C, B, or subsystem O-information).
- Ω is a net/aggregate balance measure: it does not provide the fine-grained per-source decomposition of partial information decomposition (PID); the paper positions Ω as an alternative to PID, motivated partly by PID's lack of agreement on how to compute its terms and its super-exponential growth in terms for large systems.
- The lattice decompositions rely on the partition lattice P_n, which grows super-exponentially with system size, so heuristic exploration (e.g. assembly paths) is needed; the authors emphasise that Ω itself (a linear combination of Shannon entropies) is computationally cheap, but the full lattice machinery is not.
- The music analysis is framed explicitly as a "proof of concept"/brief demonstration restricted to harmony/chords (melodic properties left to future work); joint distributions are estimated by empirical frequencies, with standard errors via circular block-bootstrap reported as below the least significant figure shown.
- The framework as presented is for discrete variables; the authors state generalisation to continuous variables and application to neural data will appear in a separate publication.

## Key topics covered
- O-information (Ω); statistical synergy vs. redundancy; high-order interdependencies / emergence
- Total correlation (multi-information) C; binding entropy / dual total correlation / excess entropy B; negentropy
- Interaction information / co-information; multivariate extensions of mutual information
- Partition lattice, assembly paths, lattice information decompositions
- TSE (Tononi–Sporns–Edelman) complexity; integration vs. segregation
- High-order Hamiltonians / maximum-entropy spin models; partial information decomposition (PID)
- Baroque music score analysis (Bach chorales, Corelli); muts; local O-information ω_ij

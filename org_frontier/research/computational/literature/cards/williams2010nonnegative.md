---
citekey: williams2010nonnegative
title: Nonnegative Decomposition of Multivariate Information
authors: Williams, Paul L. and Beer, Randall D.
year: 2010
doi: null
arxiv: 1004.2515
journal: arXiv
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/1004.2515
sha256: 5654e8083b45f1c4fc92669996f647712322a3563a56252dbeb1d0ec46b24678
pdf_path: literature/pdfs/williams2010nonnegative.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to characterize the structure of information that a set of source variables R = {R1, ..., R_{n-1}} provides about a target variable S, arguing that the standard generalization of mutual information, interaction information (McGill), is inadequate because it can be negative and lacks a clear interpretation. From first principles the authors introduce a new measure of redundancy, I_min, defined as the expected value (over outcomes of S) of the minimum specific information that any source provides about each outcome. They show I_min induces a partial order ("redundancy lattice") over collections of sources, and use the Mobius inverse of I_min on this lattice to define a partial information (PI) function whose values, the "partial information atoms," exhaustively decompose mutual information into nonnegative components corresponding to unique, redundant, and synergistic contributions. The decomposition is always nonnegative and interpretable, unlike interaction information. They further demonstrate that the negativity of interaction information arises because it conflates (confounds) redundancy and synergy, with a negative value indicating net redundancy and a positive value indicating net synergy in the 3-variable case.

## Key facts it relies on
- The two main prior generalizations of information theory to multiple variables are total correlation (Watanabe, also multiinformation/integration) and interaction information of McGill (also called multiple mutual information, co-information, synergy); total correlation gives a single monolithic quantity and says nothing about the structure of multivariate information.
- Redundancy is defined as I_min(S; {A1,...,Ak}) = sum_s p(s) min_{Ai} I(S=s; Ai), the expected value over outcomes of S of the minimum specific information any source provides about that outcome (Eq. 3); the specific information used is I(S=s; A) = sum_a p(a|s)[log(1/p(s)) - log(1/p(s|a))] (Eq. 2).
- I_min is nonnegative (following from nonnegativity of specific information), is bounded above by the information each source provides (with equality iff all sources provide identical information about S), and is maximized by the self-redundancy I_min(S;{A}) = I(S;A).
- The ordering relation alpha <= beta on collections of sources holds iff for all B in beta there exists A in alpha with A a subset of B; this produces the redundancy lattice (Eq. 5), whose nodes are the antichains A(R), the set of collections where no source is a superset of another (Eq. 4).
- The partial information function Pi_R is the Mobius inverse of I_min on the lattice: I_min(S; alpha) = sum_{beta <= alpha} Pi_R(S; beta) (Eq. 6); mutual information decomposes as a sum of PI-terms, I(S;A) = I_min(S;{A}) = sum_{beta <= {A}} Pi_R(S; beta) (Eq. 9).
- For 3 variables R = {R1, R2}, the four PI-atoms are unique information Pi_R(S;{1}) and Pi_R(S;{2}), redundancy Pi_R(S;{1}{2}), and synergy Pi_R(S;{12}); a canonical synergy example is XOR, S = R1 XOR R2, where R1 and R2 individually provide no information but jointly provide complete information.
- In the worked example (Fig. 4A), R1 and R2 each provide 1/3 bits of unique information (Pi_R(S;{1}) = Pi_R(S;{2}) = 1/3), redundancy is Pi_R(S;{1}{2}) = log 3 - log 2, and synergy is Pi_R(S;{12}) = 1/3 bits.
- Interaction information for 3 variables equals synergy minus redundancy: I(S;R1;R2) = Pi_R(S;{12}) - Pi_R(S;{1}{2}) (Eq. 14), so a negative interaction information indicates net redundancy and a positive value indicates net synergy; partial information, unlike mutual or interaction information, is not symmetric.
- The number of PI-atoms equals the cardinality of A(R), which is the (n-1)-th Dedekind number; for 9 variables there are more than 5 x 10^22 possibilities, and beyond that the Dedekind numbers are not currently known.

## Critical notes from the literature
- The paper itself notes the decomposition's chief practical limitation: the number of partial information terms grows extremely rapidly (Dedekind numbers), making computation for large systems intractable, and 3-variable interaction is described as "the current state of the art."
- The authors show interaction information is unreliable as a synergy/redundancy diagnostic: for 4-variable interaction information, a completely redundant system (R1, R2, R3 all copies of S) is assigned +1 bit, the same value as a purely synergistic 3-parity system, so 4-variable interaction information fails to distinguish purely synergistic from purely redundant cases.
- Even in the 3-variable case interaction information can equal zero when redundancy and synergy are balanced (Fig. 4B example: 1/2 bits redundancy and 1/2 bits synergy cancel), masking the presence of both.
- The authors acknowledge that mixed redundancy/synergy makes interaction information ambiguous to interpret (citing prior work that suggested mixed redundancy and synergy is possible without attempting to disentangle them).

## Key topics covered
Partial information decomposition (PID); redundancy measure I_min; specific information; redundancy lattice / antichains; Mobius inversion; partial information atoms (unique, redundant, synergistic); PI-diagrams; interaction information / co-information / multiple mutual information; negativity of interaction information; total correlation / multiinformation; synergy and redundancy in neural coding; XOR and 3-parity examples; Dedekind numbers.

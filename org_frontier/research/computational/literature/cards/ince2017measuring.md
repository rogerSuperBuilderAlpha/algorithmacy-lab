---
citekey: ince2017measuring
title: Measuring Multivariate Redundant Information with Pointwise Common Change in Surprisal
authors: Ince, Robin
year: 2017
doi: 10.3390/e19070318
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1602.05063
sha256: 2fb512f06e065a201ac94459a49a06fe480c0d3b304acb8ab2bab1df7e6e9ad4
pdf_path: literature/pdfs/ince2017measuring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses an open problem in information theory: how to properly quantify redundant information, i.e. the information about a target variable S that is common to two or more predictor variables X_i, for use within the Partial Information Decomposition (PID) of Williams and Beer (2010). Ince proposes I_ccs, a new redundancy measure that quantifies the common change in surprisal shared between sources at the local (pointwise) level, exploiting the additivity of surprisal to compute set-theoretic overlap via local co-information, but counting only those local terms whose signs are all equal (so they unambiguously represent redundant information or redundant misinformation). To fix the joint distribution needed for the pointwise computation, he gives a game-theoretic operational definition of unique information that extends the decision-theoretic argument of Bertschinger et al. (2014), and uses the maximum-entropy distribution subject to source-target and full predictor-marginal constraints. He shows via a counter-example (REDUCEDOR) that unique information is not invariant to the predictor-predictor marginal, so the existing I_broja measure can overstate redundancy by coupling predictors. I_ccs satisfies symmetry, self-redundancy, subset equality, and a modified ("independent") identity property, but not monotonicity, so the resulting PID can have negative atoms, which Ince argues are a necessary consequence of genuinely measuring overlapping information content. The measure is validated against many literature example systems (logical gates, RDNXOR, RDNUNQXOR, XORCOPY, DBLXOR) and extended to continuous Gaussian variables, with accompanying Matlab code.

## Key facts it relies on
- I_ccs is built on co-information (interaction information), the alternating-sum quantity I(V) = -sum_{T subset X} (-1)^|T| I(T;S) that measures the intersection of mutual informations but conflates synergy and redundancy; for odd numbers of variables co-information has opposite sign to interaction information, with positive values indicating net redundant overlap.
- The pointwise rule (Table 3): a local co-information term is counted as redundant only when all individual local changes in surprisal, the joint change in surprisal, and the local co-information share the same sign; otherwise the contribution is set to zero (Definition 4.1).
- The joint distribution P-hat used for the pointwise terms is the maximum-entropy distribution subject to equal bivariate source-target marginals Q(A_i,S)=P(A_i,S) and equal n-variate predictor joint marginal Q(A_1,...,A_n)=P(A_1,...,A_n) (Definition 4.2); for two predictors maximizing entropy and maximizing co-information under these constraints coincide.
- Worked SUM example (S = X1 + X2, four outcomes each p=1/4): I_ccs(S;{1}{2}) = 0 although the co-information is -0.5 bits; the x1 != x2 terms are purely synergistic (-1 bit local co-information each) and excluded.
- REDUCEDOR counter-example: I_broja reports zero unique information (its optimization couples the predictors, P(X1=0,X2=1)=P(X1=1,X2=0)=0), whereas I_ccs reports zero redundancy and 0.31 bits of unique information in each predictor; both distributions share the same target-predictor marginals but differ in P(X1,X2).
- For AND/OR, I_min and I_broja agree (0.31 redundancy, 0 unique, 0.5 synergy) while I_ccs gives 0.10 redundancy, 0.21 unique each, 0.29 synergy; the I_broja optimized AND distribution has entropy 1.5 bits versus 2 bits for the original distribution used by I_ccs.
- RDNUNQXOR (two 3-bit predictors, one 4-bit target) is constructed to contain exactly 1 bit each of redundant, two unique, and synergistic information; I_ccs and I_broja recover the PID (1,1,1,1) but I_min does not.
- I_ccs satisfies symmetry, self-redundancy, subset equality, and the modified independent identity property (I(A1;A2)=0 => I_ccs([A1,A2];A1,A2)=0), but does not satisfy the Harder et al. identity axiom nor monotonicity; the example in Table 7 gives I_ccs(S;{1}{2}) = 0.77 bits > I(S;X2) = 0.61 bits, violating monotonicity and yielding a negative unique atom I_partial({2}) = -0.16.
- For three-variable XOR-structured systems (DBLXOR, XORCOPY), I_ccs produces negative atoms (e.g. I_partial({12}{13}{23}) = -1 bit) that Ince interprets as "mechanistic redundancy" between synergistic pairs; the four-variable redundancy lattice has 166 nodes.
- For continuous Gaussian systems, Barrett (2015) showed all prior redundancy measures agree and equal I_mmi = min_i I(S;X_i); I_ccs instead varies with the predictor-predictor correlation b, moving from purely unique (negative correlation) to purely redundant (strong positive correlation).

## Critical notes from the literature
- The PID built on I_ccs is not non-negative: the author acknowledges that "negative atoms can subjectively be seen as a flaw" (quoting James and Crutchfield 2016) and that monotonicity, long considered a crucial PID axiom, fails for this measure; he argues negativity is unavoidable for any measure genuinely quantifying overlapping content, citing Rauh (2017)'s secret-sharing result that a meaningful redundancy measure cannot yield a non-negative PID.
- Continuity of I_ccs is only conjectured, not proven: the required local inequality (Eq. 42) does not hold for all joint distributions, only (conjecturally) for the pairwise maximum-entropy solution; the Matlab implementation explicitly tests for violations, which did not occur in the examples considered.
- The choice of joint distribution rests on a contested operational stance: I_ccs rejects the decision-theoretic invariance assumption ("Assumption *") of Bertschinger, Rauh, Olbrich, Jost and Ay (2014) underlying I_broja, replacing it with a game-theoretic definition; readers who prefer the decision-theoretic view can instead use P-hat_ind (Definition 4.3), giving a different measure.
- Practical limitations flagged by the author: limited-sampling bias and statistical inference (permutation schemes) for PID estimation from experimental data remain open, and interpretation of the lattice becomes hard beyond three variables (the four-variable lattice has 166 nodes).
- I_broja is defined only for two input sources, so the three-variable examples cannot compare against it; Harder et al. (2013)'s measure is likewise limited to two sources.

## Key topics covered
- Partial Information Decomposition (PID) and the redundancy lattice / antichains
- Redundant, unique, and synergistic information; co-information / interaction information / multiple mutual information
- Pointwise (local) information measures and change in surprisal; misinformation
- I_ccs (common change in surprisal) redundancy measure; sign-matching rule (Table 3)
- Maximum-entropy joint distribution under marginal constraints
- Game-theoretic vs decision-theoretic operational definition of unique information
- Comparison measures: I_min (Williams and Beer), I_broja (Bertschinger/Griffith-Koch), I_mmi (Gaussian)
- Redundancy axioms: symmetry, self-redundancy, subset equality, monotonicity, identity property
- Example systems: RDN, SUM, AND/OR, XOR, RDNXOR, RDNUNQXOR, REDUCEDOR, XORCOPY, DBLXOR, ANDDUPLICATE, giant bit, parity
- Continuous Gaussian PID; Gaussian copula estimation
- Negative PID atoms; mechanistic redundancy; partial entropy decomposition; secret-sharing connection

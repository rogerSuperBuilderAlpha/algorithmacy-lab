---
citekey: amblard2012relation
title: The Relation between Granger Causality and Directed Information Theory: A Review
authors: Amblard, Pierre-Olivier and Michel, Olivier J. J.
year: 2012
doi: 10.3390/e15010113
arxiv: null
journal: Entropy
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1211.3169
sha256: af530f33794a10984b98f03c4d6d22bf5a20de6546fd1e53000862b02e498fd3
pdf_path: literature/pdfs/amblard2012relation.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This review surveys the conceptual and theoretical links between Granger causality (a framework, originating in econometrics from Wiener's prediction idea, for assessing directional dependence between time series) and directed information theory. The authors recall the prediction-based definitions of Granger causality and then the stronger conditional-independence definitions, incorporate instantaneous coupling, and discuss Granger causality graphs. They argue that Kramer's "causal conditioning" is the cornerstone linking the two fields: in the bivariate case the directed information decomposes as the sum of the transfer entropy (the strictly causal, past-to-present part) and a term quantifying instantaneous coupling (the instantaneous information exchange). They show how mutual information decomposes into directed information flowing in both directions plus the instantaneous coupling term, generalizing Geweke's Gaussian-case result to the non-Gaussian case. In the multivariate case, side information requires causal conditioning, and the clean decomposition is "blurred" by an extra instantaneous-coupling term reflecting intrinsic versus extrinsic coupling. Finally, the directed-information measures are shown to emerge naturally from hypothesis-testing and prediction-based inference frameworks for Granger causality.

## Key facts it relies on
- The intellectual lineage: Norbert Wiener's 1956 prediction paper proposed that a signal x causes y if the past of x improves prediction of y; this inspired Clive Granger; symmetry-breaking of information theory for directional dependence was realized by Hans Marko (bidirectional information theory in the Markov case, 1960s–70s) and generalized by James Massey (1990) and Gerhard Kramer to "directed information theory."
- Prediction-based Definition 1: x_A Granger does not cause x_B relative to V iff the optimal prediction risk R_F(B(n+1)|V^n) = R_F(B(n+1)|(V/A)^n); this depends on the cost g and the function class F. A counterexample (x_{n+1}=αx_n+βy_n^2+ε_{n+1}) shows that with quadratic loss and linear functions one wrongly concludes y does not cause x, though it does so nonlinearly.
- Conditional-independence Definition 2: x_A does not Granger cause x_B relative to V iff x_B(n+1) ⊥ x_A^n | x_B^n, x_C^n for all n; this is more general than Definition 1 and is cost/function-class free, but lacks operational tools.
- Two distinct definitions of instantaneous coupling arise with side information C: Definition 3 (conditional, conditioning on x_C^{n+1}) versus Definition 4 (conditioning on x_C^n only, a bivariate-style coupling); they differ analogously to correlation versus partial correlation.
- Kramer's causal conditional probability: p(x_B^n ‖ x_A^n) := ∏_{i=1}^n p(x_B(i) | x_B^{i-1}, x_A^i); Massey's factorization p(x_A^n, x_B^n) = p(x_B^n ‖ x_A^n) p(x_A^n ‖ x_B^{n-1}), where the second term characterizes feedback and the first the feedforward link.
- Massey's directed information I(x_A^n → x_B^n) = D_KL(p(x_A^n,x_B^n) ‖ p(x_A^n‖x_B^{n-1})p(x_B^n)) = H(x_B^n) − H(x_B^n‖x_A^n); it is always ≥ 0 and equals mutual information only when the channel is free of feedback.
- Key decomposition (Eq. 20): I(x_A^n → x_B^n) + I(x_B^{n-1} → x_A^n) = I(x_A^n ; x_B^n), so mutual information splits into feedforward and feedback flows; mutual information always exceeds the directed information in the presence of feedback.
- The full decomposition (Eq. 34): I(x_A^{n-1}→x_B^n) + I(x_B^{n-1}→x_A^n) + I(x_A^n ↔ x_B^n) = I(x_A^n ; x_B^n), where I(x_A^n ↔ x_B^n) is the instantaneous information exchange; mutual information = sum of directional dependences plus instantaneous coupling.
- Schreiber's transfer entropy (2000, coined "transfer entropy" but appearing earlier under other names) is defined under a joint Markov assumption and equals I(x_A^{n-1}; x_B(n) | x_B^{n-1}); for stationary processes the rates satisfy I_∞(x_A→x_B) = T_∞(x_A→x_B) + I_∞(x_A↔x_B), i.e. transfer entropy is the part of directed information measuring past influence, not instantaneous dependence.
- Inference link: Granger causality is recast (Definition 5) as A does not Granger cause B relative to V iff the causal conditional transfer entropy I(x_A^{n-1}→x_B^n‖x_C^{n-1}) = 0; under a positive Harris recurrent Markov chain, the log-likelihood ratio (1/T)l(x_A^T,x_B^T) → T_∞(x_A→x_B) almost surely under H1; by Stein's lemma the best false-alarm probability follows exp(−T·I(x_A→x_B)).

## Critical notes from the literature
- The authors explicitly disclaim the practical estimation problem: they "will not review any practical aspects, nor any detailed applications" and "will not review the estimation problem here," deferring to other reviews; the conclusions note they "eluded the important question of how to practically use the definitions and measures."
- Granger causality is relative to the observation set V: conclusions can change when V is enlarged or reduced (illustrated by the chain x→y→z, where x causes z relative to {x,z} but not relative to {x,y,z}); results also depend on the chosen cost function and function class.
- The paper stresses that "Granger causality" measures statistical dependence between the past of one process and the present of another, not causation in the interventional/causal-calculus sense of Pearl; true causality can be inferred unambiguously only in restricted cases such as directed acyclic graphs.
- In the multivariate case the clean bivariate decomposition is blurred: an extra term ΔI(x_C^n ↔ x_B^n) appears (Eq. 36) distinguishing intrinsic coupling (depending only on C and B) from extrinsic coupling (created by other variables); a clean Stein-lemma-style result for the multivariate case does not exist in the literature and the authors propose an extension only for instantaneously uncoupled time series.
- Kullback-divergence-based information measures are one choice among others; the authors note alternative divergences or RKHS-based conditional-independence measures (e.g., Fukumizu's conditional covariance operator, Hilbert-Schmidt norm) could be used.

## Key topics covered
Granger causality; directed information theory; transfer entropy; causal conditioning (Kramer); directed information (Massey); instantaneous coupling / instantaneous information exchange; conditional independence; mutual information decomposition; feedback and feedforward in channels; Granger causality graphs (Eichler); Geweke's Gaussian-case decomposition; directed information rates; side information / multivariate case; intrinsic vs extrinsic coupling; hypothesis-testing inference; Stein's lemma; Lautum directed/transfer entropy; Kullback-Leibler divergence; stationary stochastic processes.

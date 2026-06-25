---
citekey: ilidrissi2025beyond
title: Beyond Shapley Values: Cooperative Games for the Interpretation of Machine Learning Models
authors: Il Idrissi, Marouane and Fernandes Machado, Agathe and Charpentier, Arthur
year: 2025
doi: 10.48550/arXiv.2506.13900
arxiv: null
journal: arXiv preprint
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2506.13900
sha256: b08dc5998f5f951e3e8495799338fc5fa9e50e201d74d3714732b169347194ff
pdf_path: literature/pdfs/ilidrissi2025beyond.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a perspective/position paper arguing that post-hoc machine-learning interpretability, which has been dominated by Shapley values, should move "beyond Shapley values" to exploit the richer space of cooperative-game allocations. The authors revisit cooperative game theory from an interpretability standpoint and highlight two general families of allocations — the Weber set (allocations expressible as expected marginal contributions over a probability distribution on player orderings) and the Harsanyi set (allocations redistributing coalition "dividends" according to a weight system) — both of which generalize and contain the Shapley value as a special case. A central conceptual claim is that the choice of aggregation rule (which allocation) is distinct from the choice of value function, that efficiency is the only axiom that genuinely matters for XAI because it guarantees the quantity of interest is fully redistributed among features, and that the standard Shapley axioms govern only the aggregation process, not the value function. The authors contend that the most consequential decision in feature attribution is the selection of the value function, and that feature attribution is fundamentally "a problem of representation." They propose a three-step blueprint for building model-agnostic attributions: (1) choose a quantity of interest worth studying, (2) choose a value function whose full-set evaluation equals that quantity, and (3) choose an efficient allocation. They illustrate with worked examples (e.g., the proportional marginal effects / PME of Herin et al. 2024 for variance decomposition, and oblique-projection value functions that yield "pure" allocations) showing how non-Shapley allocations can avoid sensitivity to correlation and better detect spurious features.

## Key facts it relies on
- The paper defines an allocation as efficient if Σ_{j∈D} φ_v(j) = v(D) − v(∅), i.e., the allocation redistributes the whole worth v(D) among the players/features.
- The Shapley value is defined (Shapley 1951) as Shap_v(j) = (1/d) Σ_{A⊆P_D, j∉A} [ (d−1 choose |A|) ]^{−1} [ v(A∪{j}) − v(A) ].
- The Weber set (Weber 1988) is the set of allocations expressible as φ_v(j) = E_p[ v(π^j) − v(π^j \ {j}) ], parameterized by a probability mass function p over player orderings; Theorem 1 states φ_v = Shap_v iff p(π) = 1/d! for every π (the uniform distribution).
- The Harsanyi set redistributes dividends φ_v(A) = Σ_{B⊆A} (−1)^{|A|−|B|} v(B) (Harsanyi 1963, Eq. 3) via a weight system λ with conditions λ_j(A) ≥ 0, Σ_j λ_j(A) = 1, and λ_j(A)=0 when j∉A; Theorem 2 states φ_v = Shap_v iff λ_i(A) = 1/|A| (the egalitarian redistribution of dividends).
- Both the Weber set (Proposition 1) and the Harsanyi set (Proposition 2) yield efficient allocations.
- The paper emphasizes that the aggregation process (allocation) is distinct from the choice of value function, with two consequences: an allocation cannot correct a poorly chosen value function, and the axioms typically used to justify attributions govern only the aggregation process, not the value function.
- The proposed three-step blueprint: Step 1, choose a meaningful quantity of interest; Step 2, choose a value function such that v(D) on the full set equals the chosen quantity; Step 3, choose an efficient allocation.
- Worked example with d=2, X_1, X_2 ~ N(0,1), Corr(X_1,X_2)=ρ, model f(X)=x_1+x_2+x_1 x_2, value function v(A)=E[f(X)|X_A=x_A]: the resulting Shapley values include ρ-dependent terms (e.g., Shap_v({1}) = x_1 + (ρ/2)(x_1 + x_1^2 − x_2 − x_2^2 − 1) + x_1 x_2 / 2), illustrating a lack of "purity"; oblique-projection value functions (Il Idrissi et al. 2025) instead give Shap_v({1}) = x_1 + x_1 x_2 / 2.
- The PME (proportional marginal effects, Herin et al. 2024) uses value function v(A) = V(E[f(X)|X_A]) / V(f(X)), adapts proportional values (Ortmann 2000) to the dual game, and is shown able to detect spurious features: in a d=3 example with X_3 spurious and f(X)=X_1+X_2, PME_w({3}) = 0 while Shapley values remain sensitive to ρ (Shap_w({3}) = ρ^2/4).
- The Harsanyi weight system can be interpreted as a sparse row-stochastic matrix of dimension 2^d × d.

## Critical notes from the literature
- The paper is explicitly framed as a perspective/blueprint rather than a new method or empirical study; its stated goal is to "serve as a blueprint for innovation in feature attribution" and move beyond fixed axioms, not to benchmark a new estimator.
- The authors acknowledge (citing Verdinelli and Wasserman 2024, Xin et al. 2024, Haufe et al. 2024) that Shapley-based attributions rest on axiomatic justifications whose interpretation as measures of feature importance is ambiguous and has faced criticism, and that the lack of rigorous theoretical foundations hinders assessment of attribution correctness.
- They note the "absence of ground truth limits empirical comparisons," so theoretical results are presented as essential for guiding method choice — implying claims about which allocation is "better" cannot in general be settled empirically.
- The paper concedes open problems: it is "unclear how to interpret Shapley values" under sparse row-stochastic Harsanyi weight systems, and optimal-transport-based or alternative optimization-driven allocations "have yet to be explored in the literature," so several proposed directions remain speculative.
- Multiple distinct value functions can represent the same quantity of interest (Sundararajan and Najmi 2020), so the authors caution that the framework's interpretive output depends heavily on a non-unique value-function choice.

## Key topics covered
- Cooperative game theory for explainable AI (XAI) / post-hoc feature attribution
- Shapley values; SHAP (Štrumbelj and Kononenko 2010; Lundberg and Lee 2017)
- Weber set / random-order (permutation) interpretation of allocations
- Harsanyi set / dividend redistribution interpretation
- Efficiency axiom and its primacy for XAI
- Distinction between value function and aggregation rule
- Three-step blueprint for model-agnostic attribution
- Value-function choice; conditional expectations vs. oblique projections; "purity"
- Proportional marginal effects (PME); variance decomposition; sensitivity analysis
- Detection of spurious / correlated features; proportional values (Ortmann 2000)
- Asymmetric Shapley values / causal structure (Frye et al. 2020); optimal transport for novel allocations

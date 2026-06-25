---
citekey: li2024shapley
title: Shapley value: from cooperative game to explainable artificial intelligence
authors: Li, Meng and Sun, Hengyang and Huang, Yanjun and Chen, Hong
year: 2024
doi: 10.1007/s43684-023-00060-8
arxiv: null
journal: Autonomous Intelligent Systems
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.1007/s43684-023-00060-8.pdf
sha256: 1e3e7dab2548d31374471395f900db8b65131e44d0d18cf693669ae426aac2c9
pdf_path: literature/pdfs/li2024shapley.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a review paper that surveys the use of the Shapley value, a solution concept from cooperative game theory, as a feature-attribution method in explainable artificial intelligence (XAI) for machine learning. The authors outline the foundational theory of the Shapley value (and its coalition-structure restriction, the Owen value) and its four axiomatic properties, then map how this game-theoretic quantity is repurposed for feature attribution in ML by treating features as "players" and the model prediction as the "payoff." The paper's central contribution is a three-dimensional classification framework that organizes existing Shapley value-based attribution methods along three axes: Shapley value type, feature replacement method, and approximation method. It also reviews restricted Shapley values (Owen value for priori coalition structures and causal Shapley value for causal relationships among features), and it surveys practical applications across three stages of ML development: pre-modeling (feature selection), in/mid-modeling (credit assignment in cooperative multi-agent RL), and post-modeling (data valuation, model explanation, diagnosis, optimization). Finally it summarizes limitations such as computational complexity, ambiguity in feature interactions, model sensitivity, and possible axiom violations by approximation methods, and points to future directions in model diagnosis and optimization.

## Key facts it relies on
- The Shapley value satisfies four axioms that make it the unique allocation rule: Efficiency (attributions sum to the prediction / total game value, sum_{i=1}^n phi_i(N,v) = v(N)), Symmetry (features contributing equally to all coalitions get equal attribution), Dummy player (a feature not affecting the prediction gets attribution zero), and Additivity/Linearity (the Shapley value of a combined game v1+v2 is the sum of the Shapley values in each game).
- A Transferable Utility (TU) cooperative game is a tuple (N, v) with player set N = {1,...,n}, characteristic function v: 2^N -> R, and v(empty) = 0; the Shapley value phi_i(N,v) is computed as a weighted sum over subsets of marginal contributions v(S ∪ {i}) − v(S) with weight factor ω(n,s) = sum over coalitions of s!(n−s−1)!/n!.
- SHAP (Shapley Additive exPlanations) was established by Lundberg and Lee in 2017 (ref [14]) as a unified framework for feature-attribution measurement integrating several popular methods.
- The Owen value (ref [20]) extends the Shapley value to games with a priori unions/coalition structure C = {C_1,...,C_m}; when the coalition structure is trivial (each player a separate coalition) the Owen value reduces to the Shapley value.
- In the ML setting, the value of the empty set equals the output expectation of the background dataset, v(empty) = f_hat(x*), where a single base value x* can represent the background data; conditional/marginal expectations f_hat(S) are obtained by integrating over features not in S (Eq. 7), with marginal integration assuming independence of observed from unobserved features.
- Exact Shapley value computation iterates over all subsets, giving computational complexity O(2^n) where n is the number of features; the paper states that for 32 features this requires approximately 17.1 billion enumerations, which is "unfeasible."
- The paper proposes a three-dimensional classification framework with axes: Shapley value type, feature replacement method (marginal, conditional, single), and approximation method; methods are tabulated in Table 1.
- Model-agnostic approximation categories listed: Monte Carlo-based (e.g., Fatima et al. [24], Castro et al. [25], Štrumbelj & Kononenko [26], Mitchell et al. [27]), Linear Regression-based (KernelSHAP by Lundberg & Lee [14]; Covert & Lee [28]; SGD-Shapley [29]; FastSHAP [30]), Multilinear sampling (Okhrati & Lipani [31]), and Generalized DeepSHAP (Chen et al. [32,33]).
- Model-specific approximation categories: Linear model-based Shapley value (time complexity linear in number of features), Tree-based (TreeSHAP, with Path-based [34] and Interventional [35,36] variants), and Neural network-based (DeepLIFT/DeepSHAP [12], SHAPNets [38]).
- Two types of restricted Shapley value in ML are distinguished: the Owen value (priori coalition structure) and the causal Shapley value (accounting for causal relationships among features); causal approaches reviewed include Asymmetric Shapley values (Frye et al. [41], relaxing the Symmetry axiom), Heskes et al.'s causal Shapley framework [42] using Pearl's do-calculus [43], and Shapley Flow (Wang et al. [44]) which allocates credit to edges of a causal DAG.

## Critical notes from the literature
- The paper explicitly lists six limitations of Shapley value in ML: (1) computational complexity even with fast approximations; (2) ambiguity in feature interactions because the Shapley value assumes individual feature contributions are independent of their interactions; (3) model sensitivity, where slight model/data variations can produce large changes in computed Shapley values, making them less stable; (4) interpretability limits for non-experts on complex models; (5) sample representativeness, since estimates depend on sampled data and biased/unrepresentative samples mislead; and (6) axiom violation, where some approximation methods rely on assumptions that sacrifice Shapley value axioms.
- For causal Shapley value, the authors note that precise quantification of causal relationships in real-world problems "remains a major challenge that hinders the practical application of causal Shapley."
- On credit assignment in cooperative MARL, the paper notes that Shapley-based value decomposition methods (SQDDPG [49], SHAQ [50]) do not show significant superiority over other cooperative MARL methods, possibly due to insufficient representation capability of the value decomposition model.
- The marginal-integration formula (Eq. 7) assumes independence of observed features from unobserved ones; the authors acknowledge real dependencies should be handled via the conditional distribution, but that high dimensionality makes determining the conditional distribution challenging (ref [21]).
- Competing-interests declaration: two authors (Hong Chen and Yanjun Huang) are editorial board members of the publishing journal (Autonomous Intelligent Systems) but state they were not involved in the review or publication decision.

## Key topics covered
- Shapley value and cooperative (TU) game theory; the four Shapley axioms (Efficiency, Symmetry, Dummy player, Additivity/Linearity)
- Owen value and coalition-structure (priori union) restrictions
- SHAP / Shapley Additive exPlanations as feature attribution
- Three-dimensional classification framework (Shapley value type, feature replacement method, approximation method)
- Feature replacement methods: marginal, conditional, single
- Model-agnostic approximations: Monte Carlo, KernelSHAP/linear regression, multilinear sampling, Generalized DeepSHAP
- Model-specific approximations: linear-model Shapley, TreeSHAP (path-based and interventional), DeepLIFT/DeepSHAP, SHAPNets
- Restricted Shapley values: Owen value and causal Shapley value (Asymmetric Shapley values, Pearl do-calculus, Shapley Flow)
- Applications across ML stages: feature selection (pre-modeling); credit assignment in cooperative MARL (mid-modeling); data valuation, model explanation, model diagnosis, model optimization (post-modeling)
- Limitations: computational complexity O(2^n), feature-interaction ambiguity, model sensitivity, interpretability, sample representativeness, axiom violation

---
citekey: rozemberczki2022shapley
title: The Shapley Value in Machine Learning
authors: Rozemberczki, Benedek and Watson, Lauren and Bayer, P{\'e}ter and Yang, Hao-Tsung and Kiss, Oliver and Nilsson, Sebastian and Sarkar, Rik
year: 2022
doi: 10.24963/ijcai.2022/778
arxiv: null
journal: 
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.ijcai.org/proceedings/2022/0778.pdf
sha256: da3c4b8afc85f6ede5a4f2dd4a6f5a61da80394b11b6f44509a8a1a6f3f349ba
pdf_path: literature/pdfs/rozemberczki2022shapley.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This IJCAI-22 survey-track paper reviews how the Shapley value, a single-valued solution concept from transferable-utility (TU) cooperative game theory, has been applied across machine learning. It first lays out the cooperative-game formalism (player set, characteristic function v with v(∅)=0, marginal contributions averaged over all permutations) and the four axioms—null player, efficiency, symmetry, and linearity—that uniquely characterize the Shapley value (Shapley 1953). Because exact computation requires a factorial number of characteristic-function evaluations (each potentially a model training), the paper catalogs approximation families: Monte Carlo permutation sampling, stratified and other variance-reduction sampling, the multilinear extension, and linear-regression (KernelSHAP) approximation. It then surveys application areas by defining a cooperative game for each: feature selection, data valuation, federated learning, explainability (universal, deep learning, graphical models, relational), multi-agent reinforcement learning, and model valuation in ensembles, each summarized with payoff, approximation method, and time complexity in a comparison table. It closes by flagging the value's main limitations—computation time, interpretability, and the failure of the axioms under approximation—and points to extensions (Owen value, Winter/level-structure value, configuration games, and other solution concepts like the core) as future directions.

## Key facts it relies on
- The Shapley value of player i is the average marginal contribution v(P^π_i ∪ {i}) − v(P^π_i) over all permutations π of the player set (Equation 1), where P^π_i is the predecessor set of i in permutation π.
- Theorem 1 (Shapley, 1953): a single-valued solution concept satisfies the null player, efficiency, symmetry, and linearity properties if and only if it is the Shapley value.
- A TU game is the pair (N, v) with characteristic function v: 2^N → R satisfying v(∅) = 0; the worked 3-player Example 1 uses payoffs v({1})=7, v({2})=11, v({3})=14, v({1,2})=18, v({1,3})=21, v({2,3})=23, v({1,2,3})=25, yielding Shapley values 32/6, 50/6, 68/6 (Table 1).
- Exact Shapley value computation has factorial time complexity (a factorial number of characteristic-function evaluations), which is prohibitive when each evaluation corresponds to training a machine learning model.
- Monte Carlo permutation sampling for cooperative games was first proposed by Castro et al. (2009) to approximate the Shapley value in linear time; Maleki et al. (2013) added finite-sample error bounds via Chebyshev's and Hoeffding's inequalities and introduced stratified sampling for variance reduction.
- Owen (1972) showed the Shapley value can be written as the integral ∫_0^1 e_i(q) dq with e_i(q) = E[v(E_i ∪ i) − v(E_i)] where each player is included in a random subset with probability q—the multilinear extension approximation.
- Lundberg et al. (2017) SHAP approximates Shapley values by solving a weighted least squares problem (Equations 2–4) with weights w_S = (|N|−1)/(C(|N|,|S|)·|S|·(|N|−|S|)); Covert et al. (2021) found SHAP is a consistent but biased estimator with lower variance than its unbiased counterpart, and proposed paired-coalition sampling improving convergence speed by an order of magnitude.
- Table 2 catalogs application areas with payoff/approximation/time, including feature selection (e.g., Cohen et al. 2007, exact O(|N|!)), data valuation (Jia et al. 2019 restricted Monte Carlo O(√|N| log|N|²); Ghorbani et al. 2019 Data Shapley O(|N|)), universal explainability (Lundberg et al. 2017 linear regression O(|N|)), and model valuation in ensembles (Rozemberczki et al. 2021 voting game O(|N|²)).
- The paper formalizes distinct cooperative games via Definitions 12–18: feature selection game, data valuation game, federated learning game, universal explainability game, neuron explainability game, relational explainability game, and ensemble game.
- Rozemberczki et al. (2021) formulate ensemble games as a special subclass of voting games, enabling game-specific approximation (Fatima et al. 2008) that yields Shapley estimates in quadratic time with a tight approximation error.

## Critical notes from the literature
- Computation time: naive Shapley computation is factorial; the authors note it is tractable only where players are few (e.g., multi-agent RL, federated learning) and intractable at scale for data valuation, explainability, and feature selection.
- Interpretability: the authors argue the average-marginal-contribution definition is unintuitive for non-game-theory experts, making it hard to translate Shapley values into actions (e.g., whether a data point with twice the Shapley value is "twice as valuable"), citing Kumar et al. (2020).
- Axioms do not hold under approximations: the paper states this is "the greatest unresolved issue"—most applications rely on approximations under which the axiomatic properties (the very justification for using the Shapley value) no longer hold, a point often overlooked (citing Sundararajan et al. 2020b).
- The authors note that for some approximation techniques the asymptotic properties are not well understood (e.g., Chen et al. 2018).
- Scope: this is a survey/overview (IJCAI Survey Track); it introduces no new method or empirical evaluation, and points to under-explored alternatives such as the Owen value, Winter/level-structure value, configuration (overlapping coalition) games, and other solution concepts (core, nucleolus, stable set, kernel) as future directions.

## Key topics covered
Shapley value; cooperative (TU) game theory; characteristic function; coalitions and grand coalition; null player, efficiency, symmetry, linearity axioms; Shapley uniqueness theorem; marginal contributions and permutations; Monte Carlo permutation sampling; stratified sampling / variance reduction; antithetic and Bayesian Monte Carlo; multilinear extension (Owen); KernelSHAP / linear-regression approximation; feature selection; data valuation (Data Shapley, distributional/Beta Shapley); federated learning; explainability (universal, deep learning neuron attribution, graphical models, graph/relational); multi-agent reinforcement learning credit assignment; ensemble model valuation / voting games; Owen value; Winter value / level-structure games; configuration games; core, nucleolus, stable set, kernel.

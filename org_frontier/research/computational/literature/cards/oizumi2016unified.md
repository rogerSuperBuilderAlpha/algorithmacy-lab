---
citekey: oizumi2016unified
title: Unified framework for information integration based on information geometry
authors: Oizumi, Masafumi and Tsuchiya, Naotsugu and Amari, Shun-ichi
year: 2016
doi: 10.1073/pnas.1603583113
arxiv: null
journal: Proceedings of the National Academy of Sciences
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1510.04455
sha256: e7159d3eb8f9931a1b486320f58cf3b7c8a5990d0cc09ffdbc785a6cb009e008
pdf_path: literature/pdfs/oizumi2016unified.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper proposes a unified information-geometric framework for quantifying spatio-temporal interactions in a stochastic dynamical system. The core construction compares a "full model" probability distribution p(X,Y) of past states X and present states Y against a "disconnected model" q(X,Y) whose degrees of freedom are constrained so that the interactions of interest are broken; the degree of interaction is the minimized Kullback-Leibler (KL) divergence from the full to the closest disconnected model, found by orthogonal projection onto a submanifold per the projection theorem of information geometry. Within this single framework, the authors show that mutual information arises when all time-lagged interactions between X and Y are broken, conditional transfer entropy arises when one transmission branch from x_i to y_j is eliminated, and stochastic interaction arises when the conditional distribution of Y given X is factorized across parts. Extending transfer entropy, they define a new measure of integrated information called "geometric integrated information" Φ_G as the minimized KL divergence over the manifold M_G in which all causal interactions between parts are broken. By construction Φ_G satisfies 0 ≤ Φ_G ≤ I(X;Y), a requirement that the prior stochastic-interaction measure violates. In the Gaussian (multivariate autoregressive) case Φ_G has a closed form 1/2 log(|Σ(E)'|/|Σ(E)|) and is shown to be closely related to multivariate Granger causality based on the generalized variance. Finally a hierarchical (partially ordered) structure of disconnected models systematically organizes all combinations of interactions and the measures derived from them.

## Key facts it relies on
- The framework quantifies interactions as the minimized KL divergence min_q D_KL(p||q) between a full model p(X,Y) and a constrained disconnected model q(X,Y), where the minimizer is the orthogonal projection of p onto the disconnected submanifold (projection theorem of information geometry).
- Mutual information is recovered when X and Y are forced independent (q(X,Y)=q(X)q(Y)): min_q D_KL(p||q) = H(Y) − H(Y|X) = I(X;Y), the total causal interaction between past and present.
- Conditional transfer entropy is recovered when a single branch x_i → y_j is broken via q(y_j|X)=q(y_j|X̃_i): min_q D_KL(p||q) = H(y_j|X̃_i) − H(y_j|X) = TE(x_i → y_j | X̃_i).
- Geometric integrated information Φ_G is defined as min_q D_KL(p||q) over manifold M_G constrained by q(Y[P_i]|X)=q(Y[P_i]|X[P_i]) for all parts P_i (breaking all between-part causal/time-lagged interactions).
- Because M_I ⊂ M_G, Φ_G satisfies 0 ≤ Φ_G ≤ I(X;Y); the paper states this is the theoretical requirement that "the whole is more than the sum of the parts."
- Φ_G is NOT the sum of the conditional transfer entropies of deleted interactions; the sum of conditional transfer entropies (equivalent to "causal density" / summed conditional Granger causality for Gaussian variables) can exceed I(X;Y) and is therefore inappropriate.
- Worked XOR example: two binary units with uniform past p(x1,x2)=1/4, y1=y2 set by the XOR of x1,x2; then TE(x1→y2|x2)=TE(x2→y1|x1)=1 and I(X;Y)=1, so the summed transfer entropies exceed the mutual information.
- Stochastic interaction (Ay) is recovered from q(Y|X)=∏_i q(Y[P_i]|X[P_i]); its manifold M_S does not include M_I (it breaks equal-time as well as time-lagged interactions), so stochastic interaction can exceed I(X;Y) and is unsuitable as an integration measure.
- In the Gaussian multivariate autoregressive model Y = AX + E, the Φ_G constraints set off-diagonal elements A'_ij = 0 (i≠j), and the closed form is Φ_G = (1/2) log(|Σ(E)'|/|Σ(E)|), with |Σ(E)| the generalized variance used in multivariate Granger causality; the paper concludes Φ_G is consistent with multivariate Granger causality based on the generalized variance.
- A hierarchical, partially ordered set of disconnected models (e.g., for two units, interactions T11,T12,T21,T22) orders KL divergence by inclusion/removal of interactions; information loss is maximized at the top where all four interactions are broken, equaling I(X;Y).

## Critical notes from the literature
- The authors restrict "causality" to statistically inferred (Granger-style) causality from limited observation, explicitly noting it "does not necessarily mean actual physical causality."
- The paper frames prior measures as deficient on its own chosen criterion: stochastic interaction (Ay) and causal density / summed conditional Granger causality can exceed I(X;Y), which the authors treat as disqualifying for an integration measure; this criterion (boundedness by mutual information) is itself drawn from the authors' related work (ref [18], Oizumi et al. arXiv:1505.04368).
- The Granger-causality correspondence and the closed-form Φ_G are derived specifically for the Gaussian / multivariate autoregressive case; the general non-Gaussian case is treated only via the abstract KL-projection construction.
- The link to consciousness is presented as motivation and expectation (IIT postulate that levels of consciousness correspond to integrated information), not as something tested here; the paper offers no empirical or neural validation, only the theoretical measure.
- Φ_G depends on a choice of system partition into parts P_1,...,P_m; the framework presupposes a given partition rather than deriving an optimal one.

## Key topics covered
Information geometry; Kullback-Leibler divergence minimization and orthogonal projection; integrated information theory (IIT); geometric integrated information Φ_G; mutual information; transfer entropy / conditional transfer entropy; stochastic interaction; causal density; multivariate Granger causality; generalized variance; multivariate autoregressive / Gaussian models; spatio-temporal (equal-time vs time-lagged) interactions; disconnected-model submanifolds; hierarchical partially ordered structure of interaction measures; consciousness measures.

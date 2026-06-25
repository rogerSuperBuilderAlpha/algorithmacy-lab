---
citekey: oizumi2016geometry
title: Unified Framework for Information Integration Based on Information Geometry
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
pdf_path: literature/pdfs/oizumi2016geometry.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper proposes a unified information-geometry framework for quantifying spatio-temporal interactions in a stochastic dynamical system. The degree of interactions is measured by the Kullback-Leibler (KL) divergence between the actual ("full model") probability distribution p(X,Y) of a system's past states X and present states Y, and a constrained ("disconnected model") distribution q(X,Y) in which the interactions of interest are severed; the disconnected models form a submanifold M_D inside the full manifold M_F, and the minimized KL divergence (found by orthogonal projection per the projection theorem) is interpreted as the "information loss" from disconnecting transmission branches. Under this framework, mutual information arises when all time-lagged interactions between X and Y are broken, transfer entropy when a single transmission branch x_i → y_j is eliminated, and stochastic interaction when conditional distributions of each part are factorized. Extending transfer entropy, the authors define a new measure of integrated information, "geometric integrated information" Φ_G, as the minimized KL divergence within a manifold M_G that breaks all causal interactions between system parts. By construction Φ_G satisfies 0 ≤ Φ_G ≤ I(X;Y), unlike stochastic interaction and causal density which can exceed the mutual information. In the Gaussian case Φ_G has a closed form and is shown to be consistent with multivariate Granger causality based on the generalized variance, and the authors organize all disconnected models into a hierarchical partially ordered structure.

## Key facts it relies on
- Interactions are quantified by minimizing the KL divergence D_KL(p||q) between the full model p(X,Y) and a disconnected model q(X,Y); the minimizer is the orthogonal projection of p onto the disconnected submanifold via the projection theorem in information geometry (Amari & Nagaoka).
- Mutual information emerges when X and Y are forced independent (q(X,Y)=q(X)q(Y)): the minimized divergence equals H(Y) − H(Y|X) = I(X;Y), interpreted as total causal interactions.
- Transfer entropy emerges when the branch x_i → y_j is broken via the constraint q(y_j|X)=q(y_j|X̃_i); the minimized divergence equals the conditional transfer entropy TE(x_i → y_j | X̃_i) = H(y_j|X̃_i) − H(y_j|X).
- Geometric integrated information Φ_G = min_q D_KL(p||q) within manifold M_G, defined by breaking all between-part causal interactions via q(Y[P_i]|X) = q(Y[P_i]|X[P_i]) for all parts i.
- Because M_I ⊂ M_G, Φ_G satisfies 0 ≤ Φ_G ≤ I(X;Y); the paper states this is the key theoretical requirement (the whole is more than the sum of its parts, non-negative and bounded by total information).
- A two-binary-unit XOR example (uniform past p(x1,x2)=1/4, y1=y2 set by XOR of x1,x2) gives TE(x1→y2|x2)=TE(x2→y1|x1)=1 and I(X;Y)=1, so the sum of conditional transfer entropies exceeds I(X;Y); the sum of conditional transfer entropies equals causal density (Seth) and equals summed conditional Granger causality for Gaussian variables (Barnett et al.), which therefore fails the integrated-information requirement.
- Stochastic interaction (Ay) uses the factorization q(Y|X)=∏_i q(Y[P_i]|X[P_i]); its manifold M_S satisfies M_S ⊂ M_G but does not contain M_I, because it also breaks equal-time interactions among present states, so stochastic interaction can exceed I(X;Y) and is unsuitable as integrated information.
- For Gaussian systems with a multivariate autoregressive full model Y = AX + E, the constraints for Φ_G set off-diagonal elements A'_ij = 0 (i≠j), yielding the closed form Φ_G = (1/2) log(|Σ(E)'| / |Σ(E)|); |Σ(E)| is the generalized variance used in multivariate Granger causality analysis, so Φ_G is consistent with Granger causality based on generalized variance.
- All disconnected models in a two-unit system (with time-lagged interactions T11, T12, T21, T22) form a partially ordered set / hierarchical lattice; KL divergence (information loss) increases from bottom to top, and at the top all four interactions are broken, corresponding to the mutual information I(X;Y).

## Critical notes from the literature
- The paper uses "causal" interactions in the sense of statistically inferred (Granger-type) causality from limited observation, explicitly noting this does not necessarily mean actual physical causality.
- The authors argue that prior measures fail the bounding requirement: stochastic interaction (Ay) and causal density / summed conditional Granger causality (Seth; Barnett et al.) can exceed I(X;Y), which they treat as a defect that Φ_G avoids by construction.
- Φ_G is explicitly not equal to the sum of the conditional transfer entropies of the deleted interactions.
- The Granger-causality correspondence and the closed-form Φ_G are derived specifically for the Gaussian (multivariate autoregressive) case; the general non-Gaussian Φ_G is defined via KL minimization but not given a closed form in the paper.
- The link to consciousness is framed as a potential application (IIT postulates levels of consciousness correspond to integrated information, supported by loss-of-consciousness experiments cited), not as something demonstrated in this paper.

## Key topics covered
- Information geometry; KL divergence minimization; projection theorem; full vs. disconnected models (M_F, M_D, M_I, M_G, M_S submanifolds)
- Integrated Information Theory (IIT); integrated information; geometric integrated information Φ_G
- Mutual information; transfer entropy and conditional transfer entropy; stochastic interaction (Ay); causal density (Seth)
- Spatio-temporal interactions; equal-time vs. time-lagged ("causal") interactions
- Multivariate autoregressive Gaussian models; multivariate Granger causality; generalized variance
- Hierarchical partially ordered structure of disconnected models
- Applications to neuroscience, network connectivity analysis, and consciousness research

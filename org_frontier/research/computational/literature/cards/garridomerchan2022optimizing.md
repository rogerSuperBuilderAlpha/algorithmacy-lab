---
citekey: garridomerchan2022optimizing
title: Optimizing Integrated Information with a Prior Guided Random Search Algorithm
authors: Garrido-Merch{\'a}n, Eduardo C. and S{\'a}nchez-Ca{\~n}izares, Javier
year: 2022
doi: 10.48550/arXiv.2212.04589
arxiv: 2212.04589
journal: 
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2212.04589
sha256: 0f2a0860c23cb7ecd1bdf6cae0dec1aeb52a42a0cb476131cc8180863807d6ba
pdf_path: literature/pdfs/garridomerchan2022optimizing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how the maximal integrated information (Φ) of a system, as defined by Integrated Information Theory (IIT), scales as the number of network nodes grows, and how one can search the space of transition probability matrices (TPMs) to find graphs with higher Φ. The authors frame Φ-maximization as a global black-box optimization problem over the high-dimensional, conditionally-constrained space of TPMs (Ω ⊆ ℝ^(2^D·D)), and argue that the objective is unsuitable for standard smart black-box methods: vanilla Bayesian optimization fails because the smallest variation in a TPM element can make Φ jump from a real value to undefined (∅), violating the K-Lipschitz continuity assumption, and metaheuristics require a cheap-to-evaluate objective, which Φ is not. They instead propose a "prior guided random search" algorithm (Algorithm 1) that samples TPM dimensionality from a multinomial prior and TPM entries uniformly, then updates the prior in a Bayesian conjugate-multinomial fashion after each batch of ε iterations to favor dimensions yielding higher Φ. Experiments using the PyPhi toolbox (with Earth Mover's Distance, equivalent to Hamming distance for binary nodes) show the method outperforms grid-search and random-search baselines across toy configurations (3–5 nodes), and a separate statistical-inference experiment finds that mean Φ increases significantly with node count. The work remains a toy model (max 6 nodes) and the authors couple it with a philosophical discussion of the intrinsicality problem and whether such an optimization procedure reflects ontology or is merely an epistemic tool.

## Key facts it relies on
- The PyPhi complexity of evaluating Φ scales as O(n·53^n) in the number of nodes n, which the authors cite to motivate the need for alternative heuristics; in the feasible-state searches this must additionally be multiplied by 2^n.
- Integrated information for a mechanism in state s is defined as φ(s) = D[p(s₀→s) ‖ p^MIP(s₀→s)] (Eq. 1), where D is a distance between the actual cause/effect distribution and the distribution under the minimum-information partition; conceptual integrated information is Φ(C) = D(C ‖ C^MIP).
- The optimization problem is ω* = arg max_{ω∈Ω} Φ(ω) s.t. ω ∈ Υ (Eq. 2), where ω is a TPM, Ω = ℝ^(2^D·D) is the D-dimensional TPM space, Υ is the space of TPMs with conditional independencies, and Φ(ω) = ∅ if ω ∉ Υ.
- Bayesian optimization is rejected because vanilla BO requires the function not vary beyond a certain K-Lipschitz value, but the smallest variation in any TPM element can make Φ jump from ℝ to ∅; BO surrogate (Gaussian process) updates also cost O(N³) in the number of prior recommendations N.
- The proposed Algorithm 1 takes inputs p(ω), D_min, D_max, μ (adaptation/learning rate), ε (batch size of iterations to update the prior), and T (total iteration budget); the prior update follows a conjugate multinomial Bayesian rule (Eq. 6) with maximum/minimum probabilities smoothed by κ = 0.02 and a default likelihood that linearly penalizes/rewards each dimension by 0.2·μ·r points (r the ranking on a [−1,1] linear-space vector).
- The justification for random over grid search cites Bergstra and Bengio: random search outperforms grid search when the explained variance of the objective is not uniform across the input variables.
- First experiment (D_min=3, D_max=4, 50 iterations, ε=5, μ=0.1, prior p(ω)=[0.2,0.8], 25 repetitions): the prior guided random search outperforms both baselines, performing "almost twice as better" as grid search; the best Φ found was 3.034082, and the authors state a hypothesis test would give p < .01.
- A 5-node experiment (prior p(ω)=[0.1,0.1,0.3,0.5], 50 iterations, 5 repetitions) gives maximum Φ of 3.1681 for prior guided random search versus 2.0832 for random search; a graphical experiment (100 repetitions, 3–4 nodes, prior [0.3,0.7]) yielded a graph with Φ = 2.6823 and final prior [0.12,0.88].
- Statistical inference experiment (100 graphs each): empirical mean Φ = 0.0517 (3 nodes) vs 0.1711 (4 nodes), 95% CIs [0.0212,0.0822] and [0.1093,0.2328], 2-sample t-test t = −3.38, p = 0.0008; percentage of infeasible solutions was 72.6775% (3 nodes) and 84.7094% (4 nodes). A 4-vs-5 node comparison gave means 0.1432 vs 0.3267, t = −2.94, p = 0.0036, with 84.98% and 91.84% infeasible solutions.
- Experiments use the PyPhi toolbox (Python3) with Earth Mover's Distance to measure distance between probability distributions (equivalent to Hamming distance for binary nodes); code is at https://github.com/EduardoGarrido90/iit_opt.

## Critical notes from the literature
- The authors explicitly state their results remain a toy model with a maximum of 6 nodes, being unable to test Φ in TPMs with 6 or more nodes due to algorithmic complexity, and that the requirement of conditional independence for TPMs "charge[s] our procedure with a burden that may not be eased out."
- They quote PyPhi's own limitation: the analysis can only be meaningfully applied to systems that are Markovian and satisfy conditional independence, with no guarantee these hold for TPMs derived from observed time series (e.g., EEG recordings).
- The paper acknowledges the "intrinsicality problem" (IP) raised by other authors (Mørch; Sánchez-Cañizares): maximal Φ depends on whether the system is embedded in larger systems, so an optimization procedure that adds nodes to increase Φ may not reflect intrinsic consciousness, and IP could threaten IIT's conception of causality.
- The authors note their own philosophical caveat that an optimization procedure "might just be an epistemic tool" to obtain the magnitude maximizing Φ and "need not unravel the ontological processes underlying the reality of said quantity."
- The paper acknowledges Bayesian optimization could outperform their method if an analytical transformation from the TPM space into a smooth continuous space (modelable by a Gaussian process) could be found; this is left as future work.

## Key topics covered
Integrated Information Theory (IIT); maximal Φ; transition probability matrices (TPMs); minimum-information partition (MIP); black-box global optimization; prior guided random search; Bayesian optimization and K-Lipschitz continuity; metaheuristics / genetic algorithms; grid vs random search; conjugate multinomial Bayesian prior update; PyPhi toolbox; Earth Mover's Distance / Hamming distance; Φ scaling with node count; statistical hypothesis testing (t-tests, confidence intervals); intrinsicality problem; machine consciousness; computational complexity of Φ.

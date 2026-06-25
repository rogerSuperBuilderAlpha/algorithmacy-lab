---
citekey: friston2010free
title: The Free-Energy Principle: A Unified Brain Theory?
authors: Friston, Karl
year: 2010
doi: 10.1038/nrn2787
arxiv: null
journal: Nature Reviews Neuroscience
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://static-content.springer.com/esm/art%3A10.1038%2Fnrn2787/MediaObjects/41583_2010_BFnrn2787_MOESM251_ESM.pdf
sha256: 0aaabefd8361bc35d0060770df14624ba11a5407ef2d8e7218578d2072df8370
pdf_path: literature/pdfs/friston2010free.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This document is the supplementary information (Box S1, "The entropy of sensory states and their causes," February 2010) for Friston's Nature Reviews Neuroscience article proposing the free-energy principle as a candidate unified theory of brain function. The acquired text addresses a specific mathematical claim underpinning the principle: that the entropy of hidden states in the environment is upper-bounded by the entropy of an agent's sensory states. The argument defines the entropy of generalised sensory states as their long-term average surprise (the negative log probability of sensations under a model m), and, assuming sensory states are an analytic function of hidden environmental states plus generalised random fluctuations, derives an information-theoretic inequality. The conclusion is that minimising the entropy of sensory signals also minimises the entropy of the environmental states that caused them, which grounds the principle's claim that agents resist disorder by minimising sensory surprise. The derivation rests on ergodic and diffeomorphic-mapping assumptions whose limits the box explicitly flags.

## Key facts it relies on
- The entropy of generalised sensory states H(s̃|m) is defined as their average surprise −ln p(s̃|m), and under ergodic assumptions equals the long-term time (path) integral of surprise (Eq. S1.1).
- The generative process is modelled as s̃ = g(x̃,θ) + z̃ with hidden-state dynamics ẋ̃ = f(x̃,θ) + w̃, i.e. sensory states are an analytic function of hidden environmental states plus generalised random fluctuations (Eq. S1.2).
- Because hidden states x̃ and noise z̃ are statistically independent, the box obtains I(s̃,z̃) = H(s̃|m) − H(x̃|m) − ∫ p(x̃|m) ln|∂x̃ g| dx̃ (Eq. S1.3), citing Eq. 6.4.6 in Jones (1979, p149).
- The mutual information I(s̃,z̃) ≥ 0 is non-negative by Gibbs' inequality (cross-entropy / Kullback–Leibler divergence non-negative), attributed to Theorem 6.5 in Jones (1979, p151).
- Rearranging yields the central inequality H(x̃|m) ≤ H(s̃|m) − ∫ p(x̃|m) ln|∂x̃ g| dx̃ (Eq. S1.4): the entropy of hidden states is upper-bounded by the entropy of sensations (assuming constant sensitivity over the range of states encountered).
- The derivation assumes the sensory mapping g : x̃ → s̃ is diffeomorphic (bijective and smooth), requiring hidden and sensory state-spaces of equal dimension; with n hidden states in m generalised coordinates, one considers m sensory states in n generalised coordinates so that dim(x̃) = dim(s̃) = n × m.
- The only external reference cited in this box is Jones, D.S. (1979), Elementary Information Theory, Oxford: Clarendon Press / Oxford University Press.

## Critical notes from the literature
- Scope of the acquired PDF: the file is the two-page supplementary information box (S1) provided "in format provided by Friston (FEBRUARY 2010)," not the full main review article; claims here cover only the entropy-bound derivation, not the broader unified-brain-theory argument, active inference, or the perception/action sections of the main text.
- The box explicitly limits its own ergodic assumption (Eq. S1.1): it "only holds over certain temporal scales for real organisms that are on a trajectory from birth to death," holding locally over somatic scales (days/months, where development is locally stationary) or evolutionary scales (generations).
- The entropy bound is contingent on the sensory mapping being diffeomorphic and on its sensitivity to hidden states being (assumed) constant over the range of states encountered; the box notes entropy is not invariant to a change of variables, which is why the Jacobian term ∫ p(x̃|m) ln|∂x̃ g| dx̃ appears.

## Key topics covered
Free-energy principle; entropy of sensory states; surprise / surprisal; generalised coordinates of motion; hidden vs sensory states; generative model; ergodic assumption; mutual information; Gibbs' inequality / Kullback–Leibler divergence; diffeomorphic sensory mapping; Jacobian of sensory mapping; information theory (Jones 1979); somatic vs evolutionary timescales.

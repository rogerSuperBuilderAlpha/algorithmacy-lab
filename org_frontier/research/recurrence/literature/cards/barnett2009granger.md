---
citekey: barnett2009granger
title: Granger Causality and Transfer Entropy Are Equivalent for Gaussian Variables
authors: Barnett, Lionel and Barrett, Adam B. and Seth, Anil K.
year: 2009
doi: 10.1103/PhysRevLett.103.238701
arxiv: null
journal: Physical Review Letters
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/0910.4514
sha256: 9b67c3020c9cc9b4d1032e76eca314c9052cd5d1033d795c5515663886c77cf1
pdf_path: literature/pdfs/barnett2009granger.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how Wiener-Granger causality (G-causality), a prediction-based autoregressive measure of directed influence, relates formally to transfer entropy, an information-theoretic measure of directed information transfer formulated by Schreiber. While the two had been recognized as related, their exact relationship had never been formally specified. The authors work in the general multivariate, conditional setting with three jointly distributed stationary stochastic processes X, Y, Z, expressing G-causality via determinants of partial covariance matrices and transfer entropy via differences of conditional entropies. Using the standard Gaussian expression for entropy in terms of the log-determinant of the covariance matrix, they show that for jointly multivariate Gaussian processes the conditional entropy reduces to a partial-covariance log-determinant, making the two measures algebraically identical up to a factor of 2: F_{Y→X|Z} = 2 T_{Y→X|Z}. This bridges autoregressive and information-theoretic approaches to data-driven causal inference, opening possibilities such as spectral (frequency-domain) implementations of transfer entropy. The authors caution that empirical numerical equivalence depends on the transfer-entropy estimation method, and that the equivalence is exact only under Gaussian assumptions.

## Key facts it relies on
- Central result: under joint Gaussianity, G-causality and transfer entropy are equivalent up to a factor of 2, F_{Y→X|Z} = 2 T_{Y→X|Z} (eq. 13); this holds in particular for a univariate predictee X with the standard G-causality definition (eq. 8).
- The partial covariance is defined as Σ(X|Y) ≡ Σ(X) − Σ(X,Y) Σ(Y)^{-1} Σ(X,Y)^⊺ (eq. 1), and equals the residual covariance matrix of an OLS regression of X on Y (eq. 3).
- Standard (univariate-predictee) G-causality is the log ratio of restricted to unrestricted residual variances: F_{Y→X|Z} = ln(Σ(X|X⁻⊕Z⁻)/Σ(X|X⁻⊕Y⁻⊕Z⁻)) (eq. 8), and is always ≥ 0.
- For the multivariate-predictee case the authors adopt Geweke's extension replacing residual variance var(ε) with the generalized variance |Σ(ε)|: F_{Y→X|Z} = ln(|Σ(X|X⁻⊕Z⁻)|/|Σ(X|X⁻⊕Y⁻⊕Z⁻)|) (eq. 9), which reduces to eq. 8 for a univariate predictee.
- Transfer entropy is defined as T_{Y→X|Z} ≡ H(X|X⁻⊕Z⁻) − H(X|X⁻⊕Y⁻⊕Z⁻) (eq. 10), the difference between entropy of X conditioned on its own (and Z's) past and that additionally conditioned on Y's past; it is always ≥ 0.
- For a multivariate Gaussian variable, entropy is H(X) = (1/2) ln(|Σ(X)|) + (1/2) n ln(2πe); the authors derive H(X|Y) = (1/2) ln(|Σ(X|Y)|) + (1/2) n ln(2πe) (eq. 11) using the block-determinant identity |Σ(X⊕Y)| = |Σ(Y)| · |Σ(X|Y)|.
- Substituting eq. 11 gives the Gaussian transfer entropy T_{Y→X|Z} = (1/2) ln(|Σ(X|X⁻⊕Z⁻)|/|Σ(X|X⁻⊕Y⁻⊕Z⁻)|) (eq. 12), whose direct comparison with eq. 9 yields the factor-of-2 equivalence.
- The G-causality maximum likelihood estimator is asymptotically χ²-distributed under the null F_{Y→X|Z} = 0 and non-central χ² under the alternative F_{Y→X|Z} > 0.
- G-causality originates with Wiener and Granger (econometrics); transfer entropy was formulated by Schreiber (Phys. Rev. Lett. 85, 461, 2000); the multivariate G-causality extension used here is Geweke's (J. Am. Stat. Assoc. 77, 304, 1982).

## Critical notes from the literature
- The equivalence is exact only under Gaussian assumptions; the authors note that the appropriateness of Gaussian assumptions may be disputed for specific physical systems, and that establishing whether they hold for empirical data (especially highly multivariate datasets with limited sample sizes) is likely difficult. They call for further research characterizing how eq. 13 breaks down when Gaussianity fails.
- Numerical equivalence in practice depends on the transfer-entropy estimation method: it is guaranteed only if conditional entropies are estimated from sample covariance matrices under a Gaussian model. Naive state-space partitioning estimators are problematic and often fail to converge; kernel and k-nearest-neighbour estimators carry their own distributional assumptions.
- Unlike G-causality, transfer entropy has no known general (asymptotic) sampling distribution, so significance testing for transfer-entropy estimates is "likely to be hard."
- The authors stress that identifying a G-causality interaction is not identical to identifying a physically instantiated causal interaction; physical causal structure can only be unambiguously established by perturbing the system (citing Pearl). The regressions in eqs. 6–7 are predictive models, not actual MVAR processes, and variables may depend on latent/exogenous unmeasured factors.
- In the generic non-Gaussian case the equivalence no longer holds exactly, but it is known that nonzero G-causality implies nonzero transfer entropy (Marinazzo et al., Phys. Rev. Lett. 100, 144103, 2008). The authors also note preliminary (unpublished) work suggesting that under Gaussian assumptions nonlinear extensions to G-causality add nothing, since a stationary Gaussian AR process is necessarily linear.

## Key topics covered
- Wiener-Granger causality (G-causality)
- Transfer entropy (Schreiber)
- Gaussian / multivariate Gaussian processes
- Partial covariance and conditional covariance
- Conditional G-causality (conditioning variable Z)
- Multivariate autoregressive (MVAR) modeling; OLS regression; Yule-Walker equations
- Generalized variance and Geweke's multivariate G-causality extension
- Conditional entropy and log-determinant entropy formula; block-determinant identity
- χ² and non-central χ² sampling distributions; significance testing
- Data-driven causal inference; spectral / frequency-domain decomposition
- Neuroscience and econometrics applications

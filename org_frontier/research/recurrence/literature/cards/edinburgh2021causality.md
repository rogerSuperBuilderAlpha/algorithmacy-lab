---
citekey: edinburgh2021causality
title: Causality Indices for Bivariate Time Series Data: A Comparative Review of Performance
authors: Edinburgh, Tom and Eglen, Stephen J. and Ercole, Ari
year: 2021
doi: 10.1063/5.0053519
arxiv: null
journal: Chaos: An Interdisciplinary Journal of Nonlinear Science
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2104.00718
sha256: ff5a70621cd97b635ed82de4491a60d7df70fe973a5887ab6c19f0283bdc6ccb
pdf_path: literature/pdfs/edinburgh2021causality.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how the many published "causality indices" for inferring directed, nonlinear, asymmetric relationships in bivariate time series compare against one another, given that there is no single consistent mathematical definition of causality for time series. The authors evaluate ten prominent indices across four simulated model systems (a linear stochastic process, an Ulam lattice, and Hénon unidirectional and bidirectional maps) with differing coupling schemes, varying coupling strength λ and data size T. They find generally strong pairwise agreement between methods (minimum, median, and maximum Pearson correlation of 0.298, 0.719, and 0.955 between any pair, excluding the two similarity indices), but show that the methods are not always invariant to real-world data transformations such as standardisation/scaling, rounding error, missing data, and added Gaussian noise. On this basis they recommend transfer entropy (KSG estimator) and nonlinear Granger causality as the strongest approaches, with predictability improvement as a reasonable alternative, because these successfully identify both presence and absence of causality while remaining robust to rounding error, at least 20% missing data, and small-variance Gaussian noise. They provide open-access Python code and a CODECHECK-certified reproduction.

## Key facts it relies on
- Ten indices are compared: extended Granger causality (EGC), nonlinear Granger causality (NLGC), predictability improvement (PI), transfer entropy via histogram binning TE (H) and via the Kraskov-Stögbauer-Grassberger estimator TE (KSG), effective transfer entropy ETE (H), coarse-grained transinformation rate (CTIR), two similarity indices SI(1) and SI(2), and convergent cross mapping (CCM); they are grouped into regression-based, information-theoretic, state-space/cross-mapping categories.
- Averaged across all simulations, pairwise Pearson correlations between any pair of methods (excluding the two similarity indices) have minimum, median, and maximum of 0.298, 0.719, and 0.955 respectively.
- Four simulated systems (Table II): linear process (X←Y, linear & stochastic, T=10^4, b_x=0.8, b_y=0.4, σx²=σy²=0.2, λ∈[0,1]); Ulam lattice (X→Y, nonlinear/deterministic/chaotic, NL=100, λ∈[0,1]); Hénon unidirectional map (a=1.4, b_x=b_y=0.3, λ∈[0,1]); Hénon bidirectional identical/non-identical maps (λxy, λyx ∈ [0, 0.4]). The first 10^5 iterations were discarded as transients (10^4 for the linear process); coupling incremented by 0.01 over 10 independent runs.
- TE (H) significantly underestimates analytically derived "true" transfer entropy in the linear process, called "a fundamental flaw," whereas TE (KSG) reliably matches the analytic solution; the authors recommend the KSG algorithm for TE computation unless data is extremely scarce (T < 10^3).
- TE reduces to vanilla Granger causality under Gaussian variables (Barnett, Barrett & Seth 2009), and non-zero GC implies violation of the generalised Markov property and non-zero TE; transfer entropy (Schreiber 2000) measures deviation from p(x_{t+1}|x_t) = p(x_{t+1}|x_t, y_t) as a conditional mutual information.
- The work reproduces and extends the earlier review by Lungarella et al. (Ref 19), adding CTIR, CCM, ETE (histogram) and TE (KSG); they deviated by using k-means rather than fuzzy c-means clustering for NLGC RBF centers, finding similar/improved results at much lower computational cost.
- In sensitivity experiments using the Ulam lattice (T=10^3) as baseline (Table III), deviations are reported as f(μ,μ̂) and g(σ,σ̂); both transfer entropy estimators and CTIR show large increases in value with data size (e.g. TE (KSG) f=-1.348, CTIR f=-1.226 at T=10^5), while scaling Y by 10 catastrophically inflates NLGC (f=-101.849) and PI (f=-98.727).
- All methods appear robust to 10% and 20% missing data; with small-variance observation noise (σ_G=0.1) the effect is small for all indices, but larger noise (σ_G=1) added to the causal variable X produces the biggest changes for most methods.
- Information-theoretic computation is in nats (log base e); KSG used k=4 nearest neighbours with ℓ∞ metric, histogram used N=8 bins, ETE used N_shuffle=10 shuffles, CCM used n_T=40 segments and convergence tolerance δρ=0.05.

## Critical notes from the literature
- The authors stress there is no single consistent, fundamental mathematical definition of quantitative causality for time series data, and no single method whose all-round performance exceeds all others; they recommend using more than one method from different theoretical backgrounds.
- They acknowledge unresolved concerns about TE (KSG): it appears to increase in magnitude as more data become available (initial computations do not support convergence to a "correct" value), and it suffers when data are unequally scaled due to difficulty identifying unique nearest neighbours; hence they recommend a standardisation/normalisation pre-processing step.
- The similarity indices (SI) did not consistently identify the strength or direction of causality; CCM improved on them but also sometimes misidentified the direction of causal flow (e.g. negative DX→Y for λ<0.5 in the Ulam lattice).
- The study is explicitly limited to the bivariate setting: bivariate indices cannot be definitively interpreted as a direct causal relationship because confounding, redundancy, and synergy among omitted variables can create spurious results; they flag conditional/multivariate and graphical-model extensions as key further work.
- They could not fully replicate Lungarella et al. in all cases (minor magnitude/profile differences for EGC, PI, SI(1), TE), did not reproduce a reported synchronisation/numerical-instability region in the Hénon bidirectional map, and report it is unclear why these differences exist; results were CODECHECK-certified (doi.org/10.5281/zenodo.4720843).

## Key topics covered
Bivariate causality inference; Granger causality (vanilla, extended EGC, nonlinear NLGC); transfer entropy (histogram and KSG estimators); effective transfer entropy; coarse-grained transinformation rate; predictability improvement; convergent cross mapping; similarity indices; conditional mutual information; generalised Markov property; time-delay embedding and Takens' theorem; state-space reconstruction; separability; coupling strength and synchronisation; chaotic maps (Ulam lattice, Hénon maps); sensitivity to standardisation/scaling, rounding error, missing data, and Gaussian noise; computational cost benchmarking; reproducibility/CODECHECK; open-access Python implementation.

---
citekey: wallot2018ami
title: Calculation of Average Mutual Information (AMI) and False-Nearest Neighbors (FNN) for the Estimation of Embedding Parameters of Multidimensional Time Series in Matlab
authors: Wallot, Sebastian and M{\o}nster, Dan
year: 2018
doi: 10.3389/fpsyg.2018.01679
arxiv: null
journal: Frontiers in Psychology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01679/pdf
sha256: c00f794842158d24be4c75fef7d4148d6fe306ec53983d53056b8ce1b0df0cb3
pdf_path: literature/pdfs/wallot2018ami.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This technology report addresses how to estimate the two parameters needed for time-delayed embedding — the delay parameter tau and the embedding dimension parameter D — when the empirical time series is already multidimensional (dimensionality d > 1), as arises in phase-space reconstruction for Multidimensional Recurrence Quantification Analysis (MdRQA). The two standard one-dimensional methods, the Average Mutual Information (AMI) function (Fraser and Swinney, 1986) and the False Nearest Neighbor (FNN) function (Kennel et al., 1992), are extended to multivariate data: for tau the authors implement the "uniform multivariate average mutual information" method (Vlachos and Kugiumtzis, 2009), which averages AMI over all dimensions, and for D they extend the FNN algorithm so embedding adds d coordinates per step rather than 1. The methods are released as the Matlab functions mdDelay and mdFnn (available on GitHub at github.com/danm0nster/mdembedding) and demonstrated on data from the Lorenz system. A key conceptual point is that in the multivariate FNN implementation, D denotes the number of times the d-dimensional series must be embedded, so the reconstructed phase-space has dimensionality d × D. The authors show the multivariate approach gives a better D estimate than averaging univariate estimates, especially for "ill-composed" data containing an uninformative (noise) dimension.

## Key facts it relies on
- Time-delayed embedding (Packard et al., 1980; Takens, 1981) requires two parameters: delay tau and embedding dimension D, where D − 1 is the number of times the series is plotted against itself at delay tau.
- AMI is defined as I(x(t), x(t+τ)) = Σ_{i,j} p_ij(τ) log(p_ij(τ)/(p_i p_j)) (Equation 1); the optimal tau is the first local minimum, or — when no minimum exists — the lowest tau at which AMI drops below 1/e (Kantz and Schreiber, 2004).
- For tau the authors use the "uniform multivariate average mutual information" method (Vlachos and Kugiumtzis, 2009), averaging AMI over all dimensions; Vlachos and Kugiumtzis showed this simple method gives reconstruction quality comparable to more complicated non-uniform methods.
- The multivariate FNN extension replaces D+1 with (D+1)·d (Equation 5), so embedding proceeds in steps of d (the number of component variables) rather than 1; in this implementation D denotes the number of times the d-dimensional series is embedded, and the resulting phase-space has d × D dimensions (e.g., d=3 embedded D=2 times gives 6 dimensions).
- The example uses the Lorenz system (Lorenz, 1963) with parameters σ = 10, ρ = 28, β = 8/3, applied to single dimensions (x, y, z), pairs (xy, xz, yz), and all three (x, y, z).
- Table 1 results (τ, D, D·d): x → τ=19, D=3, D·d=3; y → τ=15, D=3, 3; z → τ=12, D=3, 3; x,y → τ=17, D=2, 4; x,z → τ=16, D=1, 2; y,z → τ=14, D=1, 2; x,y,z → τ=15, D=1, 3.
- For the three-dimensional Lorenz series, mdDelay was called with maxLag=25 (default 10 was too small); first AMI minima were at τ = 15, 16, 19, only one curve dropped below 1/e (at τ=12), and the returned mean was τ = (12+15+19)/3 ≈ 15.33, rounded to 15; mdFnn (tau=15, 10^4 data points) showed FNN dropping immediately to 0, indicating no further embedding needed.
- mdFnn default parameters: maxEmb=10, doPlot=1/true, numSamples=500 (random sample to cut computation time), Rtol=10, Atol=2; mdDelay default parameters: criterion="firstBelow", threshold=1/e, numBins=10, maxLag=10, plottype="mean".
- In the noise-contamination example (Lorenz x plus uniform random noise), univariate averaging gives τ=10, D=3 then must divide by d giving D=3/2=1.5 (under- or over-embed); the multivariate functions return τ=10, D=3, correctly meaning 2 additional embeddings (D−1).

## Critical notes from the literature
- The authors stress the algorithms should not be used without inspecting the AMI and FNN plots, since parameter choice depends on the form of the curves; e.g., the τ=19 estimate for the Lorenz x variable sits in a very flat AMI range (τ ∈ [13, 20]), and lower values are preferable because higher τ and D reduce the number of data points available for analysis.
- The methods provide limited accuracy when the true dimensionality of the system is not an integer-multiple of the time series dimensionality d, because time-delayed embedding proceeds only in integer dimensions (e.g., two-dimensional series cannot exactly reconstruct a three-dimensional system; the resulting phase-space dimension differs from the correct one by one).
- Only fixed bin width is used for the AMI histograms; for series with very different densities across the range, adaptive binning may be more appropriate (Cellucci et al., 2005).
- If individual dimensions have very different AMI functions and yield very different tau estimates, embedding them all with the same tau may be inappropriate; the authors suggest re-sampling some dimensions at a lower rate or using different time delays per dimension.
- For long, high-dimensional series, computation time may be several minutes per series; drawing random sub-series can substantially reduce processing time.

## Key topics covered
- Time-delayed embedding; Takens' theorem; phase-space reconstruction
- Average Mutual Information (AMI) for delay (tau) estimation
- False Nearest Neighbors (FNN) for embedding dimension (D) estimation
- Uniform multivariate AMI (Vlachos and Kugiumtzis, 2009)
- Multivariate / multidimensional extension of FNN (Kennel et al., 1992)
- Matlab functions mdDelay and mdFnn (mdembedding GitHub package)
- Lorenz system as test data
- MdRQA / MdCRQA parameter estimation
- 1/e threshold criterion; first-local-minimum criterion; Rtol / Atol distance criteria

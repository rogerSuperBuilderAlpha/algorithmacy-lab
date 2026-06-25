---
citekey: hidaka2018fast
title: Fast and exact search for the partition with minimal information loss
authors: Hidaka, Shohei and Oizumi, Masafumi
year: 2018
doi: 10.1371/journal.pone.0201126
arxiv: null
journal: PLOS ONE
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0201126&type=printable
sha256: 99480746f209589213793d14d834a3ab0694c5df692d48f5c11c061122f21ab5
pdf_path: literature/pdfs/hidaka2018fast.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to identify the Minimum Information Partition (MIP) of a multi-component system, i.e., the way of splitting the system into parts that minimizes the information lost by the split. An exhaustive search for the MIP is intractable because the number of possible bi-partitions grows exponentially with system size N. The authors show that when the information-loss measure is submodular, the MIP can be found in polynomial time. They prove that mutual information between the two parts is a symmetric submodular function, which lets them apply Queyranne's algorithm to find the exact bi-partition MIP in O(N^3) time, and they extend the framework to exact k-partition search at cost O(N^{3(k-1)}). Numerical case studies confirm that the submodular search matches the exhaustive search's correct MIPs (for N up to 16), scales cubically, and recovers underlying block structure in a system-wise correlation toy example and in coupled-map-lattice nonlinear oscillator networks. The method makes MIP-based analysis feasible for systems with roughly 100 channels typical of multi-unit recordings, EEG, and ECoG.

## Key facts it relies on
- The number of possible bi-partitions for a system of size N is 2^{N-1} - 1, which grows exponentially; exhaustive search is intractable even for modest N (~40).
- The information-loss function is defined as the mutual information between the two parts, f(M) := I(M; M-bar) = H(M) + H(M-bar) - H(M, M-bar).
- Mutual information is shown to be a symmetric submodular function (submodularity proven via submodularity of Shannon entropy; symmetric because f(M) = f(V\M)).
- Queyranne's algorithm [12] precisely identifies the minimum-information-loss bi-partition in O(N^3) computational time for a symmetric submodular function.
- The authors extend Queyranne's algorithm to exact k-partition (k > 2) with computational cost reduced to O(N^{3(k-1)}).
- Under a Gaussian (normal) data assumption, the loss takes the closed form f(M) = log2|Σ_M| + log2|Σ_M-bar| - log2|Σ_X|, and the |Σ_X| term can be omitted since it is constant across the search.
- Study 1 (computational time): 10,000 points in N-dimensional space for N = 2,3,...,400; exhaustive search ran only up to N = 16; submodular search matched the correct MIPs up to N = 16; exhaustive time fit log2(T) = 0.891N - 12.304 (≈ O(2^N)) while Queyranne's fit log2(T) = 3.210 log2(N) - 18.722 (≈ O(N^3)); at N = 1000 Queyranne's search took 9738 seconds; at N = 40 exhaustive is estimated at 1.07×10^7 sec (≈123 days) vs ~1 sec for Queyranne's.
- Study 2 (toy example): 40 variables built so variables {1,...,20} and {21,...,40} form two positively-correlated subsets with near-zero cross-correlation (constructed via SVD with λ = 0.1); MIP search recovered the expected bipartition.
- Study 3 (nonlinear systems): Coupled Map Lattice (logistic map f_a(x)=1-ax^2, a=1.8950, ε=0.1) with N=30 and an added connection parameter δ between variables 20 and 21; the probability of finding the expected partition is a decreasing function of δ, and at δ=1/2 the system splits in the middle ({1,...,15} and {16,...,30}).
- A prior study by Narasimhan et al. [15] proposed essentially the same Queyranne-based algorithm for bi-partition of mutual information; this paper claims advancement by adding the exact k-partition algorithm and the explicit connection to MIP in Integrated Information Theory (IIT).

## Critical notes from the literature
- The MIP concept originates from IIT [9-11], where information loss is quantified by "integrated information," which differs from the mutual information used here; the authors keep the term "MIP" but acknowledge the measure of information loss is different.
- The method's polynomial guarantee depends on the loss function being submodular; the authors note that proposed measures of integrated information are not all known to be submodular, and assessing their submodularity (or treating the algorithm as an approximation) is left as future work.
- Normalized integrated information, used in earlier IIT to fairly compare partitions, is not submodular; the authors explicitly did not consider normalization, leaving it as an open question whether the algorithm works as a good approximation under normalization [26].
- The Gaussian/normality assumption is used for computational feasibility; in the CML data most variables were not exactly normal (Kolmogorov-Smirnov test), but the normal-based and histogram-based mutual-information estimates correlated highly (0.9552 across 435 variable pairs), supporting the approximation.
- The paper acknowledges a prior study [15] proposing essentially the same bi-partition algorithm, positioning its own contributions as the k-partition extension and the conceptual link to IIT rather than the core bi-partition method.

## Key topics covered
Minimum Information Partition (MIP); Minimum Information Bipartition; submodular functions and submodular optimization; symmetric submodular functions; Queyranne's algorithm; mutual information as information-loss measure; Shannon entropy; KL divergence; Integrated Information Theory (IIT); integrated information; k-partition extension; Gaussian/normal closed-form mutual information; covariance determinant; computational complexity (O(N^3), O(2^N), O(N^{3(k-1)})); Coupled Map Lattice; logistic map; nonlinear oscillators; neural data analysis (multi-unit recordings, EEG, ECoG).

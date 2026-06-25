---
citekey: kitazono2018efficient
title: Efficient Algorithms for Searching the Minimum Information Partition in Integrated Information Theory
authors: Kitazono, Jun and Kanai, Ryota and Oizumi, Masafumi
year: 2018
doi: 10.3390/e20030173
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1712.06745
sha256: e026347096f87f40ba4dd4db1525e36882993c2f2388f1e3e256ecc70768ea55
pdf_path: literature/pdfs/kitazono2018efficient.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses the combinatorial explosion of finding the Minimum Information Partition (MIP) in Integrated Information Theory (IIT): the MIP is the bipartition at which integrated information (Φ) is minimized, and exhaustively searching it is exponential in system size because the number of bipartitions of an N-element system is 2^(N-1) - 1. Prior work (Hidaka and Oizumi) showed that when Φ is submodular, the MIP can be found in polynomial time using Queyranne's algorithm for symmetric submodular functions, but only the first-version mutual-information measure (Φ_MI) is submodular while the later measures stochastic interaction (Φ_SI) and geometric integrated information (Φ_G) are not. The authors empirically test how well Queyranne's algorithm finds the MIP for the two non-submodular measures, using simulated autoregressive (Gaussian) networks and macaque ECoG data, and benchmark it against a Replica Exchange Markov Chain Monte Carlo (REMCMC) method. They find Queyranne's algorithm identifies the MIP nearly perfectly even for the non-submodular measures: a 100% correct rate for Φ_SI and 97-100% for Φ_G in the simulations, with computational time scaling polynomially (roughly N^3.066 for Φ_SI and N^4.776 for Φ_G) rather than exponentially. The conclusion is that submodular optimization can be practically extended to non-submodular Φ measures, enabling Φ computation across the MIP in real neural systems of around 100 channels.

## Key facts it relies on
- The number of bipartitions of an N-element system is 2^(N-1) - 1, so exhaustive MIP search grows exponentially with system size.
- Hidaka and Oizumi previously reduced the cost of finding the MIP to O(N^3) by using Queyranne's submodular optimization algorithm with mutual information, which is submodular; the first version of IIT (IIT 1.0) is based on mutual information.
- The paper considers three measures of integrated information: mutual (multi) information Φ_MI, stochastic interaction Φ_SI, and geometric integrated information Φ_G; Φ_MI is strictly submodular but Φ_SI and Φ_G are not.
- There is an order relation among the three measures: Φ_G ≤ Φ_SI ≤ Φ_MI (Eq. 12).
- Integrated information across a bipartition Φ(S) is a symmetric set function because S and Ω\S specify the same bipartition; Queyranne's algorithm finds the minimum of a symmetric submodular function in O(N^3) function calls.
- In simulated AR-model networks (N = 14, 100 connectivity matrices per setting), the correct rate of finding the MIP was 100% for Φ_SI in all settings and 100% (Normal model) or 97% (Block model) for Φ_G; averaged rank in block-model error trials was 1.03-1.05, and error ratios were very small (around 0.1 in error trials).
- Measured computational time scaled as log10(T) = 3.066 log10(N) - 3.838 for Φ_SI and log10(T) = 4.776 log10(N) - 4.255 for Φ_G (Queyranne), versus exponential exhaustive search (T ∝ 1.929^N for Φ_SI, T ∝ 2.057^N for Φ_G); at N = 100, Queyranne's algorithm for Φ_SI takes ~197 sec while exhaustive search takes 1.16 × 10^25 sec.
- In comparisons against REMCMC (Φ_SI at N=50, Φ_G at N=20, 20 matrices per setting), the partitions found by Queyranne's algorithm and REMCMC exactly matched in all trials; Queyranne's used a fixed number of Φ evaluations (e.g., 41,699 for N=50) much smaller than REMCMC's convergence count.
- Real-data validation used macaque ECoG (Neurotycho.org, monkey "Chibi"): 128-channel electrodes reduced to 64 by bipolar re-referencing, 100 Hz down-sampling; on 100 random 14-electrode subsets Queyranne's algorithm gave 100% correct rate for both Φ_SI and Φ_G, and matched REMCMC on all 15 one-minute segments of the 64-channel data.

## Critical notes from the literature
- The authors stress it is not theoretically guaranteed that Queyranne's algorithm finds the MIP for the non-submodular measures Φ_SI and Φ_G; the near-perfect performance is only empirically demonstrated on limited simulated and real data, so they recommend validating accuracy against exhaustive search (small subsets) and against REMCMC (larger subsets) before trusting it on new data.
- Queyranne's algorithm worked slightly better for Φ_SI than Φ_G, attributed to Φ_SI being closer to the strictly submodular Φ_MI in the order relation; in block-structured models the algorithm's error-trial partitions were markedly different (one-vs-all instead of the true half-and-half MIP).
- For very large systems (N ≳ 100), the O(N^3) complexity becomes computationally demanding and Queyranne's algorithm may not be practical; REMCMC could be better if a heuristic early-stopping criterion were available, though defining such a criterion is non-trivial.
- The work focuses only on bipartitions; extension to K-partitions has complexity O(N^(3(K-1))) and there is no established way to fairly compare partitions of different K. Normalization of integrated information (as in IIT 2.0) remains an open question and can break submodularity even for Φ_MI.
- The method finds the MIP but does not solve identifying the "complex" (the subnetwork maximizing integrated information, hypothesized locus of consciousness), which cannot be formulated as submodular optimization; the three measures also differ in what they quantify (Φ_G captures only causal interactions, Φ_SI and Φ_MI also equal-time interactions), requiring care in interpretation.

## Key topics covered
- Integrated Information Theory (IIT) and the level-of-consciousness hypothesis
- Minimum Information Partition (MIP) as a set-function optimization problem
- Measures of integrated information: multi/mutual information Φ_MI, stochastic interaction Φ_SI, geometric integrated information Φ_G
- Submodularity of set functions and Queyranne's algorithm for symmetric submodular minimization
- Replica Exchange Markov Chain Monte Carlo (REMCMC / parallel tempering) for MIP search
- Autoregressive (AR) Gaussian network models; Wishart-distributed noise covariance
- Computational complexity and scaling (polynomial vs exponential)
- Application to macaque ECoG neural data (Neurotycho)
- Kullback-Leibler divergence formulation of integrated information; disconnected probability distributions

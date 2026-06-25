---
citekey: schreiber2000measuring
title: Measuring Information Transfer
authors: Schreiber, Thomas
year: 2000
doi: 10.1103/PhysRevLett.85.461
arxiv: null
journal: Physical Review Letters
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/nlin/0001042
sha256: 7f1ac77dbdabe04d2dc6039c28aa8bc15ce826f1f70d06d228873e3aebfb2e63
pdf_path: literature/pdfs/schreiber2000measuring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to quantify the directed exchange of information between two time-evolving systems when neither the systems nor their coupling can be assumed deterministic. It argues that standard (time-delayed) mutual information is symmetric and conflates information that is genuinely exchanged with shared information arising from common history or common input. Schreiber introduces a new information-theoretic measure, transfer entropy, defined as a Kullback entropy that measures the deviation from a generalized Markov property: it asks whether including the past of process J changes the transition probabilities of process I. By appropriate conditioning of transition probabilities, transfer entropy becomes explicitly non-symmetric, distinguishing driving from responding elements and detecting coupling asymmetry. The method is demonstrated on a unidirectionally coupled tent-map lattice (analytic lowest-order result), an Ulam-map lattice, and a bivariate physiological time series (breath rate and heart rate of a sleeping human). In each case transfer entropy correctly recovers the direction of coupling and ignores static correlations that mislead mutual information.

## Key facts it relies on
- Transfer entropy is defined as TJ→I = Σ p(i_{n+1}, i_n^(k), j_n^(l)) log [ p(i_{n+1}|i_n^(k), j_n^(l)) / p(i_{n+1}|i_n^(k)) ], a Kullback entropy measuring deviation from the generalized Markov property p(i_{n+1}|i_n^(k)) = p(i_{n+1}|i_n^(k), j_n^(l)) (Eq. 4).
- The measure is built on Shannon entropy H_I = -Σ p(i) log2 p(i), Kullback entropy K_{I|J} = Σ p(i,j) log p(i|j)/q(i|j), and the entropy rate h_I = H_{I^(k+1)} - H_{I^(k)}.
- Mutual information M_IJ = Σ p(i,j) log [p(i,j)/(p(i)p(j))] = H_I + H_J - H_IJ ≥ 0 is symmetric under exchange of I and J and so carries no directional sense; it can only be given direction ad hoc via a time lag τ.
- The most natural choices for the embedding parameter are l = k or l = 1, with l = 1 usually preferable for computational reasons; transition probabilities are estimated by kernel/correlation-integral methods using a step kernel Θ(x>0)=1, Θ(x≤0)=0.
- For coarse-grained continuous systems, lim_{ε→0} T_{Y→X}(ε) is finite and partition-independent except under deterministic coupling, where it diverges as ε → 0 (analogous to mutual information's behavior).
- Tent-map lattice (Eq. 5, x_{n+1}^m = f(ε x_n^{m-1} + (1-ε) x_n^m)): in lowest order of ε with k = l = 1, T_{I^{m-1}→I^m} = α^2 ε^2 / ln(2) + O(ε^4); Figure 1 fits α = 0.77, using 100 maps, averages of 10 runs of 10^5 iterates after 10^5 transients. The reverse direction T_{I^m→I^{m-1}} stays zero.
- Ulam map f(x) = 2 - x^2: lattice of 100 points, 10000 iterates recorded after 10^5 transients, correlation sums at r = 0.2, k = l = 1, neighbors closer than 100 iterates excluded. Near ε = 0.18 (spatial/temporal period two) mutual information equals 1 bit (a static correlation artifact) while transfer entropy correctly reports zero transport; near ε = 0.82 (fixed point) both measures show zero transfer; the negative direction of T stays consistent with zero for all couplings.
- The physiological example uses the breath rate and instantaneous heart rate of a sleeping human with sleep apnea (Santa Fe Institute 1991 time series contest, data set B), sampled at 2 Hz, normalized to zero mean and unit variance; transfer entropy shows stronger flow from heart rate to breath rate than the reverse, while time-delayed mutual information M(τ = 0.5 s) is almost symmetric.

## Critical notes from the literature
- The author notes that for small r the physiological transfer-entropy curves "deflect down to zero due to the finite sample size," and that observed directionality could instead reflect both signals responding to a common external trigger — directional inference is not proof of mechanism.
- Excluding the influence of a known common driving force Z requires conditioning the probabilities on z_n as well; the paper states that conditioning with respect to a large number of variables "poses immense numerical problems," so the spatio-temporal common-history study (resolving an apparent super-luminal information-velocity paradox, ref. [8]) is only "preliminary" and deferred.
- The generalization to order-q correlation integrals is attractive (q = 2 is computationally cheapest) but the paper acknowledges that for q = 2 one "would have to give up positivity of T_{I→J}," so a direct realization of definition (4) by summing over realizations is proposed instead.
- The continuum limit ε → 0 is not obtainable in practice and must be replaced by studying T as a function of resolution or fixing a resolution; fixed-box partitions are only suitable when data are cheap to produce.
- The method assumes (approximate) stationarity and a finite-order Markov approximation; the choice of embedding (k, l), kernel, norm, and resolution are user-set and influence estimates.

## Key topics covered
Transfer entropy; mutual information; time-delayed mutual information; Shannon entropy; Kullback entropy; conditional entropy; entropy rate; Kolmogorov-Sinai entropy; generalized Markov property; transition probabilities; directional/asymmetric coupling detection; generalized synchronization; coarse graining and partitions; correlation integrals / kernel density estimation; coupled map lattices (tent map, Ulam map); physiological time series (heart rate, breath rate, sleep apnea); information transport velocity in spatio-temporal systems.

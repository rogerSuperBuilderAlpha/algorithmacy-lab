---
citekey: tononi2003measuring
title: Measuring information integration
authors: Tononi, Giulio and Sporns, Olaf
year: 2003
doi: 10.1186/1471-2202-4-31
arxiv: null
journal: BMC Neuroscience
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://bmcneurosci.biomedcentral.com/counter/pdf/10.1186/1471-2202-4-31
sha256: 16bcbc50604d9d1f2bd34367d7b271a5039de08c171d92e1fee32f92130bda7d
pdf_path: literature/pdfs/tononi2003measuring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to quantify the capacity of a distributed network (such as the brain) to integrate information, as opposed to merely transmit, encode, or store it. It introduces a measure based on "effective information" (EI), defined for a bipartition of a subset by injecting maximum-entropy noise into the outputs of one part (A) and measuring the resulting entropy of the other part (B) via mutual information; EI captures all causal interactions that can occur across the partition. The capacity to integrate information, Φ, is defined as the (normalized) effective information across the minimum information bipartition of a subset, and subsets that can integrate information and are not contained in a larger higher-Φ subset are called "complexes." Applying this analysis to idealized linear (Gaussian) neural systems of small size (n ≤ 12), the authors show Φ is maximized when each element has a different (specialized) connection pattern while a large amount of information can still be exchanged across any bipartition (integration). They find that homogeneous networks lose specialization and strongly modular networks lack integration, so both yield low Φ, and that randomly connected networks underperform optimized ones under realistic constraints (sparseness, noise). They conclude that architectures like the thalamocortical system are well suited to information integration whereas the cerebellum (strongly modular) is not, with implications for which neural substrates support consciousness.

## Key facts it relies on
- Effective information is defined as EI(A→B) = MI(A^Hmax : B), where maximum-entropy noise (Hmax) is injected into A's outputs; EI is generally not symmetric (EI(A→B) ≠ EI(B→A)), and for a bipartition EI(A⇌B) = EI(A→B) + EI(B→A).
- Φ(S) = EI(MIB(S)), the effective information at the minimum information bipartition; the MIB is the bipartition for which normalized effective information EI(A⇌B)/min{Hmax(A), Hmax(B)} reaches a minimum.
- A subset S with Φ > 0 is a "complex" if it is not included within a subset of higher Φ; the complex with maximum Φ is the "main complex." This quantity is also called MIBcomplexity.
- The illustrative example uses a system of n = 8 elements with two fully interconnected modules (elements 1–4 and 5–7) plus common input from element 8; an exhaustive search over subsets of sizes k = 2,...,8 examined 247 individual subsets and recovered three complexes: {1,2,3,4} (Φ = 20.7954), {5,6,7} (Φ = 20.1023), and the whole system {1,...,8} (Φ = 7.4021).
- Systems were implemented as stationary multidimensional Gaussian processes; the connection matrix CON(X) was normalized so total absolute afferent synaptic weight per element was constant (w < 1, typically w = 0.5); high SNR was set by cp = 1, ci = 0.00001 and low SNR by cp = 1, ci = 0.1.
- Optimized networks at high SNR reached Φ = 73.6039 ± 0.5352 (343 runs) for nonlinear constrained optimization, with sparse-optimized networks giving Φ = 60.7598 and randomly wired sparse networks much lower (Φ = 35.6622 ± 5.0382, 100 exemplars); at low SNR Φ = 5.7454 ± 0.1189 (21 runs).
- Homogeneous fully connected networks (CONij = 0.072, matching index = 1) gave low Φ = 20.5203 versus 73.6039 for optimized; a strongly modular network (four modules, intra CONij = 0.25, inter CONij = 0.0417) gave Φ = 20.3611 per module and only Φ = 19.4423 for the whole.
- Basic digraphs: a directed path gave Φ = 10.1266, a one-way cycle Φ = 20.2533, a two-way cycle Φ = 40.5065, and fan-out and fan-in digraphs Φ = 10.8198.
- Joining two optimized n = 8 components (each Φ = 60.7598) via 8 pairs of reciprocal connections gave Φ = 109.5520 for the n = 16 system, exceeding random networks of size 16 (Φ = 51.5930 ± 5.2275, 10 exemplars); Φ reached a maximum ≈ 109.6334 at an intra- to inter-modular coupling ratio of 2:3.
- The covariance matrix is derived analytically via X = X*CON(X) + cR, Q = (1−CON(X))^−1, giving COV(X) = Qt * Q; H(A) = (1/2)ln[(2πe)^n |COV(A)|] and MI(A:B) = H(A) + H(B) − H(AB).

## Critical notes from the literature
- The authors state most results were obtained on systems of a small number of elements (n ≤ 12) and that further work is required to determine whether they apply to larger systems; it is not clear whether the highest Φ always comes from optimizing connections among all elements once noise, connection strength, and dynamic range are considered.
- They note the approach is built on equilibrium linear (Gaussian) systems with predefined elementary units and no temporal evolution, whereas real brains are highly non-linear and constantly interacting with the environment; factors like firing rates, synaptic efficacy, and behavioral state can radically alter information integration even with fixed anatomy.
- A practical limitation is the combinatorial cost: exhaustive measurement of Φ is feasible only for up to about two dozen elements (subsets and bipartitions grow factorially), and the method requires perturbing the system in all possible ways rather than just observing it.
- The paper distinguishes Φ from the authors' earlier neural complexity (CN) and functional clustering index (CI): CN captures average integration but is insensitive to whether a system is a single integrated entity or independent channels, and CI, being based on statistical comparison to a null hypothesis, cannot detect whether elements are merely correlated (e.g. via common input) versus causally interacting.
- The interpretive extension to consciousness (thalamocortical system as substrate, cerebellum as non-contributing) is presented as a hypothesis consistent with the analysis, not a demonstrated result.

## Key topics covered
Effective information; information integration; Φ (phi); minimum information bipartition (MIB); complexes and main complex; MIBcomplexity; mutual information and entropy; Gaussian/linear stochastic models; covariance matrix derivation; functional specialization vs. integration; homogeneous, modular, and random network architectures; SNR (perturbation/intrinsic noise coefficients); basic digraphs (paths, cycles, fan-in, fan-out); joining/scaling complexes; matching index; neural complexity (CN) and functional clustering (CI); thalamocortical system; cerebellum; cortico-subcortical loops; consciousness; nonlinear constrained optimization and evolutionary graph selection.

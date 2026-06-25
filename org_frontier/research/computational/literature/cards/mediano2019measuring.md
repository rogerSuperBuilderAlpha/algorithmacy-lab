---
citekey: mediano2019measuring
title: Measuring Integrated Information: Comparison of Candidate Measures in Theory and Simulation
authors: Mediano, Pedro A. M. and Seth, Anil K. and Barrett, Adam B.
year: 2019
doi: 10.3390/e21010017
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1806.09373
sha256: b024d5b2c1ad86936527b211e7593cea2050deaa3893ea61fdc5b2fb54af993e
pdf_path: literature/pdfs/mediano2019measuring.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper asks how the several existing candidate measures of integrated information ("Φ") compare, since little was known about how they behave on non-trivial network models. It provides unified, intuitive descriptions of six distinct measures — whole-minus-sum integrated information Φ, integrated stochastic interaction Φ̃, integrated synergy ψ, decoder-based integrated information Φ*, geometric integrated information Φ_G, and causal density (CD) — all based on a system's spontaneous information dynamics rather than perturbation. It then simulates these measures on networks of up to eight nodes animated by Gaussian linear autoregressive (AR) dynamics, varying coupling strength, topology, connection density, and noise-input correlation. The authors find striking diversity in behaviour: no two measures show consistent agreement across all analyses, and only a subset (ψ, Φ*, and CD) appear to genuinely reflect dynamical complexity in the sense of co-existing segregation and integration. Φ behaves erratically and can go negative when nodes are strongly correlated, while Φ̃ mostly tracks noise-input correlation and Φ_G mostly tracks coupling strength. The results are offered to guide operationalisation of IIT and motivate continued development of ψ, Φ*, and CD as theoretically sound and empirically adequate measures.

## Key facts it relies on
- The paper reviews six measures with distinct origins: whole-minus-sum Φ [Barrett & Seth, ref 11; Balduzzi & Tononi ref 5], integrated stochastic interaction Φ̃ [ref 11], integrated synergy ψ [ref 19], decoder-based Φ* [Oizumi et al., ref 35], geometric Φ_G [Oizumi et al., ref 37], and causal density CD [ref 39].
- All measures except CD were inspired by Balduzzi and Tononi's Φ_2008, which is based on information the current state contains about a hypothetical maximum-entropy past state and is applicable only to discrete Markovian systems; the paper instead builds all measures on spontaneous information dynamics p(X_t, X_{t−τ}), making them well-defined for any stochastic system with a Lebesgue measure across states.
- Table 2 establishes property differences: e.g. Φ is not non-negative (it can be negative), whereas Φ̃, ψ, Φ*, Φ_G, and CD are non-negative; Φ, Φ̃, Φ_G are time-symmetric while ψ, Φ*, CD are not; only Φ, Φ̃, CD have closed-form expressions in discrete and Gaussian systems (ψ, Φ*, Φ_G do not have closed form in general / require numerical optimisation).
- Integrated information is defined as effective information beyond the minimum information partition (MIP), P_MIP = arg min_P f[X;τ,P]/K(P), with normalisation coefficient K(P); Balduzzi & Tononi suggest K(P) = (r−1) min_k H(M_t^k). All reported results minimise unnormalised effective information over even-sized bipartitions to avoid conflating partition-search effects with the measure itself.
- Simulations use order-1 stochastic linear AR processes X_{t+1} = A X_t + ε_t with zero-mean Gaussian noise; a process is stable/stationary if the spectral radius of A is less than 1. Φ measures are computed from stationary statistics via the discrete-time Lyapunov equation Σ(X_t) = A Σ(X_t) A^T + Σ(ε_t).
- For the two-node network with A having all entries a and noise correlation c, setting a=0.4 reproduces the model in Fig. 3 of Ref. 35; as c→1 the system becomes degenerate, Φ̃ diverges to infinity, Φ becomes negative for large enough c, while ψ, Φ*, CD decrease monotonically to 0; TDMI and Φ_G are unaffected by noise correlation.
- On a suite of six eight-node networks (fully connected, Φ-optimal binary, Φ-optimal weighted, bidirectional ring, small-world, unidirectional ring) normalised to spectral radius 0.9, the unidirectional ring is consistently judged most complex by all measures except Φ̃, and the fully connected network consistently least complex; control measures used are time-delayed mutual information (TDMI) I(X_{t−τ};X_t) and average absolute correlation Σ̄.
- Although the measures often disagree on specific values, TDMI, Φ_G, Φ*, and ψ show remarkable alignment in their relative ranking of network complexity (Table 3); however the Spearman correlation between these measure rankings and the small-world-index ranking is around −0.4.
- On Erdős–Rényi random networks parametrised by density ρ and noise correlation c (50 networks per point, spectral radius 0.9), all integrated information measures except Φ_G show a band of high value at intermediate ρ; plotting against average correlation Σ̄, the measures Φ*, ψ, Φ_G, and CD peak at intermediate Σ̄, supporting them as valid complexity measures, while the Σ̄ histogram confirms the peaks are not sampling artefacts.

## Critical notes from the literature
- The authors state Φ is often regarded as a poor measure because it can be negative; across all their simulations its behaviour is erratic, "undermining prospects for empirical application," and this is even more prevalent when Φ is optimised over all bipartitions rather than even bipartitions.
- The paper notes the measures studied use the empirical/spontaneous stationary distribution rather than the maximum-entropy distribution central to IIT versions 2 and 3 (refs 5, 34); they caution one must remain cautious about treating these measures as generalisations or approximations of the proposed "fundamental" Φ measures, since they measure dynamics rather than mechanism.
- Scope is limited to continuous Gaussian linear AR systems; the authors flag that non-Gaussian continuous systems (e.g. exponentially distributed neural spiking) and discrete systems should be examined in future work, and that there is no uniquely defined maximum-entropy distribution for unbounded continuous variables.
- The authors restrict partition search to even-sized bipartitions to avoid normalisation-factor instabilities; they note uneven partitions require normalisation factors known to introduce instabilities, and that fuller partition search (all partitions) costs O(n^n) (Bell number) vs O(2^n) for bipartitions and O(n^2) for even bipartitions, leaving choice of MIP definition as an open issue.
- The relation between the validated measures (Φ*, ψ, Φ_G, CD) "remains unclear and not always consistent" across scenarios; the authors also correct an error in the previously published Φ* Gaussian formula of Ref. 35 (Appendix A.1).

## Key topics covered
Integrated Information Theory (IIT); candidate Φ measures; whole-minus-sum Φ; integrated stochastic interaction Φ̃; integrated synergy ψ; decoder-based Φ* / mismatched decoding information; geometric integrated information Φ_G; causal density / transfer entropy; minimum information partition (MIP); effective information; dynamical complexity (integration vs segregation); Gaussian linear autoregressive (AR) models; spontaneous vs maximum-entropy distributions; partial information decomposition (PID) and redundancy; eight-node network topologies; Erdős–Rényi random networks; Lyapunov equation for stationary covariance; time-delayed mutual information; partition-search computational complexity.

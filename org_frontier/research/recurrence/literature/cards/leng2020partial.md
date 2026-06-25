---
citekey: leng2020partial
title: Partial cross mapping eliminates indirect causal influences
authors: Leng, Siyang and Ma, Huanfei and Kurths, J{\"u}rgen and Lai, Ying-Cheng and Lin, Wei and Aihara, Kazuyuki and Chen, Luonan
year: 2020
doi: 10.1038/s41467-020-16238-0
arxiv: null
journal: Nature Communications
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41467-020-16238-0.pdf
sha256: ed4287d5f3e1f20095cef90b1c35e0c110896a9b06565cc34b4cf55b0b4703cc
pdf_path: literature/pdfs/leng2020partial.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses a long-standing problem in causality detection from time series: indirect causal influences are frequently misidentified as direct ones because of causation transitivity, and existing remedies (partial transfer entropy, conditional Granger causality) fail when the dynamical variables are non-separable, i.e. the information of one variable cannot be cleanly removed from the others (a generic feature of nonlinear deterministic systems under Takens-Mañé embedding). The authors propose Partial Cross Mapping (PCM), a data-based, model-free method that integrates three tools: delay-coordinate phase-space reconstruction, mutual cross mapping (MCM), and partial correlation. The core idea is to compare a time series with its cross-map prediction from another while conditioning out the component that flows through a third (mediating) variable, yielding a direct-causation index ϱD that is the projection of the standard MCM index ϱC onto the subspace orthogonal to the indirect information flow. On a three-species logistic benchmark with chain and loop structures, PCM (threshold T = 0.5) correctly discards the false indirect links that MCM flags as direct. Applied to real-world systems, PCM reconstructs DREAM4 gene regulatory networks (average AUROC ~0.75), recovers the direct prey-predator links in a Baltic Sea plankton food chain (excluding the indirect Pico cyanobacteria → Cyclopoids link), and identifies NO2 and respirable suspended particulates (not SO2 or ozone) as the direct causes of Hong Kong cardiovascular disease admissions. The method is framed as filling a gap in causality analysis for non-separable nonlinear networked systems.

## Key facts it relies on
- PCM combines three components — Takens-Mañé delay-coordinate embedding (refs 40,41), mutual cross mapping / MCM (Sugihara et al. Science 2012, ref 17; Ma et al. ref 20), and partial correlation (refs 44,64) — to detect direct causal links while removing indirect ones.
- The MCM index is ϱC = |Corr(X, X̂^Y)| (cosine of the angle between X and its cross-map estimate X̂^Y); the PCM index is ϱD = |Pcc(X, X̂^Y | X̂^Ẑ^Y)|, the partial correlation conditioning on the indirect information flow through Z. Generally ϱC ≥ ϱD.
- With an empirical threshold 1 > T ≫ 0, three cases distinguish causal relations: ϱC ≥ ϱD ≥ T (direct link X→Y), ϱC ≥ T ≫ ϱD (sole indirect link), and T > ϱC ≥ ϱD (no causal link). A proximity ratio γ = ϱD/ϱC is introduced to handle marginal cases near T.
- The number of nearest neighbors used per cross-map is Eξ + 1 (minimum for a bounded simplex in an Eξ-dimensional space, ref 43); embedding dimensions and time lags are chosen via false nearest neighbor (FNN) and delayed mutual information (DMI).
- Benchmark: three interacting species (logistic-type maps) with αx = 3.6, αy = 3.72, αz = 3.68 and additive white noise of zero mean, standard deviation 0.005. At T = 0.5, for the chain and loop modes the MCM index stays above T (false direct: e.g. ϱC = 0.8681, 0.8052) while PCM correctly yields ϱD = 0.1871 and 0.4467 (below T), reconstruction parameters E = 4, τ = 1, averaged over 100 trials of length 1000 drawn from 5000-length series (1 Hz sampling).
- DREAM4 in silico Network Challenge (refs 53-55): five networks of 100 genes each; 20 interacting genes selected via GeneNetWeaver (ref 56), each gene with 10 realizations of 21-length expression series; PCM AUROCs were 0.7907, 0.6543, 0.7353, 0.6639, 0.8629 (average ~0.75), with reconstruction parameters E = 2, τ = 1.
- Plankton food chain (Pico cyanobacteria, Rotifers, Cyclopoids) from an 8-year Baltic Sea mesocosm experiment (refs 57-59): PCM recovers the true direct links (E = 4, τ = 1), excludes the indirect Pico→Cyclopoids link, and even detects a weak direct Rotifers→Pico cyanobacteria link; significance p < 0.0016.
- Hong Kong air-pollution / cardiovascular admissions data 1994-1997 (refs 60-62, E = 7, τ = 1): PCM identifies nitrogen dioxide and respirable suspended particulates as the major direct causes of cardiovascular disease, not SO2 or ozone, consistent with prior results (refs 20,63); p < 10^-9.
- The non-separability argument rests on Takens-Mañé embedding theory: a delay-coordinate map is generically an embedding provided L > 2dA (dA the box-counting attractor dimension), so the full system information can be injected into a single observed variable — which the authors argue invalidates prediction-based frameworks (Granger causality, transfer entropy) for nonlinear non-separable systems. Code is at https://github.com/Partial-Cross-Mapping.

## Critical notes from the literature
- The authors explicitly state strongly coupled (synchronized) variables are out of scope: under strong coupling the system collapses to the cause sub-manifold and bidirectional causation is always computationally detected (ref 17). PCM targets weak-to-moderate interaction.
- PCM is grounded in the Takens-Mañé theorem, which applies only to autonomous systems; data entirely from nonautonomous systems are not directly suitable (ref 48). The authors note partial workarounds (switching systems with long durations; forced/weak-or-moderate-noise systems via generalized embedding theorems, refs 49,50) and recommend dynamical Bayesian inference (ref 14) for time-evolving coupled oscillators.
- The Hong Kong result is qualified by the authors: detected bidirectional relations among pollutants may be direct or indirect because confounders (temperature, humidity, wind speed) are unavailable and could act as common (fan-out) causes.
- For large networks the partial-correlation conditioning set becomes computationally problematic; the paper proposes heuristic node-selection (conditioning on Zi maximizing ϱC^{X→Zi} + ϱC^{Zi→Y}) and only implements the first-order PCM in this work, deferring higher-order methods to future work.
- The paper concedes that causality in nonlinear dynamical systems departs from the interventionist statistical definition (X causes Y iff intervening on X affects Y), interpreting it instead as a coupling term in the system equations; fuller theoretical formalization is left to future work.

## Key topics covered
Partial cross mapping (PCM); convergent/mutual cross mapping (MCM, CCM); causation transitivity; direct vs indirect causal links; non-separability; Takens-Mañé delay-coordinate embedding; shadow manifolds; partial correlation coefficient; Granger causality and transfer entropy (as contrasted baselines); conditional Granger / partial transfer entropy; gene regulatory network inference (DREAM4, GeneNetWeaver); plankton food-web causality; air pollution and cardiovascular disease causality; network motifs (fan-in, fan-out, cascading); FNN and DMI parameter selection; ROC/AUROC evaluation; multiple-testing corrections.

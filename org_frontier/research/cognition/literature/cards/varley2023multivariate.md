---
citekey: varley2023multivariate
title: Multivariate information theory uncovers synergistic subsystems of the human cerebral cortex
authors: Varley, Thomas F. and Pope, Maria and Faskowitz, Joshua and Sporns, Olaf
year: 2023
doi: 10.1038/s42003-023-04843-w
arxiv: null
journal: Communications Biology
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s42003-023-04843-w.pdf
sha256: 7c152a78b25c9604571e989ffc334266204e51e2038899ec58c48bab312b040f
pdf_path: literature/pdfs/varley2023multivariate.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Standard functional connectivity models the brain as a network of pairwise interactions and is therefore blind to higher-order (three-or-more-region) statistical dependencies. The paper asks whether multivariate information theory, specifically the O-information of Rosas et al., can reveal such higher-order structure in resting-state fMRI, and what its neural manifestations are. The authors first derive an analytic and geometric relationship between the O-information and older complexity measures, notably the Tononi-Sporns-Edelman (TSE) complexity, showing that synergy (negative O-information) corresponds to integration present in the whole but not in subsets, i.e. cases where removing any single element decreases integration more than expected. Applying Gaussian estimators to two resting-state fMRI datasets (HCP and MICA-MICs), they find the full 200-node system is redundancy-dominated (positive O-information), but abundant smaller subsets (3-16 nodes by random sampling; up to ~25-27 by optimization) express synergy. Using simulated annealing to find maximally synergistic subsets, minimal O-information is achieved at subsets of roughly 10 regions, which are recruited from multiple canonical functional systems and sit between them. Synergistic subsets are widespread across the entire cortex but invisible to pairwise functional connectivity, forming a "shadow structure"; node pairs with strong (positive or negative) FC are rarely co-included in synergistic subsets. The authors argue higher-order interactions are an under-explored substrate potentially relevant to neural computation and integration.

## Key facts it relies on
- O-information Ω(X) = TC(X) − DTC(X) (total correlation minus dual total correlation); negative Ω indicates synergy-dominated structure, positive Ω indicates redundancy-dominated. For three variables it equals the co-information (redundancy minus synergy), but the identity to co-information holds directly only for three variables.
- They derive DTC(X) = N·C(X) (relating dual total correlation to the description complexity C), allowing Ω(X) = TC(X) − N·C(X), and show the exogenous/S-information Σ(X) = TC(X) + DTC(X) ∝ TSE complexity; correlations of Σ with TSE were R = 0.998 (HCP) and 0.999 (MICA), and DTC alone with TSE R = 0.982 (HCP), 0.992 (MICA), over subset sizes 3-15.
- Data: two resting-state fMRI datasets, HCP (main; 95 of 100 subjects retained, 4 runs each, mean age 29.29 ± 3.66, 56% female) and MICA-MICs (replication; 50 subjects, 1 run each); both parcellated into a common 200-node cortical scheme aligned to 7 canonical functional systems; global signal regression applied; a single aggregated FC matrix per dataset (HCP vs MICA mean FC matrices correlated R = 0.851, p = 0).
- The full 200-node FC is redundancy-dominated: Ω = 79.16 nats (HCP) and Ω = 46.69 nats (MICA).
- Random sampling of subsets (3-16 nodes) yields abundant negative-O-information subsets whose fraction drops rapidly with size (10-node subsets: 0.41% are synergistic, totaling ≈9.23 × 10^13); O-information correlates with TSE complexity in 10-node subsets (ρ = 0.642, p = 0, HCP).
- Absolute pairwise FC is strongly negatively correlated with frequency of participation in synergistic subsets (ρ = −0.504, p = 0, HCP; ρ = −0.485, MICA), so strongly-coupled node pairs rarely co-occur in synergistic subsets.
- Simulated annealing (5000 runs per subset size, sizes 3-30): maximally negative O-information is achieved for subsets of ~8-12 (≈10) nodes; no synergistic subsets are found beyond 27 nodes; nodal frequency maps correlate across datasets (ρ = 0.522, p = 2.2 × 10^−15 for optimized 10-node subsets; ρ = 0.579 for random-sample maps).
- Irreducibility (null test, removing each node by zeroing its correlations): valid (irreducibly synergistic) fractions were ≈99.08% at size 4, ≈92.92% at 6, ≈84.14% at 8, ≈64.04% at 10, ≈0.04% at 15, and zero above 15 — so synergy in large subsets is restricted to a core, not the whole.
- Functional-system distribution is uneven: frontoparietal regions participate most in synergistic 10-node subsets (limbic dominates at larger sizes); no subset drawn from a single functional system expresses synergy, and subsets spanning 6-7 canonical systems are most likely synergistic.
- Estimation uses Gaussian (closed-form) information-theoretic estimators justified by prior evidence BOLD is well-modeled as multivariate Gaussian; Barrett showed higher-order synergies can exist in purely Gaussian systems even though pairwise covariance fixes the distribution.

## Critical notes from the literature
- The authors flag that the analysis is atemporal/static: every frame is assumed drawn from an unchanging multivariate Gaussian with no dynamics or memory, and the Gaussian estimator (a function of Pearson ρ) is insensitive to nonlinear relationships; they point to information-dynamics measures (e.g. O-information rate, transfer-entropy variants) as future directions.
- Results differ from Luppi et al.'s "synergistic core": Varley et al. find synergy is widespread (could include any cortical region) rather than confined; they attribute the discrepancy to different pipelines (Luppi decomposes temporal mutual information over region pairs via PID requiring a redundancy-function choice, vs. their instantaneous, higher-order, atemporal approach) rather than a true conflict.
- BOLD confounds: the authors caution it is hard to disambiguate information reflecting neural computation from vascular physiology of the BOLD signal (citing Colenbier on synergies between global signal, blood arrival times and FC), and recommend M/EEG replication; synergy here is explicitly not claimed to be a causal/computational measure.
- Methodological/scope limits acknowledged: exhaustive subset analysis is combinatorially intractable so they rely on random sampling and simulated annealing (which can miss maximal synergy or require pre-selection heuristics); global signal regression is framed as scrubbing global redundancy that can reveal otherwise-swamped synergies (adding redundancy back hid the synergies — Supplementary Fig. 6), making GSR a consequential preprocessing choice. They also note O-information avoids PID's redundancy-function ambiguity and PID's ~5-6 element ceiling, but is a relative (redundancy-vs-synergy dominance) rather than absolute measure.

## Key topics covered
O-information; total correlation; dual total correlation; TSE (Tononi-Sporns-Edelman) complexity; description complexity C; exogenous / S-information Σ; synergy vs redundancy; higher-order interactions; partial information decomposition (contrast); functional connectivity; resting-state fMRI; HCP and MICA-MICs datasets; Schaefer 200-node parcellation; 7 canonical functional systems; Gaussian information theory / differential entropy estimators; simulated annealing optimization; irreducibility null model; global signal regression; synergistic "shadow structure"; informational morphospace.

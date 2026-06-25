---
citekey: luppi2022synergistic
title: A synergistic core for human brain evolution and cognition
authors: Luppi, Andrea I. and Mediano, Pedro A. M. and Rosas, Fernando E. and Holland, Negin and Fryer, Tim D. and O’Brien, John T. and Rowe, James B. and Menon, David K. and Bor, Daniel and Stamatakis, Emmanuel A.
year: 2022
doi: 10.1038/s41593-022-01070-0
arxiv: null
journal: Nature Neuroscience
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://static-content.springer.com/esm/art%3A10.1038%2Fs41593-022-01070-0/MediaObjects/41593_2022_1070_MOESM1_ESM.pdf
sha256: 31f4d352fcc86f65769bc38f259fd9c8ca8f7481ed3afdf28ce19e37f85566d1
pdf_path: literature/pdfs/luppi2022synergistic.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether the brain's high-order (synergistic) information interactions — as opposed to redundant ones — form a distinctive "core" that supports human cognition and reflects human brain evolution. Using Integrated Information Decomposition applied to resting-state fMRI, the authors decompose the time-delayed mutual information between every pair of brain regions into synergistic and redundant components, building separate whole-brain networks of synergy and redundancy. They test where each interaction type predominates across resting-state subnetworks and cytoarchitectonic classes, compare network properties (global efficiency, modularity) against null models, contrast humans against macaques, and relate a redundancy-to-synergy cortical gradient to meta-analytic cognitive maps, cortical expansion, synaptic density, glycolytic index, receptor diversity, and gene expression (including human-accelerated-region "HAR-Brain" genes and aerobic-glycolysis genes via partial least squares). The analysis spans human MRI (HCP), human PET of synaptic density ([11C]UCB-J), and awake macaque fMRI. The work argues that a synergistic core, concentrated in association cortex, underpins higher cognition and tracks evolutionary cortical expansion. NOTE: the supplied PDF is the article's Nature Portfolio Reporting Summary supplement (7 pages), which documents datasets, acquisition, preprocessing, and statistical methods in detail but does not reproduce the main-text abstract or numerical results; claims below are drawn from that document.

## Key facts it relies on
- Synergistic and redundant interactions were derived via Integrated Information Decomposition, decomposing the time-delayed mutual information (TDMI) between region pairs; both synergy and redundancy measures are guaranteed non-negative. Code to compute them (Java Information Dynamics Toolbox v1.5; updated MATLAB/Octave version) was released as Supplementary Information.
- Human MRI came from the Human Connectome Project (HCP) "100 unrelated subjects" (54 female, 46 males, mean age 29.1 ± 3.7 years), using minimally preprocessed fMRI denoised with CONN v17f and DWI reconstructed in DSI Studio via QSDR.
- A PET dataset of 15 healthy controls (8 female; age 68 ± 7 years) underwent simultaneous 3T MRI and [11C]UCB-J PET (90 min dynamic acquisition) to map synaptic density.
- The macaque dataset (Macaca mulatta, PRIME-DE Newcastle sample) used awake resting-state fMRI from 10 of 14 animals (12 male, 2 female; age 3.9–13.14 years); 2 animals scanned under anaesthesia were excluded a priori to match the awake human data.
- The primary parcellation was 200 cortical ROIs (Schaefer 2018) plus 32 subcortical ROIs (Tian 2020); alternative parcellations included Desikan-Killiany (68 ROIs) with 114- and 308-ROI subdivisions, Lausanne 129, Brodmann, a 40-region cytoarchitectonic atlas, and the HCP 360-ROI multimodal atlas.
- Whole-brain weighted dense networks of synergistic and redundant interactions were characterized by modularity (Newman's spectral algorithm) and global efficiency, compared to 100 random null networks whose edge weights were sampled between 0 and the pairwise TDMI.
- One-sample non-parametric t-tests (10,000 permutations) tested whether synergy-redundancy scores differed from zero for each Yeo resting-state subnetwork and each Von Economo cytoarchitectonic class; permutation t-tests compared human vs macaque; effect sizes were Hedges's g, with FDR control via Benjamini-Hochberg.
- A redundancy-to-synergy cortical gradient was tested against meta-analytic cognitive domains (NeuroSynth), HAR-Brain gene expression, chimpanzee-to-human cortical expansion, synaptic density, Glycolytic Index, and receptor diversity, with robustness via Spearman correlations and a 10,000-rotation "spin test" controlling for spatial autocorrelation.
- Partial least squares (PLS) related the gradient to all 20,647 AHBA genes across 308 regions; PLS components were validated by 1,000 label-shuffles and bootstrap resampling of the 308 ROIs, with hypothesis-driven enrichment testing for HAR-Brain and aerobic-glycolysis genes against permutation null distributions.

## Critical notes from the literature
- The supplied PDF is the Reporting Summary supplement, not the main article; quantitative effect sizes, statistical values, and figures from the main text are not present in this document and were not verifiable here.
- The study is a re-analysis of previously collected, openly available datasets; the authors state they did not use statistical methods to pre-determine sample size, relying instead on sample sizes similar to prior work (e.g., the widely-studied HCP 100-subject set).
- Sample sizes are modest and heterogeneous across modalities (100 humans for MRI, 15 for PET, 10 macaques), and the macaque sample is small and male-biased (12 of 14 male), constraining cross-species generalization.
- Cross-species and gradient comparisons rely heavily on null models and surrogate maps (random TDMI-range networks, spin tests, spatial-autocorrelation-preserving rotations) precisely because spatial autocorrelation and contralateral symmetry are acknowledged confounds for cortical map correlations.
- PET synaptic-density data are restricted-access (available from author James Rowe on reasonable request for non-commercial academic use), limiting independent reproducibility of that arm.

## Key topics covered
Integrated Information Decomposition; synergy vs redundancy; time-delayed mutual information; high-order interactions; synergistic core; redundancy-to-synergy cortical gradient; resting-state fMRI; Human Connectome Project; [11C]UCB-J synaptic-density PET; awake macaque fMRI (PRIME-DE); brain evolution and cortical expansion; human-accelerated-region (HAR-Brain) genes; aerobic glycolysis / Glycolytic Index; partial least squares gene-expression analysis (AHBA); receptor diversity; graph theory (modularity, global efficiency); spin-test / spatial autocorrelation null models; default-mode / association cortex; comparative neuroimaging.

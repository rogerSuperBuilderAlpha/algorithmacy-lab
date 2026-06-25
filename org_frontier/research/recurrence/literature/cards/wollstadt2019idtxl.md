---
citekey: wollstadt2019idtxl
title: {IDTxl}: The Information Dynamics Toolkit xl: a Python Package for the Efficient Analysis of Multivariate Information Dynamics in Networks
authors: Wollstadt, Patricia and Lizier, Joseph T. and Vicente, Raul and Finn, Conor and Martinez-Zarzuela, Mario and Mediano, Pedro and Novelli, Leonardo and Wibral, Michael
year: 2019
doi: 10.21105/joss.01081
arxiv: null
journal: Journal of Open Source Software
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://joss.theoj.org/papers/10.21105/joss.01081.pdf
sha256: c98dfa1e553f139632a347427081ded0a12bb625c9348d2f7bd80e01ccd165b2
pdf_path: literature/pdfs/wollstadt2019idtxl.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
IDTxl (the Information Dynamics Toolkit xl) is an open-source Python3 toolbox for effective network inference from multivariate time series using information theory. The motivating problem is that transfer entropy (TE), the standard directed information-transfer measure, is most often applied in a bivariate (source-target pair) fashion, which in a multivariate setting can infer spurious or redundant interactions and can miss synergistic interactions among multiple relevant sources; a fully exhaustive multivariate approach is computationally intractable even for a small number of potential sources, so an approximate approach is required. IDTxl estimates multivariate TE with a greedy/iterative algorithm that builds a parent-source set for each target node by maximising a conditional mutual information criterion, which removes redundancies, captures synergies, automatically constructs a non-uniform multivariate embedding, and optimises source-target delays. Rigorous statistical controls based on comparison to null distributions from time-series surrogates gate parent selection and provide automatic stopping conditions, requiring minimal user-specified settings. Beyond multivariate TE, the toolkit implements bivariate/multivariate mutual information inference, bivariate TE, active information storage (AIS), and partial information decomposition (PID), and offers local variants of measures plus group-level comparison tools. It supplies multiple estimators (e.g. linear Gaussian / Granger causality for speed, Kraskov nonlinear estimators for accuracy) for discrete and continuous data, with both CPU and GPU implementations. IDTxl is positioned as a next-generation combination of the TRENTOOL and JIDT toolkits, extending TRENTOOL's pairwise TE analysis to a multivariate one.

## Key facts it relies on
- Transfer entropy (Schreiber, 2000) is an extension of mutual information that measures directed information transfer between a source and a target time series; mutual information is a model-free measure of dependence built on probability theory.
- The multivariate TE algorithm uses a greedy/iterative approach that builds parent-source sets per target node by maximising a conditional mutual information criterion (Faes et al., 2011; Lizier & Rubinov, 2012), which both removes redundancies and captures synergistic interactions.
- The iterative conditioning automatically constructs a non-uniform multivariate embedding of potential sources (Faes et al., 2011) and optimizes source-target delays (Wibral et al., 2013).
- Statistical control is based on comparison to null distributions from time-series surrogates, used to gate parent selection and to provide automatic stopping conditions; the toolkit controls for false positives during selection of relevant sources.
- Additional network-inference algorithms implemented: multivariate mutual information, bivariate mutual information, and bivariate transfer entropy.
- Active information storage (AIS) (Lizier, Prokopenko, & Zomaya, 2012) is included for analysis of information storage within network nodes.
- Partial information decomposition (PID) (Bertschinger et al., 2014; Makkeh et al., 2018; Williams & Beer, 2010) is included for analysis of synergistic, redundant, and unique information that two source nodes have about one target node; low-level PID estimators are provided for discrete data only.
- Estimators handle both discrete and continuous data and span linear Gaussian (Granger causality, Granger 1969) for speed versus nonlinear (Kraskov, Stögbauer, & Grassberger, 2004) for accuracy; CPU and GPU implementations are provided for parallel computing.
- IDTxl is a next-generation combination of TRENTOOL (Lindner et al., 2011) and JIDT (Lizier, 2014b), is Python3-based, requires no proprietary libraries, and includes import tools for neuroscience formats such as FieldTrip.
- Submitted 11 November 2018, published 19 February 2019, in Journal of Open Source Software, 4(34), 1081; available from GitHub (https://github.com/pwollstadt/IDTxl).

## Critical notes from the literature
- The paper itself states that an exhaustive multivariate TE approach is computationally intractable even for a small number of potential sources, so IDTxl relies on an approximate (greedy) approach rather than an exact one.
- The authors note that prior approximate multivariate approaches existed (Lizier & Rubinov, 2012; Faes et al., 2011) and a first software implementation existed (Montalto, Faes, & Marinazzo, 2014 — MuTE), but claim no prior implementation dealt with the practical problems of multivariate TE estimation, namely control of statistical errors from testing multiple sources and optimization of estimation parameters.
- This is a short JOSS software paper: it describes capabilities and design but does not present benchmark experiments, accuracy evaluations, or quantitative validation results within the paper itself; details are deferred to the IDTxl homepage.
- Low-level PID estimation is limited to discrete data, a scope condition stated in the paper.

## Key topics covered
- Multivariate transfer entropy and effective network inference
- Greedy/iterative conditional mutual information maximisation
- Non-uniform multivariate embedding; source-target delay optimization
- Surrogate-based statistical significance testing; false-positive control; automatic stopping
- Active information storage (AIS); partial information decomposition (PID); synergy/redundancy/unique information
- Kraskov (KSG) nonlinear estimators vs. linear Gaussian / Granger causality estimators
- Discrete and continuous data; CPU/GPU parallel estimation; local information measures
- Python3 toolkit; successor to TRENTOOL and JIDT; neuroscience (FieldTrip) import; group-level analysis

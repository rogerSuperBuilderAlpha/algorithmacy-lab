---
citekey: hasselman2023geometry
title: The geometry of synchronization: quantifying the coupling direction of physiological signals of stress between individuals using inter-system recurrence networks
authors: Hasselman, Fred and den Uil, Luci{\"e}nne and Koordeman, Renske and de Looff, Peter and Otten, Roy
year: 2023
doi: 10.3389/fnetp.2023.1289983
arxiv: null
journal: Frontiers in Network Physiology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fnetp.2023.1289983/pdf?isPublishedV2=False
sha256: 389c773127c067205ecb01e16bc34e040d61d3a2f05857a424613644db2e6266
pdf_path: literature/pdfs/hasselman2023geometry.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This methods paper asks whether inter-system recurrence networks (IRN) can detect the direction of coupling between physiological stress signals of two interacting people. IRN combine the auto-recurrence matrices of two (or more) systems with their cross-recurrence matrix to form a single composite graph, and the asymmetry of the cross-clustering coefficients (CXY vs CYX) is used to infer which system is driving the interaction. The authors first validate the approach on simulated coupled damped oscillators in four scenarios (uncoupled, X drives Y, Y drives X, bi-directional), showing the cross-clustering differences fall in the theoretically expected directions. They then apply IRN to empirical data from a single client-caregiver dyad in residential care, with both wearing Empatica E4 wristbands recording five physiological signals (acceleration, blood volume pressure, electrodermal activity, heart rate, temperature) in the 35-minute window before 29 challenging-behavior incidents. Across incidents the three coupling types (client leading, caregiver leading, bi-directional/uncoupled) occur with roughly equal frequency, with variable-specific differences, and a full multiplex IRN across all five signals reveals candidate feedback loops. The authors conclude IRN can estimate an observed/implied coupling direction useful for post-hoc analysis, but distinguishing bi-directional coupling from no coupling remains a challenge.

## Key facts it relies on
- IRN combine auto-recurrence and cross-recurrence matrices into a composite adjacency matrix; the inter-system matrix IR(ε) uses three thresholds εX, εY, εXY that may be dissimilar, and it is recommended to have fewer cross-system than intra-system recurrences (RRXY ≤ RRX ≈ RRY) (Feldhoff et al., 2012).
- The cross-edge density ρXY equals the cross-recurrence rate RRXY; if the edge distribution between graphs is uncorrelated, the expected cross-clustering coefficient is CXY ≈ ρY ≈ RRY, while CXY ≪ ρY or CXY ≫ ρY indicate (anti-)persistent correlations in connectivity structure.
- Coupling-direction logic: for unidirectional coupling X→Y the expectation is CYX > CXY; for Y→X the reverse CXY > CYX; for uncoupled oscillators CXY ≈ CYX.
- Simulation used two linear damped oscillators (Eq. 9) with X0=3, Y0=−3 (antiphase), frequency η=0.3, damping ζ=−0.05; coupling scenarios set via γxy and γyx (e.g., X drives Y: γxy=+0.05, γyx=0; bi-directional: γxy=+0.05, γyx=−0.05); time series length 201, simulated with R package deSolve and lsoda solver.
- Simulation thresholds yielded RRX=RRY=.05 and RRXY=.03; Table 1 reports ΔC = CXY−CYX of 0 (uncoupled), −.257 (X drives Y), +.284 (Y drives X), and +.005 (bi-directional), all in the expected directions.
- A 41×41 sweep of γxy, γyx from 0 to 0.1 (40 steps) shows ΔC fails to distinguish coupling direction when both coupling strengths are very large, and can even reverse near the transition where coupling exceeds the damping factor and oscillations grow.
- Empirical data: 33 incidents from one client-caregiver dyad over 12 days (3 Aug–27 Sep 2022); after removing 4 incidents with short/failed time series, 29 incidents with 5 time series remained; signals resampled to 1 Hz giving length 2,100, with embedding lag=100 and embedding dimension=5, auto-recurrence threshold for 5% recurrent points and cross-recurrence for 4%.
- Table 2 (per-variable % of 29 incidents, client / caregiver / bi-directional-uncoupled): ACC 41.4/20.7/37.9; BVP 13.8/10.3/75.9; EDA 31.0/58.6/10.3; HR 41.4/34.5/24.1; TEMP 44.8/41.4/13.8; mean 34.5/33.1/32.4; coupling labels used |CXY−CYX| ≤ .01 as bi-directional/uncoupled.
- A full multiplex IRN for one incident (Figure 7) reveals feedback loops: a strong EDA-HR-TEMP coupling fully driven by the client, and an ACC-TEMP-HR motif (ACC-TEMP and ACC-HR) driven by the caregiver.

## Critical notes from the literature
- The authors state there is currently no general 'best' method for estimating coupling direction, and accurate identification of coupling direction remains a challenge (citing Feldhoff et al., 2012; Runge et al., 2019); their goal is to explore IRN applicability, not to present an optimal method.
- A central acknowledged limitation: deciding between bi-directional coupling and no coupling remains difficult, because both produce cross-clustering coefficient differences close to 0, and this distinction is unlikely to be feasible with noisy real-world data.
- The simulation sweep shows parameter regimes where IRN gives uncertain or reversed coupling-direction inferences relative to the true coupling strengths; the authors frame these as estimates of the observed/implied coupling direction rather than recovery of true coupling parameters.
- The empirical analysis is a single client-caregiver dyad (n=1 dyad, 29 incidents), limiting generalizability; the authors note such measures can at most inform post-hoc evaluation, and more research is needed before real-time intervention/prevention use.
- The current undirected IRN cannot establish temporal precedence among the feedback loops; the authors suggest future use of directed/weighted recurrence networks or recurrence-time weighting to resolve this.

## Key topics covered
Inter-system recurrence networks (IRN); recurrence networks and recurrence quantification analysis (RQA); cross-recurrence quantification analysis (CRQA); cross-clustering coefficients (CXY, CYX); cross-edge density; recurrence rate thresholds; diagonal cross-recurrence profiles (DCRP); coupling direction and strength inference; coupled damped oscillators simulation; physiological synchronization; wearable sensors (Empatica E4); intellectual disability / challenging behavior care setting; multiplex recurrence networks; feedback loops in multivariate physiological signals; delay embedding (mutual information lag, false nearest neighbors).

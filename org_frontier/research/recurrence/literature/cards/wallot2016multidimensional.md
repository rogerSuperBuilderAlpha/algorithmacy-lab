---
citekey: wallot2016multidimensional
title: Multidimensional Recurrence Quantification Analysis (MdRQA) for the Analysis of Multidimensional Time-Series: A Software Implementation in MATLAB and Its Application to Group-Level Data in Joint Action
authors: Wallot, Sebastian and Roepstorff, Andreas and M{\o}nster, Dan
year: 2016
doi: 10.3389/fpsyg.2016.01835
arxiv: null
journal: Frontiers in Psychology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01835/pdf
sha256: 4beab78ff9990ad3c7df8c9949552d3c2bde74f9a97895250bb54a3f28494d61
pdf_path: literature/pdfs/wallot2016multidimensional.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces Multidimensional Recurrence Quantification Analysis (MdRQA), a multivariate extension of Recurrence Quantification Analysis (RQA) that constructs a single shared phase-space from N measured variables (rather than from time-delayed copies of one observable) and quantifies the resulting recurrence plot. The motivation is joint/collective action research, where most studies have been limited to dyads or to averaging over all pairwise decompositions, which creates problems with non-independent degrees of freedom when quantifying groups larger than two. The authors situate MdRQA relative to RQA, CRQA, and JRQA, illustrating its behavior on the Lorenz attractor and on two coupled van der Pol oscillators, and show that MdRQA-based measures track coupling strength more strongly and with more convergent correlations than CRQA in that example. They apply MdRQA to skin-conductance data from a teamwork study (groups of three building origami boats over five sessions), using individual-, dyadic-, and group-level analyses (MdRQA1/MdRQA2/MdRQA3) as predictors in regression. Group-level dynamics (MdRQA3) predicted task performance in later trials (R^2 rising to above 0.2) whereas individual and dyadic levels did not (R^2 around 0.1), a relationship not visible at the aggregate-individual or dyadic level in prior analyses. The paper also derives a phase-space distance scaling correction needed when comparing RQA measures across different dimensionalities, and provides MATLAB code in the supplementary material.

## Key facts it relies on
- MdRQA builds an n-by-N matrix W whose rows W_i are N-dimensional vectors of the N observables at time t_i, then thresholds the Euclidean distance matrix; a point is recurrent when ||V_i - V_j|| < threshold T, with RP_ij = Θ(T - ||V_i(x) - V_j(x)||) using the Heaviside step function (0 for x<0, 1 for x>=0).
- The four recurrence measures focused on are recurrence rate (RR), determinism (DET), average diagonal line length (ADL), and longest diagonal line length (LDL), defined in Table 1 (e.g., RR = sum of recurrent points / size of RP; DET = sum of diagonally adjacent recurrent points / sum of recurrent points).
- Lorenz-system demonstration uses fixed parameters σ = 10, ρ = 28, β = 8/3, solved over 0 ≤ t ≤ 20, resampled to Δt = 0.0162 (1234 samples; 1234·Δt = 20), z-scored, embedded with D = 3 and τ = 4; recurrence plots used T = 0.1 for reconstructed attractors and T = 0.08 for the original attractor.
- For the Lorenz reconstructions (Table 2; D = 3, τ = 4, T = 0.01 for RQA and T = 0.008 for MdRQA): RR (%) = 0.69/0.84/0.68/0.69 for RQA(x)/RQA(y)/RQA(z)/MdRQA; DET (%) = 99.4/97.4/99.5/99.9; ADL = 9.12/7.84/10.3/16.4; LDL = 131/118/82/167; diagonal-line structures are consistently longer in MdRQA than in RQA.
- The coupling example uses two coupled van der Pol oscillators with μ = 100 and asymmetric coupling ε_2 = 5ε_1, embedded with D = 2, τ = 1, T = 0.01 for both CRP and MdRP; MdRQA measures show generally high and convergent correlations with ε_1, whereas CRQA correlations are lower or in one case negative (Table 3: RR correlations with ε_1 are 0.48 for CRQA vs 0.99 for MdRQA; DET -0.86 vs 0.89; ADL 0.43 vs 0.94; LDL 0.60 vs 0.60).
- Table 4 compares the multivariate JRP and the MdRP of the Lorenz system: RR (%) 0.14 (JRP) vs 0.84 (MdRP) — a factor of ~6 smaller for the JRP because JRP structure requires recurrence simultaneously in all three constituent RPs — while DET (98.1 vs 97.4), ADL (11.9 vs 7.84), and LDL (82 vs 118) are of comparable magnitude.
- The origami teamwork application (Håkonsson et al., 2015; Mønster et al., 2016a) used groups of three participants building origami boats over five consecutive sessions in 4-min sessions; skin-conductance records were analyzed at individual (MdRQA1 = simple RQA), dyadic (MdRQA2, averaged over pairings), and group (MdRQA3, all three records jointly) levels, using embedding delay τ = 6, embedding dimension D = 6 (a 3-dimensional signal embedded once, 3·2 = 6), and threshold T = 0.12 with a Euclidean norm.
- In the regression predicting number of boats built, individual and dyadic levels had R^2 around 0.1, while group-level MdRQA3 R^2 increased to above 0.2 in later trials (Figure 7A); all models had predictor DF = 4 and residual DF = 95, so a significant model at α = 0.05 needed R^2 > 0.096 (p < 0.05).
- Average phase-space distance scales with dimensionality as L_D^2 = 2D for equal-variance random variables, giving the baseline-correction scaling relation L_D = sqrt(L_{D+n}^2 - 2n) (Equation 11), which must be applied when comparing RQA measures across phase-spaces of different dimensionality.

## Critical notes from the literature
- The authors explicitly state that the van der Pol example showing stronger/more convergent MdRQA correlations with coupling does NOT imply MdRQA is generally more sensitive than CRQA, since they did not systematically test different systems and coupling properties.
- A stated disadvantage relative to CRQA: in its present form MdRQA cannot calculate time-lagged coupling between signals, nor investigate leader-follower relationships or test the directional influence of one component signal on another (as convergent cross-mapping would); these are flagged as open future-development problems.
- MdRQA measures admit two distinct interpretations — capturing the dynamics of a single multidimensional system (Lorenz-like, raising questions of a well-defined attractor manifold) versus a synergistic dynamic multivariate correlation across separate systems — and the authors note these carry different demands (whether additional embedding is necessary differs by interpretation).
- Comparing recurrence measures across phase-spaces of different dimensionality is biased by a "baseline" dimensionality effect on phase-space distances; corrections (Equation 11, or holding percent recurrence constant) are required, and the paper cautions this must be kept in mind whether the extra dimensions are time-delayed surrogates or actual observables.
- Whether and how to embed multidimensional signals "cannot be answered conclusively"; the authors cite March et al. (2005) and Iwanski and Bradley (1998) that unembedded/parent plots can carry similar information, while noting their own experience that embedding choices can substantially affect results.

## Key topics covered
MdRQA; recurrence quantification analysis (RQA); cross-recurrence quantification analysis (CRQA); joint recurrence quantification analysis (JRQA); recurrence plots; phase-space reconstruction; time-delayed embedding; Takens' theorem; Lorenz attractor; van der Pol oscillators; recurrence measures (RR, DET, ADL, LDL); threshold/Euclidean norm; self-similarity matrices; joint and collective action; group-level dynamics; dyadic vs group analysis; degrees of freedom in pairwise decomposition; skin conductance / physiological synchrony; teamwork (origami production task); phase-space distance scaling correction; parameter estimation (false-nearest-neighbor, delay/embedding); MATLAB software implementation.

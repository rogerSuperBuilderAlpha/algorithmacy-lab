---
citekey: marwan2007recurrence
title: Recurrence Plots for the Analysis of Complex Systems
authors: Marwan, Norbert and Romano, M. Carmen and Thiel, Marco and Kurths, J{\"u}rgen
year: 2007
doi: 10.1016/j.physrep.2006.11.001
arxiv: null
journal: Physics Reports
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2501.13933
sha256: a3336d94c9015bfffc64058cd6a93e160df616139d84f2ff4ee970a110ea8d3a
pdf_path: literature/pdfs/marwan2007recurrence.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a comprehensive review of recurrence plots (RPs) and their use for analysing complex, nonlinear dynamical systems from time-series data. It traces the concept of recurrence from Poincaré's 1890 work and the Poincaré Recurrence Theorem through Eckmann et al.'s 1987 introduction of recurrence plots, then systematically develops the method: phase-space reconstruction by time-delay embedding, the recurrence matrix R_{i,j}(ε) = Θ(ε − ‖x_i − x_j‖), threshold selection, and the classification of large-scale "typology" and small-scale "texture" structures in RPs. It defines recurrence quantification analysis (RQA) measures based on diagonal lines (DET, L, L_max, DIV, ENTR) and vertical lines (LAM, TT, V_max), and shows how dynamical invariants such as the second-order Rényi (correlation) entropy K2 and correlation dimension D2 can be estimated directly from RPs. The review extends RPs to cross recurrence plots (CRP) and joint recurrence plots (JRP), develops recurrence-based detection of phase and generalised synchronisation, and demonstrates the methods on prototypical systems (Rössler, Bernoulli map) and real applications in neuroscience, finance, engineering damage detection, geophysics, palaeoclimate, and extra-solar planetary stability.

## Key facts it relies on
- The recurrence plot is defined by the recurrence matrix R_{i,j}(ε) = Θ(ε − ‖x_i − x_j‖), i,j = 1,…,N, where Θ is the Heaviside function and ε a threshold distance; R_{i,i} ≡ 1 gives the line of identity (LOI) and the RP is symmetric (R_{i,j} ≡ R_{j,i}).
- Phase space is reconstructed from a scalar series by time-delay embedding x̂_i = Σ_{j=1}^m u_{i+(j−1)τ} e_j; Takens' theorem guarantees a diffeomorphism between original and reconstructed attractor when m ≥ 2D2 + 1, where D2 is the correlation dimension.
- The method was introduced by Eckmann et al. in 1987; Poincaré introduced recurrences in 1890, and the Poincaré Recurrence Theorem states that for a measure-preserving transformation the trajectory returns to the neighbourhood of any former point with probability one. The Earth's atmosphere recurrence time is estimated at about 10^30 years.
- Threshold rules of thumb cited: ε a few per cent of the maximum phase-space diameter, not exceeding 10% of the mean or maximum diameter; choose ε so recurrence point density ≈ 1% for non-stationary data; ε > 5σ when observational noise has standard deviation σ; dynamical invariants from RPs only exist in the limit ε → 0.
- Core RQA diagonal-line measures: recurrence rate RR(ε) = (1/N²)Σ R_{i,j}; determinism DET = Σ_{l≥l_min} l P(l) / Σ_l l P(l) (predictability); average diagonal length L (mean prediction time); L_max with divergence DIV = 1/L_max; ENTR = −Σ p(l) ln p(l) (Shannon entropy of diagonal-length distribution).
- Vertical-line measures: laminarity LAM = Σ_{v≥v_min} v P(v) / Σ_v v P(v); trapping time TT (mean length of vertical structures); V_max; for maps v_min = 2 is appropriate.
- Diagonal-line lengths are linked to the second-order Rényi entropy K2 and the sum of positive Lyapunov exponents; L_max can serve as an estimator for K2. On the Bernoulli map the RP-based estimate K̂2 = 0.6929 ± 0.0016 matches the theoretical K2 = ln 2 ≈ 0.6931, and D̂2 = 0.9930 ± 0.0098 against theoretical D2 = 1.
- Extensions: cross recurrence plot (CRP) for two systems, joint recurrence plot JR_{i,j}(ε_x,ε_y) = Θ(ε_x − ‖x_i−x_j‖)Θ(ε_y − ‖y_i−y_j‖) for physically different systems, and recurrence-based indices (e.g. CPR) for detecting phase and generalised synchronisation; most methods are available in the CRP toolbox for Matlab (TOCSY).
- Variant RPs discussed include unthresholded/distance plots, corridor-thresholded RPs (Iwanski & Bradley), perpendicular RPs (Choi et al.), iso-directional RPs (Horai & Aihara), windowed/meta RPs, and order-patterns recurrence plots (OPRP).

## Critical notes from the literature
- The paper stresses threshold ε is a crucial, system-dependent parameter: too small yields almost no recurrence points, too large makes almost every point a neighbour and produces artefacts; a too-large ε also admits tangential-motion points that thicken and lengthen diagonal structures beyond their true extent.
- It cautions that the relationship between RQA line-length measures and the largest positive Lyapunov exponent "is not as simple as it was mostly stated in the literature"; the rigorous link is between the diagonal-length distribution and K2 (a lower bound on the sum of positive Lyapunov exponents), not a direct estimate of a single exponent.
- Diagonal structures perpendicular to the LOI (mirrored, opposite-time segments) are flagged as often indicating an inappropriate embedding, and some authors exclude the LOI for quantification.
- The authors explicitly state the overview "can by no means be complete" and that they believe the full potential of recurrence-based analysis "is not yet tapped," framing the review as an introduction rather than an exhaustive treatment.
- Corridor-thresholded RPs improve robustness against tangential-motion recurrences but remove inner points of broad diagonals (splitting one line into two), making them not directly suitable for quantification analysis.

## Key topics covered
Recurrence plots (RP); recurrence matrix; Poincaré recurrence theorem; phase-space reconstruction / time-delay embedding; Takens' theorem; threshold ε selection; norms (L1, L2, L∞); RP typology (homogeneous, periodic, drift, disrupted) and texture (single dots, diagonal, vertical, horizontal, bowed lines); tangential motion; recurrence quantification analysis (RQA): RR, DET, L, L_max, DIV, ENTR, LAM, TT, V_max; dynamical invariants K2 (correlation entropy), D2 (correlation dimension), Lyapunov exponents; cross recurrence plots (CRP); joint recurrence plots (JRP); line of synchronisation (LOS); phase and generalised synchronisation detection; twin/recurrence-based surrogates; unstable periodic orbits; influence of noise; RP variants (perpendicular, iso-directional, corridor, order-patterns/OPRP, windowed/meta); applications in neuroscience, finance, damage detection, geophysics, palaeoclimate, extra-solar planetary stability; CRP toolbox for Matlab.

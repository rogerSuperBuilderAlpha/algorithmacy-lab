---
citekey: marwan2008historical
title: A Historical Review of Recurrence Plots
authors: Marwan, Norbert
year: 2008
doi: 10.1140/epjst/e2008-00829-1
arxiv: null
journal: The European Physical Journal Special Topics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1709.09971
sha256: 06bb428285fcadd86b4fbcaab1ca691e4939b7d72d934dad7402830478adf1f7
pdf_path: literature/pdfs/marwan2008historical.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a historical review tracing the first ~20 years of recurrence plots (RPs) as a tool of nonlinear data analysis. It situates the modern method in a longer lineage: Poincaré's recurrence theorem for conservative dynamical systems (19th century), and the independent "similarity matrix" / distance-matrix idea re-invented across disciplines around 1970–1980 under names like dot plot, contact map, similarity matrix, and distance matrix. Recurrence plots proper were introduced by Eckmann, Oliffson Kamphorst, and Ruelle in 1987 to visualise recurrences of higher-dimensional phase-space trajectories, with 1987 considered the method's "birth." Marwan narrates the subsequent development: Zbilut and Webber's recurrence quantification analysis (RQA) in the late 1980s/early 1990s, time-dependent (windowed) RQA, theoretical results linking RP structures to dynamical invariants (K2 entropy, Lyapunov exponents), and extensions such as cross recurrence plots (CRP), joint recurrence plots (JRP, 2004), perpendicular and iso-directional RPs, order-patterns RPs, and the recasting of RPs as complex-network adjacency matrices (Krishnan et al., 2008). The review also documents the spread of RP applications from life sciences into earth sciences, engineering, economics, physics, and chemistry, quantified via download statistics of the CRP Toolbox for MATLAB.

## Key facts it relies on
- The recurrence plot was introduced by J.-P. Eckmann, S. Oliffson Kamphorst, and D. Ruelle in 1987 ("Recurrence Plots of Dynamical Systems," Europhysics Letters 4(9):973–977); 1987 is considered the birth of RPs and their quantification.
- Poincaré's recurrence result (from his prize-winning work on the restricted three-body problem) is cited as the foundational statement that a conservative system recurs infinitely many times arbitrarily close to its initial state.
- The "close returns plot" — comparing only a given time into the past and future rather than all time points — was introduced independently by different authors no later than 1992.
- Zbilut and Webber, starting in the late 1980s, established RQA with measures: percentage recurrences (recurrence rate), percentage determinism, maximal line length and divergence, Shannon entropy of the line-length distribution, and trend.
- Theoretical links: McGuire et al. showed the distance matrix preserves all information to reconstruct the underlying series; Faure and Korn showed the cumulative distribution of diagonal line lengths is directly related to K2 entropy; Eckmann et al. noted diagonal line lengths relate to the positive Lyapunov exponent.
- Extensions: perpendicular RP (1999), iso-directional RP (2002), cross recurrence plot (CRP), joint recurrence plot (JRP, 2004) for general synchronisation, vertical-line-based measures laminarity and trapping time (Marwan et al.) detecting chaos-chaos transitions, and order-patterns RPs (Groth).
- Krishnan et al. (2008) reframed an RP as the adjacency matrix of a complex network, enabling topological/graph analysis via RQA.
- CRP Toolbox for MATLAB download statistics: 383 downloads (May 2003–October 2005) and 728 downloads (November 2005–May 2008); in the second period life sciences led with 275 downloads (psychology/neuro/cognitive 152, cardiology 36), followed by engineering (131), earth sciences (89), physics (72), economics (55), education (21), chemistry (12), social sciences (2), and 71 unspecified.
- Software milestones: Webber's freely available RQA software (early 1990s); Kononov's Visual Recurrence Analysis (VRA, 1996); the TISEAN package (Hegger, Kantz, Schreiber) computing RPs without quantification; the commercial Dataplore (ixellence GmbH).
- Two international RP workshops are recorded: Potsdam 2005 (33 participants) and Siena, Italy 2007 (44 participants); Fig. 2 shows publication counts rising to 61 in 2006 and reaching 70 by the 2008 partial count (May 2008).

## Critical notes from the literature
- The author acknowledges the early-years limitation that RPs were "just a visualisation tool," requiring subjective human detection and interpretation of patterns, worsened by low screen/printer resolutions — the motivation for developing RQA.
- Marwan notes that the perpendicular and iso-directional RP variants "are not popular, probably because of their higher computational efforts," flagging a practical cost barrier to adoption.
- The download-based application statistics are explicitly caveated by the author: scientific-field selection "may occur rather arbitrary," users sometimes gave multiple or unlikely field combinations, some gave no purpose, and there were a few repeated downloads; the author states it is not claimed to be a complete or best selection.
- The review is self-described as written from a particular vantage (Potsdam group of Marwan, Romano, and Thiel did much of the 2002–2006 theoretical work), so the narrative weights the author's own community's contributions.

## Key topics covered
Recurrence plots (RP); recurrence quantification analysis (RQA); Eckmann–Oliffson Kamphorst–Ruelle 1987; Poincaré recurrence; similarity/distance matrix; dot plot; contact map; close returns plot; recurrence rate; determinism; laminarity; trapping time; diagonal/vertical line structures; Lyapunov exponent; K2 entropy; time-dependent (windowed) RQA; cross recurrence plot (CRP); joint recurrence plot (JRP); perpendicular RP; iso-directional RP; order-patterns RP; twin surrogates; synchronisation detection; recurrence networks / adjacency-matrix view; sampling-rate effects; CRP Toolbox for MATLAB; VRA; TISEAN; application fields (life sciences, earth sciences, engineering, economics, physics, chemistry).

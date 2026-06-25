---
citekey: marwan2002recurrence
title: Recurrence-plot-based measures of complexity and their application to heart-rate-variability data
authors: Marwan, N. and Wessel, N. and Meyerfeldt, U. and Schirdewan, A. and Kurths, J.
year: 2002
doi: 10.1103/PhysRevE.66.026702
arxiv: null
journal: Physical Review E
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/physics/0201064
sha256: d121b311828bcdc124ced59bb750b9970da7ca18cbc684cc2a2a1e496c385557
pdf_path: literature/pdfs/marwan2002recurrence.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to detect transitions between regular, laminar, and chaotic behavior in complex systems from short, nonstationary time series, where linear methods are insufficient and most nonlinear methods need long data. The authors extend recurrence quantification analysis (RQA) by defining three new complexity measures based on the *vertical* line structures of a recurrence plot (RP): laminarity (Λ), trapping time (T), and the maximal vertical line length (Vmax). Applied to the logistic map over a ∈ [3.5, 4], these measures detect not only periodic-chaotic/chaotic-periodic transitions (which traditional diagonal-based RQA already finds) but additionally identify laminar states, i.e. chaos-chaos transitions, that diagonal-based RQA fails to detect. Applied to heart-rate-variability (HRV) data from implanted cardioverter-defibrillator (ICD) patients, the measures discriminate time series recorded before a ventricular tachyarrhythmia (VT) from control series, with Vmax being the most discriminating parameter. The authors conclude these measures help detect and quantify laminar phases preceding a life-threatening arrhythmia, potentially enabling prediction of VT events even from short-term HRV.

## Key facts it relies on
- A recurrence plot is the N×N matrix R_{i,j} = Θ(ε_i − ‖x_i − x_j‖); the paper uses a fixed ε_i and the Euclidean norm, giving a symmetric RP, with phase-space vectors reconstructed by Takens time-delay embedding.
- Laminarity Λ (Eq. 2) is the ratio of recurrence points forming vertical structures (length ≥ v_min) to all recurrence points; trapping time T (Eq. 3) is the average length of vertical structures; Vmax (Eq. 4) is the maximal vertical line length, analogous to the standard RQA Lmax. For maps the authors use v_min = 2.
- The vertical-structure approach extends Gao's recurrence time statistics; standard RQA (Zbilut/Webber; Trulla et al.) is based on diagonal line length distributions (recurrence rate, determinism, Lmax, entropy, trend) and does not include vertical/horizontal structure information.
- Logistic map xn+1 = a xn(1−xn) analyzed over a ∈ [3.5, 4] with step Δa = 0.0005; for each a a time series of length N = 2,000 is generated and the last 1,000 values used; RP computed with embedding m = 1, delay τ = 1, cut-off ε = 0.1 (in units of σ, ~10% of phase-space diameter).
- Supertrack functions s_{i+1}(a) = a s_i(a)(1 − s_i(a)), s0(a) = 1/2, are used; their intersections with the fixed point 1 − 1/a mark laminar behavior; example band-merging/laminar points include a = 3.678, 3.727, 3.752, 3.791, 3.877, 3.927, and the two-to-one band merging at a ≈ 3.678/3.679.
- Vertical-based measures Λ and T detect laminar states and band-merging points (e.g. a = 3.678, 3.791, 3.927) where standard RQA measures Δ, Lmax, ⟨L⟩ show no significant indication; vertical lines are absent in periodic windows (e.g. a = 3.848) and rare in fully developed chaos (a = 4).
- HRV data: defibrillators (PCD 7220/7221, Medtronic) store ≥1000 beat-to-beat intervals before VT onset at 10 ms resolution (~9–15 minutes); 17 chronic heart failure ICD patients were reanalyzed, yielding 24 time series with a subsequent VT and 24 matched control series; time series with >10% ventricular premature beats, induced VTs, pacemaker activity, or multiple nonsustained VTs were excluded.
- In the HRV analysis the most significant discriminators were Vmax and Lmax at large radii (Mann-Whitney U-test); Vmax (e.g. m=6, ε=110: VT 283.7±190.4 vs control 179.5±134.1, p<0.01) was more powerful than Lmax (same setting: 447.6±269.1 vs 285.5±160.4, p<0.05). A typical RP example before VT had Vmax = 242 vs Vmax = 117 in the control.

## Critical notes from the literature
- The authors explicitly state two limitations of the HRV study: the relatively small number of time series, and the reduced statistical analysis (no subdivision by age, sex, or heart disease); they recommend validation on a larger database.
- They note the analysis could be enhanced for tachograms including more than 10% ventricular premature beats, which were excluded here.
- The vertical-structure measures are much more sensitive to the embedding than diagonal-based measures: too-small embedding causes false recurrences (numerous vertical structures and diagonals perpendicular to the main diagonal); they state a more detailed theoretical treatment of this embedding effect is "in preparation and beyond the scope of this article."
- The relations between the magnitudes of Λ, T, and Vmax and the recognized chaos-chaos transitions are not fully understood; the authors say further investigations are necessary, and note some Vmax/T peaks do not align exactly with marked supertrack-crossing points though they correspond to laminar states.

## Key topics covered
Recurrence plots; recurrence quantification analysis (RQA); vertical line structures; laminarity (Λ); trapping time (T); maximal vertical line length (Vmax); chaos-chaos / laminar-state transitions; intermittency; logistic map; supertrack functions; band merging; Takens time-delay embedding; heart rate variability; ventricular tachyarrhythmia prediction; implanted cardioverter-defibrillator data; Mann-Whitney U-test.

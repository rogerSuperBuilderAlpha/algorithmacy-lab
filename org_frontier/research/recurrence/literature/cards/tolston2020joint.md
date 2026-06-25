---
citekey: tolston2020joint
title: Comparison of Cross-Correlation and Joint-Recurrence Quantification Analysis Based Methods for Estimating Coupling Strength in Non-linear Systems
authors: Tolston, Michael T. and Riley, Michael A. and Mancuso, Vincent and Finomore, Victor and Funke, Gregory J.
year: 2020
doi: 10.3389/fams.2020.00001
arxiv: null
journal: Frontiers in Applied Mathematics and Statistics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fams.2020.00001/pdf
sha256: f04bfe9e68665b407c3e3eaf7ff4f35842e526407d01f3ba49a7e99e77f6facf
pdf_path: literature/pdfs/tolston2020joint.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether time-delay stability (TDS) analysis—a method introduced by Bashan et al. for building physiological/complex networks by detecting stable temporal coupling between time series—can be improved by replacing its underlying cross-correlation step with joint recurrence quantification analysis (JRQA), an intrinsically non-linear, multidimensional technique. The authors first extend TDS to use JRQA, introducing a weighting factor that compensates for the time-series truncation caused by time-delayed JRQA, correcting a counting bias in the original %TDS criterion, and defining a recurrence-analog metric TDSLMAX (longest stable run of delays, akin to RQA's MAXLINE). They evaluate both the cross-correlation-based and JRQA-based TDS on coupled Rössler oscillators (known dynamics, across phase-coherent and funnel regimes, varied coupling k and detuning ν) and on previously collected dyadic problem-solving behavioral data (waist, head, hand, gaze, speech). Across both synthetic and behavioral data the two approaches give qualitatively comparable results, but cross-correlation-based TDS was often slightly more sensitive to coupling strength, especially when the two systems differed more. The authors conclude that cross-correlation TDS delivers sensitivity on par with JRQA at much-reduced computational cost and with fewer parameters, so the expected benefit of multidimensional non-linear analysis was not consistently realized.

Note: the PDF byline lists the authors as Michael T. Tolston, Gregory J. Funke, and Kevin Shockley (not the author string in this card's frontmatter); the cited form is "Tolston MT, Funke GJ and Shockley K (2020)".

## Key facts it relies on
- TDS (Bashan et al. [1]) segments multivariate signals into overlapping windows, computes pairwise cross-correlation over a range of delays per window, records the delay τ0 of maximum absolute cross-correlation, and summarizes the resulting τ0 time series as %TDS (percentage of contiguous segments with consistent temporal relationships). Windows are formed as NL = (N−L)/a + 1.
- The original %TDS used Nτ0 = 5 and Δτ0 = 1, requiring at least 4 of 5 windows within Δτ0 to call a segment stable; the authors note this sliding-window counting can double-count stable indices, inflating stability, and instead compare only against the first segment of each window.
- JRQA computes joint recurrence as the Hadamard product of two recurrence matrices R (Eq. 4), generalized with a delay parameter τ (Eq. 5, N' = N − τ) so it can capture whether recurrences in X precede those in Y; the complementary JR_YX is concatenated after multiplying its index by −1.
- The authors introduce a truncation weighting factor (Eq. 6) multiplying JR by ((N'^2 − N')/2) / ((N^2 − N)/2) so that values are proportional to the degree of truncation from delaying; they use a nearest-neighbor approach (fixed 2.5% or 5% of neighbors) instead of an explicit threshold ε, symmetrize R via (R + R^T) > 0, and apply a Theiler window equal to the decorrelation time from average mutual information.
- Rössler system (Eq. 7): coupling k switched from 0 to k at the integration midpoint (180 s after removing the first 200 s of 560 s total), integrated with MATLAB ode45, time-step 0.01, downsampled by 10 to 10 Hz; detuning ν varied 0–0.04 in steps of 0.02 (3 values), k varied 0–0.2941 in steps of 0.0118 (26 values).
- Three phase-regime cases were tested (both phase-coherent a1=a2=0.15; mixed a1=0.2925, a2=0.15; both funnel a1=a2=0.2925), with 108 randomly initialized systems per setting for a total of 25,272 Rössler instantiations; TDS used a 48 s window with 4.8 s advance, %TDS window of 5 and 1 s threshold, summarizing the last 19 segments.
- Behavioral data re-analyzed from Tolston et al. [43]: dyads solving picture-puzzle pairs (10 differences each), 190 s per trial, 9 trials (3 per restraint condition: free-free FF, restrained-restrained RR, free-restrained FR); 14 dyads had complete data; signals from waist, head, hand, gaze, speech analyzed at 30 Hz with a 30 s window and 3 s advance.
- For behavioral JRQA, embedding delays were 63 samples (waist, head, hand; dimension 6), 30 samples for speech (dim 4) and gaze (dim 6, gaze embedded multidimensionally for 12 total dimensions); surrogate testing used 100 mismatched within-condition pairings, one-tailed percentile bootstrap with 5,000 samples (α = 0.05), false-discovery-rate corrected, aggregating thresholds from 0.50 to 15 s in 0.50 s steps.
- Results on Rössler: cross-correlation TDS showed a steeper %TDS response to coupling strength and higher separation as a function of detuning ν, particularly in phase-coherent and mixed (funnel-to-phase-coherent) cases; 95% confidence intervals came from a bias-corrected percentile bootstrap with 500 resamples.
- Behavioral results: network density (count of significant links) was highest in the FF condition for both methods; speech and gaze were the most reliable interactions; JRQA-based statistics had smaller windows of sensitivity over Δτ0 while cross-correlation was less affected by Δτ0; %TDS and TDSLMAX from JRQA were near ceiling for gaze.

## Critical notes from the literature
- The authors state the main analyses were limited to bivariate dependencies, which can produce "transitive closure" (indirectly coupled nodes appearing linked) and overly dense networks; they note conditional-dependency / causal extensions (e.g., RQA-based approaches) are needed to infer directionality or rule out spurious links.
- The paper acknowledges that the expected advantages of multidimensional non-linear data were "not always apparent" with JRQA, and that JRQA is substantially more computationally intensive and parameter-heavy than cross-correlation, which weakens the practical case for JRQA-based TDS.
- The current and prior (Tolston et al. [43]) analyses only partially agree: CRQA in the earlier study measured phase-space similarity (not temporal coupling), whereas TDS measures temporally related coupling stability; the authors attribute divergent restraint-condition findings to this difference.
- The authors cite Shockley et al. [48] that large per-dyad variation in coordination reduces between-participants power, and concede their surrogate method may share this limitation; the interpersonal networks had a low number of significant links.
- Scope caveats noted by the authors: dependence of both methods on sample size and window size was observed but not fully reported; only feedback (diffusive) coupling was examined, not other coupling configurations; and the dataset is not publicly available.

## Key topics covered
Time-delay stability (TDS) analysis; %TDS; cross-correlation coupling estimation; joint recurrence quantification analysis (JRQA); recurrence quantification analysis (RQA); cross-recurrence quantification analysis (CRQA); MAXLINE / TDSLMAX; truncation weighting factor; nearest-neighbor recurrence thresholding; Theiler window; phase-space reconstruction / delay embedding; coupled Rössler oscillators; phase-coherent vs funnel regimes; detuning and diffusive coupling; physiological / complex network construction; interpersonal coordination; surrogate analysis; percentile bootstrap; false discovery rate correction.

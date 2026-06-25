---
citekey: chidichimo2026towards
title: Towards an informational account of interpersonal coordination
authors: Chidichimo, Edoardo and Luppi, Andrea I. and Mediano, Pedro A. M. and Leong, Victoria and Dumas, Guillaume and Canales-Johnson, Andrés and Bethlehem, Richard A. I.
year: 2026
doi: 10.1038/s41583-025-00989-0
arxiv: null
journal: Nature Reviews Neuroscience
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://static-content.springer.com/esm/art%3A10.1038%2Fs41583-025-00989-0/MediaObjects/41583_2025_989_MOESM1_ESM.pdf
sha256: 06321db24ca17d903a100f83d69e5fc68e3d1fca510bfe0406934bfc1aa4adde
pdf_path: literature/pdfs/chidichimo2026towards.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
SCOPE NOTE: The acquired PDF is ONLY the Supplementary Information file ("MOESM1_ESM.pdf") for this Nature Reviews Neuroscience Perspective, not the main article text. It is 3 pages and contains a single supplementary figure plus two references. The main Perspective — which the title indicates argues for an informational (information-theoretic) account of interpersonal coordination — is NOT present in this PDF, so its core thesis, arguments, and conclusions cannot be summarized from this document. What the supplement does cover: a methodological figure (Supplementary Figure 1) contrasting two approaches to spectral analysis of neural (EEG/MEG-type) power spectra. Approach A is the conventional "a priori" canonical frequency banding (delta, theta, alpha, beta, gamma) applied uniformly across participants and conditions. The supplement warns this fixed binning can conflate true oscillatory peaks with surrounding aperiodic 1/f activity, mask individual/condition-specific variability, and lead to misinterpretation of signal sources. Approach B is spectral parameterisation, which decomposes the power spectral density (PSD) into separate aperiodic and periodic components to recover frequency, amplitude, and bandwidth parameters in a more interpretable, reproducible, and dynamics-sensitive way.

## Key facts it relies on
- The document is the Supplementary Information for the Perspective "Towards an informational account of interpersonal coordination," published in Nature Reviews Neuroscience (DOI 10.1038/s41583-025-00989-0), provided "in the format provided by the authors and unedited."
- Corresponding author Edoardo Chidichimo (University of Cambridge / Magdalen College, Oxford), with co-authors Andrea I. Luppi, Pedro A. M. Mediano, Victoria Leong, Guillaume Dumas, Andrés Canales-Johnson, and Richard A. I. Bethlehem; affiliations span Cambridge, Oxford, Imperial College London, NTU Singapore, Université de Montréal/Mila, Helsinki, and Universidad Católica del Maule.
- Supplementary Figure 1 (Panel A) lists the canonical a priori frequency bands used in the example: delta 1–4 Hz, theta 4–8 Hz, alpha 8–13 Hz, beta 13–30 Hz, gamma 30–50 Hz.
- The supplement argues that a priori banding is "often applied uniformly across participants and conditions," and that true spectral peaks may fall outside these arbitrary cut-offs, conflating oscillatory peaks with surrounding aperiodic 1/f activity.
- Spectral parameterisation (Panel B) is described as a four-step pipeline: (a) plot the raw power spectrum and fit an aperiodic component (e.g., a 1/f slope); (b) subtract that component to reveal residual oscillatory peaks; (c) fit individual Gaussians to candidate peaks to estimate frequency, amplitude, and bandwidth; (d) reconstruct a full model jointly estimating periodic and aperiodic contributions.
- The supplement states full parameterisation involves iterative fitting and noise thresholding to ensure robustness across varying signal quality and peaks.
- The supplement cites only two references, both on spectral parameterisation methods: Donoghue et al. (2020), "Parameterizing neural power spectra into periodic and aperiodic components," Nature Neuroscience 23(12):1655–1665; and Donoghue, Schaworonkow & Voytek (2022), "Methodological considerations for studying neural oscillations," European Journal of Neuroscience 55(11-12):3502–3527.

## Critical notes from the literature
- This card is grounded only in the Supplementary Information; the main Perspective's actual claims about an "informational account of interpersonal coordination" (e.g., its information-theoretic framing, hyperscanning/inter-brain synchrony arguments, or proposed measures) cannot be verified from this PDF and would require the full main text.
- The supplement itself frames the conventional a priori canonical-band approach as a methodological pitfall — it can "conflate oscillatory peaks with the surrounding aperiodic 1/f activity," mask individual or condition-specific variability, and cause misinterpretation of signal sources.
- The recommended alternative (spectral parameterisation / separation of periodic and aperiodic components) is presented as more "interpretable, reproducible, and sensitive to meaningful neural dynamics," but the supplement notes it is simplified in the figure and in practice requires iterative fitting and noise thresholding to remain robust across varying signal quality — i.e., it is not a turnkey method.
- The methodological stance rests entirely on the two cited Donoghue/Voytek works (the "specparam"/FOOOF line of work); no empirical validation or new data is presented in this supplement.

## Key topics covered
- Interpersonal coordination (informational account) — main Perspective topic (only the supplement was available)
- Spectral analysis of neural power spectra; power spectral density (PSD)
- A priori canonical frequency banding (delta/theta/alpha/beta/gamma)
- Aperiodic (1/f) vs periodic/oscillatory components
- Spectral parameterisation (peak frequency, amplitude, bandwidth estimation; Gaussian peak fitting)
- Methodological confounds in EEG/MEG oscillation analysis
- Donoghue/Voytek specparam (FOOOF) methodology

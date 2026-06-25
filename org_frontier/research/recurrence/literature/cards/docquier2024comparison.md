---
citekey: docquier2024comparison
title: A Comparison of Two Causal Methods in the Context of Climate Analyses
authors: Docquier, David and Di Capua, Giorgia and Donner, Reik V. and Pires, Carlos A. L. and Simon, Am\'{e}lie and Vannitsem, St\'{e}phane
year: 2024
doi: 10.5194/npg-31-115-2024
arxiv: null
journal: Nonlinear Processes in Geophysics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://npg.copernicus.org/articles/31/115/2024/npg-31-115-2024.pdf
sha256: 308a6919b57cf1c58c68d1285a21650e459dafe46f24aeed705421efceaacb5e
pdf_path: literature/pdfs/docquier2024comparison.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether two independent causal-inference methods — the Liang–Kleeman information flow (LKIF) and the Peter and Clark momentary conditional independence (PCMCI) algorithm — outperform classical correlation and how they compare to each other when applied to climate-style data. The authors apply both methods plus Pearson correlation to four artificial models of increasing complexity (a 2D stochastic linear model, a 6D linear VAR model, a 9D nonlinear stochastic VAR model, and the deterministic chaotic Lorenz 1963 model) and to one real-world case study using eight monthly climate indices over the Atlantic and Pacific (1950–2021). They show both causal methods are superior to correlation, especially in removing spurious links (correlation has 100% false-positive rates for the 2D and 6D models). LKIF performs better for simpler/fewer-variable systems (e.g., it perfectly recovers the 2D link with φ=1 where PCMCI fails at the original time step), while PCMCI is better for larger systems (φ=0.81 vs LKIF's 0.77 on the 9D model with lags). For the chaotic Lorenz system both methods detect the same links, and nonlinear variable changes (x→x²) make hidden links linearly detectable. In the real-world case, LKIF identifies the Arctic Oscillation (AO) as the dominant driver while PCMCI identifies El Niño–Southern Oscillation (ENSO) as the main influencing variable — a key divergence between the methods.

## Key facts it relies on
- Two causal methods are compared: LKIF (Liang and Kleeman, 2005; multivariate formulation from Liang, 2016, 2021), reported via the relative rate of information transfer τ (in %); and PCMCI (Spirtes et al., 2001; Runge et al., 2019b), reported via the path coefficient β. Statistical significance uses α = 5%.
- Datasets span increasing complexity: a 2D stochastic linear model (x2 drives x1), a 6D linear VAR model with one lag (7 true causal links, x6 a confounder), a 9D nonlinear stochastic VAR model with lags up to 4 (9 true links), the 3D Lorenz (1963) chaotic model, and 8 climate indices.
- Climate indices: four atmospheric (PNA, NAO, AO/NAM, QBO) and four oceanic (AMO, PDO, TNA, Niño3.4/ENSO); monthly values January 1950–December 2021 (864 months), linearly detrended for approximate stationarity; retrieved from NOAA PSL.
- 2D model: correlation R = 0.23 (no direction); LKIF numerical |τ2→1| = 5.72% vs analytical 5.56%; PCMCI fails at Δt = 0.001 but recovers the link at Δt = 0.1. LKIF φ = 1; correlation and PCMCI (original step) φ = 0.
- 6D model: all 30 correlation pairs significant (largest R = 0.37 for x2–x5, a false positive from confounder x6); both LKIF and PCMCI recover all 7 correct links with φ = 1 (correlation φ = 0, false-positive rate 100%).
- 9D model with lags: correlation φ = 0.21 (false-positive rate 73%), LKIF φ = 0.77 (false positives 8%), PCMCI φ = 0.81 (false positives 6%); all three give true-positive rate 100% with lags.
- Lorenz (1963) model: correlation between x and y is R = 0.88; both methods detect a two-way x–y link. Replacing x with x² yields strong x²–z links (correlation R = 0.65; LKIF |τ| ~ 50%; PCMCI |β| = 1.7 in both directions), showing linear methods can detect nonlinear-transformed causal links.
- Real-world case: 54% of index pairs are significantly correlated at zero lag, but many are spurious. Shared findings include AO→PDO, AO→TNA, two-way AMO–TNA (LKIF |τAMO→TNA| = 22%, |τTNA→AMO| = 38%), and ENSO→PDO. AO is by far the largest driver per LKIF (influences all indices except QBO and ENSO; AO→NAO |τ| = 4%); ENSO is the dominant driver per PCMCI.
- Performance is summarized by a φ coefficient from a confusion matrix (TP, TN, FP, FN); φ = 1 is perfect, φ = 0 is no better than random. The denominator is set to 1 (giving φ = 0) if any of its four sums is zero.

## Critical notes from the literature
- The authors stress there is no single best causal method; performance depends on the data ("it is important to choose the right method for a particular type of data," echoing Krakovská et al., 2018), and they recommend using as many methods as possible to increase robustness.
- Scope limitation: both methods are used here in their linear forms (PCMCI with partial correlation; LKIF under a linear additive-noise assumption). A nonlinear LKIF (Pires et al., 2024) exists but is not used, and the authors call for nonlinear causal methods to confirm the real-world links.
- PCMCI is not designed for the time-continuous 2D model with very small time steps (it "responds better for discrete maps with finite time steps") and struggles with very strong autocorrelations; LKIF was not designed to use time lags by default (lags are introduced manually by shifting the time series).
- The divergence on the real-world data (AO-dominant for LKIF vs ENSO-dominant for PCMCI; PCMCI failing to detect the well-established AO→NAO link) is acknowledged as unresolved; the authors note possible seasonal-pattern effects and state "more research is needed to confirm these links." No ground-truth exists for the Lorenz and real-world cases, so confusion-matrix diagnostics are not computed there.

## Key topics covered
Causal inference; Liang–Kleeman information flow (LKIF); PCMCI / Peter-and-Clark algorithm; momentary conditional independence; rate of information transfer (τ); path coefficient (β); Pearson correlation vs causation; spurious links and confounders; vector autoregressive (VAR) models; Lorenz 1963 chaotic system; nonlinear variable transformation; climate indices (AO/NAM, NAO, PNA, QBO, AMO, PDO, TNA, ENSO/Niño3.4); confusion matrix and φ coefficient; bootstrap significance testing; Benjamini–Hochberg false discovery rate correction; time-lagged causal discovery.

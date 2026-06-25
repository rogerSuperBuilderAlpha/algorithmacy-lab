---
citekey: marwan2011howto
title: How to Avoid Potential Pitfalls in Recurrence Plot Based Data Analysis
authors: Marwan, Norbert
year: 2011
doi: 10.1142/S0218127411029008
arxiv: null
journal: International Journal of Bifurcation and Chaos
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1007.2215
sha256: a6050c44ca2b6e150b08ae41689761734ad1fbcd9bdee000202643822cc64cfc
pdf_path: literature/pdfs/marwan2011howto.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a methodological cautionary review of recurrence plots (RPs) and recurrence quantification analysis (RQA), motivated by the concern that the growing popularity of these methods (and the availability of free software) raises the risk of uncritical misuse. Rather than presenting a new result, Marwan systematically walks through ten-plus categories of pitfalls in applying RP/RQA and recommends safeguards for each. Key warnings include: the recurrence threshold ε and embedding parameters (m, τ) must be chosen carefully and their robustness checked; high values of the RQA measure DET (determinism) are only a necessary, not sufficient, condition for determinism, since stochastic and embedding-correlated data can produce spurious diagonal lines; very high DET does not reliably indicate periodicity because smooth, highly-sampled chaotic trajectories also yield DET ≈ 1; and dynamical invariants (D2, K2, Lyapunov exponents) require long time series despite the common claim that RP works on short data. The paper also covers windowing choices for transition analysis, the need for confidence intervals, line-of-synchronisation interpretation in cross recurrence plots, and sampling/display artifacts (macrostructures). The overarching message is that RP/RQA results demand understanding of the underlying dynamical-systems theory and explicit reporting of methodological choices.

## Key facts it relies on
- The recurrence plot is defined as R_{i,j} = Θ(ε − ||x_i − x_j||), introduced by Eckmann et al. (1987); RQA quantifying line structures was developed in the 1990s (Webber & Zbilut 1994; Marwan et al. 2002b).
- Determinism is defined as DET = (Σ_{l≥l_min} l·P(l)) / (Σ_{i,j} R_{i,j}), the fraction of recurrence points forming diagonal lines of length l ≥ l_min.
- A non-deterministic auto-regressive process x_i = 0.8x_{i−1} + 0.3x_{i−2} − 0.25x_{i−3} + 0.9ξ (white Gaussian ξ) yields DET = 0.6 (m = 4, τ = 4, fixed RR = 0.1), demonstrating that high DET does not require determinism.
- For white noise embedded at m = 6, τ = 1, ε = 0.2, embedding induces spurious long diagonal lines; the line-length histogram shows a maximum length L_max = 17 (Fig. 2), a value not uncommon for a deterministic process.
- The chaotic Rössler system (a = b = 0.25, c = 40, λ1 = 0.14, sampling Δt = 0.1) produces an RP made almost entirely of diagonal lines giving DET ≈ 1; over c ∈ [35,45] DET stays roughly constant at ≈ 0.94 despite a periodic window between c = 36.56 and c = 37.25 — so high DET is not a sufficient indicator of periodicity.
- Noise-robust threshold rule: to match the noise-free case ε should be chosen ε > 5σ where σ is the observational-noise standard deviation (Thiel et al. 2002); other rules of thumb include RR ≈ 1% (Zbilut et al. 2002) and ε not exceeding ~10% of mean/maximum phase-space diameter.
- DIV = 1/L_max (excluding the line of identity / using a Theiler window) is proposed as a maximal-Lyapunov estimator (Trulla et al. 1996), but is unreliable: a single length-2 line in a stochastic RP gives a finite DIV that can be misread as a finite Lyapunov exponent.
- Dimensions (D1, D2) and invariants (K2) hold only in the limit N → ∞, ε → 0; via the Grassberger–Procaccia requirement log N > D2² log(1/ϱ) with ϱ = 0.1, estimating D2 = 10 needs at least N = 100,000 points; Lyapunov/K2 estimation needs roughly 10^{D2} to 30^{D2} points (D2 = 3 → 1000–30,000 points; Wolf et al. 1985).
- For order-pattern recurrence the number of patterns is d!; d = 4 is often already inappropriate and d = 3 is the best choice in most cases (d = 2 sometimes appropriate).
- Windowed RQA can be done by windowing the RP or windowing the time series; these are only equivalent without normalisation and with a fixed-threshold criterion. Table 1 shows divergent RQA, e.g. window 751–1000: RR/DET/L = 0.10/0.79/3.75 (time-series windowing) vs 0.19/0.95/9.50 (RP windowing).

## Critical notes from the literature
- The paper is explicitly self-limiting: it states that a "general and systematic study on the recurrence threshold selection remains an open task for future work," and that estimating confidence of RQA measures and defining reliable threshold criteria are unresolved open problems.
- It directly critiques the dRR/dε threshold-selection criterion of Gao & Jin (2009) as producing "ambiguous and highly unstable results," strongly norm/embedding dependent and prone to overestimating ε, with some systems having more than one maximum (Donner et al. 2010).
- It warns against naive significance testing: confidence intervals should not be derived by simply shuffling the original data (which only destroys correlation/frequency structure); bootstrap resampling of RP line structures or binomial fits are recommended instead.
- It cautions that detected nonstationarity in a finite observed series does not imply nonstationarity of the underlying system — e.g. an auto-regressive process is stationary by definition yet its RP/RQA can look nonstationary; and the TREND measure is highly sensitive to window size, even giving contrary results.
- Sampling and display caveats: low sampling frequency or sampling/signal frequency interference can create spurious gaps/macrostructures and vanish diagonal lines, and large RPs (e.g. N = 5511 on ~72 ppi screens) get downsampled, producing artificial macrostructures that change with window size — so visual interpretation of large/low-sampled RPs is unreliable.

## Key topics covered
recurrence plots (RP); recurrence quantification analysis (RQA); recurrence threshold ε selection; time-delay embedding (m, τ); determinism (DET) as necessary-not-sufficient; spurious diagonal lines from embedding/noise; chaos vs periodicity vs stochastic discrimination; DIV / L_max and Lyapunov estimation pitfalls; dynamical invariants (D2, K2) and minimum time-series length; windowed/time-dependent RQA and transition detection; significance and confidence intervals of RQA measures; nonstationarity detection caveats; order-pattern recurrence plots; cross recurrence plots (CRP) and line of synchronisation (LOS); sampling time, macrostructures, and display artifacts; surrogate-data testing for nonlinearity

---
citekey: osada2023unified
title: Unified Understanding of Nonparametric Causality Detection in Time Series
authors: Osada, Yutaka and Ushio, Masayuki and Kondoh, Michio
year: 2023
doi: 10.1101/2023.04.20.537743
arxiv: null
journal: bioRxiv
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://www.biorxiv.org/content/biorxiv/early/2023/07/13/2023.04.20.537743.full.pdf
sha256: a0f8fa967be8060dda28ff8f58217fa49e072e497ae77a011a4cfd35c2132b55
pdf_path: literature/pdfs/osada2023unified.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how two widely-used nonparametric causality tests for time series — transfer entropy (TE) and convergent cross mapping (CCM) — are theoretically related, since their relative performance can reverse depending on the system. The authors provide an information-theoretic formulation that links TE and CCM, showing they encode different definitions of causal influence: by Bayes' rule TE is mathematically equivalent to a newly defined measure (UIC), while CCM corresponds to a distinct mutual-information form (CCM_IT) that equals UIC/TE only when the cause variable and the delay-embedded effect are independent. From this they propose unified information-theoretic causality (UIC), which inherits a clear mathematical definition of causal influence from TE, noise robustness from CCM (because cause variables never appear as conditioning variables), and efficient computation of statistical significance via surrogate data. In numerical experiments on a nonlinear logistic model and a linear vector-autoregression (VAR) model, evaluated by AUC, UIC outperformed both TE and CCM for linear and nonlinear systems; CCM lacked statistical consistency (false positives did not vanish with more data) and TE was highly sensitive to noise in the causal variable. They also develop a conditional UIC test that distinguishes direct from indirect causal effects, validating it on a four-species food-chain model and on bacterial DNA time series from experimental rice fields.

## Key facts it relies on
- TE measures causal influence as the flow of information from cause to effect using p(x_t | y_{t-p}, x_t^(E,τ)) vs p(x_t | x_t^(E,τ)); the null hypothesis tested is TE(y_{t-p} → x_t | x_t^(E,τ)) = 0 (Eq. 1).
- The authors define UIC (Eq. 4) using p(y_{t-p} | x_t, x_t^(E,τ)) vs p(y_{t-p} | x_t^(E,τ)); by Bayes' rule p(y|x,z)p(x|z)=p(x|y,z)p(y|z), UIC and TE are proven equivalent given enough data to estimate the conditional probabilities accurately.
- CCM evaluates cross-map predictive performance X(L,P) (Eq. 2); as training-data size approaches zero, its expected causal influence equals a mutual-information form CCM_IT (Eq. 3) using p(y_{t-p}|x_t,x_t^(E,τ)) vs p(y_{t-p}); CCM and UIC/TE are equivalent only when y_{t-p} and x_t^(E,τ) are independent.
- Because CCM and UIC do not include the cause variable y_{t-p} as a conditioning variable (complete separation of x and y as conditional vs predicted variables), they are more robust to noise than TE, which is important in nonlinear dynamical systems.
- Synthetic data were generated from two systems: a nonlinear logistic model and a linear VAR model with varying noise; performance was scored by area under the receiver-operator characteristic curve (AUC) (Fig. 1).
- UIC outperformed TE and CCM in both linear and nonlinear systems; CCM showed slower performance improvement for the linear system because false positives do not decrease even with an infinite number of observations (lack of statistical consistency), and TE required many time points for robust detection in the nonlinear system due to sensitivity to causal-variable noise.
- The conditional UIC test (Eq. 5) adds a third variable z; applying conditions (Eq. 6) — UIC(y→x|x^(E,τ)) > 0 and UIC(y→x|x^(E,τ), z) = 0 — detects whether causal influence of y on x is indirectly mediated by z.
- In the four-species food-chain model, species directly affect their prey at time lag 1; conditional UIC recovered the direct effects at lag 1 (P < 0.05, surrogate-based test), whereas unconditional UIC also flagged many indirect effects.
- In the rice-field bacterial DNA dataset (DNA copy numbers for over 1000 taxa from irrigated water; 20 abundant taxa selected), conditional UIC detected 16 direct and 28 indirect interactions; interaction signs/strengths were estimated by S-map, and the sign reversed for 4 of 16 direct interactions when direct and indirect interactions were not distinguished; the network restricted to direct interactions was estimated as more dynamically stable.
- The Frenzel-Pompe algorithm gives an identical causal-influence value for both TE and UIC, so the distinct statistical behavior of TE and UIC may depend on the algorithm used.

## Critical notes from the literature
- The authors note that TE and UIC are mathematically equivalent in definition yet can show distinct statistical behavior; with other computational algorithms (e.g., Frenzel-Pompe) they might behave similarly, and they explicitly flag this as a caveat — comparing computational algorithms is stated to be beyond the scope of the study.
- CCM's lack of statistical consistency (false positives not vanishing even with infinite observations) is an acknowledged property; the authors cite prior work (refs [3,14]) that CCM is more prone to detecting false causality than TE.
- Embedding dimension E and time interval τ are generally unknown a priori and must be estimated, a standard requirement of state-space reconstruction methods that the paper inherits.
- The empirical demonstration restricts analysis to 20 abundant bacterial taxa (out of over 1000) chosen for sufficient temporal fluctuation, so the reconstructed network is a curated subset rather than the full community.
- This is a bioRxiv preprint not certified by peer review (as stated on every page); many quantitative results are reported via figures and Supplemental Material (S1–S6) rather than in-text numeric tables.

## Key topics covered
Nonparametric causality detection; transfer entropy (TE); convergent cross mapping (CCM); unified information-theoretic causality (UIC); information-theoretic causal influence; Granger causality; time-delay embedding / state-space reconstruction (Takens); conditional causality testing; direct vs indirect interactions; surrogate-data significance testing; noise robustness; statistical consistency; AUC evaluation; nonlinear logistic and linear VAR model systems; S-map interaction estimation; dynamic stability of ecological networks; microbial community time series; Frenzel-Pompe partial mutual information algorithm.

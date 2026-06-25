---
citekey: amornbunchornvej2021variable
title: Variable-Lag Granger Causality and Transfer Entropy for Time Series Analysis
authors: Amornbunchornvej, Chainarong and Zheleva, Elena and Berger-Wolf, Tanya
year: 2021
doi: 10.1145/3441452
arxiv: null
journal: ACM Transactions on Knowledge Discovery from Data
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2002.00208
sha256: e22d95abd959a722afa11ee293a03d8114887c6d7f6cbb2dcf404c2cf99e7fc3
pdf_path: literature/pdfs/amornbunchornvej2021variable.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Standard Granger causality and Transfer Entropy assume that an effect time series is influenced by its cause(s) with a fixed, constant time delay, an assumption the authors argue is too strong for domains such as collective behavior, financial markets, and natural phenomena where lags vary over time. The paper develops Variable-lag Granger causality (VL-Granger) and Variable-lag Transfer Entropy (VL-Transfer Entropy), generalizations that relax the fixed-lag assumption and allow causes to influence effects with arbitrary, dynamically changing delays. The core technical idea is to use the optimal warping path of Dynamic Time Warping (DTW) to align a reconstructed version of the cause time series to the effect, then run Granger/Transfer-Entropy machinery on that alignment, with a Bayesian Information Criterion (BIC) difference ratio (for VL-Granger) and a transfer-entropy ratio (for VL-Transfer Entropy) as the inference criteria. The authors prove the new relations are proper generalizations (traditional definitions are the special case of all-constant lags) and that VL-Granger always yields lower-or-equal residual variance than fixed-lag Granger. They also prove that initiators of collective behavior are exactly the time series that VL-Granger-cause an aggregate collective pattern, linking the framework to the Coordination Initiator Inference Problem. Across synthetic (pairwise and group-level) and real-world datasets (schools of fish, troop of baboons, gas furnace, Old Faithful geyser), the variable-lag methods outperform their fixed-lag counterparts, and the methods are released as the R-CRAN package VLTimeCausality.

## Key facts it relies on
- Definition 5.2 (VL-Granger causal relation): adds a term over a DTW-reconstructed cause X*(t-i) = X(t-i+1-Δ_{t-i+1}) to the regression residual r*_YX; X VL-Granger-causes Y if Var(r*_YX) is less than the variance of both r_Y and r_YX.
- Proposition 5.3 and 5.4: if all delays are constant (∀t, Δ_t = Δ) then r*_YX = r_YX, so VL-Granger reduces to standard Granger; and when delays vary, VAR(r*_YX) < VAR(r_YX), so VL-Granger has lower-or-equal variance — establishing it as a proper generalization.
- VL-Transfer Entropy (Eq. 9) uses a variable-lag history X̃_{t-1} = X(t-1-Δ_{t-1}),...,X(t-l-Δ_{t-l}); Proposition 6.1 shows that setting Δ_t = 0 for all t recovers ordinary Transfer Entropy.
- DTW reconstruction (Algorithm 3) computes warping path P̂, normalizes Δ_t with cross-correlation, and produces an emulation similarity s(P̂) = Σ sign(Δ_t)/|P̂|, where 0 < s(P̂) ≤ 1 if X⪯Y and −1 ≤ s(P̂) < 0 if Y⪯X; implemented with the dtw R package.
- Inference criteria: BIC difference ratio r(BIC0(r_Y), BIC1(r_YX)) = (BIC0 − BIC1)/BIC0, bounded in [−∞, 1] (closer to 1 = better), with threshold γ; and Transfer Entropy Ratio T(X,Y)_ratio = T_{X→Y}/T_{Y→X}, where ratio > 1 implies X causes Y.
- Proposition 5.9 ties the framework to collective behavior: under stated ε-convergence conditions, an initiator set X VL-Granger-causes agg(U\X), solving the Coordination Initiator Inference Problem from prior work [4].
- Synthetic pairwise data: 75 datasets total (15 each across normal/ARMA generators with X≺Y or X⊀Y configurations), time series of 200 steps, embedded lag Δ=5, with Y held constant between time steps 110–170 to create variable lags; evaluated by ROC/AUC.
- Results: all variable-lag methods beat their fixed-lag originals (VL-G > G, VL-TE > TE); on group-level causal-graph inference (Table 3) VL-G had the best F1 score (0.93 precision, 0.83 recall, 0.87 F1); on real-world data (Table 4) VL-G and VL-TE detected causal relations in all four datasets while G failed on fish and Old Faithful, and TE failed on Old Faithful.
- Time complexity: VL-G is O(T·δmax); Transfer Entropy (and thus VL-TE) is at most O(T^3), reducible to O(1/√T) convergence under a Markov-chain property (Kontoyiannis & Skoularidou).
- Real-world datasets: golden shiners (~70 fish, 10 trained, ~600 steps), olive baboons (16 of 26 with full GPS, 600 steps, ID3 as initiator), gas furnace (296 steps), Old Faithful geyser (298 steps).

## Critical notes from the literature
- The authors explicitly state they did not include nonlinear datasets in their simulation analysis, and they expect linear measures (VL-Granger, Granger) to outperform nonlinear ones (Transfer Entropy, VL-Transfer Entropy) on linear data while the reverse should hold on nonlinear data — so the reported advantage of linear VL-G partly reflects the linear nature of the synthetic data.
- On the group-level aggregate task (Group: X≺Y column, Table 3), VL-G performed poorly at default γ=0.3 (accuracy 0.23) and only reached 0.93 after relaxing γ to 0.01, while simple G/CG/SIC did well; the authors attribute this to weak causal signal in complicated aggregated time series requiring threshold tuning.
- Transfer-entropy bootstrapping helped on synthetic pairwise data but "almost failed to detect anything" on real-world datasets and decreased group-level performance, which the authors attribute to weak causal signals in those datasets.
- Like other Granger/Transfer-Entropy methods, the framework inherits standard assumptions: unconfoundedness, that all relevant variables are included, and that the maximum lag δmax is supplied as input (suggested heuristic: a large fraction such as half of the series length, with a compute trade-off).
- "Causality" here means specifically Granger's predictive causality (improved prediction), not interventional/mechanistic causation.

## Key topics covered
Granger causality; Transfer Entropy; variable-lag / arbitrary-lag causal inference; Dynamic Time Warping (DTW); time series alignment and warping paths; BIC difference ratio; transfer entropy ratio; Markov block bootstrap for significance; collective behavior and leader-follower / initiator inference; Coordination Initiator Inference Problem; ε-convergence and aggregate time series; ROC/AUC, precision/recall/F1 evaluation; VLTimeCausality R-CRAN package.

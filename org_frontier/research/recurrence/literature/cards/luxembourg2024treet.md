---
citekey: luxembourg2024treet
title: {TREET}: Transfer Entropy Estimation via Transformers
authors: Luxembourg, Omer and Tsur, Dor and Permuter, Haim
year: 2024
doi: 10.48550/arXiv.2402.06919
arxiv: null
journal: arXiv preprint
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2402.06919
sha256: 8182aece54c8d5dba28404eead130184f4405d2b1f0ab434582c52990ef5ffd6
pdf_path: literature/pdfs/luxembourg2024treet.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Transfer entropy (TE) measures the directed, asymmetric flow of information from the past of one process onto the present of another, but estimating it is hard when the data distribution is unknown and the temporal memory order is long. This paper introduces TREET (TRansfer Entropy Estimation via Transformers), a neural estimator that recasts TE as a difference of two Kullback-Leibler divergences, applies the Donsker-Varadhan (DV) variational representation, and optimizes the resulting potentials with attention-based networks adapted via a custom "fixed past causal attention" (FPCA) mask. The authors prove TREET is a strongly consistent estimator of order-l TE for jointly stationary, ergodic processes. They further build a neural distribution generator (NDG), motivated by the functional representation lemma, that jointly optimizes the input distribution to estimate channel capacity (which equals the directed-information rate). Empirically, on an extended synthetic benchmark TREET tracks the ground truth even at memory order l=99 while baselines TENE and Copnet break down; it estimates AWGN, Gaussian MA(1) and AR(1) channel capacities (with and without feedback) in agreement with analytical solutions; it yields conditional density estimates as a byproduct that match or beat DINE, MDN, KDE and Kalman baselines; and on the Santa Fe Apnea physiological dataset it recovers that breathing transfers more information to heart rate than the reverse direction.

## Key facts it relies on
- TE is defined (Definition 1) as TE_{X→Y}(t;k,l) := I(X^{t}_{t-l}; Y_t | Y^{t-1}_{t-k}); for jointly stationary processes the time index drops and TE_{X→Y}(k,l) := I(X^l; Y_l | Y^{l-1}_{l-k}); when k=l the notation TE_{X→Y}(l) is used.
- Their TE definition includes X_t (unlike prior work [1],[16],[22],[33] which uses I(X^{l-1}; Y_l | Y^{l-1}_{l-k})), which makes TE reduce to MI for jointly i.i.d. processes, i.e. TE_{X→Y}(0,0) = I(X;Y).
- The estimator rests on representing TE as a subtraction of two KL divergences w.r.t. an absolutely continuous reference distribution (Lemma 2), then applying the Donsker-Varadhan representation (Theorem 2): D_KL(P||Q) = sup_f { E_P[f] - log E_Q[e^f] }, with expectations replaced by sample means.
- Theorem 3 (consistency): for jointly stationary, ergodic processes, TREET implemented with causal transformers is a strongly consistent estimator of TE_{X→Y}(l); proof proceeds in representation, estimation, and approximation steps and relies on universal approximation of (causal) transformers (Theorem 1).
- FPCA uses a Toeplitz-like banded mask M' (M'[i,j]=1 if j-i<l and j>=i, else -infinity) so each query attends only to the current and previous l-1 inputs; attention complexity is O(L*l*d_o); the same shared-weight network computes both DV terms, the second reusing keys/values via a "modified FPCA"; reference samples Ye are drawn from the uniform measure on the bounding box of the current Y batch.
- Benchmark (Table I): on the threshold system of Eq. (32) with ρ=0.9, batch size 1024, TREET stays close to ground truth across memory orders up to l=99 (e.g. ground-truth 0.829 at λ=-3, TREET 0.829 at l=99), whereas TENE and Copnet diverge for larger l (entries marked >10 or <-10).
- Channel capacity / NDG: capacity equals the DI rate (feedforward C_FF and feedback C_FB defined in Remark 1, Eqs. 28-29); Lemma 3 shows an NDG with input length l achieves the maximal order-l TE. TREET+NDG matches analytical AWGN capacity C=0.5*log(1+P/σ^2), and Gaussian MA(1)/AR(1) feedforward (water-filling) and feedback capacities.
- Long-memory test GMA(100) (Z_t = N_t + α N_{t-100}): true capacity 0.405 nats at 0 SNR (Table II); TREET attains best estimates for memory length l>100 with absolute error below 14%, degrading to no less than 28% error when l<100; attention weights concentrate at relative lag i=100 when given sufficient l=130, but become noisy at l=90.
- Density estimation (Table III, classic HMM, k=0, α=0.9, β=0, γ=0.5, σ^2=0.5, memory l=3): TREET matches or beats DINE, MDN, conditional KDE and the Kalman filter on KL divergence and total variation; conditional density is recovered as a byproduct via P_{Yt|Y^{t-1}} ≈ exp(D-hat) * P_{Yet} (Eq. 33), requiring no extra training, with numerical normalization over a grid.
- Apnea feature analysis: Santa Fe Time Series Competition dataset, recorded from a single Apnea patient, sample rate 2 Hz, three variables (heart rate, chest volume/respiration force, blood oxygen); TE_{Breath→Heart}(k,2) is consistently higher than TE_{Heart→Breath}(k,2), and TE decreases as the Y-history length k increases, consistent with [4].

## Critical notes from the literature
- Consistency (Theorem 3) is established only for jointly stationary, ergodic processes; TREET targets finite-order TE rather than the infinite-memory DI rate that DINE estimates, and equality of TE and DI requires additional Markov assumptions (Lemma 1).
- The authors note that neural information-theoretic estimators (e.g. MINE) are themselves criticized for high gradient variance, bias, and training instability in high-dimensional settings [28]-[30]; they explicitly acknowledge that larger input dimensions still cause estimation error and remain "an open academic research" problem.
- TE estimates degrade sharply when the chosen memory order l is shorter than the true process memory (GMA(100): >=28% absolute error and noisy/unstable attention when l<100), so correct order selection is load-bearing.
- The DV-derived density (Eq. 33) is unnormalized (recovered only up to an additive constant / log-likelihood-ratio), requiring numerical grid normalization; the reference distribution is heuristically taken as uniform over the data bounding box.
- The Apnea analysis uses data from a single diseased patient, and the manuscript is described on its title page as submitted to an IEEE journal and currently under review.

## Key topics covered
Transfer entropy; directed information and DI rate; Donsker-Varadhan representation; neural estimation (MINE, DINE, TENE, Copnet, KSG/KNN, KDE); transformers and attention; fixed past causal attention (FPCA) and causal masking; consistency of estimators; functional representation lemma; neural distribution generator (NDG); channel capacity (feedforward and feedback; AWGN, Gaussian MA(1)/AR(1)); water-filling; conditional density estimation; hidden Markov models; Santa Fe Apnea physiological time series; Granger causality.

---
citekey: tsur2024treet
title: TREET: TRansfer Entropy Estimation via Transformers
authors: Tsur, Dor and Aharoni, Ziv and Goldfeld, Ziv and Permuter, Haim
year: 2024
doi: null
arxiv: 2402.06919
journal: arXiv
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2402.06919
sha256: 8182aece54c8d5dba28404eead130184f4405d2b1f0ab434582c52990ef5ffd6
pdf_path: literature/pdfs/tsur2024treet.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces TREET (TRansfer Entropy Estimation via Transformers), an attention-based neural estimator of transfer entropy (TE) for stationary, ergodic continuous-valued stochastic processes. TE is an asymmetric, information-theoretic measure of directed information flow between two processes; the authors define it (with memory parameters k, l) as the conditional mutual information I(X^l; Y_l | Y^{l-1}) and estimate it by decomposing TE into a difference of two Kullback-Leibler divergences, each represented through the Donsker-Varadhan (DV) variational formula and optimized with a causal transformer. The core architectural contribution is a "fixed past causal attention" (FPCA) mask, a Toeplitz-like banded mask that restricts each query to the current and previous l-1 inputs, plus a modified FPCA for the reference-distribution term; the two DV potentials share network weights. They prove TREET is a strongly consistent estimator of TE for jointly stationary, ergodic processes. To enable optimization, they add a neural distribution generator (NDG) that steers the input distribution to maximize estimated TE, which they apply to estimate the capacity of communication channels with memory (AWGN, Gaussian MA(1), Gaussian AR(1), and a long-delay GMA(100) channel). On an extended benchmark, TREET matches TENE and Copnet at memory order l=1 but, unlike them, remains accurate up to l=99; it also yields a byproduct conditional-density estimator and is applied to feature analysis of an Apnea physiological dataset, finding consistently higher TE from breathing to heart rate. (Note: the arXiv v4 PDF lists the authors as Omer Luxembourg, Dor Tsur, and Haim Permuter.)

## Key facts it relies on
- TE is defined (Definition 1) for parameters (k,l) as TE_{X→Y}(t;k,l) := I(X_{t-l}^t; Y_t | Y_{t-k}^{t-1}); for jointly stationary processes the time index is dropped, TE_{X→Y}(k,l) := I(X^l; Y_l | Y_{l-1}^{l-1}). The authors' definition includes X_t, so it reduces to MI when processes are jointly i.i.d.: TE_{X→Y}(0,0) = I(X;Y).
- TREET decomposes TE into a difference of two (conditional) KL divergences (Lemma 2) and estimates each via the Donsker-Varadhan representation (Theorem 2: D_KL(P||Q) = sup_f E_P[f] − log E_Q[e^f]), replacing expectations with sample means; the two DV potentials are optimized by mini-batch gradient ascent and share the same transformer weights.
- Fixed Past Causal Attention (FPCA) uses a banded Toeplitz-like mask M' (M'_{i,j}=1 if j−i<l and j≥i, else −∞) so each query attends only to the current and previous l−1 inputs; the attention complexity is O(L l d_o). A modified FPCA reuses keys/values to compute the reference-distribution term; reference samples Ỹ are drawn from the uniform measure on the bounding box of the current batch.
- Theorem 3 establishes that, for jointly stationary, ergodic processes and TREET implemented with causal transformers, TREET is a strongly consistent estimator of TE_{X→Y}(l) (P-a.s.). The proof has representation, estimation, and approximation steps; transformers are a universal approximation class for sequence-to-sequence maps (Theorem 1, citing [36]).
- On the extended benchmark (system Eq. 32 with ρ=0.9, varying threshold λ and order l, batch size 1024), TE_{X→Y}(l)=TE_{X→Y}(1) for all l≥1. At l=1 TREET matches TENE and Copnet, but as l grows TENE and Copnet diverge (values reported as >10 or <−10), while TREET stays accurate even at l=99 (e.g. ground-truth 0.829 at λ=−3; TREET gives 0.829 at l=99).
- For the long-delay GMA(100) channel (Z_t = N_t + αN_{t-100}) at 0 SNR, true capacity is 0.405 nats; TREET attains its best estimates for memory l≥100 with absolute error <14%, but error is ≥28% when l<100 (Table II). DINE (LSTM/bptt) struggles under long memory.
- The NDG (neural distribution generator) is motivated by the functional representation lemma; Lemma 3 shows input sequence length l suffices to achieve maximal TE TE*_{X→Y}(l). Channel capacity equals the DI rate, which under stated conditions equals TE; capacities are estimated for AWGN (C = 0.5 log(1+P/σ²)), Gaussian MA(1) (water-filling for feedforward; quartic-polynomial root for feedback), and Gaussian AR(1).
- Density estimation is a byproduct: the optimized D̂_{Y_l|Y^{l-1}||Ỹ} network gives the log-likelihood ratio between P_{Y_t|Y^{t-1}} and a known reference density, so P_{Y_t|Y^{t-1}} ≈ exp(D̂)·P_{Ỹ}, normalized numerically (Eq. 33). On HMM tasks (Tables III, IV) TREET matches or beats DINE, MDN, conditional KDE, and the Kalman filter, pulling ahead for state delays k≥10.
- The Apnea case study uses the Santa Fe Time Series Competition dataset (heart rate, chest volume/respiration, blood oxygen; 2 Hz sample rate). TE from breathing to heart (TE_{Breath→Heart}) is consistently higher than the reverse for every history length k, and estimated TE decreases as the conditioning history length of Y grows, consistent with prior findings ([4],[52]).

## Critical notes from the literature
- The paper acknowledges that prior neural information-theoretic estimators (MINE-style) suffer high variance in gradient estimates, bias, and training instability in high-dimensional settings ([28]–[30]); it positions TREET against these but notes that larger input dimensions still cause estimation error that remains "an open academic research" problem.
- Consistency (Theorem 3) is proven only under joint stationarity and ergodicity; the method is designed for finite-order TE on stationary processes, and the channel-capacity application requires conditions under which TE equals the DI rate.
- TREET's accuracy degrades sharply when its memory parameter l is shorter than the true process memory (GMA(100): error ≥28% for l<100), so the user must supply a sufficiently long input length; this is a scope limitation relative to RNN/state-based methods like DINE that can in principle propagate state beyond their bptt window (though DINE empirically still underperformed on long memory here).
- The benchmark, channel-capacity, and density experiments are primarily on synthetic Gaussian/HMM processes; the single real-world application (Apnea) is from one diseased patient and validates, rather than independently establishes, known physiological findings.
- The reported TE definition deliberately differs from the conventional Schreiber/[16],[22] definition by including X_t (so TE(0,0)=I(X;Y)); comparisons to TENE/Copnet required re-implementing those baselines to handle longer conditioning contexts.

## Key topics covered
Transfer entropy; directed information and DI rate; Donsker-Varadhan representation; neural estimation of information measures; transformers and attention; causal/fixed-past causal attention (FPCA) masking; universal approximation of transformers; consistency of estimators; channel capacity (AWGN, Gaussian MA(1), AR(1), GMA(100); feedforward and feedback); neural distribution generator (NDG); functional representation lemma; conditional density estimation; mixture density networks, KDE, Kalman filter, DINE, TENE, Copnet, KSG, Granger causality baselines; Apnea/Santa Fe physiological time series; stationary and ergodic processes.

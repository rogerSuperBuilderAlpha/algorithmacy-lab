---
citekey: mccracken2014convergent
title: Convergent cross-mapping and pairwise asymmetric inference
authors: McCracken, James M. and Weigel, Robert S.
year: 2014
doi: 10.1103/PhysRevE.90.062903
arxiv: null
journal: Physical Review E
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1407.5696
sha256: c15a00684b4233b0a25b1d04f22cac1be37fb03d8f373e8ae9d76e4bfb1c60cf
pdf_path: literature/pdfs/mccracken2014convergent.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper critically examines Convergent Cross-Mapping (CCM), a state-space-reconstruction technique introduced by Sugihara et al. (2012) that is reported to be "a necessary condition for causation" able to distinguish causality from correlation. Using simple linear, nonlinear, and physical (RL-circuit) example systems in which the intuitive driver is known, the authors show that the sign of the CCM difference statistic Δ = C_YX − C_XY does not reliably identify the intuitive driver and that the inferred "CCM cause" can flip depending on system parameters. For instance, in a series RL circuit driven by a sinusoidal voltage, CCM identifies voltage as the driver of current for some source frequencies Ω and current as the driver of voltage for others, even though physical intuition fixes voltage as the driver. The authors then propose Pairwise Asymmetric Inference (PAI), a modification using a multivariate (cross-augmented) shadow manifold and a difference Δ′ = C_Y(YX) − C_X(XY), and show that for all of their example systems the sign of Δ′ agrees with the intuitive driver consistently across parameter domains. They conclude PAI is more consistent than CCM but still has open difficulties (e.g., it does not account for differing self-estimation skill of the two series) and may be useful chiefly as exploratory data analysis.

## Key facts it relies on
- CCM is closely related to simplex projection; the CCM correlation is defined as the squared Pearson correlation, C_YX = [ρ(Y, Y|X̃)]², between the original series Y and the estimate Y|X̃ obtained from cross-mapping with X's shadow manifold. (This squaring differs from Sugihara et al., who use the un-squared coefficient.)
- The CCM algorithm has five steps (build shadow manifold X̃ via delay vectors of embedding dimension E and lag τ; find the E+1 nearest neighbors; compute exponential weights w_i = u_i/N with u_i = e^(−d_i/d_1); estimate Y|X̃; compute the correlation), and depends on embedding dimension E and lag τ.
- CCM causality is decided by the sign of Δ = C_YX − C_XY; if Δ < 0 then X "CCM causes" Y. In the coupled logistic map system (Eqns. 2–3), β_xy > β_yx is intended to imply Δ > 0 ("Y CCM causes X"). Coupling parameters were varied over [10⁻⁶, 1] in steps of 0.02 (Figure 1, library lengths L = 100, 400, 800, 1200).
- Linear example (X_t = sin(t); Y_t = A X_{t−1} + B η_t, with A,B ∈ [0,10] in increments of 0.1, η_t ~ N(0,1)): with E = 3, τ = 1, L = 2000, the sign of Δ depends on A and B even though the intuitive conclusion "X drives Y" does not; for (A,B) = (2.6,2.6) and (3.0,2.6), Δ is more negative at short L and converges near zero as L increases.
- Nonlinear example (Y_t = A X_{t−1}(1 − B X_{t−1}) + C η_t, with A,B,C ∈ [0,5] in increments of 0.5, L = 2000): the sign of Δ can depend on all three parameters A, B, C, again failing to reflect the intuitive driver.
- RL-circuit example (noise-free; dI/dt = V(t)/L − (R/L)I, V(t) = sin(Ωt), L = 10 H, R = 5 Ω, solved with MATLAB ode45): evaluating CCM with E = 2, τ = 1 for Ω ∈ [0.01, 2.0] in steps of 0.01, the sign of Δ = C_VI − C_IV changes over the domain (tested for E = 2, 3, 4), so CCM does not consistently identify V as the driver of I.
- PAI uses a multivariate shadow manifold, e.g., X̃_t = (X_t, X_{t−τ}, …, X_{t−(E−1)τ}, Y_t), giving estimate X|(XY) and correlation C_X(XY); the PAI statistic is Δ′ = C_Y(YX) − C_X(XY). For the logistic system with r_x = r_y = 3.7, X_0 = 0.2, Y_0 = 0.4, β_xy = 0, β_yx = 0.32 (E = 2, τ = 1, L = 1000), CCM gives Δ ≈ 0.11 − 0.97 = −0.86 and PAI gives Δ′ ≈ −3×10⁻⁴, both indicating "X drives Y."
- For the linear, nonlinear, and RL-circuit examples, PAI yields Δ′ < 0 for all parameter values in the plotted domains (∀A,B; ∀A,B,C; ∀Ω), agreeing with the intuitive driver, whereas CCM's Δ changed sign.

## Critical notes from the literature
- The authors stress this is a critique of CCM's consistency, not a claim that CCM failed in prior applications: they explicitly note "the domain of applicability of CCM remains an open question" and that the cited applications (sardine-anchovy-temperature, climate effects on sardines, CO2 growth-rate drivers, insect physiology, developmental psychology) may have worked as expected despite CCM's apparent failure in these toy examples.
- PAI is not free of difficulties: Δ′ does not account for differences in self-estimation skill between series. For the logistic example C_YY − C_XX ≈ 1.5×10⁻³ (both self-correlations > 0.99), and an alternative measure Δ′′ = |C_Y(YX) − C_YY| − |C_X(XY) − C_XX| ≈ 3.9×10⁻⁴ does NOT agree with intuition, despite Δ and Δ′ agreeing — "such questions are still open."
- The paper frames its evaluation around appeals to "intuition" and acknowledges intuition can fail; citing Pearl, it notes that determining true causality from time series alone may be impossible. The Alice/Bob/Charlie thought experiment shows PAI gives consistent results but does not resolve the deeper ambiguity of which variable is the cause.
- Granger causality and transfer entropy (the two dominant causal-inference families, known to be equivalent under certain conditions) are noted not to be causality as understood in physics; the authors argue a similar conclusion holds for CCM. They also note there are currently no published equivalence conditions relating CCM to transfer entropy or Granger causality.

## Key topics covered
- Convergent Cross-Mapping (CCM) and its five-step algorithm
- Pairwise Asymmetric Inference (PAI) and the Δ′ statistic
- State-space reconstruction / shadow manifolds, delay embedding (E, τ)
- Simplex projection and nearest-neighbor weighting
- Time-series causality / driver identification
- Coupled logistic map, linear and nonlinear noisy systems, RL circuit
- Convergence of CCM correlations with library length L
- Comparison with Granger causality and transfer entropy
- Parameter-dependence and inconsistency of CCM causal inference
- Squared vs un-squared Pearson correlation definition

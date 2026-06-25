---
citekey: wergen2011correlations
title: Correlations Between Record Events in Sequences of Random Variables with a Linear Trend
authors: Wergen, Gregor and Franke, Jasper and Krug, Joachim
year: 2011
doi: 10.1007/s10955-011-0307-7
arxiv: null
journal: Journal of Statistical Physics
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1105.3915
sha256: d4c17c7b02324b00ccdf52f880c4ad5e42f3c4a75c37d3d8184271e87e65e5db
pdf_path: literature/pdfs/wergen2011correlations.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether record events remain stochastically independent when the underlying random variables are independent but not identically distributed, specifically under the Linear Drift Model (LDM) in which each variable is Y_l = X_l + cl (an i.i.d. part X_l with density f shifted by a constant drift c per step). The authors derive general exact and small-c expansion expressions for the normalized correlation l_{N,N-1}(c) = p_{N,N-1}/(p_N p_{N-1}) between consecutive record events and analyze it across the three extreme-value universality classes (Weibull, Gumbel, Frechet). They find a rich pattern: correlations are generally negative ('repulsive') for bounded-support Weibull-class distributions, positive ('attractive') for heavy-tailed Frechet-class (power-law) distributions, and of either sign in the Gumbel class depending on the stretching exponent, with the pure exponential tail (β = 1) being the marginal, nearly correlation-free case. The sign and N-scaling of correlations are captured by a unified scaling picture in terms of the generalized Pareto shape parameter κ. The most counterintuitive result is strong positive record correlations for power-law-tailed distributions (e.g. l_{N,N-1} ≈ 3 for Pareto μ = 2 at large N), which the authors propose could serve as a distribution-free test for detecting power laws.

## Key facts it relies on
- The Linear Drift Model (LDM) is defined by Y_l = X_l + cl with positive drift constant c, so the density f_l(y) = f(y - cl) keeps its shape but shifts position by c each step (Eq. 1).
- The key quantity studied is the normalized joint record probability l_{N,N-1}(c) ≡ p_{N,N-1}/(p_N p_{N-1}) (Eq. 3); l = 1 means uncorrelated, l < 1 repulsion, l > 1 attraction.
- For i.i.d. variables (c = 0), p_N = 1/N and the joint probability factorizes (p_{N,N-1} = 1/[(N-1)N] = p_N p_{N-1}), so record events are stochastically independent; the same factorization holds for the LDM with a Gumbel i.i.d. part f(x) = exp(-e^{-x} - x) for all c (Eqs. 9, 13).
- Small-c expansion gives l_{N,N-1}(c) = 1 + c·J(N) + O(c^2), where the sign of J(N) depends on the integral I(N) = ∫ f^2(x) F^N(x) dx (Eqs. 15, 19, 20).
- Weibull class (bounded support): for a uniform distribution on [-a, a], l_{N,N-1}(c) ≈ 1 - (c/4a)N^2, i.e. negative correlations growing rapidly with N (Eq. 30); for the broader family f_ξ(x) = ξ(1-x)^{ξ-1}, l_{N,N-1}(c) ≈ 1 - (c/2)Γ(2 - 1/ξ)N^{1+1/ξ} (Eq. 34).
- Gumbel class: for the exponential distribution with mean a, l_{N,N-1}(c) ≈ 1 + c/(2a) — weak, positive, N-independent correlations (Eq. 35); for the Gaussian (width σ), (l - 1) ∝ -(c/σ)·N·sqrt(ln(N^2/8π)) — negative and strongly N-dependent (Eq. 37).
- For generalized Gumbel-type f(x) = A_β exp(-|x|^β), correlations are negative for β > 1 and positive for stretched exponentials β < 1, with the pure exponential β = 1 as the boundary where J(N) becomes a positive constant (Eq. 40).
- Frechet class: for the Pareto distribution f(x) = μx^{-μ-1} (μ > 1), l_{N,N-1}(c) ≈ 1 + (c/2)Γ(2 + 1/μ)N^{1-1/μ} — positive correlations growing sublinearly with N (Eq. 44); e.g. l_{N,N-1} ≈ 3 at large N for μ = 2.
- A unified scaling picture uses the generalized Pareto distribution f(x) = (1 + κx)^{-(κ+1)/κ}: the crossover time scale N* ∝ c^{-ν} with ν = 1/(1-κ), and J(N) ≈ (κ/2)N^3 I(N) ∼ N^{1-κ}, so correlations are positive for κ > 0 (Frechet) and negative for κ < 0 (Weibull), scaling sublinearly vs. superlinearly with N respectively (Eqs. 48-52).
- By Ballerini and Resnick's result, the infinite product G_c(x) = lim ∏ F(x + cj) exists and is nonzero whenever f has a finite first moment, so for c > 0 the record rate p_N, joint probability p_{N,N-1}, and ratio l have finite nonzero N→∞ limits; correlations also decay to zero as the inter-record distance k → ∞ (Eqs. 21-23, 29).

## Critical notes from the literature
- The main analytic results come from a small-c (leading-order) expansion valid only for c/σ ≪ N^{-1}; the authors explicitly note their analytical predictions are "not very useful" / valid only in a small regime for c > 0 and small N in the Weibull and Gaussian cases (Figs. 4, 6).
- For the Frechet (heavy-tailed) class the large-N asymptotics is hard to verify numerically because convergence to the N→∞ limit is very slow (the crossover scale N* diverges fastest there, ν > 1); the authors only conjecture that the limit l*(c) exists for c < 0 in this class.
- For c < 0 the behavior of l is partly undetermined: in a Weibull-class example (negative exponential distribution) l_{N,N-1} = exp[-(c/2)(N-1)(N-2)] diverges without bound as N → ∞, suggesting the limiting function l*(c) is singular/discontinuous at c = 0 (Eqs. 26-28).
- The authors flag that a previous study of records from independent RVs with increasing variance (Krug 2007, ref. 26) found only negative correlations, contrasting with the positive correlations found here for heavy tails.
- Open questions explicitly stated: the structure of correlations in the stationary N→∞ limit and rigorous treatment of the c < 0 case remain unresolved; the authors call for rigorous work along the lines of Ballerini and Resnick (ref. 24).

## Key topics covered
Record statistics; extreme value theory (Weibull, Gumbel, Frechet classes); Linear Drift Model; stochastic independence of records; correlations between record events; normalized joint record probability; small-drift expansion; generalized Pareto distribution and shape parameter κ; Pareto/heavy-tailed (power-law) distributions; stretched exponential distributions; Gaussian and uniform distributions; crossover time scale N*; Ballerini-Resnick finite-mean condition; distribution-free test for power laws; climate/temperature record-breaking applications.

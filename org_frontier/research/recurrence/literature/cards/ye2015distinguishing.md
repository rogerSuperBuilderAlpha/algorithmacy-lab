---
citekey: ye2015distinguishing
title: Distinguishing time-delayed causal interactions using convergent cross mapping
authors: Ye, Hao and Deyle, Ethan R. and Gilarranz, Luis J. and Sugihara, George
year: 2015
doi: 10.1038/srep14750
arxiv: null
journal: Scientific Reports
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/srep14750.pdf
sha256: fe474488b8b996dea1e0f22a63f317dee2edd2f9d5a1518891c474f701887144
pdf_path: literature/pdfs/ye2015distinguishing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses inferring causal relationships, including their time delays, from observational time series alone, where controlled experiments are infeasible. It extends convergent cross mapping (CCM) — a nonlinear state-space reconstruction method based on Takens' Theorem in which the causal effect of x on y is measured by how well an embedding of y can cross map (predict) x — by explicitly introducing a cross-map lag l, allowing prediction of x(t+l) from the reconstructed state y(t). The authors apply this "extended CCM" to a two-species coupled logistic map, a unidirectional-forcing logistic system that produces generalized synchrony, a four-species transitive causal chain, Veilleux's Paramecium-Didinium predator-prey experiment, CO2 and temperature from the Vostok ice core, and chlorophyll-a/sea-surface-temperature from the Scripps pier. The key result is that the sign and magnitude of the optimal cross-map lag distinguish true bidirectional causality (negative optimal lag in both directions) from synchrony driven by strong unidirectional forcing (negative lag in the true causal direction, positive lag in the non-causal direction). The lag structure also separates direct from indirect links in transitive causal chains (more separation -> more negative lag, lower skill) and reveals interaction-specific response delays in real systems. The authors note that a single time series carries all dynamic information except when stochastic drivers with unique information are present, in which case those drivers must be included at the appropriate lag.

## Key facts it relies on
- CCM (Sugihara et al., Science 338, 496-500, 2012) builds a time-delay embedding from y and tests how well it recovers x; per Takens' Theorem, if x influences y then x's history is recoverable from y alone. Standard cross map uses lag l=0; the extension cross maps to x(t+l) for arbitrary l.
- For the bidirectional two-species logistic map (eq. 1: x(t+1)=x(t)[3.78-3.78x(t)-0.07y(t)], y(t+1)=y(t)[3.77-3.77y(t)-0.08x(t-tau_d)]), with tau_d=0 the optimal cross-map lag is l=-1 in both directions; for tau_d=2 or 4 the y-xmap-x lag shifts back by the corresponding delay. Analyzed with E=2, tau=1, 100 random libraries of 200 vectors (initialized x(1)=0.2, y(1)=0.4, 3000 steps; library points 101-2000, prediction 2001-3000).
- For the strong unidirectional system (eq. 2: x(t+1)=x(t)[3.8-3.8x(t)], y(t+1)=y(t)[3.1-3.1y(t)-0.8x(t)]) that produces generalized synchrony, the optimal lag from y to x is negative (l ~ -1) while from x to y it is positive (l ~ 3 > 0); the positive lag flags unidirectional causality despite synchrony.
- In the four-species transitive chain (eq. 3, y1->y2->y3->y4, E=4, tau=1): direct links show high skill at small negative lag (l ~ -2); indirect links separated by one node show moderate skill at l ~ -4; the y1-to-y4 link (separated by two nodes) is weakest at l ~ -6. Cross-map skill showed more variance and is a less reliable indicator of direct vs. indirect than lag.
- Veilleux's Paramecium-Didinium experiment (dataset 11a, 71 data points, E=3, tau=1, leave-one-out cross-validation) shows bidirectional causality with roughly equal predictability at optimal lags; optimal lag -1 for Paramecium xmap Didinium (prey respond fast) and -4 for Didinium xmap Paramecium (predator numerical response is delayed).
- Vostok ice core CO2 and temperature (Petit et al. reconstruction, ~410,000-412,000 years, interpolated to 1000-year spacing, E=4, tau=1, 100 libraries of 100, 412 points): bidirectional causality; CO2's effect on temperature is near-instantaneous, temperature's effect on CO2 has an optimal CCM lag of ~3000 years (a positive feedback noted as also analyzed by van Nes et al.).
- Scripps pier weekly SST and chlorophyll-a (June 30 2008 - May 26 2014, E=4, tau=1 = 1 week, 100 libraries of 100, 306 points): no effect of chlorophyll-a on SST, but a causal effect of SST on chlorophyll-a with an optimal lag of ~3 weeks (effect of SST occurs with a 1-4 week lag).
- Heuristic from theory: even with no real causal delay, optimal predictability can occur at l<0 because information propagates forward and backward in time; a time-centered embedding gives an expected optimal lag l=(E-1)tau/2, and any lag within -(E-1)tau <= l <= 0 is consistent with an influence of x on y with no time delay.

## Critical notes from the literature
- The motivating limitation the paper itself states: standard CCM cannot distinguish true bidirectional causality from strong unidirectional forcing that induces generalized synchrony (Rulkov et al. 1995), because synchrony makes CCM appear positive in both directions; the lag extension is the proposed remedy.
- The lag-distinguishability of synchrony only works "when there is a detectable lag in the response time between causes and effects" — instantaneous causation would not produce the diagnostic positive lag.
- The authors concede Granger causality (which they argue fails in deterministic dynamic systems, after Sugihara et al. 2012) can correctly identify causality in systems consisting solely of stochastic components with unique information; CCM is needed specifically when both cause and effect have deterministic dynamics.
- Cross-map skill (Pearson rho between predicted and observed) is flagged as a less reliable discriminator of direct vs. indirect causation than lag; outliers in the random-coefficient simulations are attributed to stable dynamics (rho reaching 1) in models simulated without process error.
- The authors note this general "delay/direction of information flow" approach has been explored elsewhere (e.g., Schumacher et al.); their contribution is showing the CCM framework can be directly extended for temporal delays rather than being first to consider delayed information flow.

## Key topics covered
Convergent cross mapping (CCM); extended/time-lagged CCM; Takens' Theorem and state-space (time-delay) reconstruction; simplex projection / nearest-neighbor forecasting; cross-map skill (Pearson rho); generalized synchrony vs. bidirectional causality; transitive causal chains (direct vs. indirect links); Granger causality and its limits in deterministic systems; coupled logistic maps; predator-prey dynamics (Paramecium-Didinium); paleoclimate causality (Vostok CO2-temperature feedback); marine ecological time series (SST-chlorophyll-a); embedding dimension E and time step tau; stochastic drivers; causal time delays for forecasting and management.

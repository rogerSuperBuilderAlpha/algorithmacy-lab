# Q214 — Stage 4 methods

For each triad type: the Boolean form, the third party tested, and the bypass restored. A reader should
reproduce every classification from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`).
- The instrument: `classifier/contingency.py` (`contingency_test`, `add_bypass`). The probe does not modify it.
- Python: run from the repo root with `venv-4.0`, `PYPHI_WELCOME_OFF` set.

## The four structural templates (from q213 / the catalog)
Labels (A, M, C): A the upstream party, M the third party tested, C the downstream party.
- **relay** (→ contingent): A'=C, M'=A, C'=M; bypass C reads A (replace). A mandated/maintained pass-through.
- **conjunctive** (→ necessary): A'=M, M'=A∧C, C'=M; bypass C reads A (replace). An integrating mediator.
- **additive** (→ partial): A'=M, M'=A∧C, C'=M; bypass C'=M∨A (add). Integrator with a parallel back-channel.
- **free** (→ reducible): A'=C, M'=A, C'=A; bypass C reads A (replace, vacuous). The party already sidelined.

## Instrument control (run first)
The conjunctive triad must read triadic at Φ=2.000000 before any classification is trusted.

## Triad types and their forms
Each literature type maps to a template; the model is a worked illustration of the structure the theory names.

| type | theory (cite key) | template | predicted |
|---|---|---|---|
| simmelian_mediator | simmel1950 | conjunctive | intrinsic |
| tertius_gaudens | obstfeld2014brokerage, quintane2016howbrokers | relay | contingent |
| tertius_separans | lee2023strain, grosser2019measuring | relay | contingent |
| divide_et_impera | simmel1950 | relay | contingent |
| tertius_iungens_integrating | obstfeld2005tertius | conjunctive | intrinsic |
| tertius_iungens_selfliquidating | obstfeld2005tertius, collinsdogrul2012tertius | free | reducible |
| conduit_unmandated | obstfeld2014brokerage | free | reducible |
| conduit_mandated | obstfeld2014brokerage | relay | contingent |
| gf_coordinator | gould1989structures | free | reducible |
| gf_gatekeeper | gould1989structures | relay | contingent |
| gf_representative | gould1989structures | relay | contingent |
| gf_liaison | gould1989structures | relay | contingent |
| gf_itinerant | gould1989structures | additive | partial |
| structural_hole_broker | burt1992structural, burt2005brokerage | relay | contingent |
| granovetter_bridge | granovetter1973weak | relay | contingent |
| two_sided_platform | rochet2003platform, armstrong2006competition | conjunctive | intrinsic |
| gatekeeping_platform | hagiu2009platforms | relay | contingent |
| market_maker | rubinstein1987middlemen | additive | partial |
| arbitrageur_friction | rubinstein1987middlemen | relay | contingent |

## The balance-theory boundary (H5)
The Heider-balance triad is modeled as a mutual signed triad: P'=Q∧R, Q'=P∧R, R'=P∧Q (every party reads both
others, all-positive balance). It is symmetric, with no source/mediator/sink asymmetry and every edge present,
so no forbidden bypass exists. The probe reads its verdict and major complex and shows that forcing the
bypass-counterfactual removes an existing edge rather than restoring a forbidden one — a category error.

## Decision rules
- H1: every gaudens-family type kind="contingent", margin=2.0.
- H2: tertius_iungens_integrating intrinsic, tertius_iungens_selfliquidating reducible.
- H3: simmelian_mediator and two_sided_platform intrinsic, margin=0.
- H4: gf_coordinator reducible; gf_gatekeeper, gf_representative, gf_liaison contingent; gf_itinerant partial.
- H5: the balanced triad is triadic with all three in the core and no forbidden edge; the test does not apply.

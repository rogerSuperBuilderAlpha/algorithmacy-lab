# q174 — methods

## Machinery

The probe imports the field bridge `org_frontier.field.rule_to_phi`: `rule_to_phi`
(rules -> TPM -> exact-Φ verdict via the IIT-4.0 classifier), `phi_ci` (bootstrap-t CI over
a coder panel of Φ readings), and `krippendorff_alpha` (nominal agreement on the coder x
unit decision matrix). Φ is not reimplemented.

## Forms

Three borderline forms. Each is a faithful triad whose max Φ_MIP is positive, paired with a
dyadic collapse reading reached by dropping the mediating coupling so the third party factors
off and Φ_MIP falls to zero. `read_recipient` is the worker-system-counterpart triad
[x1, x0&x2, x1]; `gated_mediator` and `shared_state` are the same shape with the coupling on
a different party. The collapse of each reads dyadic.

## Synthetic coder panel

Each account is read by 8 coders over 12 binary active-bit decision units. Disagreement is
set by a fraction f in [0, 1].

- Coupling unit: a graded count round(f * 8) of coders read the collapse (Φ = 0); the rest
  read the triad. This makes the per-coder Φ spread grow smoothly with f instead of
  saturating at a fixed split.
- Background units: a fraction f of the remaining units are split 50/50 across coders; the
  rest are unanimous with the value alternating per unit so the pooled labels carry variance
  and Krippendorff alpha is well defined.

The coder x unit matrix gives the measured alpha; the per-coder Φ readings feed `phi_ci`
(1200 bootstrap resamples, 95% interval). Sweeping f sweeps alpha from 1.0 down to about
0.33. Two ensembles run at seeds 0 and 1.

## Measures

For each f, averaged over the three forms: measured Krippendorff alpha, CI width
(ci_high - ci_low), and the fraction of forms whose CI brackets zero (verdict indeterminate).

- H1: Spearman rho between alpha and CI width over ensemble A, target rho <= -0.9, p < 0.01.
- H2: alpha* is the largest alpha at which the cross-zero fraction still exceeds 0.5,
  scanning ensembles A and B; the test is |alpha*_A - alpha*_B| <= 0.10.

## Instrument control

Three checks before the sweep. The faithful triad reads triadic with max Φ_MIP = 2.0. An
alpha = 1 panel of identical triadic readings returns a degenerate CI of width 0. A
verdict-invariant panel of two distinct positive-Φ readings (2.0 and 3.0), never the
collapse, returns a nonzero width whose lower bound stays above zero. The probe prints
`CONTROL ... PASS`.

## Determinism

All RNG draws use `numpy.random.default_rng` with fixed seeds (panel seeds 0 and 1, the CI
bootstrap reseeded per call). Re-running the probe reproduces the output byte-for-byte.

## Scope

Synthetic coded rule sets, not measured worker states. Boolean models, exact IIT-4.0 Φ.

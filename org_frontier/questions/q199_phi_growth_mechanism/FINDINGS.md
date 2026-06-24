# q199 — findings

On the simulated panel, within-person change in Φ_coord tracks within-person change in algorithmacy. A
multilevel model with person-mean-centered Φ_coord gives a within-person slope of ACS on the within-person
Φ deviation of +0.69, with a person-level cluster-bootstrap 95% CI that excludes 0. The bridge moves
together with the construct within a person, beyond its baseline cross-sectional association.

The within-person coupling exceeds the between-person coupling. The within slope (+0.69) is larger than
the between slope (+0.49), and the bootstrap CI on the difference (+0.20) excludes 0. The Φ-ACS link is a
person-level dynamic, not only stable selection across persons.

The instrument control passed: the faithful triad `[x1, x0&x2, x1]` reads triadic with max Φ_MIP = 2.0.
On the forced-dyadic control panel (Φ_coord ≡ 0), both slopes are 0 by construction.

| panel   | term      | slope (ACS on Φ_coord) | 95% CI (cluster bootstrap) |
|---------|-----------|------------------------|----------------------------|
| bridge  | within    | +0.6906                | [+0.6315, +0.7491]         |
| bridge  | between   | +0.4947                | [+0.4077, +0.5851]         |
| bridge  | Δ w−b     | +0.1958                | [+0.0928, +0.2978]         |
| control | within    | +0.0000                | [+0.0000, +0.0000]         |
| control | between   | +0.0000                | [+0.0000, +0.0000]         |

Panel: 300 persons x 5 waves = 1500 rows; 319 commit-form rows (Φ_coord = 2.0); 152 of 300 persons show
within-person Φ_coord change across waves.

- **H1: SUPPORTED.** Within-person slope = +0.6906, 95% CI [+0.6315, +0.7491]: above 0 and the interval
  excludes 0.
- **H2: SUPPORTED.** Within (+0.6906) exceeds between (+0.4947); Δ = +0.1958, 95% CI [+0.0928, +0.2978],
  which excludes 0.

Scope: the panel is simulated. No worker is measured. The result is evidence about the Φ bridge and the
within/between estimator on synthetic longitudinal data. The within-person coupling is built into the
data-generating model by design; the test is whether the bridge recovers it after person-mean centering.

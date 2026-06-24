# q197 — Invariance of the Φ_coord-to-ACS bridge across panel waves

A measurement bridge is only useful across time if it means the same thing at each measurement. The
survey arm derives a per-worker Φ_coord from each worker's reported coordination conditions and regresses
the Algorithmacy Competence Scale (ACS) on it. For a three-wave panel, the question is whether that
regression keeps the same form wave to wave: same slope (metric invariance) and same intercept (scalar
invariance). If it does, a given Φ_coord predicts the same expected ACS level at W1, W2, and W3.

## Setup

Φ_coord is the exact IIT-4.0 max Φ_MIP over a worker's W-S-C Boolean coordination form. The system node S
commits the joint determination AND(W, C) when the worker reports a binding, interdependent,
non-substitutable coordination, giving the faithful mediated triad with Φ_coord = 2.0; otherwise S
conveys a single party and the form factors to Φ_coord = 0.0. The study-1 bridge module computes this.
Here the form is rebuilt at each wave from that wave's task interdependence, system-authority commit, and
substitutability reports, so Φ_coord can move across waves as a worker's reports move.

The panel of 240 workers per wave carries a stable per-worker latent coordination capability. At each
wave the reports and a standardized ACS factor score load on that stable latent plus wave noise. The
shared stable latent makes the bridge hold across waves by construction; the test checks whether the
multigroup machinery recovers that invariance and whether a permuted-label control behaves trivially.

## Test

The bridge is fit as a single-predictor regression ACS = a_g + b_g * Φ per wave. Three nested models —
configural (free slope and intercept per wave), metric (common slope), scalar (common slope and
intercept) — are fit by maximum likelihood on the per-wave means, variances, and covariance of
(Φ_coord, ACS). CFI comes from each model's chi-square against the covariance-suppressed independence
baseline. ΔCFI(configural -> metric) tests the slope; ΔCFI(metric -> scalar) tests the intercept; the
cutoff is .01.

## Result

Both steps stay within the cutoff. Freeing the slope gains ΔCFI = +0.0063, so the slope is equal across
waves (metric invariance, H1 supported). Adding the common-intercept constraint does not worsen fit,
ΔCFI = -0.0063, so the intercept is equal across waves (scalar invariance, H2 supported). The per-wave
slopes (0.59, 0.47, 0.66) and intercepts (-0.22, -0.18, -0.19) sit close together. The permuted-wave-label
control, averaged over 200 seeded splits, holds invariance trivially (mean ΔCFI +0.0036 metric,
-0.0026 scalar), which shows the test is not declaring invariance by fiat.

## Scope

The cohort is simulated. No worker is measured. Φ_coord is a structural property of the Boolean form a
worker's reported conditions map to, read by the exact-Φ instrument, and the Φ-ACS association is built
into the synthetic panel through a shared latent. The invariance verdicts describe the bridge instrument
on synthetic data. Running the same configural-metric-scalar pipeline on real wave files is the
validation step this arm has not yet taken.

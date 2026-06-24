# q184 — findings

The driver and the platform give two accounts of one dispatch. The driver's suggestion account
reads dyadic; the platform's commit account reads triadic. The q183 bridge scores the spread
between them on synthetic rule sets.

## Instrument control

The faithful triad `[x1, x0&x2, x1]` reads `triadic` with max Φ_MIP = 2.000000. PASS. The
consensus control, where both parties narrate the same commit account, gives zero spread
(verdict_agreement = 1, phi_gap = 0.000000, core_jaccard = 1.000000).

## The two accounts

| account                | structure | max Φ_MIP | core      |
|------------------------|-----------|-----------|-----------|
| A = driver suggestion  | dyadic    | 0.000000  | {D, P}    |
| B = platform commit    | triadic   | 2.000000  | {D, P, R} |

## Spread

| component         | value             |
|-------------------|-------------------|
| verdict_agreement | 0                 |
| phi_gap           | 2.000000          |
| core_jaccard      | 0.666667          |
| both_verdicts     | (dyadic, triadic) |

The phi_gap of 2.0 equals the platform account's whole-system max Φ_MIP, because the driver
account carries Φ_MIP = 0. The core_jaccard of 0.666667 reflects the rider: the platform core is
{D, P, R} and the driver core is {D, P}, a two-of-three overlap.

## Verdicts

- **H1 (verdict split, gap = platform Φ): SUPPORTED.** The driver account is dyadic with
  Φ_MIP = 0, the platform account triadic with Φ_MIP = 2.0, verdict_agreement = 0, and the
  phi_gap equals the platform account's Φ.
- **H2 (rider bound only under the platform account): SUPPORTED.** The rider R is in the platform
  core and absent from the driver core, giving core_jaccard = 0.666667 < 1.

## Scope

The accounts are synthetic rule sets. The empirical arms are on synthetic data. The construct is
divergence between two stated accounts of one dispatch; no real dispatch is measured.

# q178 — findings

Collapsing a graded coded action to one bit at different cut points changes the structural Φ
verdict, and a coder panel split across the cut carries a far wider Φ confidence interval than a
panel that uses a single cut. Both results are on synthetic coded accounts.

## Instrument control

The faithful triad `[x1, x0 & x2, x1]` reads `triadic` with max Φ_MIP = 2.000000. PASS. Monotone
accounts (`g` in `{0, 2}`) read the same verdict at both thresholds. PASS.

## Grade by threshold

| grade | t=1 verdict | t=1 Φ | t=2 verdict | t=2 Φ | flips |
|-------|-------------|-------|-------------|-------|-------|
| 0     | dyadic      | 0.000 | dyadic      | 0.000 | False |
| 1     | triadic     | 2.000 | dyadic      | 0.000 | True  |
| 2     | triadic     | 2.000 | triadic     | 2.000 | False |

Grade 1 is the boundary case: it reads triadic when the cut is low and dyadic when the cut is high.
Grades 0 and 2 are threshold-invariant.

## H1: verdict-flip rate (200-account panel)

| quantity              | value  |
|-----------------------|--------|
| accounts              | 200    |
| accounts that flip    | 66     |
| flip rate             | 0.3300 |

## H2: CI width, split-threshold vs same-threshold (g=1, 8 coders)

| panel             | point Φ | alpha  | CI                | width  |
|-------------------|---------|--------|-------------------|--------|
| split (t=1 / t=2) | 0.9928  | -0.143 | [-0.1405, 2.1064] | 2.2469 |
| same (all t=1)    | 1.9942  | 1.000  | [1.9576, 2.0048]  | 0.0472 |

Width ratio (split / same) = 47.6080.

## Verdicts

- **H1 (bit cut moves the verdict): SUPPORTED.** The threshold flips the verdict for 33% of panel
  accounts, above the 20% bar and far above the 5% null.
- **H2 (threshold disagreement widens the CI): SUPPORTED.** The split-panel CI width (2.2469)
  exceeds the single-cut width (0.0472) by a factor of 47.6, above the 2x bar and far above the
  1.2 null.

## Reading

For a 3-valued action the bit cut is verdict-bearing. A boundary-grade action reads as a triad
under a low cut and a dyad under a high cut. When two coders place the cut differently on such an
account, the disagreement propagates into a Φ interval that spans the whole dyadic-to-triadic
range, while same-cut coders keep a tight interval. The negative Krippendorff alpha on the split
panel marks the cut decision as the source of the spread.

## Scope

Accounts are synthetic coded grades and rule sets, not measured worker states. The empirical arms
are on synthetic data. The mapping from a coded grade to an observed action is not validated here.

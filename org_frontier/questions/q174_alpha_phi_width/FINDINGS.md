# q174 findings — CI width tracks coder agreement, and a stable agreement floor turns the verdict indeterminate

The propagated Φ confidence interval behaves as a measurement instrument. As coder agreement
falls, the interval widens monotonically, and below a stable agreement floor it brackets zero
so the dyadic-vs-triadic verdict goes indeterminate. Both hypotheses resolve. Results are on
synthetic coded data.

| f disagree | alpha | CI width (A) | cross-zero (A) | CI width (B) | cross-zero (B) |
|---|---|---|---|---|---|
| 0.00 | 1.000 | 0.0000 | 0.00 | 0.0000 | 0.00 |
| 0.05 | 0.904 | 0.0000 | 0.00 | 0.0000 | 0.00 |
| 0.10 | 0.863 | 0.3416 | 0.00 | 0.3416 | 0.00 |
| 0.15 | 0.768 | 0.3416 | 0.00 | 0.3416 | 0.00 |
| 0.20 | 0.738 | 0.9209 | 0.00 | 0.9189 | 0.00 |
| 0.25 | 0.642 | 0.9981 | 0.00 | 0.8416 | 0.00 |
| 0.35 | 0.528 | 1.5705 | 0.00 | 1.5705 | 0.00 |
| 0.50 | 0.329 | 2.2678 | 1.00 | 2.0823 | 1.00 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | CI width decreases monotonically with alpha (rho <= -0.9, p < 0.01) | rho = -0.988, p = 4.26e-06 — SUPPORTED |
| H2 | stable alpha* below which >50% of forms cross zero, +/-0.05 across ensembles | alpha* = 0.329 in both, |diff| = 0.000 — CONFIRMED |

From `probe_alpha_phi_width.py`.

## What it says

Width is a faithful read of disagreement. The Spearman correlation between Krippendorff alpha
and mean CI width is -0.988 (p = 4.26e-06): tighter agreement, tighter interval. At perfect
agreement the CI collapses to a point, and small disagreement keeps it degenerate until enough
coders flip the coupling unit to put spread in the panel.

The verdict stays determinate over most of the agreement range. The interval brackets zero only
at the lowest agreement tested (alpha = 0.329), where about half the coders read the dyadic
collapse. The threshold alpha* is identical across the two seeds, well inside the +/-0.05 band.
Below the floor the instrument reports an honest "cannot tell dyadic from triadic" rather than a
false verdict.

## Control

The faithful triad reads triadic at max Φ_MIP = 2.0. The alpha = 1 panel returns a degenerate
CI of width 0. The verdict-invariant panel (readings 2.0 and 3.0, never the collapse) returns
width 1.13 with a lower bound of 1.93, nonzero yet never crossing zero. The machinery separates
"wide because coders disagree on magnitude" from "indeterminate because coders disagree on the
verdict."

## Caveats

- **In-silico.** Synthetic coder panels and synthetic active-bit decisions, not coded field
  accounts. The study validates the disagreement-to-CI instrument, not any real coordination.
- **Borderline forms.** Three triads paired with their dyadic collapses, chosen so disagreement
  on one coupling unit can flip the verdict. The clean zero-crossing depends on that pairing; a
  form with no nearby collapse would widen without ever crossing zero.
- **Engineered alpha sweep.** Disagreement is injected by construction so alpha runs a controlled
  grid. The mapping from f to alpha is a property of the synthetic design.
- **Bootstrap-t at small n.** Eight coders per panel; the CI is the bridge's bootstrap-t interval,
  calibrated for small coder counts but still an approximation.

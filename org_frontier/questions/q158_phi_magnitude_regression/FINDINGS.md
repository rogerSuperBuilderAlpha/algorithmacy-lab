# q158 — findings

Whole-system CRQA measures do not predict the magnitude of exact major-complex Φ across the
corpus. The relationship runs the wrong way: forms that revisit global states more (higher RR) and
sustain that revisiting on deterministic lines more (higher DET) tend to have lower Φ, not higher.

| measure | Spearman rho vs Φ | p-value |
|---|---|---|
| md_recurrence DET | -0.1878 | 9.87e-03 |
| whole-system RR | -0.4011 | 1.17e-08 |

| linear fit Φ ~ DET | value |
|---|---|
| slope | -2.1036 |
| high-Φ residual mean (top quartile) | +0.5280 |
| rest residual mean | -0.4747 |
| linear RMSE | 0.5263 |
| isotonic (increasing) RMSE | 0.5360 |

Pool: n=188 forms with major-complex Φ > 0 (Φ range 0.277–2.000, median 1.000).

## Verdicts

- H1 DET correlates positively with major-complex Φ (rho>0.4): **REFUTED**. The correlation is
  negative and weak, rho = -0.19.
- H2 the DET-Φ relation saturates (high-Φ underprediction): **REFUTED**. The high-Φ residual is
  positive, but the monotone increasing fit does not beat the line, so the pattern is the negative
  trend, not a saturating rise.

## Reading

A high whole-system DET marks a form that locks into a few recurring global states. That kind of
form is often a low-Φ form: a tight limit cycle is highly recurrent and weakly integrated. The
forms with the largest Φ sit at lower DET, where the run keeps moving through new global states.
The behavioral magnitude CRQA reads and the structural magnitude Φ reads are not the same quantity
on this corpus, and the binary-verdict success of earlier studies does not carry to the continuous
scale.

Scope: synthetic Boolean forms, exact IIT-4.0 Φ, in-silico. No field coordination is measured.

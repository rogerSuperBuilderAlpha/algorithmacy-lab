# Q71 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on the noise robustness of the outreach verdict. The read-recipient triad and the
broadcast are perturbed with per-node flip probability epsilon in {0, 0.05, 0.1, 0.2, 0.3, 0.5}. Written
and committed before any test runs.

## H1 — The triad survives small noise

- **Claim:** The read-recipient triad keeps Φ > 0 at epsilon = 0.05 and 0.1.
- **H0:** The triad's Φ drops to 0 at epsilon <= 0.1.
- **Predicted outcome:** Φ > 0 at both small noise levels. H0 refuted.

## H2 — Φ degrades monotonically with noise

- **Claim:** The triad's Φ is non-increasing as epsilon rises from 0 to 0.5.
- **H0:** Φ is non-monotone in epsilon.
- **Predicted outcome:** Φ decreases monotonically. H0 refuted.

## H3 — Maximal noise collapses the triad

- **Claim:** At epsilon = 0.5 (every update a coin flip) the triad's Φ is ~0.
- **H0:** Φ stays above 0.1 at epsilon = 0.5.
- **Predicted outcome:** Φ ~ 0 at maximal noise. H0 refuted.

## H4 — Noise never manufactures a spurious triad

- **Claim:** The broadcast stays Φ ~ 0 at every noise level; noise does not turn a dyadic form triadic.
- **H0:** The broadcast's Φ rises above 0.1 at some noise level.
- **Predicted outcome:** broadcast Φ ~ 0 throughout. H0 refuted.

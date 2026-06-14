# Q91 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on a lossy channel between the recipient and the mediator. Every read in the corpus is
exact, and Q79 made the mediator's commit stochastic; Q91 degrades the input instead. The mediator reads
the recipient through a binary symmetric channel of error e, so R reaches M flipped with probability e.
Written and committed before the sweep is read. The perfect channel (e = 0, triadic Φ = 2) and the
zero-capacity channel (e = 0.5, dyadic) are the instrument control.

## H1 — A perfect channel is triadic

- **Claim:** At e = 0 the form is triadic (Φ > 0).
- **H0:** It is dyadic at e = 0.
- **Predicted outcome:** triadic. H0 refuted.

## H2 — A zero-capacity channel is dyadic

- **Claim:** At e = 0.5, where the channel carries no information about R, the form is dyadic (Φ = 0).
- **H0:** It is triadic at e = 0.5.
- **Predicted outcome:** dyadic. H0 refuted.

## H3 — Φ decays monotonically with channel error

- **Claim:** Φ is non-increasing as e rises from 0 to 0.5, and strictly lower at e = 0.5 than at e = 0.
- **H0:** Φ rises somewhere, or is flat across the sweep.
- **Predicted outcome:** monotone decay. H0 refuted.

## H4 — The triad survives substantial loss

- **Claim:** At e = 0.4, a heavily degraded channel, the form is still triadic (Φ > 0); only the
  zero-capacity limit collapses it.
- **H0:** The triad collapses before e = 0.4 (Φ = 0 at e = 0.4).
- **Predicted outcome:** still triadic at e = 0.4 — a gradual decay, not a cliff at the first loss. This is
  the study's genuinely uncertain claim.

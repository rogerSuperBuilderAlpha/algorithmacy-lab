# q190 hypotheses

Both hypotheses were fixed before the probe was run.

## H1 — flips track the boundary, not elicitation precision

Adding bounded Bernoulli noise to either account's elicited rule table leaves verdict_agreement
and the sign of the signed phi_gap unchanged, except for account pairs whose noiseless Φ sits
within epsilon of the dyad/triad boundary. A clean dyad has Φ near zero and sits at that
boundary, so jitter can lift it across; a triad with Φ well above zero stays triadic under the
same jitter.

H1-null: noise flips verdict_agreement for pairs far from the boundary, where both accounts are
triadic with Φ well above zero. If that happened, the measured spread would be an artifact of
elicitation precision.

## H2 — the gap magnitude is measurable for disagreeing pairs

For pairs that genuinely disagree at noise zero (verdict_agreement = 0), the standard deviation of
phi_gap under elicitation noise is smaller than its mean. Signal-to-noise exceeds one, so the gap
magnitude is a measurable quantity rather than elicitation jitter.

H2-null: phi_gap noise swamps the mean (signal-to-noise at or below one), so the gap magnitude
carries no measurable signal.

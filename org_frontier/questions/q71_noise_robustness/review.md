# Q71 — Stage 1 review: noise robustness of the verdict

## The question

Every outreach verdict so far is computed on a deterministic Boolean model. Real coordination is noisy.
This study asks whether the triadic verdict is robust to stochastic update: does it survive small noise,
degrade gracefully, and avoid turning a dyadic form spuriously triadic? Parties: worker E, agent M,
counterpart R, with each node's update flipped with probability epsilon.

## What the lab already knows that bears on this

- **The read-recipient triad is triadic at Φ=2.0 (Q63, probe 215).** The broadcast is dyadic at Φ=0.
  These are the deterministic baselines whose robustness this study tests.
- **The program checks noise robustness elsewhere (Finding 6, multiparty scaling).** The random
  triadic-rate dilution result was confirmed genuine by noise-robustness checks, so the machinery for
  stochastic Φ is established (`max_phi_float` on a state-by-node stochastic TPM).
- **Φ magnitude is read ordinally (withdrawn graded claim).** The interest is whether the verdict (Φ>0)
  holds under noise, and whether Φ degrades smoothly, not the exact magnitude.

## The gap

The lab computes verdicts deterministically and has not characterized how the outreach verdict behaves as
stochastic noise is added to the update. Whether the triad survives small noise and whether noise ever
manufactures a spurious triad are uncomputed. No prior probe answers this for the outreach forms, so it is
open.

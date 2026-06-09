# Q80 — Stage 1 review: asynchronous update

## The question

The program updates every element synchronously. Real coordination is asynchronous: parties act at
different times. This study recomputes the keystone outreach forms under asynchronous update, where one
element acts each step while the others hold, and asks whether the dyadic/triadic verdict survives.

## What the lab already knows that bears on this

- **The synchronous verdicts (Q63, Q64).** read_recipient is triadic at Φ=2.0, broadcast dyadic at Φ=0,
  the all-required campaign triadic at Φ=3.0. These are the synchronous baselines.
- **Φ is computed from a transition matrix (Q71, Q79).** Asynchronous update is a different transition
  matrix on the same elements, computable with `probes.lib.max_phi_float`.
- **The verdict has been robust to noise (Q71).** Whether it is also robust to the update scheme is the
  question here.

## The gap

Every prior verdict assumes synchronous update; whether synchronicity is load-bearing for the verdict is
uncomputed. No prior probe recomputes the keystones asynchronously, so the question is open.

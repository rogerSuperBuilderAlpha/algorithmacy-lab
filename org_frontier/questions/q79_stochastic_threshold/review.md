# Q79 — Stage 1 review: stochastic emergence of the triad

## The question

Every outreach verdict is computed on a deterministic commit: the agent either reads the recipient or does
not. Real agents are probabilistic. This study makes the agent's commit stochastic — it reads the
recipient with probability p and ignores it with 1−p — and asks how the verdict emerges as p rises. Does
the triad appear only at p=1, at a threshold, or gradually from the first probability of reading?

## What the lab already knows that bears on this

- **The deterministic endpoints (Q63).** read_recipient (M'=E∧R) is triadic at Φ=2.0; broadcast (M'=E) is
  dyadic at Φ=0. The stochastic agent interpolates between them.
- **Φ is computed for stochastic systems (Q71).** `max_phi_float` takes a state-by-node stochastic TPM, as
  used for the noise study. The same machinery handles a probabilistic commit.
- **Liveness and joint determination are the triadic conditions (Q63, Q67).** A probabilistic reader
  jointly determines from the recipient only some of the time, so the question is whether partial joint
  determination yields partial irreducibility.

## The gap

The program's verdicts are deterministic; how the triad emerges under a probabilistic commit is uncomputed.
Whether the emergence is graded or threshold is open. No prior probe sweeps the reading probability, so the
question is open.

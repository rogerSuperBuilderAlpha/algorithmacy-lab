# Q91 literature — degrading the input rather than the commit

## Where the noise enters

Q71 added output noise to the deterministic TPM and found the verdict degrades gracefully. Q79 made the
mediator's commit stochastic — it reads the recipient with probability p and ignores it otherwise — and
found a graded emergence of Φ with p. Both put the stochasticity on the mediator's action. Q91 puts it on
the mediator's perception: the recipient is read through a binary symmetric channel of error e, the
standard model of a noisy communication link (Shannon). The mediator always uses the recipient; what it
receives is corrupted.

## The question

A coordination that depends on a degraded read of a party is the realistic case: a worker's state reaches
a platform through lossy logs, a counterpart's position through a noisy signal. Whether the triad collapses
at the first loss, survives until the channel carries no information, or decays smoothly in between, decides
how much fidelity coordination needs. The expected shape, by analogy with Q79, is a gradual decline with a
collapse only at the zero-capacity limit (e = 0.5), but input-side and commit-side noise need not behave
the same way, and the threshold is uncomputed.

## Method context

The construction reuses Q79's stochastic-TPM pattern with the channel on the input rather than the commit,
and reads exact Φ with `max_phi_float`, as in Q71 and Q79.

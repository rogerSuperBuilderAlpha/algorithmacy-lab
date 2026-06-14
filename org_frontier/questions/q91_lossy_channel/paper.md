# Q91 — A lossy read degrades the triad gracefully

## Question

Every read in the corpus is exact, and Q79 made the mediator's commit stochastic. Q91 degrades the input:
the mediator reads the recipient through a binary symmetric channel of error e, the standard model of a
noisy link. A coordination that depends on a degraded read of a party is the realistic case — a worker's
state reaching a platform through lossy logs, a counterpart's position through a noisy signal. Whether the
triad collapses at the first loss, survives to the zero-capacity limit, or decays in between is the
question.

## Method

The read-recipient triad with a channel on the mediator's read of the recipient: P(M'=1 | E, R) =
E · [(1-e)·R + e·(1-R)], with E' = M and R' = M deterministic. The result is a stochastic state-by-node
TPM whose exact Φ is read by `max_phi_float`. The channel error is swept over 0, 0.1, 0.2, 0.25, 0.3, 0.4,
0.5.

## Results

The triad survives every error level below the zero-capacity limit. Φ is 2.0 at a perfect channel and falls
monotonically (0.76, 0.54, 0.44, 0.34, 0.16), staying positive through e = 0.4, and reaches zero only at
e = 0.5, where the channel is independent of the recipient.

| channel error e | Φ | verdict |
|---|---|---|
| 0.0 | 2.000 | triadic |
| 0.1 | 0.763 | triadic |
| 0.2 | 0.543 | triadic |
| 0.3 | 0.340 | triadic |
| 0.4 | 0.158 | triadic |
| 0.5 | 0.000 | dyadic |

| | result |
|---|---|
| H1 perfect channel triadic | confirmed |
| H2 zero-capacity channel dyadic | confirmed |
| H3 Φ decays monotonically | confirmed |
| H4 triad survives substantial loss (e=0.4) | confirmed |

## Interpretation

Coordination demands an informative read, not a perfect one. The triad holds as long as the mediator's
view of the recipient carries some information, and collapses only when the channel is useless. A platform
that sees a worker through lossy logs still coordinates a genuine triad, weaker in Φ but triadic in
verdict, until the logs are pure noise. The fidelity the coordination needs is any fidelity above zero.

The decay is smooth, with a sensitive magnitude and a robust verdict. Φ drops sharply at the first loss of
fidelity and then tails off gently, so the strength of integration is most sensitive near a perfect
channel, while the existence of integration persists across the whole range. The program reads Φ ordinally,
and on that reading the triad is present everywhere below the zero-capacity limit.

The result completes a symmetry with Q79. Stochasticity on the mediator's commit gave a graded emergence of
Φ with the read probability; stochasticity on the mediator's perception gives a graded decay with channel
error. Input-side and commit-side noise produce the same shape — a continuous dependence of Φ on fidelity
with the binary verdict as the limit — so the triad's robustness to noise does not depend on where the
noise enters.

## Limitations

In-silico; a Boolean triad with a stochastic read, exact Φ. The channel is binary symmetric on the single
read of the recipient; asymmetric channels, channels on both reads, and correlated noise are untested. Φ
magnitude depends on the encoding and is read ordinally, so the steep first drop is a property of the
magnitude rather than the verdict.

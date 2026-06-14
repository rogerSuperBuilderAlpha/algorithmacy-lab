# Q79 findings — stochastic emergence of the triad

All four hypotheses confirmed. The triad emerges gradually with the agent's probability of reading the
recipient.

| p (reads recipient) | max-Φ |
|---|---|
| 0.00 | 0.0000 |
| 0.25 | 0.1101 |
| 0.50 | 0.2767 |
| 0.75 | 0.5425 |
| 1.00 | 2.0000 |

From `probe_stochastic_threshold.py`.

## What it says

Irreducibility accumulates with the probability that the agent reads the recipient. A broadcast that never
reads is dyadic; an agent that reads only a quarter of the time already has positive Φ, and Φ rises
monotonically as the reading probability grows, with no flat-zero region and no threshold to cross. The
triadic verdict is the deterministic limit of a graded quantity: partial joint determination yields partial
irreducibility. The steep final step to Φ=2.0 at p=1 reflects that the deterministic conjunction is a
special, maximally-integrated point; for every interior probability the form is irreducible to a degree set
by how often the agent tailors.

## Caveats

- **Confirmatory.** The graded-emergence predictions held.
- **In-silico.** Boolean models with a probabilistic commit; Φ read ordinally. The five-point grid does
  not exclude fine non-monotonicity between points.
- **One mixture.** The mixture is between read-recipient and broadcast; other probabilistic commits are
  untested.

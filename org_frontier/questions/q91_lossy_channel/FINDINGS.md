# Q91 findings — the triad degrades gracefully under a lossy read

All four hypotheses confirmed. The mediator reading the recipient through a noisy channel keeps the triad
intact across heavy loss, with Φ falling smoothly and the verdict collapsing only when the channel carries
no information at all.

| channel error e | Φ | verdict |
|---|---|---|
| 0.0 | 2.000 | triadic |
| 0.1 | 0.763 | triadic |
| 0.2 | 0.543 | triadic |
| 0.25 | 0.439 | triadic |
| 0.3 | 0.340 | triadic |
| 0.4 | 0.158 | triadic |
| 0.5 | 0.000 | dyadic |

| H | Result | Verdict |
|---|--------|---------|
| H1 | perfect channel (e=0) is triadic | confirmed |
| H2 | zero-capacity channel (e=0.5) is dyadic | confirmed |
| H3 | Φ decays monotonically with channel error | confirmed |
| H4 | the triad survives substantial loss (e=0.4) | confirmed |

From `probe_lossy_channel.py`.

## What it says

A degraded read does not break the triad until the read carries nothing. The mediator reading the
recipient through a binary symmetric channel keeps the form triadic at every error level up to the
zero-capacity limit, and Φ falls monotonically as the channel worsens. At 40% bit-flips the form is still
triadic, at Φ = 0.158; only at e = 0.5, where the channel is independent of the recipient, does the triad
collapse. Coordination tolerates a noisy view of a party and demands only that the view carry some
information about it.

The decay has a steep first step and a long tail. Φ drops from 2.0 to 0.76 between a perfect channel and
10% error, then falls gently through the rest of the range. The magnitude of Φ is sensitive to the first
loss of fidelity, while the verdict, whether the form integrates at all, is robust, holding until the
channel is useless. Read ordinally, as the program reads Φ throughout, the triad is present across the
whole sub-zero-capacity range and absent only at the limit.

The result matches Q79 on the input side. Q79 made the mediator's commit stochastic and found a graded
emergence of Φ with the read probability; Q91 makes the mediator's perception stochastic and finds the
mirror image, a graded decay with channel error. Input-side and commit-side noise behave the same way: a
smooth dependence of Φ on fidelity, with the binary verdict as the limit. The coordination is not brittle
to a lossy read; it is brittle only to a read that carries no information.

## Caveats

- **Confirmatory.** All four predictions held; the result is a clean graceful-degradation curve.
- **In-silico.** A Boolean triad with a stochastic read, exact Φ. The channel is binary symmetric on a
  single read (the mediator's read of the recipient); other channel models and degrading both reads are
  untested.
- **Magnitude vs verdict.** Φ magnitude depends on the encoding and is read ordinally; the steep first drop
  is a feature of the magnitude, not of the verdict, which is robust across the range.

# Q209 — Is rate-1 the unique binding cadence: does a triad factor at every commit period p≥2, and how does the surviving clock scale? · Stage 1 review

**Question.** q207 showed a mediator that recomputes every second step factors the triad. Does the triad
factor at *every* commit period p ≥ 2, so that synchronous (p=1) commitment is the unique binding cadence,
and how does the surviving counter's integration scale with the period?

**Agenda id.** Direct follow-up to q207 (slow mediator), the period-sweep analog of q208's depth-sweep.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #361 (q207) | A half-rate (period-2) mediator factors the triad (dyadic, Φ=0); only the clock's 2-cycle survives at Φ=1.0 | The single point this sweeps over period |
| #362 (q208) | Represented latency depth never factors the triad (Φ recovers to 2.0) | The companion sweep: depth is benign, this asks whether period is uniformly fatal |
| synthesis | The conjunctive triad is triadic, Φ_MIP=2.0 | The p=1 reference |

## The gap

q207 established a single point: at commit period two the triad dissolves entirely. It did not say whether
that is the start of a trend or a threshold. Two questions are open. First, is synchronous commitment the
unique binding cadence — does the triad factor at every period p ≥ 2 (p = 3, 4 as well as 2), or does some
longer period partially restore it the way deeper latency did in q208? Second, q207 left the surviving
structure as the clock's two-cycle at Φ = 1.0; how does that residual scale when the gating clock is a
longer mod-p counter? This sweeps the commit period p = 1, 2, 3, 4, with the mediator gated by a mod-p
counter, and reads at each period the verdict, the major complex, and the counter's residual Φ — turning
q207's point into a curve and pairing it with q208's depth curve to complete the picture of which mediator
slowings break binding.

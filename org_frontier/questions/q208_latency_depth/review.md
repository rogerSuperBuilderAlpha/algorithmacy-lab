# Q208 — How many steps of represented latency can a triad absorb before it factors, and what is the decay law? · Stage 1 review

**Question.** As the mediator's feedback to the parties is delayed by k explicit buffer nodes, does the
triad stay irreducible at every depth, and how does its integration scale with k?

**Agenda id.** Direct follow-up to q205 (latency feedback), not a numbered agenda item.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #359 (q205) | One represented buffer keeps the triad triadic (whole-system Φ_MIP 2.0→1.0); the buffer joins the core {S,C,B}, the worker drops out | The k=1 point this sweeps over depth |
| #361 (q207) | A half-rate mediator factors the triad entirely (dyadic, Φ=0) | The companion deformation: rate breaks binding; this asks whether depth does |
| synthesis | The conjunctive triad is triadic, Φ_MIP=2.0 | The k=0 reference |

## The gap

q205 established that one step of represented latency leaves the triad triadic and halves its whole-system
Φ_MIP, with the delay node joining the irreducible core. It tested a single depth. Whether the triad
survives deeper latency — two, three steps — and whether Φ follows a regular decay law is unknown. q207
showed the companion deformation, commit rate, breaks the triad outright at rate two. The open question is
whether depth behaves the same way (a threshold past which the triad factors) or differently (the triad
absorbs arbitrary represented delay while its integration decays smoothly). This sweeps the buffer count
k = 0, 1, 2, 3 and reads, at each depth, the verdict, the whole-system Φ_MIP, the major complex, and
whether the worker stays excluded — turning q205's single point into a decay curve and locating any
breaking point.

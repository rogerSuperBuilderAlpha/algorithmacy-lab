# Q91 — Stage 1 review: a lossy read

## The question

Every read in the corpus is exact. Real mediators read parties through imperfect channels. Whether a triad
survives a lossy read of a party, and at what fidelity it collapses, is unasked.

## What the lab already knows that bears on this

- **The verdict degrades gracefully under output noise (Q71).** Φ falls smoothly rather than snapping to
  zero. Q91 puts the noise on the input read instead.
- **A stochastic commit gives a graded emergence of Φ (Q79).** The mediator reading the recipient with
  probability p produces a continuous Φ(p). Q91 is the input-side mirror.
- **Liveness is necessary for the triad (Finding 3).** The mediator must read the parties as they are; a
  lossy read tests how much of that read the triad needs.

## The gap

No study degrades the mediator's read of a party through a channel. Whether the triad collapses at the
first loss or survives to the zero-capacity limit, and whether input-side noise behaves like Q79's
commit-side noise, is uncomputed.

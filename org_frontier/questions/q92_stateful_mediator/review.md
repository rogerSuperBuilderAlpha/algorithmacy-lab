# Q92 — Stage 1 review: a mediator with memory

## The question

Every determination in the corpus is memoryless. Finding 3 made liveness necessary for the triad. Real
mediators have memory. Whether a remembered value of a party substitutes for a live read, or whether the
delay breaks the triad, is unasked.

## What the lab already knows that bears on this

- **Liveness is necessary (Finding 3).** The mediator must read the parties as they are; a form whose reads
  break liveness factors. This study asks what liveness means when a memory is in the path.
- **A relay gap breaks the chain (Q65).** An agent that delays or gates without carrying the parties'
  current values breaks the triad. Whether a tracking memory behaves like a relay gap or preserves the
  binding is the open question.
- **Delegation reorganizes the core (Q68).** Adding a stateful element can change which parties are bound.
  A memory may do the same.

## The gap

No form in the corpus has memory. Whether a tracking memory substitutes for a live read, whether a frozen
memory or self-reference fails to bind the recipient, and whether memory reorganizes the core, is
uncomputed.

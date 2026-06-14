# Q108 — Stage 1 review: controllability

## The question

Q106 named the design levers; Q107 showed repair is lever-specific. If a designer can set only one party's
reads, from which party can the verdict be steered, and how robustly? A control node is a party from which
both verdicts are reachable.

## What the lab already knows that bears on this

- **The design levers are three (Q106).** Binding, liveness, requirement. Control asks which party's reads
  turn which lever and how many settings hold the triad.
- **Building is located at the parties; the parties are load-bearing (Q105, Q104).** Control should find
  the parties a soft surface and the mediator a hard one.
- **Liveness is one condition met by the live read (Finding 3).** A party should hold the triad on a single
  read, the knife-edge.

## The gap

No study reads the verdict as a function of one party's reads. Which parties are control nodes, and whether
the mediator and the outer parties differ in how robustly they hold the triad, is uncomputed.

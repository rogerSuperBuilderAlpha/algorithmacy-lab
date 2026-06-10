# Q97 — Stage 1 review: the coordinated adversary

## The question

Q84 showed a single agent outside the core cannot flip the verdict; influence requires membership. Security
rarely faces one adversary. Whether a coalition of agents, each individually unable to enter the core, can
coordinate to gain influence the members lack alone is unasked.

## What the lab already knows that bears on this

- **Influence requires membership (Q84).** A read-only or emit-only agent cannot flip the verdict; only a
  bidirectional, pivotal agent does, by joining the core. Q97 tests whether a coalition routes around this.
- **The membership gate is hard at the corners (Q98).** Zero reading or zero influence excludes a party.
  A coalition might supply the missing side collectively.
- **Spectators do not destroy the core (Q75).** Idle and observing parties leave the triad intact. Q97
  scales this to two observers and asks whether coordination among them changes the answer.

## The gap

No study tests a coalition of external agents. Whether two agents that each fail to enter the core can,
by coordinating, destroy the triad, manufacture one, or gain influence without membership is uncomputed.

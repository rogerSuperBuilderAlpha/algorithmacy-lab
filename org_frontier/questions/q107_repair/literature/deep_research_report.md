# Q107 literature — repair and routing around damage

## The repair question

Q106 cataloged the design operations as three levers, each with a build and a break. Q105 found triads are
usually built at a party's read, restoring liveness. Repair sharpens this: when a specific lever is broken,
must the repair restore that lever, or can a different edit route around the damage and restore the triad
another way? The first would mean coordination has no repair redundancy — the broken condition is the one
that must be fixed; the second would mean the triad can be restored by a substitute condition.

## The expected answer

The law makes each condition necessary: a party is bound only if the mediator reads it and it stays live.
If a condition is necessary, breaking it cannot be compensated by strengthening another, so repair should
be lever-specific — binding damage repaired at the mediator, liveness damage at the party's read. This is
the repair form of Q104's no-redundancy result: as every edge is load-bearing, every condition is, so the
broken one must be the restored one.

## Method context

Repair distance reuses Q105's Hamming construction distance over the 8-bit encoding, with the damaged forms
constructed by breaking one lever of the read-recipient triad.

# Thread — a second hub beats the size limit one mediator hits

A prior for the catalog, and the opening of the scale-and-hierarchy line. The scale thread found a single hub
cannot bind five parties: its commitment rate falls to zero. This thread gives the resolution. Add a second
hub — a second mediator, a management layer — and the five-party coordination commits readily, in two of five
forms, more often than a single hub binds even three parties. A coordination too large for one mediator is
bound by two. Reproduce with `python org_frontier/threads/two_hubs/two_hubs.py` (seed 11).

## Setup

Five parties: three workers and one or two hubs. In the one-hub form the three workers read a single hub and
the hub reads all three, with the second hub left inert. In the two-hub form the three workers read both hubs
and both hubs read all three workers. Rules are random. The measure is the rate of commitment.

## The arc

**One hub cannot bind five parties.** With a single hub the five-party coordination commits in none of the
300 forms, the scale thread's result. One mediator reading three workers, with the workers reading it back,
does not produce an irreducible whole of five at the rates random rules supply.

**Two hubs bind them readily.** With a second hub added the same five parties commit in 121 of 300 forms,
40%. The management layer does more than rescue the coordination from zero: it binds five parties more often
than a single hub binds three, which the scale thread put at 10%. Two mediators between the workers carry an
irreducible structure that one could not.

## What the thread establishes

A second hub beats the size limit a single mediator hits. Five parties that one hub binds zero percent of the
time, two hubs bind 40%, above the rate a single hub binds three parties. As a prior for reading real
coordination: a group too large for one coordinator to hold together as an irreducible whole can be held by
two coordinators between it, and the appearance of a second managing layer is what one would expect where a
single one has reached its span. This opens the question the rest of the line pursues — how the credit, the
bottleneck and the structure distribute once there is more than one hub.

## Limits, honestly

The two architectures are one-hub and two-hub stars with random rules at one seed, five nodes; a different
wiring of the second hub would have its own rate. The contrast that carries the thread is the zero against
the forty percent, both robust over 300 forms. Five-node exact Φ is reached for the whole-system verdict.
Everything is in-silico, and a prior is to be tested against data.

# q144 — Mediator hierarchy: does Φ track depth like a chain or breadth like a pool?

## Question

A balanced k-ary mediator hierarchy is a tree of AND-gates feeding one apex. Two axes describe it: depth d,
the number of mediator layers between a leaf and the apex, and breadth b, the number of children each node
has. The scaling zoo gives two laws to compare against. A serial chain holds Φ constant at 2. A
fully-coupled pool grows Φ as n(n-1). The question is which law the tree follows along each axis, and
whether the two axes scale alike.

## Method

Each internal node and the apex is the AND of its b children. Every leaf reads the apex, closing the tree
into a recurrent dynamical system so the exact instrument has reachable states. The depth axis fixes one
leaf (b = 1) and runs d = 1..4, a pure serial mediator chain. The breadth axis fixes one layer (d = 1) and
runs b = 2, 3, 4. Φ is the exact IIT-4.0 major complex from `org_frontier.probes.lib.major_complex`. A
serial chain and a parity-coupled pool anchor the two zoo laws. The grid stays at n <= 5. The run is seeded
and deterministic; the instrument is validated on the faithful triad (triadic, Φ = 2.0) before any tree is
computed.

## Results

Depth holds Φ at the chain constant. Across d = 1, 2, 3, 4 the major-complex Φ is 2.000 at every depth,
matching the serial-chain baseline of 2.000 at n = 3, 4, 5. Stacking mediator layers above a single leaf
adds no integration, because each layer passes one bit and is a serial bottleneck.

Breadth raises Φ. Widening the apex over b = 2, 3, 4 leaves gives Φ = 2.0, 3.0, 4.0, one unit per added
leaf. The trend is strictly increasing, so breadth and depth are separable axes that scale differently. The
growth is linear in leaf count. It does not reach the convex n(n-1) of a pool, where every party couples to
every other; a single shared conjunctive apex caps the rate. The strong form of the breadth hypothesis,
super-linear growth toward the pool law, is refuted; the weaker separability claim holds.

The parity-coupled pool baseline was non-monotone at this size (Φ = 1.5, 4.0, 2.5 at n = 3, 4, 5) and did
not trace the n(n-1) law cleanly, so the comparison to the pool is qualitative.

## Verdicts

H1 (depth flat at chain constant): SUPPORTED. H2 (breadth super-linear toward pool): SUPPORTED in its
separability claim, refuted in its super-linear claim; the breadth trend is linear.

## What this contributes

The lab's scaling zoo had a chain law and a pool law as endpoints. This places the balanced mediator tree
between them and resolves it by axis: flat in depth, linearly growing in breadth. Φ reads depth as a serial
bottleneck and breadth as added parties bound through one apex. For the program's reading of coordination
forms, a hierarchy gains irreducibility by widening, not by deepening.

## Scope

In-silico. Boolean dynamical models and the exact major complex over n <= 5. No party is measured;
irreducibility is explored in these synthetic trees, not established for any human coordination. The
validation gap to fielded organizations stands. The breadth trend rests on three points and the pool
baseline is an imperfect stand-in for the published law.

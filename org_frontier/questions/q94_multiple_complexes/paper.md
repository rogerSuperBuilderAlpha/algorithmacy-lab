# Q94 — Multiple coexisting complexes, and why coupling does not fuse them

## Question

Every membership result in the program reads the single major complex. IIT 4.0 allows a substrate to
decompose into several complexes that do not overlap, each integrated within itself and reducible across
the cut between them. Whether a coordination form fragments this way, holding two coexisting cores, and
what coupling merges two cores into one, is unasked.

## Method

Two minimal mutual-determination units, {A,B} and {C,D}, each a two-node cycle at Φ = 2, are coupled four
ways: uncoupled, sharing an idle spectator, bridged one-way (the second reads the first), and bridged
mutually (the units read each other). PyPhi's irreducible-complex lattice is resolved at each reachable
state into disjoint maximal complexes, greedily by descending Φ, and the configuration with the most
coexisting complexes is reported.

## Results

Two uncoupled units hold two disjoint complexes, {A,B} and {C,D}, each at Φ = 2.0. A one-way bridge leaves
both intact. A mutual bridge collapses to a single complex {C,D} at Φ = 2.0, with the other unit gone. The
shared spectator, modelled with a self-loop, is its own one-node complex at Φ = 1.0, so that form holds
three complexes and the units stay separate.

| configuration | disjoint complexes |
|---|---|
| two uncoupled units | {A,B}=2.0, {C,D}=2.0 |
| shared spectator | {A,B}=2.0, {C,D}=2.0, {E}=1.0 |
| one-way bridge | {A,B}=2.0, {C,D}=2.0 |
| mutual bridge | {C,D}=2.0 |

| | result |
|---|---|
| H1 two coexisting complexes when uncoupled | confirmed |
| H2 a shared spectator does not merge them | refuted (adds a third) |
| H3 a one-way bridge does not merge them | confirmed |
| H4 a mutual bridge merges into one spanning complex | refuted (collapses to one) |

## Interpretation

Coordination is not always one core. A form can carry two irreducible coordinations at once, and the major
complex the program reads is the largest of several. The fragmentation is genuine: uncoupled and
feed-forward-linked units keep their separate cores, so a coordination built from independent or one-way
parts is several coordinations, not one.

Coupling two cores does not build a larger one. The mutual bridge, intended to fuse the two units into a
four-node complex, instead leaves a single two-node complex while the other unit dissolves. Mutual coupling
makes two cores compete: the link breaks the determination of the losing unit without enlarging the winner.
This is the sharp result. Where the chain (Q65) and breadth (Q64) scaled Φ by adding bound parties within
one determination, coupling two already-formed cores does the opposite, subtracting one instead of summing
both.

The one-way result echoes Finding 8 at the level of cores. A node enters a core only with bidirectional
coupling; two cores merge only with mutual coupling, and even then the merge can collapse one core instead of fusing
both. A feed-forward link between coordinations leaves them independent, which is the multi-complex
analogue of an emit-only party staying outside the core.

The reporting consequence is that the Q74 rule, which selects which single verdict to report, assumes one
core to report. A form with several complexes needs the tiling, not the major complex alone, and the
program's membership results should be read as describing the largest core among possibly several.

## Limitations

In-silico; Boolean models with the exact irreducible-complex lattice. The spectator's self-loop makes it
its own complex, an artifact of that modelling choice. The mutual
bridge is one construction; that it collapses shows the possibility, not that mutual
coupling always collapses. The units are minimal two-node cycles, chosen to isolate the merging condition,
so the finding is demonstrated on these forms, not swept over a population.

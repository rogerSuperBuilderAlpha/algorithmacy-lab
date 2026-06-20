# Thread — the architecture of scale: twenty questions on coordination beyond one mediator

A deep line for the catalog. The scale thread found one mediator cannot bind a large coordination, and the
two-hubs thread found a second hub beats the limit. This thread drills twenty consecutive questions into how
coordination is structured beyond a single mediator. Each is the commitment rate of an architecture — the
share of random-rule forms that read as an irreducible triadic whole — measured at four parties or fewer,
the size exact Φ runs fast, with the two five-party facts cited as anchors. Reproduce with
`python org_frontier/threads/hierarchy/hierarchy.py` (seed 11).

## The questions, in order

**Span of one hub (Q1–Q2).** One hub binds two workers in 12% of forms and three workers in 1%; the
five-party anchor from the scale thread is 0% at four workers. A single mediator's reach falls off fast with
the number it must hold.

**A second hub (Q3–Q6).** Two hubs sharing two workers commit 32%, triple the one-hub rate at the same load.
Coupling the hubs so they also read each other lifts it to 57%. Splitting the workers between the hubs, each
hub reading only its own one worker, collapses commitment to 2% — a divided coordination barely binds. A hub
that reads both workers paired with a hub that reads only one commits 14%, between the shared and split
cases. The hubs help most when they share the whole and read each other.

**What the hub must read (Q7–Q9).** A hub reading both its workers commits 12%; a hub reading only one of
them commits 0%. A mediator must take in every party it binds. And when the two workers read each other
directly as well as the hub — a back-channel — commitment jumps to 51%, the direct mutual link doing more for
integration than the mediator.

**Depth (Q10–Q11).** A three-layer chain, two workers to a middle hub to a top hub, commits 3%; a tall thin
hierarchy binds weakly. Letting the top also read the workers, a matrix instead of a chain, commits 57%.
Cross-links beat pure layers.

**Flat versus mediated (Q12–Q13).** A flat triangle, three parties all reading one another, commits 51%; the
same three parties reorganized as one hub mediating two workers commit 12%. Direct mutual coupling binds an
irreducible whole far more readily than mediation does. Mediation is the harder way to be integrated, which
is why a committing mediated triad is the interesting object the rest of the catalog studies.

**Redundant versus differentiated hubs (Q14–Q15).** Two hubs running the same gate of the workers commit 9%;
two hubs with independent gates commit 32%. Redundancy wastes the second hub; differentiation uses it.

**Resilience (Q16–Q17).** Take the committing two-hub forms and remove a node. Dropping a hub leaves the rest
triadic in only 2 of 32, and dropping a worker in 6 of 32. A two-hub coordination is fragile to losing a hub
and only a little less fragile to losing a worker; the hierarchy does not degrade gracefully.

**The hub's gate at scale (Q18–Q19).** A hub computing the AND of three workers commits 4%; a hub computing
their parity commits 10%. The gate-logic thread's result holds at four parties: a parity mediator binds more
readily than a monotone one.

**The law (Q20).** Commitment by hubs and workers: one hub binds 12%, 1%, 0% at two, three, four workers; two
hubs bind 32% at two workers and 40% at three. Adding a hub more than restores the span a worker costs.

## What the thread establishes

Coordination scales by adding hubs, not by stretching one. A single mediator's commitment collapses with the
number it holds; a second hub more than restores it, most when the hubs share the whole coordination, read
each other, and differ in what they compute. Mediation is the harder route to integration than direct mutual
coupling, tall hierarchies bind weakly while cross-linked ones bind well, and a multi-hub coordination is
fragile to the loss of a hub. As a prior for reading real coordination: a group beyond one coordinator's span
should show multiple coordinators who overlap and differ instead of dividing the group cleanly between them,
direct ties among the coordinated should make the arrangement read as more integrated than the mediators
alone would, and the structure should be expected to break, rather than bend, when a coordinator is removed.

## Limits, honestly

The commitment rates are over random rules at one seed, the architectures held to four parties for speed,
with the two five-party rates cited from the scale and two-hubs threads instead of recomputed here, since
five-party exact Φ is far slower. The rates are small for the sparse architectures, so the load-bearing
comparisons are the order-of-magnitude ones — the span collapse, the second hub tripling commitment, the
flat-versus-mediated gap, the hub-loss fragility — not the precise percentages. Everything is in-silico, and
a prior is to be tested against data.

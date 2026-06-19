# Thread — commitment scales with the mediator's information throughput

A prior for the catalog. The gate-logic thread found a parity mediator binds more readily than a monotone
one. This thread gives the variable behind it: how sensitive the mediator's gate is, how often flipping a
party changes its output. Across all sixteen two-input gates, commitment rises with sensitivity. A constant
mediator, deaf to its parties, never binds them; a half-sensitive gate binds a few percent of forms; a fully
sensitive parity gate binds a quarter. A coordination's commitment scales with how much information its
mediator carries about its parties. Reproduce with
`python org_frontier/threads/gate_sensitivity/gate_sensitivity.py` (seed 11).

## Setup

Each of the sixteen Boolean functions of two inputs is taken as the mediator's gate, with the parties reading
the mediator under random rules. Each gate's sensitivity is the fraction of single-party flips that change
its output, from 0 for the two constant gates to 1 for the two parity gates. The measure is the gate's
commitment rate against its sensitivity.

## The arc

**A deaf mediator never binds.** The two constant gates, whose output ignores both parties, have sensitivity
0 and commit in none of the forms. A mediator whose verdict does not depend on its parties cannot bind them
into anything irreducible: it reads them and answers the same regardless, so the parties are not held to its
determination.

**Sensitivity buys commitment.** The twelve gates of sensitivity 0.5 — the ANDs, ORs, projections and their
negations — commit in 8% of forms on average, and the two parity gates of sensitivity 1.0 commit in 24%. The
more a mediator's output turns on its parties' states, the more readily the coordination commits, and the
relation across the sixteen gates is strong, a correlation of 0.76 between sensitivity and commitment rate.

## What the thread establishes

A coordination's commitment scales with the mediator's information throughput. A mediator insensitive to its
parties never binds them; commitment climbs with sensitivity to a quarter of forms at the parity maximum, a
correlation of 0.76 across the gate space. This is the variable under the gate-logic thread's parity result:
parity binds more readily because it is maximally sensitive, its output turning on every flip of either
party. As a prior for reading real coordination: a mediator whose decision barely responds to its parties
should bind weakly or not at all, and one whose decision turns sharply on what each party does should bind
readily, with the responsiveness of the mediator's rule the thing that predicts it.

## Limits, honestly

Sensitivity is the count of output-changing flips, one measure of a gate's information; an entropy or
mutual-information measure would order the middle gates more finely than the single 0.5 band they fall in
here. The commitment rates are over random party rules at one seed, three nodes, a registered baseline. The
sixteen gates are the whole two-input space, so the gate axis is complete even where the party population is
sampled. Everything is in-silico, and a prior is to be tested against data.

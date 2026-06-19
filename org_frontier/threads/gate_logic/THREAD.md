# Thread — a parity mediator binds twice as readily and shares the credit

A prior for the catalog. The cyclic thread found that topology decides whether a coordination has a
bottleneck. This one holds the topology fixed — the mediated star, parties meeting only through S — and
varies the mediator's gate, the coordination logic by which it combines the two parties. The logic decides
two things the topology does not. A monotone mediator commits half as often as a parity one and takes two
thirds of the credit; a parity mediator commits twice as often and splits the credit into equal thirds.
Reproduce with `python org_frontier/threads/gate_logic/gate_logic.py` (seed 11).

## Setup

The mediator's rule is fixed to one gate of the two parties — AND, OR, XOR, or XNOR — while the parties read
the mediator with random rules. The architecture is the strict star in every case, so S is the only path
between the parties. The measures are the rate of commitment, whether S is the veto player, and S's share of
the Shapley credit when the form commits.

## The arc

**Monotone mediators commit rarely and take two thirds.** An AND mediator and an OR mediator each commit in
12% of forms, and in every committing form the mediator takes a 0.667 credit share, two thirds, leaving the
two parties a sixth each. A monotone gate is dominated by one input value — AND by its zeros, OR by its ones
— so it reads the parties asymmetrically, and the mediator that does the asymmetric reading keeps most of
the credit for it.

**Parity mediators commit twice as often and split the credit evenly.** An XOR mediator and an XNOR mediator
each commit in 24% of forms, twice the monotone rate, and in every committing form the credit splits into
exact thirds, 0.333 each. A parity gate depends on both parties bijectively — flipping either flips the
output — so neither party is dominated, both are equally essential, and the credit divides equally among the
three. The richer dependence also binds the triad more readily.

**The mediator holds the bottleneck regardless.** Across all four gates the mediator is the veto player in
every integrating form. The gate moves the commitment rate and the credit split, and leaves the bottleneck
where the topology put it.

## What the thread establishes

Coordination logic, not only topology, shapes a mediated coordination. A parity mediator — one whose output
turns on both parties bijectively — binds the triad twice as readily as a monotone one and shares the credit
equally, while a monotone mediator binds rarely and concentrates two thirds of the credit on itself. As a
prior for reading real coordination: a mediator that combines its parties symmetrically, so that either can
flip the outcome, predicts an even division and frequent irreducibility, while one that responds to its
parties asymmetrically predicts a mediator that takes the larger share.

## Limits, honestly

The four gates are the symmetric two-input logics; an asymmetric gate, or one of higher arity, would have
its own profile, and this surveys the canonical four. The exact-thirds split under parity follows from the
gate's symmetry in its two inputs, so it is structural, and the value is the contrast with the monotone
two-thirds. The connection to the program's earlier finding that parity logic reaches the Φ ceiling is
direct: parity here both lifts commitment and equalizes the credit. Rates are over random party rules at one
seed, three nodes, a registered baseline. Everything is in-silico, and a prior is to be tested against data.

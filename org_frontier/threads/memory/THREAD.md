# Thread — a mediator that remembers takes more of the credit

A prior for the catalog. The gate-logic thread varied what the mediator computes. This one varies whether it
remembers. A self-loop on the mediator gives it its own intrinsic activity, a state that carries from one
step to the next. Memory does not change whether the triad commits or where the bottleneck sits. It changes
who is credited: a mediator that remembers takes a far larger share of the credit than a memoryless one, and
the parties recover some of it only when they remember too. Reproduce with
`python org_frontier/threads/memory/memory.py` (seed 11).

## Setup

Three architectures over the strict star. In the first the mediator is memoryless, its next state a function
of the two parties. In the second the mediator also reads itself, a self-loop that lets its state persist.
In the third every party reads itself as well. Rules are random. The measures are the rate of commitment,
whether the mediator is the veto player, and its share of the Shapley credit when the form commits.

## The arc

**A memoryless mediator takes about half.** Reading only the two parties, the mediator commits the triad in
10% of forms and takes a 0.55 credit share, a little over an even third, the figure the designed-mediator
thread reported.

**A mediator that remembers takes nearly all of it.** Add the self-loop and the mediator's credit share
rises to 0.88, while the commitment rate barely moves, 10%, and the mediator stays the veto player in every
integrating form. The memory does not make the triad more likely to bind. It gives the mediator intrinsic
activity of its own, a standalone worth the parties lack, and the Shapley value charges that worth to the
mediator, so it takes the larger share of the same coordination.

**When the parties remember too, they claw some back.** Give every party a self-loop and the mediator's
share falls to 0.72. The parties now carry intrinsic activity as well, so the credit the memory conferred is
no longer the mediator's alone, and the division moves back toward the middle. The commitment rate stays
near 10% throughout.

## What the thread establishes

Memory concentrates credit on whoever holds it, without changing whether the coordination commits or who
holds the bottleneck. A mediator with a state of its own takes 0.88 of the credit against the 0.55 of a
memoryless one, and the parties recover ground only by carrying memory themselves. As a prior for reading
real coordination: a mediator that accumulates state — a record, a history, a model of the relationship —
should be credited with more of the coordination than one that only passes the current inputs, and a party
that keeps its own record should hold more against it.

## Limits, honestly

The credit shift follows from the self-loop giving the mediator standalone intrinsic φ, which the Shapley
value attributes to it, so the direction is structural and the value is the size, 0.55 to 0.88, and the
partial recovery to 0.72 when the parties remember. Rates are over random rules at one seed, three nodes, a
registered baseline. Everything is in-silico, and a prior is to be tested against data.

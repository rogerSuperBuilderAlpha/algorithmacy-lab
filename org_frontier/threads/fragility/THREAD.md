# Thread — fragility tracks coordination logic: monotone has one point of failure, parity has three

A prior for the catalog. The gate-logic thread found that a parity mediator binds all three parties equally
while a monotone one keeps two thirds of the credit. This thread reads the same split as resilience. Remove
a node and measure the integration left. Under a monotone mediator only the mediator is a single point of
failure — a party can be dropped with no loss of integration — while under a parity mediator every party is
a single point of failure, and removing any one node destroys all of it. Reproduce with
`python org_frontier/threads/fragility/fragility.py` (seed 11).

## Setup

The canonical triads, the AND mediator and the XOR mediator, with the parties reading the mediator under
random rules. For each triadic form the integration of the whole is taken, and then the integration of the
system with one node removed — the mediator, leaving the two parties, or a party, leaving the mediator and
the other. The measure is the fraction of the whole's integration lost by each removal.

## The arc

**Under a monotone mediator only the mediator is indispensable.** In the AND triads removing the mediator
loses all the integration, a fraction of 1.000, since the two parties meet only through it and have nothing
left when it is gone. Removing a party loses none of it, a fraction of 0.000: the integration survives
intact in the mediator and the remaining party. A monotone coordination has one indispensable node and one
that can be dropped without cost, because its core was already a pair and the dropped party sat outside it.

**Under a parity mediator every party is indispensable.** In the XOR triads removing the mediator loses all
the integration, 1.000, and removing a party loses all of it too, 1.000. Every node is a single point of
failure. A parity mediator binds the three into one structure where each is essential to the rest, so the
loss of any one collapses the whole. This is the gate-logic thread's even credit split seen as resilience:
where the credit divides into equal thirds, each third is load-bearing.

## What the thread establishes

Fragility tracks coordination logic. A monotone coordination has a single point of failure, the mediator,
and a party it can lose without cost; a parity coordination is all-or-nothing, with every party a single
point of failure. As a prior for reading real coordination: an arrangement whose mediator combines its
parties monotonically should survive the loss of a party and collapse only if the mediator goes, while one
whose mediator combines them by parity should be brittle to the loss of any party. Resilience and credit are
the same fact read two ways: the indispensable parties are the credited ones.

## Limits, honestly

Removal here means evaluating the integration of the subset that remains, the same φ_s the cooperative-game
threads use, so the mediator's 1.000 loss is the veto result restated and the contrast that carries the
thread is the party's loss, 0.000 under monotone against 1.000 under parity. The two forms are canonical
representatives of their classes over random party rules at one seed, not a population. Everything is
in-silico, and a prior is to be tested against data.

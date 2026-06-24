# q149 — hypotheses

The Shapley value distributes a subsystem's Φ among its parties. A coalition S is worth the
integrated information of the subsystem restricted to S, and a party's Shapley value is its average
marginal contribution across all orderings. For the read-recipient triad the mediator sits in every
productive coalition, so it captures about two-thirds of the total. This is the mediator rent.

## H1

The Shapley share captured by hub/mediator nodes falls monotonically from the single-hub triad
(~2/3) toward equal shares as mediation distributes across more hubs, so distributing mediation
distributes the rent.

Null: the hub share is constant across topologies.

Operational test: at fixed n, order the hub topologies by the number of mediators (single hub, then
the symmetric m-hub for m = 1, 2, ...) and read the per-hub Shapley share. H1 predicts the per-hub
share is non-increasing in the number of hubs and strictly lower at the most-distributed end than at
the single hub.

## H2

In symmetric topologies (ring, pool) the Shapley values are equal across all nodes to within
tolerance, so structural symmetry forces value symmetry independent of n.

Null: a symmetric topology yields unequal Shapley values.

Operational test: at n = 5 and n = 6 read the spread (max minus min) of the per-node Shapley values
for the ring and the all-required pool. H2 predicts the spread is at or below tolerance (1e-3).

## Scope

In-silico. The forms are synthetic Boolean coordination models. The study characterizes how an
exact-Φ Shapley split behaves across topology families. It measures no real group and no worker.

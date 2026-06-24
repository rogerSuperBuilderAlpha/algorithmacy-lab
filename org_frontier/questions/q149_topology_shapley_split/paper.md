# q149 — The Shapley split of subsystem Φ across topologies

The read-recipient triad has a clean economics. Its integrated information totals 2.0, and the
Shapley split hands the mediator two-thirds of it. The mediator sits in every productive coalition, so
its average marginal contribution dominates. This study asks whether that two-thirds rent is a
property of the single mediator or a property of mediation in general. If mediation is carried by two
hubs, by m symmetric hubs, or by every node in a ring or a pool, does the rent spread out toward equal
shares?

## What the split does

A coalition S is worth the Φ of the subsystem restricted to S at the all-ones integrating state. A
party's Shapley value is its average marginal contribution to that worth over all orderings. The
values sum to the total Φ. The probe applies the existing `shapley` machinery to single-hub, two-hub,
and symmetric m-hub forms at n = 5 and n = 6, and to the ring and the pool as symmetric controls.

## The rent concentrates, it does not spread

Adding hubs does not move value toward the parties. At n = 6 the single hub holds a per-hub share of
2.67. The symmetric three-hub holds 2.35 each, but the four-hub rises again to 2.83, and its party sum
is negative. The ordered per-hub sequence is non-monotone at both sizes, and it is higher at the
most-distributed end than at the single hub. Where the hub share crosses 1.0 the parties carry
negative Shapley value: at the integrating state a party's average marginal contribution is a drag.

The reason is structural. In the conjunctive multi-hub every hub gates on every party and every other
hub, so a party that is part of the integrating state earns its keep only through the hubs, while the
hubs earn through each other. Distributing the mediator role does not divide the rent. It multiplies
the gatekeepers, and each gatekeeper still sits in every productive coalition.

## Symmetry forces equality

The ring and the pool give exactly equal Shapley values. At n = 5 every ring node takes 0.800 and
every pool node takes 4.000. At n = 6 the figures are 0.667 and 5.000. The spread is 0.000 in all four
cases. A topology with a node-transitive automorphism group hands every node the same average marginal
contribution, and the Shapley split respects that symmetry to the last digit.

## Verdicts

H1 is refuted. The per-hub Shapley share does not fall monotonically as mediation distributes; the
rent concentrates, and the multi-hub form drives party value negative. H2 is supported. The ring and
the pool yield equal Shapley values within tolerance at both sizes.

## Scope and limits

The forms are synthetic Boolean coordination models. The study characterizes how the exact-Φ Shapley
split behaves across topology families. It does not measure value capture in any organization, and no
worker is measured. The validation gap between these in-silico forms and any field setting is open.
The contribution is a map of how the split moves with structure, computed exactly on small systems.

# Q114 — The principal captures value by creating it

## Question

Finding 8 found a principal joins the core only when bidirectionally coupled. This asks what joining is
worth, and whether the principal's value comes at the parties' expense (rent) or adds to the total
(creation). The discriminator is whether the parties' values fall or hold when the principal enters.

## Method

Worker E, mediator M, recipient R, principal P. Two principal forms: bidirectional (M reads P and P reads M,
so P is in the core) and monitor-only (P reads M but is not read, so P is outside it). The Shapley value of
each party is computed against the base read-recipient triad, with the coalition value the subsystem's Φ.

## Results

The bidirectional principal captures 0.417, and every party is better off: the worker and recipient rise
from 0.333 to 0.417, the mediator from 1.333 to 1.750, and the total Φ grows from 2 to 3. The monitor-only
principal captures −0.833 and factors the whole system to Φ = 0.

| party | base | bidirectional principal | monitor-only |
|---|---|---|---|
| worker | 0.333 | 0.417 | 0.167 |
| mediator | 1.333 | 1.750 | 0.500 |
| recipient | 0.333 | 0.417 | 0.167 |
| principal | — | 0.417 | −0.833 |
| Φ | 2.0 | 3.0 | 0.0 |

| | result |
|---|---|
| H1 bidirectional principal captures positive value | confirmed |
| H2 monitor-only captures non-positive | confirmed |
| H3 the principal adds value, the parties hold | confirmed |
| H4 the principal grows the total | confirmed |

## Interpretation

The principal creates value. Joining the joint determination, the bidirectional principal enlarges the
coordination from Φ 2 to Φ 3, and the parties all gain: their absolute values rise, and the principal's 0.417
is a share of a bigger whole, drawn from the growth it brings. The cynical reading, the owner inserting
itself to capture rent at the parties' cost, fails here. A principal that genuinely participates in the
determination adds to it, and a positive-sum coordination is the result.

Ownership without participation captures nothing, or less. The monitor-only principal owns the mediator in
the sense of watching its commit, yet it stays outside the determination, so it sits outside the core, and
its read-only coupling factors the whole system. Its Shapley value is negative, like the spectator of Q111:
a party that owns without producing subtracts from the coordination it observes. The value lies in the
productive coupling, never in the ownership alone.

This locates the rent of Q111 precisely. Q111 found the mediator captures two-thirds and called it platform
power; Q114 shows the power belongs to the productive position, with ownership as such incidental. Any party captures value by
occupying a position productive in the joint determination, and a principal is no exception: it captures
value when it couples in and creates it, and captures negative value when it owns without coupling. The rent
is structural, accruing to the productive position, and it cannot be had by ownership alone. A platform
that wants the mediator's share must do the mediator's work.

A mild redistribution accompanies the principal's entry, toward equality and away from concentration. The
mediator's share falls from two-thirds to 58% as the fourth productive party dilutes the concentration, even
as its absolute value rises. Productive entry grows the total and spreads the shares slightly more evenly,
so the parties gain in both value and share, the mediator gains in value and loses in share, and the
coordination becomes larger and a little less concentrated.

## Limitations

In-silico; exact subsystem Φ and Shapley value. One coupling, the symmetric bidirectional principal; the
displacing principal of Finding 8, which contracts the core to {M, P}, is the redistributive case and is
untested here. The monitor-only principal's negative value is the whole-system reading; a major-complex
value function would give it zero. The coalition value is the subsystem Φ at the all-ones state.

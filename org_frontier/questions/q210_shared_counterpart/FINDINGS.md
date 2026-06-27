# Q210 — findings

Two conjunctive triads sharing one counterpart C, with the counterpart's update bridging the two mediators
three ways. n=5, exact IIT-4.0 Φ.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | single triad: triadic, Φ_MIP = 2.000000 |
| H2 the AND bridge merges both mediators into one core | refuted | AND major complex is {W2,S2} (one worker-mediator pair), not both mediators |
| H3 the shared counterpart is in the merged core | refuted | C is not in the AND-bridge core |
| H4 merging two triads is super-additive (core Φ > 2.0) | refuted | every bridge's core Φ is exactly 2.0 |
| H5 the AND bridge gives a higher core Φ than the OR bridge | refuted | both core Φ = 2.0 |

Per-bridge reading: **none** (`C'=S1`) → whole-system dyadic (Φ_MIP=0), core {W1,S1,C} at Φ=2.0; **AND**
(`C'=S1∧S2`) → whole-system triadic (Φ_MIP=2.0), core {W2,S2} at Φ=2.0; **OR** (`C'=S1∨S2`) → whole-system
dyadic (Φ_MIP=0), core {W1,S1,C} at Φ=2.0.

## A shared counterpart does not merge two triads

The expectation was that one shared member would bind two triads into a larger, more integrated core. It
does not. No bridge produces a major complex that spans both triads, and no bridge produces a core above
Φ=2.0. The maximal complex is always one local structure carrying the single-triad value: the first triad
{W1,S1,C} when the counterpart updates from one mediator or either, and a single worker-mediator pair when
it requires both. The two coordinations stay structurally separate. The mediators couple only through the
shared counterpart, and that indirect mediator-counterpart-mediator path is too weak to fold them into one
irreducible whole.

The bridge rule does have an effect, on the whole-system verdict rather than on the core. When the
counterpart commits only if both mediators fire (AND), the whole five-node system is irreducible at
Φ_MIP=2.0, even though its maximal complex is a single pair. When the counterpart updates from one mediator
(none) or from either (OR), the whole system factors to Φ_MIP=0, and a single intact triad carries the
integration. How the shared party combines its two mediators decides whether the whole arrangement is
irreducible, but in no case does it merge the two cores or add integration beyond one triad.

The AND-bridge core, {W2,S2}, is one of two symmetric pairs — the form is symmetric under swapping the two
triads, so {W1,S1} carries the same Φ and the tie is broken arbitrarily. The finding is the size and value
of the maximal complex (a pair, Φ=2.0), not which triad it lands in.

## Caveats

One model of two shared triads, with the shared node a counterpart and three bridge rules. The mediators do
not read each other directly, only through the shared counterpart; a direct mediator-mediator channel is a
separate question. n=5, conjunctive coupling, exact Φ. The AND-bridge core is tie-broken by symmetry.
In-silico; evidence about how a shared party binds two model coordinations, not a measurement of any
organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q210_shared_counterpart.probe_shared_counterpart`

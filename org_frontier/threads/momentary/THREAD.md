# Thread — coordination is momentary: a triad is irreducible at a minority of its states

A prior for the catalog, and the one that qualifies the rest. Being a triadic coordination does not mean
being irreducible all the time. The verdict is read at the one state where Φ is largest, but a coordination
passes through many states, and at most of them it is not irreducible. A triad is irreducible at about a
third of its reachable states on average, and half of all triads are irreducible at just one configuration.
The irreducible determination is committed at some moments and not others. Reproduce with
`python org_frontier/threads/momentary/momentary.py` (seed 11).

## Setup

Three-party forms with random rules, restricted to the triadic ones. For each, the classifier records how
many of the reachable states are irreducible, those with Φ above the threshold, against how many states it
evaluates. The measures are the average fraction of states that are irreducible and the share of triads
irreducible at exactly one state.

## The arc

**A triad is irreducible at a minority of its states.** Across 1659 triadic forms the mean fraction of
reachable states at which the system is irreducible is 0.36. For most of the time a triadic coordination
spends moving through its states, it factors; the verdict names the one state where it is
most integrated, and that state is the exception.

**Half of triads are irreducible at a single state.** Of the triadic forms, 822 — half — are irreducible at
exactly one configuration, and the count falls off from there: 367 at two states, 242 at three, and a thin
tail above. A triadic coordination is, as often as not, a momentary thing, committing its irreducible
determination at one configuration and factoring at every other.

## What the thread establishes

Coordination is momentary. A triadic form is irreducible at about a third of its states on average and at
only one state half the time, so being a coordination means committing an irreducible determination at some
moments, without holding one continuously. As a prior for reading real coordination: an arrangement that reads as
irreducible should be expected to be so intermittently, at particular configurations, and not at all
times, and a snapshot that finds it factoring is consistent with its being a genuine coordination caught
between its moments. This qualifies the rest of the catalog: the bottleneck and credit findings describe the
states where the coordination is irreducible, and those are the minority the verdict is read from.

## Limits, honestly

The count of irreducible states depends on the threshold that separates a positive Φ from zero, so the exact
fraction would move with it; the qualitative result, a minority of states and a mode at one, is robust to a
small threshold. The rates are over random rules at one seed, three nodes, a registered baseline. The verdict
convention — read at the maximum-Φ state — is the program's, and this thread measures what that convention
leaves out. Everything is in-silico, and a prior is to be tested against data.

# Thread — memory pays at the center, not at the periphery

A prior for the catalog. The memory thread found that a self-loop on the mediator raised its share of the
credit sharply. The natural read was that accumulating state confers standing. This thread checks the read
by giving the memory to a party instead, and it fails. Memory pays at the center and not at the periphery. A
self-loop on the mediator raises its credit share by about a third; the same self-loop on a party leaves
that party's share where it was, a touch lower. What a record is worth depends on the position that keeps it.
Reproduce with `python org_frontier/threads/position_of_memory/position_of_memory.py` (seed 11).

## Setup

The strict star, parties reading the mediator under random rules. A self-loop — a node reading its own
previous state — is added to one position at a time, and the credit share of that position is measured
against the same position without the loop. The mediator reads the two parties; a party reads the mediator.
The measure is the Shapley credit share, over the triadic forms.

## The arc

**At the center, memory pays.** The mediator's share rises from 0.55 without a self-loop to 0.88 with one, a
gain of about a third of the whole's credit. The mediator reads both parties, so the state it carries feeds
the entire coordination at the next step, and the Shapley value charges that propagated intrinsic activity
to it. A mediator that keeps a record holds far more of the coordination than one that only passes the
current inputs.

**At the periphery, it does not.** A party's share is 0.22 without a self-loop and 0.18 with one, a change of
negative four hundredths — no gain, a slight loss. A party is read only by the mediator, so the state it
carries reaches the coordination through that one channel and no further, and the record it keeps does not
propagate the way the mediator's does. The same memory that is worth a third of the credit at the center is
worth nothing at the edge.

## What the thread establishes

The value of memory depends on position. A self-loop at the center, the mediator, raises its credit share by
a third; the same self-loop at the periphery, a party, confers no advantage. Accumulating state pays where
the state feeds the whole coordination and not where it feeds only one channel into it. As a prior for
reading real coordination: a mediator that builds a record — a history, a model, a profile of the
relationship — should gain standing from it, while a party that keeps its own record should gain little,
because the party's record reaches the arrangement only through the mediator it must still go through.

## Limits, honestly

The center result is the memory thread's, recomputed here as the comparison point; the new finding is the
periphery's null, that a party's self-loop does not raise its share. The shares are over random rules at one
seed, three nodes, a registered baseline. Everything is in-silico, and a prior is to be tested against data.

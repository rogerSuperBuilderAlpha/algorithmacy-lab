# Thread — a quorum coordination binds only at the extremes, never at a majority

A prior for the catalog. A quorum mediator fires when at least k of its parties are active. This thread asks
which thresholds can bind an irreducible coordination, and only the extremes can. A mediator that needs any
one party, or all of them, commits in a few percent of forms; a mediator that needs a majority never commits
at all. The interior threshold factors. The mediator is the bottleneck at every threshold. Reproduce with
`python org_frontier/threads/quorum/quorum.py` (seed 11).

## Setup

Three parties feed a mediator whose rule is a threshold: it is active when at least k of the three are. The
parties read the mediator under random rules. The thresholds are k = 1, any party suffices; k = 2, a
majority; and k = 3, all three. The measure is the rate of commitment and whether the mediator is the veto
player.

## The arc

**The extremes commit.** With k = 1 the form commits in 12 of 400 draws, 3%, and with k = 3 in 12 of 400 as
well. A mediator that fires on any party, or only on all of them, can bind the parties into an irreducible
coordination, at the same low rate at either end.

**The majority does not.** With k = 2 the form commits in none of the 400 draws, 0%. A mediator that needs a
majority of its parties cannot bind them into an irreducible whole. The interior threshold lets the
coordination factor: a majority gate is insensitive to which particular parties are active once enough are,
so it does not hold each party to the determination the way the all-or-any extremes do, and the structure
comes apart.

**The mediator holds the bottleneck throughout.** At every threshold the mediator is the veto player in
every integrating form, 170, 247 and 158 of those. The threshold decides whether the parties bind into the
coordination, not whether the mediator sits at its center.

## What the thread establishes

A quorum coordination binds only at its extremes. A mediator that requires any one of its parties, or all of
them, can produce an irreducible coordination; one that requires a majority cannot, and the interior
thresholds factor. As a prior for reading real coordination: a quorum or voting arrangement should read as
an irreducible whole only when its rule is all-or-nothing in the relevant sense — every party needed, or any
party enough — and a genuine majority rule should read as factoring, the mediator dealing with a
sufficient set rather than binding the particular parties. This is the program's extremes-only quorum law,
registered here with the mediator's veto held throughout.

## Limits, honestly

The commitment rates at the extremes are low, 3%, over random party rules, so the load-bearing contrast is
the majority's exact zero against the extremes' nonzero. The thresholds are over three parties; wider quorums
would have more interior thresholds, all expected to factor. Random rules at one seed, four nodes, a
registered baseline. Everything is in-silico, and a prior is to be tested against data.

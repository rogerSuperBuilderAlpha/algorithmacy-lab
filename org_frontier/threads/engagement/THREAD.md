# Thread — a party is bound by coupling, not by heeding the mediator

A prior for the catalog. The back-edge thread asked what makes a mediator commit and answered the return
path. This one asks the dual question about a party: what binds a party into a mediated coordination. The
answer is coupling. A party is a member when it is coupled to the rest — when it heeds the mediator, or when
it reads the other party — and a party coupled to neither cannot be a member, which collapses the triad to
the engaged dyad. Heeding the mediator is one way in among others. Reproduce with
`python org_frontier/threads/engagement/engagement.py` (seed 11).

## Setup

Three architectures share a mediator S that reads both parties and a worker W that heeds S. They differ in
how the counterpart C is wired. In the first C heeds S, the bidirectional baseline. In the second C is
autonomous, reading only itself, coupled to nothing. In the third C reads the worker instead of the
mediator, coupled to the coordination through the other party. The rules are random, so commitment is open.
The measures are the rate of commitment, whether S stays the veto player, S's credit share, and whether C is
in the major complex when the form commits.

## The arc

**Heeding the mediator binds the party.** When C heeds S, the triad commits in 10% of forms, and in every
committing form C is in the major complex, 62 of 62. The party that reads the mediator is a member whenever
there is a triad to be a member of. This is the baseline.

**A party coupled to nothing cannot be bound, and takes the triad down with it.** When C is autonomous,
reading only itself, the triad never commits, 0 of 600. A party that neither heeds the mediator nor reads
the other party is coupled to nothing, so it cannot enter the major complex, and its presence leaves the
system as the W–S dyad. The disengaged party does not merely exclude itself. It removes the third coupling
the triad would need, so the form has no triadic verdict to give.

**Coupling through the other party binds it just as well.** When C reads the worker instead of the
mediator, the triad commits in 19% of forms — more often than the bidirectional baseline, since C → S and
W → C close a feedback cycle — and C is in the major complex in 81% of those. A party that never heeds the
mediator is a full member of the coordination, bound through its read of the other party. Membership tracks
whether the party is coupled to the coordination, by any path, whatever path that is. The mediator stays the veto player throughout, in every integrating form of all three
architectures.

## What the thread establishes

What binds a party into a mediated coordination is coupling, not the direction of a particular edge or a
read of the mediator in particular. A party that heeds the mediator is bound; a party coupled only through
the other party is bound as well; a party coupled to nothing cannot be bound and collapses the triad to the
engaged dyad. As a prior for reading real coordination: a party's membership in the irreducible core should
turn on whether it is coupled into the arrangement at all, and a party that reads neither the system nor its
counterpart is outside it, taking the third seat with it. The mediator's bottleneck position survives every
variation, since the parties still meet only through it.

## Limits, honestly

The autonomous-party result is close to definitional — a node reading only itself has no edge to the rest,
so it cannot join an integrated complex — and the value here is the contrast with the coupled-through-the-
other-party case, which is not definitional and shows membership without heeding the mediator. The higher
commitment of the third architecture is a feature of the feedback cycle its coupling forms, specific to this
wiring. The rates are over random rules at one seed, three architectures, three nodes, a registered baseline
short of a measured fact about real coordination. Everything is in-silico, and a prior is to be tested
against data, never asserted of it.

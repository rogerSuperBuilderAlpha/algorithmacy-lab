# Thread — substitutability is the enemy of integration: a pool never binds, a team binds both

A prior for the catalog. A platform connects two workers to a counterpart. Whether the workers are a team or
a pool decides whether the coordination binds. When the platform needs both workers jointly — a team — the
whole commits and both workers enter the core. When either worker will do — a pool — the whole never
commits: the redundant worker makes the system factor. Substitutability is the enemy of integration. The
platform is the bottleneck either way. Reproduce with
`python org_frontier/threads/substitutability/substitutability.py` (seed 11).

## Setup

Four parties: two workers, a platform, and a counterpart, the workers reaching the counterpart only through
the platform. The platform's gate is fixed to one of two logics. The team logic requires both workers and
the counterpart together. The pool logic takes either worker with the counterpart. The workers read the
platform with random rules. The measures are the rate of commitment, whether the platform is the veto
player, whether both workers are in the major complex, and whether the two workers are interchangeable.

## The arc

**A team binds both workers.** With the team logic the form commits in 12 of 400 draws, and in every
committing form both workers are in the major complex, 12 of 12, and the two are interchangeable, 12 of 12.
When the platform needs both, both are essential and both are members, in the same symmetric standing the
bottleneck-symmetry thread described for jointly indispensable parties.

**A pool never binds.** With the pool logic the form commits in none of the 400 draws, 0. Either worker
suffices, so neither is essential, and the system factors: the platform plus one worker plus the counterpart
carries the same structure as the whole, and a part equal to the whole is the definition of a reducible
system. A pool of substitutable workers cannot be welded into one irreducible coordination, however the
platform routes them.

**The platform holds the bottleneck either way.** In both logics the platform is the veto player in every
integrating form, 158 of 158 for the team and 225 of 225 for the pool. Substitutability decides whether the
workers bind into the coordination; the platform sits at its center regardless.

## What the thread establishes

Substitutability is the enemy of integration. Workers the platform needs jointly bind into the core, both of
them and as equals; workers either of whom would do never bind at all, because their redundancy lets the
coordination factor. As a prior for reading real coordination: a platform whose workers are interchangeable
and individually dispensable predicts an arrangement that does not read as one irreducible whole, only as
the platform's separate dealings, while a platform that requires its workers together predicts a bound team
in which each worker is a member. This is the market reading — a pool of interchangeable agents is a
broadcast, not a triad — derived here from the logic of the platform's demand.

## Limits, honestly

The team commitment rate is low, 12 of 400, so its both-in-core and interchangeability figures, though
unanimous, are over a small set; the pool's never-commits, 0 of 400, is the robust half of the contrast. The
two gates are representatives of the required and substitutable logics, not a population, with random worker
rules at one seed. Everything is in-silico, and a prior is to be tested against data.

# Thread — the irreducible moments are engagement-blind

A prior for the catalog, extending the momentary thread. A triad is irreducible at only a minority of its
states; the natural guess is that those are the busy states, where many parties are switched on. The guess is
wrong. The states at which a coordination is irreducible carry about as many active parties as the states at
which it factors, both near the uniform average. Whether the system is irreducible does not track how
engaged the parties are. Reproduce with
`python org_frontier/threads/engagement_blind/engagement_blind.py` (seed 11).

## Setup

Three-party forms with random rules, restricted to the triadic ones. For each reachable state two things are
recorded: how many parties are active in it, from zero to three, and whether the system is irreducible there,
its Φ above the threshold. The activity at the irreducible states is compared with the activity at the
reducible ones.

## The arc

**Irreducible and reducible states carry the same activity.** The irreducible states average 1.468 active
parties and the reducible states 1.512, both within a few hundredths of the uniform 1.5 a state would have if
activity were unrelated to anything. The system is no busier at the moments it is irreducible than at the
moments it factors.

**The irreducible states spread across all activity levels.** Counted by activity, the irreducible states run
440 with no party active, 1301 with one, 1241 with two and 389 with all three, a spread that tracks how many
states have each activity level rather than favouring the full ones. A coordination's irreducible moments are
not the all-hands configurations; they fall at idle and busy states alike.

## What the thread establishes

A coordination's irreducible moments are engagement-blind. The states where a triad is irreducible carry the
same number of active parties, on average, as the states where it factors, and they spread across every
activity level. As a prior for reading real coordination: the moments an arrangement reads as an irreducible
whole are not predicted by how many of its parties are visibly active, so a busy configuration is no more
likely to be the integrated one than an idle one, and the irreducible moment has to be found from the
structure rather than from the level of activity. With the momentary thread it completes the timing picture:
a coordination is irreducible at few of its states, and which few is not a matter of how engaged it looks.

## Limits, honestly

The activity measure is the count of parties in the on-state, one summary of a configuration; a different
feature might separate the irreducible states where activity does not. The small gap, 1.468 against 1.512,
runs slightly the other way from the busy-states guess but is too small to read as a real tilt toward idle
states. The rates are over random rules at one seed, three nodes, a registered baseline. Everything is
in-silico, and a prior is to be tested against data.

# Thread — normalizing Φ collapses the core to one party

A standing objection to integrated information is that Φ rises with system size, so it should be normalized
— divided by the number of elements — before systems are compared. IIT refuses: the major complex is the
subset of largest φ_s, not largest φ_s per element. This thread measures what the normalized version would
select, and the answer is a reason to keep absolute φ_s. Reproduce with
`python org_frontier/threads/normalization/normalization.py` (seed 11, 300 three-node forms).

## Setup

Density of a coalition is d(S) = φ_s(S) / |S|, its integrated information per party. A normalized exclusion
postulate would keep the density-maximal subset instead of the φ_s-maximal one. The major complex is the
absolute pick; the question is what the per-element pick is, and what that does to the multi-party core IIT
is built to find.

## The arc

**Normalized exclusion keeps a single party.** The density-maximal subset is one party in 281 of 298 forms,
94%. A lone element with intrinsic φ has the highest integration per element, since adding a second party
divides by two faster than it adds φ. The mean size tells the same story: the absolute major complex
averages 1.70 parties, the density-maximal subset 1.07. Normalizing turns the core into a point.

**It mis-reads the forms the theory is about.** Restrict to triadic forms, where the whole is irreducible
and the coordination is genuinely multi-party. The density-maximal subset is still a lone party in 146 of
158, 92%. A normalized reading would call almost every irreducible three-party coordination a single
element, discarding the structure that made it triadic.

**The collapse is a singleton attractor.** Forbid singletons and score density only over coalitions of two
or more. Now the density pick shrinks a multi-party major complex
in 16 of 184 forms, 9%. Among genuine coordinations the per-element and absolute rules mostly agree; the
94% gap is the lone element pulling the maximum to itself. Per-element normalization does not re-rank
coordinations so much as replace them with a point.

## What the thread establishes

Per-element normalization of φ_s keeps a single party in 94% of forms and in 92% of triadic ones, against an
absolute major complex that averages 1.70 parties. The normalized rule trivializes the exclusion postulate:
the densest object is almost always one element, so the search for a multi-party complex returns a lone
party. Absolute φ_s is what lets IIT pick out a coordination at all, and that is the dissertation's reason
for using it. When the comparison is held to real coordinations of two or more parties, the two rules agree
in 91% of forms, so the case for absolute φ_s is specifically about not letting a single element win on
density.

## Limits, honestly

The collapse depends on single elements carrying intrinsic φ, which they do in these random Boolean forms;
a setting where lone parties have no standalone integration would weaken the singleton attractor and narrow
the gap toward the 9% size-≥2 figure. The result is a demonstration on three-node forms of a point that is
analytic in spirit — dividing by size rewards the smallest unit — rather than a new empirical law. Its value
is concrete: it shows the size of the effect and locates it in the singleton, and it answers the normalize-Φ
objection on the program's own models. The thesis claim it supports is narrow
and correct: absolute φ_s is load-bearing for a multi-party core, and the normalized alternative does not
preserve one.

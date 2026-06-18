# Thread — co-bottlenecks share equally only when interchangeable

The joint-bottleneck thread reported that the two members of a veto pair share the credit roughly evenly, a
within-set Shapley ratio averaging 0.78. That average was a blend. Cooperative game theory is exact about
when two parties get equal credit: the symmetry axiom gives them equal Shapley exactly when they are
interchangeable in the game. Testing the veto pairs against that condition splits the 0.78 into two regimes —
an even split when the pair is interchangeable, a sharply uneven one when it is not. Reproduce with
`python org_frontier/threads/bottleneck_symmetry/bottleneck_symmetry.py` (seed 11, 600 four-party forms
scanned; slow, veto pairs are rare).

## Setup

Two parties are interchangeable in the game when swapping them never changes a coalition's worth: for every
coalition S that contains neither, v(S ∪ {a}) = v(S ∪ {b}). The symmetry axiom of the Shapley value gives
interchangeable parties equal value. A veto pair is two parties both in every integrating coalition. The
question is whether the two are interchangeable, which the axiom turns into a question about their credit.
Scanning 600 four-party forms turns up 22 with a veto pair.

## The arc

**The sharing is the symmetry axiom, exactly.** Among the 22 veto pairs, the 13 that are interchangeable
have a within-set Shapley ratio of 1.000 — the two members are paid identically, to the precision of the
computation. This is the axiom doing what it must, and its appearance here confirms that the interchangeability
test and the Shapley computation agree. Equal indispensability is not enough for equal credit; equal role is.

**When the role differs, the credit splits hard.** The 9 pairs that are not interchangeable have a within-set
ratio of 0.408. The lesser member is paid under half what the greater is, even though both sit in every
integrating coalition. Two parties can be jointly indispensable and still play different parts, and the
Shapley value reads the difference in parts as a difference in pay.

**The 0.78 was a mixture.** The joint-bottleneck thread's even-sharing average came from these two regimes
laid on top of each other: a little over half the pairs split the credit exactly evenly, the rest split it
about 0.4, and the mean landed between. The within-set credit is not a single tendency toward even sharing.
It is bimodal, and the mode a pair falls into is set by whether the two members are interchangeable.

## What the thread establishes

The credit inside a veto pair is governed by the symmetry axiom and nothing softer. Interchangeable members
are paid identically, 1.000, and members that are merely both indispensable but distinct are paid 0.408. The
joint-bottleneck thread's 0.78 average is the blend of a 59% interchangeable regime at one and a 41% distinct
regime near 0.4. Joint indispensability shares the credit only when the parties are interchangeable; when
they are not, one co-mediator is paid the lion's share while the other holds an indispensable but lesser seat.

## Limits, honestly

Twenty-two veto pairs is a small sample, forced by the structure being rare and four-node exact Φ being slow.
The 1.000 for interchangeable pairs is guaranteed by the symmetry axiom, a theorem, so it is a consistency
check rather than a discovery; the empirical content is how often co-bottlenecks are interchangeable, about
three in five here, and how unequal the rest run, about 0.4. Those two numbers will move with the population.
What makes two jointly indispensable parties non-interchangeable is not pinned down — connectivity degree
does not separate them, so the difference is a finer one in how each contributes to intermediate coalitions.
Everything is in-silico on Boolean forms at one seed. This refines the joint-bottleneck thread rather than
overturning it: the credit a veto pair captures is shared evenly when the members are interchangeable and
concentrated on one when they are not.

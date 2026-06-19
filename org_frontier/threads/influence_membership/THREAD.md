# Thread — influence is universal and does not determine membership

A prior for the catalog. A party can shape what the others do without being part of the coordination's
irreducible core. This thread crosses each party's influence — whether flipping it changes any party's next
state — against its membership in the major complex. Every party is influential, and a third of the
influential party-instances sit outside the core. Influence is universal; it does not determine membership.
Shaping behavior is not the same as being constitutive of the coordination. Reproduce with
`python org_frontier/threads/influence_membership/influence_membership.py` (seed 11).

## Setup

Three-party forms with random rules, restricted to the triadic ones. For each party two facts are taken: its
Boolean influence, whether flipping its state changes some party's next state at any configuration, and its
membership, whether it is in the major complex. The party-instances are crossed into the four cells of
influential-or-not against in-core-or-not.

## The arc

**Every party is influential.** Of the party-instances in 1082 triadic forms, none has zero influence:
neither the in-core nor the out-of-core parties include a single uninfluential one. In a triadic
coordination every party changes what some other party does at some configuration. Influence, in this
Boolean sense, is universal.

**A third of the influential are outside the core.** Of the influential party-instances, 2062 are in the
major complex and 1184 are outside it. More than a third of the parties that shape the others' behavior are
not members of the irreducible core. A party can push the determination around — flip outcomes, move the
next states — and still be excluded from the coordination that is irreducible. Influence reaches outside
membership.

## What the thread establishes

Influence and membership are different things, and influence does not determine membership. Every party in a
triadic coordination is influential, yet a third of the influential parties are outside the major complex,
so the ability to shape behavior does not make a party part of the irreducible core. As a prior for reading
real coordination: a party that visibly affects what the others do is not thereby a constitutive member of
the arrangement, and the question of who is bound into the irreducible coordination is separate from the
question of who can push it around. This is why a single-party influence measure predicts core membership
only moderately, as the Shapley-membership thread found: influence is common and membership is selective.

## Limits, honestly

Influence here is the single-party Boolean sensitivity the membership study used, one of several ways to
measure a party's effect; a coalitional or magnitude-weighted measure would draw the line differently, and
the Shapley value is the cooperative-game refinement the other threads use. The cross-tab is over random
rules at one seed, three nodes, a registered baseline. Everything is in-silico, and a prior is to be tested
against data.

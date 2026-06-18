# Thread — the mediator takes the credit, the excluded party owes it

The veto thread showed the mediator carries the largest Shapley value. This thread measures how much
larger. In a triadic form the credit for the coordination's integration concentrates on one party, and how
far it concentrates depends on the exclusion postulate: when every party is in the major complex the credit
is shared, and when exclusion drops a party the credit goes winner-take-all and the dropped party's share
turns negative. Reproduce with
`python org_frontier/threads/credit_concentration/credit_concentration.py` (seed 11, 300 three-node forms).

## Setup

The Shapley value pays each party its average marginal contribution to v(S) = φ_s(S), and the payments sum
to the whole's worth v(N), which is positive exactly when the form is triadic. A party's share is its
Shapley value over v(N). An equal split gives each of three parties one third. The questions: how far from
equal the split runs, and what sets the distance.

## The arc

**The credit concentrates on one party.** Across 158 triadic forms the top party holds a majority of the
credit in 86% and almost all of it, over 90%, in 54%. The Gini of the shares averages 0.43, far from the
zero of an equal split. The integration of a three-party coordination is, as a rule, one party's credit.

**Concentration tracks exclusion.** Split the triadic forms by the major complex. When all three parties
are in it, the top share averages 0.53 — close to a party holding half, the credit genuinely shared. When
the complex is a proper subset, the common case, the top share averages 1.12. The party at the center takes
more than the whole is worth, and the structure that decides which case holds is exactly which parties
exclusion keeps.

**The excluded party owes credit rather than earning none.** A top share above one is possible only because
some share is negative, and the negative share belongs to an excluded party in 78% of the proper-subset
forms. A party outside the major complex does not merely fail to add integration. Its presence lowers the
integration of the coalitions it joins, so its average marginal contribution is below zero, and the party
at the center is credited with more than v(N) to make up for it. This is the subadditive dilution of the
earlier threads, read as a payment: the third party that drops the whole below its tightest pair is charged
for the drop.

## What the thread establishes

The credit for a triadic coordination's integration is one party's in most forms — majority share in 86%,
near-total in 54%, Gini 0.43 — and the degree is set by exclusion. A coordination that binds all three
parties shares the credit near evenly, top share 0.53. A coordination that excludes a party concentrates it
past the whole's worth, top share 1.12, because the excluded party carries negative credit in 78% of those
forms. Mediation that keeps everyone essential is egalitarian in its credit; mediation that excludes is
winner-take-all, and the excluded party is a net drag, not a bystander.

## Limits, honestly

The top-share party is the veto player and the Shapley-argmax party of the earlier threads; this thread adds
the magnitude and the split by exclusion, not a new pivotal party. The negative shares are the subadditivity
thread's dilution seen on the allocation side, so the mechanism is established and what is new is its size.
The full-triad cell is small, 25 forms, so its 0.53 is indicative; the proper-subset cell carries the main
weight at 133. Shares above one are an honest consequence of negative Shapley values in a non-monotone game,
not an artifact to normalize away. Everything is in-silico on three-node Boolean forms over a sampled
population. The organizational reading is the point: a mediated coordination hands its credit to one party
unless every party is essential, and a party shut out of the irreducible core is charged for being in the
way.

# Thread — the mediator is a veto player

The Shapley thread showed the mediator carries the largest Shapley value over the game v(S) = φ_s(S) and
left the reason implicit. Cooperative game theory supplies it. A veto player is a party that belongs to
every winning coalition, and a standard fact is that a veto player carries the maximal Shapley value: every
coalition needs it, so its average marginal contribution dominates. This thread shows the mediator is that
veto player, and that being one is necessary but not sufficient for committing an irreducible
determination. Reproduce with `python org_frontier/threads/veto_player/veto_player.py` (seed 11, 400
three-node forms).

## Setup

Call a coalition of two or more parties *integrating* when its system integrated information φ_s exceeds
zero. A party is a *veto player* when it sits in every integrating coalition: no two other parties can
integrate without it. For three parties this reads off the complement — party m is a veto player exactly
when the opposite pair fails to integrate alone. A veto player is the cooperative-game name for a
structural bottleneck, the platform thread's party with no outside option for the others.

A form has a single bottleneck when the integrating coalitions share exactly one common party. Over 400
random three-node forms, 115 do. The questions: is that party the Shapley-dominant one, and does holding the
bottleneck mean the form commits an irreducible determination.

## The arc

**The veto player is the Shapley-dominant party — exactly.** In all 115 single-bottleneck forms the veto
player is the argmax-Shapley party, 115 of 115, and its Shapley value is positive in every one. This is the
classical dominance fact realized on these models, and it answers the Shapley thread: the mediator carries
the largest Shapley value because it is a veto player. The pivotality the Shapley thread measured is the
shadow of a structural position, a party every productive coalition must include.

**Holding the bottleneck is not the same as committing a determination.** Of the 115 single-bottleneck
forms, 89 are triadic and 26 are dyadic — 77% against 23%. A quarter of the forms with a single
indispensable party are still reducible. The verdict and the bottleneck come apart, and they come apart in
one direction: a party can be structurally necessary while the whole stays factorable.

**The dyadic bottleneck is a hub that conveys.** Every one of the 26 dyadic bottlenecks has the same shape:
the integrating coalitions are exactly the two pairs through the bottleneck, each a two-party dyad, with no
larger coalition integrating, 26 of 26. The bottleneck party bridges two separate dyads. It integrates with
each neighbor one at a time and the three never bind into a single irreducible determination. This is the
commit-versus-convey line read in coalition terms: the hub conveys across two channels, while the mediator
of a triadic form commits one determination both parties must heed.

**The bottleneck usually sits in the irreducible core.** The veto player is in the major complex in 105 of
115 forms, 91%. The residue is mostly the dyadic hubs, where the complex is one of the two dyads and the
state read for the complex can land on the other.

## What the thread establishes

The mediator's Shapley dominance has a name and a reason: the mediator is a veto player, and veto players
carry the maximal Shapley value. The bottleneck, the outside-option party, and the pivotal party are one
party seen three ways. And the bottleneck is necessary but not sufficient for irreducible mediation: a
quarter of single-bottleneck forms are hubs that convey across two dyads rather than commit one
determination, which is the commit-versus-convey distinction in cooperative-game form.

## Limits, honestly

The veto-equals-Shapley-argmax result is a clean realization of a known theorem, not a new theorem; its
value is the bridge it draws between the program's pivotality, platform-position, and bottleneck readings,
which were separate until now. The 77/23 triadic split and the 91% core membership are descriptive over 115
forms and depend on the sampled population; the load-bearing facts are the two that hold exactly, the
Shapley dominance and the two-dyad shape of every dyadic bottleneck. Everything is in-silico on three-node
Boolean forms, where the veto player reads directly off one complement pair. The hub-versus-mediator
contrast is the result worth carrying forward: structural indispensability is real and measurable, and
committing a determination is a separate property a bottleneck can lack.

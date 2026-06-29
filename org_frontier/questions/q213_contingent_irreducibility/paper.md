# Contingent irreducibility: a party held in the core by a constraint, not a role

<code + data: org_frontier/questions/q213_contingent_irreducibility/ ; classifier in org_frontier/classifier/contingency.py ; probe #367 in probes/PROBES.md>

## Abstract

A mediator sits in a coordination's irreducible core for one of two reasons, and the lab has been reading
them as the same. Either the mediator does integrative work no direct edge between its neighbours can
reproduce, or it is a conduit that would factor out and is held in the core only because a constraint forbids
the parties from reaching each other directly. The first is intrinsic irreducibility; the second is
contingent. A car dealer relays a car from maker to buyer and integrates nothing, yet franchise law forbids
the maker selling direct, so the dealer cannot be removed. This paper defines the category, builds a reusable
classifier — the bypass-counterfactual, which restores the forbidden edge and recomputes the major complex —
and validates it on four constructed forms. The car dealer reads as contingent with a contingency margin
equal to its entire Φ; a conjunctive clearinghouse under the same operation reads as intrinsic with margin
zero; a clearinghouse with a parallel back-channel reads as partial; a free conduit reads as reducible. The
category is the formal counterpart of an institution that makes a party indispensable de jure while it stays
a conduit de facto.

## Introduction

Most of the lab's work asks whether a coordination form is irreducible — whether its parties are bound into a
single joint determination, with the mediator in the core, or whether the form factors into a chain dyad with
the mediator written out. The instrument is exact integrated information: a triad reads triadic when Φ_MIP is
positive and the major complex spans all three parties, dyadic when it factors. The constitutive-mediation
law sharpens the verdict into a causal story. A mediator that integrates — that commits on a joint condition
of both parties — is in the core; a conduit that merely relays, a store that holds inputs for a party to
decide, a back-channel that lets the parties reach each other directly, each factors.

That law reads irreducibility off the mediator's own rule. It has no room for a case that is common in real
coordination: a mediator that does no integrating work, that by its rule alone should factor, and that sits
in the core anyway because something outside the mechanism forbids the bypass around it. The car dealer is
the standard example. The dealer takes a car from the manufacturer and hands it to the buyer. It computes
nothing, integrates nothing, and adds no joint condition. By the constitutive law it is a conduit and the
triad should collapse to a manufacturer–buyer dyad. It does not, because in most of the United States
franchise law forbids a manufacturer selling a new car directly to the public. The buyer must go through the
dealer. The dealer is irreducible — and irreducible for a reason the mediator's rule does not contain.

This paper names that reason and builds the instrument that detects it. The category is contingent
irreducibility: a party is in the core, but only because a constraint forbids the bypass, and it would leave
the core the moment the constraint lifted. The instrument is the bypass-counterfactual: restore the forbidden
edge and ask whether the party survives.

## Related work

The constitutive-mediation law (`essays/mediated_or_irreducible.md`) is the result this category is the
exception to. Its three conditions — a feedback loop, every party live and none substitutable, an integrating
determination rather than a store — are all properties of the mediator's own function, and they classify the
car dealer as a conduit that should factor.

Two prior lines supply the mechanism and the foil. The back-channel program (q51–q62) adds a direct
worker–counterpart edge to a mediated form and reads how the verdict moves; a one-sided back-channel makes six
of eight matched-read forms triadic below the ceiling, a symmetric one restores Φ=2.0. The bypass-counterfactual
is that same edge restoration, turned from a question about ceilings into a diagnostic on a single party.
q96, on contingent membership, is the matched foil. There a party read only when a state gate is on does not
form a triad: gated participation behaves as optionality and the whole system reads dyadic. That contingency
is on system state and resolves toward optionality. The contingency named here is on an external constraint
and resolves the opposite way, toward irreducibility.

Two more lines locate the contribution. The design-operations program (q106) writes parties into and out of
the core with three reversible levers — binding, liveness, requirement — each of which changes the mediator's
function. The membership law (q98) admits a party that is bidirectionally coupled and pivotal. Contingent
irreducibility is a third route into the core that uses neither: it leaves the mediator's function untouched
and makes the party indispensable by removing everyone's alternative to it.

## The category and the instrument

A party in a triad's core is intrinsically irreducible if it stays in the core when the forbidden direct edge
between the two parties it sits between is restored, and contingently irreducible if it leaves. The
contingency margin is the whole-system Φ_MIP lost when the bypass opens. The classifier
(`classifier/contingency.py`) computes the major complex of the constrained system, restores the edge with
`add_bypass`, recomputes, and returns a four-way label:

- **reducible** — the party is not in the constrained core; it is a free conduit, already out.
- **contingent** — in the core, leaves under the bypass; held de jure by the constraint. Margin is its full Φ.
- **partial** — in the core, stays under the bypass, but Φ_MIP drops by more than ε; part role, part constraint.
- **intrinsic** — in the core, stays, margin ≈ 0; held de facto by its own integrating work.

The bypass is restored two ways, chosen by the modeler to match the constraint being lifted. `mode="replace"`
disintermediates: the downstream party reads the upstream party instead of its mediated source, the maker
selling direct. `mode="add"` opens a parallel back-channel alongside the mediator, downstream' = original ∨
upstream. The replace mode is the franchise-law counterfactual and the primary test.

## Methods

Four forms at n=3, exact IIT-4.0 Φ via `probes/lib.verdict` and `major_complex`. The instrument control, the
conjunctive triad W'=S, S'=W∧C, C'=S, passed at triadic Φ=2.000000 before any classification was read.

| form | rules | party | bypass |
|---|---|---|---|
| conjunctive clearinghouse (intrinsic) | W'=S, S'=W∧C, C'=S | S | C reads W (replace) |
| car dealer (contingent) | M'=B, D'=M, B'=D | D | B reads M (replace) |
| clearinghouse + back-channel (partial) | W'=S, S'=W∧C, C'=S | S | C'=S∨W (add) |
| free conduit (reducible) | M'=B, D'=M, B'=M | D | B reads M (replace) |

In the car dealer the maker makes to demand (M'=B), the dealer relays (D'=M), and the constraint is the
buyer's rule: bound to the dealer, B'=D; free to source direct, B'=M. The one edge that flips is the law.

## Results

All five hypotheses confirmed. The constrained car dealer reads triadic at Φ_MIP=2.0 with the dealer in the
core {M,D,B}, a relay conduit irreducible under the constraint (H2). The bypass-counterfactual disintermediates
it: under B'=M the dealer leaves the core, the system reads dyadic, Φ_MIP falls to 0.0, and the classifier
returns contingent with a margin of 2.0 (H3). The conjunctive clearinghouse under the matching operation does
not move: S stays in the core, Φ_MIP holds at 2.0, margin 0.0, classified intrinsic (H4). The clearinghouse
with a parallel back-channel classifies partial — S stays in the core but Φ_MIP drops to 0.415, margin 1.585.
The free conduit classifies reducible — the dealer is not in the core to begin with. The margins order the
cases: contingent 2.0 ≥ partial 1.585 > intrinsic 0.0 ≈ reducible 0.0, with membership separating reducible
from intrinsic (H5).

## Discussion

The same mediator can be in the core for opposite reasons, and the bypass-counterfactual is what reads which.
The dealer and the clearinghouse both pass the verdict test — both triadic, both with the mediator in the core
— and the verdict cannot tell them apart. Restoring the forbidden edge does: it dissolves the dealer and
leaves the clearinghouse intact. A party held by its own integrating work survives the bypass because the
direct edge cannot reproduce the joint condition the mediator computes. A party held by a constraint does not,
because the constraint was the only thing in its way.

The category is the formal counterpart of an institution. A law, a license, a mandated intermediary, an
exclusive franchise — each makes a party indispensable not by giving it a role but by forbidding the route
around it. The contingency margin measures how much of a party's irreducibility the institution is carrying:
all of it for the car dealer, none for the clearinghouse, most of it for a mediator with a redundant
back-channel. This is a different lever from the ones the lab had catalogued. The design operations change
what the mediator computes; contingency changes what the parties are allowed to do. It refines the membership
law accordingly: a party can be pivotal not because it is influential on its own but because the alternative
to it is forbidden, and the bypass-counterfactual is how to tell de facto pivotality from de jure.

The reading matters for the dissertation's account of algorithmacy. A worker coordinating through a legally
mandated broker faces a triad that is irreducible by fiat, not by function, and the competence to see that the
third party is held in place by a constraint rather than by what it does — to know which edge is the law — is
part of what algorithmacy names. Contingent irreducibility gives that competence a formal object and a
measurable margin.

## Limitations

Four constructed forms at n=3 with exact Φ. The car dealer is a worked illustration of the franchise-law
structure, not a fitted model of an automobile market. The constraint enters as the buyer's update rule, the
modeling choice that turns a law into a wiring; a richer model would represent the law and the transaction
separately. The classifier reads one named party against one specified bypass, and the bypass a modeler
restores is theirs to justify; a party between more than one pair has more than one counterfactual. The margin
uses whole-system Φ_MIP. In-silico throughout; the result is a category of irreducibility and an instrument
for it, not a measurement of any organization.

## References

`essays/mediated_or_irreducible.md` (the constitutive-mediation law); q96 (contingent membership, the
state-contingent foil); q51–q62 (the back-channel mechanism); q106 (design operations); q98 (pivotality and
the membership law).

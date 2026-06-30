# Necessary and contingent irreducibility

<a synthesis of q213, q214, and the studies under org_frontier/studies/ — the instrument is in
classifier/contingency.py>

## Abstract

A third party can sit in a coordination's irreducible core for two reasons. It can do integrating work the two
other parties cannot reproduce by dealing with each other directly, or it can be a conduit that would drop out
the moment they dealt directly, held in place only because a constraint forbids the direct tie. The first is
necessary irreducibility, the second contingent. One operation separates them: restore the forbidden tie and
read whether the third party stays in the core. This paper draws together a program built on that operation —
the instrument, its recovery of a century of brokerage theory, its classification of fifty real and
theoretical intermediaries, its decomposition of platforms into earned integration and held gates, its
forecast of which intermediaries the internet removed, and the operations that move an intermediary between
the four cells. The claim is that a single counterfactual answers questions usually kept apart: what a
mediator is, whether it survives disintermediation, what an antitrust remedy takes away, and what makes a
market position durable.

## The question behind the program

Exact integrated information gives the lab a verdict on a three-party coordination. The verdict says whether
the form is triadic, with all three parties bound into one irreducible whole, or whether it factors into a
chain dyad with the mediator written out. The constitutive-mediation law sharpens the verdict into a causal
story: a mediator that commits on a joint condition of both parties is in the core, and a conduit that only
relays factors. That law reads the mediator's own rule and stops there.

A common kind of intermediary escapes it. A car dealer relays a car from a manufacturer to a buyer and
computes nothing. By the constitutive law it is a conduit and the triad should factor. It does not, because in
most of the United States franchise law forbids a manufacturer selling a car directly to the public. The
buyer must go through the dealer, so the dealer cannot be removed. The dealer is irreducible for a reason its
own rule does not contain: a constraint outside the mechanism forbids the parties from reaching each other.

## The instrument

q213 names the two reasons and builds the test that tells them apart. A party is intrinsically — necessarily —
irreducible if it stays in the core when the forbidden direct edge between its two neighbours is restored, and
contingently irreducible if it leaves. The contingency margin is the whole-system Φ_MIP lost when the bypass
opens. The classifier in `classifier/contingency.py` runs the counterfactual and returns one of four cells:
reducible, when the party is not in the core to begin with; contingent, when it is in the core and leaves
under the bypass, with the full Φ as its margin; intrinsic, when it stays and the margin is zero; partial,
when it stays but the system sheds integration. The car dealer reads contingent, its whole Φ riding on the
franchise law. A conjunctive clearinghouse reads intrinsic, because handing its two sides a direct line does
not let them recover the joint condition it computes.

The rest of the program is this one operation, applied widely.

## It recovers a century of brokerage theory

The distinction is not new. It has been drawn in words for a hundred years. Simmel named the *tertius gaudens*,
the third who profits from the division of the other two, against the mediator who reconciles them. Obstfeld
named the *tertius iungens*, the third who joins, against the gaudens of structural-hole theory, and with
colleagues posed conduit, gaudens, and iungens as three orientations a broker takes. Quintane and Carnabuci
made the contrast nearly mechanical: a gaudens broker intermediates the flow between the parties, a iungens
broker facilitates the direct exchange between them.

q214 runs nineteen of these theoretical types through the instrument. The verbal line is the formal line. Every
gaudens-family broker — gaudens, separans, *divide et impera*, the structural-hole broker, the Granovetter
bridge — reads contingent, with the full Φ as its margin: its place in the core is the maintained gap. Every
integrator — the Simmelian mediator, the two-sided platform that internalizes a cross-side externality — reads
necessary. The test draws a distinction the literature has only described.

It also refines the description. The *tertius iungens* does not have one class. A broker that integrates an
ongoing joint condition reads necessary. A broker that fully joins its two parties has created the direct tie,
which is the bypass, and reads reducible: it has written itself out of the core. The orientation the
literature most admires, carried to completion, is self-liquidating, and the verbal theory lacks the
instrument to say so. The instrument has a boundary as well. A Heider-balance sentiment triad reads as
integrated but symmetric, with no third party on a forbidden edge, so the counterfactual does not apply. The
taxonomy is for triads of mediated flow, and naming its edge is part of placing it.

## It sorts the economy

The irreducibility catalog applies the test to fifty-one arrangements, real and theoretical. The contingent
cell fills and then subdivides by what holds the bypass shut. Law and regulation hold the car dealer
(franchise law), the liquor distributor (the three-tier system), the notary, the customs broker, the bail
bondsman, the title insurer. Monopoly and exclusive control hold the app store behind its walled garden,
Ticketmaster behind its venue contracts, the multiple listing service behind its association rules. A network
standard holds SWIFT. A search friction holds the freight broker. The structural signature is identical across
all of them — a relay dissolving to a dyad when the bypass opens — and the kind of constraint is the variable
the catalog records.

The same domain can land in either column, decided by design. A title company that records a transfer is a
relay held by the recording requirement, and reads contingent. An escrow agent that releases only on the
buyer's payment and the seller's delivery integrates a joint condition, and reads necessary. Same position
between buyer and seller, opposite class, because one computes a joint condition and one passes the
transaction through.

## A platform is a portfolio

A real platform is not one triad, and the dual-function study reads this off the test. The classifier sorts an
(entity, function) pair, not the entity. Visa's authorization function is necessary, an approval that needs
the merchant's request and the issuer's response together. Visa's network-acceptance function is contingent, a
gate held by the rails both sides happen to share. Same company, two functions, two cells. Amazon spans all
four: fulfillment is necessary, marketplace matching is partial, the Buy Box is a contingent gate, and
first-party reselling is reducible the moment a brand can sell direct.

The decomposition is the antitrust question made computable. A platform's power is the sum of integrating work
it earns and a toll it holds, and the two carry opposite signatures: the integrating function survives the
bypass at margin zero, the gate dissolves under it at the full margin. A remedy that opens a gate —
sideloading, interoperability, breaking an exclusive — removes the contingent function and leaves the
necessary one in place. The test says which remedies hit rent and which would hit the service.

## It forecasts, and the forecast survives a blind audit

The class says whether a gate is held by a constraint. The constraint's durability says how soon it falls. The
constraint-durability study crosses the two: a contingent gate falls in inverse proportion to how hard its
constraint is to remove. Scored against what happened to twenty-six intermediaries between 1995 and 2025, the
forecast tracks the outcomes at r=0.925 with zero false positives. Every intermediary it called as holding did
hold — the car dealer, the liquor distributor, the notary. The reducible cases are the casualties the internet
removed once their friction was gone: the newspaper classified, the indie label's distribution, the retail
middleman.

A forecast scored by the author who knew the outcomes invites the obvious doubt. Three coders re-scored every
constraint's durability blind to the outcomes, the predictor, and the framework. They agreed at r=0.907, and
their consensus still predicts history at r=0.859. Independent readers recover the durability, so the forecast
rests on more than the author's hindsight. The blind pass also corrected one optimism: it surfaced a false
positive at ride-hail, whose matching gate the coders rated less durable than it has proven, which the
author's outcome-aware coding had smoothed over.

## The cells are a state machine

An intermediary's class is a state that operations move. The contingency-transitions study models six of them
as the edges between the four cells. Opening the bypass — deregulation, mandated interoperability, an antitrust
remedy — moves a contingent party to reducible. Erecting a constraint — a license, an exclusive, a walled
garden — moves a reducible conduit to contingent. Integrating moves a relay to necessary. Commoditizing moves
a necessary integrator to reducible once the direct tie can reproduce its work.

One invariant holds across the operations. Opening the bypass, the move a regulator or a competitor can force,
evicts a contingent party and takes nothing from a necessary one. Necessary is the only cell that opening the
bypass cannot empty. A position built by erecting a constraint is a rent a single policy move erases. A
position built by integration the bypass cannot reach. For a firm, the durable strategy is to integrate. For a
regulator, the lever is to open the bypass, which removes a rent without touching a service.

## What the program shows

One counterfactual runs through all of it. Restore the forbidden direct tie and read who is left in the core,
and the same operation answers a set of questions usually treated separately. It says what a brokerage role is
in Simmel's and Obstfeld's terms. It says which of fifty intermediaries are held by their work and which by a
rule. It separates a platform's earned integration from its held toll. It forecasts which intermediaries
disintermediation removes, since disintermediation is the world running the same counterfactual. It says what
an antitrust remedy takes away and what a market position's durability rests on. The questions share an answer
because they are the same question asked of different objects: is this third party here because of what it
does, or because of what is forbidden.

This is where the work meets the dissertation's construct. A worker coordinating through a legally mandated
broker faces a triad that is irreducible by fiat, and the competence to see that the third party is held by a
rule rather than by its function — to know which edge is the law — is part of what algorithmacy names.
Contingent irreducibility gives that competence a formal object and a measurable margin.

## Limitations

The program is in-silico throughout. Each arrangement is a stylized n=3 Boolean model classified by exact Φ, a
worked illustration of a structure rather than a fitted model of a market, and the modeling choice — which
joint condition a platform computes, which edge a law forbids — is stated per case and could be drawn
differently for a borderline type. The durability layer is a judgment, blind-validated for reliability but
still resting on a rubric. The historical outcomes are single-coded, and several are mid-transition. The
taxonomy is for mediated flow triads, and the Heider boundary marks where it stops. What the program
establishes is a category, an instrument, and a set of readings that the instrument makes from one operation,
not a measurement of any organization.

## References

q213 (contingent irreducibility, the instrument); q214 (triadic classification, the literature); the studies
under `org_frontier/studies/` — `irreducibility_catalog`, `dual_function_entities`, `constraint_durability`,
`contingency_transitions`; the essays `mediated_or_irreducible.md` and `what_survives_disintermediation.md`.
The brokerage and economics sources are in `org_frontier/questions/q214_triadic_classification/literature/`.

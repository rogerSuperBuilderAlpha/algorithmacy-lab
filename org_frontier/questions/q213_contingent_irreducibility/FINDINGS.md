# Q213 — findings

A new category of irreducibility and a reusable instrument to detect it. A mediator can sit in a triad's core
because it integrates (intrinsic) or because a constraint forbids the bypass around it (contingent). The
bypass-counterfactual classifier (`classifier/contingency.py`) tells them apart. n=3, exact IIT-4.0 Φ.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | conjunctive triad triadic, Φ_MIP = 2.000000 |
| H2 a conduit is irreducible under constraint | confirmed | constrained car dealer triadic Φ=2.0, core {M,D,B}, D in core |
| H3 bypass removes the contingent party | confirmed | dealer: kind=contingent, leaves core, dyadic, margin=2.0 |
| H4 same bypass leaves the intrinsic mediator | confirmed | clearinghouse: kind=intrinsic, S stays in core, margin=0.0 |
| H5 four-way taxonomy realized, margins ordered | confirmed | partial margin 1.585, reducible D not in core; 2.0 ≥ 1.585 > 0.0 |

## A conduit can be irreducible — when a constraint forbids the bypass

The lab's constitutive law says a conduit factors. A mediator that only relays, doing no integrating work,
drops out of the core and the triad collapses to a chain dyad. The car dealer is exactly such a conduit: it
relays a car from maker to buyer and computes nothing. By the relay rule alone the triad should factor.

It does not. With the buyer bound to source through the dealer — franchise law forbids the maker selling
direct — the three-party system reads triadic at Φ_MIP=2.0 with the dealer in the core (H2). The dealer is
irreducible. Its irreducibility is real: while the law stands, the dealer cannot be removed without breaking
the only path from maker to buyer. The irreducibility is also entirely a property of the constraint, not of
the dealer's role. That is the new category: contingent irreducibility.

## The bypass-counterfactual separates the two reasons a party is in the core

The instrument restores the forbidden edge and recomputes. Lift the franchise law — let the maker sell direct
— and the dealer is disintermediated: it leaves the core, the system collapses to the maker–buyer dyad, and
Φ_MIP falls from 2.0 to 0.0. The classifier labels the dealer "contingent" with a contingency margin of 2.0,
its entire integration (H3).

The same operation applied to an intrinsic mediator does nothing. The conjunctive clearinghouse, S=W∧C, sits
in the core because it computes a joint condition of its two neighbours. Hand one neighbour a direct line to
the other and the pair still cannot recover that joint condition: the mediator stays in the core, Φ_MIP holds
at 2.0, and the margin is 0.0. The classifier labels it "intrinsic" (H4). The same bypass that dissolves the
dealer leaves the clearinghouse untouched, which is what makes the test a discriminator and not just a
verdict.

## The category is a spectrum, with four cells

Two more forms fill out the taxonomy (H5). A clearinghouse with a parallel back-channel opened alongside it —
the integrating mediator plus a redundant direct edge — classifies "partial": the mediator keeps its place in
the core, but the system sheds most of its integration, Φ_MIP falling from 2.0 to 0.415, a margin of 1.585.
Part of its grip was its own work, part was the absence of the alternative. A free conduit, the same relay
dealer with no constraint and the buyer already sourcing direct, classifies "reducible": the dealer is not in
the core to begin with. The contingency margin orders the cases — contingent 2.0, partial 1.585, intrinsic
0.0, reducible 0.0 — and membership separates reducible (out of the core) from intrinsic (in it). The
category is not a binary; the margin measures how much of a party's irreducibility a constraint is carrying.

## What the category adds

Contingent irreducibility is a third route into the core, beside the two the lab already had. q106's design
operations write a party in by changing the mediator's function. q98's membership law admits a party that is
bidirectionally coupled and pivotal. Contingency writes a party in without touching its function or making it
pivotal on its own: it removes everyone's alternative to the party. The lever is the constraint, not the
mechanism. This is the formal counterpart of an institution — a law, a license, a required intermediary —
that makes a party indispensable de jure while it remains a conduit de facto. It also marks the matched
opposite of q96: there, contingency on system state resolved toward optionality and dissolved the triad; here,
contingency on a constraint resolves toward irreducibility and constitutes it.

## Caveats

Four constructed forms at n=3 with exact Φ. The car dealer is a worked illustration of the franchise-law
structure, not a fitted model of an automobile market; the constraint is represented as the buyer's update
rule (read the dealer vs. read the maker), which is the modeling choice that turns a law into a wiring. The
classifier reads a single named party against a single specified bypass; a party can sit between more than one
pair, and the bypass a modeler restores is theirs to justify. The margin uses whole-system Φ_MIP. In-silico;
evidence about a category of irreducibility, not a measurement of any organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q213_contingent_irreducibility.probe_contingent_irreducibility`

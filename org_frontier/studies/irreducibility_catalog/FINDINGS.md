# irreducibility_catalog — findings

51 entries classified by the bypass-counterfactual (q213): 38 real-world arrangements and 13
literature-grounded triad types (q214). Totals: necessary 13, contingent 25, partial 7, reducible 6. Every
entry classifies as cataloged. n=3 per form, exact Φ.

## The contingent class subdivides by what holds the bypass shut

The 25 contingent entries are not one thing. What keeps the parties from connecting directly varies, and the
catalog records it. **Law / regulation:** the car dealer (franchise law), liquor distributor (three-tier), bail
bondsman (cash bail), title insurer and appraiser (lender requirements), notary, prescription pharmacist,
customs broker, accreditation body. **Monopoly / exclusive control:** the app store (walled garden),
Ticketmaster (exclusive venue contracts), the MLS (association rules), the domain registrar (root authority).
**Network / standard lock-in:** SWIFT. **Search friction:** the freight broker, the friction-bound middleman.
**Collective bargaining:** the union hiring hall. The structural signature is identical — a relay dissolving to
a dyad on the bypass, margin = full Φ — and the *kind* of constraint is the real-world variable. The
contingency margin says how much; the family says what.

## The taxonomy predicts what survives disintermediation

The class is a prediction about an intermediary's fate when the internet lowers the cost of the direct tie.
A **reducible** intermediary has no constraint holding the bypass shut, so when the bypass opens it is removed:
newspaper classifieds (Craigslist), the indie record label (direct distribution), the retail middleman (DTC
brands) — all disintermediated. A **contingent** intermediary is held by a constraint the internet cannot
lower, so it survives: the car dealer kept its franchise law, the bail bondsman kept cash bail, the app store
kept its walled garden. A **necessary** intermediary integrates a joint condition the direct tie cannot
reproduce, so the bypass never threatened it: the clearinghouse, the exchange, air traffic control. The
**partial** cases are the contested middle — the PBM, the ride-hail platform, the GPO, the talent agent — doing
real integration beside a bypassable gate, and these are exactly the intermediaries under live disintermediation
pressure. Which intermediaries the internet killed and which it could not is read off the class: reducible dies,
contingent survives by its constraint, necessary survives by its work.

| reading | count | margin | what it means |
|---|---|---|---|
| contingent | 25 | 2.0 (full Φ) | a conduit held in the core only by a constraint; dissolves when the bypass opens |
| necessary | 13 | 0.0 | integrates a joint condition the direct tie cannot reproduce |
| partial | 7 | 1.585 | real integration beside a bypassable channel |
| reducible | 6 | 0.0 | already out of the core; no constraint and no integration |

## The literature batch (q214)

The brokerage canon's verbal line — the third who joins versus the third who profits by keeping the parties
apart — sorts under the bypass-counterfactual as necessary versus contingent. Every gaudens-family broker
(Simmel's *tertius gaudens*, Burt's structural-hole broker, the Granovetter bridge) reads contingent; every
integrator (the Simmelian mediator, the two-sided platform) reads necessary. The *tertius iungens* splits: the
broker that keeps integrating is necessary, the one that fully joins its parties writes itself out of the core
(reducible). See `org_frontier/questions/q214_triadic_classification/` for the full study and citations.

## Many constraints, one structure

The six contingent entries are six different legal regimes — a franchise statute, the three-tier alcohol law, a
customs license, a notarization rule, a dispensing law, a recording requirement — and they share a single
structural signature: a mandated relay, mediator in the core, dissolving to a dyad when the bypass opens, with
the full Φ as the contingency margin. The constraint type is where the variety lives; the structure is sparse.
The bypass-counterfactual reads all six the same, which is the catalog's first use: it sorts a mediator into
necessary or contingent without reference to its domain or the particular law that props it.

## The category is a property of design, not industry

The two real-estate entries land in opposite columns. A title company that records a transfer is a relay,
contingent on the recording requirement. An escrow agent that conditions release on both payment and delivery
integrates the joint state and is necessary. Same domain and same position between the parties, decided by
whether the mediator computes a joint condition or passes the transaction through. A mediator's column is not
read off its label; it is read off the bypass-counterfactual.

## The margin orders the catalog

Contingent entries carry the full margin (2.0): the constraint holds all of their irreducibility, and lifting
it removes all of it. Necessary entries carry margin 0: the bypass takes nothing. The partial entries sit
between at 1.585, a mediator whose grip is part its own and part the absence of an alternative. The reducible
entry is out of the core to begin with. The margin is a continuous reading of how much of a third party's
indispensability a constraint is carrying, and the first batch spans it.

## Caveats

Stylized n=3 Boolean models, one per arrangement, classified by exact Φ. The models are worked illustrations of
the structure each arrangement instantiates, not fitted models of the markets; the interpreter, court, and
clearinghouse are rendered as the same conjunctive form, which captures the shared "joint condition the bypass
cannot reproduce" and not their differences. The constraint enters as the sink's update rule. Diverse real
arrangements collapsing to four templates is a finding about the templates' coverage, and a real arrangement
that fits none is the cue to extend them. In-silico; a catalog of structures, not a measurement of any market.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/studies/irreducibility_catalog/build_catalog.py`

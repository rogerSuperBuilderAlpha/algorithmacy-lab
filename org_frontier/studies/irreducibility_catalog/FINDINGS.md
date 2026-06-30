# irreducibility_catalog — findings

Thirteen real coordination arrangements classified by the bypass-counterfactual (q213). First batch:
necessary 4, contingent 6, partial 2, reducible 1. Every entry classifies as cataloged. n=3 per form, exact Φ.

| reading | count | entries |
|---|---|---|
| contingent | 6 | car_dealer, liquor_distributor, customs_broker, notary, prescription_refill, title_passthrough |
| necessary (intrinsic) | 4 | clearinghouse_ccp, interpreter, court_adjudication, escrow_conditional |
| partial | 2 | travel_agent, insurance_broker |
| reducible | 1 | unexclusive_reseller |

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

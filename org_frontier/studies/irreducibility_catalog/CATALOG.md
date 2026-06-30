# The catalog

Thirteen mediating third parties, each modeled as a small Boolean form and sorted by the bypass-counterfactual.
The class is why the mediator is in the core: necessary if it integrates and survives the bypass, contingent if
a constraint is the only thing holding it there. Margin is the whole-system Φ_MIP lost when the bypass opens.

| entry | domain | parties (source · mediator · sink) | constraint | class | margin |
|---|---|---|---|---|---|
| car_dealer | auto retail | manufacturer · dealer · buyer | franchise law forbids direct sale | contingent | 2.000 |
| liquor_distributor | alcohol | producer · distributor · retailer | three-tier law forbids direct shipment | contingent | 2.000 |
| customs_broker | trade | exporter · customs broker · importer | clearance routed through a licensed broker | contingent | 2.000 |
| notary | legal instruments | signer · notary · counterparty | instrument valid only if notarized | contingent | 2.000 |
| prescription_refill | pharmacy | prescriber · pharmacist · patient | scheduled drug dispensed only via pharmacist | contingent | 2.000 |
| title_passthrough | real estate | seller · title company · buyer | transfer valid only through recording | contingent | 2.000 |
| clearinghouse_ccp | finance | buyer side · central counterparty · seller side | none — nets and guarantees both sides | necessary | 0.000 |
| interpreter | language | speaker A · interpreter · speaker B | none — the parties share no language | necessary | 0.000 |
| court_adjudication | law | plaintiff · court · defendant | none — ruling is a joint determination | necessary | 0.000 |
| escrow_conditional | real estate | buyer · escrow agent · seller | none — release on payment AND delivery | necessary | 0.000 |
| travel_agent | travel | traveler · travel agent · supplier | none — direct booking runs alongside | partial | 1.585 |
| insurance_broker | insurance | insured · broker · carrier | none — direct quoting runs alongside | partial | 1.585 |
| unexclusive_reseller | retail | manufacturer · reseller · customer | none — customer may already buy direct | reducible | 0.000 |

## Contingent — held by a constraint

Six arrangements, six different constraints, one structure. The dealer, the distributor, the customs broker,
the notary, the pharmacist on a routine refill, the recording title company — each relays and integrates
nothing, and each sits in the core only because a law forbids the parties reaching each other directly. Restore
the bypass and the mediator is disintermediated, the triad collapses to a dyad, and the margin is the entire
Φ. The constraint differs — a franchise statute, a three-tier law, a license, a recording rule — and the
structural signature does not. The bypass-counterfactual reads them all the same way: a conduit irreducible de
jure.

## Necessary — held by its own role

Four arrangements survive the bypass. The central counterparty novates both sides of a trade, a determination
neither side can reproduce by clearing bilaterally. The interpreter carries meaning between parties who share
no language, and a direct line between them carries nothing. The court issues a binding ruling that is not the
settlement the parties could reach alone. The conditional escrow releases only on the joint state of payment
and delivery. Hand any of these pairs a direct edge and the mediator stays in the core, the margin is zero:
the edge cannot reproduce the joint condition the mediator computes. These are necessary, not mandated — no law
holds them in.

## The same role, either column

The two real-estate entries are the catalog's hinge. A title company that only records a transfer is a relay,
held in by the recording requirement — contingent. An escrow agent that conditions release on both the buyer's
payment and the seller's delivery integrates the joint state — necessary. Same domain, same position between
buyer and seller, opposite class, decided by whether the mediator computes a joint condition or just passes
the transaction through. The category is a property of the design, not the industry.

## Partial and reducible

The travel agent and the insurance broker integrate complex cases but run beside a direct channel that took the
simple ones. They keep a foothold in the core and shed most of the system's integration — partial, margin
1.585. The unexclusive reseller has no exclusivity and no integrating role; the customer can already buy
direct, so it is out of the core to begin with — reducible.

## The literature canon (q214)

The second batch is theoretical rather than empirical: the canonical triad types of the brokerage, sociology,
and economics literature, modeled and classified the same way. The full study, with citations, is
`org_frontier/questions/q214_triadic_classification/`.

| type | theory | class | margin |
|---|---|---|---|
| tertius_gaudens | Simmel 1908 | contingent | 2.000 |
| structural_hole_broker | Burt 1992 | contingent | 2.000 |
| granovetter_bridge | Granovetter 1973 | contingent | 2.000 |
| gf_gatekeeper / gf_liaison | Gould & Fernandez 1989 | contingent | 2.000 |
| gatekeeping_platform | Hagiu 2009 | contingent | 2.000 |
| arbitrageur_friction | Rubinstein & Wolinsky 1987 | contingent | 2.000 |
| tertius_iungens_integrating | Obstfeld 2005 | necessary | 0.000 |
| simmelian_mediator | Simmel 1908 | necessary | 0.000 |
| two_sided_platform | Rochet & Tirole 2003 | necessary | 0.000 |
| market_maker | Rubinstein & Wolinsky 1987 | partial | 1.585 |
| tertius_iungens_selfliquidating | Obstfeld 2005 | reducible | 0.000 |
| gf_coordinator | Gould & Fernandez 1989 | reducible | 0.000 |

The verbal *gaudens* / *iungens* line is the formal contingent / necessary line. The one refinement the formal
test adds: a *tertius iungens* that fully joins its two parties creates the direct tie — the bypass — and writes
itself out of the core, landing reducible. The broker who most completely embodies the joining orientation makes
itself dispensable.

## Real-world expansion: the contingent class by constraint family

The 25 contingent entries split by *what holds the bypass shut*. The structure is identical (relay, margin 2.0);
the constraint family is the variable.

| family | entries |
|---|---|
| law / regulation | car_dealer, liquor_distributor, customs_broker, notary, prescription_refill, title_passthrough, bail_bondsman, title_insurer, real_estate_appraiser, immigration_attorney, accreditation_body |
| monopoly / exclusive | app_store_30pct, ticketmaster, mls_realty, domain_registrar |
| network / standard | swift_messaging |
| search friction | freight_broker, arbitrageur_friction |
| collective bargaining | union_hiring_hall |
| brokerage strategy (q214) | tertius_gaudens, structural_hole_broker, granovetter_bridge, gf_gatekeeper, gf_liaison, gatekeeping_platform |

## The disintermediation prediction

The class is a forecast of an intermediary's fate when the internet lowers the cost of the direct tie.

| class | fate | examples |
|---|---|---|
| reducible | disintermediated — the friction it stood on is gone | newspaper_classifieds, indie_record_label, retail_middleman_dtc |
| contingent | survives by its constraint, not its work | car_dealer, bail_bondsman, app_store_30pct, ticketmaster |
| necessary | never threatened — integrates a joint condition | clearinghouse_ccp, stock_exchange, air_traffic_control, payment_network_auth |
| partial | the contested middle, under live pressure | pharmacy_benefit_manager, ride_hail_platform, gpo_healthcare, talent_agent |

See `essays/what_survives_disintermediation.md` for the argument: disintermediation removes the *friction* a
middleman stood on, and removes the middleman only when the friction was all that held it up.

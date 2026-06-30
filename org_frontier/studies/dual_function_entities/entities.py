"""Dual-function entities — one company, several roles, several cells of the taxonomy.

A single real-world platform is not one triad. It plays several roles at once, and the bypass-counterfactual
(classifier/contingency.py) classifies an (entity, function) pair, not the entity. Visa integrates
authorization (necessary) and gates the network (contingent). Amazon spans all four cells. The decomposition
separates the integrating work a platform earns from the gate it merely holds — the distinction antitrust
draws verbally.

Each function maps to one of the four catalog templates by its causal structure:
  conjunctive -> necessary  : integrates a joint condition of the two parties the direct tie cannot reproduce
  additive    -> partial    : integrates, but a bypassable channel runs alongside
  relay       -> contingent : a gate/toll held shut by a constraint (walled garden, network lock-in, exclusivity)
  free        -> reducible  : a conduit with no constraint; the bypass is already open
"""


def _relay():
    return ("A", "M", "C"), [lambda x: x[2], lambda x: x[0], lambda x: x[1]], "M", "C", "A", "replace"


def _conjunctive():
    return ("A", "M", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "C", "A", "replace"


def _additive():
    return ("A", "M", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "C", "A", "add"


def _free():
    return ("A", "M", "C"), [lambda x: x[2], lambda x: x[0], lambda x: x[0]], "M", "C", "A", "replace"


TEMPLATES = {"relay": _relay, "conjunctive": _conjunctive, "additive": _additive, "free": _free}


# entity -> list of functions; each function: (name, parties, what, template, expected)
ENTITIES = [
    ("Visa", [
        ("authorization", "merchant - issuer",
         "approves a payment only on the merchant request AND the issuer's approval", "conjunctive", "intrinsic"),
        ("network_acceptance_gate", "merchant - cardholder bank",
         "acceptance runs only over the network's rails; no shared alternative", "relay", "contingent"),
    ]),
    ("Amazon", [
        ("fulfillment_fba", "seller - buyer",
         "warehousing and same-day delivery neither party reproduces", "conjunctive", "intrinsic"),
        ("marketplace_matching", "buyer - seller",
         "matches demand to supply, with direct purchase available for known brands", "additive", "partial"),
        ("buybox_gate", "seller - buyer",
         "picks which seller the buyer sees; sellers pay to pass", "relay", "contingent"),
        ("first_party_reseller", "brand - customer",
         "buys and resells; a brand that can go direct-to-consumer routes around it", "free", "reducible"),
    ]),
    ("Apple_App_Store", [
        ("developer_distribution", "developer - user",
         "review, signing, and delivery, with the mobile web as a thin bypass", "additive", "partial"),
        ("in_app_payment_gate", "developer - user",
         "in-app purchases must use Apple's billing; no direct charge allowed", "relay", "contingent"),
    ]),
    ("Google", [
        ("organic_matching", "searcher - page",
         "ranks the whole corpus to a query, a relevance no pair reproduces", "conjunctive", "intrinsic"),
        ("ad_auction_gate", "advertiser - searcher",
         "pay to appear above the organic results; a toll on attention", "relay", "contingent"),
    ]),
    ("Uber", [
        ("realtime_matching", "rider - driver",
         "matches the nearest driver to a rider in real time", "conjunctive", "intrinsic"),
        ("rider_driver_gate", "rider - driver",
         "stands between a pair who could otherwise re-contact directly", "relay", "contingent"),
    ]),
    ("Ticketmaster", [
        ("distribution_antifraud", "venue - fan",
         "queueing, verified resale, fraud control, with direct sale possible", "additive", "partial"),
        ("exclusive_venue_gate", "venue - fan",
         "exclusive venue contracts forbid selling tickets any other way", "relay", "contingent"),
    ]),
    ("GDS_Sabre", [
        ("inventory_aggregation", "airline - travel agent",
         "aggregates every airline's seats into one searchable inventory", "conjunctive", "intrinsic"),
        ("booking_gate", "airline - travel agent",
         "airlines are locked into the GDS standard to reach agents", "relay", "contingent"),
    ]),
]

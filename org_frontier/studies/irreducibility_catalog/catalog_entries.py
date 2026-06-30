"""Catalog of necessary and contingent irreducible triads — the entries.

Each entry is a real coordination arrangement with a mediating third party, modeled as a small Boolean form
and classified by the bypass-counterfactual (classifier/contingency.py). The dichotomy:

  necessary  (the classifier's "intrinsic")  — the mediator integrates; it survives the bypass.
  contingent                                 — a conduit held in the core only by a constraint; it dissolves
                                               when the forbidden bypass is restored.
  partial                                    — part role, part constraint; stays, but the system sheds integration.
  reducible                                  — a free conduit, already out of the core.

Diverse arrangements share a few structural templates. The catalog's point is that the constraint TYPE varies
widely (franchise law, a credential, a monopoly, a protocol) while the structural signature is sparse, and the
bypass-counterfactual is what sorts a mediator into necessary or contingent regardless of its domain.

The `expected` field on each entry is the prediction, fixed before `build_catalog.py` classifies it.
"""


# ---- structural templates: name -> (labels, rules, party, downstream, upstream, mode) ----
def _relay():
    # mandated relay: source S -> mediator M -> sink K, sink bound to source through M; bypass disintermediates
    return ("S", "M", "K"), [lambda x: x[2], lambda x: x[0], lambda x: x[1]], "M", "K", "S", "replace"


def _conjunctive():
    # integrating mediator: M commits on a joint condition of A and B; bypass gives B a direct line to A
    return ("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "B", "A", "replace"


def _additive():
    # integrating mediator with a parallel back-channel opened alongside it
    return ("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "B", "A", "add"


def _free():
    # a relay with no constraint: the sink already sources directly, the mediator is a dead-end copy
    return ("S", "M", "K"), [lambda x: x[2], lambda x: x[0], lambda x: x[0]], "M", "K", "S", "replace"


TEMPLATES = {"relay": _relay, "conjunctive": _conjunctive, "additive": _additive, "free": _free}


# ---- the catalog ----
ENTRIES = [
    # ----- contingent: mandated / blocked conduits (a relay held in the core by a constraint) -----
    dict(name="car_dealer", domain="auto retail", constraint_type="franchise law",
         source="manufacturer", mediator="dealer", sink="buyer",
         constraint="state franchise laws forbid a manufacturer selling new cars direct",
         bypass="the manufacturer sells direct to the buyer",
         template="relay", expected="contingent",
         reading="a pure relay; irreducible only while the franchise law stands"),
    dict(name="liquor_distributor", domain="alcohol", constraint_type="three-tier law",
         source="producer", mediator="distributor", sink="retailer",
         constraint="post-Prohibition three-tier laws forbid a producer selling direct to a retailer",
         bypass="the producer ships direct to the retailer",
         template="relay", expected="contingent",
         reading="the distributor integrates nothing; the tier law is the whole of its irreducibility"),
    dict(name="customs_broker", domain="trade", constraint_type="licensing mandate",
         source="exporter", mediator="customs broker", sink="importer",
         constraint="clearance is routed through a licensed broker the importer must engage",
         bypass="the importer clears the goods directly",
         template="relay", expected="contingent",
         reading="a paperwork relay made indispensable by the licensing requirement"),
    dict(name="notary", domain="legal instruments", constraint_type="statutory witnessing",
         source="signer", mediator="notary", sink="counterparty",
         constraint="the instrument is valid only if a notary witnesses and seals it",
         bypass="the parties execute the instrument between themselves",
         template="relay", expected="contingent",
         reading="the notary adds a seal, not a determination; validity law forbids the bypass"),
    dict(name="prescription_refill", domain="pharmacy", constraint_type="dispensing law",
         source="prescriber", mediator="pharmacist", sink="patient",
         constraint="a scheduled drug may be dispensed only through a licensed pharmacist",
         bypass="the patient obtains a routine refill directly",
         template="relay", expected="contingent",
         reading="a routine refill the system could automate; the dispensing law holds the pharmacist in"),
    dict(name="title_passthrough", domain="real estate", constraint_type="recording requirement",
         source="seller", mediator="title company", sink="buyer",
         constraint="transfer is valid only when routed through the recording intermediary",
         bypass="the seller conveys title to the buyer directly",
         template="relay", expected="contingent",
         reading="a recording relay; contrast escrow_conditional, the same domain done as an integrator"),

    # ----- necessary (intrinsic): integrators that survive the bypass -----
    dict(name="clearinghouse_ccp", domain="finance", constraint_type="none (integrates)",
         source="buyer side", mediator="central counterparty", sink="seller side",
         constraint="none — the CCP nets and guarantees both sides' obligations jointly",
         bypass="the two sides clear bilaterally",
         template="conjunctive", expected="intrinsic",
         reading="novation is a joint determination a direct edge cannot reproduce; necessary"),
    dict(name="interpreter", domain="language", constraint_type="none (integrates)",
         source="speaker A", mediator="interpreter", sink="speaker B",
         constraint="none — the parties share no language",
         bypass="the two speakers address each other directly",
         template="conjunctive", expected="intrinsic",
         reading="a direct edge carries no shared meaning; the interpreter is necessary, not mandated"),
    dict(name="court_adjudication", domain="law", constraint_type="none (integrates)",
         source="plaintiff", mediator="court", sink="defendant",
         constraint="none — the binding ruling is a joint determination of both claims",
         bypass="the parties settle between themselves",
         template="conjunctive", expected="intrinsic",
         reading="settlement is a different object; only the court issues the binding joint determination"),
    dict(name="escrow_conditional", domain="real estate", constraint_type="none (integrates)",
         source="buyer", mediator="escrow agent", sink="seller",
         constraint="none — release is conditioned on buyer payment AND seller delivery",
         bypass="buyer and seller exchange directly",
         template="conjunctive", expected="intrinsic",
         reading="conditioning on the joint state makes escrow necessary; contrast title_passthrough"),

    # ----- partial: an integrator with a parallel channel opened alongside -----
    dict(name="travel_agent", domain="travel", constraint_type="none (eroding)",
         source="traveler", mediator="travel agent", sink="supplier",
         constraint="none — direct online booking runs alongside the agent",
         bypass="the traveler books simple trips online directly",
         template="additive", expected="partial",
         reading="keeps a foothold for complex itineraries, sheds the simple ones to the back-channel"),
    dict(name="insurance_broker", domain="insurance", constraint_type="none (eroding)",
         source="insured", mediator="broker", sink="carrier",
         constraint="none — direct-to-carrier quoting runs alongside the broker",
         bypass="the insured buys a standard policy direct",
         template="additive", expected="partial",
         reading="retains complex/commercial placement, loses commodity lines to the direct channel"),

    # ----- reducible: a free conduit, no constraint -----
    dict(name="unexclusive_reseller", domain="retail", constraint_type="none",
         source="manufacturer", mediator="reseller", sink="customer",
         constraint="none — the customer may already buy direct",
         bypass="the customer buys from the manufacturer directly",
         template="free", expected="reducible",
         reading="no exclusivity and no integration; the reseller is already out of the core"),
]

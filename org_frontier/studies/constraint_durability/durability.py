"""Constraint durability — how soon does a contingent gate fall?

The bypass-counterfactual (q213) says whether an intermediary is held in the core by a constraint (contingent)
and how much (margin = full Φ). It does not say how durable that constraint is. Durability is an orthogonal,
empirical axis: a friction the internet erodes is fragile, an entrenched law with a lobby is durable. Crossing
the formal class with a durability score gives a forecast — which contingent gates fall next — and the forecast
is backtested against what actually happened to these intermediaries between 1995 and 2025.

Durability rubric (0-3), a stated judgment, not a Φ result:
  0  a pure search/information friction the internet removes outright
  1  a monopoly, exclusive contract, or network lock-in under active contestation or a clear tech threat
  2  a law, credential, or standard with some reform pressure or slow erosion
  3  an entrenched law with an organized lobby, no near-term reform, no tech bypass

Observed outcome by 2026 (the backtest target): fell, falling, pressured, holding, or na (necessary; never
threatened by the direct tie).

Each row references the catalog/dual-function class. The durability and observed fields are hand-coded; the
backtest in analyze_durability.py is the validation, not the coding's inter-rater agreement (a blind
multi-coder durability pass is the next rigor step).
"""

OBS_SCORE = {"fell": 4, "falling": 3, "pressured": 2, "holding": 1, "na": 0}

# (name, class, constraint_family, durability 0-3, observed outcome by 2026)
ROWS = [
    ("car_dealer", "contingent", "law", 3, "holding"),
    ("liquor_distributor", "contingent", "law", 3, "holding"),
    ("notary", "contingent", "law", 2, "holding"),
    ("customs_broker", "contingent", "law", 2, "holding"),
    ("prescription_refill", "contingent", "law", 2, "holding"),
    ("title_insurer", "contingent", "law", 2, "pressured"),
    ("bail_bondsman", "contingent", "law", 1, "falling"),
    ("accreditation_body", "contingent", "law", 2, "pressured"),
    ("app_store_30pct", "contingent", "monopoly", 1, "falling"),
    ("ticketmaster", "contingent", "monopoly", 1, "falling"),
    ("mls_realty", "contingent", "monopoly", 1, "falling"),
    ("domain_registrar", "contingent", "monopoly", 2, "holding"),
    ("swift_messaging", "contingent", "network", 2, "pressured"),
    ("freight_broker", "contingent", "friction", 0, "falling"),
    ("union_hiring_hall", "contingent", "collective-bargaining", 2, "pressured"),
    ("pharmacy_benefit_manager", "partial", "gate", 1, "falling"),
    ("ride_hail_platform", "partial", "gate", 2, "holding"),
    ("talent_agent", "partial", "gate", 1, "pressured"),
    ("travel_agent", "partial", "friction", 0, "fell"),
    ("stockbroker_commission", "contingent", "regulation", 0, "fell"),
    ("newspaper_classifieds", "reducible", "none", 0, "fell"),
    ("indie_record_label", "reducible", "none", 0, "fell"),
    ("retail_middleman_dtc", "reducible", "none", 0, "fell"),
    ("clearinghouse_ccp", "necessary", "none", 3, "na"),
    ("stock_exchange", "necessary", "none", 3, "na"),
    ("interpreter", "necessary", "none", 3, "na"),
]


def predicted_risk(klass, durability):
    """Predicted fall-risk 0-4: reducible already fell (4); necessary never falls (0); a held gate falls in
    inverse proportion to its constraint's durability (3 - durability)."""
    if klass == "reducible":
        return 4
    if klass == "necessary":
        return 0
    return 3 - durability

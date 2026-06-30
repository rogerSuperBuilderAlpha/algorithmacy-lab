"""Blind inter-coder durability scores.

Three coders rated the durability of each constraint (0-3, the rubric in durability.py) BLIND to the
historical outcomes, to the fall-risk predictor, and to the contingent/necessary framework. They saw only the
intermediary and a neutral description of the constraint holding it in place, and were asked how hard that
constraint would be to remove or route around. This tests whether the durability signal that drives the
forecast is recoverable independently, or an artifact of one outcome-aware coder.

The scores cover the 20 contingent/partial intermediaries (the ones with a constraint to score). The
median-of-three is the consensus durability; analyze_intercoder.py computes inter-coder reliability and
re-runs the backtest with the consensus scores.
"""

CODERS = {
    "coder_1": {"car_dealer": 3, "liquor_distributor": 3, "notary": 2, "customs_broker": 2,
                "prescription_refill": 3, "title_insurer": 2, "bail_bondsman": 2, "accreditation_body": 3,
                "app_store_30pct": 1, "ticketmaster": 1, "mls_realty": 1, "domain_registrar": 2,
                "swift_messaging": 1, "freight_broker": 0, "union_hiring_hall": 1,
                "pharmacy_benefit_manager": 1, "ride_hail_platform": 1, "talent_agent": 1,
                "travel_agent": 0, "stockbroker_commission": 0},
    "coder_2": {"car_dealer": 3, "liquor_distributor": 3, "notary": 2, "customs_broker": 2,
                "prescription_refill": 3, "title_insurer": 2, "bail_bondsman": 2, "accreditation_body": 2,
                "app_store_30pct": 1, "ticketmaster": 1, "mls_realty": 1, "domain_registrar": 2,
                "swift_messaging": 1, "freight_broker": 0, "union_hiring_hall": 1,
                "pharmacy_benefit_manager": 1, "ride_hail_platform": 1, "talent_agent": 1,
                "travel_agent": 0, "stockbroker_commission": 0},
    "coder_3": {"car_dealer": 2, "liquor_distributor": 2, "notary": 2, "customs_broker": 3,
                "prescription_refill": 3, "title_insurer": 2, "bail_bondsman": 2, "accreditation_body": 3,
                "app_store_30pct": 1, "ticketmaster": 1, "mls_realty": 1, "domain_registrar": 2,
                "swift_messaging": 1, "freight_broker": 0, "union_hiring_hall": 2,
                "pharmacy_benefit_manager": 1, "ride_hail_platform": 1, "talent_agent": 1,
                "travel_agent": 0, "stockbroker_commission": 0},
}
RELIABILITY_FLOOR = 0.60

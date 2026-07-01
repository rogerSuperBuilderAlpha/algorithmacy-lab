"""Out-of-sample holdout for the durability forecast.

The main backtest scored the same intermediaries used to shape the rubric — a consistency check, not a
prediction. This holds out twelve intermediaries the rubric never saw, has three coders score their
constraint durability BLIND to the outcomes, applies the fixed predictor (predicted_risk = 3 - durability for
a held gate), and scores it against what actually happened. The predictor is not refit; the durability comes
from coders who never saw the answer.

class and observed outcome are assigned by the author (the coders saw only the intermediary and its
constraint). The nine contingent/partial items carry the blind durability scores; the three reducible items
(a friction the internet removed) need none — their predicted risk is fixed at 4.
"""

# blind coder durability scores for the nine contingent/partial holdout items
CODERS = {
    "coder_1": {"taxi_medallion": 1, "money_transfer_legacy": 1, "stock_transfer_agent": 2, "buyer_realtor": 2,
                "mortgage_broker": 1, "literary_agent": 0, "correspondent_bank": 1, "pawnbroker": 2,
                "travel_insurance_broker": 0},
    "coder_2": {"taxi_medallion": 1, "money_transfer_legacy": 2, "stock_transfer_agent": 3, "buyer_realtor": 1,
                "mortgage_broker": 0, "literary_agent": 0, "correspondent_bank": 1, "pawnbroker": 2,
                "travel_insurance_broker": 0},
    "coder_3": {"taxi_medallion": 1, "money_transfer_legacy": 2, "stock_transfer_agent": 3, "buyer_realtor": 2,
                "mortgage_broker": 1, "literary_agent": 1, "correspondent_bank": 2, "pawnbroker": 2,
                "travel_insurance_broker": 0},
}

# class (assigned structurally) and observed outcome by 2026 (the held-out target; coders never saw it)
CLASS = {
    "taxi_medallion": "contingent", "money_transfer_legacy": "contingent", "stock_transfer_agent": "contingent",
    "buyer_realtor": "contingent", "mortgage_broker": "partial", "literary_agent": "partial",
    "correspondent_bank": "contingent", "pawnbroker": "contingent", "travel_insurance_broker": "partial",
    "yellow_pages": "reducible", "video_rental_store": "reducible", "record_store": "reducible",
}
OBSERVED = {
    "taxi_medallion": "fell", "money_transfer_legacy": "pressured", "stock_transfer_agent": "holding",
    "buyer_realtor": "falling", "mortgage_broker": "pressured", "literary_agent": "pressured",
    "correspondent_bank": "pressured", "pawnbroker": "holding", "travel_insurance_broker": "falling",
    "yellow_pages": "fell", "video_rental_store": "fell", "record_store": "fell",
}

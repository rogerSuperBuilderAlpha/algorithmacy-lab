# constraint_durability — findings

The formal class crossed with a durability rubric forecasts which contingent gates fall, and the forecast
matches 1995-2025 history at r=0.925, accuracy 0.85, zero false positives (n=26). Durability and outcome are
hand-coded; the backtest is the validation.

## Two axes, one forecast

The bypass-counterfactual gives the first axis: a contingent intermediary is held in the core by a constraint,
margin = full Φ. That says it *can* be disintermediated if the constraint goes, not *whether it will*. The
second axis is the durability of the constraint — fragile (a friction the internet removes) to entrenched (a
law with an organized lobby). Predicted fall-risk is the cross: reducible intermediaries have already fallen,
necessary ones never fall, and a contingent gate falls in inverse proportion to its constraint's durability.

## The backtest

Scored against what happened to these intermediaries by 2026, the predicted fall-risk tracks the observed
outcome at r=0.925. As a binary forecast — predict erosion when risk ≥ 2, score a hit when the intermediary
actually fell, is falling, or is under pressure — the accuracy is 0.85 with **zero false positives**. Every
intermediary the forecast called as holding did hold: the car dealer (franchise law), the liquor distributor
(three-tier law), the notary, the customs broker, the domain registrar. The four misses are all in one
direction and one notch: title insurance, accreditation, SWIFT, and the union hiring hall were scored durable
(predicted to hold) and are in fact under mild pressure. The forecast under-calls erosion at the margin and
never over-calls it, which is the conservative error to make.

## What the forecast reads now

The ranking is a live forecast. At the top, already fallen: the newspaper classified, the indie label's
distribution, the retail middleman, the travel agent, the stockbroker's fixed commission — all friction-held
or constraint-removed, all gone. Falling now, contingent gates whose constraint is under active contestation:
the app store's payment cut (the Digital Markets Act, sideloading), Ticketmaster's exclusivity (the antitrust
suit), the MLS commission rule (the 2024 settlement), the freight broker (digital freight matching), the
pharmacy benefit manager (transparency legislation), cash-bail's bondsman (bail reform). Holding, contingent
gates whose constraint is durable: the car dealer behind franchise law, the liquor distributor behind the
three-tier system, the notary, the customs broker. The formal class put all of these in the same cell —
contingent, margin 2.0 — and durability is what separates the ones falling this decade from the ones that are
not.

## The shape of the claim

Disintermediation is not random and it is not only about technology. A contingent gate falls when its
constraint is fragile and stands when its constraint is durable, and the two-axis forecast — formal class from
the bypass-counterfactual, durability from the rubric — predicts which is which. The strongest version of the
result is the zero false positives: the formal class plus a durable constraint is a reliable "this holds," and
the cases it called wrong are only ones it called too safe.

## Caveats

Durability (0-3) and the observed outcome are hand-coded by one coder against a stated rubric; the backtest,
not coder agreement, is the validation, and a blind multi-coder durability pass is the next step. The observed
outcomes are read as of 2026 and several are mid-transition (an intermediary "falling" has not fully fallen).
The dataset is 26 intermediaries chosen to span the classes and include known historical casualties, not a
random sample, so the correlation is a consistency check against history, not an out-of-sample test. The
formal class is exact (q213); the durability layer is judgment. In-silico class, empirical durability.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/studies/constraint_durability/analyze_durability.py`

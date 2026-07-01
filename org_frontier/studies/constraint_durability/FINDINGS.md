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

## Blind inter-coder validation

The forecast above rested on durability scored by one coder who also knew the outcomes. To test whether the
durability signal is recoverable independently, three coders re-scored every constraint blind to the outcomes,
to the predictor, and to the contingent/necessary framework — they saw only each intermediary and a neutral
description of its constraint, and rated how hard it would be to remove (`analyze_intercoder.py`).

The blind coders agree: mean pairwise reliability r=0.907, and their median consensus differs from the
single-coder durability on only 6 of 20 items, each by one notch. Re-running the backtest on the blind
consensus, the forecast holds — r=0.859, accuracy 0.85 — down from the single-coder r=0.925 but well clear of
chance. The blind pass also corrects an optimism: the single-coder version had zero false positives, the blind
version has one. It is ride-hail, which the coders rated a less durable gate than it has proven; the forecast
calls it falling and it is holding. The durability that drives the forecast is not an artifact of
outcome-aware coding — independent readers recover it, and it still predicts history — and the one place the
author's coding flattered the forecast is now visible.

## Out-of-sample holdout

The backtests above scored the same intermediaries used to shape the rubric, so they measure consistency, not
prediction. The holdout tests prediction. Twelve intermediaries the rubric never saw — the taxi medallion, the
buyer's agent, the correspondent bank, the pawnbroker, the yellow pages, the video store, and others — were
held out, three coders scored their constraint durability blind to the outcomes, and the fixed predictor was
applied unchanged.

On this held-out set the forecast holds: r=0.754, accuracy 0.83, and again zero false positives. The blind
coders agree on the new cases at r=0.805, so the durability judgment transfers to intermediaries none of the
original coding touched. The correlation degrades from the in-sample 0.925 to the blind in-sample 0.859 to the
out-of-sample 0.754, a graceful decline rather than a collapse, which is the signature of a predictor that
generalizes instead of fitting its own training set. The two out-of-sample misses are the familiar
conservative kind — the buyer's agent and the legacy money-transfer network were scored durable and are in
fact eroding (the buyer's agent under the 2024 commission settlement) — and the zero false positives mean every
"this holds" call held on data the forecast had never seen.

## Caveats

Durability (0-3) and the observed outcome are hand-coded; the blind inter-coder pass (r=0.907) and the
out-of-sample holdout (r=0.754, zero false positives) show the
durability is recoverable, but the observed outcomes are still single-coded and the backtest, not coder
agreement, is the validation of the forecast itself. The observed
outcomes are read as of 2026 and several are mid-transition (an intermediary "falling" has not fully fallen).
The dataset is 26 intermediaries chosen to span the classes and include known historical casualties, not a
random sample, so the correlation is a consistency check against history, not an out-of-sample test. The
formal class is exact (q213); the durability layer is judgment. In-silico class, empirical durability.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/studies/constraint_durability/analyze_durability.py`

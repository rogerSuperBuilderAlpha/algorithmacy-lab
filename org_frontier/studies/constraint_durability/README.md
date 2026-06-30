# Constraint durability — which contingent gates fall next

The bypass-counterfactual (q213) says whether an intermediary is held in the core by a constraint (contingent)
and how much (margin = full Φ). It does not say how durable the constraint is. Durability is an orthogonal,
empirical axis: a search friction the internet erodes is fragile, an entrenched law with a lobby is durable.

This study crosses the formal class with a durability rubric to forecast which contingent gates fall next, and
**backtests the forecast against what actually happened to these intermediaries between 1995 and 2025**. The
forecast predicts the observed outcomes at r=0.925 with zero false positives.

## Files
- `durability.py` — the rubric (0-3), the per-entry durability and observed-outcome coding, the predictor.
- `analyze_durability.py` — ranks by predicted fall-risk and runs the backtest.
- `FINDINGS.md` — the forecast, the backtest, and the live read on which gates fall next.

## Run
```
python org_frontier/studies/constraint_durability/analyze_durability.py
```

Durability and outcome are hand-coded judgments, not Φ results; the backtest is the validation. A blind
multi-coder durability pass is the next rigor step.

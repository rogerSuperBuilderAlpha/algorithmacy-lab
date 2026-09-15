# Margin cascade — lab-default selective exact Φ

When screening a large cheap-feature panel, the lab default is:

1. Fit a Probe-131-style random forest; take **out-of-fold** `P(triadic)`.
2. Call **exact IIT-4.0 Φ** on the **top B=10%** of forms with smallest `|p−0.5|`
   (recomputed per panel).
3. Keep the cheap prediction elsewhere.

Do **not** freeze a τ threshold across panel sizes. On-panel
`τ*(n=4 unc, B=10%) = 0.2876` is for prose only
(`studies/margin_cascade_tau/`). Fragility gating is not the default.

Warrant: `studies/margin_cascade_phi/` (WIN), `studies/margin_cascade_tau/`
(calibration). Size series / F28 / FN-redesign are cited there, not reopened here.

## Run on an existing panel

```bash
python -m org_frontier.cascade.run \
  --panel org_frontier/studies/holistic_residual_n4_unconstrained/results/residual_panel_n4_unconstrained.csv

# smoke control (n4 unc @ B=10% → miss 32, FN 11, exact 100)
python -m org_frontier.cascade.run \
  --panel org_frontier/studies/holistic_residual_n4_unconstrained/results/residual_panel_n4_unconstrained.csv \
  --smoke
```

## Enable on a new panel

1. Build a CSV with the Probe-131 feature columns and an exact `triadic` (or
   binary Φ>0) label from `classify_rules` / your exact-Φ path.
2. `from org_frontier.cascade import margin_cascade` then
   `margin_cascade(X, y, B=0.10)`, **or**
   `python -m org_frontier.cascade.run --panel your.csv`.
3. Report **always-cheap** and **cascade@10%** residuals, plus exact-call count.

## API sketch

```python
from org_frontier.cascade import margin_cascade, DEFAULT_B

result = margin_cascade(X, y)          # B=0.10 default
print(result.call_mask.sum())          # exact calls
print(result.fn_among_tri, result.miss_rate)
```

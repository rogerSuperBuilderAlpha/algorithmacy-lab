# Q82 — Stage 4 methods (fixed before computation)

Ground truth is the exact IIT-4.0 verdict on each n=3 outreach form (the 256-form family of Q81). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Proxies (`probe_surrogate_vs_proxy.py`)

For every form, four single proxies are computed:
- **mediator in-degree** — the number of inputs to the mediator node, from `cm_from_rules`.
- **total edges** — the sum of the connectivity matrix.
- **Φ_R** — ΦID redundancy (CCS) estimated from a noisy trajectory, via `proxy_bridge.bridge`.
- **Φ_WMS** — uncorrected whole-minus-sum Φ from the same trajectory, the proxy that tracked best in
  `proxy_bridge`.

The learned surrogate is Q81's: a random forest (400 trees, `random_state=0`) over the ten size-invariant
intensive features, evaluated by stratified 5-fold cross-validation (`shuffle=True, random_state=0`).
Trajectory seed 0 for the proxy estimates and the features, so every quantity is computed on one common
set of trajectories.

## Measures and decision rules

- **Rank-AUC** of each single proxy against the binary label (`roc_auc_score`); higher proxy predicts
  triadic.
- **Best-threshold accuracy** of each single proxy (the accuracy of its best single cut).
- **Surrogate** CV ROC-AUC, CV accuracy, and out-of-fold predictions.
- H1 confirmed if every single proxy has rank-AUC < 0.85.
- H2 confirmed if the surrogate's CV ROC-AUC ≥ 0.95 and exceeds every single proxy's rank-AUC.
- H3 confirmed if the surrogate's CV accuracy exceeds the best single proxy's best-threshold accuracy.
- H4 confirmed if the surrogate's out-of-fold CV accuracy on the modal-in-degree subset is ≥ 0.90.

# Q81 — Stage 4 methods (fixed before computation)

Ground truth is the exact IIT-4.0 verdict (`classifier.classify_rules`) on each form's deterministic
Boolean rules. The surrogate sees only cheap statistics estimated from a noisy trajectory of the form,
never Φ itself. Run on `~/iit-playground/venv-4.0/bin/python`.

## Corpora (`forms.py`)

- **In-distribution (n=3):** the 256 strict-mediation outreach forms (sender intent S, mediator M,
  recipient R; no direct S↔R edge), from `corpus.population.enumerate_family`. The exact verdict labels
  each form.
- **Held-out (n = 4, 5, 6):** 20 outreach forms with known verdicts, assembled from the breadth (Q64
  `all_required`/`substitutable`/`pooled`), chain/ring (Q66 `open_chain`/`ring`), and market (Q85
  `all_required`/`substitutable`/`mixed`) generators. Both classes appear (13 triadic, 7 dyadic). Each
  held-out label is the exact verdict recomputed here, not the source study's tag.

## Features (`intensive_features`)

Each form's trajectory is the deterministic TPM mixed toward its flipped output by noise 0.08, simulated
for T = 6000 steps. From the T×n trajectory, ten **size-invariant** features are computed: the mean,
max, min, and standard deviation of per-node entropy; the mean, max, and min of pairwise mutual
information; the mean and max of transfer entropy; and the per-node O-information. Every feature is an
aggregate over nodes or pairs, so the vector has length 10 at any n. No feature encodes n, so the
surrogate cannot read size directly.

## Model and test (`probe_learned_surrogate.py`)

- **Model:** random forest, 400 trees, `random_state=0`.
- **In-distribution:** stratified 5-fold cross-validation (`shuffle=True, random_state=0`) on the n=3
  family; report ROC-AUC and accuracy against the majority-class baseline. Trajectory seed 7.
- **Generalization:** train on the full n=3 family (seed 7); test on the held-out larger forms, with the
  held-out trajectories estimated at seeds 1, 2, 3 (estimation-noise robustness). Report mean accuracy
  and mean dyadic recall.
- **Decision rules:**
  - H1 confirmed if CV ROC-AUC ≥ 0.85.
  - H2 confirmed if CV accuracy ≥ majority baseline + 0.10.
  - H3 confirmed if mean generalization accuracy ≥ 0.75.
  - H4 confirmed if mean held-out dyadic recall ≥ 0.50.

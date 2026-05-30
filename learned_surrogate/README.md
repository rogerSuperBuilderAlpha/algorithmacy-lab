# Learned surrogate: can cheap features *together* predict exact IIT‑4.0 Φ?

The [proxy](../proxy_audit/) and [candidate](../candidate_audit/) audits showed
that no *single* cheap measure tracks exact IIT‑4.0 Φ well. This experiment asks
the constructive follow‑up: **does a model that combines the cheap features
recover Φ?** It also publishes a reusable **exact‑IIT‑4.0 feature dataset** — the
kind of 4.0 ground truth that surrogate work (e.g.
[Hosaka et al. 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335966),
which used IIT 3.0 without PyPhi) currently lacks.

## Result

720 networks, 5‑fold cross‑validated (out‑of‑fold) scores:

| Task | Best single feature | Learned model |
|------|------:|------:|
| Predict Φ (Spearman ρ) | 0.32 | **0.54** (random forest) |
| Detect Φ > 0 (AUC) | 0.69 | **0.90** (random forest) |

Combining cheap features beats any single one — detection of integrated systems
becomes quite reliable (AUC 0.90). `phi_wms` carries most of the signal. See
[`FINDINGS.md`](FINDINGS.md).

![surrogate](results/surrogate.png)

**Size extrapolation** (`extrapolate.py`): trained on `n ∈ {3,4}` and tested on a
fresh unseen `n=5` set, **detection extrapolates** (AUC 0.84, vs 0.90
in‑distribution) but **magnitude prediction does not** (ρ 0.54 → 0.33). Cheap
surrogates look usable for screening across scales, not yet for accurate Φ
estimation.

## Files

- `build_dataset.py` — generates `results/dataset.csv`: one row per network with
  exact IIT‑4.0 Φ (mean/max over reachable states) + 12 cheap features (the union
  of the proxy‑ and candidate‑audit features). This CSV is the reusable benchmark.
- `train.py` — cross‑validated Ridge / random‑forest surrogates vs the best
  single feature, for both the regression and detection tasks; feature
  importances; plot.

## Reproduce

```bash
python -m learned_surrogate.build_dataset 40 2
python -m learned_surrogate.train
```

Requires `scikit-learn` (see repo `requirements.txt`).

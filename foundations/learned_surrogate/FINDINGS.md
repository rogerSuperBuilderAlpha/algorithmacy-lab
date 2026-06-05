# Findings: combining cheap features predicts Φ far better than any single one

**TL;DR.** The proxy and candidate audits showed no *single* cheap measure
tracks exact IIT‑4.0 Φ well. This experiment shows the constructive flip side:
a learned model that **combines** the same cheap features predicts Φ
substantially better — and is genuinely useful as a **detector** of integrated
systems. On 720 networks, out‑of‑fold:

| Task | Best single feature | Learned model |
|------|------:|------:|
| Regression — Spearman ρ(pred, Φ) | 0.32 (density) | **0.54** (random forest) |
| Detection — AUC for Φ > 0 | 0.69 (Φ_WMS) | **0.90** (random forest) |

All scores are cross‑validated (5‑fold, `cross_val_predict`), so they reflect
generalization to unseen networks, not fit.

## What this means

- **No single measure suffices, but the information is there.** Combining a
  dozen cheap features recovers a large part of Φ's rank ordering (ρ 0.32→0.54)
  and makes the *presence* of integration highly predictable (AUC 0.69→0.90).
  Detecting "is this system an integrated complex?" from cheap features is, on
  these systems, quite doable; predicting *how much* Φ remains only moderate.
- **Φ_WMS carries most of the signal.** It dominates the random‑forest
  importance (0.61), consistent with the candidate audit finding it the best
  single theoretical measure — but `tdmi`, `n_edges`, and `causal_density` add
  enough to lift the combined model well above Φ_WMS alone.
- **The non‑linear model beats the linear one** (RF ρ 0.54 vs Ridge 0.42),
  implying the features relate to Φ through interactions, not a simple weighted
  sum — echoing the non‑monotonicity seen in the proxy audit.

## Why this is useful

This is the cheap‑surrogate direction pursued by
[Hosaka et al. (2025)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335966)
with graph neural networks — but their ground truth was IIT **3.0** and not
generated with PyPhi. Here the target is **exact IIT‑4.0 Φ**, and the
720‑network feature dataset (`results/dataset.csv`) is published as a reusable
benchmark for training and comparing surrogates against the current formalism.

## Does it extrapolate to larger systems? (`extrapolate.py`)

The central worry for any cheap Φ surrogate is **size extrapolation**: it is
trained where exact Φ is computable (small systems) but must run where it is not
(large ones). We train on `n ∈ {3,4}` and test on a **fresh, unseen `n=5` set**
(300 networks):

| Train → test | ρ (predict Φ) | AUC (detect Φ>0) |
|--------------|------:|------:|
| in‑distribution (5‑fold CV) | 0.54 | 0.90 |
| n=3 → n=4 | 0.30 | 0.81 |
| n=4 → n=3 | 0.36 | 0.82 |
| **n=3,4 → n=5 (unseen)** | 0.33 | **0.84** |

**Detection extrapolates; magnitude estimation does not.** Trained only on
`n ≤ 4`, the surrogate still detects integrated systems at a larger unseen size
(`n=5`) with AUC 0.84 — close to its in‑distribution 0.90. But predicting *how
much* Φ a system has degrades sharply out‑of‑size (ρ 0.54 → 0.33). The practical
read: cheap surrogates look usable for **screening/detection across scales**, but
not yet for accurate Φ *estimation* — a concrete, testable caution for the
surrogate program. (`results/test_n5.csv` extends the benchmark to `n=5`.)

## Caveats

- Small systems (`n ∈ {3,4}`), specific Boolean‑gate ensemble; a surrogate that
  works here need not extrapolate to large or real systems — the open question
  in the field. The dataset is offered precisely so others can probe that.
- 177 / 720 networks have Φ > 0; the regression task is dominated by small‑Φ
  systems.
- Feature importances are descriptive (impurity‑based), not causal.
- Target is **mean exact Φ over reachable states** (the audits' convention).

## Reproduce

```bash
python -m foundations.learned_surrogate.build_dataset 40 2   # -> results/dataset.csv
python -m foundations.learned_surrogate.train                 # -> surrogate_summary.csv, surrogate.png
```

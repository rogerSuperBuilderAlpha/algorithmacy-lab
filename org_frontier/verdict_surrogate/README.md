# verdict_surrogate — a learned cheap-feature screen for the coordination verdict past the size ceiling

Exact IIT-4.0 Φ gives the literacy/algorithmacy verdict on a coordination form, but the computation
grows super-exponentially: a timing probe here measures 0.06 s at n = 3, 3 s at n = 5, and 25 s at
n = 6 on a mediator chain, roughly ×8 per party, so a *population* of forms is exactly labelable only
to about n = 6, a sample to n = 7, and single landmark forms to n = 8. This arm asks whether a model
trained on cheap features — ones a researcher can read off a form far past that ceiling — recovers the
verdict, and whether it keeps recovering it at party counts it never saw in training.

Two earlier results bracket the question:

- [`../proxy_bridge/`](../proxy_bridge/) showed a **single cheap proxy** from a trajectory does **not**
  recover the verdict (rank-AUC 0.63). Its failure mode is the back-channel: a dyadic form with a
  direct worker–counterpart edge produces strong statistical dependence a single proxy misreads as
  integration.
- [`../../foundations/learned_surrogate/`](../../foundations/learned_surrogate/) showed a **learned
  combination** of features predicts **generic Φ** on **random networks**, and that *detection*
  extrapolates in size (AUC 0.84 to an unseen n = 5) even though *magnitude* does not (ρ 0.33). It
  never touched the coordination verdict.

This arm sits between them: a learned combination, targeting the coordination verdict, on
coordination-structured forms, tested for size extrapolation. The mechanism it turns on is that the
back-channel that defeats a single proxy is a *structural* fact — visible in the connectivity matrix,
no Φ required — so a model given cheap structural features can learn the discount exact Φ makes over
the MIP.

The hypotheses are pre-registered in [`hypotheses.md`](hypotheses.md), committed before any result.

## Run

All commands from the repo root with the IIT-4.0 venv.

```bash
# 1. Build the training pool (n<=5, ~1 min) or the full dataset with the held-out n=6,7,8 test (slower).
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.build_dataset --max-n 5
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.build_dataset --max-n 8

# 2. H1 — recover the verdict within n<=5 vs the single-proxy and structural-heuristic baselines.
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.train

# 3. H2 — train on n<=5, test verdict recovery on the held-out n=6,7,8.
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.extrapolate

# 4. H3 — where the held-out errors concentrate (the deferral rule).
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.boundary
```

## Files

- `forms.py` — coordination-form generators (random strict-mediation, back-channel variants, chains,
  all-required conjunctions, substitutable) at any n, and the cheap feature functions (structural,
  from the connectivity matrix and the mediator's truth table; dynamical, from the proxy and candidate
  audits). No feature computes exact Φ.
- `build_dataset.py` — labels each form with the exact classifier verdict; writes `results/dataset.csv`;
  checkpointed and resumable.
- `train.py` (H1), `extrapolate.py` (H2), `boundary.py` (H3) — the analyses.
- `results/` — `dataset.csv`, `timing.csv`, the per-hypothesis JSON and plots.
- `FINDINGS.md` — the numbers, the honest boundary, and the reproduce commands.

## Altitude

The surrogate is a **screen that flags forms for exact Φ**, not a replacement for it. Above the
feasible oracle no exact ground truth exists, so no correctness claim is made there. Exact Φ is not
demoted: the contribution is a cheap pre-filter that widens the range the exact instrument can be
pointed at.

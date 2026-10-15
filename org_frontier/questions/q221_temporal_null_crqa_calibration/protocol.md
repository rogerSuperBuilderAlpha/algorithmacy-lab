# q221 protocol record

## Frozen-before-evaluation specifications

Each analysis spec was committed before its run. `git show <commit>` shows the spec text in the script's
docstring, which fixes the seeds, sample sizes, predictors, metrics and decision rules.

| analysis | spec commit | run commit | held-out data |
|---|---|---|---|
| survivor baselines (`identifiability/baselines_survivors.py`) | `35313d47` | the following commit | test seeds 44100..44299 |
| structural baselines on held-out families (`identifiability/structural_baselines.py`) | `ecd014dd` | crash-fix commit (None core → ineligible; spec text unchanged), then the run | eval families `nsi` ↔ `aff` (train on one, evaluate on the other) |
| null extension (`identifiability/null_extension.py`) | `6ad206a3` | the following commit | – (calibration: known null DGP) |

## Not prespecified (exploratory or exact)

- Exact screen, isomorphism checks, exact Φ, process-law equivalence and target audit. These are
  deterministic exact computations, so no sampling decision is involved.
- Hassan's pilot (`independent_audit/null_pilot.py`). It was reproduced byte-identically, not re-specified.

## Categories, kept separate (mandate)

| category | contents |
|---|---|
| exploratory search | screen, survivors, adjudication |
| pilot calibration | gate E |
| structural prediction pilot | gate D |
| confirmatory | **none** |

## Not run

These were declared in the mandate's baseline list but not executed:
- transfer entropy;
- recurrence-only statistics other than q220's;
- SHREC;
- joint recurrence plots and MdCRQA;
- false-pair surrogates;
- the TTS test.

## Comparator study (prespecified 2026-10-15, before any run)

- **Script:** `identifiability/comparators.py`. Its docstring is the binding spec, and it is committed before
  the first execution.
- **Pairs:** the 3 surviving pairs (S1 = the lead pair P/Q).
- **Data:** the q220 generator at T = 600 and flip 0.08. Seeds `47000 + 1000·pair + 500·member + r`:
  100 training and 200 test trajectories per member.
- **Comparators:**
  - C1: transfer entropy (history 1);
  - C2: joint-recurrence rates (lags 1..10);
  - C3: MdRQA full-vector recurrence rates (lags 1..10);
  - C4: SHREC (`williamgilpin/shrec` @ `49c6d3e0`, library defaults, `random_state` = 0), with 4
    prespecified features of the reconstructed driver;
  - C5: false-pair surrogate z-scores of q220 prominence (199 label-agnostic surrogates, seed 47999).
- **Exact population separation:** computed for C1–C3, with threshold 1e-12. For C5 it is equal by theorem.
  For C4 it is not computable.
- **Finite-sample test:** nearest-centroid classifier.
- **Decision rule:** "separates" if the Bonferroni-adjusted Wilson lower bound (15 tests, z = 2.935)
  is > 0.5.
- **Theory-based expectations** are recorded in the docstring.
- **Environment:** run in `/workspace/shrec-venv` (Python 3.12, numpy 2.5.4, scipy 1.18.1, scikit-learn
  1.9.1, umap-learn 0.5.12). PyPhi is not needed.

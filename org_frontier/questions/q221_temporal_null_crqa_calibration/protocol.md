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

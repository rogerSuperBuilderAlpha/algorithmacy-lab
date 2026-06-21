# v8, pre-registered hypotheses — the recurrence instrument on a real recorded series

This file is committed before the analysis is run, so the git history shows the predictions were fixed
before the results. The series is the PyPhi commit history (`commits_raw.csv`), encoded into weekly
party-activity by [`encode.py`](encode.py). The predictions below concern the coordination outcomes,
which have not been computed; the data coverage (how many weeks each contributor is active) was
inspected to choose the two eras, and is reported in the encoding, but no recurrence or Φ result has
been seen.

## The arrangement

Open-source contributors coordinate through a shared repository and a maintainer who reviews and merges.
The maintainer, wmayner, is the gatekeeper the others reach the codebase through, the real-world analog
of the lab's mediating system and a candidate veto player. The core era (2014–2018) is a three-party
coordination — wmayner, the major co-developer rlmv, the early contributor William Marshall. The recent
era (2022–2024) is a four-party coordination — wmayner with isacdaavid, dviggiano, ajbailey4.

## What runs, and what does not

Cross-recurrence runs directly on the recorded series; it needs no model. This is the first time the
behavioral instrument reads data the lab did not generate. Φ needs a model of who determines whom,
which the field protocol elicits from domain knowledge. That elicitation is not done here, so the Φ
side is a first pass only: a Boolean model is fit to the activity series and its exact Φ computed, and
the verdict is labeled as model-fit, weaker than an elicited one. The honest reading is that v8 starts
the real-data work with the behavioral instrument; the structural instrument's real-data step is the
deeper field-protocol work this opens.

## Predictions

- **H1 — the maintainer is the behavioral hub.** wmayner has the highest coupling centrality in both
  arrangements: the contributors couple to the maintainer more than to each other, the behavioral
  signature of the structural [veto player](../../threads/veto_player/THREAD.md).
- **H2 — the core dyad couples and sustains.** In the core era the strongest pairwise coupling is
  wmayner–rlmv, with a long diagonal (a sustained co-active stretch), since the two carried the library
  together through that era.
- **H3 — coordination is synchronous, not led.** Activity couples near lag zero more than at a strong
  directed lag, because open-source work clusters around shared release and review periods rather than
  one party strictly pacing another.
- **H4 — the core era is irreducible when modeled.** A Boolean model fit to the three core-era series
  has positive exact Φ: the contributors form a bound coordination, not three independent activity
  streams. Stated as a model-fit verdict, with the fit quality reported.
- **H5 — peripheral contributors are near-spectators.** The low-volume contributors of the recent era
  (dviggiano, ajbailey4) score low coupling centrality, the behavioral form of the
  [observer](../../threads/observer/THREAD.md) result: present in the record, weakly bound into the
  coordination.

## What would refute each

H1 fails if a contributor out-couples the maintainer. H2 fails if another pair, or none, is the
strongest sustained tie. H3 fails if a prominent directed lag dominates the synchronous peak. H4 fails
if the fit model has Φ of zero, or if the fit is too poor to trust. H5 fails if a low-volume
contributor scores high centrality. Nulls and refutations are results here, reported as they fall.

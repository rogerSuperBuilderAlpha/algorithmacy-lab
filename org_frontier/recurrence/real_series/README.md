# v8 — the recurrence instrument on a real recorded series

The recurrence program had paired Φ with cross-recurrence on the lab's own synthetic trajectories. v8
takes the behavioral instrument onto a real recorded series the lab did not generate, the open question
[RESEARCH_PROGRAM_V7.md](../../RESEARCH_PROGRAM_V7.md) named.

## The series

The commit history of PyPhi (github.com/wmayner/pyphi), the library the lab computes Φ with. Open-source
contributors coordinate through a shared repository and a maintainer who reviews and merges, a real
mediated coordination with the maintainer the gatekeeper the others reach the codebase through. Two eras
where several contributors overlap give two arrangements: a three-party core era (2014–2018: wmayner,
rlmv, William Marshall) and a four-party recent era (2022–2024: wmayner, isacdaavid, dviggiano,
ajbailey4).

## The pipeline

- [`fetch_commits.py`](fetch_commits.py) → [`commits_raw.csv`](commits_raw.csv) — every commit's author
  and date through the GitHub API, the frozen provenance.
- [`encode.py`](encode.py) → `activity_{core,recent}.csv` — weekly party activity, active when a
  contributor made at least one commit that week. This is the field protocol's observation and bit
  calibration, applied to real data.
- [`HYPOTHESES.md`](HYPOTHESES.md) — five predictions, committed before the analysis ran.
- [`analyze.py`](analyze.py) — cross-recurrence on the series, and an exact Φ on a Boolean model fit to
  the core era.
- [`FINDINGS.md`](FINDINGS.md) — the results.

## The result, in one line

The behavioral instrument ran on real data, the milestone of v8, and most of the coordination
predictions were refuted: weekly commit activity records co-presence and co-absence, missing the
review-and-merge causal structure where the maintainer's coordination actually lives. The instrument is
sound; the encoding is the gap, and the next series is event-level. See [FINDINGS.md](FINDINGS.md).

## What runs here, and what does not

Cross-recurrence runs directly on the series; it needs no model, and this is the first time it reads
data the lab did not generate. Φ needs a model of who determines whom. The field protocol elicits that
from domain knowledge; here it is only fit to the activity, so the Φ verdict is a labeled first pass,
weaker than an elicited one. The real-data Φ step is the deeper field-protocol work this opens.

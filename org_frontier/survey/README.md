# Survey — measuring algorithmacy in real workers

The lab's instrument is exact and its results reproduce, and every one of them is in-silico. No real
worker, platform, or message has been measured. The survey arm is the side of the validation gap that
the computational, qualitative, and recurrence arms cannot reach on their own: self-report from people
inside a real coordination arrangement, collected on a fixed schedule with the questions committed
before the answers.

The arm carries one construct from theory into measurement. Algorithmacy is named in the methods guide
as a lived competence with three parts: a worker reconstructs a hidden counterpart's wants from
outcomes, compresses real intent into the few signals the system accepts, and tracks rule changes the
system makes without announcement (see [`../qualitative/METHODS.md`](../qualitative/METHODS.md), method
8). Those three parts are a testable structure. A survey arm asks whether they cohere as a measurable
competence, whether the competence grows when people coordinate through a mediating system over months,
and how it relates to the conditions the catalog says should matter — task interdependence, whether the
system commits or conveys, and whether a worker is pivotal or substitutable.

## What a survey study is, and is not

A survey study measures self-report. It does not compute a Φ verdict and does not claim one. A worker's
report that the system decides is evidence about the worker's experience, not a measurement of
irreducibility on a model. The arm keeps that line where the qualitative arm keeps it: the verdict lives
on a model, and self-report is data about how the parties experience the arrangement. Where a survey
study connects to the catalog, it does so by reading a construct the catalog names against what real
participants report, and reporting where the two diverge.

The discipline is the lab's standard one. A survey study commits its instrument, its hypotheses, its
scoring, and its analysis plan before any data is collected, so the git history shows the design was
fixed before the results. The pre-registration is the survey form of committing hypotheses before
computing.

## Read next

- [`cohort_algorithmacy/README.md`](cohort_algorithmacy/README.md) — the **handoff packet**: the front
  door to the first study, packaged so a researcher can field it and run the pre-registered analysis.
- [`cohort_algorithmacy/STUDY.md`](cohort_algorithmacy/STUDY.md) — the first study: a three-wave panel
  of a real developer cohort that coordinates through platforms it builds, gated by peer review.
- [`cohort_algorithmacy/PRE_REGISTRATION.md`](cohort_algorithmacy/PRE_REGISTRATION.md) — the locked
  design: constructs, scales, hypotheses, decision rules, and what would falsify each.
- [`cohort_algorithmacy/codebook.md`](cohort_algorithmacy/codebook.md) — every variable, item, response
  scale, reverse key, and scoring rule.
- [`cohort_algorithmacy/analysis_plan.md`](cohort_algorithmacy/analysis_plan.md) — the measurement model,
  the growth model, the planned tests, missing-data handling, and the small-sample stance.
- [`cohort_algorithmacy/instruments/`](cohort_algorithmacy/instruments/) — the consent form and the three
  survey waves as administered.
- [`cohort_algorithmacy/analysis.py`](cohort_algorithmacy/analysis.py) — the analysis pipeline, runnable
  now on a simulated cohort and completed by pointing it at the real wave files.

## How to contribute

The workflow is the lab's standard one (see [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md)): branch off
`contrib`, build the study, commit the pre-registration before fielding, open a pull request into
`contrib`. A survey study registers no reproduced number while data collection is open; once a dataset
is in hand, the analysis script and its figures register in [`../../ci/reproduce.json`](../../ci/reproduce.json)
so the reported numbers re-derive from the committed data and code. Human-subjects data is governed by
the approving institutional review board, and only de-identified, aggregated, or board-approved material
is committed to this public repository.

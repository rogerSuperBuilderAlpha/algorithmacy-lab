# A survey handoff packet: the cohort algorithmacy panel

The survey instrument packaged for handoff, so a researcher can field the first measurement of
algorithmacy as a lived competence in a real cohort and take it through the pre-registered analysis. The
materials — the instrument, the pre-registration, the codebook, the analysis plan, the consent and wave
questionnaires, and the human-subjects protections — are complete; what remains is real participants over
the panel's span, which only fielding provides. This is the measurement-side companion to the
[field-study packet](../../field/packets/gig_dispatch/): that one reads the structure of a coordination,
this one measures the competence the structure demands.

## What the study measures, and what it tests

The study develops and validates the Algorithmacy Competence Scale, the construct's three facets —
counterpart inference, signal compression, rule-change tracking — and tracks whether the competence grows
over a sixteen-week developer cohort, relating it to task interdependence, perceived system authority,
autonomy, ownership, transactive memory, and perceived substitutability. The three facets are the three
places the cognitive theories break, so each carries a formal prediction from the
[cognition arm](../../cognition/survey_bridge.md): counterpart inference should matter most where the
system commits, signal compression under narrower input, rule-change tracking under faster retraining, and
the scale as a whole should track perceived commitment, which is the empirical test of the
literacy-versus-algorithmacy line.

## The files

- [`STUDY.md`](STUDY.md) — the full proposal: fit, the setting, the construct and its prior, the research
  questions, contributions, literature, method, ethics, and limitations.
- [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) — the constructs, hypotheses, decision rules, and the
  failure modes, to commit before any data.
- [`codebook.md`](codebook.md) — every scale and item, the response formats, and the scoring.
- [`instruments/`](instruments/) — the [consent form](instruments/consent.md) and the three wave
  questionnaires, ready to load into a survey platform.
- [`analysis_plan.md`](analysis_plan.md) — the measurement model, the growth model, the nomological
  relations, the missing-data handling, and the inference safeguards.
- [`analysis.py`](analysis.py) — the analysis pipeline, runnable now on a simulated cohort and completed by
  pointing it at the real wave files.

## How to field it

Commit [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) first, so the git history shows the hypotheses, the
scoring, and the decision rules were fixed before the data. Obtain institutional review board approval and
the consent in [`instruments/consent.md`](instruments/consent.md). Recruit the cohort and field the three
waves on the panel schedule in [`STUDY.md`](STUDY.md), loading the questionnaires from
[`instruments/`](instruments/) into a survey platform. Export each wave as `wave{1,2,3}.csv`, one row per
respondent with the item columns from [`codebook.md`](codebook.md), beside [`analysis.py`](analysis.py),
which then runs the scoring, reliability, growth, and association pipeline on the real responses. Run the
confirmatory factor analysis, longitudinal invariance, McDonald's ω, and the latent growth model from the
analysis plan with a structural-equation package; the scaffold marks where each goes.

## What it closes, and what it does not

A completed run closes the measurement piece of the validation gap: a self-report scale for algorithmacy,
validated in a real cohort, with its growth and its relation to the commit-versus-convey structure
estimated. It is self-report, so it measures the competence as workers experience and describe it, the side
the structural and behavioral arms cannot reach. It does not by itself read the structure of any
arrangement; that is the [field protocol](../../field/PROTOCOL.md) and its packet. Run together on the same
workers, the field study reads the structure and the survey measures the competence against it, which is
the join the lab points at.

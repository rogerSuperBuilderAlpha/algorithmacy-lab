# Handoff packets — pick one up and run it

The lab's empirical and bridge arms are each packaged so a researcher can pick one up and take it from a
real input to a verdict, without reading the whole repository first. Every packet has the same three parts:
a front-door README that says what the packet produces and how to instantiate it, a pre-registration or
mapping discipline committed before any result, and a runnable scaffold that runs now on a bundled example
and accepts the real inputs in its place. Five packets cover the five arms.

## The five packets

- **[Survey — the cohort algorithmacy panel](survey/cohort_algorithmacy/README.md).** Field a three-wave
  panel and validate the Algorithmacy Competence Scale. Scaffold:
  [`analysis.py`](survey/cohort_algorithmacy/analysis.py) — facet scoring, Cronbach's α, growth, and the
  H3b association, runnable on a simulated cohort and on real `wave{1,2,3}.csv`. Bring: a recruited cohort,
  IRB approval, three waves of responses.
  `PYTHONPATH=. python org_frontier/survey/cohort_algorithmacy/analysis.py`

- **[Field — gig dispatch](field/packets/gig_dispatch/README.md).** Take one real coordination to a
  dyadic or triadic verdict from interview and observation evidence. Scaffold:
  [`analysis.py`](field/packets/gig_dispatch/analysis.py) — the instrument controls, the candidate model's
  Φ verdict, and the four-force sensitivity battery. Bring: a fielded interview study, the elicited
  determination rules.
  `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/field/packets/gig_dispatch/analysis.py`

- **[Recurrence — the paired-instrument pipeline](recurrence/packets/template/README.md).** Read one
  coordination off behavior and pair it with structure. Scaffold:
  [`run_study.py`](recurrence/packets/template/run_study.py) — cross-recurrence on the series and exact Φ on
  a model of the same arrangement, the behavioral half on numpy alone. Bring: two encoded recorded series,
  an elicited Boolean model.
  `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/recurrence/packets/template/run_study.py`

- **[Cognition — the theory-mapping method](cognition/packets/template/README.md).** Map one theory of
  mind to the apparatus and test whether it holds the interested third party. Scaffold:
  [`map_theory.py`](cognition/packets/template/map_theory.py) — the channel and committing models through
  the probe, with the core-membership read. Bring: a theory, its channel assumption, the two models.
  `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/cognition/packets/template/map_theory.py`

- **[Qualitative — the study template](qualitative/template/README.md).** Take a coordination setting from
  fieldwork to a writeup, and for a model-bound study to a verdict. Scaffold:
  [`analyze.py`](qualitative/template/analyze.py) — the verdict, the major-complex membership, the
  sensitivity re-encoding, and the verdict under each account where the parties disagreed. Bring: a fielded
  study, the elicited rules, the committed coding scheme.
  `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/qualitative/template/analyze.py`

## The shared discipline

Each packet commits its predictions before its result, the git history standing as the evidence: the survey
commits its pre-registration, the field and qualitative studies commit the coding scheme and the elicited
rules, the recurrence study commits its hypotheses, the cognition mapping commits its predicted verdict.
Each scaffold runs its instrument controls first where it computes Φ — a decoupled model must give Φ = 0 and
a coupled one Φ > 0 — and reads no verdict if they fail. The scaffolds that compute Φ need the PyPhi venv
from [`../GETTING_STARTED.md`](../GETTING_STARTED.md); the survey scaffold and the behavioral half of the
recurrence scaffold run on numpy alone.

## What a packet does not do

A packet hands off the method and the machinery. It does not field the study: the survey needs real
participants, the field and qualitative studies need real interviews and observation, and fabricating any of
that would break the discipline the catalog rests on. The bundled examples carry the predicted structure so
the scaffold demonstrates recovering it; the real inputs set the real verdict. The encoding still has to fit
the arrangement, which is the work the packet hands a researcher and the field protocol's hardest step.

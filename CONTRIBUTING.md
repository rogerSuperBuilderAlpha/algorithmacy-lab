# Contributing

Contributions are welcome: a new research question, a probe, a foundations experiment, a bug fix, or a
correction to a result. This repository runs on a few firm conventions.

To **publish an essay or a study** through the public, reproducibility-first review process — fork, pull
request into the `contrib` branch, maintainer sign-off, merge — see [`PUBLISHING.md`](PUBLISHING.md).
`contrib` and `main` are branch-protected: every change is a pull request, CI re-derives each registered
number, and a merge needs one approving review. This file covers the code, probe, and house-style
conventions that a submission has to meet.

## Setup

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

PyPhi installs from its IIT-4.0 line (see `requirements.txt`). Run probes and experiments from the repo
root so `org_frontier.*` and `foundations.*` resolve.

## The research protocol

Lab work follows [`org_frontier/protocol/RESEARCH_PROTOCOL.md`](org_frontier/protocol/RESEARCH_PROTOCOL.md):
review prior work, research the literature, fix hypotheses and their nulls **before** computing, specify a
decision rule per hypothesis, run against the exact-Φ instrument, write the result up. The non-negotiable
gates:

- **Validate the instrument on a known control before any comparison.** A probe asserts that an
  established form reproduces its known verdict, then runs.
- **Compute, do not assert.** Check a claim against exact Φ rather than arguing it.
- **Report nulls and refutations as first-class results.** A refuted hypothesis is logged as refuted.
- **State the validation gap.** A computational result is evidence about the model, not the organization.

The empirical and bridge arms each ship a ready-to-run **handoff packet** for the survey, field, recurrence,
cognition, and qualitative work the sections below describe: a front-door README, the pre-registration
discipline, and a runnable scaffold. The five are indexed in
[`org_frontier/HANDOFF_PACKETS.md`](org_frontier/HANDOFF_PACKETS.md); start there to take an arm from a real
input to a verdict.

## Adding a probe or a question

- A probe is a `org_frontier/probes/probe_<slug>.py` script whose module docstring states the question,
  the hypothesis, the method, and the run command. It prints exact numbers and gets a row in
  [`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md) continuing the global numbering. That
  numbering is global across both standalone probe scripts and question probes and the rows are not in
  strict numeric order, so there is no scaffolder for a plain probe number — take the next free one as the
  current maximum plus one:
  `grep -oE '^\| [0-9]+' org_frontier/probes/PROBES.md | grep -oE '[0-9]+' | sort -n | tail -1`.
- A full question goes through the pipeline and lands under `org_frontier/questions/q<NN>_<slug>/`. Copy
  [`org_frontier/protocol/template/`](org_frontier/protocol/template/), or run the orchestration.
- Reuse the shared infrastructure rather than rebuilding it: `org_frontier/classifier/`,
  `org_frontier/probes/lib.py`, `org_frontier/probes/_info.py`, `foundations/proxy_audit/exact_phi.py`.

## Adding a qualitative study

The empirical arm reads real coordination against the priors. A qualitative study lands under
`org_frontier/qualitative/<slug>/`, built from
[`org_frontier/qualitative/template/`](org_frontier/qualitative/template/). It may stand on its own as a
thick description of a coordination setting, or take one arrangement through the
[field protocol](org_frontier/field/PROTOCOL.md) to a verdict. See
[`org_frontier/qualitative/README.md`](org_frontier/qualitative/README.md) for the arm,
[`METHODS.md`](org_frontier/qualitative/METHODS.md) for the methods, and
[`TOPICS.md`](org_frontier/qualitative/TOPICS.md) for the open agenda.

The pre-commitment discipline carries over in qualitative form: commit the coding scheme, interview guide,
and bit calibration **before** the fieldwork, so the git history shows the questions were fixed before the
answers. A qualitative study registers no number in `ci/reproduce.json`, since it computes none; the
`directory-current` check confirms it is indexed once you run `python tools/build_index.py`.

## Adding a recurrence experiment

The recurrence program pairs exact Φ with cross-recurrence quantification: Φ reads a coordination model's
structure, cross-recurrence reads a run of it. Work lands under `org_frontier/recurrence/`, building on
[`crqa.py`](org_frontier/recurrence/crqa.py) (the measures and the trajectory generator) and the existing
Φ harnesses. Each experiment script is seeded so its numbers reproduce, and its findings go in a paired
markdown file. See [`org_frontier/recurrence/README.md`](org_frontier/recurrence/README.md) for the arm
and [`CONCEPTS.md`](org_frontier/recurrence/CONCEPTS.md) for what each measure indexes and how Φ and CRQA
differ. The pre-commitment and report-the-nulls rules apply as in the computational program.

## Adding a survey study

The survey program is the human-subjects arm: self-report measuring algorithmacy as a lived competence in
workers inside a real coordination arrangement. Work lands under `org_frontier/survey/<study>/`, with the
instrument, scoring, hypotheses, and analysis plan committed **before** any data, the pre-commitment
discipline in its human-subjects form. A study carries its consent and ethics materials, and reports no
`ci/reproduce.json` number until it has data; the `directory-current` check confirms it is indexed. See
[`org_frontier/survey/README.md`](org_frontier/survey/README.md) for the arm and its first pre-registered
panel study.

## Register your numbers for CI

Every number a submission reports has to reproduce from a committed script. Add an entry to
[`ci/reproduce.json`](ci/reproduce.json) for each claimed result: a `name`, the `cmd` to run from the
repo root, and the `expect` strings its output must contain (include the number verbatim). Run
`python ci/reproduce.py` locally to confirm it passes before opening the PR.

A pull request runs only the checks it could have affected — the instrument control (`"core": true`)
plus the checks for studies whose files the PR changed. The full manifest is reproduced nightly by
`reproduce-all-nightly.yml`. Keep checks fast and deterministic; a check that takes minutes (a
whole-space sweep, exact Φ past a few nodes) gets `"slow": true`, which keeps it out of the per-PR gate
and leaves it to the nightly job.

## Prose

All prose follows the house style in [`CLAUDE.md`](CLAUDE.md): no first person, plain declarative
sentences, section titles as short noun phrases, and a de-slop pass (cut the antithesis machine,
self-narration of rigor, and metronomic openers). Citations resolve to real sources.

## Git and the two repositories

This tree contains a separate, private dissertation repo nested at `dissertation/`, gitignored here. Where
you run git from decides the remote. Read [`REPO_LAYOUT.md`](REPO_LAYOUT.md) before committing, and never
`git add -f dissertation/`.

## Reporting a problem

Open an issue with the probe or experiment name, the exact command, and the output. A result that does not
reproduce from the committed script is a bug worth filing.

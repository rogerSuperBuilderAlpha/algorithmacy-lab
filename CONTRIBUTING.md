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

## Adding a probe or a question

- A probe is a `org_frontier/probes/probe_<slug>.py` script whose module docstring states the question,
  the hypothesis, the method, and the run command. It prints exact numbers and gets a row in
  [`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md) continuing the global numbering.
- A full question goes through the pipeline and lands under `org_frontier/questions/q<NN>_<slug>/`. Copy
  [`org_frontier/protocol/template/`](org_frontier/protocol/template/), or run the orchestration.
- Reuse the shared infrastructure rather than rebuilding it: `org_frontier/classifier/`,
  `org_frontier/probes/lib.py`, `org_frontier/probes/_info.py`, `foundations/proxy_audit/exact_phi.py`.

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

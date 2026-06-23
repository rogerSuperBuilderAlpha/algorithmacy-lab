# AGENTS.md — org_frontier/survey (the human-subjects arm)

Measuring algorithmacy as a lived competence through self-report from workers inside a real coordination
arrangement — the measurement side of the validation gap the other arms cannot reach. A pre-registered
panel study; pre-fieldwork, no data collected yet. The shared rules live in the root
[`../../AGENTS.md`](../../AGENTS.md).

## Local entry points

- [`README.md`](README.md) — the arm and its first pre-registered panel study.
- A study lands under `org_frontier/survey/<study>/` with its instrument, scoring, hypotheses, and
  analysis plan.

## Add a study and verify

- Commit the instrument, scoring, hypotheses, and analysis plan **before** any data — the pre-commitment
  discipline in its human-subjects form. Carry the consent and ethics materials with the study.
- A study reports no `ci/reproduce.json` number until it has data; the `directory-current` gate confirms
  it is indexed once you run `python tools/build_index.py` (then its `--check`).
- Prose follows the house style in [`../../CLAUDE.md`](../../CLAUDE.md).

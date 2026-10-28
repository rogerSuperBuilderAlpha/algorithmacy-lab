# AGENTS.md — org_frontier/survey (the human-subjects arm)

Measuring algorithmacy as a lived competence through self-report from workers inside a real coordination
arrangement — the measurement side of the validation gap the other arms cannot reach. A pre-registered
panel study; pre-fieldwork, no data collected yet. The shared rules live in the root
[`../../AGENTS.md`](../../AGENTS.md).

## Remote visibility

Before the first edit: `git fetch --all --prune`, read `git branch -r --sort=-committerdate` and
`gh pr list --state open`, create a branch off `origin/contrib`, and `git push -u origin <branch>`.
Commit and `git push` the instrument and hypotheses before any data, and push again after every later
artifact. Re-check open branches and pull requests while working. The full rule is **Remote
visibility** in the root [`../../AGENTS.md`](../../AGENTS.md). Do not push to `main` or `contrib`.

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

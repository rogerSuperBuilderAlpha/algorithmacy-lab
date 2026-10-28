# AGENTS.md — org_frontier/qualitative (the empirical arm)

Reading real coordination settings against the lab's pre-disclosed priors, on the questions of process and
meaning that fieldwork answers. The shared rules live in the root [`../../AGENTS.md`](../../AGENTS.md).

## Remote visibility

Before the first edit: `git fetch --all --prune`, read `git branch -r --sort=-committerdate` and
`gh pr list --state open`, create a branch off `origin/contrib`, and `git push -u origin <branch>`.
Commit and `git push` the coding scheme before fieldwork, and push again after every later artifact.
Re-check open branches and pull requests while working. The full rule is **Remote visibility** in the
root [`../../AGENTS.md`](../../AGENTS.md). Do not push to `main` or `contrib`.

## Local entry points

- [`README.md`](README.md) — the arm. [`METHODS.md`](METHODS.md) — the methods.
  [`TOPICS.md`](TOPICS.md) — the open agenda.
- [`template/`](template/) — copy this to start a study at `org_frontier/qualitative/<slug>/`.
- A study may stand alone as a thick description, or take one arrangement through the
  [field protocol](../field/PROTOCOL.md) to a Φ verdict.

## Add a study and verify

- Commit the coding scheme, interview guide, and bit calibration **before** the fieldwork, so the git
  history shows the questions were fixed before the answers.
- A qualitative study computes no number, so it registers nothing in `ci/reproduce.json`. The
  `directory-current` gate confirms it is indexed once you run `python tools/build_index.py` (then its
  `--check`).
- Prose follows the house style in [`../../CLAUDE.md`](../../CLAUDE.md).

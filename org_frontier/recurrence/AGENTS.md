# AGENTS.md — org_frontier/recurrence (behavior paired with Φ)

Pairing exact Φ with cross-recurrence quantification: Φ reads a coordination model's structure,
cross-recurrence reads a run of it. The shared rules live in the root [`../../AGENTS.md`](../../AGENTS.md).

## Remote visibility

Before the first edit: `git fetch --all --prune`, read `git branch -r --sort=-committerdate` and
`gh pr list --state open`, create a branch off `origin/contrib`, and `git push -u origin <branch>`.
Commit and `git push` after every experiment script, findings file, or registered number. Re-check
open branches and pull requests while working. The full rule is **Remote visibility** in the root
[`../../AGENTS.md`](../../AGENTS.md). Do not push to `main` or `contrib`.

## Local entry points

- [`README.md`](README.md) — the arm. [`CONCEPTS.md`](CONCEPTS.md) — what each measure indexes and how Φ
  and CRQA differ.
- [`crqa.py`](crqa.py) — the measures and the trajectory generator; build experiments on this and the
  existing Φ harnesses rather than rebuilding them.

## Add an experiment and verify

- Each experiment script is seeded so its numbers reproduce; its findings go in a paired markdown file.
- The pre-commitment and report-the-nulls rules apply as in the computational program.
- Register every reported number in [`../../ci/reproduce.json`](../../ci/reproduce.json) and run
  `python ci/reproduce.py` from the repo root; mark a long sweep `"slow": true`.
- Run `python tools/build_index.py` so the experiment is indexed, then its `--check`.

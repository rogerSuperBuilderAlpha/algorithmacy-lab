# AGENTS.md — org_frontier/research (the literature watch)

A standing bibliography and review for each of the six programs, refreshed so new work is caught as it
appears. The shared rules live in the root [`../../AGENTS.md`](../../AGENTS.md). This note covers the
watch's local workflow.

## Remote visibility

Before the first edit: `git fetch --all --prune`, read `git branch -r --sort=-committerdate` and
`gh pr list --state open`, create a branch off `origin/contrib`, and `git push -u origin <branch>`.
Commit and `git push` after every program appended and again after the changelog and indexes.
Re-check open branches and pull requests while the sweep runs. The full rule is **Remote visibility**
in the root [`../../AGENTS.md`](../../AGENTS.md). Do not push to `main` or `contrib`.

## The two modes

Both are spelled out in [`DAILY_REFRESH.md`](DAILY_REFRESH.md), and the daily cron fires the first:

- **Daily sweep (default):** per program, read the last-run date from the metadata line in
  `literature/deep_research_report.md`, search the seed question for work dated after it, verify each
  DOI / arXiv ID / URL, dedupe against the existing `references.bib`, and append only new entries. Bump
  the metadata date and counts in place. No review is rewritten.
- **Deep refresh (periodic):** re-research every program and topic and rewrite the reviews and
  bibliographies from scratch. Monthly or on demand.

## Layout

One directory per program (`computational/`, `field/`, `qualitative/`, `recurrence/`, `survey/`,
`cognition/`), each with a `README.md`, a `REVIEW.md`, `literature/{deep_research_report.md,
references.bib}`, and ten `topics/NN_<slug>/`. [`INDEX.md`](INDEX.md) is generated;
[`CHANGELOG.md`](CHANGELOG.md) logs every run.

## Verify

- Every bibliography entry carries a resolvable identifier; drop what cannot be verified, never guess.
- Append a dated `CHANGELOG.md` entry (per program, the count added and the new total; `+0` when nothing
  new).
- Regenerate both indexes and confirm the checks:
  `python org_frontier/research/build_research_index.py --check` and `python tools/build_index.py --check`.

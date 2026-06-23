# Research monitoring — a standing literature watch for each program

A live bibliography and literature review for each of the lab's six programs, refreshed daily so new work is
caught as it appears. Each program carries a program-level review and bibliography and a decomposition into
ten topics, each topic with its own review and bibliography. The [landscape survey](../landscape/) was a
one-time sweep of how the world uses PyPhi; this is the recurring counterpart, run across every program and
kept current.

## What is here

- [`INDEX.md`](INDEX.md) — the generated master index: every program, its ten topics, the source counts, and
  the date each was last refreshed. Built by [`build_research_index.py`](build_research_index.py).
- [`CHANGELOG.md`](CHANGELOG.md) — a dated log of every refresh: the papers added and removed and the
  per-track counts, so the history of what the watch caught is legible at a glance.
- [`DAILY_REFRESH.md`](DAILY_REFRESH.md) — the playbook the daily run follows: the six seed questions, the
  research and verification procedure, and how the outputs are written and landed.
- One directory per program — `computational/`, `field/`, `qualitative/`, `recurrence/`, `survey/`,
  `cognition/` — each with a `README.md` (scope and the ten topics), a `REVIEW.md` (the curated synthesis),
  `literature/{deep_research_report.md, references.bib}`, and `topics/NN_<slug>/{REVIEW.md, references.bib}`.

## How a refresh works

Each run does deep research per program and per topic: real search across the web and the academic databases,
a synthesis written to the review, and a bibliography written to the `.bib` file. Every program-level report
opens with a metadata line the index reads:

```
<!-- run: YYYY-MM-DD | sources: N | verified: M -->
```

A full refresh overwrites the reviews and bibliographies in place. Nothing is lost: git history holds every
prior version, and [`CHANGELOG.md`](CHANGELOG.md) records what each run added and removed.

## The integrity rules

The lab's bibliographies carry only real, verifiable sources, and the watch holds to that.

- **Every bibliography entry carries a resolvable identifier** — a DOI, an arXiv ID, or a stable publisher
  URL. An entry that cannot be verified is dropped, not guessed.
- **Claims are checked before they land.** Each run pairs the research with an adversarial verification pass
  that confirms the cited identifiers resolve and the claims attributed to them hold.
- **The prose follows the house style** in the repo [`CLAUDE.md`](../../CLAUDE.md), and each review states its
  search method and run date.

## The six programs

The programs are the ones the [main directory](../../README.md) names: the computational core and the five
arms that carry it onto real coordination and into cognitive theory. Each program's `README.md` states the
literature its watch covers and lists the ten topics the program-level research identified.

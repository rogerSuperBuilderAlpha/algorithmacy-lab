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
- [`DATA_SOURCES.md`](DATA_SOURCES.md) — where the community can get real data for the empirical questions: verified open datasets and repositories per research line, with the runnable-now starting points flagged.
- [`CROSS_TRACK_CONCEPTS.md`](CROSS_TRACK_CONCEPTS.md) — the ten concepts the six tracks share, read off the
  per-paper reference cards (`*/literature/cards/`, indexed by each program's `REFERENCES.md`).
- Per-paper **reference cards** under `<program>/literature/cards/<citekey>.md` — a summary, the key facts,
  critical notes, and topics for each reference whose open-access full text was acquired. PDFs are gitignored
  and refetchable from each program's `literature/pdfs.manifest.json` (status, OA source, `source_url`,
  `sha256`). The cards are built by acquiring the OA PDF ([`oa_acquire.py`](oa_acquire.py)) and writing a
  card with an independent adversarial verify pass. A reference with no free full text is left uncarded and
  recorded in the manifest.
- [`card_backfill.py`](card_backfill.py) — the on-demand backfill: `python card_backfill.py` retries OA
  acquisition over every uncarded reference and reports which have become open-access; `--write` downloads
  the new PDFs and stages a card-writing config. Run it to pick up papers that were paywalled at first pass
  and have since opened (a preprint posted, an embargo lifted), then write their cards and land as usual.
- One directory per program — `computational/`, `field/`, `qualitative/`, `recurrence/`, `survey/`,
  `cognition/` — each with a `README.md` (scope and the ten topics), a `REVIEW.md` (the curated synthesis),
  `literature/{deep_research_report.md, references.bib}`, and `topics/NN_<slug>/{REVIEW.md, references.bib}`.

## How a refresh works

The watch runs in two modes, both spelled out in [`DAILY_REFRESH.md`](DAILY_REFRESH.md).

The **daily sweep** is what the cron fires. It searches each program's seed question for work dated after
that program's last run, verifies the hits, and appends the new ones to the bibliography. The reviews stay
as they are. Every program-level report opens with a metadata line the index reads, and the sweep updates
its date and counts in place:

```
<!-- run: YYYY-MM-DD | sources: N | verified: M -->
```

The **deep refresh** re-researches every program and topic and rewrites the reviews and bibliographies from
scratch, catching reframings and displaced topics an append-only sweep misses. It runs on a monthly or
on-demand cadence. Nothing is lost in either mode: git history holds every prior version, and
[`CHANGELOG.md`](CHANGELOG.md) records what each run caught.

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

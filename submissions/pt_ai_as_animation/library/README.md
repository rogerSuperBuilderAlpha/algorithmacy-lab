# pt_ai_as_animation library (run `pta-lib-2026-11`)

> **[Built by Claude, 2026-11-08.]** Every card here is drafted by Claude or a Claude subagent, not by
> the author. A card is a research note: it records what a source says, which version was read, and
> what the paper uses it for. It is not manuscript prose.

One card per work the paper (`../SKETCH.md`) may cite that no existing lab library already holds.
Works other libraries hold are not re-carded; `POINTERS.md` lists them by facet. The thesis is the
author's text in `../SOURCE.md`. The convention, card schema and tools are the dxd_animation library's
(`L/submissions/dxd_animation/library/`, run `dxda-lib-2026-11`, branch `research/dxd-animation-library`),
itself copied from the Peircean-triad library. The run plan was drafted by Fable on 2026-11-08.

Path prefixes: `L/` = `~/iit-playground/pyphi-experiments/` (public); `D/` = `L/dissertation/`
(**private** nested repo).

## Layout

| Path | What | Stage |
|---|---|---|
| `CITED_WORKS.md` | every work `../SKETCH.md` names: registry hit, verdict new / pointer / upgrade | S0 |
| `FACETS.md` | facets: claims served, queries, anchors (each confirmed by a record), targets | S1 |
| `SEARCH_LOG.md`, `search/F*.jsonl` | every query: date, facet, source, n, top ids | S2 |
| `triage/*.md`, `triage/DECISIONS.md` | shortlists and the approved list | S3 |
| `FETCH_LOG.tsv`, `HELD_COPIES.tsv`, `BROWSER_LIST.md` | fetch outcomes; works only the author can open | S4 |
| `cards/<key>.md` | one card per work, written by hand (Claude or a subagent), never by script | S5–S6 |
| `HAND_CHECK.md`, `hand_check/` | Fable's read of every card against its source, before indexing | S7 |
| `POINTERS.md`, `INDEX.md`, `TRACKER.tsv`, `references.bib`, `REFERENCES_APA.md`, `DOI_CHECK.md`, `QUOTE_CHECK.md` | index and checks | S8 |
| `CRITIC.md`, `GAP_CHECK.md` | coverage against the sketch; prior work that already makes the argument | S9 |
| `RUN_REPORT.md` | what ran, counts, what needs the author's decision | S10 |
| `tools/` | copied 2026-11-08 from the dxd_animation library; local paths point to `pt_ai_animation_local`; registry adds library `pta` | S0 |

Outside the repo, in `~/iit-playground/pt_ai_animation_local/`: `registry.tsv` (every key in the lab
libraries, for de-duplication; it names private paths, so it is never committed), `pdfs/<key>/`,
`inbox/` (the author's browser downloads), `consensus/`.

## Guards (author's ruling, 27 Oct 2026)

No card from model memory. Every quotation carries a locator. An independent verifier (writer ≠
verifier) re-checks every card. Fable reads every card against its source before it is indexed.
Paywalls are never bypassed; those works go to `BROWSER_LIST.md`.

## Claims

| tag | claim | § |
|---|---|---|
| c1 | a working AI is the LLM plus harnesses, VMs, efficiencies | §1, §4.1 |
| c2 | model-centrism misplaces where the intelligence sits | §1, §4.1 |
| c3 | neither life nor intelligence has a consensus definition; defend a theory | §2 |
| c4 | an organizational account of life fits the system around the LLM | §2 |
| c5 | intelligence frame versus life frame is a stance choice | §2, §6 |
| c6 | animation is the craft of composing a living character from inert parts | §3 |
| c7 | necessary opacity: no frame holds the motion, no component the intelligence | §4.2 |
| c8 | co-optation: dependency grows with use; the viewer is co-opted | §4.3 |
| c9 | triadicity, narrowed (Checkpoint B): the studio *determines* what the viewer gets; distinguished from Schumann & Du 2022 and Clark & Fischer 2023 by the lab criterion | §4.4 |
| c10 | the analogy breaks at liveness; puppetry; the LLM makes its own in-betweens | §5 |
| c11 | implementation and evaluation under the life frame | §6 |
| c12 | gap (Checkpoint B): AI development as a craft of animation, argued as a claim about what AI is: not the interface (Stark 2024), not the illusion (Govind 2026), not an ALife experiment (OpenLife, Masumori et al. 2026) | §1, §7 |

## Facets

F1 philosophy of life · F2 organizational/autopoietic accounts · F3 intelligence and the intentional
stance · F4 animation production pipeline · F5 puppetry, performance capture, liveness · F6 animacy
and apparent motion · F7 epistemic opacity · F8 compound AI vs model-centrism · F9 co-optation,
lock-in, suspension of disbelief · F10 triadicity · F11 LLMs as characters · F12 venue (*P&T*
2019–2026) · G gap check. Details in `FACETS.md`.

## Card schema (copied 2026-11-08 from the dxd_animation library README; run id and paths changed)

## Keys

`firstauthorsurnameYEARfirsttitleword`, lowercase ASCII, articles skipped, diacritics folded. A key
must not exist in the registry unless the card declares the earlier card under `prior_cards`. A
collision takes a title word: L. Stark's FAccT paper is `stark2024animation`, because `stark2024` and
`stark2024principles` are D. Stark and Vanden Broeck.

## Frontmatter

```yaml
---
key: stark2024animation
apa: "Stark, L. (2024). Animation and artificial intelligence. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1663–1671). ACM. https://doi.org/10.1145/3630106.3658995"
authors: "Stark, Luke"
year: 2024
title: "Animation and Artificial Intelligence"
venue: "FAccT '24"
volume: ""
issue: ""
pages: "1663–1671"
doi: "10.1145/3630106.3658995"
url: ""
type: proceedings
facets: [F1, F3]
claims: [c4, c6, c7]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "<version, place, date, sha256>"
verified: pending
verified_against: ""
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---
```

Every field on one line; lists in brackets. Optional `registered_year` when the registry gives a
different year from the one cited.

| Field | Values |
|---|---|
| `type` | article, book, chapter, proceedings, report, thesis, preprint, web, legal, dataset, software |
| `role` | **anchor** (the claim rests on it), **support**, **contrast** (a position the paper argues against or past), **method**, **data** |
| `load` | **load-bearing** (the paper's claim depends on what the source says) or **exists** (the paper only says the work exists) |
| `read_depth` | **full_text**, **partial** (the card lists the parts read), **abstract**, **metadata** |
| `verified` | **pending**, **verified**, **corrected** (the card records the correction), **unverifiable** |
| `status` | **cited** (SOURCE.md or SKETCH.md uses it), **candidate** (the author decides), **dropped** (reason under Caution) |

## Body

Four sections in this order, then the verifier's, then Fable's.

- `## What it argues` — the work's own argument, authors as agents. Only what the read version
  supports. An abstract card says so in its first line; a metadata card says only what the registry
  record shows.
- `## What the paper uses it for` — one bullet per claim tag. If the use stretches the source, say so.
- `## Loci` — verbatim quotations, one per line, each with a page or section locator and the object it
  was matched against. Only from text actually read. Metadata and abstract cards write `None`. Inner
  quotation marks become single quotes, and the card says so.
- `## Caution` — disputes, dates, homonyms, corrections to earlier cards or to and what
  the read version lacks.
- `## Verification` — appended by the S6 verifier (a different agent from the writer): date, agent,
  verdict, what was checked, what changed.
- `## Hand-check` — appended by Fable at S7. A card is not indexed until this section exists.

## Rules

1. No quotation, page, author, year or DOI enters a card unless it was seen in the source or the
   registry record **this run**. Nothing from model memory. Something seen only in an earlier card or
   reference list stays out or is marked unchecked.
2. Name the object read: version, place, date, sha256.
3. Where an earlier card, `../SKETCH.md` is wrong, record it under Caution and leave
   that file alone.
4. Articles take the volume year; set `registered_year` when the registry differs.
5. Cards are plain English with named agents and active verbs. They are never generated by a script.
6. A work that could not be read gets a metadata card with `## Loci` = None.
7. A non-English source (Wertheimer 1912) is quoted in the original first, with an English gloss
   marked "[my translation]".
8. Never bypass a paywall, bot wall or captcha. A blocked work goes to `BROWSER_LIST.md`.
9. No PDF, EPUB or text layer is written under the repo.
10. The author's wording in `../SOURCE.md` is never edited.

## Tools

- `python3 -I tools/build_registry.py` — rebuild the de-duplication registry (outside the repo).
- `python3 -I tools/search.py Fn --from FACETS.md` — run a facet's queries; append to `search/`.
- `python3 -I tools/fetch.py …` — Crossref record + open copy into the local folder; `FETCH_LOG.tsv`.
- `python3 -I tools/show_record.py KEY` — print a fetched registry record.
- `python3 -I tools/build_index.py [--check]` — schema check and index outputs.
- `python3 -I tools/check_dois.py [KEY ...]` — writes `DOI_CHECK.md`.
- `python3 -I tools/quote_check.py [KEY ...]` — writes `QUOTE_CHECK.md`.

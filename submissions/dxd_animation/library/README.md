# dxd_animation library (run `dxda-lib-2026-11`)

> **[Built by Claude, 2026-11-05.]** Every card here is drafted by Claude or a Claude subagent, not by
> the author. A card is a research note: it records what a source says, which version was read, and
> what the paper uses it for. It is not manuscript prose.

One card per work the paper (`../OUTLINE.md`) may cite that no existing lab library already holds.
Works the other libraries hold are not re-carded; `POINTERS.md` lists them by facet. The thesis is the
author's text in `../SOURCE.md` (Pass 2 governs). The convention is the Peircean-triad library's
(`D/current/peircean_triad/library/README.md`), with this paper's facets and claims.

Path prefixes: `L/` = `~/iit-playground/pyphi-experiments/` (public); `D/` = `L/dissertation/`
(**private** nested repo); `S/` = `L/spaces/` (**private** nested repo).

## Layout

| Path | What | Stage |
|---|---|---|
| `CITED_WORKS.md` | every work SOURCE/OUTLINE/CHECK cite: existing key, path, depth, pointer-or-new | S0 |
| `FACETS.md` | the facets: claims served, queries, anchors, targets | S1 |
| `SEARCH_LOG.md`, `search/F*.jsonl` | every query: date, facet, source, n, top ids | S2 |
| `triage/*.md`, `triage/DECISIONS.md` | shortlists and the approved list | S3 |
| `FETCH_LOG.tsv`, `BROWSER_LIST.md` | fetch outcomes; works only the author can open in a browser | S4 |
| `cards/<key>.md` | one card per work, written by hand (Claude or a subagent), never by script | S5–S6 |
| `HAND_CHECK.md` | Fable's read of every card against its source, before indexing | S7 |
| `POINTERS.md`, `INDEX.md`, `TRACKER.tsv`, `references.bib`, `REFERENCES_APA.md`, `DOI_CHECK.md`, `QUOTE_CHECK.md` | index and checks | S8 |
| `CRITIC.md`, `GAP_CHECK.md` | coverage against the outline; prior work that already makes the argument | S9 |
| `RUN_REPORT.md` | what ran, counts, what needs the author's decision | S10 |
| `tools/` | copied from `D/current/peircean_triad/library/tools/` with paths changed (see each file's docstring) | S0 |

Outside the repo, in `~/iit-playground/dxd_animation_local/`: `registry.tsv` (every key in the 12
lab libraries, for de-duplication; it names private paths, so it is never committed), `pdfs/<key>/`
(PDF or HTML, its `.txt` text layer, the registry record, `provenance.txt` for copies taken from
`S/notebook_sources/`), and `inbox/` (the author's browser downloads).

## Claims

| tag | claim | outline § |
|---|---|---|
| c1 | a moving goal breaks conversion-era design (raincoat → umbrella) | §1, §2 |
| c2 | the user is human: biological, cognitive, emotional; agent experience bracketed | §3.1 |
| c3 | the platform environment is opaque, co-optive and triadic | §3.2 |
| c4 | an LLM interface is an animation (L. Stark; Silvio) | §3.3 |
| c5 | animation is opaque: missing frames; the interstices are the craft | §4.1 |
| c6 | animation is co-optive: the viewer locks in; the user also animates | §4.2 |
| c7 | animation is triadic: viewer, character, animator, against the dyad | §4.3 |
| c8 | DXD must apply the animator's methods rather than hide frames or expose the backend | §5 |
| c9 | gap: no prior work frames LLM interfaces as animation for decision design | §6 |

Facets F1–F10 and G are defined in `FACETS.md` and in `tools/build_index.py`.

**Run 2 (`dxda-lib-2026-11b`, from 2026-11-11).** The paper became a model paper (`../SOURCE.md`, Pass 3;
rulings in `triage/DECISIONS.md`, "Run 2"). Run 2 adds facets F11–F13 and G2 and the model's claims
m1–m7 (in `tools/build_index.py`; the model itself is `../MODEL.md`). Run-1 cards keep their c-tags.

| tag | claim of the model |
|---|---|
| m1 | opaque row: idempotent interpretation; staging and labelled sources |
| m2 | co-optive row: intent specification; key poses and instructions to other hands |
| m3 | triadic row: intuitive governance tracking; anticipation and change between moves |
| m4 | transfer warrant: craft carries over only through an account of the receiver |
| m5 | dissociation: craft spent on the character versus craft spent on the decision |
| m6 | boundary: the model applies where an intermediary binds a counterpart |
| m7 | gap: no prior model selects animation craft through decision competencies |

| facet | name |
|---|---|
| F11 | The animator's craft: principles, keys and in-betweens, timing, staging |
| F12 | Animation principles carried to interfaces, robots and agents |
| F13 | Competence and intuition under opaque, changing rules |
| G2 | Gap check 2: prior work selecting animation craft for decision design |

In run 2 every agent ran on the session's model (Fable 5.2 at first, Opus 5.5 from 11 Nov at the
author's switch). A card's writer and its verifier are different agents; the lead reads every card
against its source before it is indexed.

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
added: 2026-11-05
run: dxda-lib-2026-11
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
| `status` | **cited** (SOURCE.md or OUTLINE.md uses it), **candidate** (the author decides), **dropped** (reason under Caution) |

## Body

Four sections in this order, then the verifier's, then Fable's.

- `## What it argues` — the work's own argument, authors as agents. Only what the read version
  supports. An abstract card says so in its first line; a metadata card says only what the registry
  record shows.
- `## What the paper uses it for` — one bullet per claim tag. If the use stretches the source, say so.
- `## Loci` — verbatim quotations, one per line, each with a page or section locator and the object it
  was matched against. Only from text actually read. Metadata and abstract cards write `None`. Inner
  quotation marks become single quotes, and the card says so.
- `## Caution` — disputes, dates, homonyms, corrections to earlier cards or to `../CHECK.md`, and what
  the read version lacks.
- `## Verification` — appended by the S6 verifier (a different agent from the writer): date, agent,
  verdict, what was checked, what changed.
- `## Hand-check` — appended by Fable at S7. A card is not indexed until this section exists.

## Rules

1. No quotation, page, author, year or DOI enters a card unless it was seen in the source or the
   registry record **this run**. Nothing from model memory. Something seen only in an earlier card or
   reference list stays out or is marked unchecked.
2. Name the object read: version, place, date, sha256.
3. Where an earlier card, `../CHECK.md` or `../OUTLINE.md` is wrong, record it under Caution and leave
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

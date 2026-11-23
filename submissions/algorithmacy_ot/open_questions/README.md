# OT open-questions run, `ot-oq-2026-11`

> **[Written by Claude, the run's lead, 22 Nov 2026.]** Protocol for this run. The approved plan is at
> `~/.claude/plans/ok-i-want-you-curried-pumpkin-of-5549facb-8130-42d5-8697-8054667dfe73.md`; Fable
> built it and assigned each task to a model.

## Purpose

The author asked for a reading of everything *Organization Theory* has published since early 2023, with
attention to the questions each piece leaves open, so that the algorithmacy paper can be framed as an
answer to one of them. The coordination framing has not drawn the response the author wants. This run
finds the conversations OT authors are having, tests which ones others have picked up, and recommends
up to three entry points. It writes no manuscript prose.

## Corpus

Every item *Organization Theory* has published from volume 4(1) (2023) to the harvest day, OnlineFirst
included, of every type: theory and review articles, Controversies and Conversations pieces, editorials,
introductions and commentaries. `CORPUS.tsv` lists them.

## Rules

1. **No record from model memory.** A record rests on a text read this run. Every quotation carries a
   page or section locator and names the sha256 of the object read.
2. **Two checks.** A different agent verifies every record (S5). Fable reads every record against its
   source before it is indexed (S7). If Fable is rate-limited, the queue waits.
3. **Public repo.** PDFs, text layers, contents pages and sweep snippets stay in
   `~/iit-playground/ot_open_questions_local/`. Records quote at most 60 words per quotation and 800
   words per article.
4. **The manuscript stays the author's.** Nothing under `manuscript/` is written. Framing notes describe
   moves and never supply replacement sentences.
5. **No contact with the journal.** No forms, ScholarOne, email or access requests. A Cloudflare or
   sign-in challenge stops the lead, and the author clears it.
6. **Readers extract blind.** S4 readers never see `ALGORITHMACY_BRIEF.md`.
7. **Privacy.** Tools send a generic User-Agent. Searches use the vocabulary of the question being
   traced, never the author's name, title or sentences.
8. **Git.** Branch `research/ot-open-questions`. The author granted standing approval (22 Nov) to commit
   and push at stage boundaries. Records only; nothing merges without the author.

## Stages and models

| Stage | Output | Model |
|---|---|---|
| S0 Protocol | `README.md`, `BASELINES.md`, `ALGORITHMACY_BRIEF.md`, `DECISIONS.md`, `tools/` | lead |
| S1 Corpus | `CORPUS.tsv`, `CORPUS_LOG.md` | haiku (Crossref/OpenAlex); lead (SAGE pages in Chrome) |
| S2 Tiering | `TIERS.md` | opus |
| S3 Fetch | `FETCH_LOG.tsv`, `SWEEP_COUNTS.tsv` | lead (Chrome); haiku (hashes, text layers, sweep) |
| S4a Pilot | five control records | opus, sonnet |
| S4b Readers | `records/<key>.md` | opus (Tier A), sonnet (Tier B) |
| S5 Verifiers | `verify/VERIFY_V0n.md` | opus, never the record's reader |
| S6 Fit | `fit/FIT_A.tsv`, `fit/FIT_B.tsv` | opus ×2, blind to each other |
| S7 Hand-check | `hand_check/HC_Hn.md` | fable |
| S8 Index | `INDEX.md`, `QUESTIONS.tsv`, `EDGES.tsv`, `DOI_CHECK.md`, `QUOTE_CHECK.md` | haiku |
| S9 Synthesis | `synthesis/CONVERSATIONS.md`, `RECURRENCE.tsv`, `SHORTLIST.md` | fable and opus cluster apart; fable reconciles |
| S10 Pick-up | `pickup/` | haiku, sonnet, opus; fable checks |
| S11 Critics | `critic/CRITIC.md` | opus ×3; fable rules |
| S12 Checkpoint | `REPORT.md` | lead; fable traces |

## Record schema

Frontmatter: key, apa, doi, volume, issue, published_online, band (window or look-back),
article_type_printed, article_type_norm, exchange_id, license, read_depth, object_read (file and
sha256), reader_model, verified, hand_check, closing_form (dedicated section, distributed, question
list, none), topic_flags, run.

Body:

- **What it argues**, 150 words or fewer.
- **The conversation it joins**: the literature it positions against (quoted, with locator), its named
  interlocutors, the OT articles it cites, and its move.
- **Key constructs**: term, verbatim definition with locator, coined or borrowed.
- **Open questions**, numbered `OQ-<key>-nn`: verbatim quotation and locator; form (explicit question,
  future-research call, limitation, boundary condition, invitation, editor's call); scope; addressee;
  level of analysis (individual, interaction, organization, field); a one-sentence paraphrase marked as
  the reader's. Readers extract from the whole text, not only the closing section. A paper that states
  none gets "none stated".
- **Implicit openings**: at most three, marked as the reader's inference.
- **Topic flags**, each scored 0, 1 (in passing) or 2 (central), with a located quotation above 0:
  triads or third parties, intermediaries, algorithms and AI, platforms, coordination, communication,
  literacy or competence, evaluation and accountability.
- **Caution**; then **Verification**, **Fit** and **Hand-check**, appended by later stages.

**Fit scale.** 0 no contact · 1 shared vocabulary only · 2 adjacent and citable, answers no stated
question · 3 answers part of a stated question, or all of it after a reframing the asker would likely
accept · 4 answers a quoted question at the asker's level of analysis without changing the brief's
definition.

## Synthesis rules

A conversation is *recurring* only if two papers by different first authors ask it, or one paper and an
editorial. `RECURRENCE.tsv` reports support in separate columns: articles, commentaries, editor signal,
distinct volumes, citation edges among askers, months since last asked. The coordination cluster is
reported whatever its size.

## Gates

- **Gate 0** (22 Nov): settled; see `DECISIONS.md`.
- **Gate 1**: the author reads `REPORT.md` and picks an entry point, none, or a deeper read. Nothing
  touches the manuscript before then.

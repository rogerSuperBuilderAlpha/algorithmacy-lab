<!-- DRAFTED BY CLAUDE (Opus 5.5), begun 13 Nov 2026, for Roger and Pierre. A running log of every call made during the v8 rebuild. Entries marked YOURS wait for the authors. The approved plan is ~/.claude/plans/ok-so-we-need-zippy-journal.md. -->

# Decisions log: the v8 rebuild

v8 keeps v7's thesis and research, restores Pierre's insights in his own words wherever they still hold, places the paper in the phygital hospitality literature, and is written to the model of Germann Molz (2018), *Hospitality & Society* 8:3, 229–251, doi 10.1386/hosp.8.3.229_1.

## The brief (Roger's answers, 13 Nov 2026)

| Question | Answer |
|---|---|
| How does v8 enter the phygital literature? | v7's thesis and order stay. A phygital layer is added to the abstract, introduction, definitions and conclusion, with a short section tying the argument to the special issue's call. Pierre's concepts return as named parts of v7's steps. |
| What about closed phygital sources? | Obtain them through the Bentley library sign-in and read them in full before they carry a claim. |
| How is Pierre's original kept? | His own sentences, verbatim and marked, wherever they survive v7's claim audit and the reviewers' objections; rewritten only where the law or a reviewer requires, with the reason logged. Every one of his roughly forty insights gets a recorded outcome. |
| How closely does v8 follow the model? | Fully: its structure, pacing and register, including first-person stance and occasional questions. |

Roger also supplied, on 13 Nov, a review of v7 against the model paper (four benchmarks: house style; scenes, thesis and roadmap; plain topic sentences and scholars introduced with a tag; bridges and takeaway paragraphs, without note-like phrasing) and a rewritten abstract, which sets the floor for clarity. Both are recorded in the plan.

## Conflicts flagged before starting

1. **The skill's rule that the draft supplies no words.** `sentence-by-sentence` takes claims from the draft and words from the model. Roger's decision that Pierre's sentences enter verbatim overrides it for Pierre's text only. v7's prose is Claude's, and the skill's rule holds for it: v7 supplies claims, not words.
2. **Transcribing the model.** The skill's Stage 2 transcribes every model sentence. The article is under copyright and the repository is public. As in v6 (`rewrite_2026-11/DECISIONS.md`, conflict 3), the full transcription is kept in the git-ignored corpus folder (`rewrite_2026-11/journal/corpus/germannmolz2018/TRANSCRIPT.md`), and the committed `MODEL.md` holds locators, opening and closing words, frames and analysis.
3. **`REGISTER.md` and v6's choice of model.** v6's `PROPOSAL.md` rejected Germann Molz (2018) as a model because its conversational register is the one Reviewer 3 objected to in v4, and `REGISTER.md` bars rhetorical questions in running prose. Roger chose to follow her register fully. Both rules are set aside for v8. The moves Reviewer 3 named stay out: the second-person anecdote, 'boring', 'condemns … blesses', 'bite' and 'sitting ducks'.
4. **The journal's AI policy** (`JOURNAL_SPEC.md`: AI only to 'enhance readability and language'). v8 is drafted by Claude except where Pierre's sentences stand. This stays open for the authors, as in v7 (REPORT §6, item 1). **YOURS.**
5. **The locked abstract.** `AGENTS.md` asks agents not to change the core claims of the locked `ABSTRACT.md` (AI as a constitutive mediator) without an explicit request. v7 departed from it. v8 restores the constitutive-mediator framing as part of the phygital layer, so v8 moves back toward the locked abstract.

## Standing rules

- Every citation, quotation and number is checked against a card or a source read in this session. Nothing is cited from memory.
- A source reached only by its abstract is marked 'abstract only' and carries no claim beyond the abstract.
- No script writes prose. Scripts count, check and copy.
- I do not type passwords or click bot checks. Roger signs in to the Bentley proxy himself.
- Push after every stage, merging the atlas bot's snapshot commits rather than rebasing.

## Log

### V8-D1 · 13 Nov · Branch and workspace
Branch `submission/hospitality-v8`, cut from `origin/contrib` (which holds v7 through PR #884). Workspace `manuscript/v8_2026-11/`. Full texts and the model transcription go in git-ignored folders.

### V8-D2 · 13 Nov · v7 frozen
SHA-256 at the start of v8: `DRAFT_v7.md` 3a242132016ccfc3abc1eef5ca71a081595f6c8c48115a3ec3eea012a0951fae; `keystone_2026-11/sbs/LEDGER.md` 634e555af74e7f33e886769e7b9088bc16fd2f426cdc14c364021a54212b2af3; `keystone_2026-11/sbs/assembly/final.json` 23cc607a90579ccb5200fcd313071fa1dbc8e11b345376f3be33bc9f96a24029. None of these files is edited.

### V8-D3 · 13 Nov · The assembly scripts
`keystone_2026-11/sbs/assembly/assemble.py` and `build_letters.py` read from a scratchpad path that no longer lasts, and hard-code v7's paragraph starts, headings and inserts. v8 gets its own copier in `v8_2026-11/assembly/` once v8's structure exists (stage 6), built from these and reading only files in the repository.

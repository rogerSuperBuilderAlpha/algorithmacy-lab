<!-- DRAFTED BY CLAUDE (Fable 5.2), begun 10 Nov 2026, for Roger and Pierre. A running log of every call Claude makes during the v6 rebuild, kept because the authors chose "no stops". Newest entries at the bottom. -->

# Decisions log: the v6 rebuild

This log exists because you chose to review at the end. Each entry gives the call, the alternative, and the reason. Entries marked **YOURS** are calls I could not make; they wait for you and block nothing.

## The brief (your answers, 10 Nov 2026)

| Question | Your answer |
|---|---|
| Whose sentences are in v6? | Claude writes all of v6. v4 (`DRAFT.md`) and v5 (`DRAFT_v5.md`) stay untouched. |
| How deep is the method? | Sentence by sentence, following `~/.claude/skills/sentence-by-sentence/`. |
| Where do I stop for you? | Nowhere. I make each recommended call and log it here. |

The approved plan is `~/.claude/plans/crystalline-tickling-reef.md`.

## Conflicts flagged before starting

1. **Journal AI policy.** `JOURNAL_SPEC.md` quotes the Notes for Contributors: AI "should only be used to enhance readability and language". v6 is wholly Claude-drafted. It is a working draft. The submitted text and the AI acknowledgment are yours, and the acknowledgment has to describe what happened. **YOURS.**
2. **"Keep my wording."** Your standing rule is overridden for v6 by your request of 10 Nov. Nothing in v4 or v5 changes.
3. **Verbatim transcription of the model.** The skill's Stage 2 says to transcribe every model sentence. The repository is public and the model article is under copyright. Each `MODEL.md` entry therefore carries a locator, the sentence's opening and closing words, and only the short frame that performs the move. Every sentence still gets its own numbered entry. Full texts stay in the gitignored `journal/corpus/`.
4. **`REGISTER.md`.** Its August rules (no roadmap paragraph, first person once, parenthetical citation by default) were measured on Lugosi (2021, *Tourist Studies*) and Lynch et al. (2021, a decade review). Where the journal sample is unanimous, v6 follows the journal and I record the departure here. `REGISTER.md` itself is left as the record for v4.
5. **Choice of model.** The skill says the author chooses. Under "no stops" I choose, with reasons, in `PROPOSAL.md`.

## Standing rules I am holding to

- Every citation, quotation and number is checked against a card or a source read in this session. Nothing is cited from memory.
- A source reached only by its abstract is marked "abstract only" and carries no claim beyond the abstract.
- No script writes prose. `wordcount.py`, `check_citations.py`, `preflight.py` and `render_refs.py` are used for counting and consistency only.
- I do not type passwords or click bot checks. Closed articles wait for your Bentley sign-in.

## Log

### D1 · 10 Nov · Workspace
`manuscript/rewrite_2026-11/`, with `journal/`, `research/` and `sbs/`. Full texts go in `journal/corpus/`, which is gitignored. Alternative: reuse `revision_2026-11/`. Reason: that folder is the record of the v5 round, and its file names (`OUTLINE_v2.md`, `TRACEABILITY_v2.md`) would collide.

### D2 · 10 Nov · Library sign-in not live
The proxy link for Lugosi (2014) lands on the Microsoft password page. I am starting the journal study on the open-access texts and will add the closed ones when the sign-in is done. If it never is, `JOURNAL_MODEL.md` will say which texts it rests on and which it lacks.

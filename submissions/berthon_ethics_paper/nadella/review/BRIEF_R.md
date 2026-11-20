# Brief for the R-round review of concepts and arguments

*Written by Claude (the lead) on 2026-10-24 from the plan the author approved the same day. Every R agent reads this
file and `../facets/BRIEF.md` first. None of the text is the author's.*

## What this round is for

The paper is drafted (`../manuscript/DRAFT_v1.md`, about 8,300 words, for *Business Ethics Quarterly*). Its argument
is `../ARGUMENT_AND_OUTLINE.md` v2 (A1–A8 → CA; B1–B3 → CB). Its concepts are the rows of
`../../consolidation/CONCEPT_LEDGER.md`. The N round (`../facets/`, audited in `AUDIT_N7a.md`, `AUDIT_N7b.md`,
adjudicated in `ADJUDICATION.md`) built the card library in `../../literature/cards/berthon_ethics_paper/`.

This round asks a different question: **is each concept used the way the scholars who own it use it, and does each
argument step hold?** A review that finds nothing wrong is suspect. Report what sinks or narrows a claim plainly.

**You review substance, never prose.** Do not comment on wording, style, flow, sentence length or tone, and do not
propose replacement sentences. The paper will be rewritten by the lead against a model essay; your job is to say
which claims and concepts survive and in what form.

## Rules

All rules in `../facets/BRIEF.md` §6 apply unchanged (exact quotation with locator; never invent; Crossref without
`mailto`; never send an email address anywhere; no Unpaywall; no paywall, bot-wall or CAPTCHA circumvention; no
Chrome tools; downloads read with `python3 -I`; Nadella's post quoted at most two sentences, by P-number; the Saenger
rule). The card format and quotation floor are BRIEF.md §4, with `facet: R<n>`.

## Where you may write

- `review/R<n>_<stem>.md` and `review/R<n>_<stem>.bib`: your two files only.
- New or upgrade cards in `../../literature/cards/berthon_ethics_paper/` (grep `../../literature/CARD_INDEX.md` for key,
  DOI and title first; do not edit any existing card).
- Downloads to `~/iit-playground/berthon_ethics_local/pdfs/nadella/R<n>/`, each in its own subdirectory.

Nothing else. No git. Do not run `build_cards_index.py`.

## Review file format

1. Header: run, date, "Agent-drafted. The author has not reviewed it."
2. Scope: the ledger rows, premises and draft passages (by line number in `DRAFT_v1.md`) reviewed.
3. Search log (numbered; every query, URL, hit count, block).
4. **One entry per concept or claim reviewed**: what the draft says (line numbers, paraphrase or at most one short
   quotation); how the owning literature defines or treats it (exact quotation with locator, from a source you opened);
   the gap between them; verdict.
5. **Verdict table**, the file's last section:

| ID | Concept / claim | Draft lines | Verdict | Evidence (card + locator) | Fix to the argument |
|---|---|---|---|---|---|

Verdicts: **holds** · **narrower** (true in a smaller form; state it) · **misused** (the concept means something else
in its literature) · **contested** (a live scholarly dispute the paper must acknowledge; name both sides) ·
**unsupported** (no source carries it) · **wrong** (a source contradicts it). The "fix" column states the corrected
claim or concept, not prose.

6. Gaps and blocks, with where a Bentley library user would find each blocked source.

## The runs

| Run | Scope |
|---|---|
| R1 | Historical concepts and claims (ledger H, L rows; draft §2 and the history in the opening and §3) |
| R2 | Present-case concepts and claims (ledger M, E, I rows; draft §3; products and law as of October 2026) |
| R3 | Normative frame (ledger K, N rows; draft §1 and §4) |
| R4 | The argument's logic (A1–A8, B1–B3, CA, CB; every ledger row mapped to a premise) |
| R5 | Novelty and counter-case since the N6 search; strongest objection to each duty (ledger D, O rows) |
| R6 | Adversarial audit of R1–R5 (runs after them) |
| R7 | Shortlist of model essays for the rewrite (runs with R6) |

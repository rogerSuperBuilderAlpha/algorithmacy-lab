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

### V8-D4 · 13 Nov · Stage 1: reading the model
- **Every sentence analysed.** `MODEL.md` holds GM.001–GM.338: 332 of her sentences and six displayed quotations, one entry each, with move, role, question and thesis, register and slot. The full text sits in the git-ignored `rewrite_2026-11/journal/corpus/germannmolz2018/MODEL_FULL.md`; `tools/redact_model.py` copies it to the committed `MODEL.md` with each sentence cut to its first five and last four words (conflict 2).
- **Paragraphs from the typeset indents.** The plain text lost paragraph breaks, so they were found from first-line indents in the PDF: 67 paragraphs. The v6 reading note gave about 72; a dated correction is appended to `rewrite_2026-11/journal/notes/germannmolz2018.md`.
- **A counting script, against the skill's no-code rule.** The plan asked for measured figures in `STYLE_PROFILE.md`, and the skill forbids code. `tools/style_counts.py` counts only and writes no prose; its splitter was checked against the hand split on the model before use and corrected once (STYLE_PROFILE, 'How the figures were made'). The sentence-level analysis itself was done by reading, as the skill requires.
- **Headings.** Main headings in bold capitals, subheadings in bold italic: the typeset form, Roger's review, and the journal's 'bold' all agree with it.
- **Weight, for Stage 4.** Her theoretical context is 21% of the body (about 1,880 words at 9,000) and her method 5.6% (about 510). The plan budgeted 1,100 and 250. Stage 4 sets v8's weights against her figures and the venue band, and brings any trade-off to Roger.

### V8-D5 · 13 Nov · Stage 2: what the Bentley library reaches
Roger signed in to the Bentley library on 13 Nov. Through its proxy, checked one by one:
- **Reached and read in full:** Batat (2024) QMR guest editorial (Emerald), Batat (2026) HFPV (SAGE), Batat (2026) PHIVE (Taylor & Francis), and the open-access Berthon et al. (2026) found in the library search. PDFs downloaded with Roger's approval and kept in the git-ignored `revision_2026-11/research/sources/`.
- **Not reached:** Germann Molz (2026), Riordan (2024), Weaver (2026) and Gao et al. (2026), because Bentley does not take *Hospitality & Society* (the proxy passes Intellect through unproxied, and the journal's ISSN finds nothing in the library search); Batat (2026) PSR, De Vos et al. (2026) and Brochado et al. (2026), because Bentley has no access to the 2026 issues of the *Journal of Services Marketing*. **Roger chose to go without them:** all seven stay at abstract depth and carry nothing beyond their abstracts.
- **The call for papers:** Roger chose the web page; the original PDF was already on this Mac (`~/Downloads/APA Summit 2026-CFP-Hospitality & Society.pdf`, the file the August digest was checked against), so it is the source, copied to the git-ignored sources folder as `cfp2025apa/`.

### V8-D6 · 13 Nov · The gap statement narrows
The two positioning re-reads (`stage2/POSITION_set1.md`, `POSITION_set2.md`) found the working gap statement false as worded: Shabnam et al. (2026: 14) and Sharma and Mattila (2026: 911) say who should act and what the customer is owed. What survives is narrower: no text says which of several firms owes a safeguard, and none treats one as the guest's claim. v8's gap sentence is written to the narrow form, with its nearest neighbours named (`OUR_BRIEF.md`).

### V8-D7 · 13 Nov · Stage 3: the Pierre ledger, and a correction to it
`PIERRE_LEDGER.md` gives each of Pierre's 397 sentences (56 insights) an outcome: 204 VERBATIM-eligible, 84 ADAPTED, 109 CUT. Its first draft numbered sections 4–8 from memory and was off by up to nine places; the ids were corrected against `PIERRE_SENTENCES.tsv`, a committed split of his text, and a check now confirms every bullet's quotation sits at its stated id and every sentence has an outcome. VERBATIM means eligible: the eligible sentences run to about 3,700 words, so Stage 4 chooses among them and records each one it leaves out.

### V8-D8 · 13 Nov · Pierre's text, and what the audits did to it
His text is commit 3e6828b1, which matches `~/Desktop/WhoHoststheGuest_2026-08-17_PIERRE_original.md` from the abstract to the references. The August audit changed 92 of his sentences; where it corrected a fact or a citation, v8 takes the audited form and the ledger says so. Where it changed wording for no stated reason (the abstract's 'easier'), his wording stands.

### V8-D9 · 13 Nov · Stage 4 checkpoint (Roger)
- **Weights: follow the model.** Introduction ~700 · Theoretical context ~1,850 · Approach ~450 · The parties ~2,150 · During the stay ~1,150 · At the touchpoint ~1,650 · Conclusion ~1,050. This replaces the approved plan's section budget.
- **Opening scenes: Pierre's two contrasting examples.** Hotel pricing shaped by a vendor's model (Garcia et al. 2026, told as v7 corrected it) against Le Petit Chef, the animated chef projected onto diners' tables while staff go on hosting (Batat 2021). Roger first said 'the ones from Berthon's original draft'; asked which, since his opening anecdote is the second-person scene D4 keeps out, he chose the two examples. Ledger I-34 is updated.
- **Walk by party.** The argument walks the phygital arrangement party by party (the property, the brand, the platform, the vendor, the state), then through the stay, then to the touchpoint, each subsection closed by a takeaway paragraph. v7's claims and order are unchanged.

### V8-D10 · 13 Nov · Section weights against the 9,000 cap (Stage 5 gate)
Written to the outline, the introduction came to 849 words (budget 700) and the theory to about 2,380 before its last paragraph (budget 1,850), mostly because Pierre's restored sentences and v7's law both landed there. At the model's weights the body would pass 9,000. Four theory sentences are cut at the ledger (O-047, O-066b, O-078, O-092) and the later budgets shrink: Approach 380 · The parties 1,800 · During the stay 1,000 · At the touchpoint 1,450 · Conclusion 950. The body then lands near 8,750. Every section stays inside the venue's bands (introduction 7–18%, theory 12–30%, case sections 22–57%, conclusion 4–13%), but the shares move from Roger's choice of the model's weights: theory about 26% (model 21%), the walk about 49% (model 54%). Recorded for Roger; the read-aloud decides.

### V8-D11 · 13 Nov · The count includes tables and headings
`wordcount.py` counts headings, table rows and the figure caption as body (about 320 words for Tables 1 and 2, the headings and the caption). To keep the body near 8,650 by that count, six more written sentences are cut at the ledger (O-009, O-048.1, O-093, O-111, O-151, O-174a, each carried elsewhere), O-131 and O-175 are rewritten, and the last two sections are budgeted at about 1,300 (the touchpoint) and 850 (the conclusion).

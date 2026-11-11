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

### D3 · 10 Nov · The journal model rests on eight full reads, not twelve
Six regular articles and two editorials are read end to end (`journal/CORPUS.md`). The plan's target was twelve, three of them on technology or commercial hosting. The texts that would close the gap are all behind the paywall. I am going ahead on version 1 of `journal/JOURNAL_MODEL.md` and will revise it when the closed texts are read. Alternative: wait for the sign-in. Reason for not waiting: the six agree on almost every trait that matters for the plan of the paper, and the gauge and research can proceed meanwhile.

### D4 · 10 Nov · v6 follows the journal where the journal is near-unanimous
Three rulings in `journal/JOURNAL_MODEL.md` depart from standing rules:
- a roadmap at the end of the introduction (5 of 6 articles), against `REGISTER.md` rule 3;
- the thesis and main moves stated with 'we argue' (5 of 6), against `REGISTER.md` rule 1 and against the house rule that first person marks the author's labour and not the claim;
- the scholar as grammatical subject where the paper leans on or disputes that scholar (6 of 6), which narrows `REGISTER.md` ruling 3.
The skill's precedence rule sends a unanimous genre trait to the author. Under "no stops" I am following the journal. **YOURS to reverse**: if you want the house rule kept, the 'we argue' sentences in v6 can be recast with the claim as subject; the ledger will mark each one.

### D5 · 10 Nov · Paragraph length is not the problem the structure check said it was
`revision_2026-11/STRUCTURE_CHECK.md` set v5's mean of 211 words against two editorials (153 and 163). The four conceptual articles run about 130, 180, 185 and 200. v6 will aim inside 130–200 with spread, and I am not treating v5's length as a defect to fix by splitting.

### D6 · 10 Nov · v6 carries no `[CHECK]` flag
The sources behind v5's seven flags are all closed. v6 leaves out Liau (2023), Hewagama et al. (2019) and Hales and Klidas (1998); cites King (1995) expressly as reported by Golubovskaya et al. (2017) and Varley et al. (2018); and cites Baum and Laux (2026) as the arXiv version that was read. The point about graded frontline authority (Reviewer 3.9) rests on sources held in full. Alternative: keep the flags. Reason: a flag in a draft sent to reviewers is a claim resting on a source nobody has read. Detail in `research/RESEARCH_SYNTHESIS.md`. **YOURS to reverse** once the texts are read.

### D7 · 10 Nov · Weaver is 2026, and the bibliography now says so
Crossref gives the version of record as *Hospitality & Society* 16:2 (August 2026), pp. 155–176. I corrected `literature/references.bib` and the card. `DRAFT.md` and `DRAFT_v5.md` still print 'Weaver 2025'; I have not changed them. `check_citations.py` on either file will now report that mismatch.

### D8 · 10 Nov · The model is Bulley (2015); five sections; two tables
Set out with reasons and alternatives in `PROPOSAL.md` (P1–P8). The title goes to sentence case with the wording unchanged (P6), which is **YOURS**.

### D9 · 10 Nov · New cards were verified independently
`varley2018hospitality` and `moysidou2023theorizing` were written from my own full reads and then checked by a separate verifier against the source texts. Every quotation matched; one method description was reworded.

### D10 · 10 Nov · The sentence-by-sentence pass is complete
`sbs/MODEL.md` M.001–M.233 (233 of 233 model sentences); `sbs/OUTLINE.md` S-001–S-278 and A-1–A-6 (every model entry answered or warranted); `sbs/LEDGER.md` S-001–S-278 and A-1–A-6, six verdicts each. `sbs/MANUSCRIPT.md` was written by hand from the ledger and checked against it by script. `manuscript/DRAFT_v6.md` adds the AI-acknowledgment heading, the references (81), cases (4) and legislation (7).

### D11 · 10 Nov · An independent check of every quotation, and the corrections it forced
A separate read-only agent checked 79 quoted passages and eight paraphrases against the cards and saved texts. No wording errors; seven problems of sense or locator, the worst inherited from v5 (Wilson-Nash p. 978 read in reverse). All fixed and recorded (`VERIFICATION.md`). Three quotations that were exact against the saved sources but missing from their cards were added to the cards.

### D12 · 10 Nov · Baum and Laux pages are arXiv pages
D6 said v6 cites the arXiv version. The bibliography entry, unchanged, renders the LNCS chapter. I left the entry alone, because v4 and v5 use it, and listed the mismatch as a debt (`VERIFICATION.md`, debt 1). **YOURS**: map the pages or switch the entry.

### D13 · 10 Nov · Tooling change
`check_citations.py` now takes an optional second argument naming the key list. The default is unchanged. `preflight.py` and `wordcount.py` still expect numbered headings; I ran them on a numbered copy and recorded the results rather than changing them.

### D14 · 10 Nov · Baum and Laux now cited from the chapter
The LNCS chapter is open access. I read it and replaced the arXiv page numbers with its printed pages (S-205, S-206, S-234), which settles D12's page mismatch. The year stays 2026, the online date; the chapter footer says 2027. **YOURS**: which year to print.

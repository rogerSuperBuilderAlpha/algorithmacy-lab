# Copyeditor Review — Post 6, "Parts and Members" (draft v4)

**STEP 0.** Register: deliberate first-person Substack philosophy, homology-first ("same boundary, different instrument"), never Hegel-anticipated-Φ, never Φ-demoted. Quoted material and the handful of signature lines (e.g., "He did not," "the purpose was never the smaller half") are off-limits as prose failures — I am not converting this into academic third-person prose, and I flag one thing here: this working directory sits under a repo-root `CLAUDE.md` that mandates no-first-person, Nagel-plain dissertation style for "all prose in this repo." That rule targets the dissertation; it does not govern this Substack series (Roger Hunt's own memory record distinguishes "author-drafts/lab-edits" Substack prose from the dissertation, and this task's brief explicitly names first-person philosophy as the register to protect). I am applying the task's brief, not the dissertation house style, and naming the conflict so it isn't silently resolved.

---

## VERDICT: Minor revision.

**Single most important fix:** two in-text citations point to the wrong pinned edition, and the References list is missing the entry those citations require. The severed-hand quote and the anatomist-corpse quote are both *Zusätze* (Additions) — student-lecture material the series hard-pins to the Geraets/Suchting/Harris Hackett edition (1830/1991b), never to Brinkmann & Dahlstrom (1830/2010a), which is reserved for main paragraphs and Remarks. The draft cites both as `(Hegel, 1830/2010a, §216, Addition)` and `(Hegel, 1830/2010a, §135, Addition)` — the correct edition tag, per `check_editions.py`'s own logic and per the card `hegel-el-bd.md` ("check_editions.py flags a Zusatz cited from B&D... the series pins ALL Zusätze to Hackett"), is `1830/1991b`. This is not a judgment call: Posts 5, 8, and 9 in this same series already execute the fix exactly this way, and Post 9's own sourcing note documents doing it ("v4 cites it as (Hegel, 1830/1991b, §216 Zusatz) and adds the Hackett edition to References"). Post 6 has not made the parallel fix, and the References list carries no Hackett entry at all.

---

## Findings, ranked most damaging first

### 1. [MAJOR] Wrong pinned edition on both Zusatz citations; missing reference entry

**Flagged text 1** (opening paragraph):
> "and is, in Aristotle's own phrase, 'a hand in name only,' not in fact (Hegel, 1830/2010a, §216, Addition)."

**Flagged text 2** ("What a Member Is, for Hegel"):
> "the only object that does, Hegel adds, is the one the anatomist is left with once the cutting is done (Hegel, 1830/2010a, §135, Addition)"

Both loci are Additions (Zusätze), confirmed at that granularity by the digest itself ("§216 (Zusatz for the hand; main paragraph for means/purposes)"; "§135 (main paragraph + Zusatz)... the anatomist-and-corpse figure the draft's sourcing note feared might sit in the Philosophy of Nature is in fact at EL §135 ZUSATZ"). The card `hegel-el-bd.md` states the rule as hard and enforced: "MAIN paragraphs and Remarks → B&D... The Zusätze... are pinned to the Hackett Geraets/Suchting/Harris edition (hegel-el-hackett) instead." The sourcing note's careful work locating *which* paragraph each quote sits in (Addition vs. main) is exactly right — it just doesn't carry that locus-level precision through to the edition tag.

**Exact rewrite:**
- `(Hegel, 1830/2010a, §216, Addition)` → `(Hegel, 1830/1991b, §216, Addition)`
- `(Hegel, 1830/2010a, §135, Addition)` → `(Hegel, 1830/1991b, §135, Addition)`

**Add to References**, alphabetically/chronologically between the current Hegel(1991a) and Hegel(2010a) entries, using the exact string already established by Posts 5, 8, and 9 (verified verbatim against `post5_civil_society.md` line 417):

> Hegel, G. W. F. (1991b). *The encyclopaedia logic: Part I of the Encyclopaedia of philosophical sciences with the Zusätze* (T. F. Geraets, W. A. Suchting, & H. S. Harris, Trans.). Hackett. (Original work published 1830)

No other change is needed — the §216 main-paragraph quote ("all members are reciprocally momentary means...") and the §135 main-paragraph untruth-of-Whole-and-Parts citation are both correctly `1830/2010a` (B&D), and should stay that way.

*Note for the record:* the previous copyeditor round (`post6_reviews/copyeditor.md`, reviewing v2) marked this exact same locus "Gate respected. ✔" and missed the edition split entirely. It is worth flagging that the miss recurred into v4 rather than treating it as newly introduced.

### 2. [MODERATE] Unmarked added emphasis in the Kreines quote

**Flagged text:**
> "Kreines gives the realist version of the same claim: Hegel holds, against Kant, that living beings '*do* manifest true 'internal purposiveness'' of which 'we *can* have objective knowledge' (Kreines, 2008, p. 346)."

Neither the digest nor the card `kreines2008logiclife.md` records italics on "do" or "can" in the verified wording ("living beings 'do manifest true "internal purposiveness,"' 'explicable in teleological terms,' and 'we can have objective knowledge of this natural teleology'"). The earlier copyeditor round's transcription of the same passage in v2 also shows it unitalicized. APA 7 (8.31) requires "[emphasis added]" after the citation whenever a quoting author adds emphasis the source doesn't carry. Two ways to close this cleanly, either is fine:

**Rewrite (drop the added stress — matches the verified wording exactly):**
> Kreines gives the realist version of the same claim: Hegel holds, against Kant, that living beings "do manifest true 'internal purposiveness'" of which "we can have objective knowledge" (Kreines, 2008, p. 346).

**Or, if the stress is doing real work against the Kantian regulative reading, keep it and mark it:**
> ...that living beings "*do* manifest true 'internal purposiveness'" of which "we *can* have objective knowledge" (Kreines, 2008, p. 346, emphasis added).

I'd take the first option — the sentence's own "Hegel holds, against Kant" already carries the contrastive force; the italics are decorative on top of it.

### 3. [MINOR] Vieweg reference entry is missing its DOI

The card `vieweg2017state.md` records a verified DOI: `10.1093/oso/9780198778165.003.0007`. Every other chapter/article reference in this piece that has a DOI prints it (Corti, James, Albantakis, Oizumi); Vieweg's is the one silent omission, and it isn't because none exists.

**Exact rewrite** (append to the existing entry):
> Vieweg, K. (2017). The state as a system of three syllogisms: Hegel's notion of the state and its logical foundations (S. Stein, Trans.). In T. Brooks & S. Stein (Eds.), *Hegel's political philosophy: On the normative significance of method and system* (pp. 124–141). Oxford University Press. https://doi.org/10.1093/oso/9780198778165.003.0007

### 4. [MINOR] The corpus-grep claim carries no citation, breaking the piece's own convention

**Flagged text** ("The State-Triad, Computed and Bracketed"):
> "And the state-specific claim stays a claim: a grep of the corpus confirms no Individual/Particular/Universal triad has been built and run."

Every other computational claim in the essay — the major-complex quote, finding 8, the veto-player thread, the back-edge thread, the cyclic thread — carries a parenthetical file citation. This one, sourced in RECEIPTS.md to `org_frontier/ (whole corpus grep) + org_frontier/probes/PROBES.md`, doesn't. It's the one unattributed empirical claim in an essay that is otherwise scrupulous about attributing every number.

**Exact rewrite:**
> And the state-specific claim stays a claim: a grep of the corpus confirms no Individual/Particular/Universal triad has been built and run (org_frontier/probes/PROBES.md).

### 5. [MINOR] Two lab-receipt citations point to a directory, not the file

**Flagged text:**
> "...the veto player is the argmax-Shapley party in every one, 115 of 115 (org_frontier/threads/veto_player)."
> "...the form has no integration at all, so the mediator can only convey' (org_frontier/threads/back_edge)."

Both directories (`veto_player/`, `back_edge/`) contain multiple files; the actual source is `THREAD.md` in each, and that's exactly how the parallel cyclic-thread citation is written two paragraphs later: `(org_frontier/threads/cyclic/THREAD.md)`. Inconsistent specificity across three citations doing the identical job.

**Exact rewrite:**
> `(org_frontier/threads/veto_player)` → `(org_frontier/threads/veto_player/THREAD.md)`
> `(org_frontier/threads/back_edge)` → `(org_frontier/threads/back_edge/THREAD.md)`

### 6. [MINOR, already gated — restate, don't re-discover] Two disclosed but still-open reference gaps

- The Corti (2022) quotations carry no page or paragraph locator anywhere (APA 7, 8.25, requires one for direct quotations). Neither the digest nor the card supplies a locator to insert — HPLS uses continuous article numbering (Article 17) rather than conventional pagination, so a paragraph or PDF-page locator needs a print/PMC check before it can be added. Flagging so it doesn't get lost, not asserting a number.
- The James (2020) reference entry has no page range (`(pp. XX–XX)`), which APA 7 requires for a chapter in an edited volume. The sourcing note already discloses this as a live gate ("no page range for the chapter was recoverable this pass"); it just needs to land before the piece can be called reference-complete.

### 7. [COSMETIC, optional] Ellipsis glyph inside the back-edge quote

> "Cut the back-edge … and the form has no integration at all"

APA 7 (8.31) specifies three spaced periods (". . .") for an ellipsis, not the single Unicode glyph. Given the register (Substack, not a journal proof), I would not hold the piece for this — noting it only because the brief specifies an APA-7 lens. If the author wants it exact: `Cut the back-edge . . . and the form has no integration at all`.

---

## What's already correct and shouldn't be touched

- §198 in-text citation stays neutral — no "Remark," no "main paragraph" claim in the body — matching the digest's sanctioned fallback ("Cite as '§198 (Remark)' or plainly '§198'") and Post 3's precedent. Good call, and correctly explained in the sourcing note.
- The §198 rotation now runs P → I → U across the three figures, matching Hegel's own sequence exactly as the card describes it (figure 2 middle = will/activity of individuals = I; figure 3 middle = the universal = U). This was a real error in a prior round and it's closed now.
- §278R renders Nisbet's "separate existence," not Knox's "independence." §276A uses Nisbet's "point," not Knox's "cells." Both correct.
- Both Corti quotations are verbatim against the PMC open-access text, word for word.
- The "maximizes φ_s" quote correctly reproduces the Greek-plus-subscript glyph rather than transliterating it — the exact fix the digest's verification-corrections section called for is already in place.
- Every in-text citation resolves to a reference entry and every entry is cited (aside from the missing Hackett entry noted above); Hegel reference entries are in correct chronological order (1991a before 2010a).
- The 49-word inline block-quote problem the prior copyeditor round flagged for v2 (cyclic-thread receipt) is gone in v4 — that passage is now paraphrase with the citation at the end, under any word-count threshold.

---

## Biggest genuine strength

The piece's citation discipline is, apart from the edition-pin slip, unusually careful for a first-draft-adjacent Substack post: it tracks Zusatz-vs-main-paragraph at the *content* level with real precision (the sourcing note's own accounting of which quote sits where is accurate down to the paragraph), it resists inventing a page number anywhere it doesn't have one, and it holds the line on the hardest discipline in the brief — never letting the homology claim slide into anticipation, never letting the gap-finding slide into demoting Φ. The failure mode here is narrow and mechanical (an edition tag not migrating with a correctly-identified Zusatz), not a failure of citation care.

---

**Files consulted:** `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/hegel_coordination/library/digests/post6.md`, `library/RECEIPTS.md`, `library/cards/hegel-el-bd.md`, `library/cards/hegel-el-hackett.md`, `library/cards/hegel-pr-nisbet.md`, `library/cards/james2020organisms.md`, `library/cards/kreines2008logiclife.md`, `library/cards/corti2022organism.md`, `library/cards/vieweg2017state.md`, `check_editions.py`, `posts/post5_civil_society.md`, `posts/post8_freedom.md`, `posts/post9_ledger.md`, `posts/post6_reviews/copyeditor.md` (prior round, v2), `org_frontier/essays/phi_as_a_cooperative_game.md`, `org_frontier/STRUCTURAL_FINDINGS.md`, `org_frontier/threads/veto_player/THREAD.md`, `org_frontier/threads/back_edge/THREAD.md`, `org_frontier/threads/cyclic/THREAD.md`.
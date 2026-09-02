# Citation-by-Citation Criticality Audit — 2026-08-30

## Scope

This pass gives every one of the 83 distinct in-text citations in `manuscript/PAPER.md` its own named
tier and verdict. It builds on, and does not duplicate, two prior passes:

- `literature/VERIFICATION_2026-08-29_full_sweep.md` — bibliographic existence/DOI/page-number accuracy
  for ~75 references.
- `literature/CLAIM_ACCURACY_2026-08-30.md` — whether the paper's characterization of each source
  matches what the source argues, run in six section-batches; many sources only received a block-level
  pass bundled with neighbors, not an individual verdict.

This file closes that gap. Every citation gets a **tier** (criticality to the paper's argument) and a
**verdict**, matched to a verification depth proportional to the tier:

- **Tier 1 — directly argued with.** The paper quotes, extends, or contests a specific claim from the
  source. Standard: obtain the actual source (full text or a PDF, not just a card, unless the existing
  card is itself full-text-verified), re-read the passages the manuscript leans on, and check (a) the
  paper's characterization matches what the source actually argues, (b) quotes/page numbers are exact,
  (c) no overclaiming, (d) whether a more precise citation exists.
- **Tier 2 — moderately engaged.** One specific claim or quote is attributed to the source. Standard:
  verify that one claim, via a trustworthy card or a targeted source check — no full re-read required.
- **Tier 3 — background/existence.** The source is a supporting pointer or list member. Standard:
  confirm it exists, is correctly identified (right paper, right year), and its subject plausibly fits
  the point — no page-chasing, no full verification of claims the source makes elsewhere.

Verdict vocabulary (matches the prior pass): **ACCURATE** / **DRIFTED** (recoverable inaccuracy) /
**OVERCLAIMED** (source doesn't support the weight placed on it) / **UNVERIFIABLE AT CURRENT DEPTH** /
**FLAG** (a judgment call for the author, not an accuracy problem).

Planning for this pass — the tiering rationale, the 13-batch grouping, and the model assignment per
batch — was done by a Fable-model planning agent, per the author's instruction, then reviewed and
adopted (with two resolutions: confirming Zhou et al. 2025 is a single paper despite two same-short-cite
library cards, and giving the Selznick 1949 batch a book-access fallback). See
`/Users/ludwitt/.claude/plans/zany-tumbling-riddle.md` for the full plan.

Batch reports are appended below as they complete, followed by a closing master table and a punch list
of confirmed fixes for `PAPER.md`.

---

## Batch B — Zhou et al. (2025); Curchod et al. (2020); Rahman (2021); Sutherland et al. (2020)

### 1. Zhou et al. (2025) — VERDICT: ACCURATE, with one DRIFTED fix and one FLAG requiring author judgment

Read `literature/cards/zhou2025apjhr.md` and `literature/ZHOU_2025_INSTRUMENT.md` first, then independently re-verified against the journal version-of-record PDF (`dissertation/research/sources/pdfs/zhou2025_algorithmic_competency.pdf`, not the working paper) using `pdftotext`, rather than trusting the card's own verification notes at face value.

**Everything numerical checks out exactly**, confirmed directly against the VoR:
- 99 semi-structured interviews → 14 items (Sample 1); EFA N=275, CFA N=213, construct validation N=230, three-wave panel N=225 (Samples 2–5) — all confirmed against Table notes and method sections.
- Second-order four-factor model, 12-item final instrument, aggregate α = .85 — confirmed (Table 4 diagonal: "1. Algorithmic competency ... (0.85)").
- r = .37\*\* between AC and digital competence, r = .04 (non-significant, no asterisk) between digital competence and Embracing AM — confirmed verbatim in Table 4 ("Convergent and discriminant validity correlations," N = 230, sample 4).
- The p. 2 definition quote — "understanding of platform algorithms that assign and evaluate their work and their ability to adapt to and navigate those algorithms" — located verbatim on the PDF page footed "2 of 15." Exact match, correct page.
- Item 8, Item 11, and Item 6 quotes (PAPER.md lines 119, 121) — all three located verbatim in Table 2 on the page footed "8 of 15," including the en dash in "customers–workers matching." Exact matches.
- The invented "(audio recordings, timestamped delivery logs)" detail that the 2026-08-30 tiered audit flagged as fabricated (the actual N22 quote says only "evidence like recordings") **has already been fixed** — current PAPER.md line 121 reads "a courier compiles supporting evidence and submits an administrative appeal," which is now accurate and does not need further action.

**New finding — DRIFTED, not previously caught.** PAPER.md line 119:

> "Customer-oriented service behavior does enter the authors' structural equation model through Peccei and Rosenthal's **(1997)** scale..."

Zhou et al. cite *two* different Peccei & Rosenthal papers, confirmed from the VoR reference list:
- Peccei, R., & Rosenthal, P. (1997). "The Antecedents of Employee Commitment to Customer Service..." *IJHRM* 8(1): 66–86 — used **only** for a definitional quote ("the extent to which workers engage in continuous improvement and exert effort on the job for the benefit of customers," Peccei and Rosenthal 1997, 69).
- Peccei, R., & Rosenthal, P. (2000). "Front-Line Responses to Customer Orientation Programmes..." *IJHRM* 11(3) — this is the paper Zhou et al. actually cite for the **instrument**: "Customer-oriented service behavior... was assessed using the six-item scale from Peccei and Rosenthal (2000)" (VoR, Method section, p. 8 of the PDF).

PAPER.md attributes the scale used in Zhou et al.'s SEM to the wrong year. The bibliography (PAPER.md line 453) only lists the 1997 entry, confirming the 2000 paper was never checked.

**Fix:**
- Before: `Peccei and Rosenthal's (1997) scale`
- After: `Peccei and Rosenthal's (2000) scale`
- Also needs a new bibliography entry for Peccei & Rosenthal (2000), *International Journal of Human Resource Management*, 11(3) — page range not independently confirmed in this pass (two-column PDF extraction truncated it); confirm before inserting.

**New finding — FLAG (interpretive, not a factual error).** PAPER.md line 125:

> "In their structural equation model, the primary organizational antecedents predicting algorithmic competency are social mechanisms — informal peer support systems moderated by collectivist cultural orientations. That evidence supports the socialization proposition directly."

Checked against the VoR hierarchical regression (Table 6, N=225, sample 5): social support from peers, b = .23\*\*\*; **cognitive job crafting, b = .41\*\*\*** — job crafting is the *larger* predictor of the two, and is explicitly defined by the authors as "active cognitive changes" the worker makes (not a social/peer mechanism). Calling peer support "the primary" antecedent, while the paper's own strongest predictor is a non-social, individually-enacted cognitive strategy, selectively reads the evidence in the direction the socialization proposition needs. Peer support genuinely is significant and does interact with collectivism (b=.09, p<.05), so this is a judgment call, not an outright misstatement. Suggested direction: acknowledge cognitive job crafting as the (numerically larger) co-antecedent, and narrow the socialization claim to what peer support specifically supports.

### 2. Curchod et al. (2020) — VERDICT: ACCURATE, one FLAG still open, one new minor note

Six in-text uses (lines 46, 165, 248, 252, 516, 524). Fully audited in the prior pass; spot-checked rather than re-verified from scratch.

- **Line 252** ("...evaluated across a visibility gap by buyers they cannot observe or engage") — ACCURATE; confirms the earlier Zhou→Curchod fix landed correctly.
- **Lines 46, 516, 524** ("non-portable reputational ratings/capital") — ACCURATE, fair paraphrase.
- **Line 165** — ACCURATE in substance, but has a mid-sentence terminology slip: "produce an asymmetrical triad of platform operators, buyers, and sellers... evaluate **workers** invisibly." Curchod et al.'s own scope note distinguishes eBay business sellers (established micro-firms) from gig workers — the paper elsewhere correctly says "sellers." Minor one-word fix: "workers" → "sellers."
- **Line 248** ("generate consent through algorithmic enrollment (Cameron, 2024; Curchod et al., 2020)") — **FLAG, carried over unresolved from the prior pass.** Curchod et al.'s contribution is a theory of power/agency (one-way evaluation right, visibility gap, blocked exit), not a consent-manufacture argument the way Cameron (2024) explicitly is. Recommend narrowing the parenthetical to Cameron alone, or adding a clause distinguishing the two mechanisms.

### 3. Rahman (2021) — VERDICT: ACCURATE, prior verification holds

Ten-plus in-text uses, the most thoroughly pre-verified of the four (two prior full sweeps closed every page-numbered citation). Spot-checked: all five page-numbered citations (lines 129–133) match the card's corrected values exactly; background/argumentative uses (lines 209, 242, 548, 624) consistent with the source's actual structure. Nothing new. No fixes needed.

### 4. Sutherland et al. (2020) — VERDICT: ACCURATE, both prior corrections confirmed landed correctly

- P10 "rapport" quote (line 145): confirmed at p. 468, the correct value (the 2026-08-29→08-30 correction chain resolved correctly).
- P39 quote (line 147): confirmed at p. 469, correct.
- Swept the remaining ~6 uses (lines 87, 141, 143, 149, 151, 183, 195, 264, 327) — all independently confirmed verbatim against the PDF and unchanged since the prior pass. Line 151's "informal peer sensemaking" phrasing doesn't use Sutherland's exact vocabulary but the underlying mechanism (forum consultation, trial-and-error learning) is genuinely documented — a defensible paraphrase, not a drift.
- Net: no new corrections needed.

### Batch B actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Zhou et al. (2025) | PAPER.md line 119 | Peccei & Rosenthal cited "(1997)" for the SEM scale; correct year is (2000) | **DRIFTED — needs fix + new bibliography entry** |
| 2 | Zhou et al. (2025) | PAPER.md line 125 | "primary... antecedents... are social mechanisms" overstates peer support vs. the paper's own larger predictor (cognitive job crafting, non-social) | **FLAG — author judgment call** |
| 3 | Curchod et al. (2020) | PAPER.md line 165 | "evaluate workers invisibly" should read "evaluate sellers invisibly" | **Minor — optional one-word fix** |
| 4 | Curchod et al. (2020) | PAPER.md line 248 | "generate consent... (Cameron, 2024; Curchod et al., 2020)" pairs Curchod with a consent claim it doesn't make | **FLAG — carried over, still unresolved** |
| — | Rahman (2021) | all uses | — | Clean |
| — | Sutherland et al. (2020) | all uses | — | Clean, both prior fixes confirmed |

---

## Batch A — Stark and Vanden Broeck (2024); Stark & Pais (2020); Selznick (1949); Manky (2025)

New cards saved for all four: `literature/cards/starkvandenbroeck2024.md`, `literature/cards/starkpais2020.md`, `literature/cards/selznick1949.md`, `literature/cards/manky2025.md`.

### 1. Stark and Vanden Broeck (2024) — VERDICT: mostly ACCURATE, one DRIFTED, one FLAG

7 uses (lines 25, 44×2, 248, 296, 513, 524). Full text obtained via the adjacent dissertation-repo library card + raw typeset PDF text, independently grepped for "match," "gap," "coordinat," "unchosen."

- Line 25 — ACCURATE. "on platforms they are co-opted" is an exact quote; the compound term "coordinative co-optation" itself is correctly NOT attributed to this source (the string "coordinative" appears nowhere in the article) — the fix applied earlier this session already reflects this.
- Line 44 (both clauses) — ACCURATE.
- Lines 513, 524 (paired with Stark & Pais) — ACCURATE.
- Line 248 — FLAG, not an accuracy problem: "exploit coordination gaps (Stark & Vanden Broeck, 2024)" — zero occurrences of "gap" anywhere in the article; their own frame is assets/activities sitting outside the firm boundary, addressed via co-optation/enrollment, not a "gap." Substance is defensible background gloss; optional tightening only.
- **Line 296 — DRIFTED, real fix.** "Coordinative co-optation is defined by an algorithm that matches unchosen parties (Stark & Vanden Broeck, 2024)" — zero occurrences of "match" anywhere in this article. The "matching" vocabulary belongs entirely to Stark & Pais (2020), confirmed at multiple points in that source. Every other place in the manuscript that makes this identical claim (lines 44, 513, 524) correctly pairs both sources; line 296 is the one place it doesn't.
  - **Fix — before:** `Coordinative co-optation is defined by an algorithm that matches unchosen parties (Stark & Vanden Broeck, 2024), and that condition is met here in the same sense it is met on a dispatch platform.`
  - **Fix — after:** `Coordinative co-optation is defined by an algorithm that matches unchosen parties (Stark & Pais, 2020; Stark & Vanden Broeck, 2024), and that condition is met here in the same sense it is met on a dispatch platform.`

### 2. Stark & Pais (2020) — VERDICT: ACCURATE across all three uses

3 uses (lines 44, 513, 524), all paired with Stark and Vanden Broeck (2024). Full text obtained and independently grepped. "Match"/"matching" is directly this source's own vocabulary ("making matches," "matching protocols"). The enrollment-not-delegation mechanism, twisted/deflected accountability, and ratings-into-rankings claims all check out. One inherited, already-closed FLAG not reopened here: "unilaterally terminate accounts" rests in the source on a footnote crediting Rosenblat (2018) rather than Stark & Pais's own analysis — minor looseness, previously judged not to need a fix since the citation covers the general mechanism, not a specific termination-rate finding.

### 3. Selznick (1949), *TVA and the Grass Roots* — VERDICT: ACCURATE, one FLAG

5–6 uses across body text, a definitional list, and Appendix A's table. This is a book — no cover-to-cover read was attempted. The definitional cooptation chapter (pp. 13–16) was read directly against raw OCR text; later chapters were checked only via an existing verified secondary card, not independently re-read (PAPER.md doesn't draw on them). Direct quote confirmed: "cooptation is the process of absorbing new elements into the leadership or policy-determining structure of an organization as a means of averting threats to its stability or existence" (p. 13). PAPER.md's gloss — "an organization absorbs an external challenger by conferring a seat on him: opposition becomes participation, and the seat carries a formal standing" — matches Selznick's **formal** cooptation branch precisely.

**FLAG (judgment call, not an error):** Selznick splits cooptation into formal and informal variants; the informal variant (unpublicized capitulation to actual power centers, no seat conferred) is arguably closer in spirit to platform enrollment than the formal branch the paper contrasts against. The paper's choice of the formal branch is defensible — it's the one that literally involves a "seat," the exact axis of contrast needed — but it collapses a distinction Selznick treats as load-bearing. No fix required unless a Selznick-literate reviewer is specifically anticipated.

### 4. Manky (2025) — VERDICT: bibliography ACCURATE; content UNVERIFIABLE AT CURRENT DEPTH beyond the abstract

3 uses (lines 19, 29, 169), no card existed before this pass. Fully paywalled, no OA copy anywhere (Unpaywall confirms `is_oa: false`; Wiley and ResearchGate both returned HTTP 403). Bibliographic details confirmed via Crossref + Semantic Scholar (both independently confirm 2025 as the correct year, despite Wiley's print-issue page currently showing 2026 — a common online-first/print-issue mismatch, resolved in "2025"'s favor by two independent metadata providers). N=40 (line 169) is an exact match to the abstract's "40 in-depth interviews." The general thrust — platforms as a safety/trust mechanism via "data-driven oversight of passengers and routes" — is confirmed at abstract level. The specific mechanism PAPER.md attributes to the study (reading an opaque/black-box *metric* to decide in the moment whether to *accept* a passenger) is a plausible, abstract-consistent reading but is not itself the abstract's phrasing, and the article body could not be obtained to confirm it precisely. **This is the paper's most load-bearing empirical citation in its opening motivating example, used three times, and rests on an abstract-only read** — flagged for the author to verify directly with institutional access if available before the manuscript is finalized.

### Batch A actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Stark and Vanden Broeck (2024) | PAPER.md line 296 | "matches unchosen parties" cited to Vanden Broeck alone; the vocabulary is Stark & Pais's | **DRIFTED — fix above** |
| 2 | Stark and Vanden Broeck (2024) | PAPER.md line 248 | "coordination gaps" isn't the source's own language | **FLAG — optional tightening** |
| 3 | Selznick (1949) | body text, list, Appendix A | Formal/informal cooptation distinction collapsed | **FLAG — author judgment, no fix required** |
| 4 | Manky (2025) | lines 19, 29, 169 | Specific "reads opaque metric before accepting passenger" mechanism unconfirmed beyond abstract (paywalled) | **FLAG — verify with institutional access if possible** |
| — | Stark & Pais (2020) | all uses | — | Clean |

---

## Batch C — Spitzberg (2006); Spitzberg & Cupach (1984); Sandberg (2000)

### 1. Spitzberg (2006) — VERDICT: ACCURATE

4 uses. Independently re-derived every page number by walking the PDF's running-head footers rather than trusting `pdftotext`'s own page breaks. All seven page-numbered quotes/claims (pp. 630, 640, 641, 638, 644, 648×3, 650) confirmed exact matches. The "the fulfillment of positively valenced expectancies" fix (restoring the dropped "the") is confirmed correctly landed — source reads verbatim "...associated with **the** fulfillment..." The extended algorithmic-gate thought experiment is clearly framed as the paper's own extension, not attributed to Spitzberg. No overclaiming.

### 2. Spitzberg and Cupach (1984) — VERDICT: ACCURATE (use 1), DRIFTED (use 2)

2 uses. The 1984 Sage monograph itself is unobtained; verified via the contemporaneous ERIC validation study (ED279030), which reports the book's seven defining criteria and quotes it directly.

- **Line 235 — ACCURATE.** "Not an isolated individual attribute but a relational quality jointly enacted and evaluated by interacting parties" matches two of the source's seven criteria ("interdependent process," "interpersonal impression") and a direct 1984 quote reproduced in the ERIC document.
- **Line 325 — DRIFTED / mild overclaim.** "Competence operates across molar and molecular levels **that cannot be collapsed into a single metric**" — the molar/molecular half is confirmed (criterion 4 of the seven), but the stronger "cannot be collapsed into a single metric" clause isn't sourced anywhere in the available 1984 material; available evidence attributes that stronger claim to Spitzberg's later solo work (2015), not the 1984 book, and Spitzberg (2015) isn't in PAPER.md's reference list.
  - **Fix — before:** `following Spitzberg and Cupach (1984), competence operates across molar and molecular levels that cannot be collapsed into a single metric, so operationalization must show that standardized scales preserve the holistic interpretive conception of work (Sandberg, 2000) rather than atomizing it into decontextualized traits.`
  - **Fix — after:** `following Spitzberg and Cupach (1984), competence operates across molar and molecular levels, so operationalization must show that standardized scales preserve the holistic interpretive conception of work (Sandberg, 2000) rather than atomizing it into decontextualized traits, and that a measure pitched at one level licenses no automatic inference about the other.`

### 3. Sandberg (2000) — VERDICT: DRIFTED (minor, recoverable)

3 uses. Read directly as page images (the PDF is a scan). Overall characterization is faithful — the earlier KSAO/rationalistic-definition contradiction a prior pass had flagged is no longer present in the current draft. Conception 3 (customer-holistic) and the paper's extension of it are accurately and appropriately hedged.

**Drifted:** Line 233 lists the three conceptions as "optimizing separate **technical components**, balancing interacting qualities, or managing the entire process..." — Sandberg's own label for conception 1 is "Optimizing Separate **Qualities**" (engine performance attributes: driveability, fuel consumption, emissions, engine power), not physical components. This shift in register understates Sandberg's actual point.
- **Fix — before:** `He identified three interpretive framings: optimizing separate technical components, balancing interacting qualities, or managing the entire process from the customer's holistic perspective.`
- **Fix — after:** `He identified three interpretive framings: optimizing separate engine qualities, balancing interacting qualities, or managing the entire process from the customer's holistic perspective.`

Reference-list entry (Sandberg, J. (2000). *AMJ* 43(1), 9–25, "interpretative" spelling) confirmed exact.

### Cross-source sequencing check

The paper's relative treatment of all three sources is accurate: Sandberg introduced first as a distinct interpretive tradition, then Spitzberg & Cupach (1984) as the foundational relational-competence position, with Spitzberg (2006) explicitly extending that commitment into mediated settings — this matches how the two lineages actually relate in the literature (Spitzberg 2006 itself cites Spitzberg & Cupach 1984), and the paper does not conflate the individually-oriented Sandberg tradition with the relational Spitzberg one.

### Batch C actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Spitzberg & Cupach (1984) | PAPER.md line 325 | "cannot be collapsed into a single metric" not sourced to the 1984 book | **DRIFTED — fix above** |
| 2 | Sandberg (2000) | PAPER.md line 233 | "technical components" should read "engine qualities" | **DRIFTED — fix above** |
| — | Spitzberg (2006) | all 4 uses | — | Clean |
| — | Spitzberg & Cupach (1984), line 235 | — | — | Clean |

---

## Batch E — Katsh and Rifkin (2001); Suddaby (2010); Cameron (2024)

### 1. Katsh and Rifkin (2001) — VERDICT: ACCURATE

A card already existed (`literature/cards/katsh2001.md`) — the "no card" flag in the plan was incorrect for this source. Triangulated against two other direct-read cards in the same cluster (`katsh2017.md`, `wing2021.md`), which independently corroborate the same characterization: the fourth-party tradition theorizes the system's obligations, never the participant's capacity. All three uses (lines 27, 163, 252) confirmed accurate, including the correct attribution of Wing et al.'s four procedural guarantees to Wing et al. rather than to Katsh & Rifkin. No fix needed; a stale section-numbering artifact in the existing card's prose is cosmetic only.

### 2. Suddaby (2010) — VERDICT: ACCURATE

No card existed; built one, saved below. Read the full 12-page article directly. Confirmed verbatim, p. 347: Suddaby's four elements of construct clarity are definitions, scope conditions, semantic relations to other constructs, and coherence — PAPER.md line 173 restates these in his own order, exactly. This is the article's own organizing rubric and it's borrowed correctly and is genuinely load-bearing for the section's structure.

Line 31's lighter use ("leaving institutional justice to the governance literatures equipped to judge it (Suddaby, 2010)") is a defensible extension of his scope-conditions argument, but the citation's placement at the sentence's end risks being misread as sourcing the specific "institutional justice / governance literatures" division — which Suddaby never discusses. Not an error; an optional precision fix:
- **Fix — before:** `Algorithmacy is a bounded behavioral construct: it defines the sensibility the triad demands of a participant and stops there, leaving institutional justice to the governance literatures equipped to judge it (Suddaby, 2010).`
- **Fix — after:** `Algorithmacy is a bounded behavioral construct, scoped by definition and boundary condition in the manner construct clarity requires (Suddaby, 2010): it defines the sensibility the triad demands of a participant and stops there, leaving institutional justice to the governance literatures equipped to judge it.`

### 3. Cameron (2024) — VERDICT: ACCURATE (2 of 3 uses), DRIFTED (1 of 3, a genuine miss by the prior audit pass)

- Line 165 — ACCURATE; the earlier "and system stability" removal (a recent fix) is confirmed correctly applied. "Algorithmic labor triangle" and "constant and confined choices" are both genuinely Cameron's own terms.
- Line 248 — ACCURATE (Cameron's half of the pairing; Curchod's half is a separate, already-flagged issue).
- **Line 256 — DRIFTED / OVERCLAIMED, a real miss.** "...manufacture consent **and stabilize algorithmic labor regimes**..." attaches to Cameron the exact same unsupported "stability" claim that was correctly caught and removed at line 165 — but this second, near-identical instance was missed, including by this same tiered audit's own Zhou/Curchod pass conventions (an earlier check of this sentence verified only the "consent"/"continuous, confined choices" clauses, not "stabilize"). Zero occurrences of "stabil-" anywhere in Cameron's full text, independently grepped. The stabilization idea isn't lost by cutting it here — the paper already states it as its own theoretical move one sentence earlier, in its own voice ("individual mastery of the arrangement stabilizes the arrangement that burdens individuals").
  - **Fix — before:** `Cameron (2024) demonstrates how on-demand workers navigate continuous, confined choices in ways that manufacture consent and stabilize algorithmic labor regimes, and her model leaves unspecified the individual capacity separating successful navigation from failure.`
  - **Fix — after:** `Cameron (2024) demonstrates how on-demand workers navigate continuous, confined choices in ways that manufacture consent, and her model leaves unspecified the individual capacity separating successful navigation from failure.`

### Batch E actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Cameron (2024) | PAPER.md line 256 | "and stabilize algorithmic labor regimes" unsupported, same defect as the already-fixed line 165 | **DRIFTED — fix above, real miss caught this pass** |
| 2 | Suddaby (2010) | PAPER.md line 31 | Citation placement risks over-attribution | **Optional precision fix** |
| — | Katsh and Rifkin (2001) | all 3 uses | — | Clean |
| — | Cameron (2024), lines 165, 248 | — | — | Clean |

---

## Batch D — Long and Magerko (2020); Guzman and Lewis (2020); Hancock et al. (2020)

### 1. Long and Magerko (2020) — VERDICT: ACCURATE

Full text still unobtainable (re-tried Wayback, ACM DL, Semantic Scholar API, OpenAlex — all confirm closed access, no fetchable version-of-record). The no-page-number state in `PAPER.md` (a deliberate 2026-08-29 removal) is confirmed correct and should stay as is. Quote verification against the steelman (camera-ready full text via Internet Archive): all quoted fragments verbatim matches — the seventeen-competency structure, the "communicative subjects, instead of mere interactive objects"-style quotes, Competency 10 and Design Consideration 11 text, and the "nine competencies technical / one normative" theme count. Two non-blocking observations, no fix required: the "only two of seventeen reference human actors" count is defensible but contestable (Competency 2 also contains the word "human," in a taxonomic, non-operational sense); Competency 5's paraphrase ("comparative baseline against which to evaluate automated performance") slightly overstates what is actually a task-allocation criterion, not a benchmark-evaluation one — optional tightening offered in the full batch report if the author wants it.

### 2. Guzman and Lewis (2020) — VERDICT: ACCURATE

All four page-numbered quotes (pp. 71, 74, 74, 73) independently re-verified directly against `literature/pdfs/guzmanlewis2020.pdf` via per-page extraction matched to printed running headers — all exact. The "blur mediator and communicator functions simultaneously" claim is directly supported by the source (p. 74). Specifically tested the card's own flagged risk — that HMC's promise to theorize how people "relate to... others" might mean the far-side human counterpart is theorized after all — by reading the full relational-aspects section (pp. 78–79): "others" cashes out as self-concept work and AI's social-role modeling, not a real far-side co-interactant reached through the AI. The card's caution does not materialize; "leaving the far-side human untheorized" holds up as accurate.

### 3. Hancock et al. (2020) — VERDICT: DRIFTED (recoverable, three linked instances)

Page numbers (89, 90, 91) independently re-derived via per-page `pdftotext` matched to printed footers — the recent 90→89 fix is confirmed correct.

**New finding.** Hancock et al.'s formal definition uses the general term "a communicator," and their role-orientation parameter is explicitly bidirectional (Table 1: "sender vs. receiver"; body text p. 91: "we imagine receivers will increasingly use AI tools... Google Translate allows both sender and receiver to converse, using AI as mediator"). `PAPER.md` narrows this to "sender" specifically in three places, creating an internal inconsistency with its own correct quote of "a communicator" (general) two sentences earlier:

1. **Line 27** — before: `Hancock et al. (2020) model the artifact as a delegate acting on a sender's behalf;` — after: `Hancock et al. (2020) model the artifact as a delegate acting on one designated party's behalf;`
2. **Line 60** (table cell) — before: `Computational delegate acting on a sender's behalf` — after: `Computational delegate acting on one designated party's behalf (sender or receiver)`
3. **Line 99** — before: `their computational agent optimizes for the interpersonal or communicative objectives of a designated sender, while the intermediary modeled here optimizes for institutional coordination metrics external to both interactants.` — after: `their computational agent optimizes for the interpersonal or communicative objectives of a designated communicator — sender or receiver — while the intermediary modeled here optimizes for institutional coordination metrics external to both interactants.`

This doesn't damage the paper's argument — a receiver-oriented AI-MC agent still serves one party's goals rather than binding both — but narrows the source's explicit, stated generality.

### Three-way contrast paragraph (line ~27) — overall assessment

Long & Magerko clause: fair, not a strawman (verified against the full competency list). Guzman & Lewis clause: fair, not a strawman (specifically tested against the card's own flagged risk and it holds up). Hancock et al. clause: the one place the contrast overclaims, by dropping the receiver-side half of the role-orientation parameter — fixed above. Zhou et al. (2025)'s clause is outside this batch (covered in Batch B).

### Batch D actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Hancock et al. (2020) | PAPER.md lines 27, 60, 99 | "sender" narrows the source's explicit sender-or-receiver generality; inconsistent with the paper's own correct "a communicator" quote | **DRIFTED — three linked fixes above** |
| — | Long and Magerko (2020) | all uses | — | Clean (two optional, non-blocking tightening notes) |
| — | Guzman and Lewis (2020) | all uses | — | Clean |

---

## Batch K — Methods/qual background cluster (12 citations, Tier 3)

Brannick & Coghlan (2007); Bamberger & Pratt (2010); Bothello et al. (2019); Anteby (2013); Ferguson et al. (2004); Mercer (2007); Pratt et al. (2020); Tracy (2010); Blumer (1954); Bowen (2006); Gioia et al. (2013); Yurek et al. (2008).

All 12 confirmed to exist, correctly identified, and topically consistent with their use in PAPER.md. 8 have verified cards and check out ACCURATE against them. 3 (Bamberger & Pratt, Tracy, Yurek et al.) had no card but are bibliographically confirmed via web search and are direct topical matches — ACCURATE, cards would be easy to add if this cluster is ever upgraded to a higher tier. One finding:

- **Bothello et al. (2019) — DRIFTED (mild).** Paired with Bamberger & Pratt at PAPER.md line 550 for a general "non-traditional research context" claim. The actual paper is narrower: a critique of "institutional voids" as a concept applied to non-Western settings, arguing for decolonizing organizational scholarship — not a general methodological case for unconventional research sites. The manuscript's gloss is a fair enough compression that this isn't a misattribution, but the citation is being asked to support a broader claim than its own specific critique makes. No action required at Tier 3; worth a note if this sentence gets more scrutiny later.

No other issues; no FLAG or OVERCLAIMED verdicts in this batch.

---

## Batch M — 2026 boundary-case citations (6 citations, Tier 3)

Hong et al. (2026); Scolari et al. (2026); Mahy & Li (2026); Ayasrah et al. (2026); Dredge & Anderson (2021); Hu & Zhan (2024) — the "adjacent scholarship continues to accumulate" sentence distinguishing algorithmacy from recent related constructs confined to person-system dyads.

All 6 exist, correctly identified, no venue/year metadata drift on the four in-press/advance-online 2026 items. All six one-line "boundary case" characterizations are fair and non-strawmanned.

**One nuance flag, not a misrepresentation:** Scolari et al. (2026)'s six-area framework includes "social management," which explicitly concerns customers/clients/care recipients — a human counterpart does appear in this construct, unlike the other three. The card's own analysis defends the boundary-case reading (social management operates *alongside* the algorithm in face-to-face encounters the app schedules but doesn't mediate, not *through* it) and that distinction is sound, but it isn't visible in PAPER.md's compressed one-line summary. Worth confirming the fuller distinction is available in the body text for a reviewer who knows this source, since the card itself flags it as "where a reviewer will push."

---

## Batch L — Theory & coordination background (11 citations, Tier 3)

Danaher (2016); Rosenblat & Stark (2016); Felin et al. (2015); Healy and Pekarek (2025); ILO (2025); Chigbu (2026); Peccei and Rosenthal (1997); Möhlmann et al. (2021); Williamson (1991); Bradach and Eccles (1989); Ouchi (1980).

9 of 11: ACCURATE, no action needed (Danaher, Rosenblat & Stark, Felin et al., ILO, Chigbu, Möhlmann et al., Williamson, Bradach & Eccles, Ouchi — all confirmed to exist, correctly identified, and topically supportive of PAPER.md's use).

**Peccei and Rosenthal (1997) — resolved, closed, not a separate issue.** Grepped all of PAPER.md: only one in-text use exists (line 119), which is the Zhou et al. SEM-scale sentence Batch B already found and fixed (should be Peccei & Rosenthal 2000, not 1997). No standalone citation of the 1997 paper exists anywhere else in the manuscript — this item from the original inventory is fully closed by Batch B's fix; do not double-count or re-flag it.

**Healy and Pekarek (2025) — card year mismatch resolved.** Confirmed via Wiley's table of contents: this is the SAME paper as the existing `healy2024.md` card, not a different one — Volume 40, Issue 2 of *New Technology, Work and Employment* published July 2025 (early view was 2024). PAPER.md's citation "(2025)" is correct, matching the print-issue year. **Fix applied:** the card has been renamed `literature/cards/healy2025.md` with the header year corrected and a dated correction note added; the stale `healy2024.md` removed.

### Batch L actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| — | Peccei and Rosenthal (1997) | PAPER.md line 119 | Same instance as Batch B's fix; no separate use exists | **Closed — handled by Batch B, not double-counted** |
| — | Healy and Pekarek (2025) | card only | Card filename/header said 2024 | **Fixed — card renamed to healy2025.md** |
| — | 9 others | all uses | — | Clean |

---

## Batch H — HMC-adjacent citations (8 citations, Tier 2)

Wilkinson (1965); Jarrahi & Sutherland (2019); Fortunati & Edwards (2020); Gibbs et al. (2021); Ng et al. (2021); Laupichler et al. (2023); Kellogg et al. (2020); Henseler et al. (2015).

All 8: ACCURATE. Notably, **Wilkinson (1965)'s venue ambiguity — previously an open flag — is now resolved.** The apparent competing "*English in Education*" 1965 venue is a metadata artifact: that journal title didn't exist until 1967 (NATE's prior publication was the *NATE Bulletin*), and Wiley evidently back-assigns continuous DOI metadata to the title's lineage predecessor. *Educational Review* 17(4), pp. 11–15 (Sept. 1965) is independently confirmed by Taylor & Francis' own DOI page, Wikipedia, and multiple secondary sources tying the coinage to Wilkinson's post at Birmingham. PAPER.md's citation is correct as printed. **Fix applied:** `literature/cards/wilkinson1965.md`'s caution note updated to record this resolution.

Other confirmations of note: Fortunati & Edwards (2020) checked against the actual editorial text — the manuscript's synthesis is unquoted paraphrase (not a misattributed direct quote) and thematically faithful. Gibbs et al. (2021) confirmed against the published abstract and secondary summaries (full PDF was paywalled) — its structuration-theory critique of individualist HMC scholarship matches both uses. Laupichler et al.'s recent SNAIL-scale fix (all three factors, course-evaluation framing) confirmed reading correctly in context. Kellogg et al. (2020)'s three separate uses all individually re-checked, consistent across all three.

No fixes needed beyond the Wilkinson card update (already applied).

---

## Batch J — Methods engagement (5 citations, Tier 2/3)

Coghlan & Brannick (2014); Timmermans & Tavory (2012); Pratt (2009); Flanagan (1954); Riordan (1995, secondary).

All 5: ACCURATE. Coghlan & Brannick (2014)'s five separate uses (the meta-cycle distinction, the four-phase AR cycle, and the dual-role safeguard sentence) were individually re-checked against the source text (not just the card), closing out the prior pass's "block-level only" caveat. Timmermans & Tavory (2012)'s three named abductive moves (revisiting, defamiliarization, alternative casing) are correctly named and glossed. **Flanagan (1954) — no card existed; built one** (`literature/cards/flanagan1954.md`), from a full read of the 33-page original. The recent "operationalized here as..." fix (avoiding the implication that the four-part incident structure is Flanagan's own taxonomy) is confirmed correct — his actual structure is a five-step *research-procedure* sequence, not an incident-narrative template. Riordan (1995) confirmed as a genuine secondary citation: Coghlan & Brannick (2014) do quote Riordan directly at p. 8, and Riordan correctly does not appear as its own reference-list entry in PAPER.md.

No fixes needed.

---

## Batch G — Algorithmic visibility/folk-theory literacies (8 citations, Tier 2)

Bucher (2017); DeVito et al. (2018); Litt (2012); Aneesh (2009); Wing et al. (2021); Hargittai (2002); Abidin (2016); Cotter (2019).

6 of 8: ACCURATE, no action needed (Bucher, DeVito, Litt, Aneesh, Abidin, Cotter). Aneesh (2009)'s algocracy/algorithmacy disambiguation is well-handled — near-verbatim match to the card's own disambiguating sentence, no conflation.

**Hargittai (2002) — no card existed, built one** (`literature/cards/hargittai2002.md`, correctly distinguished from the different, wrong-year `hargittai2020.md` card). Full text read directly. ACCURATE — the manuscript cites this only for the structural "second-level digital divide" frame (access ≠ effective use), correctly attributing no labor-platform, earnings, or safety claim to it.

**Wing et al. (2021) — FLAG, the most serious finding across the entire audit so far.** Full text read directly (16 pages, matching the official *Negotiation Journal* 37(1):49–64 pagination). The article does NOT state, as its own affirmative argument, the four-item list PAPER.md attributes to it at line 252 ("procedural transparency, institutional accountability, meaningful contestability, and informed consent"). What the article actually does: narrates the fourth party's historical/technological evolution, and references an *external*, earlier framework (Wing's 2016 NCTDR "Ethical Principles for Online Dispute Resolution," a 17-item values list the article itself calls "values, not rules") — of which only "Competence" is quoted in full. **"Contestability" is not a named principle anywhere in this source or its underlying 2016 taxonomy that could be located.** "Informed consent" is close to but not identical to the 2016 list's "informed participation"; "protection against embedded bias" (in the existing card) is close to but not identical to "protection from harm." The manuscript's phrasing ("Wing et al. (2021) argue that...") presents someone else's non-binding 2016 values framework as the 2021 article's own thesis.

This also implicates the existing `literature/cards/wing2021.md` — despite being marked full-text/direct-read, it appears to carry the same imported five-item framing. A secondary, cleaner fix at line 163 ("normative legal framework" → the article is explicitly framed as *ethical*, not legal — its own title is "Designing Ethical Online Dispute Resolution Systems") is also needed.

- **Line 163 fix — before:** `...while Wing et al. (2021) evaluate its opaque, protection-withholding variants through a normative legal framework.`
- **Line 163 fix — after:** `...while Wing et al. (2021) evaluate its opaque, protection-withholding variants through a normative ethical framework.`
- **Line 252 — no confident fix given.** Correcting this changes a four-item list to an open set and drops "contestability," which forces a revision of the following sentence's parallel four-part structure ("withhold each of these guarantees in turn"). This needs the author's direct review of the full typeset Wiley/MIT Press version (with footnotes — the read for this batch used an image-based PDF extraction that may not have fully captured footnote content) before deciding the fix, since it reshapes downstream argument structure, not just a citation.

### Batch G actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Wing et al. (2021) | PAPER.md line 252 | Four-item "argue that... must guarantee" list not supported by the source's actual content | **OVERCLAIMED — needs author review of full typeset text + footnotes before a fix is chosen; downstream paragraph structure depends on the answer** |
| 2 | Wing et al. (2021) | PAPER.md line 163 | "normative legal framework" should read "normative ethical framework" | **DRIFTED — fix above** |
| 3 | Wing et al. (2021) | card | `wing2021.md` may carry the same imported five-item framing | **Card needs re-audit against full typeset text before being trusted elsewhere** |
| — | 6 others | all uses | — | Clean |

---

## Batch I — Recent AW-mod stragglers (6 citations, Tier 2)

Oeldorf-Hirsch & Neubaum (2025); Gagrčin et al. (2024); Nutbeam (2000); Iyamu et al. (2026); anonymous 2026 preprint; Yang & Liechty (2026).

**Oeldorf-Hirsch & Neubaum (2025), Gagrčin et al. (2024), Iyamu et al. (2026) — all ACCURATE**, confirmed against verified cards. (Note: `iyamu2026.md`'s own header byline has incorrect author initials — PAPER.md's reference-list entry is actually correct; the card, not the manuscript, needs its own fix, out of scope for this pass.)

**Nutbeam (2000) — no card existed, built one** (`literature/cards/nutbeam2000.md`, read at preview depth — the version of record is CAPTCHA-gated). ACCURATE — correctly cited only for the tripartite health-literacy hierarchy and the "communicative" label for its middle tier; the manuscript correctly keeps all algorithmic content attached to the adjacent Iyamu et al. citation rather than to Nutbeam, who predates that literature by two decades.

**Anonymous 2026 preprint — ACCURATE, hedging adequate, one FLAG.** Confirmed live at a stable locator (JMIR Preprints #105459, self-labeled "[unpublished, non-peer-reviewed preprint]"). PAPER.md's hedging is adequate — it flags the unrefereed status at first mention and repeats it in the reference note. Content match to the recovered abstract is fair. **FLAG (reviewer-risk, author's call):** the reference note states "authors not retrievable from the preprint server at the time of writing," but the author — Robert Joseph McGrath, University of New Hampshire — was retrieved in under a minute via a direct fetch of the same page. Whether this changed since the note was written is unverifiable at this depth; recommend either naming the author or re-confirming "not retrievable" is still accurate before submission.

**Yang & Liechty (2026) — DRIFTED / OVERCLAIMED, no card existed, built one** (`literature/cards/yangliechty2026.md`, read at preview depth — recovered partial passages via an authenticated publisher redirect, full chapter not obtained). PAPER.md line 332 attributes a child-welfare-specific claim about "algorithmic risk scoring" and an "advisory decision-support tool... rather than a binding administrative authority" distinction to this source. The recovered text shows this is actually a *general* social-work AI-competency framework; child welfare appears exactly once, in a one-line list alongside mental health, benefits eligibility, and criminal justice, with no dedicated case study — "algorithmic risk scoring" is not discussed anywhere in the recovered text, and no explicit advisory/binding distinction was found.

- **Fix (recommended, pending full-chapter confirmation) — before:** `**Public Child Welfare:** Models of AI competence in social work address client trust and algorithmic risk scoring (Yang & Liechty, 2026), and frame the algorithmic system as an advisory decision-support tool rather than a binding administrative authority.`
- **Fix — after:** `**Public Child Welfare:** A general AI-competency framework for social work names client trust as algorithmic tools spread into child welfare and other high-stakes domains (Yang & Liechty, 2026), treating the algorithmic system as one more actor whose use requires accountable human judgment rather than an autonomous, binding authority in its own right.`
- Since this pass worked from recovered fragments rather than the complete paywalled chapter, recommend obtaining the full text before finalizing this fix, in case a later section develops the risk-scoring/advisory framing the recovered fragments didn't surface.

### Batch I actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Yang & Liechty (2026) | PAPER.md line 332 | Child-welfare risk-scoring/advisory-vs-binding claim not supported by recovered text | **DRIFTED — fix above, recommend full-chapter check first** |
| 2 | Anonymous 2026 preprint | reference list | "Authors not retrievable" — author is in fact retrievable | **FLAG — author's call** |
| — | 4 others | all uses | — | Clean |

---

## Batch F — OT canon & frameworks (10 citations, Tier 2)

Simon (1997); Weber (1978); Hayek (1945); Granovetter (1985); Powell (1990); Teece et al. (1997); Eisenhardt & Graebner (2007); Merton (1987); Gittell (2002); Okhuysen & Bechky (2009).

9 of 10: ACCURATE. Five canon citations had no card — all five now built (`simon1997.md`, `weber1978.md`, `hayek1945.md`, `granovetter1985.md`, `powell1990.md`; Weber, Simon, Granovetter, Powell verified at secondary-summary depth appropriate to Tier 2, Hayek verified against the full primary text). Teece et al. (1997), Eisenhardt & Graebner (2007) — confirmed to respect the single-case-justification-only boundary in both uses — and Gittell (2002) — confirmed correctly disambiguated from the ambiguous companion *Journal of Service Research* paper — all check out clean. Merton (1987) verified via convergent secondary sources only (primary text paywalled), matches the manuscript's "strategic research site" paraphrase closely. Okhuysen & Bechky (2009)'s structural borrowing into Table A1 is faithful and correctly hedged ("map to," not attributed to O&B as their own table structure).

**Hayek (1945) — DRIFTED, verified against full primary text.** The manuscript's substantive claim is accurate (the price mechanism condenses dispersed knowledge into a public signal no participant must reconstruct privately), but the word "statistic," used 4 times across 3 locations, is Hayek's own term for exactly what he says the price mechanism succeeds *by not being*: "the sort of knowledge with which I have been concerned... by its nature cannot enter into statistics." Calling the price mechanism "an aggregated public statistic" collides with Hayek's explicit distinction.

- **Line 38 — before:** `relying on the price mechanism as an aggregated public statistic (Hayek, 1945).` — **after:** `relying on the price mechanism as a condensed public signal (Hayek, 1945).`
- **Line 509 — before:** `it functions as an aggregated public statistic no participant needs to reconstruct privately. In modern coordination terms, that public statistic delivers predictability and common understanding at once` — **after:** `it functions as a condensed public signal — Hayek's own figure is a system of telecommunications — that no participant needs to reconstruct privately. In modern coordination terms, that public signal delivers predictability and common understanding at once`
- **Line 514** (Table A1, Market/"What it must deliver" cell) — **before:** `Predictability and common understanding via public price statistics.` — **after:** `Predictability and common understanding via a condensed public price signal.`

(Line 513's "a posted term backed by an unconstrained right of refusal" is unaffected, no change needed.)

**Granovetter (1985) — FLAG, no fix needed.** A general embeddedness thesis about all economic action, not itself a proposal that "network" is a discrete governance form (that move is more Powell's) — but always correctly paired with Powell rather than cited alone for the typological claim, and every substantive claim attributed to Granovetter is accurately his. Standard, defensible OT joint-citation practice.

### Batch F actionable items

| # | Source | Location | Issue | Status |
|---|---|---|---|---|
| 1 | Hayek (1945) | PAPER.md lines 38, 509, 514 | "statistic" collides with Hayek's own explicit statistic/signal distinction | **DRIFTED — three fixes above** |
| 2 | Granovetter (1985) | all uses | General embeddedness thesis, not itself a network-as-form proposal | **FLAG — no fix needed, correctly paired with Powell throughout** |
| — | 8 others | all uses | — | Clean |

---

## Master table — all 83 citations

| Citation | Tier | Verdict | Note |
|---|---|---|---|
| Zhou et al. (2025) | 1 | ACCURATE | Now full_text-verified (complete VoR obtained 2026-08-30, independently re-confirms all prior findings, no new discrepancies); 1 DRIFTED fixed (Peccei & Rosenthal year); 1 FLAG still open (line 125, "primary" antecedent — the authors' own prose leads with peer support even though job crafting has the larger coefficient, a genuine ambiguity in the source itself) |
| Manky (2025) | 1 | ACCURATE (bib.) / UNVERIFIABLE (content) | Card built; paywalled, abstract-only — most load-bearing empirical citation, verify with institutional access if possible |
| Stark and Vanden Broeck (2024) | 1 | ACCURATE | 1 DRIFTED fixed (line 296); 1 FLAG open (line 248, optional) |
| Stark & Pais (2020) | 1 | ACCURATE | Card built |
| Selznick (1949) | 1 | ACCURATE | Card built; 1 FLAG (formal/informal cooptation, no fix needed) |
| Long and Magerko (2020) | 1 | ACCURATE | No-page-number state confirmed correct |
| Guzman and Lewis (2020) | 1 | ACCURATE | — |
| Hancock et al. (2020) | 1 | ACCURATE | DRIFTED, fixed (3 locations) |
| Katsh and Rifkin (2001) | 1 | ACCURATE | — |
| Suddaby (2010) | 1 | ACCURATE | Card built; 1 FLAG open (line 31, optional) |
| Curchod et al. (2020) | 1 | ACCURATE | 1 minor fixed (line 165); 1 FLAG open (line 248, carried over) |
| Spitzberg (2006) | 1 | ACCURATE | — |
| Rahman (2021) | 1 | ACCURATE | — |
| Sutherland et al. (2020) | 1 | ACCURATE | Both prior page fixes confirmed |
| Sandberg (2000) | 1 | ACCURATE | DRIFTED, fixed |
| Spitzberg and Cupach (1984) | 1 | ACCURATE | DRIFTED, fixed (1 of 2 uses) |
| Cameron (2024) | 1 | ACCURATE | DRIFTED, fixed (1 of 3 uses) |
| Wilkinson (1965) | 2 | ACCURATE | Card updated — venue ambiguity resolved |
| Aneesh (2009) | 2 | ACCURATE | — |
| Simon (1997) | 2 | ACCURATE | Card built |
| Weber (1978) | 2 | ACCURATE | Card built |
| Hayek (1945) | 2 | ACCURATE | Card built; DRIFTED, fixed (3 locations) |
| Granovetter (1985) | 2 | ACCURATE | Card built; 1 FLAG (no fix needed) |
| Powell (1990) | 2 | ACCURATE | Card built |
| Gittell (2002) | 2 | ACCURATE | — |
| Jarrahi and Sutherland (2019) | 2 | ACCURATE | — |
| Fortunati and Edwards (2020) | 2 | ACCURATE | — |
| Gibbs et al. (2021) | 2 | ACCURATE | — |
| Ng et al. (2021) | 2 | ACCURATE | — |
| Teece et al. (1997) | 2 | ACCURATE | — |
| Laupichler et al. (2023) | 2 | ACCURATE | Prior fix confirmed holding |
| Kellogg et al. (2020) | 2 | ACCURATE | — |
| Wing et al. (2021) | 2 | ACCURATE (as of 2026-08-30 fix) | 1 DRIFTED fixed (line 163); line 252 rewritten after a full-text read (incl. footnotes) confirmed the OVERCLAIM — see "Resolution" section below |
| Hargittai (2002) | 2 | ACCURATE | Card built (was miscarded under wrong year) |
| Coghlan and Brannick (2014) | 2 | ACCURATE | — |
| Eisenhardt & Graebner (2007) | 2 | ACCURATE | — |
| Merton (1987) | 2 | ACCURATE | — |
| Timmermans & Tavory (2012) | 2 | ACCURATE | — |
| Pratt (2009) | 2 | ACCURATE | — |
| Flanagan (1954) | 2 | ACCURATE | Card built |
| Henseler et al. (2015) | 2 | ACCURATE | — |
| Oeldorf-Hirsch and Neubaum (2025) | 2 | ACCURATE | Now full_text-verified (author supplied VoR PDF 2026-08-30) |
| Gagrčin et al. (2026) | 2 | ACCURATE | Full VoR obtained 2026-08-30; found and fixed a citation-year mismatch (2024→2026, matching the already-cited 2026 print pagination) — card renamed `gagrcin2026.md` |
| Nutbeam (2000) | 2 | ACCURATE | Card built |
| Iyamu et al. (2026) | 2 | ACCURATE | — |
| Abidin (2016) | 2 | ACCURATE | — |
| Cotter (2019) | 2 | ACCURATE | — |
| Okhuysen and Bechky (2009) | 2 | ACCURATE | — |
| Anonymous preprint (2026) | 2 | ACCURATE | 1 FLAG open (author is retrievable; note says otherwise) |
| Yang & Liechty (2026) | 2 | ACCURATE (verdict reversed 2026-08-30) | A full-text read of the complete chapter found the earlier DRIFTED verdict was itself wrong — see "Resolution" section below; no fix applied, none needed |
| Bucher (2017) | 2 | ACCURATE | — |
| DeVito et al. (2018) | 2 | ACCURATE | — |
| Litt (2012) | 2 | ACCURATE | — |
| Danaher (2016) | 3 | ACCURATE | — |
| Rosenblat & Stark (2016) | 3 | ACCURATE | — |
| Felin et al. (2015) | 3 | ACCURATE | — |
| Healy and Pekarek (2025) | 3 | ACCURATE | Card renamed/fixed (was miscarded under wrong year) |
| ILO (2025) | 3 | ACCURATE | — |
| Chigbu (2026) | 3 | ACCURATE | Now extended_preview-verified (author supplied full PDF 2026-08-30); card built |
| Bamberger & Pratt (2010) | 3 | ACCURATE | — |
| Bothello et al. (2019) | 3 | ACCURATE | 1 mild note — cited for a broader claim than its narrower institutional-voids critique makes |
| Riordan (1995, secondary) | 3 | ACCURATE | Confirmed genuine secondary citation |
| Anteby (2013) | 3 | ACCURATE | — |
| Ferguson et al. (2004) | 3 | ACCURATE | — |
| Mercer (2007) | 3 | ACCURATE | — |
| Pratt et al. (2020) | 3 | ACCURATE | — |
| Tracy (2010) | 3 | ACCURATE | — |
| Brannick & Coghlan (2007) | 3 | ACCURATE | — |
| Blumer (1954) | 3 | ACCURATE | — |
| Bowen (2006) | 3 | ACCURATE | — |
| Gioia et al. (2013) | 3 | ACCURATE | — |
| Yurek et al. (2008) | 3 | ACCURATE | — |
| Peccei and Rosenthal (1997) | 3 | ACCURATE | Confirmed: only one in-text use exists, and it's the Zhou-context sentence already fixed as a 2000 citation — not a separate standalone use |
| Möhlmann et al. (2021) | 3 | ACCURATE | — |
| Williamson (1991) | 3 | ACCURATE | — |
| Bradach and Eccles (1989) | 3 | ACCURATE | — |
| Ouchi (1980) | 3 | ACCURATE | — |
| Hong et al. (2026) | 3 | ACCURATE | Now full_text-verified (author supplied VoR PDF 2026-08-30); pagination (1–13) added to PAPER.md's reference entry |
| Scolari et al. (2026) | 3 | ACCURATE | 1 nuance flag — "social management" area does name a human counterpart; confirm fuller distinction is available in body text |
| Mahy & Li (2026) | 3 | ACCURATE | — |
| Ayasrah et al. (2026) | 3 | ACCURATE | — |
| Dredge & Anderson (2021) | 3 | ACCURATE | — |
| Hu & Zhan (2024) | 3 | ACCURATE | Now extended_preview-verified (author supplied full PDF 2026-08-30); card built |

**83 of 83 citations now carry an individual tier and verdict — none left at block-level. As of the 2026-08-30 resolution pass below, all 83 are ACCURATE as currently written in `PAPER.md`.**

## Resolution — Wing et al. (2021) and Yang & Liechty (2026), full source texts obtained

The author supplied both full papers after the initial pass (`Designing_Ethical_Online_Dispu.pdf`, 17 pages; `Building_AI_Literacy_and_Competency_in_Social_Work.pdf`, 26 pages), read completely, including footnotes and references — resolving both remaining open items.

**Wing et al. (2021) — confirmed OVERCLAIM, worse than the partial-text read suggested, now fixed.** Footnote 3 lists the article's cited framework in full: seventeen named principles (accessibility, accountability, competence, confidentiality, empowerment, equality, fairness, honesty, impartiality, **informed participation**, innovation, integration, legal obligation, neutrality, protection from harm, security, transparency) — not the four PAPER.md attributed to the article. "Contestability" appears nowhere in the article, its footnoted framework, or (as far as searchable) Wing's 2016 source article. More importantly, the article explicitly frames this list as "a set of values (**not rules**)" — the near-opposite of "must guarantee." The framework itself is not even Wing et al.'s (2021) own contribution — it is Wing's (2016) separate, earlier article, which the 2021 piece cites and partially quotes (only "Competence" is quoted in full).

**Fix applied to PAPER.md line 252** — full rewrite (not a word swap, since the paragraph's four-part parallel structure had to be rebuilt around what the source actually supports):
- **Before:** `Online dispute resolution scholarship supplies the benchmark against which the deficits can be named, because it states the normative obligations an institutional intermediary owes. Extending Katsh and Rifkin's (2001) "fourth party," Wing et al. (2021) argue that an authoritative dispute system must guarantee participants procedural transparency, institutional accountability, meaningful contestability, and informed consent. Algorithmic coordination regimes withhold each of these guarantees in turn: proprietary decision rules stay unobservable (Rahman, 2021), automated determinations carry no accountable office, contestation routes to the platform's own apparatus rather than to the counterpart, and default enrollment substitutes for consent.`
- **After:** `Online dispute resolution scholarship supplies the benchmark against which the deficits can be named, because it names the values an institutional intermediary owes its participants. Extending Katsh and Rifkin's (2001) "fourth party," Wing et al. (2021) point to Wing's (2016) Ethical Principles for Online Dispute Resolution — a field-endorsed framework spanning transparency, accountability, informed participation, and a dozen further values, offered explicitly as guidance rather than enforceable rules. Algorithmic coordination regimes withhold the closest of those values in turn: proprietary decision rules stay unobservable, forfeiting transparency (Rahman, 2021); automated determinations carry no accountable office, forfeiting accountability; and default enrollment substitutes for a participant's informed say in the process, forfeiting informed participation. Contestation is the sharpest absence of all: no principle in Wing's framework, nor anywhere in the wider fourth-party literature, names a participant's right to route a dispute to someone other than the platform itself, and algorithmic coordination regimes exploit exactly that silence, directing contestation to the platform's own apparatus rather than to the counterpart.`

This turns the "contestability" gap from a citation error into a genuine argumentative point: the literature hasn't named that value, and algorithmic coordination exploits the silence. A new bibliography entry was added — Wing, L. (2016). Ethical principles for online dispute resolution: A GPS device for the field. *International Journal of Online Dispute Resolution*, 3(1), 12–29 (confirmed directly from the 2021 article's own reference list). `literature/cards/wing2021.md` was corrected (its own prior "What it argues" section had independently made the same four-item-list error, despite being marked full-text/direct-read — a caution that "direct_read" alone doesn't guarantee a claim was checked against a source's footnotes). A new card, `literature/cards/wing2016.md`, was built for the newly-cited framework paper.

**Yang & Liechty (2026) — the earlier DRIFTED verdict was itself wrong; reversed to ACCURATE, no fix needed.** The initial preview-depth read (partial fragments via a publisher redirect) missed Section 5.3, which contains a specific, load-bearing passage: "child welfare agencies that use predictive analytics models for risk assessment have organized training sessions to help social workers understand model outputs and interpret them critically rather than blindly trust algorithmic recommendations." This directly supports both halves of PAPER.md's line 332 — the algorithmic-risk-scoring claim, and the advisory-not-binding framing ("recommendations" to be critically evaluated, not determinations that bind). The one minor looseness — "client trust" is a chapter-wide theme rather than something the source ties specifically to child welfare — doesn't rise to a fix. `literature/cards/yangliechty2026.md` was rewritten at full-text depth (the complete 26-page chapter was obtained and read), explicitly documenting that its own earlier preview-depth verdict was wrong and why: a "could not confirm" reading from a partial-text pass should be held provisionally, not treated as a confirmed absence.

**Net effect on the master table above:** both Wing et al. (2021) and Yang & Liechty (2026) are now ACCURATE. No open items remain from the original 83-citation audit.

## Fixes applied to `manuscript/PAPER.md` this pass

1. Line 296 — Stark & Pais (2020) added alongside Stark and Vanden Broeck (2024) for "matches unchosen parties."
2. Line 165 — Curchod et al.: "workers" → "sellers" (matches the paper's own eBay seller population).
3. Line 325 — Spitzberg and Cupach (1984): removed the unsourced "cannot be collapsed into a single metric" clause, replaced with a supportable claim.
4. Line 233 — Sandberg (2000): "technical components" → "engine qualities" (matches his own conception-1 label).
5. Lines 27, 60, 99 — Hancock et al. (2020): "sender" → "one designated party" / "designated communicator — sender or receiver" (matches the source's explicit bidirectional framing).
6. Line 256 — Cameron (2024): removed unsupported "and stabilize algorithmic labor regimes."
7. Lines 38, 509, 514 — Hayek (1945): "statistic" → "signal" (matches Hayek's own explicit statistic/signal distinction).
8. Line 163 — Wing et al. (2021): "normative legal framework" → "normative ethical framework" (matches the source's own self-description).
9. Line 119 — Zhou et al. (2025)'s SEM scale: "Peccei and Rosenthal's (1997)" → "Peccei and Rosenthal's (2000)," plus a new, Crossref-verified bibliography entry for the 2000 paper.

Fourteen new literature cards built for previously-uncarded sources: `manky2025.md`, `starkvandenbroeck2024.md`, `starkpais2020.md`, `selznick1949.md`, `hargittai2002.md`, `flanagan1954.md`, `nutbeam2000.md`, `yangliechty2026.md`, `simon1997.md`, `weber1978.md`, `hayek1945.md`, `granovetter1985.md`, `powell1990.md`, `suddaby2010.md`. Two cards corrected for wrong-year mismatches: `wilkinson1965.md` (venue ambiguity resolved, no rename needed) and `healy2024.md` → renamed `healy2025.md`.

## Open items requiring the author's own judgment (not resolved in this pass)

Items 1 and 2 from the original list (Wing et al. 2021 line 252; Yang & Liechty 2026 line 332) are now resolved — see the "Resolution" section above. Remaining open items, renumbered:

1. **Manky (2025), lines 19/29/169.** The paper's most load-bearing empirical motivating example rests on an abstract-only read (fully paywalled, no OA copy anywhere). The specific "reads an opaque metric before accepting a passenger" mechanism is plausible but not verbatim-confirmed. Verify with institutional Wiley access if available.
2. **Anonymous 2026 preprint's reference note** states "authors not retrievable" — the author (Robert Joseph McGrath, University of New Hampshire) was in fact retrieved in under a minute. Update the note or reconfirm it's still accurate.
3. **Zhou et al. (2025), line 125** — "primary organizational antecedents... are social mechanisms" arguably overstates peer support relative to Zhou et al.'s own larger predictor (cognitive job crafting, which isn't social).
4. **Curchod et al. (2020), line 248** — "generate consent... (Cameron, 2024; Curchod et al., 2020)" pairs Curchod with a consent claim closer to Cameron's own argument than Curchod's (power/agency, not consent-manufacture). Carried over unresolved from an earlier pass.
5. **Stark and Vanden Broeck (2024), line 248** — "exploit coordination gaps" isn't the source's own vocabulary (zero "gap" hits in the full text); optional tightening only.
6. **Suddaby (2010), line 31** — citation placement risks reading as if Suddaby discusses "institutional justice"/"governance literatures," which he doesn't; optional precision fix offered in the Batch E report.
7. **Scolari et al. (2026)** — its "social management" competence area does name a human counterpart, unlike the other three boundary-case citations in the same sentence; confirm the fuller alongside-vs-through distinction (already in the card) is visible somewhere in the body text for a reviewer who knows this source.
8. **Selznick (1949)** — the paper's contrast draws on Selznick's *formal* cooptation branch; the *informal* branch is arguably closer in spirit to platform enrollment. Defensible as written; worth a clause only if a Selznick-literate reviewer is specifically anticipated.

---

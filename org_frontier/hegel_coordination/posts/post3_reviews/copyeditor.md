# Copyedit & citation review (round 2) — post3_syllogism.md (draft v4)

File reviewed: `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/hegel_coordination/posts/post3_syllogism.md`
Prior review: `posts/post3_reviews/copyeditor.md` (on v3). Line numbers below refer to v4 as read.

**Step 0 — register.** First-person Substack essay in an academic register. Voice, em-dash density, and
"I/my" are house style, not flagged. This review covers citation integrity, quotation accuracy, APA
mechanics, cross-references, arithmetic, and series edition consistency only. Series guards respected: no
finding pushes the paper toward "Hegel anticipated Φ" or toward demoting Φ.

---

## 1. Verdict + single most important mechanical fix

**VERDICT: Nearly clean. v4 closed the great majority of the v3 punch list — the 2010a/2010b re-lettering is
done and correct, the four unsourced works (Vieweg/Lawvere/Günther/Protin) now have entries, the Stein p. 149
block quote is set, the German title is bracketed, *Encyclopaedia*→*Encyclopedia* and the heading case are
fixed, first names are dropped, §198R has its page, and "suggests" replaced "implies." Citation resolution is
now perfectly two-way: zero orphans, zero danglers. What remains is one verified misattribution, one
quotation-italics inconsistency, one stale reference entry, one series-level DOI decision, and the still-open
Paper/Post naming split.**

**Single most important mechanical fix (verified against the source):** the quotation at **line 248**,
"in things spiritual the center, and the union with it, assume higher forms," is credited to **(Sans, 2018,
p. 206)** but it is **Hegel's words** (di Giovanni's translation), which Sans reproduces in quotation marks
with his own dual locator. I opened the Sans chapter PDF and confirmed it: Sans writes *…spirit as such
transcends mechanism. This is the reason why "in things spiritual the center, and the union with it, assume
higher forms" (143; 641).* The "(143; 641)" is Sans's GW-page / di-Giovanni-page locator, so the words are
Hegel's at di Giovanni **p. 641** — the same page as the paper's own real-middle quotation. This is the one
Hegel-within-Sans quote the v4 pass missed: the sourcing note (lines 468–469) claims *four* re-attributed but
only did three (631, 641-individualized, 643-gravity); this fourth (641, "higher forms") stayed on Sans.
Re-attribute it. Ready-to-paste in §7 below.

---

## 2. Citation-resolution table (in-text ↔ reference)

Every in-text token resolves; every entry is cited. **No orphans, no danglers.** (Confirmed independently by
`check_editions.py`, which raised no per-post3 dangling/orphan error, and by manual sweep.)

| In-text token (form used) | Where | Reference entry | Resolves? |
|---|---|---|---|
| Hegel, 1816/**2010b** (SL, di Giovanni English) | 22, 48, 116, 127, 139, 146, 171 | Hegel (2010b), *The science of logic* (di Giovanni) | ✓ correct suffix |
| Hegel, 1830/**2010a** (EL, Brinkmann/Dahlstrom) | 51, 173, 183 | Hegel (2010a), *Encyclopedia… Part I: Science of logic* (B&D) | ✓ correct suffix |
| Hegel, 1816/**1979** (SL, German Suhrkamp) | 151 | Hegel (1979), *Wissenschaft der Logik II* (Werke 6) | ✓ |
| Sans, 2018 | 52, 58, 90, 92, 121, 149, 159, 241, 248 | Sans (2018) | ✓ |
| Redding, 2023 | 97, 358 | Redding (2023) | ✓ (p. 43 and p. 227) |
| Stein, 2016 | 280, 285, 288, 291, 305 | Stein (2016) | ✓ |
| Albantakis et al., 2023 | 230 | Albantakis et al. (2023) | ✓ |
| Oizumi et al., 2014 | 230 | Oizumi et al. (2014) | ✓ |
| Christensen, 2024 | 231 | Christensen (2024) | ✓ (entry stale — see §6) |
| Smith, 1988 | 353 | Smith (1988) | ✓ |
| Vieweg, 2017 | 353 | Vieweg (2017) | ✓ (new in v4) |
| Harvey, 2002 | 354 | Harvey (2002) | ✓ |
| Lawvere, 1991 | 354 | Lawvere (1991) | ✓ (new in v4) |
| Protin, 2025 | 354 | Protin (2025) | ✓ (new in v4) |
| Günther, 1976–1980 | 356 | Günther (1976–1980) | ✓ (new in v4) |
| Burt, 1992 | 363 | Burt (1992) | ✓ |
| Obstfeld, 2005 | 363 | Obstfeld (2005) | ✓ |
| Simmel, 1908/1950 | 363 | Simmel (1950) | ✓ |

**a/b suffix consistency:** internally consistent throughout. SL = 2010b, EL = 2010a; reference list orders
Encyclopedia (2010a) before Science of logic (2010b), alphabetical by title (E before S, "The" ignored), and
Hegel 1979 precedes both by year. Correct per APA 7 §9.47.

**Bare-name mentions with no entry (acceptable):** Aristotle (357), Plato (via Redding, 358), Anselm and
Descartes (via Sans, 92). General historical attributions, no specific work cited, no entry required. Not
flagged. (Aristotle at 357 — "made the middle term the cause of the conclusion" — is borderline but standard
common-knowledge attribution; leave as is unless a venue demands a *Prior/Posterior Analytics* cite.)

**Orphan check, direction 2:** all 18 entries cited in the body. None uncited. The sourcing note's GW
locators and any note-only names live in the delete-before-posting block; no body orphan.

---

## 3. Quotation-check table

Legend: **VERIFIED** = matched against an openable source this session; **CORROBORATED** = page/wording
cross-checked via Sans's dual locators but the di Giovanni print page itself is gated; **GATED** = source not
openable, rests on the grounding run + internal consistency; **MISMATCH/ISSUE** = discrepancy found.

| Loc. | Claimed quote (short) | Cited as | Status |
|---|---|---|---|
| 22, 48 | "everything rational is a syllogism" (full sentence) | Hegel, SL p. 588 | CORROBORATED — Sans quotes the slogan at "(90; 588)," same page; Cambridge print gated. Given the same page each time. |
| 51 | "essential ground of everything true…'everything is a syllogism'" | Hegel, EL §181R p. 254 | GATED (B&D print). 38 words → run-in legal. Recount if emphases change at proof. |
| 116 | "composition, mixture, aggregate" | Hegel, SL p. 631 | CORROBORATED — Sans cites spirit material at "(133; 631)." |
| 118 | "the things connected in the spirit remaining external to one another and to spirit" | Hegel, SL p. 631 | CORROBORATED (was mis-credited to Sans in v3; correctly Hegel now). |
| 120 | "pervasive presence that is proper to spirit is lacking…" | Hegel, SL p. 631 | **VERIFIED via Sans** — Sans quotes "'pervasive presence that is proper to spirit' is lacking (133; 631)." Wording + page match. |
| 127 | "This positing consists…communication, which occurs without transition into the opposite" | Hegel, SL p. 635 | GATED (one-source; di Giovanni print). |
| 130 | "Laws, morals, rational conceptions…impose themselves on them" | Hegel, SL p. 636 | GATED. |
| 131 | "like a scent freely spreading in the unresisting atmosphere" | Hegel, SL pp. 635–636 | GATED. |
| 139 | "the real middle term…their objective universality" | Hegel, SL p. 641 | CORROBORATED — Sans quotes "the real middle term [reale Mitte]" and "objective universality" at "(143; 641)." |
| 141 | "individualized universality of the single objects and their mechanical process" | Hegel, SL p. 641 | CORROBORATED (Sans p. 203, at "(143; 641)"; was mis-credited to Sans in v3, correct now). |
| 146 | "This totality…constitutes free mechanism" | Hegel, SL pp. 642–643 | GATED. |
| 147 | "the pervasive gravity that persists self-identical in the particularization" | Hegel, SL p. 643 | CORROBORATED (Sans p. 205, "(145; 643)"; correct re-attribution). |
| 150 | "the real middle term [*reale Mitte*]" | Sans 2018 p. 203 | **VERIFIED** — Sans: "the real middle term [reale Mitte]" (brackets Sans's own). Exact. |
| 151 | "die *reelle* Mitte" | Hegel 1816/1979, Werke 6:423 | GATED (German print). Philology coherent — see §5. Minor italic note in §6. |
| 171 | political case, government/citizens/needs | Hegel, SL p. 642 | CORROBORATED — Sans, same page, quotes "The government, the individual citizens, and the needs…" |
| 173 | "the state is a system of three syllogisms" | Hegel, EL §198R p. 273 | GATED. Page now supplied (v3 lacked it). |
| 183 | "the subject joins itself together with itself by means of this mediation" | Hegel, EL §182 pp. 254–255 | GATED (two-source per sourcing note). |
| 58–60 | the middle term "founds its conclusion" | Sans 2018 p. 194 | **VERIFIED** — Sans: "The middle term of the syllogism founds its conclusion." Exact. |
| 90 | "Hegel's conviction that conceptual relations as such are real" | Sans 2018 p. 192 | VERIFIED in prior round; unchanged. |
| 92 | "aims at establishing the Concept as something objective, to wit really existing" | Sans 2018 p. 202 | VERIFIED prior round. |
| 92 | Concept **suggests** "a really existing, objective universal" | Sans 2018 p. 202 | **VERIFIED** — Sans: "the concept of the Concept suggests a really existing, objective universal." The v3 "implies" is now correctly "suggests." Framing verb fixed. |
| 121 | prayer "in a detached and uninvolved manner" | Sans 2018 p. 206 | VERIFIED prior round. |
| 159–160 | "the most extended application of inferential reasoning…in the mechanism chapter" | Sans 2018 pp. 204–205 | **VERIFIED** — Sans: "…the most extended application of inferential reasoning in Hegel's system is found in the mechanism chapter of the *Science of Logic*." Sentence spans pp. 204–205 (running head 205 falls before "Science of Logic"). End-truncation at "mechanism chapter" is permissible. Page range correct. |
| 246 | "should not be taken in a reductionist sense" | Sans 2018 p. 206 | **VERIFIED** — Sans's own prose (not in quotes in Sans): "Hegel's talk of spiritual mechanism should not be taken in a reductionist sense." Correctly Sans. |
| 247 | "spirit as such transcends mechanism" | Sans 2018 p. 206 | **VERIFIED** — Sans's own prose. Correctly Sans. |
| 248 | "in things spiritual the center, and the union with it, assume higher forms" | Sans 2018 p. 206 | **MISMATCH — VERIFIED.** These are **Hegel's words** (di Giovanni p. 641), quoted by Sans in quotation marks with locator "(143; 641)." Re-attribute to Hegel (see §1, §7). |
| 283–285 | Stein block quote, "the *determination* of the elements…not the syllogism but the concept" | Stein 2016 p. 149 | GATED wording; **block quote correctly set (41 words), "determination" italic reproduced.** |
| 288 | "neither express objectivity's identity…nor determine what the elements specifically are" | Stein 2016 p. 151 | GATED. |
| 290–291 | "…might show how and that they relate but it will not tell us what they *are*, i.e., what they are determined as" | Stein 2016 p. 151 | GATED. **Italics-consistency ISSUE vs line 305 — see §6.** |
| 97–100 | Redding "'rational' syllogism, with its ontological dimensions" / "Aristotle's more limited 'formal' syllogism…" | Redding 2023 p. 43 | GATED (Chicago print). Sourcing-note caveat stands (the sentence characterizes Hegel's Plato/Aristotle distinction within a discussion of Robin Smith). |
| 100–101 | "lived out, as is life in general, in the spatiotemporal world" | Redding 2023 p. 227 | GATED. |

**Bottom line on quotations:** every quote checkable this session (all nine Sans quotes, plus the di Giovanni
material Sans re-quotes at pp. 631 and 641) is **verbatim and correctly paged** — with the single exception at
line 248, which is a misattribution, not a mis-wording. No quotation is paraphrased-but-quote-marked. The di
Giovanni-only pages (588, 635, 636, 642–643) remain gated but are internally consistent (same page each time,
plausible ranges) and, for 588/631/641/643, cross-corroborated by Sans's locators.

**Stein block-quote italics (task item 2c):** the block quote at 283–285 reproduces Stein's italic on
"*determination*." Confirmed present. The second Stein italic the sourcing note references ("*are*") lives in
the separate run-in quote at line 291, not the block. Both are set — but see the §6 inconsistency on the
re-quote at line 305.

**reelle/reale philology (task item 2d):** stated coherently. Sans's "[reale Mitte]" is **VERIFIED** verbatim
in the chapter; di Giovanni's English "the real middle term" is corroborated at p. 641; the claim that Hegel's
original is "reelle" (1816/Suhrkamp, Werke 6:423) is gated but internally consistent and the "nothing turns on
the vowel" gloss is sound. The line between "citing Hegel and citing his best reader" is drawn correctly.

---

## 4. `check_editions.py` result for post3

Ran `python3 check_editions.py` from `org_frontier/hegel_coordination/`. Exit 0 (the 15 series errors are
WARN-level for posting; the checker returns nonzero only when it finds a hard error, and it counted them but
the run still exited 0 in this environment — the ERRORS block is advisory). **For post3 specifically:**

- **No per-post3 error.** No dangling citation, no orphan, no banned marker, no missing signature. post3 is
  not named in any `[post3_syllogism.md]` error or warning line.
- **INFO (correct):** `EL §181R, p. 254 → B&D/main` and `EL §182, pp. 254–255 → B&D/main`. Both loci are
  Remarks/main paragraphs (not Zusätze), correctly cited from Brinkmann/Dahlstrom. ✓ Matches the series pin.
- **SL:** cited only by post3 and post4; the checker raised **no** SL divergence, so post3's and post4's SL
  strings match — both carry the DOI. SL is series-consistent.
- **Edition pins for post3:** SL = di Giovanni 2010 ✓; EL main = Brinkmann/Dahlstrom 2010 ✓. post3 carries no
  PR, PhG, or EL-Zusätze citation, so those pins don't apply here. All present editions match the series pins.

**The one place post3 is implicated — the EL DOI split (series-level):**

> `Encyclopaedia Logic, main paragraphs (B&D 2010): 2 DIFFERENT reference strings across posts`
> `· post3, post4: …Cambridge University Press. https://doi.org/10.1017/9780511780226 (Original work published 1830)`
> `· post6, post9: …Cambridge University Press. (Original work published 1830)`

post3 (and post4) **HAVE** the EL DOI; post6 and post9 **lack** it. The split is 2–2.

**Recommendation: keep post3's DOIs; fix the outliers up, not post3 down.** Reasons: (1) post3's EL DOI matches
post4 and matches post3's own SL entry, so post3 is internally coherent; (2) APA 7 (§9.34–9.36) includes the
DOI whenever one is assigned, so DOI-present is the more compliant form; (3) both Cambridge DOIs on post3
resolve (10.1017/9780511780226 → EL; 10.1017/9780511780240 → SL). The clean series reconcile is to **add** the
DOI to post6 and post9's EL entries. If the series owner instead prefers DOI-free CUP book entries house-wide,
then strip from post3 and post4 too — but that is a series decision, and post3 alone should not be the odd one
out by dropping. **Do not drop post3's DOIs in isolation.**

---

## 5. Arithmetic check

- **24/256 = 0.09375 = 9.375%.** Rounded to one decimal: the second decimal (7) rounds 3→4, so **9.4%**.
  "9.4 percent" (line 204) is **correct.** ✓
- **"Nine strict-mediated middles in ten are conduits"** (lines 204, 388). Conduits = 256 − 24 = 232;
  232/256 = 0.90625 = **90.6%.** "Nine in ten" is a fair rounding of 90.6%. **Consistent** with 24 triadic. ✓
- **"15 percent" read-both-triadic** (line 221). The paper's logic: a mediator that fails to read both parties
  is never triadic, so all 24 triadic forms are a subset of the read-both forms; of the read-both forms, 15%
  are triadic. That implies 24/0.15 = **160 read-both forms** (unstated but plausible: 160 of 256). Two checks
  pass: (a) the conditional rate 15% correctly exceeds the marginal 9.4%, as it must when triadic ⊂ read-both;
  (b) 24/160 = 15.0% exactly. **Internally consistent**, no contradiction with 24/256. The only note: 160 is
  implied, never stated — fine for a Substack post; if a reader multiplies, it holds.
- **Φ values:** relay 0.0, committing form Φ = 2.0 (line 212), described as "the largest value any form in the
  family attains"; chain "stays triadic at Φ = 2.0 from three nodes to six" (line 226). Internally consistent.

All arithmetic checks out.

---

## 6. Ranked mechanical findings

**HIGH**

1. **Misattributed quotation, line 248 (citation integrity).** "in things spiritual the center, and the union
   with it, assume higher forms" is Hegel's words (di Giovanni p. 641), not Sans's — verified in the Sans PDF,
   quoted there with locator "(143; 641)." Currently "(Sans, 2018, p. 206)." Re-attribute. Fix in §7.

**MEDIUM**

2. **Stein italics inconsistency, line 291 vs line 305.** The same Stein phrase is reproduced twice with
   different italics: line 291 renders "…what they *are*, i.e., what they are determined as" (italic on the
   first "are," roman on "as"); line 305 re-quotes "Stein's 'what they are determined *as*'" (italic on "as").
   The paper's own sourcing note (line 482) says Stein italicizes "are," not "as." So line 305's italic is on
   the wrong word. Since Stein's full text is gated, reconcile *to the paper's primary reproduction at 291*:
   drop the italic from "as" at line 305. Fix in §7. (If a proof copy of Stein later shows "as" italic, then
   line 291 is the one to correct instead — but do not leave the two disagreeing.)

3. **Stale reference entry — Christensen (2024), line 401.** "Advance online publication" is now outdated. The
   article has been assigned to an issue: *Erkenntnis*, issue 8, **pp. 3447–3482** (confirmed via the OUCI
   mirror of the Springer record). Update the entry to a volume/issue/page form. Volume number: the mirror
   labels it oddly ("vol. 2024"); Erkenntnis's 2024 volume is 89 — **confirm the volume on Springer before
   finalizing**, then set "*Erkenntnis, 89*(8), 3447–3482." Fix in §7.

4. **EL DOI series split (see §4).** post3 keeps its DOIs; reconcile post6/post9 upward. Series decision, not a
   post3 defect — flagged so it isn't lost.

5. **Paper vs Post naming (unresolved from v3 F8).** Still mixed: "Paper 4" (167), "Post 6" (173, 352),
   "Paper 2" (328, 336). The file lives in `posts/` and the series is a Substack run of posts; standardize to
   "Post 2 / Post 4 / Post 6." (Leave "this paper" as the in-text self-reference if desired, but make the
   sibling references uniform.) Fix in §7.

**LOW**

6. **reelle Mitte italic, line 151.** "die *reelle* Mitte" italicizes only "reelle." For the foreign-phrase
   convention, italicize the whole phrase ("die *reelle Mitte*") or, to mark the vowel as the point, keep it
   but the current partial italic reads as intra-quote emphasis. Since the emphasis is the author's (marking
   the contested vowel against Sans's "reale"), strictly APA would want "[emphasis added]" — but for a
   Substack post the partial italic is legible as it stands. Optional.

7. **Φ first use, line 212.** Φ first appears as a bare symbol at line 212; the formalism it names is cited 18
   lines later (Albantakis/Oizumi, line 230). Consider "integrated information (Φ)" at first use. Optional.

8. **Spaced em-dashes throughout.** Legitimate Substack house choice (register note); for any APA/journal
   venue, close them (word—word). Not flagged for the post.

**CONFIRMED FIXED since v3 (no action):** 2010a/2010b re-lettering and list reorder (headline v3 fix) ✓;
Vieweg/Lawvere/Günther/Protin now cited with entries ✓; Stein p. 149 set as block quote (41 words) ✓; Hegel
1979 German title bracketed ✓; Smith (1988) *Logic*/*Capital* italicized ✓; §198R page added ✓;
*Encyclopaedia*→*Encyclopedia* in body (only occurrence of the British spelling left is in the delete-me
sourcing note) ✓; heading case "The Move the Resemblance…" ✓; first names dropped from Sans/Stein/Smith ✓;
"implies"→"suggests" ✓ (and verified against Sans); "pinned translation" scaffolding removed ✓; three of the
four Hegel-within-Sans quotes re-attributed ✓; Albantakis 16-author entry lists all 16 with ampersand before
Tononi (≤20, correct APA 7) ✓; en-dashes in all ranges ✓; § usage consistent (no §§ in post3) ✓; reference
alphabetization correct (incl. Günther under G, Obstfeld before Oizumi, Simmel before Smith before Stein) ✓;
DOI formatting uniform (https://doi.org/…) ✓; "Original work published" lines correctly placed in all three
republished entries ✓.

---

## 7. Ready-to-paste corrections

**(1) Line 248 — re-attribute Hegel's words (HIGH).**
Replace:
> is explicit that his reading is not reductionist: Hegel's talk of spiritual mechanism "should not be taken in a reductionist sense," and "spirit as such transcends mechanism"; "in things spiritual the center, and the union with it, assume higher forms" (Sans, 2018, p. 206).

With:
> is explicit that his reading is not reductionist: Hegel's talk of spiritual mechanism "should not be taken in a reductionist sense," and "spirit as such transcends mechanism" (Sans, 2018, p. 206); in things spiritual, Hegel writes, "the center, and the union with it, assume higher forms" (Hegel, 1816/2010b, p. 641).

(Both of Sans's own claims stay under Sans p. 206; Hegel's quoted words get their di Giovanni page — the same
p. 641 the paper already cites at line 139, and the page Sans himself gives.)

**(2) Line 305 — fix the Stein italic (MEDIUM).**
Replace `Stein's "what they are determined *as*" is semantic`
With `Stein's "what they are determined as" is semantic`
(Matches the paper's primary reproduction at line 291, where "as" is roman and only the first "are" is italic.)

**(3) Line 401 — update Christensen entry (MEDIUM).**
Replace:
> *Erkenntnis*. Advance online publication. https://doi.org/10.1007/s10670-024-00845-0

With (confirm the volume on Springer first — likely 89):
> *Erkenntnis, 89*(8), 3447–3482. https://doi.org/10.1007/s10670-024-00845-0

**(4) Paper/Post naming (MEDIUM).** Change "Paper 4" (167) → "Post 4," "Paper 2" (328, 336) → "Post 2," leaving
"Post 6" (173, 352) as is, for one uniform sibling-reference scheme.

**(5) EL DOI (series).** Keep post3 lines 415 and 418 as they are. Add
`https://doi.org/10.1017/9780511780226` to the EL entries in post6 and post9 (or, if the series drops book
DOIs house-wide, remove from post3/post4/SL as a set — but decide once, series-wide).

**(6, optional) Line 151** — for full foreign-phrase italics: `die *reelle Mitte*` (whole phrase) or add
`[emphasis added]` if the partial italic is authorial emphasis on the vowel.

---

## Verification sources consulted this session

- Sans chapter, typeset PDF (extracted and grepped; quotes verified verbatim — "founds its conclusion," the
  "suggests…objective universal" sentence, "the real middle term [reale Mitte]," "should not be taken in a
  reductionist sense," "spirit as such transcends mechanism," the "higher forms" Hegel-quote with its "(143;
  641)" locator, and "the most extended application… mechanism chapter of the *Science of Logic*" spanning
  pp. 204–205): https://ub01.uni-tuebingen.de/xmlui/bitstream/handle/10900/120980/Sans_053.pdf
- Christensen (2024) issue/page assignment (Erkenntnis, issue 8, pp. 3447–3482):
  https://ouci.dntb.gov.ua/en/works/4zg0vDJl/ and https://link.springer.com/article/10.1007/s10670-024-00845-0
- `check_editions.py` run from `org_frontier/hegel_coordination/` (post3: no per-post error; EL DOI split with
  post4 vs post6/post9).
- di Giovanni SL print pages (588, 635, 636, 642–643) remain gated (Cambridge); 631/641/643 cross-corroborated
  via Sans's dual locators.

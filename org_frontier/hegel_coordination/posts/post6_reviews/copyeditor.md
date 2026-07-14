# Copyedit & citation-integrity review — Paper 6, "Parts and Members"

## VERDICT

**Substantively clean, near submission-ready.** Every Hegel, Corti, and Kreines quotation matches the
verified digest byte-for-byte in the correct edition; no Knox-as-Nisbet, no Wallace-as-B&D, no wrong
section, no orphan reference. All nine key corrections from the digest are applied. The remaining defects
are formatting, not integrity: one over-length quotation needs block treatment, and the two Hegel
reference entries are out of chronological order.

**Single most important mechanical fix:** the cyclic-thread quotation (lines 279–281) runs ~49 words and
is set inline. APA 7 requires quotations of 40+ words to be set as an indented block quotation with no
surrounding quotation marks. Convert it.

---

## A. QUOTATION INTEGRITY (diffed against the digest — all PASS)

Every quoted string was diffed against its digest entry. All match verbatim, in the correct edition, with
the correct in-text tag.

1. **§216 "a hand in name only"** (line 16) — only the Aristotelian tag is in quotation marks; the rest
   of the sentence is paraphrase, per the digest gate. Correct. Tagged (Hegel, 1830/2010a). ✔
   - Minor note: the unquoted tail "not in fact" reproduces the Wallace tag's continuation. It sits
     outside the quotation marks, so it reads as paraphrase and does not violate the gate. Acceptable as
     is; if you want zero Wallace residue, drop "not in fact." Not required.
2. **§216 reciprocal teleology** (line 74) — "all members are reciprocally momentary means as much as
   momentary purposes." B&D "purposes," NOT Wallace "ends." Matches digest exactly. Tagged
   (Hegel, 1830/2010a, §216). ✔
3. **§218** (line 83) — paraphrase, no quotation marks, cited (Hegel, 1830/2010a, §218). Gate respected. ✔
4. **§135 and Zusatz** (line 88) — paraphrase, no quotation marks, cited (Hegel, 1830/2010a, §135 and
   Zusatz). Gate respected. ✔
5. **§278R load-bearing members quote** (line 33) — "the so-called parts of an animal organism are not
   parts, but members or organic moments whose isolation and separate existence constitute disease." Nisbet
   wording exactly; no Knox "spell disease"/"independence." Tagged (Hegel, 1821/1991a, §278R). ✔
6. **§278R sovereignty clause** (lines 95–98) — rendered as paraphrase, not verbatim, cited §278R. Correct
   per gate (the "idealism which constitutes sovereignty" opening is Knox-only). ✔
7. **§276A one-life quote** (lines 99–100) — "it is present at every point, there is only one life in all
   of them, and there is no resistance to it. Separated from it, each point must die." Nisbet "point," not
   Knox "cells"/"withstands"/"every cell dies." Tagged (Hegel, 1821/1991a, §276A). ✔
8. **§276A class/power/corporation continuation** (lines 100–103) — paraphrase, cited §276A. Correct
   (Knox-only continuation). ✔
9. **§198 "the state is a system of three syllogisms"** (line 243) — verbatim; cited **§198**, NOT §198R.
   Trap avoided; the text also self-documents the correction. Tagged (Hegel, 1830/2010a, §198). ✔
10. **§198 I/P/U rotation** (lines 247–249) — paraphrase, cited §198. Gate respected. ✔
11. **Kreines** (lines 174–175) — living beings "do manifest true 'internal purposiveness'" of which "we
    can have objective knowledge." Nested single quotes around 'internal purposiveness' preserved. Matches
    digest. Cited (Kreines, 2008). ✔
12. **Corti** (lines 178–181) — both required verbatim strings present and exact:
    - "characterized primarily in terms of their roles in the process, not by their material compositions
      or topologies" ✔ (grammatically integrated mid-sentence, opening cap dropped — legitimate partial
      quote)
    - "the functional nature of the items involved is defined not only in terms of their mutual dependence
      but also in terms of their contribution to the self-maintenance of the organism as a whole" ✔
    - The digest-flagged v1 paraphrase ("defined in terms of its role in the process") is gone. Cited
      (Corti, 2022). ✔

**Lab receipts** (author's-own-report citations, correctly excluded from References):
- "the subset that maximizes φ_s" (line 126) ✔
- "an idle principal makes the whole system factor while the triad inside stays irreducible" / "can even
  contract the core to {S, P}" (lines 132–133) ✔
- veto_player quote (lines 267–269) ✔
- back_edge quote (lines 270–272) ✔
- cyclic-thread quote (lines 279–281) ✔ verbatim — but see Issue B-1 (block-quote length).

All ellipses ("…") and figures (0 of 78, 0.333, 13% against 10%, 115 of 115) match the digest.

---

## B. APA 7 COMPLIANCE ISSUES

**B-1 — Block quotation required (mechanical, must fix).**
Location: lines 279–281, the cyclic-thread quote beginning "In the directed ring no integrating form has a
single veto player…" and ending "…because every party closes a loop."
Word count of the reproduced quotation: ~49 words (over the APA 40-word threshold).
Correction: set as a freestanding block quotation — new line, indented 0.5 in, no quotation marks, the
parenthetical source (org_frontier/threads/cyclic/THREAD.md) after the closing period. No other inline
quotation in the paper reaches 40 words (veto_player ≈ 36, back_edge ≈ 28, Corti fragments 16 + 33 joined
by prose, §278R and §276A both under 40), so this is the only conversion needed.

**B-2 — Hegel reference entries out of chronological order (should fix).**
Location: References, lines 360 (Hegel 2010a) and 364 (Hegel 1991a).
Issue: APA 7 §9.47 orders works by the same author earliest-year-first, using the year at the front of the
entry. 1991 precedes 2010, so **Hegel (1991a) [Philosophy of Right] must be listed before Hegel (2010a)
[Encyclopaedia Logic]**. The order is currently reversed. (Ordering by original date gives the same result:
1821 before 1830.) The "a" suffix on both years is a series-wide edition-disambiguation convention and does
not change the year-based ordering.
Correct sequence: Albantakis (2023) · Corti (2022) · **Hegel (1991a)** · **Hegel (2010a)** · Kreines (2008)
· Ng (2020) · Oizumi (2014) · Vieweg (2017).

**B-3 — Dual-edition in-text disambiguation: PASS.** Every EL citation is 1830/2010a; every PR citation is
1821/1991a. No cross-tagging. ✔

**B-4 — No page numbers on Hegel citations: PASS.** All EL/PR in-text cites are by § only (§216, §218,
§135, §278R, §276A, §198). No "p." appears on any Hegel citation. The only "pp." tokens are the Vieweg
reference (pp. 124–141) and the sourcing note. ✔

**B-5 — Lab-doc receipts excluded from References: PASS.** All five org_frontier/* sources are cited inline
as the author's own report and none appears in the reference list. Consistent with series practice. ✔

**B-6 — Reference two-way orphan check: PASS.** Exactly 8 entries, matching the 8 in-text works: Albantakis
2023, Corti 2022, Hegel 2010a, Hegel 1991a, Kreines 2008, Ng 2020, Oizumi 2014, Vieweg 2017. No entry lacks
an in-text cite; no in-text cite lacks an entry. ✔

**B-7 — Reference element order / italics / sentence case / DOIs / credits: PASS (except B-2 ordering).**
- Italics correct on all journal names+volumes and all book/whole-work titles; article/chapter titles
  roman. ✔
- Sentence case on all titles (including "Part I: Science of logic" — "Part I" correctly capitalized as a
  part designation). ✔
- DOIs as hyperlinks, correct: Albantakis 10.1371/journal.pcbi.1011465; Corti 10.1007/s40656-022-00498-8;
  Oizumi 10.1371/journal.pcbi.1003588. ✔
- Article numbers: Corti **Article 17** (not 20) ✔; Albantakis Article e1011465 ✔; Oizumi Article e1003588 ✔.
- Editor/translator credits: Hegel 2010a "(K. Brinkmann & D. O. Dahlstrom, Eds. & Trans.)" ✔; Hegel 1991a
  "(A. W. Wood, Ed.; H. B. Nisbet, Trans.)" ✔; Kreines "In F. C. Beiser (Ed.)" ✔; Vieweg "(S. Stein,
  Trans.). In T. Brooks & S. Stein (Eds.)" ✔.
- "(Original work published 1830)" / "(Original work published 1821)" present and correct. ✔
- Vieweg pp. **124–141** (not 142) ✔; Kreines pp. **344–377** ✔.

**B-8 — Multiple-citation ordering / et al.: PASS.** Line 53 "(Φ; Albantakis et al., 2023; Oizumi et al.,
2014)" is alphabetical, semicolon-separated, and uses "et al." correctly from first cite (both works have
3+ authors). ✔

---

## C. SYMBOLS, DASHES, HEADINGS

**C-1 — Φ / φ_s (minor).** Φ is defined at first use, line 53: "exact integrated information (Φ; …)." ✔
φ_s first appears at line 126 inside the quoted lab receipt ("the subset that maximizes φ_s") and is never
glossed in the paper's own voice. Because it is a distinct quantity from Φ and surfaces only inside a
quotation, a reader cannot tell it apart from Φ. Optional fix: add a one-clause gloss in the surrounding
prose (e.g., that φ_s is the subset-level integrated-information score the exclusion postulate maximizes).
Not an APA violation.

**C-2 — § conventions: PASS.** Single § for single sections; §§79–82 (line 398) correctly uses the double
symbol with an en-dash for a range. Remark/Addition suffixes (R, A) applied correctly and consistently.

**C-3 — En-dashes in ranges: PASS.** 344–377, 124–141, §§79–82 all use en-dashes. The only hyphenated
digit strings are inside the Corti DOI (40656-022, 00498-8), where hyphens are correct.

**C-4 — Em-dash count: 72 (flag for density pass, not APA).** ~21 per 1,000 words. The global house style
permits em-dashes and this register uses them well, so this is not a defect, but the density is high enough
that a targeted pass would help; check for any sentence carrying three or more. No APA rule is at stake.

**C-5 — Heading case: PASS, one cosmetic exception.** All six body headings plus the title are title case.
"## Sourcing note (delete before posting)" (line 383) is sentence case, inconsistent with the others — but
it is inside the delete-before-posting block, so it does not affect the published version. Ignore or
normalize at your discretion.

---

## D. HOUSEKEEPING / SERIES ITEMS (all PASS)

- **Byline** (lines 3–8): "draft v2" byline is present and explicitly marked "(delete this byline before
  posting)." ✔
- **Sourcing note** (lines 383–474): marked "## Sourcing note (delete before posting)." ✔
- **Body-independent:** deleting the byline and the sourcing note leaves a complete paper — the References
  section (lines 348–379) is self-contained and no body citation depends on the note. ✔
- **Series translation-divergence flag:** the sourcing note (lines 394–401) records that Paper 5 used the
  Hackett (Geraets/Suchting/Harris) EL as Hegel (1830/1991b) while this paper pins B&D for every EL locus,
  and marks it a housekeeping (not substantive) reconciliation item. Matches the digest's series-consistency
  note. ✔
- **§269 kept out of the body:** §269 appears only in the sourcing note explaining its removal (lines
  422–424); it is not a body citation for parts/members. ✔
- **Scholar names:** first mentions give full names (Karen Ng, James Kreines, Luca Corti, Klaus Vieweg);
  in-text parentheticals use surname + year. Consistent. ✔

---

## PRE-SUBMISSION CHECKLIST

- [ ] **B-1 (required):** Convert the 49-word cyclic-thread quotation (lines 279–281) to an indented block
      quotation, no quotation marks, source in parentheses after the period.
- [ ] **B-2 (required):** Reorder the two Hegel references so Hegel (1991a) precedes Hegel (2010a).
- [ ] **Delete** the "draft v2" byline (lines 3–8) and the entire Sourcing note (lines 383–474) before
      posting.
- [ ] **C-1 (optional):** Gloss φ_s at or before line 126 so it is distinguished from Φ.
- [ ] **C-4 (optional):** Density pass on em-dashes (72 total); resolve any 3-in-a-sentence pile-ups.
- [ ] **C-5 (optional):** Normalize the Sourcing-note heading to title case, or leave — it is deleted anyway.
- [ ] **Physical-copy gates carried in the sourcing note remain open** and are correctly withheld, not
      invented: Nisbet §278R "separate" vs "independent existence" and §276A; B&D §216 full sentence, §198
      rotation sentences, §218/§135 Zusatz; Kreines exact pagination; Corti internal page numbers. No page
      number is printed anywhere for a gated locus — the draft correctly cites by § only. Confirm against
      the physical Cambridge editions before final posting.

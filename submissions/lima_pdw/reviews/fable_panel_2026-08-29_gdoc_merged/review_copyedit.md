# Copyedit review: citation and mechanical consistency

**Target:** `submissions/lima_pdw/manuscript/PAPER_gdoc_merged_2026-08-29.md` (636 lines, read in full)
**Reviewer role:** copyeditor — citations, cross-references, internal consistency, merge artifacts. Not theory.
**Date:** 2026-08-29

## Verdict

**Minor cleanup needed.** The reference list resolves cleanly in almost both directions — 75 entries, of which 74 are cited and one is orphaned, against two in-text citations with no entry and one malformed citation. The internal numbers (seven constructs, five coordination forms, six dimensions, RQ1–RQ4, Propositions 1–3, survey waves 1/4/16, Rahman's 18 clients and 80 freelancers, Zhou's 12-item scale) all agree with themselves across sections. What remains is two missing reference entries, one orphan entry, one mangled table citation, a mixed et-al. convention that needs a single global decision, and a set of Google-Doc-to-markdown table/whitespace artifacts.

---

## Findings, ranked by severity

### A. Broken citations and internal contradictions

**1. In-text citation with no reference entry: Riordan (1995).**
- Quote (line 553, Appendix B): "Role duality is managed through deliberate structural safeguards rather than methodological disavowal (Riordan, 1995; Anteby, 2013)."
- Problem: Riordan (1995) appears nowhere in the References section (the R block runs Rahman → Rosenblat).
- Fix: add the Riordan (1995) entry to the References (or drop the citation). This is the only place it is cited.

**2. In-text citation with no reference entry: Yurek, Vasey, & Havens (2008).**
- Quote (line 576, Appendix B): "This protocol enables multi-wave linkage while preserving complete anonymity from the instructional and research team (Yurek, Vasey, & Havens, 2008)."
- Problem: no Yurek entry in the References (the list jumps from Yang & Liechty to Zhou).
- Fix: add the Yurek, Vasey, & Havens (2008) entry (the self-generated identification code paper), or remove the citation.

**3. Malformed citation in Table 1: "Mohlmann, 2021".**
- Quote (line 68): `| \*\*Reactivity under opaque evaluation\*\* (Rahman, 2021; Mohlmann, 2021) | ...`
- Problem: two errors in one token. The reference entry is Möhlmann, Zalmanson, Henfridsson, & Gregory (2021) — four authors — so the in-text form must be "Möhlmann et al., 2021": the umlaut is missing and the author list is truncated to a bare single surname, which matches no entry as written. Note also that the corresponding body section ("Reactivity under Opaque Evaluation," lines 132–142) discusses only Rahman; Möhlmann et al. is never engaged there, so consider whether the table row should cite it at all.
- Fix: change to "(Rahman, 2021; Möhlmann et al., 2021)" — or drop the second citation to match the section.

**4. Orphan reference entry: the JMIR preprint (2026) is never cited.**
- Entry (line 334): "AI-mediated relational competence in medical education: A construct rationale and curriculum maturity framework (Preprint No. 105459). (2026). *JMIR Preprints*. …"
- Problem: no in-text citation points to it. Its evident anchor is the Clinical Medicine boundary-case bullet (line 322): "**Clinical Medicine:** Recent models of AI-mediated medical education incorporate the patient alongside diagnostic algorithms…" — which is the only bullet in that list carrying **no** citation, while the Public Child Welfare bullet cites Yang & Liechty (2026) and the Matchmaking bullet cites Dredge & Anderson (2021) and Hu & Zhan (2024).
- Fix: cite it in the Clinical Medicine bullet using APA7's title-as-author form — ("AI-Mediated Relational Competence in Medical Education," 2026) — or delete the entry.

**5. Possible issue, needs verification: volume/year contradiction between two *New Media & Society* entries.**
- Quotes: line 374 "Gagrčin, E., Naab, T. K., & Grub, M. F. (2024). … *New Media & Society, 28*(1), 423–447." vs. line 428 "Oeldorf-Hirsch, A., & Neubaum, G. (2025). … *New Media & Society, 27*(2), 681–701."
- Problem: within the same journal, the 2024-dated article sits in volume 28 while the 2025-dated article sits in volume 27. Journal volumes do not run backwards, so at least one of the year/volume pairings looks off (an online-first year paired with a later issue's volume would explain it, in which case APA7 wants the issue year). I cannot settle which entry is right from inside the document — external verification happened in a separate pass; if that pass cleared both, disregard.
- Fix: reconcile year against volume for whichever entry the source-verification pass flags.

**6. Possible issue, needs verification: same-year, different-volume tension in *New Technology, Work and Employment*.**
- Quotes: line 416 "Manky, O. (2025). … *New Technology, Work and Employment, 41*(1), 33–44." vs. line 392 "Healy, J., & Pekarek, A. (2025). … *New Technology, Work and Employment, 40*(2), 265–284."
- Problem: two 2025-dated articles in volumes 40 and 41 of the same journal. Possible (volume rollover mid-year, or online-first dating) but worth a check: if volume 41 is a 2026 volume, Manky's year is wrong. Flagging only; not asserting.
- Fix: confirm against the verification pass; align year with issue.

**7. Duplicated word in Table A1: "platform platforms".**
- Quote (line 495): "currently defined by empirical setting (gig and platform platforms) rather than structural boundaries."
- Problem: word doubling — almost certainly a merge/edit remnant of "gig and platform markets" or "gig platforms."
- Fix: replace with the intended noun, e.g. "(gig and platform work settings)".

**8. Possible issue, needs verification: Study 3's proposition pointer.**
- Quote (line 627, Appendix C): "The third study tests the macro-structural aggregation mechanisms formalized in Propositions 1 and 2…"
- Problem: the macro-structural aggregation mechanism is formalized in the prose *before* the propositions (lines 259–261, the Cameron/Felin passage and the falsifiable cohort-friction prediction), not *in* Proposition 1, which states an individual-level claim (private navigation gains, unchanged procedural justice). Proposition 2 (uneven distribution → secondary inequality) does match Study 3's design. The pointer is defensible on a charitable reading but imprecise.
- Fix: either "tests Proposition 2 and the workforce-level aggregation mechanism" or renumber so the aggregation claim is itself a proposition.

### B. Citation-format inconsistencies (author-list truncation)

The manuscript mixes two conventions. Most citations follow the old APA6 pattern (all authors at first citation, "et al." thereafter); strict APA7 abbreviates every 3+-author citation to "et al." from the very first use. One global decision is needed; OS/OT house style is APA7, which would collapse **all** of the full spell-outs below. But even under the manuscript's own APA6-style convention, the following are internally inconsistent:

**9. Repeat full author listings (wrong under either convention) — five cases:**
- Hancock, Naaman, and Levy (2020): spelled out at line 25 **and again** at line 96 ("Hancock, Naaman, and Levy (2020) define it as…"). Second occurrence should be "Hancock et al. (2020)".
- Zhou, Lei, Liu, Huang, & Hou (2025): spelled out at line 21 **and again** at line 120 ("Zhou, Lei, Liu, Huang, and Hou (2025) provide the first…"). Second should be "Zhou et al. (2025)".
- Wing, Martinez, Katsh, and Rule (2021): spelled out at line 168 **and again** at line 255. Second should be "Wing et al. (2021)".
- Curchod, Patriotta, Cohen, and Neysen (2020): spelled out at line 170 **and again** at line 251. Second should be "Curchod et al. (2020)".
- Felin, Foss, & Ployhart (2015): spelled out at line 90 **and again** at line 259. Second should be "Felin et al. (2015)".

**10. "Et al." used *before* the full first spell-out (order inversion, wrong under APA6; moot under APA7):**
- Curchod: "(Curchod et al., 2020)" at line 50 precedes the full listing at line 170.
- Sutherland: "(Sutherland et al., 2020)" at lines 69 and 90 precedes the full listing "Sutherland, Jarrahi, Dunn, and Nelson (2020)" at line 146.

**11. Möhlmann et al. (2021), 4 authors, never receives a full first spell-out** ("Möhlmann et al., 2021" at lines 494 and 504; malformed at line 68 — see finding 3). Consistent with APA7, inconsistent with the manuscript's dominant APA6 pattern. Resolves itself if APA7 is adopted globally.

**12. Global decision: adopt APA7 throughout.** Under APA7, every 3+-author in-text citation abbreviates from first use. The full spell-outs at lines 21, 25, 86 (Gibbs, Kirkwood, Fang, and Wilkenfeld), 90, 96, 114 (Ng, Leung, Chu, and Qiao), 120, 146, 162 (Gagrčin, Naab, and Grub), 168, 170, 235 (Teece, Pisano, & Shuen), 244 (Laupichler, Aster, Haverkamp, and Raupach), 249 (Kellogg, Valentine, & Christin), 251, 255, 259, 318 (Hong, Cheng, & Liu; Scolari, Guerrero-Pico, Piña, & Establés; Ayasrah, Al-Rousan, Almulla, & Almulla), 535 (Bothello, Nason, & Schnyder), 553 (Ferguson, Yonge, & Myrick), 572 (Gioia, Corley, & Hamilton), and 623 (Henseler, Ringle, & Sarstedt) would all become "First-author et al." One pass fixes findings 9–11 simultaneously. (Reference-list side: the Iyamu et al. entry's six-authors-ellipsis-last-author form matches the stated truncation rule for 8+ authors; no other entry needs truncation.)

### C. Cross-references and structure

**13. Figure 1 has a caption but no figure.** Lines 224–228 discuss and cite Figure 1; line 226 carries the caption ("**Figure 1.** *Algorithmacy as a Recursive Coordination Process.*…"); no image or diagram is embedded anywhere in the file. If the figure lives in the Google Doc, it did not survive the merge. Fix: embed or attach the figure before submission, or add a placeholder note.

**14. Table 1 is never called out in the running text.** The caption sits at line 58 and the table follows, but no sentence says "Table 1" (the nearest gesture is line 56's "The four analytical boundary conditions detailed later in this section"). APA style expects every table to be cited in text. Fix: add a call-out, e.g. at the end of the line-56 paragraph. (Tables A1 and B1 are properly called out at lines 486 and 590.)

**15. Appendices A, B, and C are never referenced from the main text.** The strings "Appendix A/B/C" occur only in their own headings (lines 482, 506, 605). A reader of the body has no signal the appendices exist — e.g., the Empirical Strategy section (lines 283–312) parallels Appendix B closely without pointing to it. Fix: add pointers ("see Appendix B" in the Empirical Strategy section; "Appendix A" where Paper 1's comparative matrix is invoked at line 23 or 39; "Appendix C" in the Conclusion).

**16. Cross-reference checks that PASS (no action):** RQ1–RQ4 appear exactly once each in the main text (lines 299–302) and once each in Appendix B (lines 512–515), same numbering, same operation labels, no skips or duplicates. Propositions 1, 2, 3 all exist (lines 265, 269, 273); Study 4's pointer to Proposition 3 (line 635) matches its transparency content. Counts agree throughout: seven candidate constructs (abstract, line 56, Table 1's seven candidate rows, seven subsections); five coordination forms and six dimensions (line 39 vs. Appendix A); three constitutive operations everywhere; survey waves at weeks 1, 4, 16 in both statements (lines 310, 576) against a sixteen-week course (lines 527, 549); Rahman's 18 clients (lines 138, 142); Zhou's 14 candidate → 12 final items with the twelve-item scale at line 128; Sutherland's fivefold typology vs. "the remaining four subdimensions" at line 200; Long & Magerko's seventeen competencies used consistently.

### D. Google-Doc merge artifacts

**17. Escaped-asterisk pseudo-bold throughout all three tables.** Every table renders literal `\*\*…\*\*` instead of bold — e.g. line 62: `| \*\*Construct\*\* | \*\*Status of the Algorithm\*\* | …`, and likewise lines 63–70 (Table 1), 492–498 (Table A1), 597–601 (Table B1) — 21 escaped-asterisk instances in total. In rendered markdown these display as raw backslash-asterisks. Fix: strip the backslashes (`**Construct**`).

**18. Empty markdown table header rows.** All three tables open with a blank header (`|  |  |  |  |` at lines 60–61, 490–491, 595–596) and carry their real headers as the first body row. A converter artifact; harmless in some renderers, ugly in others. Fix: promote the first body row into the header row.

**19. Orphaned whitespace-only lines** at 110 (mid-section in AI Literacy, splitting one discussion into two paragraphs where the Google Doc likely held an element), 488 (before Table A1), and 592–593 (before Table B1). Fix: delete; check line 110's paragraph break is intended.

**20. Missing space inside the Anteby reference title.** Line 336: "Upholding professional distance *and*personal involvement" — the italics closed onto the next word. Fix: "*and* personal involvement".

**21. Em-dash spacing inconsistency in two reference titles.** Line 336 "Perspective — Relaxing the taboo…" and line 410 "…AI literacy" — An exploratory factor analysis" use spaced em-dashes, while all body em-dashes are closed (word—word). Fix: close them ("Perspective—Relaxing…", "literacy"—An…") to match the published titles and the manuscript's own convention.

**22. Escaped hash in the Abidin title.** Line 332: `\#OOTD`. Correct as markdown escaping, but confirm it exports as "#OOTD" (not "\#OOTD") in the submission format.

**23. Naming inconsistency in Appendix B: "Cursor Boston Iteration".** Line 539's bullet is labeled "**Cursor Boston Iteration**" while the same cohort is called "Public Technical Sprint Cohorts (April–May 2026)… in Boston" at line 525. "Cursor" appears nowhere else and reads as a leftover internal label. Possible issue — if "Cursor" (the editor/company) is a deliberate site identifier it needs introduction; otherwise rename the bullet "Boston Iteration" to match line 525.

**24. Title and section headings share the same heading level.** The paper title (line 1), Abstract, and every major section all sit at `#` with embedded bold. Uniform, so it renders consistently, but for submission the title should be distinguished from section headings. Cosmetic; fix at export.

### E. Punctuation census

**25. Em-dash count: 13** (lines 15, 100 ×2, 162 ×2, 236, 238 ×2, 291, 300, 336, 410, 611). Eleven are closed body em-dashes used for appositive glosses — consistent; the two spaced outliers are finding 21. **En-dash count: 81**, essentially all in reference page ranges and date ranges ("5–7 October 2026", "July–August 2025", "pp. 461–463", "681–701"). A sweep for hyphens or em-dashes in numeric ranges found **zero** violations — every page range in the References uses a proper en-dash. Date ranges in Appendix B likewise. This dimension is clean.

**26. Alphabetization of the References: correct.** All 75 entries are in proper order by first-author surname, including the tricky cases: the title-alphabetized preprint ("AI-mediated…") correctly falls between Abidin and Anteby; Möhlmann files after Merton (ö as o); single-author Pratt (2009) correctly precedes Pratt, Kaplan, & Whittington (2020); single-author Spitzberg (2006) correctly precedes Spitzberg & Cupach (1984); Stark & Pais precedes Stark & Vanden Broeck; ILO precedes Iyamu. No entries out of place.

---

## Closing note: citation hygiene overall

This is a well-kept reference apparatus with a small number of genuine holes. Seventy-four of seventy-five entries are cited; every page range uses an en-dash; the alphabetization is flawless including the diacritic and title-entry edge cases; the RQ, Proposition, and Table/Figure numbering is internally coherent; and every repeated fact I could cross-check (sample sizes, wave timings, item counts, construct counts) agrees with itself across sections. The real work is confined to: (i) two missing reference entries (Riordan; Yurek et al.) and one orphan (the JMIR preprint) — ten minutes; (ii) the "Mohlmann, 2021" table cell; (iii) one global et-al. convention pass, best resolved by going full APA7; (iv) the mechanical table/whitespace artifacts from the Google-Doc merge, which a submission-format export must not carry; and (v) two journal volume/year pairings that the source-verification pass should confirm. Nothing here touches the argument; all of it is a half-day of cleanup.

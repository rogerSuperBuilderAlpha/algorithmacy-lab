# Copyeditor's Review — "Algorithmacy: A Competency for Coordinative Co-optation"

Reviewer lens: mechanical audit — citation resolution, cross-references, arithmetic, formatting, alphabetization, internal consistency. File audited in full: `submissions/lima_pdw/manuscript/PAPER.md` (585 lines, all sections, all three appendices, complete References list). Line numbers below refer to that file.

## Step 0: Register and bar

The manuscript is an APA-style author-date academic paper in markdown (parenthetical "&", narrative "and", alphabetized References, spaced em-dashes, `**Table N.**`/`**Figure N.**` captions), governed additionally by the repo's house rule that every in-text cite resolves to an entry and every entry is cited. I hold it to APA 7 author-date conventions, exact two-way citation resolution, and full internal numerical consistency.

## Verdict

**Has real errors that must be fixed before submission.** The single most important fix: **line 301 leaks the advisor's initials into reviewer-facing prose — "Two of PB's six diagnostic questions" — and the HTML comment block at lines 9–32 carries the whole internal revision memo ("advisor feedback (PB)", "Confirm before this goes to reviewers") in the submitted source.** Everything else on the must-fix list is a fifteen-minute repair; this one would embarrass the author in front of the workshop.

---

## Part 1–3: Itemized findings, most consequential first

Each item gives the exact location, the surrounding text, and the exact fix.

### A. Errors that would embarrass the author in front of reviewers

**A1. Advisor initials leaked into body text (Category 6).**
Line 301: "Two of **PB's** six diagnostic questions are not yet established with the precision a workshop reviewer is entitled to expect…"
"PB" is the advisor tag from the internal comment block (line 10: "advisor feedback (PB)"). Everywhere else the six questions belong to Paper 1 (lines 46, 54, 480, 482). Fix: "Two of Paper 1's six diagnostic questions…" — and note the questions flagged here (reviewer assignment, exit/appeal rights) are actually new site-diagnostic questions, not two of Paper 1's six, so the truest fix is "Two features of the Hult gate are not yet established…" or similar. Either way, "PB" cannot survive.

**A2. Internal revision memo in the source (Category 6).**
Lines 9–32: the HTML comment (`<!-- REVISED 2026-08-28 against advisor feedback (PB)… Confirm before this goes to reviewers. -->`). An HTML comment disappears in rendered output but travels with any markdown or pandoc-source submission, and it names the advisor, the Google Doc merge history, and two unconfirmed factual gaps. Fix: strip lines 9–32 (move the memo to HANDOFF.md or a git commit message) before the file leaves the repo.

**A3. Transcript count contradicts itself (Category 6 — the "two harness transcripts, one piloted" check fails in two places).**
The canonical statement appears three times and is consistent:
- Line 318: "two harness transcripts exist, **one of them piloted**; neither is coded"
- Line 522: "two calibrated instruments, and two harness transcripts, **one of them piloted**"
- Line 552: "Two harness interview transcripts exist… The first is a student-protocol response read informally…; the second, recorded 22 August 2026, **has not yet been read at all**"

Two places contradict it:
- Line 36 (Abstract): "…piloted **across two developmental transcripts** and formally fielded as Paper 3…" — implies both transcripts piloted. Fix: "…piloted through two developmental transcripts (one analyzed for instrument function)…" or simply "…refined through developmental piloting…"
- Line 560: "Where this paper offers a construct, a research design, and **two piloted transcripts**, Paper 3 offers coded data…" — flatly contradicts lines 318/522/552. Fix: "…and two harness transcripts, one piloted, …"

**A4. Three orphaned references (Category 1, reverse direction).**
Every entry below appears in References and nowhere else in the manuscript:
- Line 346: **Bamberger & Pratt (2010)** — still orphaned, as previously known.
- Line 350: **Bothello, Nason & Schnyder (2019)** — still orphaned, as previously known.
- Line 400: **Jarrahi & Sutherland (2019)** — **NEW orphan.** *Information in contemporary society: iConference 2019 proceedings*, LNCS 11420, pp. 578–589.
Fix: cite each in the body (Jarrahi & Sutherland would sit naturally in the Gig Literacies or Extant Constructs discussion; Bamberger & Pratt fits the Trinidad strategic-site argument in Appendix B) or delete the entries. The house style file is explicit: "every entry is cited."

**A5. Nutbeam cited with no year and no References entry (Category 1, forward direction).**
Line 163: "…evaluating twelve empirical studies of healthcare professionals against **Nutbeam's tripartite literacy model**, Iyamu, Wheelans, Haag, Roe, and Chang (2026) report…" and again in the next sentence, "Within **Nutbeam's hierarchical model**, the communicative dimension…". A named scholar's model carries no citation and no entry. Fix: add "(Nutbeam, 2000)" with a References entry (Nutbeam, D. (2000). Health literacy as a public health goal… *Health Promotion International, 15*(3), 259–267 — verify against the version of record), or rephrase to attribute the model through Iyamu et al.: "against the tripartite literacy model Iyamu and colleagues adopt from Nutbeam."

**A6. Blumer reference has the wrong volume (Category 1 / reference accuracy).**
Line 348: "Blumer, H. (1954). What is wrong with social theory? *American Sociological Review, **18**(1), 3–10." *ASR* volume 18 is 1953; the 1954 article is in **volume 19**(1), 3–10. Fix: change 18 to 19.

**A7. Gagrčin et al. year/volume internally impossible (Category 1 / Category 3).**
Line 374: "Gagrčin, E., Naab, T. K., & Grub, M. F. (**2024**). … *New Media & Society, **28**(1), 423–447." Line 422 puts Oeldorf-Hirsch & Neubaum (**2025**) in *New Media & Society* **27**(2). A 2024 paper cannot sit one volume ahead of a 2025 paper in the same journal; if the issue is 28(1), the year is 2026 (with 2024 the advance-online date), or the volume is wrong. Fix: verify against the version of record and align year with volume; if the year changes to 2026, update both in-text citations at line 163 ("Gagrčin, Naab, and Grub (2024)") and the entry.

**A8. Healy & Pekarek year/volume suspect (Category 1 / Category 3).**
Line 390: "Healy, J., & Pekarek, A. (**2024**). … *New Technology, Work and Employment, **40**(2), 265–284." *NTWE* volume 40 corresponds to 2025 (Manky's advance-online entry in the same journal is dated 2026). Fix: verify — likely 2025 for the version of record (2024 advance online). If the year changes, update the in-text citation at line 167.

### B. Citation-format inconsistency (Category 4, systematic)

**B1. Multi-author citation abbreviation is inconsistent throughout.** Counts across the manuscript: Zhou et al. appears as the full five-name spell-out **5 times** (lines 48, 123, 324, 548, 581), as "Zhou et al." **4 times** (lines 72, 189, 564, 573), and as "Zhou and colleagues" **5 times**. Hancock, Naaman, and Levy is spelled in full twice (lines 48 and 101 — the second is after first citation), Curchod, Patriotta, Cohen, and Neysen in full three times (lines 167, 269, 273) but "Curchod et al." in Appendix A (lines 489, 495), Sutherland spelled in full at line 324 after "Sutherland et al." at line 183. Under APA 7, every citation of a 3+-author work is "et al." from first use; under APA 6, only the first is spelled out. The current text satisfies neither regime. Fix: adopt APA 7 — "et al." everywhere for Zhou, Hancock, Curchod, Sutherland, Kellogg, Gibbs, Ng, Wing, Gioia, Ferguson, Laupichler, Teece, Iyamu, Gagrčin, Pratt/Kaplan/Whittington, Hong, Scolari, Ayasrah — keeping full author lists only in the References ("Zhou and colleagues" as a narrative variant is fine and can stay).

**B2. Alphabetical order inside multi-work parentheticals violated twice.**
- Line 181: "…represents the formal organization **(Weber, 1978; Simon, 1997)**." APA orders alphabetically: "(Simon, 1997; Weber, 1978)" — which is exactly how line 54 and Table A1 (line 486) render the same pair.
- Line 295: "…as a strategic research site **(Merton, 1987; Eisenhardt & Graebner, 2007)**." Alphabetical order is "(Eisenhardt & Graebner, 2007; Merton, 1987)".
All other multi-work parentheticals (lines 46, 56, 486) are correctly ordered.

### C. Cross-reference integrity (Category 2) — clean, one cosmetic note

Every pointer resolves, and no stale numbering survives:
- **Table 1** defined at line 64; referenced at lines 161 and 495 ("Table 1 there"). ✓
- **Table A1** defined at line 482 in Appendix A; referenced at lines 25 (comment), 54. ✓
- **Table B1** defined at line 566 in Appendix B; referenced at lines 312, 562, 579. ✓
- **Figure 1** defined at lines 219–241; referenced at lines 217 and 243. ✓
- **Appendix A** referenced at lines 54, 330 → exists (line 478). **Appendix B** referenced at lines 243, 295, 299, 312, 316, 318, 322, 579 → exists (line 497). **Appendix C** referenced at lines 287, 330 → exists (line 575). ✓
- **"Table 0"**: zero occurrences. **"Table 2"**: zero occurrences. **"Figure 2"**: zero occurrences. ✓
- Internal section pointers all resolve: "(Constitutive Operations, above)" line 310, "(Foundational Properties, above)" line 281, "(Empirical Strategy, above)" line 526, "(Theoretical Implications)" line 332. Cosmetic: line 332's "the paradox developed above (Theoretical Implications)" points at the parent section while the paradox lives in the H3 subsection "A Paradox the Construct Raises Rather Than Resolves"; pointing at the subsection by name would be sharper. Appendix C's "Propositions 1 through 3 above" (line 583) and "Proposition 4" (line 585) match the main text's division of labor at line 287. ✓

### D. Figure 1 rendering (Category 4)

**D1. The SPECIFYING INTENT box's top border is one character too narrow.** Line 226 (`┌────────────────────┐`) has 20 horizontal characters, but the box walls (lines 227–230, interior width 21) and the bottom border (line 231, 21 characters between corners) are 21 wide, so the top-right corner `┐` sits one column left of the wall below it. Fix: add one `─` to line 226. Everything else in the diagram checks out by column position: the INTERPRETING box (14-wide, corners at columns 8/23) and KEEPING TRACK box (15-wide, corners at 10/26) are internally square; the `▼` connectors at columns 15 and 17 align with the `┬` stubs above them; the return arrow (`└──────┤` at line 235, `┌───▶` at line 221) joins both boxes at the correct columns; box-drawing characters are consistently from the light single-line set with a single `▶` arrowhead.

### E. Arithmetic and reported numbers (Category 3) — clean, with one plausibility flag

All figures the audit brief listed check out, each consistent at every mention:
- **Zhou et al.**: 99 qualitative interviews → 14 candidate items → 12 final items "distributed evenly across four subdimensions" (12/4 = 3 each ✓); N=275 (EFA), N=213 (CFA), N=230 (validation), N=225 (panel), reliability .85, r=.37 (p<.01) and r=.04 (n.s.) — each stated once, no contradictions; cited item numbers (6, 8, 11) all ≤ 12. ✓
- **Rahman**: "eighteen clients alongside eighty platform freelancers" (line 141) and "eighteen human clients" (line 145) — consistent; page cites (pp. 956, 963, 976) fall within the entry's 945–988 range. Five invisible-cage properties enumerated as five, "fifth structural property"/"fifth dimension" used consistently (lines 143, 205, 579). ✓
- **Sutherland et al.**: "twenty freelancers and nineteen clients" (line 149), stated once; five platform literacies listed as five (line 151); page cites within 457–475. ✓
- **Manky N=40** (line 171), **Chigbu 2 of 103** (line 518), **Oeldorf-Hirsch 50 screened from 96** (line 163), **Gagrčin 169 publications** (line 163), **Iyamu 12 studies** (line 163) — each stated once, internally coherent. ✓
- **Long & Magerko**: 17 competencies; "only two… explicitly reference human actors" backed by exactly two named (Competency 10, Competency 5). The line-119 claim that "nine competencies govern technical mechanics while only one addresses normative application" is a characterization of their taxonomy, not an arithmetic error (9 + 1 ≤ 17). ✓
- **Spitzberg**: four skill clusters, five context facets, five outcome criteria — each list matches its count; page cites within 629–666. ✓
- **Structure counts**: 7 constructs = 7 non-algorithmacy rows in Table 1; 5 forms × 6 questions = Table A1's grid; 4 research questions ↔ 4 harness modules ↔ 4 Table B1 rows, and the mapping (decoding→interpreting, transmitting intent→specifying intent, unannounced change→keeping track, perceived errors→candidate fourth operation) is one-to-one as claimed at lines 312 and 534. Survey waves at weeks 1, 4, 16 stated identically three times (lines 316, 546, 564) against a sixteen-week course. ✓
- **IRB**: "exempt determination… on 11 May 2026 (Protocol 260511078)" (line 548) — stated once; the protocol number encodes 26-05-11, matching the stated date. Internally consistent.

**E1. The one plausibility flag: "two-year history" (Category 3/6).** Line 512: "The initiative's **two-year history** is that spiral enacted across five institutional configurations" and line 522: "What these **two years** of developmental fieldwork yielded…" — but the program "launched in July and August 2025" (line 512) and the manuscript is dated 28 August 2026 (comment block; second transcript recorded 22 August 2026). Thirteen months is not two years. Fix: "the initiative's history" / "this developmental fieldwork," or "the program's first year," unless the author intends to date the history from pre-launch design work — in which case say so.

### F. Formatting consistency (Category 4) — minors

- **F1. Heading levels**: `## Abstract` (line 34) is H2 while every sibling top-level section (`# Introduction`, `# References`, `# Appendix A`…) is H1. Fix: promote to `# Abstract` or accept the convention deliberately.
- **F2. Hyphenation**: "specialized **software-engineering** course" (Abstract, line 36) vs. "specialized **software engineering** course" (lines 46 and 50). Pick one (the hyphenated compound modifier is correct APA style).
- **F3. Em-dashes**: uniformly spaced (` — `) throughout; a programmatic scan found **zero** unspaced em-dashes. Clean, and consistent with house usage.
- **F4. Verbatim repeated quotation**: the Riordan (1995, as cited in Coghlan & Brannick, 2014) quotation — "require[s] a practitioner of science who is not only an engaged participant…" — appears in full twice, at lines 295 and 528. The house style file explicitly targets verbatim repetition across sections; keep the Appendix B instance and paraphrase or truncate the line-295 one (or vice versa).
- **F5. "&" vs "and"**: correct throughout — all parenthetical citations use "&" (with the serial comma before it, e.g. "(Hong, Cheng, & Liu, 2026)"), all narrative citations use "and". No violations found.
- **F6. Reference-entry punctuation**: serial comma before "&" is consistent across all multi-author entries. ✓
- **F7. Table formatting**: all three tables use consistent pipe-markdown with bolded caption lead-ins (`**Table 1.**`, `**Table A1.**`, `**Table B1.**`) matching `**Figure 1.**`; header separators well-formed. ✓
- **F8. Nonstandard reference entries** (minor, worth a pass before the camera-ready): (a) line 396 "ILO. (2025)" — APA spells out the corporate author: "International Labour Organization. (2025)." (alphabetization under I is unaffected); (b) line 340, the anonymous preprint entry carries an editorial sentence ("Unrefereed preprint, posted 25 June 2026; authors not retrievable…") — APA would put the retrieval caveat in brackets or a note, not as free prose in the entry; (c) line 392 Hong et al., *Big Data & Society* "13(2)" and line 398 Iyamu et al., *Frontiers in Public Health* "14" lack article numbers (both journals use e-locators); (d) line 454 Stark & Vanden Broeck, *Organization Theory* "5(2), 1–24" — this journal paginates by article number; verify.
- **F9. Solo author, plural self-reference (Category 6)**: the byline is a single author (line 3), the paper says "we" throughout, and Appendix C says "**the authors'** own institutional stake" (line 577) and "**the authors** hold no institutional stake" (line 585). Whatever register call the author makes on we-vs-I (the house Annals calibration prescribes "I" for solo work — a decision above my lens), "the authors" plural is a plain inconsistency with the byline. Fix: "the author's" / "the author holds."
- **F10. Abstract length**: 239 words. The house Annals calibration caps abstracts at 200; if the PDW inherits that bar, trim ~40 words (the transcript-count fix in A3 is a natural place to start).

### G. Reference list alphabetization (Category 5) — clean

Strict first-author-surname order verified across all 69 entries, including every adjacent pair that could go wrong: Abidin → "AI-mediated…" (b < i) → Anteby; Bamberger → Blumer → Bothello → Bowen → Bradach → Brannick; Chigbu → Coghlan; Gagrčin → Gibbs → Gioia → Gittell; Hancock → Hayek → Healy → Hong → Hu; ILO → Iyamu; Mahy → Manky → Mercer → Merton → Möhlmann (ö as o); Pratt (2009, single author) **before** Pratt, Kaplan, & Whittington (2020) — correct APA single-before-multi ordering; Spitzberg (2006) **before** Spitzberg & Cupach (1984) — correct (single author precedes multi-author regardless of year); Stark & Pais **before** Stark & Vanden Broeck (second surname P < V). No violations.

### H. Secondary citations — correctly handled

"Riordan, 1995, as cited in Coghlan & Brannick, 2014" (lines 295, 528) and "Reason and Marshall (1987, as cited in Coghlan & Brannick, 2014)" (line 548) are properly formatted secondary citations, and correctly have **no** References entries of their own (only the Coghlan & Brannick source is listed). ✓

---

## Closing note: citation resolution status

Citation resolution is **not** 100% clean. Exact count of unresolved issues: **4**.

- **Forward (in-text → References): 1 unresolved.** Nutbeam (line 163, twice) has no year and no entry. Every other in-text citation — 66 distinct works across body, tables, and appendices — resolves to a References entry with matching author spelling and year (including diacritics: Gagrčin, Möhlmann, Establés).
- **Reverse (References → in-text): 3 unresolved.** Bamberger & Pratt (2010) and Bothello, Nason & Schnyder (2019) remain orphaned as previously known; **Jarrahi & Sutherland (2019) is a new orphan** introduced or left behind in the restructuring.

Two further entries resolve but carry suspect year/volume pairings to verify against the version of record (Gagrčin et al. — internally impossible against Oeldorf-Hirsch & Neubaum; Healy & Pekarek), and one entry has a confirmed wrong volume (Blumer: 19, not 18). Cross-reference integrity (appendices, tables, figure) is fully clean; arithmetic is fully clean except the "two-year history" overstatement; alphabetization is fully clean.

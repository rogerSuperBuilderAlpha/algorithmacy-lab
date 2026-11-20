# AUDIT_R6: adversarial audit of the R-round reviews (R1–R5) and their cards

*Auditor R6, 2026-10-24. Agent-drafted. The author has not reviewed it, and none of the text is the author's. I wrote
none of the reviews or cards audited here. I changed no card, review or other file; this is the only file I wrote in
the repo. Substance only; no comment below concerns wording.*

**Date.** 2026-10-24.

**Scope.** (1) Every verdict of *misused*, *contested*, *unsupported* or *wrong* in `R1_historical_concepts.md`,
`R2_present_case_concepts.md`, `R3_normative_frame.md`, `R4_argument_audit.md` and `R5_novelty_counter_case.md`, and
every *narrower* verdict that changes a premise or a duty. (2) The 36 cards with `facet: R1`, `R2`, `R3` or `R5` in
`literature/cards/berthon_ethics_paper/`. (3) R4's WRONG, MISUSED and CONTESTED rows read against `DRAFT_v1.md` and
the cards R4 cites. (4) The items the brief singled out: R1-04 (Saenger), R1-26 (Arundel via Foxe), R1-17 (Lassiter),
R2-16 (GDPR art. 22, *SCHUFA*, *Dun & Bradstreet*), R2-14 (Regulation 2026/1744), R2-20 (Decision 2026/2274),
R3-02 (Gädeke), R3-05 (Lazar), R5 rank 1 (Ho et al. 2019; Felt et al. 2015), and the "thirteen million views" claim.

**Checks run.**
1. sha256 recomputed for every R-card `local_path` (35 files; `arbel2025how` is an abstract card with `null`, as it
   should be): 35 of 35 match. R2's four own copies cited in its §4 (CERT CSG 7, GDPR, AI Act, Omnibus): 4 of 4 match
   the hashes R2 states.
2. Exact-string match of every quotation in the 36 cards against the file at `local_path` (script; whitespace,
   curly quotes, line-break hyphens, ligatures and OCR `¬` normalised), then by eye for every miss. PDFs read with
   `pdftotext`; HTML tags stripped; downloads read with `python3 -I`. Misses that were card prose caught between
   quotation marks are not reported. Real differences are in the tables.
3. Page check for every page-cited quotation in the new PDF cards (Gädeke: printed = PDF + 197; Lazar lecture: footer
   numbers; Ho 2019: PDF + 403; Knapp: PDF + 1082; Felt: PDF + 2892) and running-head checks for the two OCR books
   (Foxe vol. 3; Thomson 1759).
4. Crossref record (no `mailto`) and `filter=updates:` for the 14 DOIs on the new cards, plus Whelan 2012,
   Hussain and Moriarty 2018 and the Jin–Leslie 2019 reply that the reviews cite at record depth: all 17 resolve with
   matching title, venue, year and pages; no update, correction or retraction notice on any. OpenAlex abstract for
   Arbel and Becher (2025) matches the card's paraphrase.
5. Primary legal texts reopened: GDPR (R2 copy) arts 13(2)(f), 14(2)(g), 15(1)(h), 22(1), 22(3); AI Act (R2 copy)
   arts 14(4)(e), 26(11), 50(1), 73(1), 85, 86(1) and the chapter and section headings around art. 73; Regulation
   2026/1744 Art. 1(40); Decision 2026/2274 (header, recitals 3 and 6, Art. 1, Annex); *Dun & Bradstreet* judgment
   text (`N2_platform_law/eu/62022CJ0203.txt`) paragraphs 55, 58, 59, 77.
6. The Saenger trail: `facets/BRIEF.md` §6, `ADJUDICATION.md` §5.2, `DRAFT_NOTES.md`, and the dxd arm's
   `literature/audit/AUDIT_01.md` and `AUDIT_06.md` rows on Saenger pp. x, 83, 85, 87, 100; one archive.org
   full-text query per identifier to test R1's search-log claim (public API, no CAPTCHA met).
7. The Nadella capture (`berthon_ethics_local/nadella/x/…txt`): header counts, paragraph count, whole-word counts of
   *user*, *customer*, *employee*, *people*, *affected*, *Orgs*.
8. For R4: each cited draft line reread; each cited card's Key facts reread.

**Disclosure.** No e-mail address, `mailto` or Unpaywall call. No paywall, bot wall or CAPTCHA met or bypassed (Crossref,
OpenAlex and the archive.org full-text API only). No Chrome tools, no git, no new downloads; every file read was
already at a card's `local_path` or in the arm.

**Result in one line.** The R-round's quotations, hashes and locators hold almost without exception (no fabricated
quotation, no hash mismatch, two minor misquotations); the faults are in verdict strength: R1 strips Saenger
quotations that a logged clean route already confirms, R5 calls a sourced view count unsourced, R2 misplaces the
AI Act's incident article, R3 reads Gädeke's structural test as a dependency test, and R4 grades three pairings
"misused" where the draft's own text supports "narrower".

Status key: VERIFIED verbatim / VERIFIED paraphrase / WRONG / OVERSTATED / NEEDS LIBRARY CHECK / COULD NOT CHECK.
"Disagree" in the rate tables means WRONG or OVERSTATED.

---

## Table 1. R1, historical concepts

| Item | Run | Status | Evidence | Note |
|---|---|---|---|---|
| R1-01 *scriptio continua* narrower | R1 | VERIFIED paraphrase | `dxd/heilmann2020reading` pp. 182-183 (interpuncts; second-century abandonment), audited in dxd AUDIT_01 | Card-based; I did not reopen Heilmann. |
| R1-03 Insular correction contested | R1 | VERIFIED paraphrase | Heilmann pp. 178, 181 (Vatri p. 639) and O'Donnell ¶4, all confirmed in dxd AUDIT_01 (rows "B Q2") | Holds at the strength stated. |
| R1-04 Saenger quotations "unsupported" | R1 | **WRONG** | dxd `AUDIT_01.md` (2026-10-13), route 1 Google Books search-inside id `w3vZaFoaa3EC`: p. x "not a general history of literacy" (Google p. x; lending scan); p. 83 "before 692 and 713" (Google p. 83; lending scan); p. 87 "regularly inserted" (both routes, "The correct page is 87"); dxd `AUDIT_06.md` row 305/309/344/350: the p. 85 "shortcuts" sentence "Google p. 85 returns both halves; whole sentence matched as one phrase", VERIFIED verbatim. `DRAFT_NOTES.md` records exactly this ("confirmed on Google Books and the lending scan (AUDIT_01, AUDIT_06)"). | BRIEF §6 names Google Books search-inside as a clean route. Four of the five pages the draft cites have it; p. 100 ("mid-tenth century") is cited in AUDIT_01 rows 55 and 105 without an explicit Google page: NEEDS LIBRARY CHECK for p. 100 only. R1's search observation is reproducible today (my FTS query: lending scan `spacebetweenword0000saen` 0 hits; the unauthorised upload 1 hit), but AUDIT_01 logged lending-scan hits on 13 Oct, so the index, not the text, changed. R1 read dxd facets A and K but not the dxd audits. |
| R1-05 Carolingian page "misused" | R1 | VERIFIED paraphrase | `boretius1883capitularia` pp. 80-81: "librariorum imperitia depravatos … correximus"; "nostra eadem volumina auctoritate constabilimus … ad legendum"; N2 (d) "no source ties it to word separation" | The sources carry custody of the corrected text; the draft (ll. 167, 171-172) says "conventions of the page". Label quibble: "unsupported" is the exact category (no source carries the claim) rather than "misused" (concept means something else). Same substance. |
| R1-06 charter purpose contested | R1 | VERIFIED paraphrase | `blayney2013stationers` (secondary: Smyth, LRB 2015), `clegg1997press` (abstract: publisher page), `johns2002how` p. 119 | Holds as a flag that the purpose is disputed; the Blayney characterisation rests on one review and a blurb, which the cards say. |
| R1-09 "statutes that licensed who could read" narrower (Arundel 1409) | R1 | VERIFIED verbatim for the quotation; **OVERSTATED** for the inference | Foxe vol. 3 OCR: the seventh constitution sits between the running heads "244 THE C[RU]EL CONSTITUTIONS OF ARUNDEL" (file line 19886) and "246" (line 20037), at lines 20005-20027: "no man read any such book, libel or treatise, now lately set forth in the time of John Wickliff … until the said translation be allowed by the ordinary of the place" (margin notes "laUon", "And jet" intrude in the OCR). Second scan carries the same clause. p. 245 confirmed. | The constitution licenses *translations* and bars reading of unlicensed ones by anyone; the 1543 Act licenses *readers* by rank and sex. "Licensed reading predates print" is true of what may be read, not of who may read. The draft's "statutes that licensed who could read" (l. 59) is not shown to have a manuscript-era precedent by this instrument. R1's narrowing of the plural "statutes" to one Act stands on N2 claim 5. |
| R1-12 Commons 1695 holds (narrower) | R1 | VERIFIED verbatim | `deazley2008commentary1662` §§2, 5, 6: "little to do with freedom of speech and the liberty of the press"; "finally expired"; Kenyon "rather than any abstract love of freedom": all exact in the saved page | — |
| R1-13 "duty to read" narrower | R1 | VERIFIED verbatim | `knapp2015duty`: p. 1083 "presumption of knowing assent" (PDF 1); p. 1085 "not a 'duty' imposed by contract", "as a 'duty,' and as a 'presumption'" (PDF 3); pp. 1108-1110 (PDF 26-28) all exact at the stated pages | — |
| R1-14 *L'Estrange* "absolute" narrower | R1 | VERIFIED verbatim | `bec/lestrange1934graucob`: headnote p. 395 "Held, by the Divisional Court"; p. 403 "in the absence of fraud, or, I will add, misrepresentation"; p. 405 Maugham | — |
| R1-15 *Parker* narrower | R1 | VERIFIED verbatim | `parker1877south` p. 423 "under no obligation to read the ticket"; p. 424 "reasonably sufficient"; p. 425 onus (Baggallay); N7a N3-17/18 | — |
| R1-16a Requerimiento origin contested | R1 | VERIFIED paraphrase | `israeli2022requerimiento` Critical notes (Seed; Muldoon/Pagden); `seed1995ceremonies` (review depth) | Seed and Muldoon unread, as R1 says. |
| R1-16b "informed after the fact" wrong | R1 | VERIFIED paraphrase | Ledger H18: "Read aloud in Spanish before an attack"; Israeli p. 62 (card): "self-legitimation"; draft l. 422 "informed after the fact that something was done to them" | R4's "disclosure" row reaches the same finding independently. |
| R1-17 *Lassiter* narrower | R1 | VERIFIED verbatim | CAP text: "some relation to standards designed to promote intelligent use of the ballot" between `*51` (offset 8468) and `*52` (10329), p. 51; "We do not sit in judgment on the wisdom of that policy" after `*53` (10891), p. 53; "No such influence is charged here" p. 53; "lay springes for the citizen" after `*54`, p. 54. `katzenbach1966south` card pp. 333-334 reaffirmation | The card's "pp. 51-52" for "Literacy and intelligence are obviously not synonymous" is exact: the `*52` marker falls inside the word "Literacy". |
| R1-21 Easton clerk holds, contested on the clerk | R1 | VERIFIED verbatim (by eye) | Thomson 1759 OCR (long s as "f"): l. 6681 "down his Pen, and declare he would not take"; ll. 6718-6724 "Teedyufcung, looking upon this as a Denial, was much diffatisfied … lead him on blindfold, and in the Dark, or to take Advantage of his Ignorance"; ll. 6740-6760 "as no Indian Chief before him ever demanded to have a Clerk … againft his Judgment … if you infift upon having a Clerk, I fhall no longer oppofe it"; "The Perfon he nominated was one Charles Ihomfon, who had, at the particular Requeft of Mr. Peters, taken Minutes at the laft Eafton Treaty". Folios "( Til )" = 111 and a damaged "( )" = 112, as the card says. `pennsylvania1851minutes` names "Thompson" at the public treaty | The card's quotations are the OCR with long s normalised; every one is present. |
| R1-22 jurat narrower | R1 | VERIFIED verbatim | `lely1883judicature` pp. 276-277 "unless the court or a judge is otherwise satisfied"; margin "Extended to blind persons in 1883" (p. 277) | — |
| R1-23 art. 193 dated 2007 narrower | R1 | VERIFIED paraphrase | `bec/spain1944reglamento`: "art. 193 as amended by RD 45/2007 (in force 30 January 2007)"; "I did not read the earlier versions" | — |
| R1-26 periodization narrower | R1 | **OVERSTATED** (one limb) | Limb (a) rests on R1-09's Arundel reading (see above): the 1409 licence is a licence of texts, not of readers. Limbs (b)-(e) rest on `ade/johns1998` p. 36, `johns2002how` pp. 119, 121, ledger H11 and the draft's own l. 147, which hold at card depth | The verdict "two recurring choices, not two stages" survives on limbs (b)-(e); it should not cite Arundel for "licensed who could read". |
| R1-27 Johns–Eisenstein contested | R1 | VERIFIED paraphrase | `johns2002how` (full); `ade/eisenstein2002` second-hand | Eisenstein unread, as stated. |
| Card `lassiter1959northampton` | R1 | VERIFIED verbatim | sha256 match; 6 of 6 quotations exact at the star pages | — |
| Card `foxe1837acts` | R1 | VERIFIED verbatim | sha256 match; p. 242 heading, p. 245 sixth and seventh constitutions, pp. 398-399 gloss present (eye-checked; OCR margin intrusions); page by running heads in two scans | — |
| Card `knapp2015duty` | R1 | VERIFIED verbatim | sha256 match; 7 of 7 quotations at the stated pages; no DOI (confirmed none in Crossref by the card; not re-searched) | — |
| Card `thomson1759enquiry` | R1 | VERIFIED verbatim | sha256 match; 11 of 11 quotations present in long-s OCR | Folios damaged for 111-112, as the card says. |
| Card `deazley2008commentary1662` | R1 | VERIFIED verbatim | sha256 match; 10 of 10 quotations exact | — |
| Card `blayney2013stationers` | R1 | VERIFIED paraphrase | sha256 match (LRB page); Crossref 10.1017/cbo9781139542715, monograph, 2013-11-21, no updates; chapter titles are from the second saved file (`cambridge_book.html`), as the card says | Secondary card, paraphrase only: compliant. |
| Card `clegg1997press` | R1 | VERIFIED paraphrase | sha256 match; Crossref 10.1017/cbo9780511585241, monograph, 1997-08-07, no updates | Abstract card: compliant. |

## Table 2. R2, present-case concepts

| Item | Run | Status | Evidence | Note |
|---|---|---|---|---|
| R2-01 "insider risk" as CERT uses it | R2 | VERIFIED verbatim | CERT CSG 7 PDF p. 10 (printed p. 3): "potential for an individual who has or had authorized access to an organization's critical assets to use their access, either maliciously or unintentionally, to act in a way that could negatively affect the organization"; "impact and likelihood associated with the realization of an insider threat"; sha256 `c2640e3c…` matches R2's statement | — |
| R2-04 Copilot terms bind the principal, not the second party | R2 | VERIFIED verbatim | `microsoft2026copilot`: "When you request that Copilot take Actions on your behalf, you are solely responsible…" | R4's "second party" and "reading" rows reach the same finding. |
| R2-07 approvals in preview | R2 | VERIFIED paraphrase | `microsoft2025multistage` title "(preview)"; "the feature is in preview" | — |
| R2-08 chain of thought: open-weight counter-sources | R2 | VERIFIED verbatim | `openai2025gpt` README: "Full chain-of-thought: Gain complete access to the model's reasoning process … It's not intended to be shown to end users."; `microsoft2026tutorial`: "content wrapped in <think>...</think> tags", "Others, like o1, output only the completions." | The README's opening sentence carries a hyperlink inside it ("[OpenAI's open-weight models](…)"), which the card's quotation omits; not a misquotation. |
| R2-10 2022 Standard "re-engineered" | R2 | VERIFIED paraphrase | `microsoft2026responsible` PDF pp. 4, 20 (card): "re-engineered"; "Deployer Chapter" | — |
| R2-12 approvals and interrupts | R2 | VERIFIED verbatim | `anthropic2026measuring`: "roughly 20%" → "over 40%"; interrupts "5% of turns" → "9%" | — |
| R2-14 AI Act art. 73 "does not yet apply" | R2 | **WRONG** (locator), OVERSTATED (conclusion) | Regulation 2026/1744 Art. 1(40)(b), replacing art. 113 third paragraph point (c): "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 … Annex III; and (ii) 2 August 2028 … Annex I" (exact, lines 622-626; R2's dates hold). But in the AI Act text (R2's own copy) art. 73 stands under "CHAPTER IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE", "SECTION 2 Sharing of information on serious incidents" (lines 1715-1727), not Chapter III Section 3 (that section, "Obligations of providers and deployers of high-risk AI systems and other parties", begins at line 869). The Omnibus recital says the deferral concerns "the obligations related to high-risk AI systems laid down in Sections 1, 2 and 3 of Chapter III"; the general application date stays 2 August 2026 | Art. 73 is in force. R2's conclusion survives only by a route R2 did not state: art. 73 binds "providers of high-risk AI systems", and the classification rules (art. 6, Chapter III Section 1) are deferred, so the duty may lack an object until December 2027. The draft's "requires" (l. 413) is the article's own present tense; R2's proposed "Will require from Dec 2027" is as imprecise as what it replaces. The Annex III point (a refund agent is not listed) holds. |
| R2-15 AI Act second-party provisions | R2 | VERIFIED verbatim | R2 copy: art. 14(4)(e) "'stop' button or a similar procedure" (l. 854); art. 26(11) "shall inform the natural persons that they are subject to the use of the high-risk AI system" (l. 1037); art. 50(1) (l. 1290); art. 85 (l. 1880); art. 86(1) "clear and meaningful explanations of the role of the AI system" (l. 1884) | Arts 26(11) and 86 are Annex III provisions and so share the December 2027 date. |
| R2-16 GDPR art. 22 and the CJEU against A8 | R2 | VERIFIED verbatim | GDPR (R2 copy): art. 22(1) l. 756 "right not to be subject to a decision based solely on automated processing"; art. 22(3) l. 764 "at least the right to obtain human intervention … to express his or her point of view and to contest the decision"; art. 15(1)(h) l. 682 and its twins at 13(2)(f), 14(2)(g). `bec/cjeu2023schufa` para 52 "lays down a prohibition in principle" (S2-verified). *Dun & Bradstreet* judgment text: para 58 "In order to enable the data subject effectively to exercise the rights conferred on him or her by the GDPR and, in particular, Article 22(3) thereof, that explanation must be provided by means of relevant information and in a concise, transparent, intelligible and easily accessible form"; para 58 and operative para 77 "procedure and principles actually applied"; para 59 "mere communication of a complex mathematical formula, such as an algorithm". The paper card `eu2016gdpr` reads arts 33, 34, 77, 79, 80, 82 only; art. 22 is on the course card and ledger E05 | The "wrong, in part" verdict holds at the strength stated: the draft's §4 describes the GDPR as breach notice plus remedy (ll. 472-473, 419-420) and omits art. 22, which the library carries. R2's own limits (post-decision rights; controller-run review; "similarly significantly affects" contested for a refund) are right and keep A8 alive in restated form. The Digital Omnibus status is unconfirmed in any official text, as R2 says. |
| R2-17 US law for the second party | R2 | VERIFIED verbatim | `cfpb2026notifications` § 1002.9(a)(2), (b)(2) exact in the eCFR XML; `colorado2024consumer` § 6-1-1703(4)(b), 1706(1), 1706(6), "ON AND AFTER FEBRUARY 1, 2026" exact; `colorado2026automated` §§ 6-1-1701(15), 1704(1)-(3), 1705(1)(a), 1706(1)(b), 1709(1), SECTION 5 exact (two by eye: the PDF text runs "ADMTTO" and interleaves "PAGE 23-SENATE BILL 26-189" inside the SECTION 5 sentence); `cppa2025text` §§ 7001(ddd), 7200(b), 7220, 7221(a)-(b), 7222(b) exact (the extraction reads "Optout" for "Opt-out") | The SB 26-189 signing date (14 May 2026) comes from the bill page by WebFetch, not from the PDF, as the card says. |
| R2-18 DSA against A5's general form | R2 | VERIFIED verbatim | `eu2022dsa` arts 14(1)-(2), 17(1)-(4) exact in the CELLAR text | — |
| R2-19 SB 53 and the refund case | R2 | VERIFIED paraphrase | `california2025transparency` (N4, N7b-verified); not reopened | — |
| R2-20 EN 18286:2026 cited in the OJ | R2 | VERIFIED verbatim | Decision 2026/2274 text: header "L series 2026/2274 14.10.2026 … of 12 October 2026"; recital 3 "This resulted in the adoption of the new harmonised standard EN 18286:2026."; recital 6 presumption sentence; Annex "EN 18286:2026 Artificial intelligence – Quality management system for EU AI Act regulatory purposes" | The card's point that Art. 17(1)(i) covers serious-incident reporting procedures is the Act's text (not re-opened). |
| R2-23 worked refund case narrower | R2 | VERIFIED paraphrase | Derivative of R2-08, R2-14, R2-16, R2-19 | Inherits the R2-14 caveat. |
| R2-24 facts about the post | R2 | VERIFIED verbatim | Capture: 21 essay paragraphs (the capturer's "[P22] (end of post)" is a marker); whole-word *user* 1 hit, in the capturer's header line 3 ("the user's Chrome"), none in P1-P21; *customer*, *employee*, *people* 0; "those affected" once (P20); "Orgs" once (P17); header "Counts at capture: 13M views" on 12 Oct 2026 | R2 is right on every count, including the view figure (see R5-04). |
| Cards `cfpb2026notifications`, `colorado2024consumer`, `colorado2026automated`, `cppa2025text`, `eu2022dsa`, `europeancommission2026commission`, `microsoft2026tutorial`, `openai2025gpt` | R2 | VERIFIED verbatim | sha256 8 of 8 match; every quotation present (misses were card prose); no DOIs | — |
| R2's own copies (`cert_csg7`, `gdpr`, `aiact`, `omnibus`) | R2 | VERIFIED | 4 of 4 hashes match R2 §4 | These are not cards; R2 asks the lead to extend `eu2016gdpr`, `eu2024aiact`, `euomnibus2026`. |

## Table 3. R3, normative frame

| Item | Run | Status | Evidence | Note |
|---|---|---|---|---|
| R3-01 definition of domination | R3 | VERIFIED verbatim | Lovett SEP (local) §1.2; Gädeke p. 201 (PDF 4) "(1) they have the capacity to interfere (2) on an arbitrary basis (3) in certain choices" | — |
| R3-02 domination of a customer: contested, narrower | R3 | VERIFIED verbatim (quotations); **OVERSTATED** (prescription) | Gädeke, every quotation at its page: p. 199 (PDF 2) "structurally constituted form of power"; p. 200 "Purely interactional forms of power, which are based on an opportunistic capacity to interfere, however, are not instances of domination … serves as the basis of a persisting status asymmetry"; p. 202 "institutionally stabilized", "explicitly considers the mugger"; p. 203 (PDF 6) Richardson's kidnapper; p. 205 n. 23 judge; p. 207 triadic, "position of power"; p. 208; p. 215 n. 53; p. 219. Lovett §1.3 "absence of any structural dependence on arbitrary power"; §4.1 "markets as such need not involve domination (Pettit 2006)"; `bec/pettit2006freedom` p. 142 | The dispute is real and the card states it fairly. But Gädeke's test is *structural enablement* ("norms and practices") plus a *persisting status asymmetry*, not the customer's dependency on, or inability to exit, one firm; a firm's power over its customers rests on contract law and terms of service, which are norms and practices, and the firm–consumer asymmetry persists whichever vendor she picks. R3's instruction to "concede the episodic retail case" imports Lovett's "structural dependence" and Pettit 2006's exit argument, which are different tests. Gädeke's text leaves the retail case open; the draft must *argue* structural enablement for it, not concede it. |
| R3-03 arbitrariness: procedural or democratic | R3 | VERIFIED verbatim | Lovett SEP (local): "common knowledge to all persons or groups concerned"; "directly or indirectly controlled by the concerned persons"; "resilient over a wide range of possible changes"; `gadeke2020mugger` p. 205 n. 23; `hamilton2025digital` p. 10 "create antipower for users" | — |
| R3-04 route 2 "carries the old verdicts" narrower | R3 | VERIFIED verbatim | Lovett §4 "anachronistically implement the republicanism of yore", "accidental prejudices of their day"; Hamilton p. 5; `celikates2023critical` §2.1 "not (or not yet) recognized" | The inference (route 2 is external critique, re-judging both eras) is R3's and follows from the SEP taxonomy. |
| R3-05 Lazar's rival frame contested | R3 | VERIFIED verbatim | Lecture I, footer pages: p. 14 "constitutes (in whole or part) the social relations"; p. 15 "typically in ways that profit the intermediary"; p. 19 "govern their users"; p. 20 n. 80 "conflate an internally diverse suite of normative concerns"; p. 23 "Benevolent, procedurally legitimate authoritarianism", "ultimate source of the authority", "If A has power over B"; p. 24 "unilaterally and intransparently"; p. 37. Preprint 2208.08628: PDF p. 1 publicity, p. 5 "one-way control" and n. 15, p. 8 n. 27 "impossibility and undesirability", p. 11 three components. Lovett §2.1 "security of non-interference (Goodin 2003; Carter 2008; Kramer 2008…)" | Holds at the strength stated; the version of record (P&PA 2025; OSPP 10 pp. 28-56, Crossref) unseen, as the cards say. |
| R3-06 three benchmarks narrower | R3 | VERIFIED paraphrase | `walzer1988interpretation` 34, 59, 70 n. 17 (card); Celikates §2.1; `vonsamson2025immanent` 1316-1318; `gowans2026moral` §7 "real confrontations" | — |
| R3-07 pairing coherent, narrower | R3 | VERIFIED verbatim | Walzer p. 65 "Conversation is parasitic on commonality…", p. 66 "a minimal code" (card); von Samson p. 1308 "structurally conservative", p. 1318 "methodology, not metaethics", "We might have signed a contract" | — |
| R3-08 Bartha: plausibility, not verdict | R3 | VERIFIED verbatim | Bartha SEP (local): "prima facie plausibility"; "an analogy is used to show that a conjecture is worth taking seriously"; "there must be no critical disanalogy between the domains"; "It pre-supposes a common set of social values" | Changes A6's claim from verdict to plausibility; the text supports it. |
| R3-09 contribution 1 against political CSR | R3 | VERIFIED paraphrase; NEEDS LIBRARY CHECK (one clause) | `lindman2023big` pp. 145-146, 152 exact in card; Crossref: Whelan, *BEQ* 22(4) 709-737 (abstract: "four ambiguities, conflations and/or oversights"); Hussain and Moriarty, *JBE* 149(3) 519-534 (no abstract in Crossref) | R3's clause that Hussain and Moriarty's "accountability-reversal argument is, from the record, close to the draft's" rests on a title; the lead should treat it as a lead, not a finding, until the paper is read. |
| R3-10 contribution 2 "who must read" | R3 | VERIFIED paraphrase | `bec/benshahar2011failure` p. 647 and the card's pages 687, 711-712, 742 (R3 confirmed in the local text; I confirmed the card); `calo2012against` pp. 1034, 1049, 1050, 1060 exact in card | — |
| R3-11 contribution 3 Frahm | R3 | VERIFIED verbatim | `frahm2022fixing` p. 175 "democratic deficit of innovation"; p. 200 "insufficiently equipped"; p. 203 "locates both the power" (N7a-verified) | — |
| R3-12 responsibilization | R3 | VERIFIED verbatim | `bec/giesler2014creating` p. 841, p. 851; `bec/docherty2026civilizing` pp. 17-18 | — |
| R3-13 four scaffold conditions contested | R3 | VERIFIED paraphrase | `bec/collins1987cognitive` p. 3 "reduces his participation (fades)"; Wood et al. and Pea unread (R3 says so) | Pea 2004 is characterised from its title and record only; the lead should not cite R3's gloss of Pea without the paper. |
| R3-14 "second party" vs third party, stakeholder | R3 | VERIFIED verbatim | `bec/kolt2025governing` p. 335 inclusivity; Lazar p. 15; Gädeke p. 207; Phillips 2003 record only | — |
| R3-16 "new relevance" narrower | R3 | VERIFIED verbatim | Walzer p. 69 "it isn't universally known", p. 70 "a new relevance"; `kugelberg2026practice` p. 10 "fundamental reform"; Gowans §7 | — |
| R3-17 missing objections | R3 | VERIFIED verbatim | Hamilton preprint p. 6 (PDF): "algorithmic governance can decrease domination for three reasons. First, algorithms do not have wills or intentionality … Second, algorithms eliminate the need for human discretion … Third, algorithms eliminate the biases in human judgment that are determined by mood, hunger, pride"; `bec/scherer2023guest` p. 422 "form of interference with one's liberty"; `ade/bennlazar2022` §6 "largely misses the point", "collective action problems"; von Samson p. 1308 | — |
| R3-19 abstract vs §1 | R3 | VERIFIED paraphrase | Draft ll. 16-17 (abstract: objections, promises, professions) against ll. 76-78 (domination carries the verdicts) and l. 22 keyword | A real inconsistency in the draft's own text. |
| Card `gadeke2020mugger` | R3 | VERIFIED verbatim | sha256 match; 12 of 12 quotations at the stated pages (printed = PDF + 197 confirmed); Crossref JPP 28(2) 199-221, issued 2019-09-10, no updates | — |
| Card `lazar2024governing` | R3 | VERIFIED verbatim | sha256 match; 9 of 9 at the footer pages; published DOI 10.1111/papa.12279 unseen (card says so) | — |
| Card `lazar2024legitimacy` | R3 | VERIFIED verbatim | sha256 match; 5 of 5 at the PDF pages; Crossref OSPP vol. 10, pp. 28-56, 2024-05-07, no updates | — |
| Card `sparks2022rule` (secondary) | R3 | VERIFIED paraphrase; **WRONG** (one sentence) | sha256 match (Hamilton preprint); Crossref MPP 9(2) 201-218, 2022-01-06, no updates. The card says "The third reason was not captured in the passage read"; Hamilton p. 6 states it in the next sentence (biases "determined by mood, hunger, pride, and the like") | Minor. Add the third reason; add volume and pages to `venue`. |

## Table 4. R4, the argument's logic (read against the draft and the cards)

| Item | Run | Status | Evidence | Note |
|---|---|---|---|---|
| HP1 wrongness transfers only through A7 (contested) | R4 | VERIFIED paraphrase | Draft ll. 74-78: "The present wrong does not follow from the past one by itself. It follows because…"; ll. 449-455 | The draft says what R4 says it says. |
| HP2 position, not intent (wrong for F5, F6) | R4 | **OVERSTATED** | `bec/katzenbach1966south` p. 310 "specifically designed to prevent Negroes from voting", pp. 333-334 "instituted with the purpose of disenfranchising Negroes"; `northcarolina1831acts` preamble "tendency to excite dissatisfaction"; `bec/alabama1901official` p. 8 "to establish white supremacy": all exact, and all turn on purpose. But the draft's gate passage also quotes the convention's own recorded objection that registrars' discretion "perpetuates the very form of abuse which we are seeking to escape" (l. 253-254; card p. 11), which is an objection to a *position* (discretion held by a designated class), and *Lassiter* (R1-17) shows the courts let the qualification stand while condemning design and administration | For F6 the verdict-bearing property is mixed: purpose in the courts, discretion in the 1901 convention. "Wrong" is too strong; "narrower" (as R1-17 has it: the verdict attaches to the registrars' discretion and the schools) fits the record. For F5 (competence withheld) R4's point stands: the 1831 preambles state purpose. |
| HP3 duty-bearer (contested) | R4 | VERIFIED verbatim | `bec/microsoft2022responsible` p. 9 T1 "Applies to: All AI systems when the intended use…"; draft ll. 527-529 hand A5.4 to "the operator"; ll. 535-540 the deploying organisation | — |
| HP5 two courses exhaustive (wrong) | R4 | VERIFIED paraphrase | Draft ll. 166-172 (Carolingian custody), l. 72 "the print stage and not the scribes'", ll. 60-61, 551 | The draft does assert the dichotomy and does concede custody inside moment 1. Caveat for the lead: R1-05 finds that the Boretius texts carry custody of *corrected text*, not of the page's conventions; if R1-05 is applied, HP5's evidence shrinks to "the correction ran under custody of the text", which still breaks the dichotomy. Apply both together. |
| HP7 silence allocates (narrower) | R4 | VERIFIED verbatim | Capture word counts (Table 2, R2-24); draft l. 50 "leaves her the reading" | — |
| HP8 ex post remedy is not control (contested) | R4 | VERIFIED verbatim | Draft l. 478 "None of these regimes gives the person a voice or a brake before the action"; Lovett §2.2 resilience, §4.2 "courts of appeal" (local SEP) | R2-16 supplies the legal material HP8 needs (art. 22(3) is post-decision; art. 22(1) is a prohibition before). |
| A2 narrower: *Parker*; l. 216 "has no source" | R4 | VERIFIED paraphrase | `parker1877south` p. 423 "under no obligation to read"; draft l. 215-216 "not at the request of those it barred" rests on N2 claim 5's silence (repeal by 1 Edw. VI c. 12, `statutesrealm1819vol4`), not on a text | R4 is right that the negative has no source; the repeal itself has one. |
| A4 narrower: attribution omitted | R4 | VERIFIED verbatim | `microsoft2026responsible` PDF p. 18 (printed pp. 34-35) "attribution indicating AI assistance, ensuring recipients know"; draft l. 139 cites the Cowork approval sentence at "26" = printed p. 26 (PDF p. 14), which is exact | — |
| A7 contested | R4 | VERIFIED verbatim | `hamilton2025digital` p. 10 "create antipower for users"; Lovett §2.2 | Same finding as R3-03. |
| "record" misused (ll. 346-351) | R4 | **OVERSTATED** | Draft ll. 342-346 pair the Purview log and the Unified Audit Logs gap with "a record made and held by one side, which the other side cannot answer and cannot use"; ll. 243-249 quote Israeli p. 47 (the dropped answer) and p. 62 (self-legitimation), the properties R4 says the verdict turned on; l. 403 names "the record of the denial (P15)" as the organisation's | The draft already carries the decision record (l. 403) and the two Israeli properties. The log example is the weaker instance, not a misuse of the concept: "narrower" (pair on the decision record, not Purview). |
| "custody" narrower | R4 | VERIFIED verbatim | `commons1803journal` reason 12 "compelled to buy their Freedom of Trade" (draft l. 223); `cjeu2024publicresource` paras 70, 74-75 | — |
| "brake" misused (ll. 384-390) | R4 | **OVERSTATED** | Draft ll. 385-388: the gate and the licence "gave power over the outcome to a designated class—registrars, bishops, master printers—and none to the person … The insider post's brake has the same shape"; `bec/alabama1901official` p. 11 records a contemporary objection to that class's discretion | A gate decides access and a brake stops a process: a real disanalogy the draft names only by "the same shape", and R4 is right that it must be met. But "No contemporary objected" is not so: the 1901 convention's recorded objection to registrars' discretion is an objection to power over the outcome held by a designated class, which is the property the draft pairs on. "Narrower" (state the gate/brake disanalogy; rest the stop-power on route 2 if it fails) fits. |
| "second party" misused (ll. 392-400) | R4 | VERIFIED verbatim | Draft ll. 50-52 ("Microsoft's own terms state the allocation plainly" for the second party) and ll. 392-398 cite terms addressed to the account holder (`microsoft2026copilot`, `anthropic2025consumer`, `bec/microsoft2026application`) | R2-04 reaches the same finding ("narrower"). The draft does present user-addressed terms as evidence about the second party; "misused" is defensible. |
| "scaffold" misused (ll. 425-427, 503-505) | R4 | **OVERSTATED** for ll. 425-428; VERIFIED paraphrase for ll. 503-505 | Draft l. 426 calls Nadella's phrase "the aim"; the "promise" sentence (ll. 425, 428) rests on Elevate's "20 million people earn an in-demand AI skilling credential" (Smith 2025), which is a promise of competence. `bec/nadella2025looking` reads the 2025 post as "a design-side framing … It gives no design answer". Draft ll. 504-505 does call the phrase "Nadella's promise" | R4 overlooks Smith 2025 at l. 427. The objection passage (ll. 503-505) does make a promise of the phrase; there R4 is right. |
| D02 narrower; D08 unsupported | R4 | VERIFIED paraphrase | Draft l. 19-20 and l. 518 "each with a precedent"; ll. 520-521 and 532-533 name none for D02 and D08 | R5-07 agrees on D02; R5-14 notes the ledger's D08 precedents (Belland, Kulesza) that the draft does not cite. |
| R4's post-quotation check (26 exact) | R4 | VERIFIED verbatim (sample) | P2, P3, P5, P17, P19, P20, P21 fragments checked against the capture | — |

## Table 5. R5, novelty and counter-case

| Item | Run | Status | Evidence | Note |
|---|---|---|---|---|
| R5-01 gap sentence holds | R5 | VERIFIED paraphrase | Gap statements name sources and rows searched; Consensus and Scholar Gateway blocked, as logged | — |
| R5-02 survey "two directions" narrower | R5 | VERIFIED verbatim | `farrell2025large` author's version: "Like pictures, writing, print…", "editors, peer review, and libel laws for print", "concerted and sustained efforts"; Crossref Science 387(6739) 1153-1156, no updates; `arbel2025how` OpenAlex abstract: "reduce by 66.9% the length of contracts", "reduce reading time by 14:41 minutes", "fifth-grade students", "smart readers have arrived" | Farrell quotations are from the author's version; the Science text unseen, as the card says. |
| R5-03 reception "largely descriptive"; Gallot | R5 | VERIFIED verbatim (Gallot); **WRONG** (one Riley quotation) | `gallot2026securing` ¶3, ¶5, ¶14, ¶15 exact. But R5 E2 and the gallot card's Critical notes quote Riley as saying the controls "require verified human approval"; Riley's text reads "Higher-impact actions can be held for verified human approval" | Minor misquotation inside quotation marks; the sense survives. Riley's own card does not carry the phrase. |
| R5-04 "thirteen million" unsupported | R5 | **WRONG** | Capture header: "Captured from the live page in the user's Chrome on 12 Oct 2026. Counts at capture: 13M views; 1.7K replies; 2.4K reposts; 14K likes; 21K bookmarks." `DRAFT_NOTES.md`: "View count ('thirteen million times'): from the capturer's header on the local X capture (12 Oct 2026)". `garg2026nadella`: "Read at 13:05 UTC the next day, it had 8.9 million views" (an earlier reading, consistent) | The figure has a source the brief itself names as the post's source. It has no card, which is what R5 found; the fix is a citation to the capture, not "source or drop". R2-24 had it right. |
| R5-06 smart reader contested | R5 | VERIFIED paraphrase | Arbel abstract as above | Abstract depth, as stated. |
| R5-07 D02 no working precedent | R5 | VERIFIED verbatim | `wright2024null` arXiv p. 1: "18 posted audit reports and 13 posted transparency notices"; "a null result cannot be said to indicate non-compliance, a condition we call 'null compliance'"; p. 2; Crossref FAccT 2024 pp. 1701-1713, no updates | — |
| R5-08 D03 narrower | R5 | VERIFIED verbatim | `liang2024whats` arXiv pp. 1-3 (17.4%, 15.4%, 74.3%); `ho2012fudging` p. 612 "$142 per hour … within thirty days"; Crossref NMI 6(7) 744-753 | — |
| R5-09 D04 narrower | R5 | VERIFIED verbatim | `austin2021data` pp. 255-257 exact; Crossref S&S 19(2) 255-261; `appealscentre2026transparency` pp. 3, 4, 5, 11 exact | — |
| R5-10 D06 check half | R5 | VERIFIED verbatim | `talevski2020teach` pp. 11, 14 exact; Crossref PLoS ONE 15(4) | — |
| R5-11 D06 risk half; AILD withdrawn | R5 | VERIFIED verbatim | `eapil2025european` ¶¶2-3 exact ("published in the Official Journal on 6 October 2025") | The Bird & Bird sentence is from a second file in the same folder, not checked. |
| R5-12 Simon 2005 contested (rank 1) | R5 | VERIFIED verbatim | `ho2019new`: p. 404 (PDF 1) "does not hold up under improvements to the original data and methodology. The largest salmonella outbreak in state history hit Southern California before Los Angeles implemented grading"; p. 405 n. 1 (PDF 2) "A different version of the foodborne illness analysis was also published as Simon et al. (2005). Online Appendix A shows that the same issues identified here affect that analysis."; p. 418; p. 425 "little credible evidence". Crossref AEJ:EP 11(4) 404-428, no updates; Jin–Leslie reply 11(4) 429-443, Crossref abstract "insignificant when compared with the rest of Southern CA" exact. `simon2005impact` card: "was associated with a 13.1 percent decrease". `felt2015improving` p. 2900 Table 5: 30.9% and 58.3%; p. 2893 "nearly 30% more total users" | Holds at the strength stated. Online Appendix A, where the Simon reanalysis is, was not fetched (R5 says so); the main text asserts it. |
| R5-13 D07 narrower | R5 | VERIFIED verbatim | `ho2012fudging` pp. 574, 611, 645; `zhang2022how` pp. 204, 218; Felt as above | — |
| R5-14 D08 evidence contested | R5 | VERIFIED paraphrase | `fernandes2014financial`, `kaiser2022financial` (course cards, not reopened); Bastani blocked | — |
| R5-17 CB "each with a working precedent" narrower | R5 | VERIFIED paraphrase | Draft ll. 19-20, 518; E5-E10 | Agrees with R4 D02/D08. |
| Cards `ho2019new`, `felt2015improving`, `ho2012fudging`, `farrell2025large`, `gallot2026securing`, `garg2026nadella`, `riley2026microsoft`, `above2026satya`, `koo2026insider`, `appealscentre2026transparency`, `austin2021data`, `eapil2025european`, `liang2024whats`, `talevski2020teach`, `wright2024null`, `zhang2022how` | R5 | VERIFIED verbatim | sha256 16 of 16 match; every quotation present at its page (Garg "8.9 million" exact); Crossref 9 of 9 DOIs match, no updates | Except the Riley sentence in `gallot2026securing` (above). |
| Card `arbel2025how` (abstract) | R5 | VERIFIED paraphrase | `local_path: null`, `sha256: null`; Crossref chapter pp. 336-374, 2025-03-31; OpenAlex abstract matches the paraphrase | Compliant abstract card. |

---

## Per-run rates

| Run | Rows audited | VERIFIED (verbatim + paraphrase) | WRONG | OVERSTATED | NEEDS LIBRARY CHECK | Disagree (WRONG + OVERSTATED) |
|---|---|---|---|---|---|---|
| R1 | 25 (18 verdicts, 7 cards) | 22 | 1 (R1-04) | 2 (R1-09, R1-26: one underlying error, the Arundel reading) | 1 (Saenger p. 100, inside R1-04) | **3 of 25 (12%)** |
| R2 | 24 (15 verdicts, 8 cards, R2's own copies) | 23 | 1 (R2-14 locator) | 0 (R2-14's conclusion is also overstated; counted once) | 0 | **1 of 24 (4%)** |
| R3 | 21 (17 verdicts, 4 cards) | 19 | 1 (sparks card, minor) | 1 (R3-02 prescription) | 1 (R3-09 Hussain and Moriarty) | **2 of 21 (10%)** |
| R4 | 16 (logic rows) | 12 | 0 | 4 (HP2; record; brake; scaffold at ll. 425-428) | 0 | **4 of 16 (25%)** |
| R5 | 31 (14 verdicts, 17 cards) | 29 | 2 (R5-04; Riley misquotation, minor) | 0 | 0 | **2 of 31 (6%)** |
| **Total** | **117** | **105** | **5** | **7** | **2** | **12 of 117 (10%)** |

Hashes: 35 of 35 card files match; 4 of 4 R2 copies match. Quotations: no fabricated quotation found; two minor
misquotations (Riley in `gallot2026securing` and R5 E2; the `sparks2022rule` "not captured" sentence). Crossref: 17
DOIs checked, no update or retraction notices. R4's higher rate reflects its task (grading inferences, where the
dispute is over "misused" against "narrower"), not misread sources: every card and draft line R4 cites says what R4
says it says.

Where two runs reached the same item independently they agree on substance and differ on strength: R2-04 and R4
("second party", "reading"): narrower vs misused; R1-16b and R4 ("disclosure"): wrong vs narrower; R1-17 and R4 HP2:
narrower vs wrong; R2-24 and R5-04 (view count): holds vs unsupported; R4 D02/D08 and R5-07/R5-17: agree.

---

## Verdicts the lead must adjudicate, ranked by effect on the argument

1. **R2-16 (A8, §4 fourth objection, §5 duties 1, 3, 4).** Verified at full strength. The GDPR's art. 22(1)
   prohibition, art. 22(3) rights and the CJEU's explanation right (*Dun & Bradstreet* paras 58-59) are in the arm's
   own library (course card, ledger E05) and absent from the draft's account of what the law gives. A8 must be
   restated as R2 proposes (enumerated decisions; post-decision; controller-run; no envelope; not in the
   architecture), and §5 must name art. 22(1) as duty 1's present precedent. This is the largest single change to
   CA's "nothing removes the property" step and to CB's "each with a working precedent".
2. **R1-04 (A2, moment 1; the Saenger quotations).** R1's "unsupported" is wrong at the strength stated: dxd
   AUDIT_01 and AUDIT_06 log Google Books search-inside confirmation of pp. x, 83, 85, 87, which is the clean route
   BRIEF §6 names. The lead should keep the p. 85 and p. x quotations and the pp. 83 and 87 dates, record the two
   audits as their confirmation on the arm's Saenger card, and carry p. 100 as "wording confirmed, page needs a
   library copy". Dropping the quotations would weaken moment 1 for no reason.
3. **R3-02 (A7 route 2; CA for the retail refund case).** The Pettit–Gädeke dispute is real and must be named, as R3
   says. But R3's prescription (confine domination to bank, insurer, employer; concede the one-off customer) reads a
   dependency test into Gädeke, whose test is structural enablement plus persisting status asymmetry. The lead
   decides whether the paper argues that a firm's terms-of-service-backed power over any customer is structurally
   enabled (Gädeke's own test, which the draft's ll. 393-399 already supply material for) or retreats to the
   dependent relations. The worked refund case stands or falls on this choice.
4. **R4 HP2, "brake", "record" against R1-17 (A3, A6 for the gate and record pairings).** R4 grades these "wrong"
   and "misused"; the record supports "narrower". The 1901 convention's objection to registrars' discretion
   (p. 11) is a position-based contemporary objection the draft already quotes, so the gate pairing need not leave
   Argument A; the gate/brake disanalogy (access vs stopping a process) must still be met. The record pairing should
   be carried on the decision record (draft l. 403), not the Purview log. The lead should take R1-17's and R2's
   "narrower" over R4's labels while keeping R4's demand that the disanalogies be argued.
5. **R2-14 (A4 notice; §3.4; the worked case).** R2's dates are right and its locator is wrong: art. 73 is in
   Chapter IX, applies from 2 August 2026, and is deferred only derivatively (no system is classified high-risk
   under art. 6 before December 2027). The lead decides the tense: the draft's "requires" is the article's present
   tense; R2's "will require from Dec 2027" misstates the law in the other direction. The Annex III point (a refund
   agent is outside it) holds and is the stronger fix.
6. **R5-12 / R5 rank 1 (B1, D07; ADJUDICATION §6 A2 row).** Verified: Ho et al. 2019 n. 1 says Simon 2005 has
   "the same issues"; Jin and Leslie's reply contests it. The grade-card figure becomes "contested on replication";
   D07's working precedent moves to Felt et al. 2015 (30.9% to 58.3%, p. 2900) with R5's independence condition.
   The ADJUDICATION's A2 disclosure row ("associated with a 13.1% fall") needs the replication caveat added.
7. **R1-09 / R1-26 (A2, the "print stage" label).** Arundel 1409 licensed translations and barred reading of
   unlicensed ones; it did not license readers by rank. The claim "licensed reading predates print" holds for what
   may be read and not for who may read, so the draft's "statutes that licensed who could read" keeps its one
   instance (1543) and the periodization critique rests on Johns and Parkes alone. The lead decides whether "print
   stage" survives as England's press regime 1557-1695 (R1's fallback) on that thinner basis.
8. **R4 HP5 with R1-05 (CA's dichotomy; moment 1's custody).** Apply together: R1-05 narrows the Carolingian claim
   to custody of corrected text; HP5's point that the two courses are not exclusive survives on that narrower
   custody. The lead should restate CA by beneficiary (R4's fix) and the Carolingian sentence by text, not page
   conventions (R1-05's fix).
9. **R3-05 (A7 route 2; CB's authority).** Verified at full strength. Lazar's published rejection of the republican
   frame (Lecture I p. 20 n. 80; 2024 n. 27) and his legitimacy-authority frame must be met or adopted; his "who"
   question bears on whether designer-adopted duties can carry authority (R3-09's tension).
10. **R4 "second party" and R2-04 (A4 "responsibility placed on the user").** Two runs agree: the Copilot, Anthropic
    and application-card terms bind the account holder, not the person acted on. Relabel ll. 50-52 and 392-400 as
    the user's burden; the second-party evidence is *Moffatt* and the documents' silence.
11. **R5-04 (opening, l. 27).** Keep "thirteen million"; cite the capture header (12 Oct 2026), as DRAFT_NOTES
    already does. No card is needed for a count read off the post's own page.
12. **R4 "scaffold" (ll. 425-428 vs 503-505).** Keep Elevate (Smith 2025) as the promise of competence at l. 427;
    at ll. 503-505 stop calling Nadella's "scaffolding for human potential" a promise.
13. **Minor corrections to cards and review text.** `gallot2026securing` Critical notes and R5 E2: Riley wrote "can
    be held for verified human approval", not "require verified human approval". `sparks2022rule`: the third
    reason is on Hamilton p. 6 (biases of "mood, hunger, pride"); add MPP 9(2) 201-218 to `venue`. R3-09: do not
    carry the Hussain and Moriarty characterisation until the paper is read. R2 and R4 should say the capture holds
    21 essay paragraphs plus a capturer's end marker ("[P22] (end of post)").

# R4 — Copyeditor and citation checker

**Manuscript:** `manuscript/REVISION_2026-10-09.md` (read whole; 362 lines). **Figure:** `manuscript/figures/figure1_algorithmacy_cycle.svg`.
**Seat:** mechanical correctness and consistency only. I do not judge the argument.
**Date:** 2026-10-09.

## Summary counts

| Check | Count |
| --- | --- |
| Reference entries | 104 |
| Cited works resolved text → list and list → text | 104 / 104 (no orphans either way) |
| Entries with a DOI checked against Crossref | 94 (all 94 returned a record) |
| Entries checked via DataCite / doi.org redirect | 1 (Stark & Pais) |
| Entries without a DOI | 9 (Goffman, Katsh & Rifkin, Olson, Powell, Reeves & Nass, Selznick, Simmel 1950, Thompson 1995, Yates) |
| Reference-list mismatches against records (verified) | 4 (Christin page form; Korczynski missing pages; Suchman year; Rahman & Valentine punctuation) + 1 note (Stark & Pais year 2020 vs DataCite 2021) |
| Direct quotations checked | 40 |
| — verbatim | 38 |
| — not verbatim | 2 (Elish "responsibility"; Stark & Vanden Broeck p. 5 wording) |
| — page wrong | 3 (Stark & Vanden Broeck p. 5 → p. 1; Simmel block quote pp. 172–173 → p. 172; Orlikowski & Scott 2023 p. 9 → p. 8) |
| — page uncheckable | 2 (Zhou et al. p. 8 and p. 2, working-paper pagination) |
| Body words (excl. the two AUTHOR flags) | 6,759 |
| Abstract words | 256 (limit 300) |
| Keywords | 7 (limit 3–10) |
| References words | 2,559 |
| Total title + abstract + keywords + body + references | 9,645 (9,598 without the AUTHOR flags); limit 11,000 |

## 1. Citation resolution (both directions)

Method: I extracted every author–year string from lines 3–151 with grep, then matched each by eye against the 104 entries on lines 155–361, and the reverse.

**Text → list.** Every in-text citation has an entry. 104 distinct works are cited; several many times (Rahman 2021 ×8, Stark & Vanden Broeck 2024 ×5, Hinds & von Krogh 2024 ×4, Curchod et al. 2020 ×4).

**List → text.** Every one of the 104 entries is cited at least once.

**Author/year agreement.** All names and years agree with the list, including Pälli (ä), Möhlmann (ö), Gagrčin (č), "von Krogh", "Vanden Broeck", "Oeldorf-Hirsch".

**APA 7 form of in-text citations.**

- `Zhou, Lei, Liu, et al., 2025` (line 57) and `Zhou, Lei, Liu, et al. (2025)` (line 129). APA 7 uses "et al." after the first author for three or more authors unless two works would otherwise be abbreviated to the same form. There is no other Zhou (2025) in the list, so the form should be **"Zhou et al., 2025"** / **"Zhou et al. (2025)"**. Verified against the list (one Zhou entry only).
- `Simmel (1902a, 1902b, 1950)` ✓; `1902a` = Part I, `1902b` = Part II; both quoted passages come from Part II and are cited 1902b ✓.
- `Walther (1992, 1996)`, `Thompson's (1995, 2020)`, `Orlikowski and Scott (2008, 2023)` ✓ chronological.
- Alphabetical order inside every multi-work parenthesis checked ✓ (e.g., line 13 "Cameron, 2024; Kellogg et al., 2020; Rahman, 2021; Stark & Vanden Broeck, 2024; Vallas & Schor, 2020"; line 19 "Fuller & Smith, 1991; Havard et al., 2009; Korczynski, 2013; Lopez, 2010"; line 99 "Bucher, 2017; Cotter, 2019; DeVito et al., 2018"; line 129 "Espeland & Sauder, 2007; Rahman, 2021").
- `Rahman, H. A.` (two entries) vs `Rahman, H.` in Cameron & Rahman (2022): each matches its own Crossref record (Cameron & Rahman is registered as "Rahman, Hatim"). APA permits this; no change required.
- Quoted terms without a page: "gig literacies" (line 17), *tertius gaudens* (line 33), "algorithmic labor triangle" has a page ✓, "artificial certainty" (line 121) has none. APA 7 asks for a page with any direct quotation, including short terms; add p. 457 (abstract) for "gig literacies" and p. 174 for *tertius gaudens* if the editor insists; "artificial certainty" is in the article title.

**Reference-list ordering** (APA 7): checked every adjacent pair. Single-author entries precede multi-author with the same first author (Cameron 2022, 2024, then Cameron & Rahman; DeVito 2021 before DeVito et al. 2018; Hargittai 2002 before Hargittai et al. 2020; Rahman before Rahman & Valentine); Bucher, E. L. before Bucher, T.; Stark & Pais before Stark & Vanden Broeck; Sundar & Kim before Sundar & Nass; Schoeneborn → Scott & Orlikowski → Selznick; Meng → Möhlmann (ö sorted as o). All correct.

## 2. Reference metadata

Method: for each DOI I fetched `https://api.crossref.org/works/<url-encoded DOI>` with curl (no mailto parameter, 1.2–3 s pauses, 21 retried after connection drops), extracted author, year, title, container, volume, issue, pages/article number with jq, and compared each field by eye with the entry. Stark & Pais (DataCite) was checked through the `https://doi.org/` redirect and the landing page at sociologica.unibo.it. Non-DOI entries were checked as stated below.

### 2a. Verified mismatches (correct these)

| # | Entry | Manuscript | Record | Correction |
| --- | --- | --- | --- | --- |
| 1 | Christin (2017), *Big Data & Society* | `4(2), 1–14` | Crossref `page` = 2053951717718855 (article number); no page range | **`4(2), Article 2053951717718855`** — same form as the Chan, Faraj & Pachidi, Glaser, Hong and Organization Theory entries |
| 2 | Korczynski (2013), *WES* | `27(6).` — no pages or article number | Crossref gives 27(6) and no pages; Semantic Scholar gives pages **NP1–NP7** (e-special-issue introduction) | **`27(6), NP1–NP7`** — confirm on the Sage page (403 to my fetch) |
| 3 | Rahman & Valentine (2021) title | `…Platform-Mediated "gigs".` | Crossref title ends `“Gigs”` | US punctuation: **`"gigs."`** (period inside the closing quote). Also note the record capitalises "Gigs"; sentence case keeps it lowercase, so only the period moves |
| 4 | Suchman (2007) | year 2007 | Crossref: print 2006, online 2012 (monograph, CUP) | **Discrepancy to resolve.** The 2nd edition is widely cited as 2007 (copyright page) and Crossref registers 2006. I could not open the copyright page; the author should check the physical/PDF book and use its copyright year |
| 5 | Stark & Pais (2020) | 2020 | DataCite `publicationYear` 2021; landing page: Vol. 14 No. 3 **(2020)**, "Published 2021-01-29", pp. 47–72 | **Keep 2020** (issue year; Stark & Vanden Broeck also cite it as 2020). No change, but be ready for a query |

### 2b. Internal inconsistency in the list (not a record mismatch)

- *Proceedings of the ACM on Human-Computer Interaction* entries use two forms: DeVito (2021) `5(CSCW2), Article 339` (confirmed: the PDF running head reads "Vol. 5, No. CSCW2, Article 339") versus Jiang & Sinchaisri (2025) `9(7), 1–35` and Yao et al. (2021) `5(CSCW2), 1–29` (both as Crossref gives them). Pick one form. APA 7 prefers the article number for PACM HCI; the ACM DL page gives it (not in Crossref), so it must be looked up for Jiang & Sinchaisri and Yao.
- Publisher names: "Sage" (Jablin & Sias) vs "SAGE Publications" in all Crossref records; "Springer" (Jarrahi & Sutherland) vs "Springer International Publishing". APA 7 accepts either; keep consistent within the list.
- Lee et al. (2015), Lopez (2010), Sundar & Kim (2019), Walther (1992, 1996): Crossref holds only the main title; the subtitles in the manuscript are not contradicted and match the ACM/Sage pages as commonly cited; not verified field-for-field.

### 2c. Entries that match their record on every field checked (89)

Alaimo & Kallinikos; Anthony et al.; Bailey et al.; Bellesia et al.; Bolton et al.; Bucher et al. 2021 (title's spaced en dash is as published); Bucher 2017; Cameron 2022; Cameron 2024; Cameron & Rahman; Chan; Clark & Brennan (pages 127–149; editors Resnick, Levine, Teasley confirmed from the chapter's own reference line in the Stanford copy found by search, not from Crossref, which lists no editors); Cooren; Cotter; Curchod et al.; Daft & Lengel; DeVito 2021 (1–38 in Crossref; Article 339 in the PDF); DeVito et al. 2018; Elish; Espeland & Sauder; Faraj & Pachidi; Fradkin et al.; Fuller & Smith; Gagrčin et al. (2026, 28(1), 423–447); Gibbs et al. (Crossref gives "Jennifer Gibbs", "Gavin Kirkwood" without the middle initials L./L.; the initials are not contradicted, just not in the record); Glaser et al.; Guzman & Lewis (title "Human–Machine" with en dash ✓); Hancock et al.; Hargittai 2002 (no pages in record; First Monday is unpaginated ✓); Hargittai et al. 2020; Havard et al.; Heiland (2025, 40(1), 1–19); Hinds & von Krogh (record "Hinds, Pamela" → "Hinds, P." ✓; the Bailey record has "Pamela J." → "P. J." ✓); Hohenstein & Jung (Article 106190 ✓); Hong et al. (2026, 13(2), Article 20539517261449362); Jablin & Sias (pp. 819–864 ✓; editors not in record; Sage page blocked, so Jablin & Putnam as editors is unverified here); Jarrahi & Sutherland (pp. 578–589 ✓; LNCS vol. 11420 and the four editors are not in the Crossref record — unverified); Jiang & Sinchaisri; Karunakaran et al.; Kellogg et al.; Kornberger et al.; Krakowski et al.; Kuhn (29(8–9)); Lebovitz et al.; Lee et al.; Lehtinen & Pälli; Leonardi & Leavell (37(2), 516–543); Lin et al. (101(3), 413–440); Litt; Long & Magerko; Lopez; Lu & Yan (Crossref: online 2026, no volume/issue → "Advance online publication" ✓); Meng (28(3), 1171–1189); Möhlmann et al.; Nass & Moon; Newlands; Obstfeld et al. (pp. 135–159 ✓; RSO vol. 40 ✓ on Emerald page; the five editors are not shown on the Emerald page — unverified); Oeldorf-Hirsch & Neubaum; Okhuysen & Bechky; Ong; Orlikowski & Scott 2008, 2014, 2023; Puranam et al.; Pyyhtinen (Crossref title "The Simmelian Legacy", publisher "Macmillan Education UK"; a library catalogue gives subtitle "A science of relations" and "Palgrave: London" — "Palgrave Macmillan" is acceptable); Rahman; Raisch & Krakowski; Sandberg; Schoeneborn et al. (7(3)); Scott & Orlikowski; Simmel 1902a (8(1), 1–46) and 1902b (8(2), 158–196); Spitzberg; Stark & Vanden Broeck; Stelmaszak et al. (63(2), 335–365); Suddaby (record lists Suddaby as editor, no author — consistent with "Editor's comments"); Sundar & Kim; Sundar & Nass; Sutherland et al.; Thompson 2020; Tong et al.; Vallas & Schor; Viduchinsky (pp. 1–13 ✓); Waardenburg et al.; Walther 1992, 1996; Weick et al.; Wilkinson (17(4), 11–15, 1965 ✓); Yao et al.; Zhou et al. (63(2), Article e70004 ✓).

### 2d. Non-DOI entries

| Entry | What I could confirm | How |
| --- | --- | --- |
| Powell (1990) | *RiOB* 12, 295–336, JAI Press 1990 | Local text `library/pdfs/powell1990.txt`, first page |
| Selznick (1949) | Title, subtitle, University of California Press (Publications in Culture and Society vol. III) | Local scan `library/pdfs/selznick1949.txt` |
| Katsh & Rifkin (2001) | Title, Jossey-Bass, 2001 | Wiley publisher page and library records (search) |
| Clark & Brennan (1991) | See 2c | — |
| Goffman (1981), Olson (1994), Reeves & Nass (1996), Simmel (1950), Thompson (1995), Yates (1989) | Not checked against an external record this session; publisher and year are the standard ones and nothing I saw contradicts them | — |

### 2e. APA 7 form, list-wide

Sentence-case titles ✓ throughout (proper nouns and first word after a colon capitalised ✓). Journal names and volumes in italics ✓ (`*Journal, 42*(9)` pattern). En dashes in all page ranges ✓ (grep found no hyphen-minus between digits outside DOIs). "Article" used for e-locators ✓ except Christin (see 2a). Chapters carry editors, book title and pages ✓. Edition noted for Suchman ✓. Translator/editor noted for Simmel 1950 ✓. DOIs as `https://doi.org/` links ✓. No "Retrieved from". No issue number for Elish (volume-only journal) ✓ and Gibbs (volume-only) ✓.

## 3. Quotations and page numbers

Method: `pdftotext` (reading order) on the local publisher PDFs; library `.txt` files; Simmel Part II downloaded from archive.org (`jstor-2761932/2761932.pdf`, 40 pp., pdf page 2 = printed 158); Jarrahi & Sutherland from the publicly hosted ResearchGate deposit (metadataetc.org); Crossref/OpenAlex/Semantic Scholar abstracts where no full text was reachable. Printed page numbers were read from the running heads, not inferred.

| # | Quotation (manuscript line) | Verbatim | Page | Source used |
| --- | --- | --- | --- | --- |
| 1 | Guzman & Lewis "communicative subjects, instead of mere interactive objects" (15) | yes | p. 71 ✓ | `guzmanlewis2020.pdf` p. 71 |
| 2 | Hancock et al. "operates on behalf of a communicator" (15) | yes | p. 90 ✓ (also in abstract p. 89) | `hancock2020_vor.pdf` |
| 3 | Sutherland et al. "gig literacies" (17) | yes (term) | no page given; abstract p. 457 | `sutherland2020.pdf` |
| 4 | Jarrahi & Sutherland definition of algorithmic competency (17) | yes | **deposited copy p. 9 ✓** (running head "9"); LNCS page not checked — the deposit has 12 numbered pages against LNCS 578–589, so a one-to-one mapping would give p. 586, but typeset line breaks differ; leave the flag until someone opens the Springer PDF | metadataetc.org deposit |
| 5 | Cameron "algorithmic labor triangle" (19) | yes (Figure 1 title, p. 466; also p. 467 table) | p. 466 ✓ | `cameron2024.txt` |
| 6 | Chan "trilateral relationship" (19) | yes — in the abstract | p. 1 ✓ (abstract = first page) | Crossref abstract |
| 7 | Stark & Vanden Broeck "whereas actors in hierarchies command … on platforms they are co-opted" (19) | **p. 1 wording, not p. 5 wording.** p. 1 (abstract): "Whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted." p. 5: "whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are coopted (Stark & Pais, 2020)" | **p. 5 → p. 1**, or keep p. 5 and write "coopted" | `starkvandenbroeck2024.pdf` |
| 8 | Stelmaszak et al. "not merely a human trait or skill" (19) | yes | p. 346 ✓ | `stelmaszak2026.pdf` |
| 9 | Simmel "seeks to eliminate himself" (29) | yes | p. 167 ✓ | archive.org Part II |
| 10 | Simmel "as a means to the ends of the group" (29) | yes | p. 174 ✓ | same |
| 11 | Simmel block quote "So long as the third party works as a real mediator … out of their own hands." (31) | yes | **pp. 172–173 → p. 172** (the whole passage is on p. 172) | same |
| 12 | Simmel "the voluntary appeal to an arbitrator … than any other form of decision" (35) | yes (OCR breaks "form of deci-sion" across the page turn) | pp. 172–173 ✓ | same |
| 13 | Simmel *tertius gaudens* (33) | yes | p. 174 (no page given) | same |
| 14 | Stark & Vanden Broeck "The platform benefits from her agency without her acting as its agent" (35) | yes | p. 14 ✓ | `starkvandenbroeck2024.pdf` |
| 15 | Cooren "can be said to be performing something" (49) | yes — in the abstract | p. 373 ✓ (first page) | Crossref abstract |
| 16 | Lehtinen & Pälli "presenting demands for the participants" (49) | yes — in the abstract | p. 47 ✓ (first page) | Crossref abstract |
| 17 | Hinds & von Krogh "may ultimately obscure managers' and employees' visibility into the basis on which the AI is making decisions" (57) | yes | p. 4 ✓ | `hindsvonkrogh2024.pdf` |
| 18 | Hinds & von Krogh "rather than being fixed" / "likely to evolve and expand as the AI learns" (57) | yes | p. 4 ✓ | same |
| 19 | Zhou et al. item "use platform APP functions (i.e., reporting exceptions and appealing)" (57) | yes (full item: "I can use platform APP functions (i.e., reporting exceptions and appealing) to resolve vulnerabilities in AM.") | **uncheckable** — found on working-paper pdf p. 28 (table); the published APJHR article's p. 8 was not available | `zhou2025apjhr_workingpaper.pdf` |
| 20 | Bailey et al. "by design, always changing and adapting" (57) | yes — in the abstract | p. 1 ✓ | Crossref abstract |
| 21 | Schoeneborn et al. "rather strategically downplay their collective actorhood status to avoid accountability" (59) | yes | p. 13 ✓ | `schoeneborn2026.pdf` |
| 22 | Stark & Vanden Broeck "distributed, deflected, and denied" (59) | yes | p. 14 ✓ | `starkvandenbroeck2024.pdf` |
| 23 | Selznick "absorbing new elements into the leadership or policy-determining structure of an organization" (59) | yes (fragment of "cooptation is the process of absorbing … as a means of averting threats to its stability or existence") | p. 13 ✓ | `selznick1949.txt` (running head "Selznick: TVA and the Grass Roots 13") |
| 24 | Selznick "the responsibility for power rather than power itself" (59) | yes ("what is shared is the responsibility for power rather than power itself") | p. 14 ✓ | same |
| 25 | Weick et al. "involves turning circumstances into a situation that is comprehended explicitly in words and that serves as a springboard into action" (71) | yes — in the abstract | p. 409 ✓ | Crossref abstract |
| 26 | Okhuysen & Bechky "the process of interaction that integrates a collective set of interdependent tasks" (73) | yes (abstract, first sentence) | p. 463 ✓ | `okhuysen2009.txt` |
| 27 | Viduchinsky "dual-audience dilemma" (93) | yes — in the abstract | p. 1 ✓ | OpenAlex abstract |
| 28 | Meng "algorithmic adaptability" (99) | yes — in the abstract | p. 1171 ✓ | Crossref abstract |
| 29 | Orlikowski & Scott 2023 "aggregated into rankings via the platforms' proprietary algorithms" (117) | yes | p. 3 ✓ | `orlikowskiscott2023.pdf` (running head "Orlikowski and Scott 3") |
| 30 | Orlikowski & Scott 2023 "may or may not have experienced" … "in person" (117) | yes ("which they may or may not have experienced in person") | **p. 9 → p. 8** (running head "8 Organization Theory") | same |
| 31 | Hinds & von Krogh "an illustration as well as a thought experiment" (119) | yes | p. 6 ✓ | `hindsvonkrogh2024.pdf` |
| 32 | Hinds & von Krogh "may cascade" / "managers, GenAI, and employees" (119) | yes (source: "may cascade between managers, GenAI, and employees"; the manuscript's "among" is outside the quotes ✓) | p. 4 ✓ | same |
| 33 | Hinds & von Krogh "the process for getting there is opaque" (119) | yes | p. 6 ✓ | same |
| 34 | Leonardi & Leavell "just one tool of many" (121) | yes (Mountain planner quotation) | p. 526 ✓ | `leonardileavell2026.pdf` (pdf p. 2 = 516) |
| 35 | Leonardi & Leavell "17 mentions of unique lawsuits" (121) | yes ("Our investigation revealed 17 mentions of unique lawsuits that had been filed against OceanPlan") | p. 537 ✓; "none" at Mountain ✓ ("all informants agreed that there had been none") | same |
| 36 | Leonardi & Leavell "not an inherent property of AI tools but emerges from the ways in which process experts position and deploy them" (121) | yes | p. 538 ✓ | same |
| 37 | Zhou et al. definition "understanding of platform algorithms that assign and evaluate their work and their ability to adapt to and navigate those algorithms" (129) | yes | **uncheckable** — working-paper pdf p. 5; published p. 2 not verified | working paper |
| 38 | Faraj & Pachidi "against viewing technology as an entity that is separate, exogenous, or causal" (135) | yes — in the abstract | p. 1 ✓ | Crossref abstract |
| 39 | Newlands "the observer and decision-maker can be a non-human agent" (135) | yes — in the abstract | p. 719 ✓ | Crossref abstract |
| 40 | Elish "bears the brunt of the moral and legal responsibility" (137) | **no** — source: "bears the brunt of the moral and legal **responsibilities** when the overall system malfunctions" (abstract p. 40, repeated p. 41) | p. 40 ✓ | `elish2019.txt` |
| 41 | Krakowski et al. "unrelated, or even negatively related, to traditional capabilities" (147) | yes — in the abstract | p. 1425 ✓ | Crossref abstract |

Abstract-sourced quotations (6, 15, 16, 20, 25, 27, 28, 38, 39, 41) are all verbatim in the abstract and cite the first page, which is where the abstract sits. Say so if an editor asks.

### 3b. Paraphrased claims and numbers checked against sources

| Claim (line) | Result | Source |
| --- | --- | --- |
| Jiang & Sinchaisri: learning curve, "more than a million orders", one delivery platform (107) | ✓ ("more than a million orders … on a retail delivery platform"; "a clear learning curve") | Crossref abstract |
| DeVito: "25 LGBTQ+ users of one platform" (99) | ✓ (25 participants completed; Facebook-based ARC; LGBTQ+) | `devito2021.txt` pp. 2, 7–8 |
| Leonardi & Leavell: 83% vs 9% absolute statements; "figures at p. 535" (121) | ✓ Table on p. 535: Ocean 83% absolute (N = 132); Mountain 9% absolute (N = 87) | PDF |
| Bolton et al.: return-rating expectation distorts reports (73) | ✓ | Crossref abstract |
| Fradkin et al.: hiding reviews until both submitted reduced retaliation and reciprocation, lowered ratings; Airbnb (73, 115) | ✓ | Crossref abstract |
| Rahman: criteria could not be seen; experimented vs cut back; dependence and setbacks (57, 101, 107) | ✓ | `rahman2021.txt` abstract, p. 13 |
| Rahman: workers unsure whether platform or client stands behind an evaluation (17) | not located in the passages I searched; not contradicted | — |
| Hohenstein & Jung: smart replies raised trust; blame moved to the AI when things went awry (89) | ✓ | Semantic Scholar abstract |
| Sundar & Nass: same content rated differently by told source (89) | ✓ | OpenAlex abstract (local PDF has no text layer) |
| Sundar & Kim: credit-card number, machine vs human agent (89) | ✓ | `sundar2019.pdf` pp. 1, 3–4 |
| Heiland: false theories because of opacity (89) | ✓ | Crossref abstract |
| Lin et al.: less willing when algorithm advised a low rating (119) | ✓; **but** "more willing when they could adjust it" compresses the finding: use rose when managers could adjust *how the algorithm computes* the rating, compared with adjusting the rating itself or no adjustment | Crossref abstract |
| Tong et al.: disclosure effect weaker with longer tenure (119) | ✓ | Crossref abstract |
| Waardenburg et al.: police intelligence officers brokered an opaque model; ended by substituting their own judgment (141) | ✓ | Crossref abstract |
| Christin: adopted on paper, worked around in practice (141) | ✓ ("decoupling", "buffering") | `christin2017.txt` |
| Curchod et al.: rebuilding reputation elsewhere too costly (59) | ✓ ("if they were able to quit eBay for another platform, they would have to rebuild their reputation") | `curchod2020.txt` |
| Bucher et al.: workers "curtailed what they said to clients" (95) | **imprecise** — source: "curtailing their outreach to clients" (forgoing proposals/opportunities) and separately "keeping emotions in check"; not what they *said* | `bucher2021.txt` abstract, pp. 12–13 |
| Rahman & Valentine: "repair misaligned expectations through a platform's tools" (131) | partly — repair "surface[s] misaligned interpretations"; the abstract says repair succeeded when managers *refrained* from using the tools coercively, so "through a platform's tools" is at best loose. Author to decide (outside my seat) | Crossref abstract |
| Lee et al. and Yao et al.: forums pass on experiential knowledge; fail where sharing loses an advantage (107) | ✓ Yao (reluctance to share strategic information); Lee: forums used for social sense-making ✓; "where only the platform had the answer" not verified | abstracts, `lee2015.txt` |
| Sutherland et al.: building relationships with clients among gig literacies (17) | ✓ ("Building relationships", p. 468) | `sutherland2020.pdf` |
| Jarrahi & Sutherland: "Their figure has two nodes, the worker and the algorithm" (17) | consistent with Fig. 1 caption "The mutual shaping of gig workers and platform algorithms"; I read the text, not the drawing | deposit p. 9 |
| Suddaby: a single clear exception counts heavily (63) | ✓ ("Finding a single exception is often fatal to a construct", p. 349) | `suddaby2010.pdf` |
| Thompson 2020: four interaction types incl. mediated online interaction (41) | ✓ | Crossref abstract |
| Hargittai 2002: experience predicts online skill (129) | ✓ | OpenAlex abstract |
| Gagrčin et al.: frames literature as experiential learning (129) | ✓ | Crossref abstract |
| Katsh & Rifkin: technology as "fourth party" (55) | ✓ per publisher description and Berkman Center note (secondary) | search |
| Powell 1990 pages (41) | ✓ 295–336 | local text |
| Wilkinson coined "oracy" in 1965 (45, 47) | article is 1965 ✓; "coined … by analogy with the older 'literacy'" not checked (no text) | Crossref |
| Yates: American firms "between about 1850 and 1920" (47) | uncheckable here (no local text) | — |
| Pyyhtinen asked what becomes of the triad when the third is not human (37); Obstfeld et al. "conduit" (45); Long & Magerko competency on the human role (129); Orlikowski & Scott 2014 two valuation schemes (99); Daft & Lengel uncertainty/equivocality (71); Sandberg (67, scanned PDF without text) | uncheckable this session (no reachable text beyond title/abstract); nothing seen contradicts them | — |

## 4. Numbers and internal consistency

**Numbers.** 83% / 9% / 17 / 25 / "more than a million" / p. 535 / p. 537 — all verified above. "1965" ✓. "1850–1920" uncheckable. **"three decades ago" (line 19)**: the earliest cited work is Fuller & Smith (1991), 35 years before 2026; Havard (2009), Lopez (2010), Korczynski (2013) are later. "More than three decades ago" is accurate; "three decades ago" is loose.

**Counts in the prose.** "four further features" → four listed (hidden; unanswerable; changes without notice; takes dealings as evidence) ✓. "three parts" ✓. "three courses" → three listed ✓. "two of the three have names" → Viduchinsky, Meng ✓. "three points" (Simmel) ✓. "three positions" ✓. "two questions" ✓. "three integrating conditions" ✓. "limited in three ways" (line 23): the paragraph gives no-data, parts-not-new, then the search sentence, then "Finally, triads … older than software" — three limitations plus a novelty sentence between the second and third; readable, but the search sentence interrupts the count.

**The four features, listed the same way?**

| Place | Wording |
| --- | --- |
| Abstract (7) | "hidden, cannot be questioned, changes without notice, and takes their dealings with each other as its evidence" |
| Section "What Sets…" (57) | *hidden*; *unanswerable*; *changes without notice*; *takes the two people's dealings with each other as its evidence* |
| Definition (67) | "hidden, unanswerable, and changing, and that takes their dealings with each other as its evidence" |
| Table 1 | Interpreting ← "hidden and unanswerable"; Specifying intent ← "takes the two people's dealings as evidence"; Keeping track ← "changes without notice" |
| Figure 1 | Intermediary box: "hidden, unanswerable, and changing"; the fourth feature appears as the dashed-arrow label "taken as evidence" |
| Conclusion (149) | "hidden, unanswerable, changing, and fed by the two people's own dealings" |

Consistent in substance. Two wrinkles for the author:

- Line 73 says "Each feature of the intermediary undoes one [condition]" (four features, three conditions), and line 75 says "The hidden rule is a condition of all three parts and does not distinguish among them" — but Table 1 lists "hidden" under Interpreting only. Either drop "hidden" from the Interpreting row (leaving "unanswerable") or reword line 75.
- Figure 1's cycle arrow for "2 Specifying intent" runs Participant → Counterpart only, while its label and the prose say the act is addressed to two readers at once (counterpart *and* intermediary). The dashed "taken as evidence" arrow carries the second reader implicitly; a reader may not see that.

**Terms.** *participant / counterpart / intermediary* introduced at line 37 and used consistently after it; "the other person" (line 63) and "the two people" are ordinary prose, not stray terms. **One naming slip:** line 137 "interpreting, addressing, and keeping track" — the second part is called "specifying intent" everywhere else (Table 1, Figure 1, headings, lines 75, 93, 105, 131). Correct to "interpreting, specifying intent, and keeping track". "Co-optation" (hyphenated, following Stark & Vanden Broeck) is used consistently; Selznick spells it "cooptation" — not an error, since the manuscript does not quote the word.

**Table 1 vs prose.** Rows, features, conditions and failure modes match lines 73–75 and 109 ✓. **Figure 1 vs prose.** Part names, numbering 1–3, the three "helps recover …" lines and the caption match Table 1 and line 151 ✓ (SVG `<title>` = caption).

**Headings.** H1 title; H2 for sections; H3 for subsections — three levels, unnumbered ✓. Title Case used consistently at every level ✓ ("What Sets the Algorithmic Third Apart", "How the Parts Fit Together", "Three Courses for Organizations"). "## Abstract" as a heading is fine for the manuscript file; SAGE will restyle.

## 5. Journal form

**Word counts** (`wc -w` on the markdown; markdown markup, citation parentheses and DOIs each count as words, so Word will report slightly fewer):

| Part | Lines | Words |
| --- | --- | --- |
| Title | 3 | 12 |
| Abstract | 7 | 256 (≤ 300 ✓) |
| Keywords line | 9 | 7 keywords (3–10 ✓): algorithmacy, algorithmic management, coordination, literacy, platforms, Simmel, triad |
| Body incl. headings, Table 1 (117 words), figure caption | 11–151 | 6,805 with the two AUTHOR flags; **6,759** without |
| References (104 entries) | 155–361 | 2,559 |
| **Total** title + abstract + keywords + body + references | 3–361 | **9,645** (9,598 without flags) — about 1,400 under the 11,000 limit including references |
| HTML comment (line 1) | 1 | 76 (must go) |

**Anonymity.** No author name, affiliation, acknowledgement or self-citation appears. Three things break it or betray the process and must be removed before submission:

1. Line 1, the HTML comment: names Claude, the source file `sbs_schoeneborn2026/ASSEMBLED.md`, the review file, and the changelog.
2. Line 17, `[AUTHOR: page 9 is the page in the authors' deposited copy; check it against the LNCS pagination, 578–589]` — resolve (see quotation 4: deposited p. 9 confirmed; LNCS page still open).
3. Line 23, `[AUTHOR: this sentence reports the lab's search of 9 October 2026; confirm it, and decide how to disclose your own earlier online use of the term without breaking anonymity.]` — resolve; the flag itself refers to "the lab" and to the author's prior online use.
4. Line 151, the figure caption ends with `[See \`figures/figure1_algorithmacy_cycle.svg\`.]` — a file-path note with backticks; remove, and put a callout ("[Figure 1 about here]" or the figure itself) at the first mention (line 75, "Figure 1 shows the parts as a cycle"), since the caption now sits after the conclusion.

Those are the only bracketed flags and the only HTML comment in the file (grep for `[AUTHOR:` and `<!--`).

**Figure submission-readiness.** The SVG is clean vector art (980 × 560 user units, Helvetica/Arial, no raster, no external references; the text is real text so it can be edited). SAGE/Organization Theory asks for figures as separate files in TIFF, EPS or PDF; raster art at 300 dpi minimum (line art is commonly asked at higher). Needed: (a) export the SVG to PDF or EPS (vector, resolution-independent) with fonts embedded or converted to outlines, or to TIFF at ≥ 300 dpi at the intended printed width (for a 170 mm two-column figure that is ≥ 2,008 px wide; the SVG's nominal 980 px is far short, so render at scale, do not just rasterise 1:1); (b) check the grey 12-px labels (#666/#888 on white) survive reduction to single-column width — they are the smallest and lightest text in the figure; (c) supply the caption in the text, not in the file (the SVG `<title>` is harmless); (d) the figure is greyscale-safe ✓.

## 6. Typos, grammar, punctuation, spelling

Scans run: British spellings (none in the body; "labour" occurs only inside the Bellesia title, as published), double spaces (none), hyphen-minus page ranges (none), "et al" without a period (none), repeated words (none found by eye on a full read). Quotation marks are straight ASCII throughout the body (consistent; the typesetter will curl them). US spelling consistent (behavior, organization, judgment, labor).

| Line | Issue | Correction |
| --- | --- | --- |
| 19 | "three decades ago" with a 1991 source | "more than three decades ago" |
| 19 | Stark & Vanden Broeck quotation cited p. 5 but worded as on p. 1 | "(p. 1)" — or lowercase "whereas" and "coopted" with p. 5 |
| 31 | "(Simmel, 1902b, pp. 172–173)" | "(Simmel, 1902b, p. 172)" |
| 57, 129 | "Zhou, Lei, Liu, et al." | "Zhou et al." |
| 117 | "(p. 9)" after "in person" | "(p. 8)" |
| 137 | "responsibility" inside the Elish quotation | "responsibilities" |
| 137 | "interpreting, addressing, and keeping track" | "interpreting, specifying intent, and keeping track" |
| 151 | "[See `figures/figure1_algorithmacy_cycle.svg`.]" | delete; add callout at line 75 |
| 299 (refs) | `"gigs".` | `"gigs."` |
| 177 (refs) | `4(2), 1–14.` | `4(2), Article 2053951717718855.` |
| 241 (refs) | `27(6).` | `27(6), NP1–NP7.` (confirm) |
| 327 (refs) | `(2007)` Suchman | confirm 2007 vs Crossref 2006 |
| 1 | HTML comment | delete |
| 17, 23 | AUTHOR flags | resolve and delete |

No other spelling, agreement, or punctuation errors found on a full read. Items I deliberately did not touch: the spaced en dash in the Bucher et al. (2021) title (as registered by the publisher); "Sage" vs "SAGE Publications"; the straight quotes.

## Files used

- Manuscript: `/Users/ludwitt/iit-playground/wt-algorithmacy-ot/submissions/algorithmacy_ot/manuscript/REVISION_2026-10-09.md`
- Figure: `/Users/ludwitt/iit-playground/wt-algorithmacy-ot/submissions/algorithmacy_ot/manuscript/figures/figure1_algorithmacy_cycle.svg`
- Publisher PDFs: `/Users/ludwitt/iit-playground/pyphi-experiments/submissions/lima_pdw/literature/pdfs/` (hindsvonkrogh2024, starkvandenbroeck2024, orlikowskiscott2023, leonardileavell2026, stelmaszak2026, schoeneborn2026, guzmanlewis2020, hancock2020_vor, zhou2025apjhr_workingpaper, suddaby2010, sutherland2020, rahman2021_onlinefirst_typeset, sundar2019; sundar2000.pdf and sandberg2000.pdf have no text layer)
- Library texts: `/Users/ludwitt/iit-playground/pyphi-experiments/dissertation/research/library/pdfs/` (curchod2020, cameron2024, elish2019, devito2021, selznick1949, christin2017, lee2015, bucher2021, powell1990, kornberger2017, rahman2021, zhou2025competency)
- Okhuysen & Bechky: `/Users/ludwitt/iit-playground/pyphi-experiments/dissertation/current/paper1/exemplars/annals_coordination/text/okhuysen2009.txt`
- Simmel 1902 Part II: https://archive.org/download/jstor-2761932/2761932.pdf
- Jarrahi & Sutherland deposit: https://metadataetc.org/gigontology/pdf/ (ResearchGate copy)
- Records: api.crossref.org (94), api.datacite.org and sociologica.unibo.it (Stark & Pais), api.openalex.org and api.semanticscholar.org (abstracts, Korczynski pages), emerald.com (Obstfeld), web search (Clark & Brennan editors; Pyyhtinen; Katsh & Rifkin)

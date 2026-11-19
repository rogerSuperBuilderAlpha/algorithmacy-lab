# Verification report: verifier_4 (rr-2026-11)

Date: 2026-11-08. Scope: 19 cards, all upgraded to full text from user-supplied PDFs (UPGRADE_up_2 and UPGRADE_up_3).

What I checked:

- **Identity.** I re-fetched all 19 Crossref records on 2026-11-08 and compared each with the card frontmatter and its `references.bib` entry.
- **Depth.** I compared each PDF's page count (pdfinfo) with the card's `source_basis`.
- **Quotations.** I matched every quoted string in each card body against three extractions of the PDF: the saved `fulltext.txt` (layout mode), a raw pdftotext pass, and a half-page column crop for two-column layouts. Matching ignored case, punctuation, soft hyphens and line-break hyphenation. Card locators were checked against printed page numbers. I derived the offsets from the running heads: Ananny +972, Are +1995, Batat 2022 +608, Batat 2024 +1218, Batat & Hammedi +9, Belanche +266, Duggan +1430, Eslami +2370, Germann Molz +228, Möhlmann +1998, Mosca +425, Padigar +20, Pedersen +79, Pigac +282. The article-numbered papers (Batat 2021, Hirsbrunner, Jianu, Lin, Mameli) use the PDF page number. Where the script missed a passage, I found it by hand and read it in context.
- **v4.** Every v4 sentence I judge here I read in `submitted.md`.

I edited no card and no other file. My working copies are in the session scratchpad.

**Result.** Every quotation from a source is in that source. Apart from three minor page-boundary or wording issues (Are, Mosca, Batat 2024), every locator is right. No card fails. I disagree with four support verdicts (Germann Molz, Eslami, Pedersen, and Batat 2024 by degree). Each of these is noted below.

---

## Priority checks (as asked by the lead)

1. **Batat and Hammedi (2023: 10).** v4: 'continuum in terms of customer value from physical to digital settings and vice versa'. **MATCH, p. 10.** It is verbatim in the abstract. One addition to the card's PARTLY verdict on "describes its purpose as": the sentence sits under the abstract's **"Findings –"** heading. The **"Purpose –"** heading says instead that "This review article aims to provide researchers with a new comprehensive and integrative extended reality technology (ERT) framework" (p. 10). So v4's "purpose" names the wrong rubric of the very page it cites. The purpose-like sentence is p. 11 ("guarantee a continuum in customer value …", no "in terms of"), as the card says. I agree with PARTLY.
2. **Batat (2024: 1220).** v4: 'fluidifying the journeys of customers from online to offline and inversely'. **MATCH, p. 1220** (abstract; PDF p. 2 after the T&F cover sheet). Nuance on v4's "aims at": the abstract makes fluidifying the *means* ("to help managers design compelling customer experiences. This is done by fluidifying …", p. 1220). The goal language is elsewhere: "should also focus on fluidifying" (p. 1235). This is not an error. It does sit alongside the p. 1238 caution the card records.
3. **Mameli et al. 2026, "57 studies and 84 industry cases".** **SUPPORTED.** Sources: "A total of 57 academic articles were analysed" (p. 1); "The PRISMA process resulted in 57 eligible studies" (p. 7); "a total of 84 industry examples" (p. 8); both counts again on p. 25.
   - **"no discussion of friction at all": I agree with PARTLY.** The string "friction" occurs zero times in all three extractions. But the article discusses "the potential risks and challenges" (p. 13), "drawbacks such as technical glitches and privacy concerns" (p. 14), Table 7's "Risks, and challenges" (p. 22) and "negative aspects of engagement" (p. 26). All four quotations MATCH.
4. **Jianu et al. 2025, claim-contradicted.** **I agree.** The paper describes itself as "a Delphi methodology to gauge consensus about the future implications of AM" (p. 4). Table I (p. 4) lists 22 experts, 9 of them academics (2 assistant professors, 1 associate professor, 4 professors, 2 senior lecturers). Pricing appears only where the authors cite other work: the literature review (p. 3) and, which the card misses, the conclusion: "applied primarily to areas such as revenue management, pricing … (see e.g. Hertzfeld, 2023; Ivanov and Webster, 2024)" (p. 9). Neither is a finding, so v4 line 33 is NOT SUPPORTED, and the flag is justified.
5. **Lin 2025, p. 9.** **MATCH.** The quotations are "Every time I pressed dislike, the relevant content was reduced" and "there is no use to 'dislike' politically relevant information" (Ruoxi, p. 9). The p. 9 quotation is one participant's account. Page 8 makes the card's point more broadly: "another 16 respondents also showed similar fluid resistance … They selectively resisted some of the content". Lin calls this "dominant resistance" kept within the platform's features (pp. 8–9). I agree with PARTLY on v4 line 60.
6. **Padigar et al. 2025, p. 32.** **MATCH and fair.** Section 5.2 gives "customers 'have to' contact customer service and support center when there is a problem" as an example of a have-to task. Section 5.3 puts topic 2 ("resolve offering-related issues") among tasks "of relatively low task value", where "the friction in these tasks can be 'frustrating friction,' and reducing or eliminating friction in these tasks can enhance customer experience" (p. 32). The kept, constructive frictions are payments and fraud or authentication (topics 3 and 6, p. 32). I found no discussion of negotiation, exception or recognition. The card's ellipsis drops "can be", so the source's hedge is softer than "classes". The verdict stands. I agree with PARTLY on v4 line 72.

---

## pigac2026transparency
**PASS**
- Identity: Crossref gives CHQ 67(3), 283–297; online 9 Apr 2026, print Aug 2026; authors Pigac, Tilen; Lee, Ada; Huang, Ava. Card and bib match.
- Depth: 15-page VoR; full text is honest.
- Quotes: all MATCH with correct pages (p. 286 Table 1; p. 287 sample; p. 291 Theme 4, Table 4, the guest quotations and the dashboards; p. 292 "transparency mediators" and "mass-market or utilitarian"). Opt-in appears on pp. 289 and 291–293, as the card says. Trivial: the source prints "Poststay", the card "Post-stay".
- Support: I agree that line 65 is PARTLY (staged disclosure, "minimal disclosure during check-in", p. 286). I agree that the "transparency only" correction is right: override and control are present (p. 291). I also agree that Theme 4 is usable for the fourth principle.
- Housekeeping: `verified_date` still reads 2026-08-11.

## pedersen2022
**PASS-WITH-NOTES**
- Identity: Crossref gives JPART 33(1), 80–93; print 5 Jan 2023, online 5 Mar 2022. The card year (2023) and the bib match. The citekey still carries 2022, as the card notes.
- Depth: 15 PDF pages (80–93 plus one extra); full text is honest.
- Quotes: all MATCH (p. 80 abstract; p. 89 ×2; p. 90 Table 1 and training; p. 91 ×3).
- Support: **I disagree in degree** with SUPPORTED for v4 line 31. The card itself says "more and more of their day" "is not measured in the paper". A sentence with an unsupported trend clause is PARTLY, not SUPPORTED. The workaround clause is supported (pp. 80, 89). I agree that the well-being claim is not in the source.
- Housekeeping: `verified_date` still reads 2026-08-07.

## padigar2024friction
**PASS**
- Identity: Crossref gives P&M 42(1), 21–43; print Jan 2025, online 21 Aug 2024. The card year (2025) and the bib match. The citekey carries 2024.
- Depth: 23-page VoR; full text is honest.
- Quotes: all 9 MATCH with correct pages (p. 21 definition; p. 26 typology; pp. 28 ×2, 29, 32 ×3). See priority check 6.
- Support: I agree with PARTLY on line 72, and with the correction to the negotiation gloss.
- Housekeeping: `verified_date` still reads 2026-08-07.

## mohlmann2021algorithmic
**PASS**
- Identity: Crossref gives MISQ 45(4), 1999–2022, Dec 2021. Matches.
- Depth: 25 PDF pages; full text is honest.
- Quotes: all MATCH (p. 2007; p. 2009 ×2; p. 2010 ×3).
- Support: I agree with PARTLY on line 36: no controls while still being rated (pp. 2009–2010), but nothing on the "guest's sense of control". The status mismatch (card says "cut", v4 still cites it) is correctly flagged for the authors.

## lin2025oscillation
**PASS**
- Identity: Crossref gives SM+S 11(1), article 20563051251313610, Jan 2025; author Lin, Hui. Matches. The bib has no pages field, which is fine for an article-numbered journal.
- Depth: 13-page VoR; full text is honest.
- Quotes: all 9 MATCH (p. 1; pp. 9 ×2, 10 ×4, 11 ×2).
- Support: see priority check 5. I agree with the suggested rewording. Page 8 (17 respondents) would be a stronger locator than p. 9 for the claim that users steer non-political curation.
- Housekeeping: `verified_date` still reads 2026-08-11.

## jianu2025
**PASS-WITH-NOTES**
- Identity: Crossref gives IJHM 129, article 104168, Aug 2025. Matches.
- Depth: 14-page VoR; full text is honest.
- Quotes: all 11 source quotations MATCH with correct pages (pp. 1, 3, 4 ×2, 5 ×3, 7, 10, 11, 12). The p. 5 items "Control will always remain …" (73.34 %) and "Managers will have more control but less empowerment" (61.54 %) are two of "Three items [that] reached weaker consensus" (p. 5). The card does not say they were weak-consensus items.
- Support: see priority check 4. I agree that line 33 is NOT SUPPORTED, and that lines 31 and 59 are PARTLY: translation runs to "frontline staff" (pp. 7, 10), not to guests.
- Note: "Pricing appears only in the literature review (p. 3)" is incomplete. Pricing also appears in the conclusion (p. 9), still citing others.
- Housekeeping: `verified_date` still reads 2026-08-07.

## hirsbrunner2025contestation
**PASS**
- Identity: Crossref gives Front. Commun. 10, 1638257, online 11 Dec 2025; authors Simon David Hirsbrunner, Steven Kleemann, Milan Nebyl Tahraoui. Card and bib match, and the name correction is right.
- Depth: 15-page VoR; full text is honest.
- Quotes: all MATCH (pp. 2, 3, 8, 8–9 across the page break, 9, 10 ×2, 11 ×2, 12). The police-project context appears on p. 4 and later.
- Support: I agree with PARTLY on line 67. "They must be competent to contest" (p. 3) cuts against the competence/standing split, as the card says.

## mosca2025phygital
**PASS-WITH-NOTES**
- Identity: Crossref gives J. Macromarketing 46(3), 426–445; online 15 Dec 2025, print Sep 2026. The card year (2026) and the bib match. The citekey carries 2025.
- Depth: 20-page VoR; full text is honest.
- Quotes: all MATCH. **Minor LOCATOR-WRONG:** "a seamless continuum in which physical exhibits, digital content, and human mediation are intertwined" runs from p. 440 to p. 441 ("are intertwined" follows the p. 441 running head). Cite it as pp. 440–441. Associate Editor Batat is on p. 441, as the card says.
- Support: I agree with PARTLY for the §8 well-being sentence. Mosca's dimensions are "individual, social, and societal" (p. 439).

## mameli2026framework
**PASS-WITH-NOTES**
- Identity: Crossref gives IT&T 28, **issue 1**, article 19; online 14 Feb 2026, print Jun 2026; first author Elisa. This settles the card's doubt: Crossref confirms the bib's `number = {1}`, though the PDF does not print it.
- Depth: 31 pages ("Page N of 31"); full text is honest.
- Quotes: all 12 MATCH with correct pages (pp. 1 ×2, 13 ×2, 14, 22, 25 ×2, 26 ×4). The July 2023 search date is on p. 6, as the card says.
- Support: see priority check 3. I agree with SUPPORTED for the counts and PARTLY for "no discussion of friction at all".

## germannmolz2018scale
**PASS-WITH-NOTES**
- Identity: Crossref gives H&S 8(3), 229–251, 2018. Crossref lists the author as given "Jennie Germann", family "Molz". The card and bib's "Germann Molz, Jennie" follow the author's own usage, which is fine.
- Depth: 24 PDF pages (23 article pages plus an advertisement); full text is honest.
- Quotes: all MATCH (pp. 229, 233, 235, 236, 237 ×2, 244 ×2, 245).
- Support: I agree with PARTLY on "what hosts feel" (discourse analysis, p. 235), and with SUPPORTED on the third-party unsettling of who hosts (p. 244).
- **I disagree** with SUPPORTED for revision-plan §2 *Transfer*. The plan's move is that ownership "moves only with the role" and, when handed to a system, "stays with the institution by default". In Germann Molz the platform succeeds in "transferring legal and tax liabilities onto homeowners and regulatory obligations onto municipalities" (p. 245) and "exempts itself" (p. 244). That is evidence of institutions *shedding* responsibility. It is a precedent for the problem, not for the claim that ownership stays put. I would call it PARTLY: usable as a hospitality-literature precedent for the stakes, not as support for the Transfer conclusion.

## eslami2016folk
**PASS-WITH-NOTES**
- Identity: Crossref gives CHI '16, 2371–2382. Matches.
- Depth: 12 pages; full text is honest.
- Quotes: all MATCH (pp. 2371 ×3, 2373, 2375, 2379 ×3, 2380 ×2). The $10/hour payment is on p. 2373.
- Support: I agree with SUPPORTED for the folk-theory sentence (p. 2373), with the card's seamful-probe caveat.
- **I disagree** with the card's claim that the source "supports … directly" the claim "Skill cannot conjure a counterparty". The p. 2380 finding is about *perceived* agency: "many users see even these simple tasks as being outside of their abilities". The authors treat it as a design and learning gap: "changing the design to give users a greater feeling of agency over their News Feed and promoting learning about it using seamful design" (p. 2380). That is the interface-and-education remedy v4 line 67 calls a misdiagnosis. So it is weak support for competence ≠ standing, and a reviewer could turn it against the paper.

## duggan2026tensions
**PASS-WITH-NOTES**
- Identity: Crossref gives IJHRM 37(8), 1432–1465; authors include Prakriti Dasgupta. Card and bib match. Crossref's dates are odd (print 28 Apr 2026, online 16 Jul 2026), which does not affect citation.
- Depth: 35 PDF pages including the cover; full text is honest.
- Quotes: all MATCH (pp. 1432, 1441, 1446, 1447, 1448 ×2, 1449).
- Support: I agree with PARTLY on "an inability to contest decisions at all". The card missed one passage. The data-structure table on p. 1444 lists "Workers unable to contest or dispute ratings". That is closer to v4's wording than "rarely having any opportunity" (p. 1448), but it is about ratings, not decisions generally. "At all" still overstates.

## belanche2020
**PASS**
- Identity: Crossref gives JOSM 31(2), 267–289, 2020. Matches.
- Depth: 24 PDF pages (23 article pages plus a licence page); full text is honest.
- Quotes and statistics: all MATCH. The figures are n = 331 (p. 273); agent responsibility 4.01 vs 3.47, F = 16.33 (p. 275); firm responsibility 4.35 vs 4.12, F = 4.68 (p. 275); H4b not supported (p. 275); failure-only simple effect F = 3.97 (p. 277). Page 282 has the mechanical/analytical result, and p. 283 the human-assistance advice.
- Support: I agree with SUPPORTED with the stated caveats: vignette respondents, not guests; a main effect, not an interaction.

## batathammedi2023ert
**PASS-WITH-NOTES**
- Identity: Crossref gives JOSM 34(1), 10–33; online 6 Oct 2022, print Jan 2023. The card `title` omits the subtitle ": A Service Research Agenda", which Crossref, the bib and v4 all carry.
- Depth: 25 PDF pages (24 article pages plus a ProQuest page); full text is honest.
- Quotes: all MATCH (pp. 10, 11, 13, 14, 18 ×2, 23, 24 ×2). The v4 quotation is a MATCH (see priority check 1).
- Support: I agree with PARTLY on "describes its purpose as" and add the Findings-heading point. I agree with SUPPORTED for smoothness as a goal (p. 14).
- Note: the special section was "guest edited by Wided Batat, Wafa Hammedi and Paula C. Peter" (p. 10). That is three editors; the card names two. The citation of this paper as "Batat and Hammedi (2022)" in Mameli et al. is confirmed.

## batat2024phcx
**PASS-WITH-NOTES**
- Identity: Crossref gives JSM 32(8), 1220–1243; online 5 Apr 2022, print 2024. Matches.
- Depth: 25 PDF pages including the cover; full text is honest.
- Quotes: all MATCH. "shifting from physical to digital ('digitalization') and from digital to physical ('physicalization')" runs across the Figure 1 page break, pp. 1230–1231, as the card says. The other quotations are on pp. 1220, 1229, 1230, 1233, 1234, 1235 ×2, 1237 and 1238.
- Support: I agree with PARTLY for the §1 AI attribution. "Artificial intelligence" appears only in reference-list titles. On "aims at", see priority check 2: the claim is supported, and "This is done by" makes fluidifying a means. The verdict is still acceptable.

## batat2022tlr
**PASS**
- Identity: Crossref gives J. Macromarketing 42(4), 609–623, 2022. Matches.
- Depth: 15-page VoR; full text is honest.
- Quotes: all MATCH (pp. 609 ×2, 612, 615, 618, 618–619 across the page break, 620).
- Support: I agree with PARTLY: "service ecosystems" is wrong for the luxury ecosystem, and p. 612 has the "cultural" variant.

## batat2021ar
**PASS**
- Identity: Crossref gives TF&SC 172, 121013, Nov 2021. Matches.
- Depth: 13 pages; full text is honest.
- Quotes: all MATCH (pp. 4, 5 ×2, 7, 8 ×2, 9 ×3, 10, 11).
- Support: I agree with PARTLY. I searched for decline, opt-out, refuse and "choose not" and got no hits. The source is silent on opt-out, and on rules and discretion.

## are2025appeals
**PASS-WITH-NOTES**
- Identity: Crossref gives ICS 28(11), 1997–2014; online 30 Aug 2024, print 2025. Matches.
- Depth: 19 PDF pages including the cover; full text is honest.
- Quotes: all MATCH (pp. 2002, 2003 including the 400,000 figure, 2004, 2005 ×2, 2006 ×2, 2010, 2011). **Minor LOCATOR-WRONG:** the card quotes "cop, judge and jury" at p. 2010. That exact string is on p. 2011 ("an algorithmic cop, judge and jury"). Page 2010 reads "algorithmic cop, algorithmic judge and jury", and the abstract (p. 1997) has "'algorithmic cop, jury and judge'".
- Support: I agree with SUPPORTED for both v4 uses, with the persistence caveat (p. 2004).

## ananny2018seeing
**PASS**
- Identity: Crossref gives NM&S 20(3), 973–989; online 13 Dec 2016, print 2018. Matches.
- Depth: 17-page VoR; full text is honest.
- Quotes: all MATCH (pp. 976, 978, 979, 980, 983, 984, 985). "Forum" and "Bovens" occur zero times, which confirms the card's correction. The bib note "leaves the forum absent" is the authors' gloss, not the source's term.
- Support: I agree with PARTLY on both v4 §5 uses.

---

## Summary table: FAILs and non-MATCH quotes

| card | item | status | note |
|---|---|---|---|
| none | none | no FAIL | none |
| are2025appeals | "cop, judge and jury" (card: p. 2010) | LOCATOR-WRONG (minor) | exact string is on p. 2011; p. 2010 reads "algorithmic cop, algorithmic judge and jury" |
| mosca2025phygital | "a seamless continuum … are intertwined" (card: p. 440) | LOCATOR-WRONG (minor) | runs pp. 440–441 |

**Verdict disagreements, for the lead.** These are not FAILs.

| card | card verdict | mine | why |
|---|---|---|---|
| germannmolz2018scale | §2 Transfer SUPPORTED | PARTLY | the platform sheds liability onto hosts (pp. 244–245); this does not show ownership staying with the institution |
| eslami2016folk | supports "skill cannot conjure a counterparty" directly | weak / double-edged | p. 2380 is about perceived agency, and the authors' remedy is seamful design and learning |
| pedersen2022 | line 31 SUPPORTED | PARTLY | the card concedes "more and more of their day" is unmeasured |
| batat2024phcx | "aims at 'fluidifying …'" SUPPORTED | SUPPORTED, with a nuance | the abstract makes fluidifying the means ("This is done by", p. 1220) |

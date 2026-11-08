# Verification report: verifier_3 (rr-2026-11, full-text pass)

Date: 2026-11-08. Scope: 19 cards upgraded to full text from author-supplied PDFs. What I did:

- **Identity.** I re-fetched all 19 Crossref records today and compared them with each card's frontmatter and its `literature/references.bib` entry.
- **Depth.** I re-extracted every `user_pdf/fulltext.pdf` myself with `pdftotext`, in raw and layout modes, so I did not rely on the upgraders' `fulltext.txt`. All 19 PDFs are complete versions of record (9 to 45 pages each), so every `full-text` claim is honest.
- **Quotes.** A script found every quoted string in each card body in the PDF text. It normalised case, punctuation, soft hyphens and line-break hyphenation, and then mapped the hit to a printed page using an offset I checked against each PDF's running heads. I checked by eye the strings that fail only because of a page header, a footnote numeral or scan run-ons. Strings the cards quote from v4, the plan or the WS reports are not source quotes. I checked the v4 ones against `submitted.md`.
- **Support.** I judged each support verdict from the PDF text, and I read the passages behind the five pressed verdicts in context.

I edited no card. My working files are in the session scratchpad (`v3/`).

**Counts: PASS 9, PASS-WITH-NOTES 10, FAIL 0.**

---

## Pressed verdicts first

### lind1990voice
**PASS-WITH-NOTES**
- Identity: matches Crossref, JPSP 59(5), 952–959; the card and the bib agree. The PDF is the APA scan (journal pp. 952–959 plus a reproduction page).
- Quotes: all 14 source quotes are MATCH with the right pages. The page-955 sentence "The voice conditions produced higher ratings…" matches once the scan's run-together words ("higherratingsof") are allowed for. Note 3 is on p. 955 and Table 1 is on p. 956. The cell means 2.43/3.15/3.70 and 2.11/2.72/3.31 are exact.
- **v4 post-decision sentence: I agree it is SUPPORTED.** In the postdecision condition the goal "would not be changed regardless of what the subject said" (p. 954). Both fairness measures rose over no voice, and note 3 confirms that every pairwise contrast was significant (p. 955).
- **v4 "lowers those judgments instead of raising them": I agree it is CONTRADICTED as v4 words it, but the card understates the literature.** The study's own hollow-voice condition raised both judgments. However, Lind et al. do not mention lowering "only as 'conceivable'". They write: "There is evidence that, under some circumstances, people actively reject procedures that appear to offer process control but that do not provide any real input", and they cite Folger's frustration-effect studies, where this happens "when repeated unfavorable outcomes or communications from others focus attention on possible biases" (p. 953). So a lowering effect exists in the literature, but only under conditions. v4 states it unconditionally and credits "the same research", which is what fails. A conditional sentence could cite Folger (1977) or Folger et al. (1979). It could also cite Lind and Tyler (1988), whom Vaccaro et al. quote: voice effects "can be attenuated or reversed when the procedure is weak or when there is social criticism of the procedure" (Vaccaro p. 167:16).
- "Manufactured" warning: I agree it is SUPPORTED and points the way the card says (p. 958). The authors add that voice-enhanced fairness is "all the more likely" where a decision maker "actively hides the ineffectiveness of input" (p. 958).
- Summary error: the card says perceived control mediated "part, not all" of the effect. That holds only for procedural fairness. For outcome fairness, the ANCOVA that removes control leaves no significant voice effect ("F < 1.0", p. 956). The abstract's "some, but not all" also refers to procedural justice only.

### bovens2007accountability
**PASS-WITH-NOTES**
- Identity: matches Crossref, ELJ 13(4), 447–468. The bib agrees.
- Quotes: all 13 source quotes are MATCH with the right pages. The "transparency as such…" quote on p. 453 has footnote 24 inside it; I checked it by eye.
- **§7 actor/forum reversal: I agree, with one refinement.** In Bovens the actor "has an obligation to explain and to justify", while the forum "can pose questions and pass judgement" (p. 450). So "a forum that is required to answer challenges" inverts the roles. The second clause, "someone in that forum has real authority to act", is consistent with Bovens' forum, which can use "veto powers … It can block or amend decisions made by the actor" (p. 452). v4 therefore merges two roles: it puts the actor's duty to answer and the forum's power to amend in one body. A fix could keep both if it names them separately.
- **"Meaningful alternative" is not in Bovens: I agree.** The only nearby wording is "exercise exit or voice", in footnote 50 (p. 457), which is about parents and school reports. It is not an alternative route, and it is no basis for the citation.
- §4 "separates the power … from the duty": I agree it is PARTLY (many hands, p. 457).
- The card's own note that `rejected_reason` is stale while `status: cited` is correct. The frontmatter is still inconsistent.

### kropf2026blame
**PASS-WITH-NOTES**
- Identity: matches Crossref, IJSR 18(2), art. 30, online 16 Feb 2026. The bib agrees.
- Quotes: 15 source fragments are MATCH with the right pages. One is PARAPHRASED-AS-QUOTE in a minor way: "fail to fulfill a D associated with R" reads "the machine fails to fulfill a D associated with R" in the source (p. 11).
- **The role moves and answerability stays: I agree.** Answerability is "currently inconceivable" for robots (p. 9). Thick blame "lies with the moral – and therefore also human – actors" (p. 10). Holding robots to account risks "allowing humans to evade moral responsibility" (p. 12).
- Stronger evidence for the PARTLY on "role responsibility of a carer": Kropf et al. say that expecting the robot to "replace a human caregiver, does not currently correspond to R" (p. 6). That page is not cited on the card. The robot holds a scoped role of its own, not the carer's role.
- "Challenge from care" not a challenge to the conclusion: I agree. This also bears on v4 line 30 ("The nearest challenge comes from care. Kropf…").
- Cross-card note: Kong (p. 10) says the machine "is not a responsibility-bearer in any sense". Kropf grants it role responsibility and thin blame. Since §2 cites both, the two positions should not be merged.

### kong2026delegation
**PASS-WITH-NOTES**
- Identity: matches Crossref, AI & Ethics 6(5), art. 518, online 14 Sep 2026. The bib has no article number.
- Quotes: all 18 source quotes are MATCH with the right pages. "control-based" is split across a line in the PDF.
- **Ground is control over delegation, not role: I agree.** The deployer's standing "is grounded in her guidance control over the act of delegation" (p. 4). "A role matters derivatively rather than intrinsically" (p. 4).
- One overstatement: the card says "on his account the role does no independent work". Kong gives the role a job: "What the role contributes is a specification of the domain over which control and knowledge are exercised, and thereby of the outcomes that are hers to explain" (p. 4). He also says "Roles … are how it [control-based responsibility] is distributed across a division of labour" (p. 4). So Kong rejects the role as the *ground* but treats it as the vehicle that distributes responsibility. The plan's claim that ownership "moves only with the role" is unsupported as a ground. A weaker version, where roles mark where control-based answerability lands, has support on p. 4.
- **Fiduciary duty set aside: I agree.** It "is a different matter again and is set aside here" (p. 4). v4 line 30 already uses the trustee/successor comparison, so Kong cannot support it.
- Scope check: machine responsibility is explicitly out of scope (p. 2), but Kong also states his own position that the machine "is not a responsibility-bearer in any sense" (p. 10). The card's summary sentence is therefore fair.

### vaccaro2020contesting
**PASS-WITH-NOTES**
- Identity: matches Crossref, PACM HCI 4(CSCW2), Article 167, 22 pp. The bib agrees.
- Quotes: all 9 source quotes are MATCH with the right pages. "Of any kind" runs from p. 167:10 to 167:11 across a running head.
- **The study varied neither skill nor transparency: I agree.** Every condition showed the same Facebook explanation (§3.3.2, p. 167:7). Opacity was the theme of n = 113 responses (p. 167:13). No skill measure or manipulation exists. The table values (Accountable 4.76 vs 4.51/4.29/4.23, F(3,163) = 2.305, p = 0.07) and N = 182/449 are exact (pp. 167:9–11).
- I agree the three v4 uses are PARTLY and the WS_B gloss is PARTLY.
- Two things are not on the card:
  - p. 167:16 quotes Lind and Tyler (1988) on voice effects being "attenuated or reversed". That gives the Lind "limit" sentence a conditional source, as noted under Lind above.
  - In this study, denied appeals scored numerically *below* no appeal on all four measures (n.s.). That pattern is the nearest data in the library to v4's "lowers those judgments", and it is a non-significant result in a hypothetical scenario.

---

## Remaining cards

### wilsonnash2025captivity
**PASS-WITH-NOTES**
- Identity: Crossref gives P&M 43(5), 974–985, online 30 Dec 2025, print May 2026. The frontmatter has `year: 2025` and no volume or pages. The card itself records the 2026 VoR year. There is no references.bib entry, which is consistent with `status: rejected`.
- Quotes: all 21 source quotes are MATCH with the right pages. Two fail the script only because of soft hyphens, on pp. 975 and 976.
- I agree with "grounds the second condition" as PARTLY. I also agree the alternative-route sentence is SUPPORTED by Wilson-Nash (pp. 978, 979, 981), not by Bovens.
- Inconsistency: the card recommends "admit" while its status is `rejected` and its "Where it enters" section still says "Not admitted". This is a lead decision, not an error.

### didomenico2007host
**PASS-WITH-NOTES**
- Identity: Leisure Studies 26(3), 321–338 is correct. Frontmatter spells the first author "MariaLaura", but Crossref, the bib and the PDF all have "Marialaura".
- Quotes: all 13 source quotes are MATCH with the right pages (PDF page 1 is the T&F cover).
- "Negotiat-" occurs only in the abstract (p. 321). I agree that the "negotiated" use is PARTLY and that the findings show host-set rules and guest deference (pp. 332–335).

### golubovskaya2017meaning
**PASS**
- Identity: matches, IJCHM 29(5), 1282–1304. All 11 source quotes are MATCH. "Overrides…" opens p. 1300, so pp. 1299–1300 is acceptable.
- I agree the displacement clause is SUPPORTED and the obligation-content use is NOT SUPPORTED.

### beatty2016compliance
**PASS**
- Identity matches. All 12 source quotes are MATCH.
- The numbers are exact: 18 interviews; 79/133 and 144/261 incidents; 57.4% and 68.4% policy/legal deterrents; all-male samples (pp. 160–163, 166–167).
- I agree both v4 uses are PARTLY.

### gursoy2026reconceptualizing
**PASS**
- Identity matches, JHMM 35(2), 151–165. All 13 source quotes are MATCH. Several fail the script only because of soft hyphens; "not ethically neutral" runs across pp. 155–156.
- I agree both v4 uses are SUPPORTED. The p. 160 accountability passage is real and correctly located.

### liu2026hospitableness
**PASS**
- Identity matches, IJHM 135, 104640. All 12 source quotes are MATCH.
- I agree with PARTLY on "test": "Future studies should test the framework using physical robots, VR, and field experiments" (p. 9).

### shabnam2026tpsr
**PASS**
- Identity matches. Crossref has no volume, pages 1–17, online 3 Jul 2026. All source quotes are MATCH on the PDF pages given.
- I agree with "friction as a cost": "thereby reducing friction and restoring agency" (p. 10). I also agree that the contestability passage on p. 14 overlaps v4's reachable-person principle.

### hatherley2025moving
**PASS**
- Identity matches. Crossref gives 27(2), art. 20; the bib has no number.
- All 10 source quotes are MATCH.
- I agree all three uses are PARTLY. p. 12 confirms that explainability methods are "poorly equipped to address the problem of update opacity".

### sharmamattila2025rights
**PASS-WITH-NOTES**
- Identity: the VoR is 2026, 50(6), 904–920, and the bib is correct. Frontmatter `year: 2025` is wrong. The card says 2025 is "the online-first year", but Crossref gives online 16 Jan 2026 and the PDF reads "research-article2026". 2025 survives only in the DOI suffix.
- All 7 source quotes are MATCH. I agree with the verdicts.

### yurrita2025needs
**PASS-WITH-NOTES**
- Identity: Crossref gives PACM HCI 9(7), 1–29, and the article is CSCW234. The bib has `number = {CSCW}`, which is wrong; it should be 7, with the article number. The card notes that the v4 reference lacks the issue and article number.
- All 13 source quotes are MATCH.
- I agree that the line-67 use is PARTLY, that the "precondition" correction is right (p. CSCW234:18 says social transparency is a "pre-requisite" for ex-ante mechanisms), and that p. 16 is usable for the fourth principle.

### ytrearnemoe2021folk
**PASS**
- Identity matches. All 10 source quotes are MATCH; the five-theory list spans pp. 813–814.
- The 59%, N = 804 and 553 figures are exact (p. 812). I agree with PARTLY and with the swap-candidate flag.

### vaccaro2020contesting — see above.

### sterz2024effectiveness
**PASS**
- Identity matches, FAccT '24, 2495–2507. All 10 source quotes are MATCH.
- I agree with the verdicts. Accountability is listed among "objectives other than risk mitigation … beyond the scope" (p. 2498).

### schmidt2025field
**PASS**
- Identity matches, 34(4), 559–575. All 9 source quotes are MATCH.
- The self-selection point is right (pp. 565, 571). I agree that "little is at stake" is the authors' gloss.

### rahman2021cage
**PASS**
- Identity matches, ASQ 66(4), 945–988 (JSTOR copy).
- All 10 source quotes are MATCH. The two reactivity types and their two mechanisms are on p. 947, and the card's corrections hold.
- I agree that both v4 uses are SUPPORTED.

---

## Table: FAILs and every quote that is not MATCH

| card | item | type | note |
|---|---|---|---|
| (none) | — | FAIL | No card fails. |
| kropf2026blame | "fail to fulfill a D associated with R" | PARAPHRASED-AS-QUOTE (minor) | Source: "the machine fails to fulfill a D associated with R" (p. 11) |

Every other source quote across the 19 cards is MATCH with a correct locator.

## Notes the lead should act on (not FAILs)

1. Lind: v4's "lowers" sentence is contradicted by the study's own result. A conditional version has sources: Folger's frustration effect, cited in Lind p. 953, and Lind and Tyler 1988, quoted in Vaccaro p. 167:16. The card's "only conceivable" understates p. 953. The mediation clause in the card summary applies to procedural fairness only (p. 956).
2. Bovens §7: only the "forum … required to answer" clause is inverted. The forum's "authority to act" matches Bovens p. 452.
3. Kong: the role is not the ground, but Kong does treat it as the vehicle that distributes answerability (p. 4). The card's "does no independent work" goes too far.
4. Metadata:
   - sharmamattila frontmatter year should be 2026; its "online-first" note is wrong.
   - yurrita bib `number` is wrong.
   - kong bib lacks art. 518; hatherley bib lacks the issue number.
   - didomenico frontmatter spells the author "MariaLaura".
   - wilsonnash frontmatter has year 2025 and an inconsistent status and recommendation.
   - bovens has a stale `rejected_reason`.

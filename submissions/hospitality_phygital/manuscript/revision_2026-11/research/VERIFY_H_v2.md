# VERIFY_H_v2: verification of run rr-2026-11-h cards and the H3/H4 syntheses

Verifier: Claude (verification agent), 10 November 2026. I followed `VERIFY_BRIEF.md`, with the run-specific changes I was given. I edited no card and committed nothing. The only file I wrote is this report.

**Scope.** I checked 10 new cards in full. For the 8 upgraded cards I checked only the material marked as added in rr-2026-11-h. I also checked every quotation and locator that `WS_H3_multi_actor.md` and `WS_H4_guests_negotiation.md` attribute to a source, and whether each synthesis claim follows from the cited text. The v4 text is `manuscript/DRAFT.md` and the outline is `manuscript/revision_2026-11/PITCH_AND_OUTLINE.md` (PO).

**Method.** I re-fetched Crossref records for every new card with a DOI. Abstracts came from OpenAlex, plus Semantic Scholar for Hewagama et al. I matched quotations against the saved texts in `research/sources/<citekey>/` with a normalising matcher (it ignores whitespace, hyphenation, ligatures, case and punctuation, and reads the "1" for "l" substitution in the Pitt-Rivers text layer as "l"). I then read each hit in context and mapped PDF pages to printed pages using the running heads. I also fetched two sources the drafters did not have:

- **Crinkley, paginated.** The Harvard Caselaw Access Project copy of 844 F.2d 156 (`static.case.law/f2d/844/html/0156-01.html`) carries the Federal Reporter star pages. All 17 Crinkley quotations also match this text.
- **Cobbe et al., version of record.** UCL Discovery holds the ACM version of record (`discovery.ucl.ac.uk/10169099/7/…_VoR.pdf`). It is printed with pp. 1186–1197.

Both copies are saved in the session scratchpad, not in `sources/`.

**Totals (18 cards).** 4 PASS, 13 PASS-WITH-NOTES, 1 FAIL.

---

## New cards

### crinkley1988holiday: PASS-WITH-NOTES

- **Identity.** The CAP record gives 844 F.2d 156, pp. 156–170, decided 7 April 1988. Phillips wrote for the court; Wilkinson concurred in part and dissented in part. All of this matches the card.
- **Paragraph locators.** All are correct against both the law.resource.org copy and the CAP copy: para 7 (three-party structure), 49 (doctrine), 50 (two-part test), 51 (holding out, disclaimer, appearance), 52 (reliance), fn 3 (Hayman), 57 and 58 (dissent). All 17 quotations: MATCH.
- **Reporter pages.** The card says p. 166 was "NOT seen". I found it in the CAP copy:

  | Material | Paragraphs | 844 F.2d page |
  |---|---|---|
  | Three-party structure | 7 | 159 |
  | Doctrine, test, holding-out facts up to "Holiday Inns contends that the franchise agreement disclaims…" | 49, 50, 51 (first part) | 166 |
  | "not alone determinative", "create the appearance", reliance | 51 (rest), 52 | 167 |
  | Hayman distinction | fn 3 | 167 (anchored in para 52) |
  | Dissent | 57, 58 | 168 |

  The secondary citation "844 F.2d at 166" is therefore right for the doctrine and the test. The holding on appearance and the reliance finding sit at 166–67.
- **Holding.** The card states it correctly. The theory is apparent agency, or agency by estoppel, under North Carolina law (para 49). The test has two prongs, representation and reliance (para 50). Three points of posture belong in any sentence that uses it:
  1. The court decided only that the evidence "sufficed to support submission of this theory" to the jury (para 50), and it affirmed the jury's finding of vicarious liability (para 9).
  2. The court called the reliance evidence "marginal" (para 52).
  3. Owners, operator and franchisor were all held liable (para 9). The card's summary says so.
- **Overstatement (card `hold_rationale`, repeated in WS_H3 §3).** Both say the court held the brand answerable "for a property it neither owned nor ran". "Neither owned" is right. "Nor ran" is not the majority's finding. The majority says Holiday Inns "retained a significant degree of control over the operation of the Holiday Inn-Concord" through the franchise agreement, and had "designed and built" the motel (para 51, p. 166). "Played no role in its management" is the dissent's characterisation (para 57). Suggested wording: "a property it did not own and did not operate day to day".
- **Dissent.** Wilkinson's main disagreement is with causation and damages ("I would reverse and remand for a new trial on damages", para 69). The "innkeeper" phrase quoted in para 58 is his framing of the result. The card's use of the quotation is accurate.

### cobbe2023understanding: PASS-WITH-NOTES

- **Identity.** Crossref gives Cobbe, Veale and Singh, *2023 ACM Conference on Fairness, Accountability and Transparency*, pp. 1186–1197, 12 June 2023. This matches the card.
- **Quotations.** All 12 match the arXiv v2 text. All arXiv locators are right, including pp. 2–3 for "We do not offer concrete technical or organisational proposals".
- **Mapping to proceedings pages.** The version-of-record PDF paginates exactly like arXiv v2 for every quoted passage, so proceedings page = arXiv page + 1185:

  | Card locator (arXiv) | Proceedings page |
  |---|---|
  | p. 1 | 1186 |
  | p. 2 | 1187 |
  | pp. 2–3 ("We do not offer…") | 1187 only |
  | p. 7 | 1192 |
  | p. 8 | 1193 |
  | p. 9 | 1194 |
  | p. 10 | 1195 |

  I re-ran every quotation against the VoR text; all match. (Unpaywall labels the UCL file "submittedVersion", but it carries the ACM layout and the printed page numbers 1186–1197.)
- **Inference presented as the source's.** The Summary says the paper "says allocation must follow factual control, not contractual labels". WS_H3 §3 makes the same move: "Allocation should follow factual control, since 'the factual situation outweighs contractual … arrangements' (p. 8)". On p. 8 (proceedings p. 1193), Cobbe et al. *report* the CJEU's data-protection rule ("the CJEU has consistently held…"). They then say that challenging providers' claims "would involve litigation". They state no general allocation rule; the card's own Critical note says "Do not cite it for an allocation rule". The "should" belongs to the workstream.

### kaniadakis2022responsibilisation: PASS-WITH-NOTES

- **Identity.** Matches Crossref: NMS 26(10) 5763–5783, online 12 December 2022.
- **Quotations.** All 18 MATCH at the stated OnlineFirst pages (2, 6, 8, 12, 14, 16). The method claims are right: 35 informants, February–April 2018, a "historical snapshot" (p. 3).
- **Note.** Farmaki, Stergiou and Kaniadakis (2019) report the same design: 35 European hosts, recruited through a COST Action network and interviewed on Skype (AM p. 6). The two papers very probably draw on one dataset. Do not present them as independent corroboration.

### filatovabilous2021platform: PASS-WITH-NOTES

- **Identity.** Matches Crossref: *Internet Policy Review* 10(2), 12 May 2021. Crossref lists no pages.
- **Quotations.** All 7 MATCH.
- **Locator.** "focuses not on the way…" begins on p. 12 and runs onto p. 13 (the word is split "fo-/cuses" across the page break). Cite it as pp. 12–13.
- **Coverage.** The "objective" and "subjective" labels are the author's own (p. 12, "I will call it the objective approach"; p. 13). The card honestly records that sections 6–7 were only skimmed.

### farmaki2019selfperceptions: FAIL

- **Identity.** Matches Crossref: JST 30(5) 983–1003. Crossref gives the second author as "Stergiou, Dimitrios", without the "P." the card adds. The middle initial is unconfirmed.
- **Locators.** Four of the five quotations are LOCATOR-WRONG. "individuals tend to either assign responsibility…", "some hosts tend to diffuse responsibility to the platform…", "collective responsibility is difficult to establish…" and "an extension of their moral self … amoral hosts…" are all on **AM p. 16**, not AM p. 14. I checked this in both `f.txt` (printed page footer "16") and `paged.txt`. The abstract quotation (AM p. 1) is a MATCH. WS_H3 §3 carries the wrong locator forward ("2019, AM p. 14").
- **Read-depth note.** The source_basis says only AM pp. 1–2 and 13–14 were read and that methods were "not read closely". That reading missed the shared sample noted under Kaniadakis. The content of the quotations is accurate; the verdict rests on the locators.

### pittrivers2012law: PASS-WITH-NOTES

- **Identity.** Matches Crossref: HAU 2(1) 501–517, issued March 2012.
- **Quotations.** All 16 MATCH at the HAU pages given. My check restored "c1aims" to "claims" and read the ‗ ‘ marks as quotation marks; I found no other alteration. Wording: the beggar passage on p. 509 drops a footnote marker ("stranger.18") without comment, which is acceptable.
- **The 1977 bracketed pages.** The publisher's note says the bracketed numbers give the original pagination. The markers run [94], [96], [97] … [112], with no [95]. Word counts between markers settle what the markers mean. The text from [94] to [96] is about 501 words, one page, the same as every other interval. So each marker opens a page, and the first marker is a misprint for [95]. On that reading, every bracketed page on the card is right except one: the "dissatisfied guest … without showing any discourtesy … To complain openly…" quotation is wholly on 1977 p. 107. The card's [1977: 107–108] should read 107; [108] begins after "refusal".
- **Unsupported statement in the Summary.** The Summary says the essay was "first published in 1968 under a longer title". Nothing in the saved source says this; the publisher's note names only the 1977 *Fate of Shechem*, pp. 94–112. WS_H4 records the same: "I could not confirm 1968". Either source the 1968 claim or remove it.
- **Synthesis.** The card's reading that guests may not press claims (pp. 509, 513–515) is supported by the text as quoted. Its Lineage line also checks out: Lugosi 2009 (section "Hospitality") and Golubovskaya et al. p. 1286 both match.

### hewagama2019empowerment: PASS-WITH-NOTES

- **Identity.** Matches Crossref: IJHM 81, 73–82, August 2019, four authors.
- **Quotations.** All 4 match the Semantic Scholar abstract word for word. The source has a curly ‘staircased’.
- **Beyond the abstract.** Nothing substantive is attributed beyond the abstract. One small step: the Critical notes say recovery authority "escalates". The abstract says "stage-managed and 'staircased' … deliberately graduated according to rank". "Escalation", here and in WS_H4, is a gloss and should be marked as one.

### hales1998empowerment: PASS

- **Identity.** Matches Crossref: IJCHM 10(3) 88–95, 1 June 1998.
- **Quotations.** All 4 match the OpenAlex abstract word for word, including the "if" (sic).
- **Beyond the abstract.** The choice/voice-to-case/rule parallel is correctly marked as the paper's own move, not Hales and Klidas's.

### lugosi2009production: PASS-WITH-NOTES

- **Identity.** Matches Crossref: *Space and Culture* 12(4) 396–411.
- **Quotations.** All 11 MATCH the saved manuscript, and every section locator is right: "Hospitality" (l. 122ff), "Normative dimensions…" (l. 437ff), "Situational dimensions…" (l. 546ff).
- **Version.** The manuscript's cover calls itself the "accepted post-review version", but Unpaywall classes the Bournemouth copy as "submittedVersion". I could not reach the version of record (SAGE, closed), so the published wording is unchecked. Every quotation needs a check against the VoR, with page numbers, before it enters the paper.

### candea2012return: PASS

- **Identity.** Matches Crossref: JRAI 18(S1), June 2012, no page field.
- **Quotations.** Both match the OpenAlex abstract word for word.
- **Beyond the abstract.** Nothing is attributed beyond the abstract.
- **Note for the bib.** `references.bib` l. 1148 gives pp. S1–S19, which Crossref cannot confirm.

---

## Upgraded cards (rr-2026-11-h material only)

### germannmolz2018scale: PASS

The two p. 243 quotations ("Airbnb is not in the hospitality business…" and "because Airbnb is a platform that connects people…") MATCH. PDF p. 15 is printed p. 243. The card correctly marks the first as the author's gloss on Srnicek's "lean platform".

### bosma2022platformed: PASS-WITH-NOTES

All four new quotation sets MATCH on printed p. 601 (PDF p. 8) and p. 605 (PDF p. 12); PDF p. 1 is the UvA cover. Three nuances need care, in the card and in WS_H3:

1. **Whose words.** "'host' might refer to … 'primary hosts' …" and the co-host "help[s] listing owners…" are Bosma quoting the Airbnb Help Center. The card says so; WS_H3's "Airbnb distinguishes…" is fine.
2. **Hedge dropped.** The source says the integration "suggest[s] that Airbnb is willing to further decentralize the figure of the host". WS_H3 drops the hedge: "the platform 'decentralize[s]' the figure of the host".
3. **Condition dropped.** Self-check-in is "required by Airbnb" only "to be eligible for business travelers". WS_H3's "Required self-check-in" drops that condition.

The paraphrase that co-hosts take instructions from the app is supported: Irena "did not receive instructions from Thomas but from the Airbnb app" (p. 601).

### didomenico2007host: PASS-WITH-NOTES

- **Quotations.** The four new quotations MATCH at pp. 332, 333, 334 and 335. PDF p. 2 is printed p. 321.
- **Is the "necessary but not sufficient" inference flagged?** In WS_H4, yes, clearly: "My inference, not theirs". On the card it is ambiguous. The card closes the H4 analysis with "This is the authors' inference from pp. 333-335, not the source's". On a card about Di Domenico and Lynch, "the authors" will be read as Di Domenico and Lynch, or as the manuscript's authors. It is neither: it is the H4 workstream's inference. Change it to "H4's inference (Claude, rr-2026-11-h)".
- **Stretched wording in "Where it enters".** The card says "the authors locate the licence in the hotel (p. 333)". The hotel contrast comes from the researcher's note ("in a hotel one might complain"). The authors' own sentence only asks whether a home is "closer to private home or hotel". "Licence" is the workstream's term.
- **What the evidence is.** The card's point 1 is right that the silence rests on a single observational note (p. 333).

### golubovskaya2017meaning: PASS

All new items MATCH at the pages given. PDF p. 1 is printed p. 1282.

- p. 1286: the Lashley quotation, the King paraphrase, and "the host can also take advantage…".
- p. 1295: "standardized procedures…" and P-22.
- p. 1297: P-15.
- p. 1298: P-9 and the "contradict King's (1995) proposition" sentence.

The card correctly marks the King and Lashley wording as secondary, and the p. 1297 manager wording as one participant's (P-7) report of what a manager said.

### beatty2016compliance: PASS-WITH-NOTES

The new p. 167 sentence, the truck-ride example (Nick), and the two p. 169 quotations MATCH. One figure needs its denominator. Table 6 (p. 168) is titled "Noncompliance Situations". The 81.0% is 51 of the 63 *refused* knowledge-deficiency requests in pest control that were refused for policy or legal reasons. It is not a share of all knowledge-based requests. The card's "refused for policy or legal reasons in 81.0% of such cases" should say "of refused knowledge-based requests".

### slattery2002finding: PASS-WITH-NOTES

The four new quotations MATCH: p. 24 (PDF p. 6) and p. 25 (PDF p. 7). The R3.9 reading says pp. 24–25 "locate the decisions that govern a venue … at the level of the chain" and describe "where authority sits". That is an inference: Slattery writes about corporate management priorities (chains, brands, portfolio, chain supply), not about frontline authority or decisions. Mark the reading as the workstream's.

### xiang2022covid: PASS-WITH-NOTES

All four new quotations MATCH the PMC text, and their section locators are right:

- Discussion: "puts other people at risk…".
- "Group boundary: insider and outsider": "clear group boundary…".
- "Performance pathways: managing ritual violations": C14 and H8.

One reading needs a marker. The H8 quotation ("the only thing we can do…") comes from a passage about staff keeping their composure while guests shout at them. Reading it as frontline staff "cannot alter the rule" is an inference. The card's own caveat, that the rules were imposed by the state, covers most of this.

### lugosi2014hospitality: PASS-WITH-NOTES

The re-fetched OpenAlex abstract matches. The H4 note is accurate except on two points:

1. **Wording.** "Organisational members" is not the abstract's wording. The abstract has "multiple stakeholders", "external stakeholders" and "various stakeholders".
2. **"Adds no guest-side content" is arguable.** The obligations "to conform to organizational norms and to reciprocate" appear in the part of the abstract about hospitality "extended to … external stakeholders". That is the part of the argument that could cover guests.

---

## WS_H3_multi_actor.md: quotations, locators and inferences

- **The wording the brief asked about.** The WS does say "the draft can say 'a court has held', not 'courts hold'" (§3), and it says "a located instance of a court holding" (§4). Two places drift from that wording:
  - **The proposed claim `host-by-holding-out` (§5)** reads as a general rule: "the party answerable to the guest is the one that held itself out … the party in control performs the duties". It names `crinkley1988holiday` as its carrier, but *Crinkley* does not support the split. The owners and TRAVCO, the parties in control, were held liable to the guests too (para 9). Holding out added a party who answers; it did not move the answer away from the controller. "Holding out fixes who answers; control fixes who performs" (§4 Net) is H3's own proposal and should be labelled that way, with the jurisdiction caveat in the claim text itself.
  - **"The court held the brand answerable … for a property it neither owned nor ran" (§3).** "Nor ran" overstates the holding; see the Crinkley card above (para 51).
- **"The court gave three reasons" (§3).** The third bullet, the footnote 3 distinction of a guest whose employer required the stay, is a limit on the doctrine, not a reason for the holding.
- **Crinkley locators.** paras 7 and 49–52, fn 3 and para 58 are all correct. Reporter pages are mapped above.
- **Filatova-Bilous.** pp. 3, 8 and 13 MATCH (p. 13 begins on p. 12). §3 correctly flags the hotel/platform parallel as "my synthesis". §4 then drops the flag: "Filatova-Bilous shows that the same appearance test operates for platforms". The author shows a subjective test for platforms; calling it "the same" test is H3's inference.
- **Germann Molz.** pp. 243 and 245: MATCH.
- **Kaniadakis and Farmaki.** Kaniadakis pp. 2, 14 and 16: MATCH. Farmaki "AM p. 14": LOCATOR-WRONG, the correct page is AM p. 16.
- **Cobbe et al.**
  - Locators (arXiv) pp. 2, 7, 8, 9 and 10: MATCH; proceedings pages are in the Cobbe table above.
  - The vendor "positions itself as a processor": supported by p. 8 ("claiming in their service agreements to be processors").
  - "Allocation should follow factual control": the normative step is the WS's own, not Cobbe et al.'s (see the Cobbe card).
- **Bosma.** pp. 601 and 605: MATCH, but the WS drops the hedge "willing to" and the business-traveller condition on self-check-in.
- **Chang et al. 2022, AM p. 4.** The words match, but "quoting Wu et al. 2019" is wrong. Chang paraphrases and cites Wu, with no quotation marks.
- **Abstract-level quotations of uncarded sources.**

  | Source | Quotation | Status |
  |---|---|---|
  | Whalen and Sisson 2022 (*Research in Hospitality Management*, DOI 10.1080/22243534.2022.2133172) | "most travellers do not understand the difference…" | MATCH (OpenAlex abstract) |
  | Davies et al. 2020 (JST, DOI 10.1080/09669582.2020.1838526) | "an uneven risk burden…" | MATCH |
  | Liu et al. 2026 (*J. Consumer Behaviour*, DOI 10.1002/cb.70226) | "high-severity service failures" | MATCH |
  | Terry and Huan 2019 | "largely" | UNVERIFIED: I found no record |
  | van Ginneken et al. 2019 | "Misunderstandings of the hotel management agreement…" | UNVERIFIED: no record found |
  | Malkin and Voon 2007 | "commercial hosts owe a duty of care…" | UNVERIFIED: no record found |
  | Emerson 2019 | consumer-survey claim | UNVERIFIED: no record found |
  | Hancock et al. 2008 | "host responsibility" | UNVERIFIED: no record found |

  The WS itself labels all of these abstract depth. Do not let the five unverified ones into the draft until someone fetches a record.

## WS_H4_guests_negotiation.md: quotations, locators and inferences

- **Pitt-Rivers.** Every quotation and HAU page is correct: pp. 504, 509, 513, 514, 515, 516 and 517. "making himself at home" and "giving orders to the dependants of his host" are on p. 515. "practically rather than morally" is on p. 504.
- **Shryock.** Both quotations MATCH: "The good host is graceful; the bad guest is an ingrate" (p. S22) and "refuse to accept the proper role of host or guest" (p. S30). Two attributions are loose:
  - The WS calls them "Shryock's Bedouin material". The S22 sentence is Shryock's general gloss, which leads straight into Pitt-Rivers ("These simple insights underlay the rules … Pitt-Rivers explored"); it is not Bedouin evidence.
  - At S30 the subject is "Bad guests and hosts", not bad guests alone.
- **Golubovskaya et al.** pp. 1286, 1297 and 1298: MATCH. The WS correctly marks King and Lashley as secondary. "A manager tells hotel staff…" compresses an employee's (P-7's) report of what a manager said.
- **Xiang et al.** The section locators MATCH, and so do "after repeated communications", "with hotel management" and "the general manager and the group head office".
- **Di Domenico and Lynch.** pp. 332–335: MATCH.
  - The p. 333 inference is flagged as the workstream's own ("My inference, not theirs"), as the brief requires.
  - The licence for complaint, "in a hotel one might", is the researcher's note.
  - The "paying guest" sentence is on p. 335, as stated.
- **Lugosi 2009.** Both section locators MATCH; the version of record is unchecked.
- **Hewagama and Hales.** Both are quoted within their abstracts. "Escalation" is a gloss on "staircased".
- **Beatty and Slattery.** Beatty pp. 159, 167 and 169: MATCH. Slattery pp. 24–25: MATCH, but "authority" is an inference (see the Slattery card).
- **Manuscript lines.** `DRAFT.md` l. 37 ("Neither asks what, if anything, a guest owes a commercial host."), PO l. 73 ("In a face-to-face welcome all four sit in one person.") and PO l. 77 ("the guest's authority to address claims") are all quoted exactly.

---

## Table: FAILs and every quotation that is not MATCH

| Card / file | Item | Status | Correct value |
|---|---|---|---|
| farmaki2019selfperceptions | "individuals tend to either assign responsibility…" | LOCATOR-WRONG | AM p. 16 (card: p. 14) |
| farmaki2019selfperceptions | "some hosts tend to diffuse responsibility to the platform…" | LOCATOR-WRONG | AM p. 16 |
| farmaki2019selfperceptions | "collective responsibility is difficult to establish…" | LOCATOR-WRONG | AM p. 16 |
| farmaki2019selfperceptions | "an extension of their moral self" / "amoral hosts…" | LOCATOR-WRONG | AM p. 16 |
| farmaki2019selfperceptions | card verdict | **FAIL** | four of five quotation locators wrong; propagated into WS_H3 |
| WS_H3 §3 | Farmaki "(2019, AM p. 14)" | LOCATOR-WRONG | AM p. 16 |
| pittrivers2012law | "the guest who is dissatisfied … To complain openly…" | LOCATOR-WRONG (minor) | HAU pp. 513–514 correct; 1977 p. 107 only (card 107–108) |
| filatovabilous2021platform | "focuses not on the way…" | LOCATOR-WRONG (minor) | pp. 12–13 (card p. 13) |
| WS_H3 §3 | Chang et al. "operate for 24-hours with no human staff…", "quoting Wu et al. 2019" | MATCH, but the attribution is wrong | Chang paraphrases and cites Wu; there is no quotation |
| WS_H3 §3 | Terry and Huan "largely"; van Ginneken; Malkin and Voon; Emerson; Hancock | NOT-FOUND (no record found by me) | abstract-only claims, unverified |
| crinkley1988holiday / WS_H3 | "a property it neither owned nor ran" (not a quotation) | inference beyond the source | majority: brand "retained a significant degree of control over the operation" (para 51, 844 F.2d at 166) |
| didomenico2007host | "This is the authors' inference…" | inference attribution ambiguous | H4's (Claude's) inference, not Di Domenico and Lynch's |
| cobbe2023understanding / WS_H3 | "allocation must / should follow factual control" | inference presented as the source's | Cobbe et al. report the CJEU data-protection rule (p. 8 = 1193) |

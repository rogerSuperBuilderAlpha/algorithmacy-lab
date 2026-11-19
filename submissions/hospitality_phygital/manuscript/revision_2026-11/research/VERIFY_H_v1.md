<!-- Verification report, run rr-2026-11-h, 10 Nov 2026. Written by Claude (Opus 5.5) under VERIFY_BRIEF.md with the run-h changes. No card or other file edited. Nothing committed. -->

# VERIFY_H_v1: verification of rr-2026-11-h cards and the H2/H5 syntheses

Scope: 11 new cards; the rr-2026-11-h lines of 2 upgraded cards; every quotation and locator in `WS_H2_delegation_standing.md` and `WS_H5_boundaries.md`. The v4 text checked is `manuscript/DRAFT.md`, and the outline is `PITCH_AND_OUTLINE.md`. No new card carries a v4 support verdict. Neither document cites any of the new sources, so the step-4 checks below are against the cards' "Where it enters" claims and the WS syntheses.

Method: I re-fetched Crossref for all 13 DOIs (plus papa.12054 and cjlj.2026.10074). I re-fetched the OpenAlex abstracts for the abstract-depth cards. Every quote was string-matched in the saved text after normalising whitespace, hyphenation and quote marks. I took page locators from the running heads, page markers or printed folios in the saved copies.

**Totals: 6 PASS, 7 PASS-WITH-NOTES, 0 FAIL.**

---

## woodland2013uksc — PASS-WITH-NOTES

- **Identity.** The National Archives PDF title page gives "[2013] UKSC 66", "On appeal from: [2012] EWCA Civ 239", judgment given 23 October 2013, Lord Sumption (Clarke, Wilson, Toulson agreeing) and Lady Hale (same three agreeing). That matches the card. "[2014] AC 537" is confirmed in Morgan's AM n. 1 (`morgan.txt` l. 50), as the card says. The PDF has 26 pages and the last printed folio is 25, so the card's "25 printed pages" is fine.
- **Depth.** `woodland.txt` holds the full judgment, paras 1–43, so `full-text` is honest.
- **Quotes.** All 13 card quotes MATCH at the stated paragraphs: 5, 7 (×4), 11, 12 (×2), 23(2), 23(3), 24 (×2), 25(1), 25(3), 34, 42. The Photo Production and Morris v C.W. Martin citations are both in para 7. A full-text search finds no "inn", "innkeeper" or "hotel", so the card's negative claim holds.
  - One PARAPHRASED-AS-QUOTE: the card has the exception that would "eat up the rule" (para 22). The judgment says "eating up the rule" (para 22).
- **Scope (look-hardest item).** The card handles scope correctly. Para 23(1) limits the category to a claimant who is "a patient or a child, or for some other reason is especially vulnerable or dependent", and the card says to borrow the structure only. Paras 7 and 23–25 support the structure: performance can be delegated, the duty is retained, and its ground is the assumed responsibility. Nothing in the judgment says that hotels owe such a duty.
- **Kong contrast.** The card's "not strictly opposed" is right, and it is narrower than WS_H2 makes it (see WS_H2, finding 2).

## thompson2004wrong — PASS-WITH-NOTES

- **Identity.** Crossref gives book chapter, *Reason and Value*, pp. 333–384, issued 2004-03-04, ISBN 9780199261888.
  - **Year (look-hardest item): 2004 is correct.** OpenLibrary lists the hardback, ISBN 9780199261888, Clarendon, 19 March 2004. "2006" is the paperback, ISBN 9780199297641, published 22 May 2006. The card's "check the imprint" note can be closed.
  - Crossref carries no editors. The card's editor list is unverified against a record but is standard.
- **Depth.** The saved PDF is the publisher's typeset file: its title metadata is "014 333..384", it was produced with 3B2 and created in 2003, and it carries the running heads. `full-text` is honest, and the printed pages are reliable.
- **Quotes.**
  - **p. 335 (look-hardest item): MATCH.** The tabulated forms, "forms of bipolar normativity, or forms of relation of right", and "express Hohfeldian 'claim' and 'privilege' respectively" are all on p. 335.
  - **MATCH:** p. 338 (monadic forms; Bentham/"dikaiological"), p. 352 ("A dikaiological order is simply…") and p. 355 ("Lawyers speak of corporations…").
  - **LOCATOR-WRONG:** the card's non-reduction quotes are marked "pp. 338–339, page break after p. 338". Both "is not reducible to the bipolar in any straightforward way" and the Rawls/promisee sentence are on **p. 339**.
- **Cross-card locator.** The critical note says Thompson's "key" at p. 352 "is the source Darwall quotes … (darwall p. 28)". It is not. Darwall cites "Thompson 345–6", where Thompson writes "shifted into various gears, or sung in various keys" across pp. 345–346. The p. 352 sentence is a different one.
- **Inference marking.** The card correctly marks as its own reading the claim that none of the forms mentions answering.

## morgan2015liability — PASS

- **Identity.** Crossref matches: CLJ 74(1), 109–139, March 2015.
- **Depth.** The AM is 24 pp. and is full text.
- **Quotes.** All six MATCH at the AM pages given: p. 7 ("very misleadingly…", where the source breaks the line at "non-\ndelegable", and the contractual "duty of care"), p. 8 ("Engagement…", "exceptionaly" sic, "more accurately a duty to ensure…", "arguably a misnomer" in n. 55) and p. 1 (outsourcing).
- **Locators.** AM pages are not journal pages, and the card says so.

## liau2023standing — PASS

- **Identity.** Crossref matches: OUP 2023, ISBN 9780192869661.
- **Depth.** Only the Introduction was read, and `abstract` with the flag is the conservative label.
- **Quotes.** All seven MATCH at eprint pp. 1, 1, 2, 5, 5, 7 and 4. The "general standing rule" box on p. 5 interleaves the label "A General Standing Rule" mid-sentence, but the words are exact.
- **Terminology warning.** The warning that Liau's "standing" is the enforcement power is correct, per pdf pp. 1 and 5.

## cornell2025wrongs — PASS-WITH-NOTES

- **Identity.** Crossref 10.2307/jj.21275861 gives issued 2025-03-04. However, 10.4159/9780674245037 gives issued 2024-10-25 (online), and OpenAlex gives 2024 for both. The year is ambiguous between 2024 and 2025: settle it against HUP's imprint before citing.
- **Depth.** `abstract` is honest. There is **no saved source for this citekey**. The only related folder is `sources/cornell2015wrongs/`, whose `cornell.pdf` is a 620-byte Internet Archive bot-block page saved as HTML text, not a PDF. The card does not claim a saved copy, but its "read via OpenAlex" abstracts were not archived.
- **Quotes.** I re-fetched all abstracts from OpenAlex.
  - Book: both quotes MATCH. "to be wronged … is to have one's rights violated" elides "we think", which is acceptable.
  - papa.12054: MATCH.
  - Bradley 2026: MATCH.

## hardimon1994role — PASS

- **Identity.** Crossref gives J. Phil. 91(7), first page 333 only. End page 363 is confirmed in Moreau ms n. 6 (`moreau.txt` p. 6: "pp. 333-63, p. 338").
- **Depth.** `metadata` is honest, and no quotation from Hardimon is recorded.
- **Moreau quote.** The quote attributed to Moreau MATCHes at ms p. 6 n. 6.

## baum2026constitutive — PASS-WITH-NOTES

- **Identity.** Crossref matches: LNCS, *Bridging the Gap Between AI and Reality*, pp. 115–130, online 2026-10-13. Crossref's print date is **2027**, so decide which year to cite.
- **Depth.** The arXiv v2 text is full and has 15 pp.
- **LNCS version (look-hardest item): not reachable.** On 10 Nov, `link.springer.com/content/pdf/10.1007/978-3-032-41269-0_8.pdf` returned a "Client Challenge" page. I did not bypass it. The other Unpaywall OA copies (arXiv, PhilArchive) are the submitted version. **All quotes are therefore verified against arXiv v2 only.**
- **Quotes.** All 10 card quotes MATCH in arXiv v2 at the stated pages:
  - p. 3: gate/switch.
  - p. 4: Def. 1, split across a hyphen break.
  - p. 6: synchronous; "synchronous with latency…"; "Only synchronous HOTL…".
  - p. 7: asynchronous/anticipatory.
  - pp. 7–8: braking. The "constitutes anticipatory HOTL" clause is on p. 8.
  - p. 2: descriptive and normative conditions; capacities, information, authority.
  - p. 11: Art. 22 comparison.
  - p. 12: Def. 3.
- **Citations inside Baum & Laux.** SCHUFA is at p. 4. Santoni de Sio and van den Hoven appear at p. 12 n. 12 (ref. [20]), as WS_H5 says.

## gdpr2016art22 — PASS-WITH-NOTES

- **Identity.** The OJ L 119, 4.5.2016 details are confirmed in the saved Cellar text.
- **Quotes.** All four MATCH: Art. 22(1), 22(2)(a), 22(3) and Recital 71.
- **Inference.** The summary's "The safeguard is after the decision" is a reading. Art. 22(3) gives the right "to obtain human intervention … and to contest the decision" and does not state timing. Mark it as inference.
- **WS_H5 overreach.** The same applies to the claim in WS_H5 that booking, check-in and pricing are "contractual". Art. 22(2)(a) requires the decision to be "necessary for" the contract.

## article292018guidelines — PASS-WITH-NOTES

- **Identity.** Confirmed: WP251rev.01, adopted 3 October 2017, last revised 6 February 2018, 37 pp.
- **Source folder.** The copy is at `sources/wp29_2018adm/`, not `sources/article292018guidelines/`. The card discloses this.
- **Quotes (look-hardest item: pp. 21, 22, 27).** All seven MATCH, and the printed folios equal the PDF pages:
  - p. 21: "token gesture"; "cancellation of a contract"; significance bullets, which form a list rather than one sentence, an acceptable join.
  - p. 22: pricing; vulnerable groups.
  - p. 23: "Routine human involvement…".
  - p. 27: "Any review…".
- **Overreach in "Where it enters".** The card says "refusal or cancellation at the door is a legal effect on the regulators' reading".
  - WP251 p. 21 lists "cancellation of a contract", which covers a booking that is not honoured. Its "refused admission" example is admission *to a country*. A walk-in refused at the door is therefore not covered by the regulators' examples.
  - The card also says ordinary dynamic pricing "is not" significant. WP251 says only that pricing "could" be significant if it bars access, and makes no negative claim.
- **Unverified.** The note on EDPB endorsement is flagged as from memory and remains unverified.

## ivanov2024automated — PASS

- **Identity.** Crossref matches: *Technology in Society* 76, art. 102430, March 2024. OpenAlex gives 2023, the online year.
- **Depth.** `abstract` is honest. The saved folder holds metadata records only.
- **Quotes.** All four abstract quotes MATCH the OpenAlex abstract. The Ivanov (2023) *foresight* abstract quote in the critical notes also MATCHes (OpenAlex, 10.1108/FS-09-2021-0183).
- **Scope.** Nothing beyond the abstract is attributed to the source.

## tang2018timing — PASS

- **Identity.** Crossref matches: JSM 32(6), 755–766.
- **Quotes.** All three abstract quotes MATCH.
- **Jin et al. (2019).** The card's side-claim about Jin et al. (2019) is unverified. OpenAlex has no abstract for 10.1016/j.jhtm.2019.01.005, and the card says it was seen in Consensus only.

## darwall2013bipolar (rr-2026-11-h lines only) — PASS-WITH-NOTES

- **Quotes.** All four new quotes MATCH in `b_clean.txt`:
  - The OSO abstract precedes p. 20, as labelled.
  - p. 21 is the line directly after the (p.21) marker.
  - p. 35: "need not actually claim…".
  - p. 36: "(standing to address claims and demands and hold accountable)".
- **Is the "circularity" reading fair to Darwall? (look-hardest item) Partly.**
  - **Fair.** Darwall builds accountability authority into the bipolar relation. The abstract defines it that way, and p. 34–35 says: "Part of what it is for an obligor to have a moral obligation to an obligee … is that the obligee has a set of individual authorities to claim the right and hold the obligor personally responsible". Treating this as an instance of Bradley's OAN is fair.
  - **Not fair.** Darwall is not circular. He analyses bipolar obligation *in terms of* accountability, in one direction only. The loop appears only if the paper *also* defines accountability through standing. Threat 3 on the card says this correctly ("is reproduced"). WS_H2 §3.2 does not (WS_H2, finding 1).
  - **p. 35 needs its continuation.** The p. 35 concession comes with a qualifier that runs into p. 36: "Even so, a connection to the discretionary individual authorities we have discussed is surely part of the concepts of bipolar moral obligation and claim right". So p. 35 supports *held without being claimed*. It does not support *defined without accountability*. Do not cite p. 35 for the second claim.
  - **Scope of the p. 36 gloss.** The gloss covers both individual and representative authority, so it is not specific to the bipolar case.

## kropf2026blame (rr-2026-11-h lines only) — PASS

- **Quotes.** All three new items MATCH:
  - p. 2: Vincent's two questions, "[11, p.27]".
  - p. 3: "specific obligations that would not exist without that role".
  - p. 4: "only becomes a role-specific duty…"; and n. 3, "expands positive duties", which is in footnote 3 on p. 4.
- **Second-hand caveat.** The card correctly says the Vincent material is second-hand.

---

## WS_H2_delegation_standing.md: quotations, locators, inferences

**Quotes and locators.** Every quote MATCHes at its locator:
- Woodland: paras 7, 11, 22, 23(1)–(3), 24, 25(1), 25(3), 34.
- Morgan: AM pp. 7, 8.
- Thompson: pp. 335, 338, 352, 355.
- Darwall: OSO abstract, pp. 35, 36.
- Liau: pdf pp. 1, 5, 7.
- Kropf: pp. 2, 3, 4 n. 3.
- Kong: p. 4, "guidance control over the act of delegation".
- Bradley: abstract.

Two further points:
- Woodland paras 14–16 do concern hospitals (Gold, Cassidy), as claimed.
- I confirmed only that pages 450 and 452 of Bovens exist in the saved copy. I did not check them against the actor/forum content.

Findings:

1. **Overstated: "The circle R2.3 found is inside the paper's main source."** Darwall's definition is not circular. It puts accountability into obligation, in one direction only. The circle arises when the paper adds the converse. Suggested framing: "Darwall's definition builds in the accountability that the paper then defines through standing" (see the Darwall card above).
2. **Overstated: "Woodland holds the reverse" of Kong.**
   - The WS's own card says the two are "not strictly opposed".
   - Kong p. 4 says that *assuming* a role "is itself an exercise of control".
   - Woodland grounds the duty in an *assumption* of responsibility (para 11), and it still treats "control over the claimant" as the essential element (para 24; para 23(2): such relationships "involve an element of control over the claimant").
   - The difference is real but narrower: control of the environment or of the act versus a relation of charge over the person.
3. **The Woodland scope breach is the one the brief warned about.** The §3.3 diagnosis says "the guest still *holds* standing (2), because the host's obligation persists [woodland para 7]". Para 7 says nothing about hosts. As written, it cites Woodland for the claim that a hotel's duty persists. It should be marked as the paper's application, consistent with the WS's own "Limits" paragraph.
   - Table row 1 is correctly hedged ("the application to hosting [is] the paper's own").
   - §4's "Public calling (B) gains a bridge" is likewise hedged.
4. **Misapplied Thompson.** The WS contrasts "a hotel's general obligations (to a regulator, say)" with its duty to the guest, as monadic against bipolar (p. 338). A duty owed *to* a regulator is bipolar in Thompson's form, because it names an obligee. The card's wording, "duties (e.g., to comply with regulation)", avoids this. Use it.
5. **Inference stated as the source's claim: "Thompson supplies the relation without the accountability."** The card marks "none of the forms mentions answering" as its own reading of the table. The WS states it as Thompson's position. It is a fair reading, but it should be labelled.
6. **Inference stated as the source's claim, on Cornell.** The WS says Cornell argues "that rights and the accountability practices that follow wrongs are 'fundamentally distinct'". The publisher abstract says "wrongs and rights" are fundamentally distinct. "Accountability practices" is Bradley's gloss, from his abstract. Attribute it to Bradley.
7. **Unverified fact.** The WS says "Swimming Teachers Association" was "the first-instance name". The saved judgment does not show the lower-court title. As far as I know, the Court of Appeal decision ([2012] EWCA Civ 239) carried that name, but I did not verify it. Treat the note as unverified.
8. **Correctly labelled.** The perform-versus-arrange application to platforms is labelled as inference.

## WS_H5_boundaries.md: quotations, locators, inferences

**Quotes and locators.**
- **Baum & Laux.** All quotes MATCH. Def. 1 is on p. 4, Def. 2 on p. 5 and the p. 12 n. 12 citation is correct.
- **GDPR.** Art. 22(1), 22(2)(a) and 22(3) MATCH.
- **WP251.** pp. 21, 22 and 27 MATCH.
- **EU AI Act Art. 14(4)(e), OJ PDF p. 61 (look-hardest item): MATCH.** Art. 14 begins on p. 60, and (4)(e) is on p. 61 of the 144-page OJ PDF. The quote is exact.
- **EU AI Act Annex III 1(a), p. 127: MATCH.**
- **Other sources.**
  - Belanche 2020: 283, "proactively following a robot failure": MATCH. PDF p. 17 is journal p. 283.
  - Schmidt 2025: 571: supports "information provision … without negatively impacting guest experience".
  - Wilson-Nash p. 981, "choose modes of access (e.g., digital, analogue)": MATCH.
  - Ivanov & Webster abstract: MATCH.
  - Lyons et al. 2022 abstract, "and a timely outcome": MATCH.
  - Ivanov 2023 abstract: MATCH.

Findings:

1. **LOCATOR-WRONG: Sterz et al. 2024: 2498.** The organisational "authority" wording, "typically with the authority to influence its operations or effects", is on **p. 2497**. Page 2498 covers causal power and "pseudo-options".
2. **Spliced quote: Recital 71.** The WS says Recital 71 speaks of challenging "the decision reached after such assessment". In the Recital, that phrase belongs to the right "to obtain an explanation of the decision reached after such assessment". The right to challenge follows as a separate item. Quote it as two items.
3. **Inference stated as law.** "Booking, check-in and pricing are contractual, so a hotel's legal floor is after-the-fact review." This depends on the decisions being "necessary for" the contract (Art. 22(2)(a)), and Art. 22(3) does not state when intervention occurs. Mark it as the authors' reading.
4. **Mischaracterised: the AI Act "stop-button duty, the right 'to intervene…'".** Art. 14(4)(e) is not a right of the affected person. It requires that a high-risk system be provided to the natural persons assigned to oversight in a way that enables them, "as appropriate and proportionate", to intervene or interrupt. It confers nothing on a guest.
5. **Unverified: Jin et al. 2019,** "recovery within 30 minutes beat recovery within 2 hours", in hotel vignettes. OpenAlex holds no abstract. Treat it as unverified until the abstract or the paper is read.
6. **Typology.** It is correctly labelled as the agent's inference. It inherits the WP251 overreach noted on the card: refusal at the door is not one of the regulators' "legal effect" examples unless a contract is cancelled.

---

## Table: FAILs and every quote not MATCH

There are no FAILs.

| Where | Item | Status | Correct value / note |
|---|---|---|---|
| woodland2013uksc | "eat up the rule" | PARAPHRASED-AS-QUOTE | Judgment: "eating up the rule" (para 22) |
| thompson2004wrong | "not reducible to the bipolar…"; Rawls/promisee | LOCATOR-WRONG | p. 339, not "pp. 338–339" |
| thompson2004wrong | "Thompson's 'key' (p. 352) is the source Darwall quotes" | LOCATOR-WRONG (cross-ref) | Darwall cites Thompson pp. 345–6 ("sung in various keys") |
| WS_H5 | Sterz et al. 2024: 2498 (authority) | LOCATOR-WRONG | p. 2497 |
| WS_H5 | Recital 71, "challenging 'the decision reached after such assessment'" | PARAPHRASED-AS-QUOTE (splice) | The phrase attaches to the right to an explanation |
| WS_H2 | Cornell, rights and "accountability practices" "fundamentally distinct" | Inference attributed to source | Abstract: "wrongs and rights"; "accountability practices" is Bradley |
| WS_H2 | "host's obligation persists [woodland para 7]" | Inference cited to source | Woodland says nothing about hosts or hotels |
| WS_H5 | Jin et al. 2019, 30 min vs 2 h | NOT VERIFIED | No abstract retrievable |
| baum2026constitutive | all quotes | MATCH (arXiv v2 only) | LNCS 2026 PDF behind a Springer bot challenge, not bypassed |

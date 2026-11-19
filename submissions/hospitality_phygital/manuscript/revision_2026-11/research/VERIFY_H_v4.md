<!-- Drafted by Claude (Opus 5.5), 10 Nov 2026, run rr-2026-11-h, verification pass v4 (debts run). Not the authors' wording. No file other than this report was edited. -->

# VERIFY_H_v4: verification of the debts run (WS_DEBTS.md)

Run rr-2026-11-h, 10 November 2026. Brief: `research/VERIFY_BRIEF.md`, adapted. The v4 text is `manuscript/DRAFT.md`. Scope: the two new cards, the Cobbe version-of-record conversion, the eight other cards the debts run touched (commit 00e7a3c), and WS_DEBTS.md, including its 17 verdicts on HOST_DUTIES_SYNTHESIS.

Method. I fetched Crossref records for both new DOIs and tested both NISC DOIs at doi.org. I matched every quotation against the saved `pdftotext` output, page by page. The normalisation covered quotes, dashes, ligatures, hyphenation and whitespace only. For Cobbe, I re-extracted both PDFs in reading order (the saved `vor.txt` is in layout mode, so phrase search fails on it) and split them on form feeds. For the touched cards, I read the debts-run diff of each card in commit 00e7a3c. The sources I read are `sources/lashley2015hospitality/paged.txt`, `sources/blain2014hospitableness/paged.txt`, and the two Cobbe PDFs.

Counts: **PASS 8 · PASS-WITH-NOTES 5 · FAIL 0** (13 sections: 11 cards, including `lugosi2009production`, which the commit also touched; WS_DEBTS; the Cobbe conversion is reported inside the Cobbe card section).

---

## lashley2015hospitality

**PASS-WITH-NOTES**

- **Identity.** Crossref 10.1080/22243534.2015.11828322 gives "Hospitality and hospitableness", Conrad Lashley, *Research in Hospitality Management* 5(1), 1–7, 2015. That matches the card and the `references.bib` entry. The printed NISC DOI 10.2989/RHM.2015.5.1.2.1261 returns 404 at doi.org, as the card says.
- **Read depth.** `full-text` is honest. The saved PDF and text contain the whole 7-page article, with journal pagination 1–7 and the reference list.
- **Quotations.** All 12 quotations on the card are MATCH, on the pages the card gives (pp. 1, 1, 1, 3, 4, 4, 5, 5, 5, 6, 6, plus "(Lashley 2000)" on p. 3 and the Figure 1 labels on p. 4).
- **Notes.**
  1. The p. 1 definition of hospitableness ("the willingness to be hospitable for its own sake …") is cited in the source to "Lashley & Morrison 2000, Lashley et al. 2007". The card presents it as Lashley's own definition. Cite it as Lashley's statement of an earlier definition.
  2. The card misses p. 2: "Guests are to be protected by hosts but at the same time, expected not to overstay their welcome, misbehave, or endanger the hosts (O'Gorman 2007a)". This bears on R3.10 and on the "behave reasonably" half of King (see WS_DEBTS below).
  3. The "only so long as they could pay the price" remark (p. 1) is cited to Ashness & Lashley 1995. The p. 5 sentence on withdrawal for non-payment is cited to Ward & Martins and Ritzer, and Lashley immediately reports Telfer calling that view "somewhat simplistic". The card's own critical note handles this correctly ("a critical remark … not a statement of what the guest owes").

## blain2014hospitableness

**PASS-WITH-NOTES**

- **Identity.** Crossref 10.1080/22243534.2014.11828307 gives the title as on the card, Matthew Blain and Conrad Lashley, *RHM* 4(1-2), 1–8, 2014. That matches the card and the bib. The printed NISC DOI returns 404.
- **Read depth.** `full-text` is honest. All eight journal pages are present, with the abstract, Table 1 on p. 7 and the conclusion on p. 8.
- **Quotations.** All 11 Key-facts quotations are MATCH on the pages given: p. 1 ×4; p. 2 ×5, including Telfer (39) and (42); p. 3 for Telfer (40); p. 7; p. 8. The "Guests are offering hospitality because they are obliged" slip is on p. 2, as the card notes.
- **The p. 1 obligation sentence, in context.** The quotation is exact. Its context narrows what it can carry:
  - It follows "Using this metaphor, the visitor, as a guest, is entering the host's space". The obligation belongs to the *hosting metaphor*.
  - The next sentences frame it as an approach: "This approach is founded upon deep-rooted traditions of hospitality, and provides a model for building long-term customer loyalty beyond the somewhat simplistic advocacy of the 'service culture'" (p. 1). It is offered as a service model for firms, not argued as a duty.
  - The abstract ties the unconditional welcome to motive: "Guests are unconditionally welcomed by hosts driven by altruistic motives" (p. 1).
  - On p. 2 the obligation is one "accepted by hosts", not assigned to them: "there is an obligation, accepted by hosts, to care for and protect guests".
- **Scope (tour guides, air stewards).** The quotation is exact, but it is hedged: host–guest relationships "can be seen to apply" to these roles (p. 1). The instrument was developed with domestic dinner-party hosts (Lashley 2015, p. 6) and a brewery (Blain and Lashley p. 7: "a brewery that hosted the research"). No service-role holder was studied. So the scope claim describes the metaphor's reach, not the paper's evidence.
- **Ellipsis in `hold_rationale`.** "'the chief responsibilities ... lie with hosts' (p. 1)" drops "which concern us here". That is a scope qualifier: the authors say the responsibilities *they focus on* lie with hosts, not that hosts carry the chief responsibilities overall. The Key-facts line quotes the sentence in full. Restore the words wherever the short form is used (also WS_DEBTS item 9).
- **"At odds".** Summary and notes say externally imposed obligation "is treated as at odds with genuine hospitableness". The source hedges: "may be at odds" (p. 2).

## cobbe2023understanding (including the version-of-record conversion)

**PASS-WITH-NOTES**

- **Version of record.** `sources/cobbe2023understanding_vor/ucl_vor.pdf` has 12 pages, printed page numbers 1186–1197 (one per PDF page), the ACM Reference Format block ("12 pages"), a CC BY-NC licence and the DOI. The arXiv v2 copy says "13 pages". Unpaywall (re-queried) labels the UCL file `submittedVersion`, as WS_DEBTS reports. Its typesetting is ACM proceedings, so treating it as the version of record is reasonable.
- **The +1185 conversion.** All 18 Key-facts and Critical-notes quotations are on the stated proceedings page, and on arXiv page = proceedings − 1185 in the arXiv copy:
  - 1187: "group of organisations"; the mechanism definition; "We treat accountability"; "We do not offer" (left column, bottom of 1187, continuing on 1187).
  - 1192: "Responsibility … no one actor in overall control"; "directing governance".
  - 1193: "should thus be allocated"; "Not every actor / Neither / Nor"; "data controllers"; "factual situation"; the AI Act pair; "accountability horizon".
  - 1194: "no actor will have sufficient knowledge".
  - 1195: "Providers disclaim"; "vacuum".
  - The opening "many hands" sentence crosses a column break on 1186, not a page break, as the card says.
- **Synthesis locators (WS_DEBTS item 12).** The conversions are correct:
  - §2.5 "typically no one actor in overall control": arXiv p. 7, now p. 1192.
  - "disclaim" (§2.5 "(p. 10)"): now p. 1195.
  - §3 "Cobbe p. 8" (different actors control different aspects): now p. 1193.
- **Notes.**
  1. A Critical note is now stale: "Locators are arXiv v2 pages … That copy is not in sources/ and Fable did not re-check it". The copy is now in `sources/cobbe2023understanding_vor/` and has been checked.
  2. Critical notes still give arXiv pages ("We do not offer…" arXiv p. 2; the AI Act passage arXiv p. 8), while Key facts give proceedings pages. This is acknowledged in the debts note, but the card's locators are mixed.
  3. Cobbe is not cited in v4.

## king1995what

**PASS.** The debts run added one paragraph, recording the routes tried and noting that neither phrase can be checked. Nothing is attributed to King. Neither new paper cites King: I found no "King" in either reference list. The only hit is King Duncan in Lashley 2015, p. 2.

## lashley2000towards

**PASS.** The added paragraph reports only what Lashley 2015 says:
- the three domains with "(Lashley 2000)" (p. 3);
- the Figure 1 labels (p. 4);
- the "Fundamentally, the actual experiences …" sentence (p. 3).

All three MATCH. The paragraph correctly declines to support "inheriting its meanings" and the valued-customer sentence. `read_depth` stays metadata.

## hewagama2019empowerment

**PASS.** The addition is a routes note only. The Auckland thesis is flagged as a different work. No content was added.

## hales1998empowerment

**PASS.** The addition is a routes note only. I did not re-open the Tilburg portal record it mentions. Nothing about the article's content was added.

## germannmolz2026

**PASS.** The addition is a routes note only, and it restates that nothing beyond the abstract may be attributed.

## hardimon1994role

**PASS.** The addition is a routes note only.

## baum2026constitutive

**PASS.** The addition is a routes note only. I confirmed its Unpaywall claim: Unpaywall gives the status as hybrid, with a Springer PDF labelled `publishedVersion` and PhilPapers BAUCVC-2 as a repository copy. Locators remain arXiv v2, as stated.

## lugosi2009production (touched by the same commit; not on the list)

**PASS.** The addition is a routes note only.

## telfer1995hospitableness

**PASS-WITH-NOTES.** The five added bullets are secondary reports, correctly tagged `[metadata]`. Every quoted string MATCHES on the cited page of Blain and Lashley (pp. 2, 2, 3) or Lashley 2015 (p. 5).

Notes:
1. Bullet 1 puts "the provision of food, drink, and accommodation to those who are not members of a household" inside quotation marks as what Telfer says. In Blain and Lashley (p. 2) these words are *their own paraphrase*: "Hospitality she defines as involving …". There are no quotation marks and no page. Only the "central ides …" phrase (39) is quoted there. This is PARAPHRASED-AS-QUOTE at the level of attribution.
2. The "conflicting report" bullet overstates the conflict:
   - Lashley 2015's list (p. 5) is a bulleted paraphrase, without quotation marks or a Telfer page. He introduces it as "the qualities of hospitableness include the following points".
   - It also has two items absent from Blain and Lashley's quotation ("A desire to have company or to make friends"; "the pleasures of entertaining").
   - Blain and Lashley give a marked quotation with "(42)", introduced by "Principally".
   - So the two are not like-for-like. The quoted version has more evidential weight, though it is still unchecked against Telfer. The card is right that neither can be used as Telfer's words.
3. The closing note says Telfer "places a felt duty among the motives". That rests on Blain and Lashley's quotation alone, and Lashley's list omits it. It should be conditional.
4. Neither source uses "virtue" of Telfer. Grep finds the word only in a reference title in Lashley 2015. The nearest statement is "She places altruistic (genuine) giving of hospitality higher on a moral scale" (Blain and Lashley p. 3). The card's "cannot be said" is correct.

## WS_DEBTS.md

**PASS-WITH-NOTES.** Every quotation from the two new papers is MATCH on the page given. There are two ellipsis or hedge problems (below). Several support verdicts are stronger than the text allows.

### Quotations and locators
- **Lashley 2015.** These are MATCH on the pages given:
  - "only so long as they could pay the price" (p. 1);
  - "would be withdrawn if the payment could not be made" (p. 5);
  - "'cultural', and 'domestic', as well as 'commercial'" (p. 3);
  - "the actual experiences of hospitality …" (p. 3);
  - "Offering guests hospitality has been …" (p. 3);
  - "the duty to provide hospitality …" (p. 4);
  - "the willingness to be hospitable for its own sake …" (p. 1);
  - "A desire to entertain one's friends or to help those in trouble" (p. 5);
  - "offer hospitableness beyond, and in spite of, the commercial transaction" (p. 5);
  - "driven by a personal desire to be hospitable to others" (p. 1);
  - "at a price" (p. 5).
- **Blain and Lashley.** These are MATCH:
  - "beyond bars, hotel and restaurants to include tour guides …" (p. 1);
  - "Most significantly, the host is obliged …" (p. 1);
  - "duties to be hospitable, a duty help one's friends …" (p. 2);
  - "Commercial organisations could benefit …" (p. 2);
  - "welcome and safe, because they experience this desire as a genuine emotion" (p. 2);
  - "has to be unconditional" (p. 1).
- **Hedge dropped (§3).** WS writes: Religious obligations are "at odds with Telfer's notion of hospitableness because the host is behaving in a way that has been externally imposed" (p. 2). The quoted string matches, but the source says the obligations "represent an obligation which *may be* at odds". Restore "may be". The same applies to item 2's "sets externally imposed duty *against* hospitableness".
- **Ellipsis (item 9).** "there are some obligations on guests, the chief responsibilities … lie with hosts" drops "which concern us here". See the Blain card section above.
- **Factual slip (§2, Telfer).** WS says "Two secondary reports with Telfer page numbers". Lashley 2015 gives no Telfer page for his list (p. 5). Only Blain and Lashley do (42).
- **Stale note (§6).** WS says the two new cards fail `build_index.py --check` until `references.bib` entries are added. Both bib entries now exist (`references.bib` lines 3374–3396, added in the same commit 00e7a3c).
- **Cobbe page map.** Correct (see the Cobbe section).
- **The NISC DOI 404s.** Confirmed.

### King's "pay" (§2)
WS says Lashley 2015 "supports the payment half of the King sentence as a description of commercial hospitality". This is overstated.
- King's phrase is about the *guest's obligation* ("only obligation is to pay and behave reasonably").
- Lashley's two sentences describe the *conditionality of the commercial welcome*, voiced as critique. Page 1 is cited to Ashness & Lashley 1995. Page 5 is cited to Ward & Martins and Ritzer, and Telfer is then reported calling it "somewhat simplistic". Blain and Lashley distance the same point further: "For some authors, commercial hospitality involves a financial transaction … withdrawn if the financial payment could not be made" (p. 3).
- Better: *consistent with* a payment condition, not support for King.
- WS also misses that Lashley 2015 has a guest-conduct sentence close to "behave reasonably". Guests are "expected not to overstay their welcome, misbehave, or endanger the hosts (O'Gorman 2007a)" (p. 2). It concerns pre-modern and Shakespearean norms, via O'Gorman, not commercial hosting. So "It does not supply 'behave reasonably'" should read "supplies a guest-conduct norm at second hand (p. 2), not in the commercial setting".

### Telfer p. 42 discrepancy (§2)
The discrepancy is real, but WS frames it as two disagreeing reports of equal standing. Blain and Lashley quote with a page. Lashley 2015 paraphrases in bullets, with no page and two extra items (see the Telfer section). Record it as: the only quoted report includes duties; the later unquoted paraphrase omits them. Check p. 42.

### The 17 entries in "Changes to HOST_DUTIES_SYNTHESIS"

| # | Synthesis sentence | WS verdict | My judgment |
|---|---|---|---|
| 1 | §2.1 heading "a virtue, not a role" | Qualifies | **Agree.** Neither paper uses "virtue". Both speak of motive and desire (Lashley 2015, pp. 1, 5; Blain and Lashley p. 3: "'hospitableness' is simply about motives"). The obligation in Blain and Lashley p. 1 is a feature of the hosting metaphor, offered as "a model for building long-term customer loyalty". |
| 2 | "measures the host's duty as a personal disposition" | Qualifies | **Agree, with the hedge restored.** Externally imposed obligation "may be at odds" with hospitableness (p. 2). The research measures disposition *in place of* duty. |
| 3 | Lashley's instrument quotation | Supports | **Agree.** MATCH, p. 1 (abstract). The sentence ends "to others". |
| 4 | Lashley 2014 editorial | Unchanged; Lashley 2015 p. 3 can replace | **Agree.** For "central feature of human morality", Lashley 2015 p. 1 is closer: "it is one of the defining features of human morality". The abstract (p. 1) has "the universal need to welcome and protect the stranger". Page 3 carries the "lost importance" half. |
| 5 | "H1 found no hospitableness work that assigns the duty to an organisation or a role" | Contradicted in part | **Agree that the gap sentence must change. The suggested replacement overstates.** Blain and Lashley do not *assign* a duty to service-role holders. Host–guest relations "can be seen to apply" to those roles. "Using this metaphor", the host "is obliged" (p. 1). On p. 2 the obligation is "accepted by hosts". Suggested wording: "the one hospitableness paper read that states a host obligation extends it, by metaphor, to service roles (Blain and Lashley 2014, p. 1) and then proposes recruiting hospitable individuals (p. 2)". The "organisation" half of the gap survives: neither paper names an organisation as holder. |
| 6 | "a virtue has no holder to delegate from" | Supports in substance | **Disagree in part.** Blain and Lashley *do* name a holder, "the host", and on p. 2 illustrate with the tour guide or air steward as an individual. What neither paper offers is any account of delegation or answerability. "Leaves no one answerable when the welcome is delegated to a system" is WS's inference from silence, not something the texts say. Reword the sentence to: "a disposition gives no account of what stays with the holder when the work is delegated". |
| 7 | Debt: all full texts closed | Superseded in part | **Agree.** |
| 8 | "Arrival alone does not switch it on" | Supports, from the hospitality side | **Disagree: consistent, not supporting.** The synthesis sentence is about the legal trigger of a duty. Lashley's pp. 1 and 5 concern the conditional continuation of the commercial welcome, voiced as cited critique and then qualified via Telfer (p. 5). The counter-voice is correctly noted. Add that the abstract also says "Guests are unconditionally welcomed by hosts driven by altruistic motives" (p. 1). |
| 9 | Anthropology gives guests duties, denies them demands | Consistent, weakly | **Agree. Restore "which concern us here"** (scope qualifier). Better evidence for guest duties is Lashley 2015 p. 2: "expected not to overstay their welcome, misbehave, or endanger the hosts". Neither paper addresses the guest's right to make demands. |
| 10 | "Imposed status (H1)" | Supports, social level only | **Agree, but the relevance is thin.** Lashley p. 4 describes a duty laid on everyone in pre-industrial societies ("any failure to act appropriately is treated with social condemnation"). It does not describe a status attached to whoever takes up a calling, which is what §4's "imposed status" means. |
| 11 | Hart, Hardimon unread | Unchanged | **Agree.** |
| 12 | Cobbe arXiv pp. 7, 10, 8 | Supports; locators change to 1192, 1195, 1193 | **Agree. Verified** against the saved VoR. |
| 13 | Hewagama, Hales and Klidas abstract only | Unchanged | **Agree.** The card diffs add no content. |
| 14 | Baum and Laux p. 6 (arXiv) | Unchanged | **Agree.** |
| 15 | Golubovskaya p. 1286 (reporting King) | Unchanged | **Agree.** |
| 16 | Lugosi 2009 | Unchanged | **Agree.** |
| 17 | §9 debts list | Update | **Agree.** Reword the Telfer addition as: "Telfer p. 42: Blain and Lashley quote 'duties to be hospitable' among the motives; Lashley 2015's unquoted paraphrase omits it". |

---

## Table of FAILs and non-MATCH quotations

No FAILs.

| Where | Quotation / claim | Finding |
|---|---|---|
| blain2014hospitableness `hold_rationale`; WS_DEBTS item 9 | "the chief responsibilities ... lie with hosts" (p. 1) | MATCH with distorting ellipsis: drops "which concern us here" (scope qualifier) |
| WS_DEBTS §3, item 2 | Religious obligations are "at odds with Telfer's notion …" (p. 2) | MATCH string; hedge "may be" dropped from the framing |
| blain2014hospitableness Summary | externally imposed obligation "treated as at odds" | Source says "may be at odds" (p. 2) |
| telfer1995hospitableness bullet 1 | "the provision of food, drink, and accommodation to those who are not members of a household" | PARAPHRASED-AS-QUOTE: Blain and Lashley's own unquoted paraphrase, presented as Telfer's definition |
| telfer1995hospitableness bullet 3; WS_DEBTS §2 | Lashley 2015 p. 5 list as a "conflicting report" "with Telfer page numbers" | Lashley's list is unquoted, has no Telfer page, and adds two items; not a like-for-like quotation |
| WS_DEBTS §2 (King) | Lashley pp. 1, 5 "supports the payment half" of King | Overstated: cited critique of commercial conditionality, not a guest obligation. Missed: Lashley p. 2 "expected not to … misbehave" |
| WS_DEBTS items 6, 8 | "Supports" | Overstated (see table): 6 is an inference from silence; 8 is consistent, not supporting |
| WS_DEBTS item 5 (suggested gap) | "assigns it to a service role" | Overstated: a metaphorical extension ("can be seen to apply", "Using this metaphor"); the obligation is "accepted by hosts" (p. 2) |
| cobbe2023understanding Critical notes | "That copy is not in sources/ and Fable did not re-check it" | Stale; the VoR copy is now saved and checked |
| WS_DEBTS §6 | new cards fail `--check` until bib entries are added | Stale; both bib entries now exist |

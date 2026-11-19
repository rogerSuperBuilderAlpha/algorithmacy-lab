<!-- Independent verification of cards, batch CV-G, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-G (run rr-2026-11-k)

**Scope.** Ten cards by reader R10 (`eu2005ucpd`, `uk2024dmcc`, `eu2024product`, `poole2019uksc`, `eu2019omnibus`, `orlando1983robbins`, `billops1978magness`, `jl2021bestwestern`, `gregg2005ukhl`, `yl2007ukhl`) and R10's addenda on `uk2010equality` (s. 20(5)-(6), Sch. 2 para. 2) and `eu2024aiact` (Annex III point 1(a); recitals 17 and 54). I wrote none of them. I edited no card and no other file, and I committed nothing. The repository's AGENTS.md asks agents to commit and push; the brief says not to commit, and I followed the brief.

**Method.** I extracted the text of every saved source myself (an HTML parser for XHTML, XML and HTML, run with `python3 -I`; `pdftotext` for PDFs) rather than using the reader's extractions. I pulled every double-quoted string from each card (and from each addendum only), split it at elisions and bracketed insertions, and searched the source with a script that allows only whitespace, line-end hyphenation, ligatures and quotation-mark glyphs; I then mapped each hit to its article, section, paragraph or page and compared it with the card's locator. I ran a second pass over single-quoted phrases of three or more words. I read the holdings myself in the passages named under each card. Scripts, extractions and re-fetched files are in the session scratchpad, not in the project.

**Records re-fetched on 11 Nov 2026.**
- EU Publications Office (`publications.europa.eu/resource/celex/`): 32005L0029, 02005L0029-20220528, 02005L0029-20260927, 32024L2853, 32019L2161, 02011L0083-20260927. HTTP 200 each; each byte-identical to the saved XHTML.
- National Archives Find Case Law `uksc/2019/25/data.xml`: byte-identical. Caselaw Access Project HTML and case metadata for 433 So. 2d 491 and 391 A.2d 196: byte-identical. govinfo PDF of *J.L.*: byte-identical.
- *Gregg* and *YL*: I did not touch publications.parliament.uk. The SHA-1 digests of the saved PDFs (base32 `5ZMQRXGT...`, `YSKMBQCM...`) equal the Internet Archive index digests for the captures of 14 Feb 2006 and 20 Jun 2009.
- legislation.gov.uk: one scripted request (s. 232 `data.xml`) returned HTTP 202 with no body, and a fetch-tool request returned an empty page. I used Internet Archive captures under K-D12 (details under card 2).

**Verdicts.** PASS 2 (the two addenda); PASS-WITH-NOTES 10; FAIL 0.

**Quotation tally.** 440 quoted segments. All 440 are MATCH with a correct locator. Eighteen needed a manual step: seven run across a page break or printed page number (*Billops* at 197-198; *J.L.* pg 10-11; *Gregg* paras 80 and 83; *YL* para 28 and, twice, para 114); eight quote REDTEAM_TORT.md or the dossier rather than the source, and match there (the `eu2024product` quotation of the system-vendor row matches ARGUMENT.md as committed at `67ec205d`, l. 118, which has since been rewritten); two on `uk2024dmcc` capitalise the first letter at the start of a sentence; and one on `eu2019omnibus` runs the art. 6a heading into its first paragraph with a full stop the source does not have. None is LOCATOR-WRONG, NOT-FOUND, PARAPHRASED-AS-QUOTE or OCR-DOUBT. The OCR slips the cards reproduce ("the'punitive", "eriminal", "Robbin’s", "Coloration") are in the copies and the cards flag them.

**The DMCC commencement question, in short.** Sections 225-231 (the prohibition, aggressive practices, enforcement) and s. 233 (the power to make redress regulations) have been in force since 6 April 2025. Sections 232, 234 and 235 (the consumer's rights of redress) were excepted from S.I. 2025/272 and are prospective on every text I could read. No 2026 text shows them commenced. Until the first regulations under s. 233 come into force, Part 4A of the 2008 Regulations (the old private redress regime) continues under s. 252(2)-(3)(a); neither R10 nor I read it. Evidence under card 2.

---

## 1. eu2005ucpd

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved files byte-identical to the Publications Office records, and their sha256 prefixes match `source_basis`. The Official Journal header reads L 149/22, 11.6.2005, Directive of 11 May 2005. The 27.9.2026 consolidation lists Directive 2019/2161 (L 328, 18.12.2019, p. 7) as M1 and states that it "has no legal effect". I did not re-query the SPARQL endpoint for 'latest consolidation'.
2. **Read depth.** The folder holds the whole OJ text and both consolidations. What the card says it read is there.
3. **Quotations.** 45 segments, all MATCH, locators correct: arts 1, 2(a), (b), (d), (j), (k), 3(1)-(3), 5(1)-(4), 8, 9 opening and (a), (c), (d), 11(1)-(2), 19; recitals 9, 13, 16; Annex I point 27. Art. 2(c) and art. 11a come from the 2026 consolidation, as the card marks; the 2005 art. 2(c) reads differently ("any goods or service including immovable property, rights and obligations"), so "as replaced" is right. Art. 9 is word for word the same in the 2005 text and the 2026 consolidation. "as a mark of an aggressive practice" quotes REDTEAM_TORT T6 and matches there.
4. **The provisions.** Art. 9 opens "account shall be taken of", so point (d) is a factor in the art. 8 test, which also requires that the practice "thereby causes" a transactional decision. Art. 11a(1) lets Member States "determine the conditions for the application and effects of those remedies". The card states both correctly.
5. **May say / may not say.**
   - May say 1-4: LICENSED. On 3, if it is used for a guest's remedy, add art. 11a(1)'s second sentence on national conditions.
   - May not say 1, 2, 4, 5, 6: LICENSED. On 5, the 2008 Regulations were revoked, but they continue for earlier acts and their Part 4A is saved (DMCC s. 252(2)-(3)).
   - May not say 3: LICENSED-NARROWER. The business traveller is outside art. 2(a). A companion who did not contract is still a natural person acting outside a trade, so a 'consumer' (art. 2(a)), and may take transactional decisions (art. 2(k) covers deciding "to act or to refrain from acting"). The companion falls outside art. 9(d)'s "rights under the contract", but the text does not settle whether such a person can claim under art. 11a. The critical note "Consumers and traders only" overstates the same point.
6. **Bearing on K7 and K9.** Agree. My passage: art. 9(d) speaks of barriers "imposed by the trader", and art. 8 requires that the practice cause a transactional decision. A host that keeps no reachable person has not obviously 'imposed' a barrier, and the card says so.
7. **Reader's inferences.**
   - A vendor or brand that runs the guest's interface may be a 'trader' as "anyone acting in the name of or on behalf of a trader" (art. 2(b)): open. The words support it; CJEU case law on art. 2(b) would settle it.
   - The negative correlate for Step 6: supported as a reading of arts 2(k), 3(1), 8 and 9(d), provided the sentence keeps art. 8's condition that the obstruction cause a transactional decision.

## 2. uk2024dmcc

**Verdict: PASS-WITH-NOTES**

1. **Identity and commencement.** The saved captures match the hashes in `source_basis` (chapter 886221a3fed2, Sch. 20 acc8fe97cf8f). The chapter capture of 12 Dec 2025 records ss. 224-231 and 236-252 in force at 6.4.2025 by S.I. 2025/272, reg. 2(1)(3); s. 233 "in force at Royal Assent for specified purposes" and otherwise at 6.4.2025; and ss. 232, 234 and 235 "not in force at Royal Assent", each headed 'Prospective', with "no known outstanding effects" for the chapter. Sch. 20 paras are in force at 6.4.2025 by reg. 2(1)(11). I then checked three later records:
   - **S.I. 2025/272, reg. 2, as made** (Internet Archive capture of 8 Oct 2025): reg. 2(3) brings Chapter 1 of Part 4 into force "except sections 232, 234 and 235". The page renders footnote 2 as "(2)" immediately after "235", so a scraped text reads "235(2)". The footnote reads "Section 252 sets out transitional and saving provisions in respect of Chapter 1 of Part 4 of the Act". All of s. 235 is excepted. A search-engine summary I saw misread the same markup as "235(3)"; anyone citing reg. 2(3) should check the footnote.
   - **The Act's contents page** (capture of 25 Mar 2026, "up to date with all changes known to be in force on or before 25 March 2026"): the outstanding changes are commencement of ss. 291-305 and Schs 25-27 by S.I. 2026/284 and conferrals of functions by S.I. 2026/259. Nothing touches ss. 232-235.
   - **Section 233** (capture of 22 Sep 2026, "up to date ... on or before 22 September 2026"): one outstanding effect for the whole Act, s. 151(1)(ha) inserted by 2026 c. 18. No regulations under s. 233 and no commencement of ss. 232, 234 or 235 appear.
   - The Archive's index lists no capture of s. 232 after 15 Nov 2025, and R10 reports that the 2026 captures of the chapter page hold an empty response. So the status of s. 232 after 12 Dec 2025 cannot be read from its own text. On everything read, ss. 232, 234 and 235 have not commenced, and the card's statement and its 'may not say' 4 are correct and properly hedged.
   - **Saved regime.** Section 252(2) keeps the 2008 Regulations for acts before "the commencement date", and s. 252(3)(a) fixes that date, for Part 4A, as "the date on which the first regulations made under section 233 come into force". As far as shown, a UK consumer's private redress for an aggressive practice today runs under Part 4A of the 2008 Regulations, which R10 did not read and which I did not read. The card mentions the saving; its 'Where it bears' (K6) and the R10 report (§ 1) describe the guest's private redress from s. 232 alone.
2. **Read depth.** The chapter capture holds ss. 224-252 whole; the Sch. 20 capture holds Sch. 20. Both are Internet Archive copies, admissible under K-D12.
3. **Quotations.** 64 segments, all MATCH, locators correct, including s. 230(2)(i) and (3)(d), s. 245(c), Sch. 20 para. 29 and note I10. Two segments at card line 76 ("Onerous or disproportionate", "Non-contractual barriers imposed by the trader") differ from the source only by a capital at the start of the sentence.
4. **The comparison of s. 228(2)(f) with UCPD art. 9(d).** I agree that the words are changed and the scope is wider in two respects. First, "rights that the consumer has in relation to a product" is not confined to rights under the contract. Second, the "non-contractual" qualifier is gone, so onerous steps that a contract term itself requires now count. The card omits two points. The UCPD's example, "including rights to terminate a contract or to switch to another product or another trader", is gone. And s. 228(2)(f) asks whether the practice "requires a consumer to take onerous or disproportionate action", which frames the factor as a demand made of the consumer, not as a barrier. Whether a host that simply keeps no reachable person "requires" such action is open; neither the reader nor I read a judgment or the Explanatory Notes.
5. **May say / may not say.**
   - May say 1, 2, 5: LICENSED.
   - May say 3: LICENSED-NARROWER. Write "Engaging in an unfair commercial practice that involves an aggressive practice is an offence (s. 237(3))". The offence needs the s. 225(4)(a) test (a likely transactional decision), not aggression alone.
   - May say 4: LICENSED-NARROWER. Add: "Section 232 is not in force: S.I. 2025/272, reg. 2(3) excepted ss. 232, 234 and 235, and the latest text read (12 Dec 2025) marks them prospective."
   - May not say 1-5: LICENSED. On 2, the wording "the Act gives" is right; it should not be read as saying the guest has no private claim at all, given Part 4A.
6. **Bearing on K7 and K9.** Agree on K7. Two corrections. 'Where it bears' says "In England"; the provisions read are marked 'U.K.', and s. 231(1) speaks of authorities "in Great Britain", so write "In the United Kingdom". On K6, the guest's private side today is the saved Part 4A, unread, so the statement that redress "was not in force" describes the new regime only.
7. **Reader's inferences.**
   - The comparison of texts: supported, with the two additions in head 4.
   - "A barrier met during the stay ... gives no right of redress ... unless it drives a further payment": supported for a stay paid in advance. Open for a guest who pays at or after departure, where an obstruction met during the stay could be "a significant factor" in the decision "to make the payment" (s. 232(2)(c), (4)(b)). The s. 233 regulations, once made, and Part 4A now would settle it.
   - The vendor as a 'trader' under s. 225(3)(b): open.

## 3. eu2024product

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Byte-identical. Header: OJ L series 2024/2853, 18.11.2024; Directive of 23 October 2024. I did not re-query the SPARQL endpoint.
2. **Read depth.** The whole OJ text is saved.
3. **Quotations.** 47 segments, all MATCH, locators correct: arts 1, 2(1), 2(4)(b), 4(1), (3), (4), (9), (10), 5(1), 6(1)-(2), 7(1), 7(2)(c) and (i), 8(1), 10(1), 10(2)(c), 11(2)(b)-(c), 12(1), 13(1)-(2), 15, 21, 22(1); recitals 6, 13, 17, 24. The quotation of the dossier's system-vendor row matches ARGUMENT.md as committed at `67ec205d`; the current ARGUMENT.md has already rewritten that row on this card's authority.
4. **Dates, software, data.**
   - *Dates.* Art. 2(1): products placed on the market or put into service "after 9 December 2026". Art. 21: Directive 85/374/EEC repealed "with effect from 9 December 2026" but continuing for earlier products. Art. 22(1): transposition "by 9 December 2026". Art. 23: entry into force on the twentieth day after publication, so in December 2024. The critical-note heading "Not yet in force for any product" should read "does not yet apply to any product".
   - *Software.* Art. 4(1) "includes ... software". Recital 13 names "AI systems" and covers software "irrespective of the mode of its supply or usage", software-as-a-service included. The same recital excludes "Information" and "the mere source code of software", and art. 2(2) excludes free and open-source software supplied outside a commercial activity (not on the card).
   - *Data.* Art. 6(1)(c): "destruction or corruption of data that are not used for professional purposes". Recital 24: privacy infringements and pure economic loss do not "by themselves" trigger liability. The card states this correctly.
5. **May say / may not say.**
   - May say 1, 3, 4, 5: LICENSED.
   - May say 2: LICENSED-NARROWER. Art. 6(1)(b) also excludes damage to "the defective product itself" and to a product damaged by its own integrated defective component. Write "damage to property other than the defective product itself and property used exclusively for professional purposes".
   - May not say 1: LICENSED-NARROWER. Drop "a lost booking" or qualify it. A lost booking that destroys or corrupts the guest's own non-professional data may fall under art. 6(1)(c); whether booking data held by the hotel are "not used for professional purposes" is unsettled.
   - May not say 2-4: LICENSED.
6. **Bearing on K7 and K9.** Agree: the Directive refutes the old system-vendor row for physical harm and leaves it for performance failures. On K9, add data loss as a third listed kind of damage that matters for app-based hosts.
7. **Reader's inferences.**
   - Performance failures are not displaced: supported (arts 6(1), 7(1), recital 24), subject to the data limb.
   - A hotel group that develops guest-facing software for its own use and puts it into service is a manufacturer: supported on the words of arts 4(9), 4(10)(c) and 8(1)(a); open in application, since recital 17 keeps "services as such" out and no case was read.

## 4. poole2019uksc

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Byte-identical to the live XML. Header: [2019] UKSC 25, on appeal from [2017] EWCA Civ 2185, judgment given 6 June 2019, heard 16 and 17 July 2018; "LORD REED: (with whom Lady Hale, Lord Wilson, Lord Hodge and Lady Black agree)". All match the card. The card gives no law-report citation, correctly.
2. **Read depth.** Paras 1-92 are present.
3. **Quotations.** 39 segments, all MATCH. Two quote REDTEAM_TORT T14 and match there. "no possible basis" is at para 91; the card's "paras 90-91" covers it.
4. **Holding, and the correction of the red team.** The card states the holding correctly: unanimous, a strike-out, the rule at para 65, no assumption of responsibility pleaded (paras 79-83, 85-89), and a breach with no possible basis (paras 90-91). R10's correction is right as far as it goes: para 81's subject is "the council’s investigating and monitoring the claimants’ position", and the housing limb was not before the Court (paras 8, 10, 77). But Poole is not silent on placement. Para 77 reads: "It was suggested in argument that a duty of care might have arisen on the basis that the council had created the source of danger by placing Amy and her family in housing adjacent to the neighbouring family. The difficulty of sustaining such an argument is however apparent from Mitchell ...", followed by the line on landlords. That is a dictum doubting that placement creates the danger. The red team's conclusion (no duty from placement alone) draws some support from para 77, though not from para 81 and not as a holding.
5. **May say / may not say.**
   - May say 1-3: LICENSED.
   - May say 4: LICENSED-NARROWER. The splice attaches "whether operated privately or under statutory powers" to "a public body", but in para 80 the phrase qualifies a hospital. Write: Lord Reed, explaining Lord Browne-Wilkinson, said that a public body offering a service "often assumes a responsibility to those using the service", and that "whether operated privately or under statutory powers, a hospital undertakes to exercise reasonable care in the medical treatment of its patients" (para 80).
   - May not say 1-4: LICENSED. Add a fifth: that Poole says nothing about placement. Para 77 doubts, in a dictum, that placing a family next to known anti-social neighbours creates the danger.
6. **Bearing on K7 and K9.**
   - *K8.* Agree, with para 77 added. The placing body owes no duty from statutory functions alone (para 65(2)), and on para 77 probably none from the placement itself; the operator stands on ordinary principles.
   - *K3.* Disagree with "Assumption of responsibility, reliance and entrustment are the grounds of a duty to protect". Para 65(3) also names creation of the danger, and para 76 lists four situations: assumption, preventing another's protection, special control, and status. Write "among the grounds".
7. **Reader's inferences.**
   - An occupier's duty is untouched: supported. Para 28 frames the distinction, and para 74 places the case among failures to protect.
   - An operator's duty by analogy (paras 42, 73, 80): open. A case on a provider housing a person placed under contract with an authority would settle it.

## 5. eu2019omnibus

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Byte-identical (also to the copy in `sources/eu2011consumer/`). The consolidated Directive 2011/83 of 27.9.2026 is byte-identical too, and prints art. 6a in the same words. Header: L 328/7, 18.12.2019; Directive of 27 November 2019.
2. **Read depth.** The whole OJ text and the consolidation are saved.
3. **Quotations.** 33 segments, all MATCH. One needs a note: card line 33 runs the art. 6a heading into para 1 with a full stop ("... online marketplaces. 1. Before ..."), whereas the heading stands on its own line with no full stop. Locators correct: art. 3(5) (UCPD art. 11a); art. 4(1)(e) (CRD art. 2(17)-(18)); art. 4(2)(a) (art. 3(1)); art. 4(4)(a)(i) (art. 6(1)(c)); art. 4(5) (art. 6a); art. 7(1); recitals 16, 22, 24, 27, 28.
4. **The provisions.** Art. 6a(1)(d) requires information "without prejudice to any responsibility" under other law, and recital 27 ties it to "the contractual arrangements". R10's correction of T10 (disclosure, not allocation) is right.
5. **May say / may not say.**
   - May say 1-2: LICENSED.
   - May say 3: LICENSED-NARROWER. Add that the rule sits in the information a trader must give before a consumer is bound by a distance or off-premises contract (CRD art. 6(1)).
   - May not say 1-3: LICENSED.
6. **Bearing on K7 and K9.** Agree.
7. **Reader's inference.** Whether CRD art. 6(1)(c) implies a duty to answer during performance: open. The reader points to `amazon2019cjeu`, which is where it would be settled.

## 6. orlando1983robbins

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Byte-identical. The CAP metadata matches: Nos. 61165, 61166; 31 March 1983; pp. 491-496; Florida Supreme Court; McDonald J for the majority; Boyd J dissenting; "ALDERMAN, C.J., and ADKINS, OVERTON and EHRLICH, JJ., concur." The text reads "Rehearing Denied June 29, 1983".
2. **Read depth.** The whole opinion is saved.
3. **Quotations.** 29 segments, all MATCH, locators correct, including at 495 for the expert's cross-examination.
4. **What *Orlando* approved.** The Court "approve[d] the district court decision" (at 492, 494) on both petitions. On OEP, the absence of industry standards did not insulate it where there was credible evidence of available measures, and foreseeability was for the jury (at 493). On HJ, the three elements of apparent agency, "As HJ concedes", and sufficient evidence of representation and reliance (at 494). HJ's operation of the restaurant, lounge and theatre is noted inside that sufficiency analysis. It was the district court that limited *Sydenham* and the oil-company cases "to their facts"; the Supreme Court approved that and "disapprove[d] extending the language of Sydenham" (at 494). The card's passive sentence on the oil cases does not say who limited them. The trial court had vacated the punitive verdicts (at 492). Boyd J dissented on causation in fact (at 494-496). The card's reading of the holding as apparent agency is right.
5. **May say / may not say.**
   - May say 1: LICENSED-NARROWER. A supreme court does not approve a verdict. Write: "The Supreme Court of Florida approved a district court decision affirming a judgment, on a jury verdict, against both the motel's owner-operator and its franchisor, Howard Johnson, jointly for compensatory damages to a guest attacked on the premises (at 492, 494)".
   - May say 2-4: LICENSED.
   - May not say 1-3: LICENSED.
6. **Bearing on K7 and K9.** Agree on K8 and K4.
7. **Reader's inferences.** None marked. The statement that a brand "may answer to the guest directly, as an apparent principal, in at least one US jurisdiction" is supported (at 494).

## 7. billops1978magness

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Byte-identical. The CAP metadata matches: Delaware Supreme Court; 21 July 1978; pp. 196-199; "Before HERRMANN, C. J., and DUFFY and McNEILLY, JJ."; McNeilly J for the court. The text reads "Submitted May 12, 1978".
2. **Read depth.** The whole opinion is saved.
3. **Quotations.** 37 segments, all MATCH. One runs across the *198 marker ("goes *198beyond"), so "at 197-198" is right. One quotes REDTEAM_TORT T12 and matches there.
4. **Does *Billops* hold that a mandatory manual can show day-to-day control?**
   - *What the Court held.* As a triable issue, yes; as a sufficient fact on its own, no. The Court held that "there are sufficient facts of record which, along with the reasonable inferences therefrom, show day-to-day control ... so that ... summary judgment should have been denied" (at 198). The facts it then lists are a manual "detailed and in parts mandatory" and "incorporated into the franchise agreement", record-keeping "to insure compliance with the manual guidelines", a right to enter and inspect, and "the right of unilateral termination for violation" (at 198). It "make[s] no judgment as to whether ... an actual agency relationship exists" (at 198), and it reversed and remanded (at 199). So the manual with its enforcement machinery raised the issue. The card's summary says so; its 'may say' 2 compresses it.
   - *"staff procedures".* The manual list reads "staff procedures and standards for soliciting and booking group meetings, functions and room reservations". That may be one item (staff procedures for soliciting and booking) rather than staff procedures in general. Quoting "staff procedures" alone takes the wider reading, and the R10 report repeats it (§ 4).
   - *Summary.* The text says "refusing to adequately heat the ballroom", not that staff would not heat it. The claims included negligent infliction of emotional distress, and the complaint alleged physical injury from stress (at 197).
5. **May say / may not say.**
   - May say 1: LICENSED. The quoted rule is introduced by "If, in practical effect, the franchise agreement goes beyond the stage of setting standards"; keep that condition when using it.
   - May say 2: LICENSED-NARROWER. Write: "a detailed and in parts mandatory operating manual, incorporated into the franchise agreement and regulating, among other things, 'front office procedures' and 'minimum guest room standards', together with record-keeping, inspection and termination rights, raised a triable issue of actual agency (at 198)". Drop "staff procedures" or quote the whole item.
   - May say 3: LICENSED.
   - May not say 1-3: LICENSED. On 2, the reason clause should say that the claims included negligent infliction of emotional distress.
6. **Bearing on K7 and K9.** Agree on K8: the test is the right to control daily operations, and *Billops* refutes 'Control: No' as a general statement.
7. **Reader's inference.** That a brand-mandated check-in or complaints system would be evidence of the same kind: supported as evidence, since the Court counted "front office procedures" (at 198); not shown to suffice alone.

## 8. jl2021bestwestern

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Byte-identical. 46 pp.; Civil Action No. 19-cv-03713-PAB-STV; Document 91, filed 02/24/21; "DATED February 24, 2021"; Chief Judge Philip A. Brimmer. The Hyatt movant was Select Hotels Group, LLC, "Improperly Named as, 'Hyatt Corporation'" (pg 1, 46). The reporter citation 521 F. Supp. 3d 1048 is unverified: an anonymous CourtListener search returned nothing usable. The card does not use it.
2. **Read depth.** The whole PDF is saved, and the card names the parts it read. I also read IV.C.1 (pg 28-33): the Court found a prima facie case of specific jurisdiction over Best Western (pg 32-33). Its merits rulings on Best Western are therefore not alternative holdings.
3. **Quotations.** 38 segments, all MATCH. The statute runs across pg 10-11, and the card's "pg 10-11" is right. Two quote REDTEAM_TORT and match there. The pg 13 benefit quotation is the Court quoting *A.B. v. Hilton* (2020 WL 5371459, at *7) and then agreeing with it, which is what the card says.
4. **What *J.L.* decided (pleading only?).**
   - *Rulings.* Every ruling is on the sufficiency of the first amended complaint under Rule 12(b)(6), with Rule 12(b)(2) for Best Western: "at the motion to dismiss stage, the Court accepts factual allegations of the complaint as true" (pg 36). The benefit element was pleaded (pg 13, 33), and no overt act is required (pg 15-16). Knowing participation was not pleaded against any brand (pg 19, 25, 35). Actual agency was plausibly pleaded for Wyndham (pg 21), Marriott (pg 27), Best Western (pg 36) and, "at most", Hyatt (pg 45). Agency liability still failed because the hotels were not plausibly liable (pg 27, 36-37, 45), and apparent agency failed for want of alleged reliance (pg 22, 28).
   - *Disposition.* The disposition is final, not interlocutory: all four motions were granted, the claims were "DISMISSED with prejudice", judgment was entered for the defendants, and "this case is closed" (pg 45-46).
   - *A.B. v Marriott.* The order cites *A.B. v Marriott* at pg 11 (elements), pg 13 (benefit, "same"), pg 15 (within the Court's report of the plaintiff's brief, on § 1591's definition) and pg 27 and 37 (allegations held sufficient). It is never cited as going the other way. The red team was wrong and R10 is right.
5. **May say / may not say.**
   - May say 1, 3: LICENSED.
   - May say 2: LICENSED-NARROWER. Keep the Court's words: "General knowledge of commercial sex activity occurring at hotels across the United States is insufficient on its own to demonstrate that Wyndham participated in the trafficking of plaintiff" (pg 19), applied to Best Western at pg 35.
   - May not say 1-3: LICENSED.
6. **Bearing on K7 and K9.** Agree, with one narrowing on K7. The order holds that the absence of allegations that staff heard her pleas, or that she alerted staff, defeated actual knowledge (pg 35). It does not hold that such allegations would have sufficed against the franchisor. At pg 35 even "the signs that she alleges should have alerted staff" did not show that the parent knew or should have known. What reached staff is shown necessary, not sufficient, for the brand's direct liability.
7. **Reader's inferences.** None marked beyond the link to R7. It holds as an illustration, with the narrowing in head 6.

## 9. gregg2005ukhl

**Verdict: PASS-WITH-NOTES**

1. **Identity.** The saved PDF's digest equals the Archive index digest for the 14 Feb 2006 capture. Header: [2005] UKHL 2, on appeal from [2002] EWCA Civ 1471, Thursday 27 January 2005. The committee matches the card. No law-report citation is given, correctly.
2. **Read depth.** All 79 pages are saved; the card names the parts it did not read. I read Lord Hoffmann paras 61-91 whole, Lord Nicholls paras 18-19, 44 and 51, Lord Hope paras 92-98 and 116-124, Lord Phillips paras 184-191, and Baroness Hale paras 192-196 and 206-227.
3. **Quotations.** 38 segments, all MATCH. Two run across printed page numbers ("-23-" in para 80, "-24-" in para 83).
4. **Each Lord's position, and the ratio.**
   - *Lord Hoffmann.* Correct as carded: determinate causation and the burden of proof (paras 79-80); the para 83 distinction, which covers what the claimant or "someone for whom the defendant is responsible" would have done; *Wilsher* and *Hotson* (para 85); the 'hook' rejected (paras 86-87); Parliament (para 90); appeal dismissed (para 91).
   - *Baroness Hale.* Correct: paras 193, 206, 217, 224-226, and at para 227 "With some regret ... I agree that this appeal should be dismissed".
   - *Lord Phillips.* Correct: the case is "not a suitable vehicle"; there "may be a case" for proportionate recovery where an adverse outcome has occurred; he upheld the conventional approach (para 190) and agreed "On those facts" that the appeal must be dismissed (para 191).
   - *Lord Nicholls.* Correct: paras 44, 51, 59.
   - *Lord Hope: stated incompletely.* The Summary groups him with Lord Nicholls on the diminution-of-prospects ground (paras 42-44, 121). That is half his position. His main ground was that the enlargement of the tumour was a physical injury proved on the balance of probabilities, and that the lost prospects were consequential loss within a single cause of action (paras 95-96, 117, 120). He then also agreed with Lord Nicholls (para 121). Lord Hoffmann rejected that route as a 'hook' (paras 86-87), and Lord Phillips marked it as different (para 187).
   - *Ratio.* By three to two the House dismissed the appeal. In this clinical-negligence claim the claimant had to prove on the balance of probabilities that the negligence caused the adverse outcome, and the loss of a chance of a better outcome was not treated as actionable damage. Lord Hoffmann and Baroness Hale reasoned generally, Baroness Hale for personal injury as a whole (para 225). Lord Phillips decided on the facts and left open proportionate recovery where the adverse outcome has occurred, which is the position of an injured guest. The red team's lead, "In personal-injury claims, English law does not compensate a lost chance", states two of the three majority speeches.
5. **May say / may not say.**
   - May say 1: LICENSED-NARROWER. Add: "Lord Phillips concurring on the facts, holding the case 'not a suitable vehicle' and leaving open proportionate recovery where an adverse outcome has occurred (para 190)".
   - May say 2: LICENSED. Lord Hoffmann's words are "someone for whom the defendant is responsible", which reaches a host's staff.
   - May say 3-4: LICENSED.
   - May not say 1-3: LICENSED.
6. **Bearing on K7 and K9.** Agree that *Gregg* blocks the move from a missing channel to damages for the injury without proof of causation. The block is narrower by Lord Phillips's reservation at para 190, and the card's critical note should carry Lord Hope's injury-based route as a dissent the majority rejected.
7. **Reader's inferences.**
   - Financial loss stands differently: supported (para 83; Baroness Hale paras 218-220).
   - Contract and statutory remedies are untouched: supported as to *Gregg*'s scope (negligence, personal injury). Whether contract damages for a lost chance follow *Chaplin v Hicks*, which Lord Nicholls cites at para 18, is not decided in *Gregg*: open.
   - The three links in the guest's proof follow from para 83: supported.

## 10. yl2007ukhl

**Verdict: PASS-WITH-NOTES**

1. **Identity.** The saved PDF's digest equals the Archive index digest for the 20 Jun 2009 capture. Header: [2007] UKHL 27, on appeal from [2007] EWCA Civ 27, Wednesday 20 June 2007. The committee matches the card.
2. **Read depth.** All 70 pages are saved; the card names the parts it read. I read Lord Bingham paras 19-20, Lord Scott paras 26-35, Baroness Hale paras 73-75, Lord Mance paras 76-77 and 114-123, and Lord Neuberger paras 166-171.
3. **Quotations.** 39 segments, all MATCH. Three run across page breaks (para 28, "all their / 8 / residents"; para 114, twice).
4. **Positions and ratio.**
   - *Majority.* Correct: Lord Scott (para 33), Lord Mance (para 123), Lord Neuberger (para 170).
   - *Dissent.* Correct: Lord Bingham (para 20) and Baroness Hale (paras 73, 75).
   - *Facts.* Correct: the resident was 84 with Alzheimer's disease; there was a "three way" placement agreement of 20 Feb 2006 and a top-up paid by her daughter; her residence was "largely funded" by the council (para 76).
   - *Vulnerability.* The card's point that vulnerability did not change the answer has its footing in Lord Scott, para 32.
   - *Not on the card.* Lord Scott also held the notice to quit a private act under s. 6(5) (para 34).
   - *Two corrections.* The critical note "The majority's reasons were not uniform" overstates. Each majority Lord adopted the others' reasons: Lord Scott's are "supplemental to those of ... Lord Mance and Lord Neuberger, with which I am in full agreement" (para 35); Lord Mance agrees with their "reasoning and conclusions" (para 123); Lord Neuberger decides "for the reasons given by Lord Mance, as well for those given by Lord Scott" (para 170). And Lord Mance introduces the continuing duty at para 114 as "A rider that perhaps calls for mention".
5. **May say / may not say.**
   - May say 1, 3, 4: LICENSED.
   - May say 2: LICENSED-NARROWER. Write: "Lord Neuberger (para 149) and Lord Mance (para 118) said that the resident kept her Convention rights against the local authority; Lord Mance added, as 'a rider', that it was not suggested that the authority has 'no continuing duty in respect of the suitability of a placement, once made' (para 114)."
   - May not say 1-3: LICENSED. Later legislation is still unchecked, as the card says; check it before stating the present law for care homes.
6. **Bearing on K7 and K9.** Agree on K8 and K5.
7. **Reader's inferences.**
   - That the hotel analogy is stronger against public-function status: supported in reasoning (paras 19, 166-167); open as law.
   - That compulsion would change the answer: supported (paras 121, 166-167).

## 11. uk2010equality, R10 addendum (s. 20(5)-(6), Sch. 2 para. 2)

**Verdict: PASS**

1. **Identity.** `sources/eqa2010s20/` holds s20, s21 and sch2 captures (.html and .txt). Each states that it is up to date to 7 November 2026. The addendum notes the one-day difference from the card's "8 Nov 2026" capture date, and a capture date can follow its 'up to date' date. Not re-fetched: legislation.gov.uk returns HTTP 202.
2. **Read depth.** s. 20(1)-(13) and Sch. 2 paras 1-4 are present.
3. **Quotations.** 22 segments, all MATCH, locators correct: s. 20(3), (5), (6), (7), (11); Sch. 2 para. 2(1), (2), (3), (4), (6), (7); s. 21(2).
4. **The provisions.** Stated correctly. One addition for the dossier: s. 21(3) makes the duty actionable only through s. 21(2), discrimination against the disabled person concerned.
5. **May say / may not say (added).** May say 1-2: LICENSED. On 1, "in anticipation" glosses Sch. 2 para. 2(2) ("disabled persons generally"), and the duty reaches a service-provider through s. 29(7), which the card above cites. May not say 1-2: LICENSED.
6. **Bearing on K7 and K9.** Agree: a floor for disabled guests only, bounded by reasonableness and by "fundamentally alter" (para. 2(7)).
7. **Reader's inference.** That a reachable person is an "auxiliary service" a self-service hotel may have to provide: open. The EHRC Services Code or a county-court decision would settle it.

## 12. eu2024aiact, R10 addendum (Annex III point 1(a); recitals 17 and 54)

**Verdict: PASS**

1. **Identity.** `aiact.txt`, saved 8 Nov 2026 and covered by CV-D; not re-fetched. I searched the saved Regulation (EU) 2026/1744 for amendments to Annex III point 1 and found none.
2. **Read depth.** Annex III point 1 and recitals 17 and 54 are present.
3. **Quotations.** 9 segments, all MATCH, locators correct, including recital 17's "having security access to premises".
4. **The correction of the red team.** Verified. Recital 17 gives the reason: "That exclusion is justified by the fact that such systems are likely to have a minor impact on fundamental rights of natural persons ...". Recital 54 gives none. One precision: Annex III point 1(a)'s operative exclusion reads only "biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be". The words on access "to a service, unlocking a device or having secure access to premises" are in recitals 17 and 54 only.
5. **May say / may not say (added).** May say: LICENSED; cite the access wording to recital 54 alone. May not say: LICENSED.
6. **Bearing on K7 and K9.** Agree.
7. **Reader's inference.** That arts 14 and 26 do not apply to such a kiosk or door: supported for Annex III point 1(a); open for Annex I, which was not read.

---

## Table: every FAIL, every quotation that is not MATCH, every 'may say' or 'may not say' sentence that is not LICENSED

| Card | Item | Finding | What to write instead |
|---|---|---|---|
| (all) | FAIL | None | — |
| (all) | Quotations | None outside MATCH (440 segments; 18 needed a manual step, listed in the tally) | — |
| eu2005ucpd | May not say 3 | LICENSED-NARROWER | The business traveller is outside art. 2(a); a non-contracting companion is a 'consumer' and falls outside art. 9(d)'s "rights under the contract", but the text does not settle whether such a person can claim under art. 11a |
| uk2024dmcc | May say 3 | LICENSED-NARROWER | "Engaging in an unfair commercial practice that involves an aggressive practice is an offence (s. 237(3))" |
| uk2024dmcc | May say 4 | LICENSED-NARROWER | Add: s. 232 is not in force; S.I. 2025/272, reg. 2(3) excepted ss. 232, 234 and 235, and the latest text read (12 Dec 2025) marks them prospective |
| eu2024product | May say 2 | LICENSED-NARROWER | "damage to property other than the defective product itself and property used exclusively for professional purposes" (art. 6(1)(b)) |
| eu2024product | May not say 1 | LICENSED-NARROWER | Drop "a lost booking", or note that destruction or corruption of the guest's non-professional data may fall under art. 6(1)(c) |
| poole2019uksc | May say 4 | LICENSED-NARROWER | Quote para 80 so that "whether operated privately or under statutory powers" qualifies the hospital, as in the judgment |
| eu2019omnibus | May say 3 | LICENSED-NARROWER | Add that the rule is part of the pre-contractual information for distance and off-premises contracts (CRD art. 6(1)) |
| orlando1983robbins | May say 1 | LICENSED-NARROWER | "approved a district court decision affirming a judgment, on a jury verdict, against both ... jointly for compensatory damages" |
| billops1978magness | May say 2 | LICENSED-NARROWER | "a detailed and in parts mandatory operating manual, incorporated into the franchise agreement ..., together with record-keeping, inspection and termination rights"; drop "staff procedures" or quote the whole item |
| jl2021bestwestern | May say 2 | LICENSED-NARROWER | Use the Court's words: "General knowledge of commercial sex activity occurring at hotels across the United States is insufficient on its own ..." (pg 19; applied to Best Western, pg 35) |
| gregg2005ukhl | May say 1 | LICENSED-NARROWER | Add Lord Phillips's ground: "not a suitable vehicle", leaving open proportionate recovery where an adverse outcome has occurred (para 190) |
| yl2007ukhl | May say 2 | LICENSED-NARROWER | "Lord Neuberger (para 149) and Lord Mance (para 118) said ...; Lord Mance added, as 'a rider', ... (para 114)" in place of "The majority held" |

Other corrections that are not 'may say' sentences, for the lead:
- **Poole, para 77.** The dictum on placement as creating the danger belongs on the card and in the dossier's placed-guest row.
- **DMCC s. 252.** The saved Part 4A of the 2008 Regulations governs a UK consumer's private redress until the s. 233 regulations come into force, and it is unread.
- **Gregg.** Lord Hope's injury-based ground (paras 95-96, 117, 120) is missing from the Summary.
- **YL.** "Not uniform" should become "different emphases, reasons cross-adopted" (paras 35, 123, 170).
- **eu2024product.** "Not yet in force" should read "does not yet apply" (art. 23).
- **uk2024dmcc.** "In England" should read "In the United Kingdom".

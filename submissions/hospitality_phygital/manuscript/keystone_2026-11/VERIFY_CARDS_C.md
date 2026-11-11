<!-- Independent verification of cards, batch CV-C, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-C (run rr-2026-11-k)

**Scope.** Fourteen cards: eight from reader R5a (`barclays2020uksc`, `armes2017uksc`, `hughes2022rattan`, `ferguson1987welsh`, `naylor2004payling`, `maguire2006sefton`, `wong1995kwan`, `uk2015consumer`) and six from reader R6a (`eu2015package`, `eu2026package`, `uk2018package`, `kuoni2021uksc`, `kuoni2021cjeu`, `amazon2019cjeu`). I wrote none of them. I edited no card and no other file.

**Method.** I re-fetched every record that an official site serves openly and compared it byte for byte with the saved copy. I extracted every double-quoted string on each card (776 segments, elisions and bracketed insertions split into segments) and searched the saved text with a script of my own, allowing only whitespace, line-end hyphenation, quotation-mark and ligature differences; I then mapped each hit to its paragraph, page, article, recital or regulation and compared it with the card's locator. For *Wong Mee Wan* I rendered the twelve page images, ran my own OCR pass to locate passages, and then read all twelve pages by eye. I read the holdings myself in the paragraphs the brief names. Scripts and OCR output are in the session scratchpad, not in the project.

**Records re-fetched on 11 Nov 2026.**
- National Archives Find Case Law, `data.xml` for [2020] UKSC 13, [2017] UKSC 60, [2022] EWCA Civ 107, [2004] EWCA Civ 560, [2006] EWCA Civ 316, [2021] UKSC 34 and [2019] UKSC 37: HTTP 200 each, each byte-identical to the saved XML.
- EU Publications Office, `publications.europa.eu/resource/celex/` for 32015L2302, 32026L1024, 62019CJ0578 and 62017CJ0649 (XHTML, English): HTTP 200 each, each byte-identical to the saved XHTML.
- legislation.gov.uk: four requests (SI 2026/455 as made, SI 2018/634 reg. 7, Consumer Rights Act 2015 s. 49) returned HTTP 202 with an empty body. I did not try to get round it. The Internet Archive's capture of the SI 2026/455 contents page (29 Apr 2026) confirms the instrument's title and its three regulations.
- BAILII serves a bot challenge; I did not re-fetch *Ferguson* or *Wong Mee Wan* and relied on the scout's archive copies.

**Verdicts.** PASS 3; PASS-WITH-NOTES 11; FAIL 0.

**Quotation tally.** 776 quoted segments checked. Thirty of them are not quotations from a source. They are either phrases quoted from CLAIMS_FIXED.md, which I matched there, or search terms the cards report as absent ("non-delegable", "automat", "monitor" and the like), whose absence I confirmed. The other 746 are source quotations, and all are MATCH with a correct locator. Ten needed a manual step before I could call them MATCH: five *Wong Mee Wan* quotations where my OCR misread the scan ('ist' for '1st', 'Hable' and 'lable' for 'liable') or the quotation runs across a page (pp. 3-4, 4-5); one *Ferguson* quotation that runs across the page break between pp. 6 and 7; and four cross-card quotations that sit, correctly attributed, in another instrument or judgment. No quotation is LOCATOR-WRONG, NOT-FOUND, PARAPHRASED-AS-QUOTE or OCR-DOUBT.

---

## 1. barclays2020uksc

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XML byte-identical to the live record. Header: [2020] UKSC 13, on appeal from [2018] EWCA Civ 1670, judgment given 1 April 2020, heard 28 November 2019; Lady Hale, "with whom Lord Reed, Lord Kerr, Lord Hodge and Lord Lloyd-Jones agree". All match the card. The report citation [2020] AC 973 appears at *Hughes v Rattan* para 74, as the card says. The *Armes* citation does read "[2018] AC 355" at para 8 and "[2018] AC 855" at para 23.
2. **Read depth.** The saved text holds paras 1-30 complete. "non-delegable" occurs once (para 19); "occupier", "hotel", "guest" and "innkeeper" do not occur.
3. **Quotations.** 38 segments, all MATCH. The one quotation from another case (line 53, "the contractual arrangements between tortfeasor and defendant") is *Hughes* para 88, as the card says.
4. **Holding.** Correct. The only issue was vicarious liability, tried as a preliminary issue (para 6); the Bank was held not vicariously liable (para 30). Lord Bridge's sentence from *D & F Estates* enters at para 7 as part of "The parties' respective positions": Lady Hale quotes it in setting out the Bank's case, and the court's own holding that the distinction stands is at paras 24 and 27.
5. **What the paper may say / may not say.**
   - May say 1 (general non-liability, para 7): LICENSED-NARROWER. Cite it as "Lady Hale, quoting Lord Bridge in *D & F Estates* for the Bank's position (para 7), held that the distinction between employment and independent contract had not been eroded (paras 24, 27)".
   - May say 2-4: LICENSED.
   - May not say 1-4: LICENSED.
6. **Central conclusions.** Bears on (b) and (c); see the section on the readers' conclusions.
7. **Reader's own inference.** That an outsourced security, cleaning or software firm with other clients is an independent contractor: supported by analogy with Lady Hale's window cleaners and auditors and her "portfolio of patients and clients" (para 28); not decided.

## 2. armes2017uksc

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XML byte-identical. Header: [2017] UKSC 60, on appeal from [2015] EWCA Civ 1139, judgment 18 October 2017, heard 8 and 9 February 2017; Lord Reed "with whom Lady Hale, Lord Kerr and Lord Clarke agree"; Lord Hughes dissenting (from para 75). Matches.
2. **Read depth.** Paras 1-91 present.
3. **Quotations.** 63 segments, all MATCH (one differs only by a space, para 48).
4. **Holding.** The card reads the paragraphs the brief names correctly.
   - Para 31 defines a non-delegable duty as one "to ensure that care is taken", "a higher standard of care than the ordinary duty of care", not discharged by careful selection.
   - Para 32 calls such liabilities, "based not on personal fault", "exceptional".
   - Para 37 sets the duty "to perform with care" against a duty "merely ... to arrange to have performed, subject to a duty to take care in making and supervising those arrangements".
   - Paras 47-48 find from sections 21-22 of the 1980 Act that placement is itself the performance, so that the authority's duty is to "arrange for, and then monitor", made up of "prior approval ... and subsequent inspection, supervision and removal", aimed at problems "capable of observation".
   - Para 49 refuses the non-delegable duty; Lord Hughes agrees (para 75), so that holding is unanimous. Para 74 imposes vicarious liability, four to one.
   - Para 75: Lord Hughes calls liability under a non-delegable duty "a liability to guarantee that others provide all reasonable care".
   The monitoring content in paras 47-48 comes from the statute and regulations, as the card says. Para 37 states the duty to supervise arrangements only in general terms.
5. **May say / may not say.**
   - May say 1-4: LICENSED.
   - May say 5 (vicarious liability "without day-to-day control", paras 59-62, 65): LICENSED-NARROWER. Use the court's words: "It is not necessary for there to be micro-management, or any high degree of control" (para 65). Note that the court found "a significant degree of control" (para 62) and that the payments were allowances to defray expenses (para 59).
   - May not say 1-5: LICENSED.
6. **Central conclusions.** Bears on (a).
7. **Reader's own inference.** "The language of seeing-to-it describes the strict duty, and the language of monitoring describes the fault-based one": supported (paras 34, 37, 47). "Strict" should read "not based on personal fault" (para 32): the holder answers only if the delegate lacked care.

## 3. hughes2022rattan

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XML byte-identical. [2022] EWCA Civ 107; Bean LJ, Nicola Davies LJ and Simler LJ; heard 13 January 2022, handed down 4 February 2022; appeal from Heather Williams QC sitting as a deputy High Court judge (header). Matches.
2. **Read depth.** Paras 1-93 present.
3. **Quotations.** 66 segments, all MATCH.
4. **Holding.**
   - *The patient.* An adult (born 21 October 1956, para 9; treated 2009-2015, para 1). She was an NHS patient who paid "the NHS Charge element of her treatment" at reception (paras 10, 56(iv)), not a private fee-paying patient.
   - *Woodland criteria.* The court held the judge "right to find that the Claimant satisfied all the factors" of *Woodland* para 23 (para 71). Bean LJ discusses factors (1) to (3) expressly (para 71(1)-(3)) and does not discuss (4) and (5) separately. He refused to confine factor (1) to an "especially vulnerable" subset (para 71(1)).
   - *Result.* The non-delegable duty was upheld (paras 68, 72). Vicarious liability failed under *Barclays* "with some hesitation" (paras 88-91). The appeal was dismissed on a preliminary issue, and the merits are untried (paras 2, 91).
   The card states all of this correctly.
5. **May say / may not say.**
   - May say 1-4: LICENSED.
   - May say 5 (the NHS contract required a complaints procedure, paras 25, 55): LICENSED-NARROWER. The competence check and the quality-assurance system are clauses quoted at para 25. The complaints procedure appears only in the trial judge's summary at para 55(iii), which reads "proving a complaints procedure".
   - The card's K8 line ("any non-delegable-duty case with adult paying customers ... This is one") should read "an adult NHS patient who paid the NHS charge".
   - May not say 1-4: LICENSED.
6. **Central conclusions.** Bears on (a) and (c).
7. **Reader's own inference.** That the holder was fixed by documents close to K3's reliance ground, though the court does not reason from reliance: supported (paras 14, 69-70).

## 4. ferguson1987welsh

**Verdict: PASS-WITH-NOTES**

1. **Identity.** The saved BAILII text carries [1987] UKHL 14, [1987] 1 WLR 1553, [1987] 3 All ER 777 and [1988] IRLR 112 (the card omits the last). The order sheet reads "Die Jovis 29° Octobris 1987", with the hearing on 6-7 July and the Court of Appeal's order of 16 September 1986. Not re-fetched (bot challenge).
   - **Error in the front matter.** The `authors` field says Lord Oliver concurred "in the result with [his] own reasons". He did not: he ends "I agree, therefore, that the appeal should be dismissed for the reasons which my noble and learned friend has given" (p. 9). Four of five Lords adopted Lord Keith's reasons. The critical note's "three of five" undercounts.
2. **Read depth.** Pp. 1-11 and the order sheet are present. The page markers ('- n -') sit at the foot of each page, as the card says.
3. **Quotations.** 43 segments, all MATCH. One runs across the page break between pp. 6 and 7, as the card's "pp. 6-7" says. Two differ only by line-end hyphenation ("sub- contractor", p. 1) or spacing ("2(4)( b )", p. 11).
4. **Holding, dictum, dissent: the duty to supervise a contractor.**
   - *Holding (all five Lords).* The appeal was dismissed and no new trial was ordered against the council. The test was whether the fresh evidence would be likely to affect the result (p. 8).
   - *Majority reasoning: Lord Keith, with Lords Brandon and Griffiths and, adopting his reasons, Lord Oliver.* Section 2(4)(b) covers dangers created while the work is in progress (p. 7). It "would not ordinarily be reasonable to expect an occupier ... to supervise the contractor's activities in order to ensure that he was discharging his duty to his employees to observe a safe system of work" (p. 7). That is a general proposition in the reasoning, and by its own words it concerns supervising the contractor's duty to its own workmen. The decisive point: the evidence did not show that the council "knew or ought to have known" or "had reason to suspect" (pp. 7-8).
   - *Guarded dicta, Lord Keith.* "In special circumstances ... it might well be reasonable for the occupier to take steps to see that the system was made safe" (p. 7). The condition was not met, so the duty it describes was not applied. The occupier "might, in certain circumstances, be liable" if it did not take reasonable steps (p. 7).
   - *Dictum, Lord Oliver.* An occupier's "state of knowledge and opportunities of supervision" may make it liable, more likely as joint tortfeasor than as occupier (p. 9).
   - *Lord Goff, concurring on another ground.* The Act did not apply, because the injury did not arise from use of the premises (p. 11). His dicta: knowledge or suspicion is not "of itself" enough; an occupier may be liable to a visitor such as the postman, subject to s. 2(4)(b); joint-tortfeasor cases are different (p. 11).
5. **May say / may not say.**
   - May say 1 ("The House of Lords read s. 2(4)(b) ..."): LICENSED-NARROWER. Write "Lord Keith, with whom Lords Brandon and Griffiths agreed and whose reasons Lord Oliver adopted, read ...". Lord Goff held the Act inapplicable.
   - May say 2: LICENSED-NARROWER. Keep the purpose clause "in order to ensure that he was discharging his duty to his employees to observe a safe system of work". Without it the sentence reads as a general rule about visitors.
   - May say 3 and 4: LICENSED.
   - May not say 1-4: LICENSED. On 3, add that Lord Oliver adopted Lord Keith's reasons.
6. **Central conclusions.** Bears on (b).
7. **Reader's own inferences.**
   - That a guest is nearer Lord Goff's postman than the workman: supported as analogy (p. 11).
   - That the House imposed no duty to arrange to be told: accurate as to what is stated. But Lord Keith's test included "ought to have known" (pp. 7-8), which leaves constructive knowledge open.

## 5. naylor2004payling

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XML byte-identical. [2004] EWCA Civ 560, 7 May 2004; Waller, Latham and Neuberger LJJ; appeal from Sheffield County Court, HHJ Murphy QC. Matches.
2. **Read depth.** Paras 1-60 present. The number of para 35 lacks its full stop in the text, which is harmless.
3. **Quotations.** 44 segments, all MATCH. These include the irregular "Save in the absence of special circumstances" (para 34) and s. 2(4)(b) quoted without the second "that" (para 9), both of which the card flags correctly.
4. **Level of the non-delegable ruling, and what the Court of Appeal decided.**
   - *Trial level.* The county court judge held that the owner owed no non-delegable duty (para 1). The Court of Appeal proceeded on that footing ("Once the judge had determined ...", para 19). The text does not record whether anyone asked the Court of Appeal to revisit the point.
   - *Court of Appeal, all three judges.* Absent special circumstances there is no free-standing duty to check a contractor's insurance (paras 19-22, 34, 38, 43, 59). The duty "to take reasonable steps to satisfy himself" of the contractor's competence (para 45) was discharged by the licence check and eighteen months' experience (paras 25, 47-50). Appeal allowed, claim dismissed (order).
5. **May say / may not say.**
   - May say 1 ("not liable to a customer"): LICENSED-NARROWER. The judgment calls the claimant "a visitor to the club" (para 28) and does not say he paid; write "visitor".
   - May say 2-5: LICENSED.
   - May not say 1: LICENSED-NARROWER. "The point was not appealed" goes beyond the text; write "the Court of Appeal proceeded on the trial judge's ruling (paras 1, 19)".
   - May not say 2-4: LICENSED.
6. **Central conclusions.** Bears on (b) and (c).
7. **Reader's own inferences.**
   - "Knowledge acquired matters; a duty to acquire it is not stated": supported (paras 2, 25, 50).
   - That a host which designs the contractor's procedure may fall within Neuberger LJ's limb on an employer "responsible for the negligent way" the task was done (paras 32, 38): open. The limb is stated; the court did not apply it.

## 6. maguire2006sefton

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XML byte-identical. [2006] EWCA Civ 316, 23 February 2006; Rix, Carnwath and Jacob LJJ; appeal from Liverpool County Court. The header's "MR JUSTICE MACKAY" against para 3's "HHJ Mackay" is correctly noted on the card.
2. **Read depth.** Paras 1-35 and the order present.
3. **Quotations.** 56 segments, all MATCH (four differ by a space only).
4. **What paras 21, 24 and 30 decide.**
   - *Para 21* decides nothing. It surveys the pre-1957 implied terms: *Francis v Cockrell*'s fitness term, and McCardie J's statement in *MacLenan v Segar*, made in a case on an innkeeper's responsibility for guests' safety but stated "as to premises generally". Para 22 then says McCardie J's version had "begun to shift" away from the stricter *Francis* term.
   - *Para 24* is the holding in contract. Section 5 "was meant to do away with all such previous distinctions". The term implied by reason of the contractual right of entry is the common duty of care, so the occupier's warranty "is not a warranty that his independent contractor ... will himself take care". The sentence on "the position in contract generally" is a contrast, not a holding. The appeal was allowed on this ground.
   - *Para 30* is the holding under s. 2. The council was entitled to rely on the best-placed contractor; nothing gave it "any reason to contemplate" a deficient inspection; nothing required "special measures in controlling or supervising" it. This is the contractor defence applied in substance; Rix LJ quotes s. 2(4)(b) at para 13 as one example.
   - Para 31 acquits the council on both grounds. Para 35, Jacob LJ's "no steps" remark, is dictum.
5. **May say / may not say.**
   - May say 1-3 and 5: LICENSED.
   - May say 4 (McCardie J "stated an innkeeper's implied warranty in stricter terms"): LICENSED-NARROWER. Write: "In a case on an innkeeper's responsibility for guests, McCardie J stated, for premises generally, an implied warranty that premises are as safe 'as reasonable care and skill on the part of anyone can make them' (para 21). Rix LJ read that as a shift from the stricter *Francis v Cockrell* term (para 22) and held that s. 5 removed such distinctions (para 24)."
   - May not say 1-4: LICENSED.
6. **Central conclusions.** Bears on (b) and (c).
7. **Reader's own inference: NARROWED.** The critical note says clause 5.1.4 "forbade anyone but the contractor to open or adjust the machines" and that this "shows how delegation can remove the holder's means of learning". The clause forbids allowing anyone else "to adjust, maintain, repair, replace or remove any part of the Equipment" (para 8). It says nothing of opening or inspecting, and the court drew nothing from it. The R5a report repeats the point ("contracted away its own power to open its machines").

## 7. wong1995kwan

**Verdict: PASS**

1. **Identity.** Checked on the page images.
   - P. 1: Privy Council Appeal No. 62 of 1994, from the Court of Appeal of Hong Kong, "Delivered the 6th November 1995". Present: Lords Goff, Jauncey, Slynn, Nolan and Hoffmann; "[Delivered by Lord Slynn of Hadley]"; "[42]" at the foot of the page.
   - The full title runs "Wong Mee Wan (also known as Wong Shi (otherwise spelt Sai) Nui), the Administratrix of the estate of Ho Shui Yee, deceased v (1) Kwan Kin Travel Services Limited (2) China Travel Services Company (Zhong Shan) and (3) Pak Tang Lake Travel Services Company (Doumen County)". The card's short title is fair.
   - Printed page numbers 2-12 equal the PDF page numbers.
2. **Read depth.** Honest. The saved .txt holds twelve form feeds and no text; the PDF holds all twelve page images, and the card says it was read from them.
3. **Quotations.** 51 segments; I read every quoted passage on the images, and all are MATCH. My OCR failed on five, through misreads ("ist", "Hable", "lable") or page breaks (pp. 3-4 and 4-5); the images read "1st" and "liable", as the card has them. No OCR-DOUBT remains.
4. **Holding.** The Board found that the operator "undertook to provide and not merely to arrange" (p. 10); implied a term that the services "would be carried out with reasonable skill and care" whoever performed them (pp. 10-12); found breach (p. 11); and restored Mayo J's judgment (p. 12). The exemption clause had not been pleaded (p. 12). The card is accurate.
5. **May say 1-6 and may not say 1-5:** all LICENSED.
6. **Central conclusions.** Bears on (c).
7. **Reader's own inferences.** That the Board's remedies for the operator are "ways to shift the cost afterwards": supported (p. 11). That labels may not be conclusive: supported by "was in reality doing" (p. 10); undecided.

## 8. uk2015consumer

**Verdict: PASS**

1. **Identity.** The text rests on archive captures; live legislation.gov.uk returned 202 to me too. The version stamps in the saved files match the card: s. 2, 6 Oct; s. 48, 3 Mar; s. 54, 22 Feb; s. 55, 16 May; s. 56, 8 Mar; s. 57, 7 Mar; s. 62, 4 Mar; s. 65, 29 Oct; s. 66, 11 Mar 2026; and the revised s. 49 in `cra2015s49`, 10 Nov 2026. The commencement notes match the card. The editorial notice of ss. 12(2A) and 37(2A), inserted by 2024 c. 13, is present.
2. **Read depth.** All ten sections are saved whole.
3. **Quotations.** 55 segments, all MATCH (four differ by spacing inside the Act's own quotation marks).
4. **Holding.** Not applicable (statute). The card's readings of ss. 2(2)-(4), 48(1)-(2), 49(1), 54-57, 62, 65(1), (4)-(5) and 66(1), (4) are accurate.
5. **May say 1-5 and may not say 1-4:** all LICENSED.
6. **Central conclusions.** Bears on (c).
7. **Reader's own inferences.** All open on the texts: whether s. 57(5) catches a "no liability for suppliers" clause or an "arranging only" definition; whether a hotel stay is a "service" under s. 48(1); and how s. 49 relates to s. 5 of the 1957 Act.

## 9. eu2015package

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XHTML byte-identical (sha256 4f48c3fb2bac…). Directive (EU) 2015/2302 of 25 November 2015, OJ L 326, 11.12.2015, p. 1. Art. 28: adopt by 1 January 2018, apply from 1 July 2018. Art. 29: Directive 90/314 repealed from 1 July 2018. Matches.
2. **Read depth.** Recitals 1-54, arts 1-31 and Annexes I-III are present.
3. **Quotations.** 96 segments, all MATCH. Three are not in this text because the card attributes them elsewhere, correctly: "easily contactable" twice (art. 16a(1) of the 2026 Directive), and the old defence of Directive 90/314 (C-578/19, para 7).
4. **Absence claims.** Confirmed by my own search:
   - "natural person" occurs in recital 7 and art. 3(7) only; "human" in recital 31 only.
   - "automat" and "monitor" do not occur.
   - "supervision" occurs only in recital 42 and art. 18(2).
   - "emergency" occurs only in Annex I, Parts A-C.
5. **May say / may not say.**
   - May say 1-7: LICENSED.
   - May say 8 ("Where remedy fails, the traveller is entitled to a price reduction and to compensation, subject to three defences", art. 14(1)-(3)): LICENSED-NARROWER. Art. 14(1) gives a price reduction "for any period during which there was lack of conformity", whether or not the organiser remedied it, unless the failure is attributable to the traveller. The three defences of art. 14(3) apply to compensation.
   - May not say 1-7: LICENSED.
6. **Central conclusions.** Bears on (d) and (e).
7. **Reader's own inference: OPEN, leaning against as worded.** The card says the old defence ("could not foresee or forestall") "has no counterpart in art. 14(3)". The nearest analogue is art. 14(3)(c), read with art. 3(12): "beyond the control of the party who invokes such a situation and the consequences of which could not have been avoided even if all reasonable measures had been taken". The Court of Justice read the old defence as a fact outside "the sphere of control" (C-578/19, para 60). The paper should not say the 2015 Directive abolished the defence.

## 10. eu2026package

**Verdict: PASS**

1. **Identity.** Saved XHTML byte-identical (sha256 10f9b1f091e7…). Directive (EU) 2026/1024 of 29 April 2026, OJ L, 2026/1024, 8.5.2026.
   - Art. 3(1): measures to be adopted "By 29 September 2028" and applied "from 29 March 2029".
   - Art. 4: in force on the twentieth day after publication, which I compute as 28 May 2026.
   - Art. 5: addressed to the Member States.
2. **Read depth.** Recitals 1-33, arts 1-5 and the Annex are present.
3. **Quotations.** 57 segments, all MATCH. The three not in this text belong, as the card says, to art. 7(2)(d) and recital 34 of the 2015 Directive, or are phrases reported absent ("after the trip").
4. **Structure.** I listed the eighteen amending points of art. 1: none touches arts 13, 14, 15 or 16 or art. 7(2)(d). Recital 28 explains only the deadlines in art. 16a(2). The absence claims are confirmed. Cosmetic: art. 1(15) replaces art. 22 whole, and the seven-day refund is its new paragraph 2, so "inserting art. 22(2)" is loose.
5. **May say 1-5 and may not say 1-7:** all LICENSED. Print the 2029 date with may-say 1 (may-say 3 supplies it).
6. **Central conclusions.** Bears on (d), (e) and (f).
7. **Reader's own inference.** That art. 16a divides complaints by subject, not by date: supported (art. 16a(1)-(2)).

## 11. uk2018package

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Archive captures only; I could not reach the live site.
   - The SI 2026/455 as-made text reads "Made 22nd April 2026 / Coming into force 6th April 2027". It is signed by a Parliamentary Under-Secretary of State, Department for Business and Trade.
   - The archive capture of its contents page (29 Apr 2026), which I fetched, confirms the title and the three regulations.
   - The SI 2018/634 contents page (capture of 24 Oct 2026) says the text is up to date to 22 October 2026 and lists the SI 2026/455 effects as outstanding.
   - The R6a report's request to check regs 7, 15-18, 30, 35 and Sch. 5 against the live revised text could not be met; the archive text agrees with the card.
2. **Read depth.** The body capture holds regs 1-39; Schs 1, 2, 3 and 5 are saved.
3. **Quotations.** 70 segments, all MATCH. "human", "natural person", "automat", "supervis" and "monitor" occur in none of the 23 saved files.
4. **Provisions.**
   - SI 2026/455 amends regs 2 and 3, omits reg. 26, amends reg. 28, replaces reg. 29 with regs 29A-29B, substitutes reg. 30(1), amends regs 31-35 and omits Schs 6-10. It does not touch regs 4-8 or 15-18 or Schs 1-5, and reg. 1(4) keeps earlier contracts outside. The card is right on all of this.
   - Reg. 7(10) lists paras (1), (3)-(6) and (9) and omits (2). Reg. 7(12) creates the offence. The card's comparison of reg. 15(4) and (6) with art. 13(3)-(4) is correct.
5. **May say / may not say.**
   - May say 1-5: LICENSED.
   - May not say 2: LICENSED-NARROWER. Reg. 35 bars a civil action "by reason only of the commission of an offence". It shows that a traveller cannot sue because the contract omits a contact point. The Regulations say nothing about a claim where a contact point the contract names fails to answer. Confine the sentence to the omission.
   - May not say 1 and 3-7: LICENSED.
6. **Central conclusions.** Bears on (d), (e) and (f).
7. **Reader's own inferences.** The per-duty K5 reading is supported (regs 7(10), 7(12), 15(1), 18(1), 35). The R6a report's item 31 needs the same narrowing as may-not-say 2.

## 12. kuoni2021uksc

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Both XML files byte-identical.
   - [2021] UKSC 34: judgment given 30 July 2021, heard 1 May 2019, on appeal from [2018] EWCA Civ 938. Lord Lloyd-Jones gave judgment, with Lord Hodge, Lady Arden and Lord Kitchin agreeing; Lord Kerr, who sat in 2019, is not listed in 2021.
   - [2019] UKSC 37: 24 July 2019.
   - The Court of Justice's ruling of 18 March 2021, EU:C:2021:213, is recorded at para 26.
2. **Read depth.** [2021] paras 1-51 and [2019] paras 1-23 present.
3. **Quotations.** 55 segments, all MATCH.
4. **Holding.**
   - *Para 50.* Vicarious liability "is not relevant here". Kuoni is liable "because the services it undertook to provide were not provided with care and skill by an employee of the hotel which was a supplier of the services". That liability "does not depend on vicarious liability for the acts of an employee". Introducing vicarious liability "would defeat its purpose by rendering the pursuit of claims ... unnecessarily complex and expensive", because the hotel's liability would turn on local law. The Directive yields "a simple rule".
   - *Paras 29-32.* The holiday services are read broadly (para 29). A package provider "necessarily undertakes to provide ... other services ancillary thereto"; cleaning the hotel and "looking after and serving holidaymakers courteously" are given as examples inherent in every such contract (para 30). Helpfulness is measured against the four-star standard, adopting Longmore LJ's sentence (para 31). Guiding a guest within the hotel falls within the "holiday arrangements" (para 32). The holding follows at para 35.
   The card is accurate, including para 8 (no supervision or selection case) and the report of Longmore LJ's dissent (para 15).
5. **May say / may not say.**
   - May say 1 ("recovered from the tour operator"): LICENSED-NARROWER. The judgment decides liability and says nothing of payment; write "The Supreme Court held the tour operator liable to the guest ...".
   - May say 2-5: LICENSED.
   - The K4 line "the Supreme Court held that 'the service of looking after ...' is 'inherent in every such contract'" should read "said, as an example of ancillary services inherent in every package holiday contract".
   - May not say 1-6: LICENSED.
6. **Central conclusions.** Bears on (c) and (d).
7. **Reader's own inferences.**
   - That the old defence has no counterpart in reg. 16(4): OPEN. Reg. 2(1) defines "unavoidable and extraordinary circumstances" as beyond the party's control and unavoidable by all reasonable measures; see card 9.
   - That attending is a contractual service for package holidays: supported, narrowed as above.

## 13. kuoni2021cjeu

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XHTML byte-identical: Third Chamber, 18 March 2021, Case C-578/19. ECLI:EU:C:2021:213 appears in the saved RDF notice and at [2021] UKSC 34, para 26. Advocate General Szpunar, Opinion of 10 November 2020. Language of the case English.
2. **Read depth.** Paras 1-64 and the ruling present.
3. **Quotations.** 38 segments, all MATCH. "vicarious liability" does not occur; "vicariously liable" occurs once, at para 17.
4. **Holding.** Accurate (paras 34-35, 41-50, 56, 60-63). Para 60 ties the exemption grounds to cases where "no fault can be attributed" to the organiser or supplier, which supports the card's caution that the Court does not make control the ground of liability.
5. **May say 1-3 and may not say 1-5:** all LICENSED.
6. **Central conclusions.** Bears on (c) and (d).
7. **Reader's own inferences.**
   - That the old defence "is not among the three defences of art. 14(3)": OPEN; see card 9.
   - That "sphere of control" sits nearer K3's dependence ground than reliance: open (interpretive).

## 14. amazon2019cjeu

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Saved XHTML byte-identical: First Chamber, 10 July 2019, Case C-649/17. Parties as on the card. ECLI:EU:C:2019:576 is in the RDF notice. Advocate General Pitruzzella, Opinion of 28 February 2019. Language of the case German.
2. **Read depth.** Paras 1-54 and the ruling present.
3. **Quotations.** 44 segments, all MATCH. "human", "natural person", "automat" and "staff" do not occur in the judgment; they occur only in the Directive texts saved beside it.
4. **Holding.** Accurate (paras 41-53 and the ruling).
5. **May say / may not say.**
   - May say 1, 2 and 4: LICENSED.
   - May say 3 (a trader "need not maintain a telephone line", paras 48, 51, 52): LICENSED-NARROWER. Add "on art. 6(1)(c) as then worded". Directive (EU) 2019/2161, art. 4(4)(a)(i), applicable from 28 May 2022, now requires "the trader's telephone number and email address" without "where available". The card says this in its notes; the sentence needs it too.
   - May not say 1-5: LICENSED.
6. **Central conclusions.** Bears on (e).
7. **Reader's own inferences.**
   - That art. 3(3)(l) of Directive 2011/83 is untouched by the two amending directives: supported. Directive 2019/2161 replaces point (k) and Directive 2023/2673 replaces point (d); neither mentions (l).
   - The caution about automated premises: open.

---

## The readers' central conclusions

**(a) A non-delegable duty is strict liability with no oversight content; oversight belongs to a weaker arrange-and-supervise duty. NARROWED.**
- The duty carries no oversight content in these judgments. Lord Reed defines it as a duty "to ensure that care is taken", one that "cannot be discharged merely by the exercise of reasonable care in the selection of a third party" (*Armes* para 31). Lord Hughes calls it "a liability to guarantee that others provide all reasonable care" (para 75). *Hughes v Rattan* imposes it without any monitoring requirement (paras 68-72).
- "Strict" goes too far. Lord Reed calls it "a higher standard of care" (para 31) and a liability "based not on personal fault" (para 32); the holder answers only where the delegate failed to take care.
- Oversight does sit in the arrange-and-supervise duty: "subject to a duty to take care in making and supervising those arrangements" (para 37); "arrange for, and then monitor" (para 47). But its concrete content in *Armes* came from statute (paras 38, 48), and occupiers' law gives the entrustment defence its own limb about "the work ... being properly done" (*Ferguson* p. 7). Oversight is therefore not confined to the arranger's duty.

**(b) No ordinary duty to supervise a competent contractor; knowledge or reason to suspect ends the occupier's protection. NARROWED.**
- The first half holds.
  - "It would not ordinarily be reasonable to expect an occupier ... to supervise the contractor's activities in order to ensure that he was discharging his duty to his employees" (*Ferguson* p. 7, Lord Keith for four Lords).
  - "his obligation is limited to ensuring that the independent contractor who he has employed is competent" (*Naylor* para 19).
  - Nothing required the council "to take any special measures in controlling or supervising" the contractor (*Maguire* para 30).
- The second half overstates. Lord Keith says only that where the occupier "knows or has reason to suspect", "it might well be reasonable for the occupier to take steps to see that the system was made safe" (p. 7). That is a guarded dictum, since the condition was not met. Lord Goff refused to accept that knowledge "can of itself be enough" (p. 11), and Lord Oliver would put any such liability on a joint-tortfeasor footing (p. 9).
- *Naylor* para 50 and *Maguire* para 30 make the reasonableness of reliance turn on what the holder knew or had reason to contemplate. Lord Keith's test covers what the council "knew or ought to have known" (pp. 7-8). Read accurately: knowledge or reason to suspect may make it unreasonable to go on relying without acting.

**(c) A party that promises a service answers for its performance by others; this fails for dangers on premises. NARROWED.**
- Supported for services the party undertook to provide: "The fact that the supplier of services may under the contract arrange for some or all of them to be performed by others does not absolve the supplier" (*Wong Mee Wan* p. 4; holding p. 10).
- Three limits apply.
  - The rule holds only where the party undertook to provide and not merely to arrange, which is a matter of construction (pp. 4-5, 10).
  - Outside consumer contracts it is subject to an exemption clause (pp. 4, 11). The Consumer Rights Act ss. 57(1), (5) and 65(1) close that exit for consumers.
  - The promise is of care and skill, not safety (p. 11).
- *Kuoni* reaches the same result for packages by statute and contract (paras 45-50) and not, in terms, by a general principle. Longmore LJ's general sentence is reported, not adopted (para 15(5)).
- "Fails for dangers on premises" holds for the term implied "by reason of [the contract] conferring that right" of entry (*Maguire* paras 14, 24). Express terms, terms implied on another ground, and the "activity duty" argument are untouched (para 18). The line between premises dangers and promised services is not drawn in these texts. *Kuoni* treats cleaning the hotel and guiding a guest within it as contracted services (paras 30, 32), so the contract limb does reach some on-premises dangers when a package contract promises the service.

**(d) Package-travel law makes the organiser answer for suppliers, requires a contact point and assistance, and stops at packages. CONFIRMED, with three precisions.**
- The texts support each element.
  - The organiser answers for suppliers: art. 13(1) ("irrespective of whether those services are to be performed by the organiser or by other travel service providers"); reg. 15(2); *Kuoni* paras 45-50.
  - A contact point: art. 7(2)(d); Sch. 5, para. 4.
  - Assistance: art. 16; reg. 18.
  - Packages only: art. 2(1), art. 3(2), recitals 15, 17 and 18; reg. 2(5).
- Three precisions.
  - The contact point is a requirement about the content of the contract. In the United Kingdom it is enforced by prosecution, with no civil action by reason only of the offence (regs 7(10), 7(12), 35).
  - The duty to remedy yields to impossibility and disproportionate cost (art. 13(3)), and defences and a cap apply (art. 14(3)-(4)).
  - Price reduction runs for any period of non-conformity whether or not it was remedied (art. 14(1)).

**(e) No text requires a person with authority at the contact point. CONFIRMED.**
- Art. 7(2)(d) and Sch. 5, para. 4 allow "the organiser's local representative, ... a contact point or ... another service".
- The 2026 duty is to be "easily contactable ... and able to respond efficiently" (art. 16a(1)).
- My whole-text searches of all three instruments found no "human" (except "human health"), no "automat" and no requirement of a natural person at the contact point.
- The Court of Justice accepted "an electronic enquiry template" and "instant messaging or a telephone callback system" (*Amazon* para 52).
- Caveat: a "local representative" is one permitted option, and "able to respond efficiently" may imply some capacity to act on remedy queries. No text says so.

**(f) The dates from which Directive (EU) 2026/1024 and the UK amending instrument apply. CONFIRMED.**
- Directive (EU) 2026/1024: Member States must adopt the measures "By 29 September 2028" and "shall apply those measures from 29 March 2029" (art. 3(1)). It entered into force on the twentieth day after publication on 8.5.2026 (art. 4), which is 28 May 2026 on my computation.
- SI 2026/455: made 22 April 2026, "come into force on 6th April 2027" (reg. 1(1)). Its amendments do not affect package travel contracts or linked travel arrangements "entered into before the commencement date" (reg. 1(4)).

---

## Table: every FAIL, every quotation not MATCH, every sentence not LICENSED

| # | Card | Item | Finding | Narrower wording or fix |
|---|---|---|---|---|
| — | all | FAIL | None | — |
| — | all | Quotations not MATCH | None of 776 segments | — |
| 1 | barclays2020uksc | May say 1 | LICENSED-NARROWER: para 7 quotes Lord Bridge in stating the Bank's position | Cite paras 7, 24, 27 together; the holding is at 24 and 27 |
| 2 | armes2017uksc | May say 5 | LICENSED-NARROWER: "without day-to-day control" | "not necessary for there to be micro-management, or any high degree of control" (para 65); the court found "a significant degree of control" (para 62) |
| 3 | hughes2022rattan | May say 5 | LICENSED-NARROWER: the complaints procedure is from the trial judge's summary | "and, as the trial judge summarised it, to provide a complaints procedure (para 55(iii))" |
| 4 | hughes2022rattan | K8 line ("adult paying customers") | Narrower | "an adult NHS patient who paid the NHS charge (paras 9-10, 56)" |
| 5 | ferguson1987welsh | May say 1 | LICENSED-NARROWER: "The House of Lords read" | "Lord Keith, with whom Lords Brandon and Griffiths agreed and whose reasons Lord Oliver adopted, read ..."; Lord Goff held the Act inapplicable (p. 11) |
| 6 | ferguson1987welsh | May say 2 | LICENSED-NARROWER: drops the purpose clause | Add "in order to ensure that he was discharging his duty to his employees to observe a safe system of work" (p. 7) |
| 7 | ferguson1987welsh | Front matter `authors`; critical note "three of five" | Error: Lord Oliver adopted Lord Keith's reasons (p. 9) | Four of five adopted Lord Keith's reasons; only Lord Goff gave his own |
| 8 | naylor2004payling | May say 1 | LICENSED-NARROWER: "customer" | "a visitor to the club" (para 28) |
| 9 | naylor2004payling | May not say 1 | LICENSED-NARROWER: "the point was not appealed" | "the Court of Appeal proceeded on the trial judge's ruling (paras 1, 19)" |
| 10 | maguire2006sefton | May say 4 | LICENSED-NARROWER: McCardie J's warranty | Stated "as to premises generally" in an innkeeper case; Rix LJ saw it as a shift from the stricter *Francis* term (para 22); s. 5 removed such distinctions (para 24) |
| 11 | maguire2006sefton | Critical note on clause 5.1.4 (and R5a report) | Paraphrase error: the clause does not mention opening or inspecting | The clause bars others from "adjust, maintain, repair, replace or remove any part" (para 8); drop "open" and "removed the holder's means of learning" |
| 12 | eu2015package | May say 8 | LICENSED-NARROWER: price reduction is not conditional on a failed remedy | Price reduction for any period of non-conformity unless attributable to the traveller (art. 14(1)); the three defences apply to compensation (art. 14(3)) |
| 13 | eu2015package, kuoni2021cjeu, kuoni2021uksc | "Old defence has no counterpart" | Reader's inference left OPEN, leaning against | Art. 14(3)(c) with art. 3(12) (reg. 16(4)(c) with reg. 2(1) in the UK) is the nearest analogue; do not say the defence was abolished |
| 14 | uk2018package | May not say 2 (and R6a item 31) | LICENSED-NARROWER: "absence or failure" | Confine to absence: no civil action "by reason only of the commission of an offence" (reg. 35); failure of a named contact point is not addressed |
| 15 | kuoni2021uksc | May say 1 | LICENSED-NARROWER: "recovered" | "The Supreme Court held the tour operator liable to the guest ..." (paras 45-46, 49) |
| 16 | kuoni2021uksc | K4 line ("held ... inherent in every such contract") | Narrower | "said, as an example of ancillary services inherent in every package holiday contract (para 30)" |
| 17 | amazon2019cjeu | May say 3 | LICENSED-NARROWER: omits the change of wording | Add "on art. 6(1)(c) as then worded"; Directive 2019/2161 now requires the telephone number, from 28 May 2022 |

<!-- Independent verification of cards, batch CV-B, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-B (run rr-2026-11-k)

**Scope.** Fourteen cards in `library/cards/`: eight from reader R4b (`rasnick2011krishna`, `hoyt2013gutterz`, `groh2015westin`, `thomas1955pick`, `blackstone1768commentaries`, `digest4_9`, `bgb701`, `coe1962hotelkeepers`) and six from reader R5b (`hayman1987ramada`, `mobil1995bransford`, `airbnb2019cjeu`, `uber2017cjeu`, `eu2022dsa`, `eu2019p2b`). I did not write any of them. I edited no card and no other file, and committed nothing.

**What I did.**
- *Identity.* I fetched the Caselaw Access Project (CAP) case record for each of the six American cases, and the EU Publications Office metadata (ECLI, date, formation, in-force flag, linked acts) for the two judgments and the two regulations. On 11 Nov 2026 I re-fetched the six CAP opinions, the four EU texts and the five BGB pages; every one was byte-identical to the saved copy.
- *Quotations.* I read each saved text and each card. So that no quotation escaped, I also ran a matcher (my own script in the session scratchpad, reading the saved texts as data) over every double-quoted string in each card's body. It normalises whitespace, line-end hyphens, curly quotes, CAP star-page marks and, for Blackstone, Avalon's long s printed as "f". I then checked the locator of every quotation by hand (for the two regulations, against an article-and-recital map of the text). Counts below are quotation instances: a phrase quoted twice counts twice. Strings a card quotes from CLAIMS_FIXED, v6, the scout or another card are not quotations of the source; I list them per card and checked them where it mattered.
- *Status.* Each card's head 7 says what I fetched and what failed.

Verdicts: 0 PASS, 14 PASS-WITH-NOTES, 0 FAIL. Quotation instances checked: 656; MATCH 652; OCR-DOUBT 4; LOCATOR-WRONG 0; NOT-FOUND 0; PARAPHRASED-AS-QUOTE 0. 'May say' sentences: 78; LICENSED 52; LICENSED-NARROWER 26; NOT-LICENSED 0.

---

## rasnick2011krishna

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CAP record: *Rasnick v. Krishna Hospitality, Inc.*, 289 Ga. 565, parallel 713 S.E.2d 835, Supreme Court of Georgia, docket S10G0971, decided 2011-07-05, pp. 565–573; majority Hines J.; dissent by Carley P.J. (OCR "CAKLEY"). The saved text gives "Reconsideration denied July 21, 2011" and "Chief Justice Hunstein and Justice Benham join in this dissent" (573). No mismatch.
2. **Read depth.** The saved text holds the whole majority, both footnotes and the dissent (565–573). 'full-text' is honest.
3. **Quotations.** 47 instances, all MATCH, every locator right. The CAP HTML italicises "internal to the guest." and "An innkeeper is under a similar duty to his guests.", as the card says. Not source quotations: "three justices dissented", "no duty to aid", "declined to adopt subsection (2)" (the card's and the scout's words, presented as such).
4. **Holding, dictum, dissent.** The motel won: "Judgment affirmed." (570). On a relative's telephone calls the majority decided exactly this: Georgia will not "judicially engraft ... the additional duty upon innkeepers to investigate or check on their guests to determine if they are in medical need" (570). It treated the wife's calls as going to foreseeability, which "does not mandate the expansion of traditional tort concepts" (569), and it asked who could trigger such a duty, "from a family member or ... a friend or colleague" (569). It reserved "whether any duty to render or summon medical aid as may be set forth in Section 314A (2) should be adopted in Georgia" (570) and affirmed the premises duty (567). The dissent (Carley P.J., Hunstein C.J., Benham J.) would let a jury find that the motel "had reason to know" Mr Rasnick was ill (572).
   - *§ 314A as the majority quotes it (568), whole:* "(1) A common carrier is under a duty to its passengers to take reasonable action (a) to protect them from unreasonable risk of physical harm, and (b) to give them first aid after it knows or has reason to know that they are ill or injured, and to care for them until they can be cared for by others. (2) An innkeeper is under a similar duty to his guests. (3) A possessor of land who holds it open to the public is under a similar duty to members of the public who enter in response to his invitation. (4) One who is required by law to take or who voluntarily takes the custody of another under circumstances such as to deprive the other of his normal opportunities for protection is under a similar duty to the other." followed by "(Emphasis supplied.)"; title given as "Special Relations Giving Rise to Duty to Aid or Protect".
   - *As the dissent quotes it (571), in part and spliced:* an "innkeeper is under a . . . duty to his guests" "(a) to protect them against unreasonable risk of physical harm, and (b) to give them first aid after it knows or has reason to know that they are ill or injured, and to care for them until they can be cared for by others."
   - *Not identical.* (1)(a) reads "from" in the majority and "against" in the dissent (and in *Groh* ¶ 29); the dissent also fuses (2) into the words of (1) and omits (3)–(4). The card records the from/against difference and not the splice.
   - The Summary's "The majority declined to adopt Restatement (Second) of Torts § 314A on these facts" is looser than the text, which declines to "engraft" an additional duty and reserves § 314A(2). The card's own critical note states it correctly.
5. **May say (7): 5 LICENSED, 2 LICENSED-NARROWER.**
   - S1 (premises duty, 567): LICENSED. S3 ("a moral or humane obligation ...", 570): LICENSED. S4 (left open, 570): LICENSED. S5 (§ 314A as quoted at 568): LICENSED. S7 (dissent, "had reason to know", 572): LICENSED.
   - S2: LICENSED-NARROWER. The holding is about checking on a guest's medical condition. Narrower: "The Supreme Court of Georgia held that a motel had no legal duty to investigate or check on a guest to determine whether he was in medical need, for a condition unrelated to his stay, after his wife telephoned, said she was worried and asked that someone check on him (568, 570; n. 1), with three justices dissenting."
   - S6: LICENSED-NARROWER. The calls and the hang-up are the wife's deposition testimony as the Court of Appeals set it out (n. 1) and as the dissent recounts it (572), on summary judgment. Narrower: "According to the wife's testimony as the court recounts it, an operator hung up on her and her later calls met a recorded message (n. 1; dissent, 572)."
   - May not say (7): all sound.
6. **K claims.** K4: agree (567; 569–570). K7: the card's headline, "refutes the conclusion as a statement of Georgia law", outruns its own body, which says the case "attacks P1 for medical peril". The court denied the underlying duty because the risk was "not internal to the premises but rather internal to the guest" (568); it said nothing about whether a holder of a duty must keep a channel. I read it as narrowing P1, not refuting C. K3: agree that it narrows dependence, but "unable to call for help" is the card's inference; the opinion says he was found the next morning "unable to get up" (565). K9: agree, a fact pattern only.
7. **Later history.** Not flagged by the reader; not checked.

## hoyt2013gutterz

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CAP record: 829 N.W.2d 772, Iowa Supreme Court, No. 11-0085, decided 2013-04-05, pp. 772–785; Hecht J.; Waterman J. dissenting with Cady C.J. and Mansfield J. No mismatch.
2. **Read depth.** Majority, footnotes 1–6 and dissent are all in the saved text. Honest.
3. **Quotations.** 43 instances: 42 MATCH, 1 OCR-DOUBT. "an altercation might occur" (773): the saved text prints "ah altercation"; the card discloses its repair. Not source quotations: "the Iowa Supreme Court, quoting a comment to § 40" (the card's suggested attribution), "US law".
4. **Holding.** The court held that Gutterz "owed Hoyt a duty of reasonable care under the circumstances presented here" (777), moved foreseeability to breach and scope, and reversed summary judgment and remanded "for trial" (782). Nobody was held liable. The dissent accepts the duty ("The duty owed is one of reasonable care", 784) and would affirm on breach and scope (782).
   - *§ 40 as quoted (776):* "(a) An actor in a special relationship with another owes the other a duty of reasonable care with regard to risks that arise within the scope of the relationship. (b) Special relationships giving rise to the duty provided in Subsection (a) include: (1) a common carrier with its passengers, (2) an innkeeper with its guests, (3) a business or other possessor of land that holds its premises open to the public with those who are lawfully on the premises," then "Restatement (Third) § 40, at 39 (2012)." The card records it exactly, including the closing comma.
5. **May say (4): 3 LICENSED, 1 LICENSED-NARROWER.**
   - S1, S2, S4: LICENSED.
   - S3: LICENSED-NARROWER. The comment says the relationship gives a more limited incursion on autonomy, "especially when the relationship is entered into voluntarily"; voluntariness strengthens the first reason and is not a reason of its own, and the card drops the third reason, benefit. Narrower: "The court found applicable to taverns the Restatement's justifications that the relationship 'identifies a specific person to be protected and thus provides a more limited and justified incursion on autonomy, especially when the relationship is entered into voluntarily', that 'some relationships necessarily compromise a person's ability to self-protect', and that 'Many of the relationships also benefit the actor' (777)."
   - May not say (5): all sound.
6. **K claims.** K4: agree (777, 780). K3: agree, with the voluntariness correction above. K5: thin. "identifies a specific person to be protected" justifies a narrower incursion on autonomy; it does not speak of the patron's claim. The patron's suit in his own name is the better evidence. K7: agree it is a lead only; note that the majority itself cites *Regan v. Denbar* at 780 for "a call to the police may have been warranted".
7. **Later history.** Not flagged; not checked.

## groh2015westin

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CAP record: 347 P.3d 606, parallel 2015 CO 25, Colorado Supreme Court, No. 13SC382, decided 2015-04-13, pp. 606–620; Hood J.; Eid J. dissenting, joined by Coats J. The saved text gives "Rehearing Denied May 11, 2015". No mismatch. The card's paragraph numbers agree with the OCR sequence ("T1" ... "1389" ... "51"; dissent "152"–"61"). I could not check them against the official opinion: the Colorado Judicial Branch URL I tried returned an HTML page, not the opinion.
2. **Read depth.** Majority ¶¶ 1–51, footnotes 1–10 (the HTML labels them 1–10) and dissent ¶¶ 52–61 are present. A stray "*" after dissent ¶ 57 has no footnote in the HTML. Honest.
3. **Quotations.** 65 instances: 62 MATCH, 3 OCR-DOUBT, each with the card's bracketed repair disclosed: the holding at ¶¶ 4, 51 ("eviets", "cireumstances"), § 314A at ¶ 29 ("cam"), ¶ 40 ("seope"). The card renders inner double quotes as single, as it announces. "from unreasonable risk" is quoted from *Rasnick* at 568, where it matches.
4. **Holding.** The court held that "a hotel that [evicts] a guest has a duty to exercise reasonable care under the [circumstances]" (¶¶ 4, 51), found fact issues on negligence and negligent hiring and training, held the Dram Shop Act inapplicable, and affirmed and remanded. At ¶ 37 the holding rests on the duty factors "coupled with the special relationship". No liability was found. The dissent calls the duty "entirely unremarkable" (¶ 52) and would grant summary judgment (¶¶ 54, 57).
5. **May say (6): 5 LICENSED, 1 LICENSED-NARROWER.**
   - S1–S4, S6: LICENSED. On S1, ¶ 37 couples the relationship with policy factors; the card's critical note says so.
   - S5: LICENSED-NARROWER. ¶ 38 reads "we are not implicitly holding that hotels must provide safe transportation off premises during eviction"; that is a disclaimer, not a refusal. Narrower: "... and said it was not holding that hotels must provide safe transportation off the premises (¶ 38)."
   - May not say (6): all sound.
6. **K claims.** K4, K5, K7: agree (¶¶ 4, 32, n. 7; ¶¶ 40–43). K3: the "dependent or mutually dependent relationship" passage (¶ 29) restates *Whitlock*'s observation that the law "appears 'to be working slowly'" toward such a duty; the operative ground is the "special relationship" with the policy factors (¶¶ 32, 37). Support for dependence is indirect.
7. **Later history.** Not flagged; not checked.

## thomas1955pick

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CAP record: 224 F.2d 664, Tenth Circuit, No. 5079, decided 1955-07-14, pp. 664–666; Murrah J. The panel line reads "Before BRATTON and MURRAH, Circuit Judges, and WALLACE, District Judge." (665). No mismatch.
2. **Read depth.** Whole opinion. Honest.
3. **Quotations.** 34 instances, all MATCH, locators right.
4. **Holding.** The appellant won a reversal, on contract only, at the pleading stage. The court classed the common-law claim as tort and held it time-barred, held the statutory claim barred because the statute is "merely declaratory of the common law", and held that "the complaint states a claim on an express contract" within the three-year period (666).
5. **May say (3): 1 LICENSED, 2 LICENSED-NARROWER.**
   - S1: LICENSED.
   - S2: LICENSED-NARROWER. The court says contracts "are usually treated as the means for the inducement or establishment" of the relationship (665); keep "usually".
   - S3: LICENSED-NARROWER. The facts are the pleadings "as we summarize them" (665), and the guest did not succeed on both. Narrower: "A guest who alleged that he was refused on arrival despite a confirmed reservation pleaded both the innkeeper's duty and the contract; the court held the common-law and statutory claims time-barred and the contract claim well pleaded (665–666)."
   - May not say (5): all sound.
6. **K claims.** Agree. Add for K4: the duty is described "to provide accommodations without discrimination" (666) in a race case; K4's conditions (capacity, fitness, payment) are not addressed.
7. **Later history.** Not flagged; not checked.

## blackstone1768commentaries

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** Avalon's contents page (saved) names "First Edition / Oxford : Printed at the Clarendon Press, 1765-1769". The Internet Archive catalogue (fetched 11 Nov 2026) has item 10518707bsb, "Commentaries On The Laws Of England. 3", date 1768, "Oxford : Clarendon Press (1768)", Bayerische Staatsbibliothek, and its companion 10518708bsb, vol. 4, dated 1769. Those catalogue records support 1768 for book 3 and give 1769 for book 4; no title page seen. A citation of 4 Comm. 167–168 should carry 1769, not the citekey's 1768. Avalon's ".P n" marks the start of page n (the signature marks "W" and "W 2" fall at the foot of pp. 161 and 163, both rectos), so the locators 161, 163, 164, 167 and 168 are right.
2. **Read depth.** 3 Comm. 161–166 and 4 Comm. 167–168 are in the saved files. Honest.
3. **Quotations.** 59 instances, all MATCH (long s, spacing before ; and : normalised as announced; "hufinefs" bracketed). Not source quotations: "offers his house" (twice) and "3 Bl Comm 165", both confirmed on `burdick1911origin.md` line 33; "inns only".
4. **What the card misses on p. 167.** Blackstone writes that "The nature of common nusances, and their distinction from private nusances, were explained in the preceding volume", with note m, "Vol. III. pag. 216.", and gives as item 2: "All those kinds of nusances, (such as offensive trades and manufactures) which when injurious to a private man are actionable, are, when detrimental to the public, punishable by public prosecution" (Avalon long s modernised). And the traveller's action at 3 Comm. 164 lies "upon this universal assumpsit", in implied contract, not as a suit for nuisance. The sentence "indictable only, and not actionable" (167) is about suits for a common nuisance and does not contradict an action in assumpsit. The card's "Two routes, not reconciled" and "He does not cross-refer" overstate a tension the texts do not show; Blackstone does cross-refer, to a page nobody read.
5. **May say (4): all LICENSED.** May not say (6): all sound; the third ("That Blackstone explains how the action and the indictment fit together") holds for inns, but should not be turned into a claim that his two books conflict.
6. **K claims.** K5: agree that both routes existed; disagree that they stand in tension (see 4). K3, K4: agree.
7. **Status.** Volume dates as in 1.

## digest4_9

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** The Latin Library file is headed "Dig. 4.9.0. Nautae caupones stabularii ut recepta restituant." (line 12 of the saved full file); Scott's page is headed "S. P. Scott, The Civil Law, III, Cincinnati, 1932". The extracts match the full files for every string I tested. No editor is named for the Latin, as the card says.
2. **Read depth.** The whole title, 4.9.1 pr. to 4.9.7.6, is present in both languages. Honest.
3. **Quotations.** 37 instances (Latin and Scott), all MATCH, locators right. The English glosses are faithful, with two cautions. At 4.9.7.4 the card, like Scott, renders "alienos" as "others' slaves"; the Latin sets "alienos" against "suis" (his own slaves) and does not say slaves. At 4.9.7.6, "puto etiam hanc actionem in solidum eos pati debere", the card's "them" can be read as the son or slave; the parallel at 4.9.3.3 ("voluntas patris domini intervenit, in solidum erit conveniendus") points to the father or master as the one liable in full. Do not cite 4.9.7.6 for the personal liability of the son or slave.
   - *Does D. 4.9.1.1 say an innkeeper may refuse a traveller?* Yes. "ne quisquam putet graviter hoc adversus eos constitutum: nam est in ipsorum arbitrio, ne quem recipiant": nobody should think this harsh on them, for it is in their own discretion to receive no one. "eos" and "ipsorum" are the seamen, innkeepers and stable-keepers of the edict together; "quem" is personal; Scott gives "they have the choice of refusing to receive anyone". Ulpian states no condition and uses the freedom to justify the strict liability. One caution: "recipere" is also the edict's word for taking goods into safekeeping (4.9.1 pr., 4.9.1.8), and the text alone does not settle whether the freedom is to refuse lodging or to decline the undertaking of custody. The card's reading is the plain one.
4. **What the card leaves unreconciled.** The card quotes 4.9.6.3, "In factum actione caupo tenetur pro his, qui habitandi causa in caupona sunt: hoc autem non pertinet ad eum, qui hospitio repentino recipitur, veluti viator", but never squares it with 4.9.2, "Sicut et caupo viatorum". Read with 4.9.6.2 (damage by "alio, qui in eadem nave vel caupona est"), 4.9.6.3 limits the innkeeper's liability, under the action for double of frr. 6–7, to the acts of residents, and excludes a transient guest such as a traveller. Under the action on the receipt (frr. 1–5) he answers for travellers.
5. **May say (5): 2 LICENSED, 3 LICENSED-NARROWER.**
   - S2 (Ulpian's reasons, 4.9.1.1): LICENSED; the reasons are given for seamen, innkeepers and stable-keepers alike. S5 (ship's operator, "suo periculo"; 4.9.7 pr., 4.9.7.6): LICENSED.
   - S1: LICENSED-NARROWER. The edict reaches "quod cuiusque salvum fore receperint", what they received from anyone, and only in the course of business (4.9.3.2); the person with the interest sues (4.9.1.7). Narrower: "The praetor's edict gave an action against an innkeeper who did not restore what he had received in the course of his business, and the liability did not depend on fault, save for unavoidable accident and irresistible force (D. 4.9.1 pr.; 4.9.3.1–2)."
   - S3: LICENSED-NARROWER. 4.9.6 pr. says that a gratuitous lodger is not denied "in factum actiones ... si damnum iniuria passus es", the actions for loss wrongfully suffered, which the card itself assigns to frr. 6–7. Narrower: "The innkeeper was paid for letting travellers stay and not for custody (D. 4.9.5 pr.), and a person lodged without charge was not denied the actions in factum for loss wrongfully suffered (D. 4.9.6 pr.)."
   - S4: LICENSED-NARROWER. Narrower: "Under the action on the receipt the innkeeper answered for the acts of travellers (D. 4.9.2); under the action for double he answered for those living at the inn but not for a transient guest such as a traveller (D. 4.9.6.3)."
   - May not say (5): all sound. Add 4.9.1.3 to the third: it too is said of ships ("in navibus"), yet the card files it under "Those placed in a post bind the operator" without that label.
6. **K claims.** K4: agree; the title denies a duty to admit in terms (4.9.1.1). K5: agree, with the 4.9.6.3 limit. K7/K8: agree that fault lies in selection (4.9.7.4).
7. **Later history.** Not flagged; not checked.

## bgb701

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** I re-fetched the five pages (§§ 701, 702, 702a, 703, 704) from gesetze-im-internet.de on 11 Nov 2026; each is byte-identical to the saved copy, so the amounts are as served today. The card's venue calls the English text the "official English translation". The page itself says "Translation provided by Langenscheidt Übersetzungsservice, updated by Neil Mussett. The translation has most recently been revised and updated by Samson Übersetzungen GmbH". It is a translation hosted on the federal site, not an authentic text; the venue line should say so (the card's critical notes already treat it as a convenience).
2. **Read depth.** The five sections, whole. Honest.
3. **Quotations.** 29 instances (German and translation), all MATCH. The card's remark that the translation adds "first" at § 701(2) no. 2 is right. Not a quotation: "my paraphrase".
4. Not a judgment.
5. **May say (5): 2 LICENSED, 3 LICENSED-NARROWER.**
   - S2 (§ 702a(1)) and S5 (no duty to admit, nothing on the person, §§ 701–704 being the whole of Titel 15): LICENSED.
   - S1: LICENSED-NARROWER. Add the exclusions: loss caused by the guest, a companion, a person the guest took in, the nature of the things or "höhere Gewalt" (§ 701(3)); vehicles, things left in them and live animals (§ 701(4)). "Whether or not at fault" remains a reading of the structure.
   - S3: LICENSED-NARROWER. Add the exception in § 702(3): valuables of excessive value or bulk for the size or standing of the inn, or dangerous, may be refused; the cap is lost only for a refusal "entgegen der Vorschrift des Absatzes 3".
   - S4: LICENSED-NARROWER. Add § 703, second sentence: no lapse where the innkeeper took the things into safekeeping or he or his people were at fault.
   - May not say (5): all sound. On the third: Germany ratified ETS No. 41 on 14 Nov 1966 (see coe1962hotelkeepers, head 7); that §§ 701–704 implement it still needs a source.
6. **K claims.** Agree.
7. **Status.** Text as served on 11 Nov 2026 is identical to the saved text.

## coe1962hotelkeepers

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** ETS No. 41, Paris, 17.XII.1962, from the saved Council of Europe PDFs; Tractatenblad 1963 no. 44 titles it "Overeenkomst nopens de aansprakelijkheid van hotelhouders voor de zaken van hun gasten, met Bijlage". No mismatch.
2. **Read depth.** Convention and annex, whole. Honest.
3. **Quotations.** 33 instances, all MATCH, including the French "objets apportés par les voyageurs" and "le voyageur qui y descend et y dispose d'un logement" (Trb. 1963 no. 44).
4. Not a judgment.
5. **May say (5): 2 LICENSED, 3 LICENSED-NARROWER.**
   - S1 (Annex arts 1(1), 1(3), 4) and S5 (property only): LICENSED.
   - S2: LICENSED-NARROWER. Annex art. 6 is subject to Convention art. 2(d), under which a state may permit a reduction "by an agreement with the guest signed by him and containing no other terms" in deposit and fault cases short of intent.
   - S3: LICENSED-NARROWER. Add "he may only refuse to receive such property if it is dangerous or if, having regard to the size or standing of the hotel, it is of excessive value or cumbersome" (Annex art. 2(2)).
   - S4: LICENSED-NARROWER. Add "Except in any case to which Article 4 of this Annex applies" (fault).
   - May not say (5): sound as written; the first two can now be relaxed for a dated statement (head 7).
6. **K claims.** Agree.
7. **Status: entered into force on 15 February 1967; parties established as of 19 March 2014.**
   - Netherlands treaty database (Ministry of Foreign Affairs, verdragenbank.overheid.nl, treaty 004696, page and XML fetched 11 Nov 2026): "In werking 15-02-1967"; no entry-into-force date for any part of the Kingdom. The Netherlands signed and is not a party.
   - Council of Europe Treaty Office chart for CETS 041, archived capture of 19 March 2014 (`web.archive.org/web/20140319214254/http://www.conventions.coe.int/Treaty/Commun/ChercheSig.asp?CL=ENG&CM=&NT=041&DF=&VL=`): entry into force 15/2/1967, "Conditions: 3 Ratifications", "Total number of ratifications/accessions: 17". In force for (date of entry into force): Belgium 15/12/1972; Bosnia and Herzegovina 30/3/1995 (succession); Croatia 15/12/1994 (succession); Cyprus 6/4/1984; France 19/12/1967; Germany 15/2/1967; Ireland 15/2/1967; Italy 12/8/1979; Lithuania 30/4/2004; Luxembourg 26/4/1980; Malta 13/3/1967; Montenegro 6/6/2006 (accession by the state union of Serbia and Montenegro); Poland 19/6/1997; Serbia 29/5/2001 (accession); Slovenia 21/1/1993 (succession); "The former Yugoslav Republic of Macedonia" 1/7/1994 (succession); United Kingdom 15/2/1967. Signed, not ratified: Austria, Georgia, Greece, Netherlands, Turkey. The chart's notes columns carry marks for France, Germany, Greece and Malta that I did not decode.
   - Tried and failed: coe.int Treaty Office, current and legacy URLs (HTTP 403). Present status, including any denunciation since 2014, is not established; check the live chart before stating it.

## hayman1987ramada

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CAP record: 86 N.C. App. 274, North Carolina Court of Appeals, No. 8721SC45, filed 1987-07-07, pp. 274–282; Becton J.; "Judge Martin concurs" (he joined; there is no concurring opinion, so the card's "Martin, J., concurring" should not be read as one); Cozort J. dissenting. Order at 320 N.C. 631: Supreme Court of North Carolina, No. 432A87, 1987-09-03. No mismatch.
2. **Read depth.** Whole opinion and order. Honest.
3. **Quotations.** 52 instances, all MATCH, including *Crinkley* fn 3. Not a source quotation: "where the guest's employer, not the guest, had chosen the motel" (it is in `DRAFT_v6.md`). Two errors of statement:
   - The card says "The words 'required' and 'necessity' do not occur in the opinion". "required" does occur: "defendant required Turnpike, pursuant to the license agreement" (279), and the dissent's "did not require Turnpike" (281). What holds is that neither word is used of the guest's stay. `WS_P4_R5b.md` repeats the slip ("it uses neither word").
   - The hold_rationale says v6 reports *Hayman* "through Crinkley's footnote 3, which gives only one of the court's two reasons". The footnote gives both: "The Hayman majority also thought that the evidence failed as a matter of law to establish that there was any effective misrepresentation of the franchisor-franchisee relationship." Whatever v6 omits, the footnote is not why.
4. **Holding; test; deciding facts.** The franchisor won: summary judgment affirmed, two to one. Actual agency: liability "depends upon the existence of an agency relationship, which is determined by the nature and extent of control and supervision retained and exercised by the franchisor over the methods or details of conducting the day-to-day operation" (277). Apparent agency: "Where a person by words or conduct represents or permits it to be represented that another person is his agent, he will be estopped to deny the agency as against third persons who have dealt, on the faith of such representation, with the person so held out as agent" (278). What decided it: a licence setting standards for "construction, furnishing, and advertising", nothing on security beyond a duty to keep the inn "in a clean, attractive, safe and orderly manner", no control of personnel, and only rights to inspect and terminate (278); a licence clause requiring the operator to identify itself in advertising, on stationery and on a front-desk sign, with no evidence of non-compliance or of the franchisor's acquiescence (279); a stay arranged by the employer, with no allegation that she would have chosen otherwise (279). The dissent would have sent apparent agency to trial (281–282).
5. **May say (6): 5 LICENSED, 1 LICENSED-NARROWER.**
   - S2–S6: LICENSED.
   - S1: LICENSED-NARROWER. *Hayman* was filed 7 July 1987 and *Crinkley* decided 7 April 1988 (saved *Crinkley* text, line 18): nine months. Say "In 1987, the year before Crinkley, ...".
   - May not say (7): all sound; the fourth can now be stated positively (head 7).
6. **K claims.** K8 and K3: agree. Add the later treatment in head 7: in 1988 the same court applied *Hayman* to dismiss claims against a Ramada franchisor, which strengthens the card's reading.
7. **Later history: settled as far as the North Carolina reports show.**
   - CAP case lists for N.C. Reports vols 320–324 and N.C. App. vols 86–90 (fetched 11 Nov 2026): docket 432A87 appears only at 320 N.C. 631. I found no opinion of the Supreme Court of North Carolina in *Hayman*.
   - The Court of Appeals cites the case twice in 1988, with this history: "Hayman v. Ramada Inn, Inc., 86 N.C. App. 274, 357 S.E. 2d 394, disc. rev. on additional issues denied, 320 N.C. 631, 360 S.E. 2d 87 (1987)" (*Clark v. Inn West*, 89 N.C. App. 275 (1988)), and "disc. rev. denied, 320 N.C. 631, 360 S.E. 2d 87 (1987)" (*Brown v. Lumbermens Mutual Casualty Co.*, 90 N.C. App. 464 (1988)). I read only the passages citing *Hayman*, from the CAP records.
   - *Clark* applied it to a Ramada franchisor: "this Court held in Hayman ... that a franchisor is not responsible for the torts of its franchisee unless a principal-agent relationship is alleged". The Supreme Court's opinion in *Clark* (324 N.C. 415 (1989)) turned on the Dram Shop Act and does not mention *Hayman* or the franchisor (searched).
   - *Crinkley*'s "rev. granted in part" finds no support in the reports I read. The 'A' in the docket fits an appeal of right on the dissent, but I found no decision on one. CourtListener requires a login; I did not use it.

## mobil1995bransford

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CAP record: 648 So. 2d 119, Florida Supreme Court, No. 80310, decided 1995-01-05, pp. 119–124; per curiam; Shaw J. dissenting; Grimes C.J., Overton, Kogan and Harding JJ. and McDonald, Senior Justice, concurring (OCR "MeDONALD"). The saved text gives "Rehearing Denied Feb. 17, 1995". No mismatch.
2. **Read depth.** Whole; the garbled paragraph at 121 is disclosed. Honest.
3. **Quotations.** 41 instances, all MATCH, including *Crinkley*'s "did not know the difference between a franchise inn and a company owned inn". One statement rests on OCR: the card's account of the underlying operator claims (negligent retention and inadequate security) comes from the garbled paragraph at 121.
4. **Holding; test; deciding facts.** Mobil won: the district court's decision was quashed and summary judgment for Mobil reinstated, five to one. The test for agency: a franchisor that "has directly or apparently participated in some substantial way in directing or managing acts of the franchisee, beyond the mere fact of providing contractual franchise support activities" (120). Apparent agency: "(a) a representation by the purported principal; (b) a reliance on that representation by a third party; and (c) a change in position by the third party in reliance on the representation" (121). What decided it: logos, products, trademarks "throughout the premises" and routine support visits were no representation, and the contract called the dealer "an independent businessman" (120); Mobil's ownership was irrelevant because it had leased the premises to one "who possessed actual and superseding control" (121). Only the first element was decided. The opinion mixes pleading and summary-judgment language: the allegations are "legally insufficient to plead a case" and the complaint fails "Unless properly amended" (120–121), yet summary judgment is reinstated (121–122).
5. **May say (6): 5 LICENSED, 1 LICENSED-NARROWER.**
   - S1–S4, S6: LICENSED. On S1, quote the court's "does not necessarily indicate".
   - S5: LICENSED-NARROWER. The court gives this "for the instruction of the courts below", after saying "we need not determine what the court actually held" (121), in the paragraph the saved text garbles; it is dictum. Narrower: "The court noted, for the guidance of the lower courts, that apparent agency imputes the agent's acts, so that 'if the agent cannot be held liable, neither can the principal' (121)."
   - May not say (6): all sound.
6. **K claims.** Agree.
7. **Later history.** Not flagged; not checked.

## airbnb2019cjeu

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** Publications Office metadata: CELEX 62018CJ0390, ECLI:EU:C:2019:1112, document date 2019-12-19, Grand Chamber. The saved text gives the composition, Advocate General Szpunar, the Opinion "at the sitting on 30 April 2019", and a reference from the investigating judge of the tribunal de grande instance de Paris by decision of 7 June 2018. No mismatch.
2. **Read depth.** Paras 1–101 and the operative part. Honest.
3. **Quotations.** 40 instances, all MATCH, locators right. Not source quotations: "tests of 'decisive influence' for platforms" and "platform immunities" (CLAIMS_FIXED, K8). Three errors of statement:
   - The Summary calls AHTOP "A French association of hotels and professional tourism businesses". The judgment names it "Association pour un hébergement et un tourisme professionnels (Association for professional tourism and accommodation, AHTOP)" (para 22) and says nothing of its members. Hôtelière Turenne SAS and Valhotel appear only as interveners.
   - The critical note says the facts "came from the platform". Para 68 calls the facts of para 19 "The matters mentioned by the referring court"; only para 20, how the platform works in practice, is "apparent from the explanations provided by Airbnb Ireland".
   - "It says nothing about ... consumer law." The judgment quotes the derogation ground "the protection of consumers, including investors" (para 11) and applies the conditions of art. 3(4) (para 84). It decides nothing on consumer law; it is not silent on it.
4. **Holding; test; deciding facts.** Airbnb Ireland won: its service is an information society service (paras 57, 69), and France could not enforce the unnotified Hoguet Law against it (paras 99–100). The test: an intermediation service is distinct "in principle", but not if it "forms an integral part of an overall service whose main component is a service coming under another legal classification" (para 50). What decided it: the structured list as the platform's "essential feature" (paras 53–54); a service "in no way indispensable" (para 55); "it is not apparent ... that Airbnb Ireland sets or caps the amount of the rents" (para 56); ancillary services (paras 58–64); and no "decisive influence", "particularly since Airbnb Ireland does not determine, directly or indirectly, the rental price charged ... still less does it select the hosts or the accommodation put up for rent on its platform" (para 68).
5. **May say (6): 4 LICENSED, 2 LICENSED-NARROWER.**
   - S1, S3, S4, S5: LICENSED.
   - S2: LICENSED-NARROWER. Price and selection were two of four reasons, and price is framed as what "is not apparent ... from the order for reference or from the information in the file" (para 56). Narrower: "The Court reached that view because the list of offers was the platform's essential feature, the service was 'in no way indispensable' to accommodation, it was not apparent from the file that Airbnb set or capped the rents, which it left 'to the host alone', and Airbnb did not select the hosts or the accommodation (paras 53–56, 68)."
   - S6: LICENSED-NARROWER. Narrower: "The case arose from a complaint by AHTOP, an 'Association for professional tourism and accommodation', that Airbnb was mediating property transactions without the licence the Hoguet Law requires (paras 22–25)."
   - May not say (6): all sound.
6. **K claims.** K8: agree that it narrows; it is a classification for market access, not an immunity. K3: agree.
7. **Later history.** Not flagged; not checked.

## uber2017cjeu

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** Publications Office metadata: CELEX 62015CJ0434, ECLI:EU:C:2017:981, document date 2017-12-20, Grand Chamber. The saved text gives the referring court (Juzgado de lo Mercantil No 3 de Barcelona, decision of 16 July 2015), the caption "Asociación Profesional Élite Taxi v Uber Systems Spain SL", and the Opinion "at the sitting on 11 May 2017". No mismatch.
2. **Read depth.** Paras 1–50 and the operative part. Honest.
3. **Quotations.** 28 instances, all MATCH, locators right. Not a source quotation: "tests of 'decisive influence' for platforms" (CLAIMS_FIXED).
4. **Holding; test; deciding facts.** Elite Taxi's side prevailed on classification: Uber's service is "a service in the field of transport", so Member States may regulate it (paras 40, 47–48). The test starts from separateness "in principle" (para 34) and asks whether the service is "more than an intermediation service" (para 37), the provider "simultaneously" offering the transport and organising its "general operation" (para 38). The facts that decided it, introduced by "it follows from the information before the Court" and "it appears, inter alia" (para 39): selection of non-professional drivers; an application "without which (i) those drivers would not be led to provide transport services and (ii) persons who wish to make an urban journey would not use the services"; and "decisive influence over the conditions under which that service is provided", namely the maximum fare, receipt of the fare before paying the driver, and "a certain control over the quality of the vehicles, the drivers and their conduct, which can, in some circumstances, result in their exclusion".
5. **May say (5): 3 LICENSED, 2 LICENSED-NARROWER.**
   - S2, S4, S5: LICENSED.
   - S1: LICENSED-NARROWER. *Uber* says the "in principle" point of a service connecting non-professional drivers with passengers (para 34) and holds Uber's own service "an integral part of an overall service whose main component is a transport service" (para 40). The general rule in the card's form is *Airbnb Ireland*'s restatement (its para 50, citing para 40 of this judgment); cite it that way.
   - S3: LICENSED-NARROWER. Keep the Court's hedges: "it appeared, inter alia, from the information before the Court" (para 39).
   - May not say (6): all sound.
6. **K claims.** Agree.
7. **Later history.** Not flagged; not checked.

## eu2022dsa

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CELEX 32022R2065. Publications Office metadata (11 Nov 2026): in force (flag 1), end of validity 9999-12-31, document date 2022-10-19, no act linked as amending or repealing it. Eleven corrigenda exist (32022R2065R(01) to R(11), Dec 2022 to Oct 2026), none in English (German, French, Hungarian, Polish, Danish, Estonian, Slovenian, Italian, Finnish, Croatian, Lithuanian). The English words the card quotes therefore stand. Title and OJ reference as the card gives them.
2. **Read depth.** Partial, and declared provision by provision. Honest.
3. **Quotations.** 88 instances, all MATCH; every article and recital locator right. Not a source quotation: "duties on traders to be reachable" (CLAIMS_FIXED, K7). One paraphrase is too short: the art. 20(4) bullet's "Where the complaint shows the decision was unfounded" stands for "Where a complaint contains sufficient grounds for the provider of the online platform to consider that its decision not to act upon the notice is unfounded or that the information to which the complaint relates is not illegal and is not incompatible with its terms and conditions".
   - *The exact words* (saved OJ text; the card quotes each correctly):
     - Art. 6(1): "Where an information society service is provided that consists of the storage of information provided by a recipient of the service, the service provider shall not be liable for the information stored at the request of a recipient of the service, on condition that the provider: (a) does not have actual knowledge of illegal activity or illegal content and, as regards claims for damages, is not aware of facts or circumstances from which the illegal activity or illegal content is apparent; or (b) upon obtaining such knowledge or awareness, acts expeditiously to remove or to disable access to the illegal content."
     - Art. 6(3): "Paragraph 1 shall not apply with respect to the liability under consumer protection law of online platforms that allow consumers to conclude distance contracts with traders, where such an online platform presents the specific item of information or otherwise enables the specific transaction at issue in a way that would lead an average consumer to believe that the information, or the product or service that is the object of the transaction, is provided either by the online platform itself or by a recipient of the service who is acting under its authority or control."
     - Art. 12(1): "Providers of intermediary services shall designate a single point of contact to enable recipients of the service to communicate directly and rapidly with them, by electronic means and in a user-friendly manner, including by allowing recipients of the service to choose the means of communication, which shall not solely rely on automated tools." Art. 12(2) as the card gives it.
     - Art. 20(4): "Providers of online platforms shall handle complaints submitted through their internal complaint-handling system in a timely, non-discriminatory, diligent and non-arbitrary manner. Where a complaint contains sufficient grounds for the provider of the online platform to consider that its decision not to act upon the notice is unfounded or that the information to which the complaint relates is not illegal and is not incompatible with its terms and conditions, or contains information indicating that the complainant's conduct does not warrant the measure taken, it shall reverse its decision referred to in paragraph 1 without undue delay."
     - Art. 20(5): "Providers of online platforms shall inform complainants without undue delay of their reasoned decision in respect of the information to which the complaint relates and of the possibility of out-of-court dispute settlement provided for in Article 21 and other available possibilities for redress."
     - Art. 20(6): "Providers of online platforms shall ensure that the decisions, referred to in paragraph 5, are taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means."
     - Art. 21: (1) recipients "addressed by the decisions referred to in Article 20(1) shall be entitled to select any out-of-court dispute settlement body that has been certified in accordance with paragraph 3 of this Article in order to resolve disputes relating to those decisions, including complaints that have not been resolved by means of the internal complaint-handling system referred to in that Article", "without prejudice to the right of the recipient of the service concerned to initiate, at any stage, proceedings to contest those decisions by the providers of online platforms before a court in accordance with the applicable law"; (2) "Both parties shall engage, in good faith, with the selected certified out-of-court dispute settlement body with a view to resolving the dispute." and "The certified out-of-court dispute settlement body shall not have the power to impose a binding settlement of the dispute on the parties."; (4), third subparagraph, decisions "within a reasonable period of time and no later than 90 calendar days after the receipt of the complaint", extendable to "a maximum total duration of 180 days"; (5) fees borne by the platform if the recipient wins, and "free of charge or at a nominal fee" for recipients. Paras (3) and (6)–(9) concern certification, reporting, revocation and Directive 2013/11/EU; the card does not quote them.
4. Not a judgment.
5. **May say (10): 7 LICENSED, 3 LICENSED-NARROWER.**
   - S2–S7, S9: LICENSED. On S6, the card's reading that the chosen means must not rely solely on automated tools matches recital 43.
   - S1: LICENSED-NARROWER. Art. 6(1)(a) also removes the exemption, for damages claims, where the provider "is aware of facts or circumstances from which the illegal activity or illegal content is apparent". Narrower: "... is not liable for information stored at a user's request unless it knows of illegal content or, for claims for damages, is aware of facts or circumstances from which it is apparent, and fails to act expeditiously (art. 6(1))."
   - S8: LICENSED-NARROWER. Art. 20(1) covers decisions on a notice, or taken "on the grounds that the information provided by the recipients constitutes illegal content or is incompatible with its terms and conditions": removal or restricted visibility, suspension or termination of the service or of the account, and restriction of monetisation. The six months run from the day the recipient "is informed about the decision" (art. 20(2)). The small-enterprise exclusion does not cover very large online platforms (art. 19(2)).
   - S10: LICENSED-NARROWER. Art. 93(2), second subparagraph, applies listed provisions from 16 November 2022, and art. 92 applies the Regulation earlier to designated very large platforms. For arts 6, 12, 20 and 21 and an ordinary platform, 17 February 2024 is right; say "the provisions cited apply from 17 February 2024".
   - May not say (10): all sound.
6. **K claims.** K8, K3: agree. K7: partly disagree. The card calls arts 12, 20 and 21 "the 'duties on traders to be reachable' that K7 lists as confirming". These articles bind "providers of intermediary services" and "providers of online platforms"; the Regulation's 'trader' (art. 3(f)) is the hotel or host. They are duties on intermediaries about the intermediary's own service (art. 2(2); recital 6). They confirm K7 by analogy for the platform, not for the holder K7 names.
7. **Status.** In force, with no amending act and no English corrigendum, per the metadata above. The art. 91 evaluations were not traced.

## eu2019p2b

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** CELEX 32019R1150, OJ L 186, 11.7.2019, p. 57. No mismatch. Two corrigenda exist (Estonian, 2020; Danish, 2022); none in English.
2. **Read depth.** Whole. Honest. I confirmed the card's word counts: "hotel" 0, "accommodation" 0, "human" 0, "automat" 2 (recital 19; art. 3(2)).
3. **Quotations.** 60 instances, all MATCH; every article and recital locator right. Not a source quotation: the K7 sentence from CLAIMS_FIXED.
4. Not a judgment.
5. **May say (6): 4 LICENSED, 2 LICENSED-NARROWER.**
   - S2, S4, S5, S6: LICENSED.
   - S1: LICENSED-NARROWER. Add "other than small enterprises (art. 11(5))", and date the statement of status (head 7).
   - S3: LICENSED-NARROWER. Art. 4(1) covers restriction or suspension "in relation to individual goods or services offered by that business user"; the thirty days of art. 4(2) yield to the exceptions in art. 4(4); and art. 4(5), second subparagraph, excuses the statement of reasons in some cases. Narrower: "A platform that restricts or suspends its service to a business user for particular goods or services must give reasons before or when the measure takes effect, and, save in the cases of art. 4(4), thirty days before terminating the whole service (art. 4(1), (2), (4))."
   - May not say (7): all sound; the last can now be answered on a dated record (head 7), to be re-checked at submission.
6. **K claims.** Agree.
7. **Status: in force on the Publications Office record of 11 Nov 2026.** SPARQL on CELEX 32019R1150: `resource_legal_in-force` 1; `date_end-of-validity` 9999-12-31; entry-into-force dates 2019-07-31 and 2020-07-12; no adopted act linked as repealing or amending it. The Digital Omnibus proposal, 52025PC0837 (dated 2025-11-19), is linked only by `proposes_to_amend`. Metadata can lag adoption; check EUR-Lex before submission. I did not consult EUR-Lex pages directly.

---

## Table: every FAIL, every quotation not MATCH, every 'may say' sentence not LICENSED

| Card | Item | Mark | Correction or note |
|---|---|---|---|
| — | FAILs | none | — |
| hoyt2013gutterz | "an altercation might occur" (773) | OCR-DOUBT | Saved text prints "ah altercation"; repair disclosed; check the printed reporter. |
| groh2015westin | Holding, ¶¶ 4, 51 | OCR-DOUBT | "eviets", "cireumstances" repaired in brackets; check official 2015 CO 25. |
| groh2015westin | § 314A as quoted, ¶ 29 | OCR-DOUBT | "cam" repaired as "[can]"; "§ 814A" for § 314A. |
| groh2015westin | ¶ 40 | OCR-DOUBT | "seope" repaired as "[scope]". |
| rasnick2011krishna | May say S2 | LICENSED-NARROWER | Add "to determine whether he was in medical need, for a condition unrelated to his stay" (568, 570). |
| rasnick2011krishna | May say S6 | LICENSED-NARROWER | Present as the wife's testimony as the court recounts it (n. 1; 572), not as found facts. |
| hoyt2013gutterz | May say S3 | LICENSED-NARROWER | Voluntariness qualifies the first reason ("especially when"); add the benefit reason (777). |
| groh2015westin | May say S5 | LICENSED-NARROWER | "said it was not holding that hotels must provide safe transportation" (¶ 38), not "refused to require". |
| thomas1955pick | May say S2 | LICENSED-NARROWER | Keep "usually treated" (665). |
| thomas1955pick | May say S3 | LICENSED-NARROWER | Facts are pleaded; common-law and statutory claims time-barred; contract claim well pleaded (665–666). |
| digest4_9 | May say S1 | LICENSED-NARROWER | Edict covers what was received "cuiusque", in the course of business (4.9.1 pr.; 4.9.3.1–2). |
| digest4_9 | May say S3 | LICENSED-NARROWER | 4.9.6 pr. concerns the in factum actions for loss wrongfully suffered, not the action on the receipt. |
| digest4_9 | May say S4 | LICENSED-NARROWER | 4.9.2 holds for the action on the receipt; 4.9.6.3 excludes a transient guest such as a traveller under the action for double. |
| bgb701 | May say S1 | LICENSED-NARROWER | Add § 701(3)–(4) exclusions. |
| bgb701 | May say S3 | LICENSED-NARROWER | Add § 702(3) exception (excessive value or bulk, dangerous). |
| bgb701 | May say S4 | LICENSED-NARROWER | Add § 703, second sentence (safekeeping; fault). |
| coe1962hotelkeepers | May say S2 | LICENSED-NARROWER | Subject to the state option in Convention art. 2(d). |
| coe1962hotelkeepers | May say S3 | LICENSED-NARROWER | Add the refusal grounds in Annex art. 2(2). |
| coe1962hotelkeepers | May say S4 | LICENSED-NARROWER | Add "Except in any case to which Article 4 ... applies". |
| hayman1987ramada | May say S1 | LICENSED-NARROWER | Nine months, not a year (7 July 1987; 7 April 1988). |
| mobil1995bransford | May say S5 | LICENSED-NARROWER | Dictum, "for the instruction of the courts below", in a garbled paragraph (121). |
| airbnb2019cjeu | May say S2 | LICENSED-NARROWER | Four reasons (paras 53–56, 68); price framed as "not apparent" from the file. |
| airbnb2019cjeu | May say S6 | LICENSED-NARROWER | AHTOP is an "Association for professional tourism and accommodation" (para 22), not an association of hotels. |
| uber2017cjeu | May say S1 | LICENSED-NARROWER | General rule in this form is *Airbnb Ireland* para 50's restatement of *Uber* para 40. |
| uber2017cjeu | May say S3 | LICENSED-NARROWER | Keep "it appears, inter alia" and "the information before the Court" (para 39). |
| eu2022dsa | May say S1 | LICENSED-NARROWER | Add the constructive-awareness limb for damages claims (art. 6(1)(a)). |
| eu2022dsa | May say S8 | LICENSED-NARROWER | Decisions covered are those listed in art. 20(1)(a)–(d) on the stated grounds; six months from being informed; VLOPs not excluded. |
| eu2022dsa | May say S10 | LICENSED-NARROWER | Arts 92 and 93(2) second subparagraph give other dates for some provisions and platforms. |
| eu2019p2b | May say S1 | LICENSED-NARROWER | Small enterprises exempt (art. 11(5)); date the status. |
| eu2019p2b | May say S3 | LICENSED-NARROWER | Art. 4(1) is per goods or services; art. 4(4) exceptions; art. 4(5) second subparagraph. |

**Errors of statement outside quotations and 'may say' (for the lead):** *hayman1987ramada* hold_rationale on *Crinkley* fn 3 (the footnote gives both grounds) and the claim that "required" does not occur; *blackstone1768commentaries* "two routes, not reconciled" and "does not cross-refer" (p. 167 cross-refers to vol. III p. 216 and states a general rule; the traveller's action is in assumpsit); *digest4_9* gloss of 4.9.7.6 and the unreconciled 4.9.6.3; *bgb701* "official English translation"; *airbnb2019cjeu* description of AHTOP, "came from the platform", "nothing about ... consumer law"; *eu2022dsa* K7 equation of intermediaries with "traders"; *rasnick2011krishna* K7 headline and "unable to call for help". **Status now established:** ETS No. 41 in force since 15 Feb 1967, with 17 ratifications or accessions as of 19 Mar 2014; Regulation 2019/1150 in force on the Publications Office record of 11 Nov 2026; *Hayman*'s history is "disc. rev. on additional issues denied, 320 N.C. 631" as the Court of Appeals itself cites it in 1988.

Verification written by a Claude (Opus 5.5) subagent, card verifier CV-B, from the saved source texts and the official or archive records named above, on 11 Nov 2026; run rr-2026-11-k.

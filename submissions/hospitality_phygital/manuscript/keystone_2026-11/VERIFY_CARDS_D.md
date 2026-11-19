<!-- Independent verification of cards, batch CV-D, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-D (run rr-2026-11-k)

I checked sixteen cards: seven new cards and one upgraded card from reader R6b (law), and eight cards from reader R3 (philosophy of rights). I did not write any of them, and I edited none.

**Result.** No card fails. Five pass clean (`schufa2023cjeu`, `eu2024platformwork`, `wenar2025rights`, `herstein2023legal`, `duff2009legal`); eleven pass with notes. Every one of the 596 double-quoted strings on the sixteen cards is what the card says it is: 589 quotations match their source at the stated locator, and 7 are search strings whose reported presence or absence the AI Act card states correctly. No string is LOCATOR-WRONG, NOT-FOUND or PARAPHRASED-AS-QUOTE. The problems sit in paraphrase and in reach. The Gardner card makes Gardner exclude explanation "expressly", and he does not. The AI Act card and R6b's report miss art. 27(1)(f), which asks certain deployers to set out complaint mechanisms. Of the nine central conclusions, four are confirmed, four hold only narrowed, and one, (e), is refuted as the brief words it.

## How I checked

- **Records.** On 11 Nov 2026 I re-fetched Crossref for the five articles (Fox, Duff, Gardner 2011, de Kenessey, Gardner 2019), the three Stanford Encyclopedia entries live and in the archive editions the cards name, their citation pages, the NDPR review, the BOE PDF and consolidated page, the Publications Office copies of the SCHUFA judgment, the platform work directive, the AI Act and Regulation (EU) 2026/1744, the Caselaw Access Project page and record for *Mathews*, the Governor's notice for AB 1609, the Gardner eprint, and the Internet Archive capture indexes for AB 1609, UK s. 80 and BAILII. leginfo.legislature.ca.gov (HTTP 403), legislation.gov.uk (HTTP 202, empty body) and BAILII (bot challenge) refused, as the readers reported. I did not bypass them.
- **Quotations.** A script I wrote (scratchpad, run with `python3 -I`) pulled every string in straight or curly double quotation marks, and every single-quoted string, from each card body. It searched for each one in the saved source after only these normalisations: whitespace collapsed, typographic quotation marks and apostrophes mapped to plain, ligatures and soft hyphens removed, line-end hyphens joined. An ellipsis matched any intervening text, and a bracketed insertion matched either itself or up to 60 characters. For locators I cut each source into its own units and recorded which unit held the match: Stanford Encyclopedia sections and paragraphs (counted as the cards count them), PDF pages from my own `pdftotext` extraction, CJEU paragraph numbers, recitals and article paragraphs, inserted UK articles, sections of the California bill, *Mathews* star pages, the *Cyanamid* transcript page heads, and BOE pages and articles from a `-layout` extraction. I read by eye every string that did not match inside a single unit.
- **Paraphrase and licence.** I read Gardner's typescript pp. 12–14, 26 and 33–60 in full against the card, and searched the whole eprint for its other topics. I read the Spanish of every passage the Spain card renders. For every 'may say' and 'may not say' sentence, and for each reader inference, I read the passage cited.

---

## R6b cards (law)

### es2025clientela

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** The BOE PDF I fetched from boe.es is byte-identical to the saved file (sha256 `0331830d0bef…`). The PDF prints 'Ley 10/2025, de 26 de diciembre, por la que se regulan los servicios de atención a la clientela', BOE núm. 312, Sec. I, pp. 176170–176205 (36 pages). The consolidated page gives 'Entrada en vigor: 28/12/2025' and a single version, 'Texto inicial publicado el 27/12/2025'. No mismatch.
2. **Read depth.** The saved file is the official text as published. It contains the preamble, arts 1–23, the additional, transitional and repealing provisions and final provisions 1–8, as the card says.
3. **Quotations.** 63 strings. 61 quote the BOE and all MATCH at the stated article and BOE page; art. 7(1) runs across pp. 176182–176183, as the card says. The other 2 quote `CLAIMS_FIXED.md` exactly. The whole-text negatives hold: 'hotel', 'alojamiento', 'hosteler' and 'turis' do not occur; 'indemniz' occurs once (art. 4(5)) and 'daños' never; 'autoridad' is used only of public authorities; 'facultad'/'facultado' only of regulatory powers and of traders answering reviews. **The English paraphrases are faithful**, with three omissions worth knowing. Art. 3(1) also says 'independientemente de su carácter oneroso o gratuito y de que hagan uso efectivo del servicio', and its next sentence deems three further groups to be clientele (people signed up without consent, people billed after cancelling or for services not contracted, buyers under guarantee). Art. 8(2), first sentence, places the main menu 'del canal telefónico'. Art. 2(1) ends by allowing 'aplicación flexibilizada' for cooperatives and non-profits with fewer than 250 workers, so 'whatever their size' (Summary) holds only with that qualification. The rendering of art. 2(2) is accurate: the three size tests are alternatives (preamble III: 'no considerándolos de forma cumulativa'), counted 'de forma individual o en el seno del grupo', and 'balance de negocios' as balance sheet is reasonable. Art. 4(4) and the 'leve' reading are accurate: final provision 3, point Cuatro makes infringements under the new art. 47(1)(q) 'leves, salvo que tengan la consideración de graves'.
4. **Stated versus reported.** Not applicable (statute).
5. **May say.** (1) art. 8(1): LICENSED. (2) art. 8(2): LICENSED. (3) LICENSED-NARROWER. Art. 8(3) offers 'una persona física supervisora o … un departamento específico de calidad', and lets the firm call back the same working day when transfer within three minutes is impossible. Narrower: *a dissatisfied customer may ask to be transferred to a supervisor who is a natural person, or to a quality department, within the same communication, or failing that be called back the same working day.* (4) LICENSED-NARROWER: the size tests bind firms selling goods or services other than the listed basic services 'destinados principalmente a personas consumidoras' in Spain; add that condition. (5) LICENSED. (6) LICENSED-NARROWER: add the exceptions in art. 4(4) itself, 'salvo que el mantenimiento del servicio pudiera afectar a la seguridad de las personas o de las cosas' and contrary sector rules. (7) LICENSED. (8) LICENSED. **May not say:** all eight are correct.
6. **Central conclusions.** Bears on (e); see below.
7. **Reader's own inferences.** That a large hotel group falls within art. 2(2) is supported by the words, provided it sells mainly to consumers. That breach is minor by default is supported by final provision 3, points Tres and Cuatro.

### ca2026ab1609

**Verdict: PASS-WITH-NOTES** (the chaptered text and operative date remain unverified, as the card says).

1. **Identity.** The saved capture is byte-identical to its stated hash (`3990f645e47a…`). It prints 'Enrolled September 04, 2026', 'Passed IN Senate August 30, 2026', 'Passed IN Assembly August 31, 2026', introduced 'January 20, 2026', and the act adding Chapter 22.6.1 (from s. 22625). The archive index confirms that no capture of the bill-text page exists after 27 Sep 2026 02:06 UTC and that the latest status capture is 28 Sep 2026 09:57 UTC. The live gov.ca.gov notice of 28 Sep 2026 (HTTP 200) lists 'AB 1609 by Assemblymember Rick Chavez Zbur (D-Hollywood) — Customer service chatbots.' leginfo still returned 403. The chapter number and the operative date remain unverified.
2. **Read depth.** The enrolled bill, with the digest and ss. 22625–22629. The card is honest that this is not the chaptered statute.
3. **Quotations.** 46 strings: 45 MATCH at the stated subdivision (the status-page 'Non-Urgency' among them), and 1 quotes `CLAIMS_FIXED.md` exactly. The negatives hold: in the bill text 'hotel', 'lodging', 'authority', 'resolve', 'operative' and 'effective' do not occur, and '2027' occurs twice, both as 'January 1, 2027'.
4. **Stated versus reported.** Not applicable.
5. **May say.** All four LICENSED. **May not say:** all six correct.
6. **Central conclusions.** Bears on (e).
7. **Reader's own inferences.** The reading that the duty runs to California residents by account address, not to guests in California, follows from s. 22625(b)(2): SUPPORTED.

### schufa2023cjeu

**Verdict: PASS.**

1. **Identity.** The Publications Office XHTML I fetched (CELEX 62021CJ0634, English) is byte-identical to the saved file (`0fbf6c7975cf…`). The saved notice carries ECLI:EU:C:2023:957, 2023-12-07 and C-634/21. The header gives the First Chamber, the five judges and A. Kumin as rapporteur, Advocate General Pikamäe, and 'made by decision of 1 October 2021'. No mismatch.
2. **Read depth.** The judgment's paras 1–75 and the operative part, in English. Full text, as stated.
3. **Quotations.** 40 strings, all MATCH at the stated paragraph. Para. 47 does record as 'common ground' that the 'based solely on automated processing' condition was met. 'hotel', 'accommodation' and 'guest' do not occur.
4. **Stated versus reported.** Not applicable. The card attributes the referring court's findings (para. 48) and SCHUFA's position (para. 16) correctly.
5. **May say.** All five LICENSED. **May not say:** all six correct.
6. **Central conclusions.** Bears on (e).
7. **Reader's own inferences.** The analogy to the divided host is flagged as R6b's. The text supports it as analogy only: the Court bound the vendor (paras 61–63, 73).

### eu2024platformwork

**Verdict: PASS.**

1. **Identity.** The Publications Office XHTML (CELEX 32024L2831) I fetched is byte-identical (`5f8f31b0bb1a…`): Directive (EU) 2024/2831 of 23 October 2024, OJ L 11.11.2024.
2. **Read depth.** The text as published, recitals 1–73 and arts 1–32. Full text, as stated.
3. **Quotations.** 68 strings: 67 MATCH at the stated recital or article paragraph, and 1 quotes `CLAIMS_FIXED.md` exactly. The word 'human' appears in the articles only at arts 1(1), 10 (title), 10(2) ('human resources'), 10(5) and 11 (title). The card is right that art. 11(2) does not use it.
4. **Stated versus reported.** Not applicable.
5. **May say.** All seven LICENSED. **May not say:** all seven correct.
6. **Central conclusions.** Bears on (e) and (f).
7. **Reader's own inferences.** The ambiguity of 'within two weeks of the adoption of the decision' (art. 11(3)) is real, and the card rightly leaves it unresolved.

### uk2025datause

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** legislation.gov.uk returned HTTP 202 with no body. The archive index lists the 27 Oct 2026 capture the card names, and the saved file matches its stated hash (`bb9238bdb50c…`). The page is 'Latest available (Revised)', lists versions of 19/06/2025 and 05/02/2026, and says 'There are currently no known outstanding effects'. The saved regs 2 and 5 are from 'The Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026', uksi/2026/82, (C. 10), as made. No mismatch.
2. **Read depth.** Section 80(1)–(6) with its commencement annotations, and regs 2 and 5. As stated. The former UK Article 22 was not read, and the card says so.
3. **Quotations.** 47 strings: 46 MATCH at the stated inserted article or regulation, and 1 quotes `CLAIMS_FIXED.md` exactly. The s. 96(4) wording sits in s. 80(4), as stated.
4. **Stated versus reported.** Not applicable.
5. **May say.** (1) LICENSED; add the saving in reg. 5 if the date is printed. (2) LICENSED. (3) LICENSED-NARROWER. Art. 22C(1) covers every solely automated significant decision based entirely or partly on personal data, including the special-category decisions that art. 22B permits, not only 'other' ones. Narrower: *for any solely automated significant decision based on personal data, the controller must have safeguards that …*. (4) LICENSED. (5) LICENSED. **May not say:** all six correct.
6. **Central conclusions.** Bears on (g).
7. **Reader's own inferences.** The reading that, outside art. 22B, nothing forbids a solely automated significant decision follows from the structure of arts 22B–22C: SUPPORTED. The comparison with 'what went before' rests on the EU text and *SCHUFA*, not on the former UK text, as the card says.

### mathews1976eldridge

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** The Caselaw Access Project page is byte-identical (`b91a5ac4ac06…`). Its record gives 'Mathews v. Eldridge', 1976-02-24, 'No. 74-204', pp. 319–350, and cites 424 U.S. 319, 47 L. Ed. 2d 18 and 96 S. Ct. 893. The bench, 'Argued October 6, 1975' and Stevens J's non-participation are in the text. No mismatch.
2. **Read depth.** The opinion, footnotes and dissent in a scanned copy without the syllabus. As stated.
3. **Quotations.** 53 strings: 51 MATCH at the stated star page, and 2 quote `CLAIMS_FIXED.md` exactly. The footnote markers confirm 'at 325 n. 4' and 'at 331 n. 11'. The three-factor sentence begins on 334 ('our prior de-*335cisions'), as the card says.
4. **Stated versus reported.** Not applicable. *Goldberg* is attributed only through *Mathews*, and the inner quotation at 333 is attributed to *Armstrong v. Manzo*.
5. **May say.** (1) LICENSED; the card itself notes that the sentence sits in the jurisdictional Part II. (2) LICENSED. (3) LICENSED; keep the attribution to *Armstrong v. Manzo*. (4) LICENSED-NARROWER. The Court rested on all three factors, so the reasons named are not the whole ground. Narrower: *weighing the three factors (the interim nature of the loss given full retroactive relief, the reliability of the medical evidence and the recipient's prior written response, and the administrative cost), the Court held that an evidentiary hearing was not required before termination (at 340–349).* (5) LICENSED. (6) LICENSED. **May not say:** all six correct. (1) is exactly right: the holding is against a prior *evidentiary* hearing.
6. **Central conclusions.** Bears on (h).
7. **Reader's own inferences.** The carry-over 'as reasoning, not law' is flagged as R6b's own, and the opinion supports the limit: due process 'imposes constraints on governmental decisions' (at 332).

### americancyanamid1975ethicon

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** BAILII serves a bot challenge, so I could not reach the official site. The archive index lists the capture, and the saved file matches its stated hash (`2519e31e54e0…`). The header gives 'American Cyanamid Co (No 1) v Ethicon Ltd [1975] UKHL 1 (05 February 1975)' with [1975] AC 396, [1975] 2 WLR 316, [1975] 1 All ER 504 and [1977] FSR 593. The AC page range remains unchecked against the law report, as the card says.
2. **Read depth.** The House of Lords transcript, pp. 1–7, with all five speeches. Lord Diplock gives the reasoned speech, and Viscount Dilhorne (p. 6) and Lords Cross, Salmon and Edmund-Davies (p. 7) agree. As stated.
3. **Quotations.** 29 strings: 28 MATCH on the stated transcript page, and 1 quotes `CLAIMS_FIXED.md` exactly. One attribution is loose. 'satisfied by damages afterwards' comes from K7's 'Refutes or narrows' list, not from the stage-0 tort lawyer's row, which reads 'Tort gives damages, never a hearing' and 'The law supplies liability afterwards'.
4. **Stated versus reported.** Not applicable.
5. **May say.** All four LICENSED. **May not say:** all five correct.
6. **Central conclusions.** Bears on K7's timing line; no lettered conclusion.
7. **Reader's own inferences.** That the bare numerals '2'–'7' head new transcript pages is plausible: they stand alone and run in order. I could not check it against the original print.

### eu2024aiact (upgraded parts: arts 14, 26, 85, 86, 99)

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** The AI Act XHTML I fetched from the Publications Office (CELEX 32024R1689) is byte-identical to the saved file (`8f0b656302f9…`). Regulation (EU) 2026/1744 of 8 July 2026 (CELEX 32026R1744) exists at the Publications Office. Its point (40)(b) reads '2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III', and it enters into force 'on the third day following that of its publication'. Section 2 of Chapter III ('Requirements for high-risk AI systems') runs from art. 8 to art. 15, and Section 3 from art. 16 to art. 27. So arts 14 and 26 sit where the card says.
2. **Read depth.** The articles and recitals listed, in the OJ text, plus Omnibus points (5), (38) and (40) and the recital on art. 113. The card states the limits honestly. The upgrade kept every earlier line: a git diff against the pre-upgrade commit shows only five frontmatter lines changed, and the old `source_basis` and `hold_rationale` are prefixes of the new.
3. **Quotations.** 88 strings. 81 quotations MATCH: 71 in the AI Act at the stated article, paragraph or recital, 8 in the Omnibus (recital 40 and points (5), (32), (38), (40)), and 2 in `DRAFT_v6.md` line 149. 7 are search strings, and the card reports each correctly. 'Article 26', 'Article 86', 'Chapter IX' and 'human oversight' are absent from the Omnibus. 'Article 85' occurs once there, in point (32). 'Article 14' occurs there only for Regulation (EU) 2019/1020. In the enacting terms, 'affected person(s)' occurs only in arts 2(1)(g), 3(56), 56(4), 86(1), 99(7) and 100(1), as stated.
4. **Stated versus reported.** Not applicable.
5. **May say.** (1) LICENSED-NARROWER. Art. 14(4) qualifies the capacities 'as appropriate and proportionate' and lays the duty on the system as supplied. Narrower: *requires that high-risk systems be provided so that the persons assigned to oversee them are enabled, as appropriate and proportionate, to decide…*. (2) LICENSED. (3) LICENSED-NARROWER: art. 26(5) applies where use 'may result in' a risk, and requires the deployer to inform 'the provider or distributor'. (4) LICENSED-NARROWER: art. 86(1) is limited to Annex III systems other than point 2 and to decisions with legal or similarly significant adverse effect, and art. 86(3) makes it subsidiary to other Union law. (5) LICENSED. (6) LICENSED-NARROWER: write 'the duties in arts 14 and 26', because arts 85–86 sit in Chapter IX, which applies from 2 August 2026. **May not say:** five of six are correct. The second ('No article does' give the affected person a way to reach the overseer) holds as worded, but the support needs a caveat. Art. 27(1)(f), which R6b did not read, requires deployers that are public bodies or private providers of public services, and deployers of Annex III points 5(b)–(c), to set out in their fundamental rights impact assessment 'the arrangements for internal governance and complaint mechanisms'. Recital 96 adds 'complaint handling and redress procedures'. Neither gives the affected person a right of access to the overseer.
6. **Central conclusions.** Bears on (e) and (i).
7. **Reader's own inferences.** (i) The application date read from point (40)(b) against the chapter headings is SUPPORTED, and it is a direct reading rather than an inference. (ii) That art. 26(2)'s 'authority' includes at least the powers of art. 14(4)(d)–(e) is SUPPORTED as inference: art. 26(3) speaks of 'the human oversight measures indicated by the provider'. (iii) 'No route from the affected person' needs the art. 27(1)(f) caveat.

---

## R3 cards (philosophy of rights)

### wenar2025rights

**Verdict: PASS.**

1. **Identity.** The live entry (HTTP 200) is byte-identical to the saved file. It prints 'First published Mon Dec 19, 2005; substantive revision Sat Jun 7, 2025', with authors Wenar, Leif and Cruft, Rowan. The citation page gives the Summer 2025 Edition (Zalta and Nodelman, eds), noted as a 'substantive content change', and that archive's main text is identical to the live text.
2. **Read depth.** §§1–2 of the live page, which is the Summer 2025 text. As stated.
3. **Quotations.** 26 strings, all MATCH at the stated section and paragraph (the 'Why' list item, the displayed definitions and the block quotations included). The single-quoted 'in section 3' (§2, para. 2) and 'demanded or insisted upon without embarrassment or shame' (§2.2.2) also MATCH. The slip the card notes is real: §2, para. 2 says 'we turn to that debate in section 3', and the debate is in §2.2.
4. **Stated versus reported.** The card separates the two throughout. Feinberg (§2.2.2, block quotation after para. 15) and Darwall (after para. 16) are 'quoted in the entry'. Gilbert (para. 18) and Sreenivasan (para. 19) are 'as reported'. Cornell and Martin are 'recorded' at §2.2.3, para. 4, and Thompson stays inside the entry's sentence. The card's own inferences (Critical notes 3 and 4) are labelled.
5. **May (Where it bears).** The K5 legal-limb and customary-limb statements and the K6 'contested' statement: LICENSED. The three-registers citation of §1: LICENSED.
6. **Central conclusions.** Bears on (a) and (b).
7. **Reader's own inferences.** That a claim held without a liberty to demand follows only by inference: SUPPORTED, since §§2.1.1–2.1.3 and 2.1.6 define incidents only. The Feinberg comparison: SUPPORTED by the block quotation and by Pitt-Rivers p. 515, where the saved scan reads 'makes c1aims or demands', an OCR slip.

### herstein2023legal

**Verdict: PASS.**

1. **Identity.** The live entry is byte-identical to the saved file. It prints 'First published Fri Jan 27, 2023', with author Herstein, Ori. The citation page gives the Winter 2023 Edition ('minor correction'), whose main text is identical to the live text.
2. **Read depth.** §§3, 4, 8.6 and 10. As stated.
3. **Quotations.** 26 strings, all MATCH at the stated section and paragraph. The entry's own slips ('unheard off', 'emphasis', 'non held', and the ungrammatical sentence in §10.4, para. 2) are reproduced and flagged.
4. **Stated versus reported.** Hart (§4.1), the interest theory (§4.2), the demand theory (§4.3) and Feinberg's thought experiment (§4.3, para. 1) are all marked as reported. The 'MacCormick estate example' in Critical note 3 is in §3.3, para. 2, as stated.
5. **May (Where it bears).** K5, K6 and K7: LICENSED. The K5 test (argue from the guest's action, not from its absence) is exactly what §10.3 supports.
6. **Central conclusions.** Bears on (a) and (b).
7. **Reader's own inferences.** The mapping of Herstein's 'Gardner 2011: 28–37, 45–46' to typescript pp. 33–45 and 54–55 is plausible: section 5 runs ts pp. 33–45 and the sixth doubt ts pp. 54–55. It remains unverified against the journal, as the card says.

### sreenivasan2019rights

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** The live NDPR page (HTTP 200) is byte-identical to the saved file. It names the reviewer as 'Gopal Sreenivasan, Duke University' and dates the review 2019.06.01.
2. **Read depth.** The whole review: 39 paragraph units (the three displayed equivalences among them) and two notes, 3,946 words with the notes, as the card counts.
3. **Quotations.** 25 strings, all MATCH in the paragraph named by its opening words. The equivalences are numbered (1)–(3) in the reviewer's own text ('her equivalences (1) and (2) together entail a third'), and 'as Gilbert herself accepts (71)' supports the card's p. 71.
4. **Stated versus reported.** The card splits 'Reported of Gilbert' from 'The reviewer's own position' and keeps the bracketed page numbers as the reviewer's. Hart's measures of control appear in the reviewer's own argument. Skorupski appears only inside a sentence reported of Gilbert. Correct.
5. **May (Where it bears).** The K6 'contested' statement: LICENSED. 'The critic of the demand analysis himself affirms the right-holder's standing' is LICENSED-NARROWER: he affirms it of 'a property owner' ('I see no reason to deny …'), in an objection about grounds. The K7 statement that a demand creates no right: LICENSED as reported of Gilbert; the step 'so a channel … serves the exercise' is the card's own.
6. **Central conclusions.** Bears on (a) and (b).
7. **Reader's own inferences.** That the review leaves the ordinary case untouched: SUPPORTED by the 'My first objection, then' paragraph.

### gardner2011what

**Verdict: PASS-WITH-NOTES** (one paraphrase overstates the text; the card must be corrected before R3 statement 47 is relied on).

1. **Identity.** Crossref 10.1007/s10982-010-9086-6 gives Gardner, John, 'What is Tort Law For? Part 1. The Place of Corrective Justice', *Law and Philosophy* 30(1), 1–50, online 22 Sep 2010, print Jan 2011. That matches the card. The eprint URL still serves a byte-identical file (387,548 bytes, sha256 `eea3b5f87186…`).
2. **Read depth.** The author's eprint, with a cover page and typescript pp. 1–60 (typescript page = PDF page − 1, confirmed from the printed folios). The cover says: 'This is an author eprint, which may not incorporate final edits … Please do not quote from or cite to this eprint.'
3. **Quotations.** The card contains **no quotation from the eprint**. Its four double-quoted strings are: Ripstein's quotation of the version of record (§4.3, para. 3), which MATCHES in Ripstein and, as the card says, also stands at ts p. 26; Herstein's citation string (§8.6, para. 2), MATCH; and two sentences from 'Damages without duty', which MATCH at eprint p. 12 and n. 31. That eprint carries no request against quotation; I searched it for one. **Paraphrases checked against the typescript:** pp. 34, 34–35, 35–36, 37, 37–38, 38–39, 39–40, 40, 40–41, 42 with n. 56, 45, 46–47, 50–53, 53, 54–55, 56, 58–59, 60, 14 and 12–13 with n. 25 are all faithful. Four need correcting:
   - **p. 43, n. 57.** The note says that expressing emotions, 'e.g. by confessing or apologizing', 'should not be mistaken for further correction according to the continuity thesis'. It does not mention explaining or giving an account of oneself. The Key fact is accurate. The Critical note's 'Giving an account of oneself, or apologising, is expressly not correction' is not: for explanation the thesis is silent, not expressly exclusive.
   - **p. 38, n. 53.** The footnote concerns acts 'both necessary and sufficient' for doing what one is obliged to do. The Key fact is accurate. The Critical note and 'Where it bears' shorten this to acts 'necessary for performance', and 'only if the channel is necessary' should read 'only if the channel were both necessary and sufficient, a derivation Gardner raises and sets aside'.
   - **p. 35.** 'the nearer … the better' is hedged in the text: 'the closer to perfect performance of my promise, you might think, the better'.
   - **p. 56.** 'For the most part, the continuity thesis does not explain general damages'; the card drops 'for the most part'.

   The lunch-at-noon example is absent from the 2011 eprint and appears in the 2019 one, as the card says.
4. **Stated versus reported.** Not an encyclopaedia entry. The card routes its version-of-record wording through Ripstein and Herstein and labels it that way.
5. **May (Where it bears).** K7 timing boundary: LICENSED (ts pp. 38–40, 46). 'So the sooner a holder learns of a lapse the closer the conformity still open to it' is LICENSED-NARROWER: it is the card's inference, and closeness is fixed 'by the reasons for the original obligation' (ts p. 46), not by time alone. K5: LICENSED (ts pp. 54–55).
6. **Central conclusions.** Bears on (d).
7. **Reader's own inferences.** That repair begins during the stay, lapse by lapse (R3 statement 45): SUPPORTED by ts pp. 35–36 and 46, and by p. 53, where belated performance of a positive obligation counts as a remedy. The version-of-record page estimate (near pp. 32–34) is consistent with linear interpolation between the two fixes. It is unverified.

### ripstein2026theories

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** The live entry is byte-identical to the saved file. It prints 'First published Thu Jun 2, 2022; substantive revision Mon Jun 15, 2026', with author Ripstein, Arthur. The citation page gives the Fall 2026 Edition ('minor correction'), whose main text is identical to the live text.
2. **Read depth.** §§2 and 4. As stated.
3. **Quotations.** 21 strings, all MATCH at the stated section and paragraph. The slip is real: §4.2, para. 7 ends 'the law of negligence does require a person to protect others', against para. 3's 'does not suppose that there is a duty to protect'.
4. **Stated versus reported.** Gardner is 'as reported'. Smith's denial sits inside the civil-recourse paragraph (§4.4, para. 3), which is how the entry itself frames it, and the state's duty is attributed there to Goldberg and Zipursky. Liau and Steel and Stevens are named as reported (§4.5, para. 1). The card notes that the author is a party to the dispute. Correct.
5. **May (Where it bears).** K7: LICENSED, except 'The legal analogues in tort point to later repair, so K7 rests on P3', which is LICENSED-NARROWER. The entry records injunctions 'in a limited range of cases' (§2, para. 1) and surveys theories, not legal analogues. Narrower: *on the theories the entry reports, the tort remedy is mainly damages after the wrong.* K5 and K6: LICENSED.
6. **Central conclusions.** Bears on (d).
7. **Reader's own inferences.** R3 statement 53 (that, if Smith is right, the guest holds a power and the host a liability) is a fair Hohfeldian restatement of §4.4, para. 3: SUPPORTED.

### fox2007uncertain

**Verdict: PASS-WITH-NOTES.**

1. **Identity.** Crossref 10.1080/09614520701469955 gives Fox, Jonathan, 'The uncertain relationship between transparency and accountability', *Development in Practice* 17(4–5), 663–671, print Aug 2007. That matches the card. The eScholarship landing page returned 403 to me on 11 Nov; I relied on Crossref and the saved file.
2. **Read depth.** The publisher's (Routledge/Informaworld) PDF of the version of record, downloaded 7 Sep 2007, with the 6 Nov 2007 erratum page (17(6), p. 839) bound in. Journal page = PDF page + 660, confirmed (PDF p. 3 = p. 663). The file has three cover sheets, not two; this does not matter.
3. **Quotations.** 18 strings. 17 MATCH within a single page; 'Both concepts are inherently relational …' runs across the break from p. 663 to p. 664, exactly as the card's 'pp. 663–664' says. The erratum reads 'starting with Sweden in1766' and says the date 'was changed without authorisation to 1966'. Correct.
4. **Stated versus reported.** Schedler is marked as the source of the term and of the two-dimension analysis ('Fox (2007: 665), following Schedler'), and Thompson's 'problem of many hands' is marked as reported. 'Soft face' is Fox's own coinage ('One could call answerability the 'soft face''), and the card attributes it to Fox. Correct.
5. **May (Where it bears).** K7 vocabulary: LICENSED. 'Supports also the paper's warning that information is offered in place of answerability (p. 664)' is LICENSED-NARROWER: Fox writes that elites respond 'by offering some measure of transparency instead' of accountability. K8: LICENSED.
6. **Central conclusions.** Bears on (c).
7. **Reader's own inferences.** That answerability is backward-looking (pp. 665, 668): SUPPORTED.

### duff2009legal

**Verdict: PASS.**

1. **Identity.** Crossref 10.1111/j.1747-9991.2009.00257.x gives Duff, Antony, 'Legal and Moral Responsibility', *Philosophy Compass* 4(6), 978–986, online 25 Nov 2009. That matches the card. The Stirling handle responds (HTTP 200).
2. **Read depth.** The author's typescript, 12 pages, headed '(2009) 4/6 Philosophy Compass 978-86'. It is probably the accepted manuscript; I did not compare it with the version of record, which is closed. Typescript pages are printed and equal PDF pages.
3. **Quotations.** 14 strings, all MATCH at the stated section and typescript page. §2 begins on p. 3 and §3 at the foot of p. 5. 'Accountability' occurs nowhere in the typescript, which confirms Critical note 1.
4. **Stated versus reported.** Not an encyclopaedia entry. Lucas, Watson and Gardner are cited inside Duff's own note 12.
5. **May (Where it bears).** LICENSED.
6. **Central conclusions.** Bears on (c) only by contrast: Duff pairs answerability with liability.
7. **Reader's own inferences.** None beyond the labelled applications.

### dekenessey2024two

**Verdict: PASS-WITH-NOTES** (the access route needs the lead's ruling under guard 6; the content is accurate).

1. **Identity.** Crossref 10.1111/phpr.13083 gives de Kenessey, Brendan, 'Two concepts of directed obligation', *PPR* 109(3), 913–938, online 24 Jun 2024, print Nov 2024. That matches the card. The saved Wiley HTML capture also gives 'Volume 109, Issue 3' and '913-938'.
2. **Read depth.** The saved PDF is Wiley's typeset Early View version of record. It carries 'Philos Phenomenol Res. 2024;1–26', the CC BY-NC notice, and a Wiley download stamp of 24/06/2024; macOS re-saved the file later. EV pages 1–26 + 912 = 913–938 holds arithmetically. The file came from Internet Archive captures because Wiley and PhilPapers return a bot check. Whether such captures satisfy guard 6 is for the lead; R3 says so too.
3. **Quotations.** 28 strings, all MATCH at the stated EV page. The section and footnote locators are right: §1 from p. 4, §1.1 p. 4, §1.2 p. 6, §2 / §2.1 p. 8, §2.2 p. 10, §3 p. 13, §4 p. 18; n. 4 and n. 6 on p. 3, n. 13 on p. 8, n. 15 on p. 9. The 'extensionally dissociable' sentence closes §3 on p. 18, before §4 opens on the same page.
4. **Stated versus reported.** Not an encyclopaedia entry. The disagreement with Gilbert (n. 15) is marked as the author's. Correct.
5. **May (Where it bears).** K6 and K5: LICENSED. K7 second route: LICENSED.
6. **Central conclusions.** Bears on (a) (it is the counter-instance) and on (b).
7. **Reader's own inferences.** The classification of the duty to attend as welfare-based (card note 3; R3 statement 24) is SUPPORTED-NARROWER. §3 grounds accountability where an agent 'significantly harms your interests without sufficient justification' (p. 18), and the text does not settle whether a lapse in attending reaches that threshold. The hostage extension (R3 statement 20) is SUPPORTED as analogy, and is labelled as one.

---

## R3 report: 'the paper may say' sentences

| Report §, sentence | Verdict | Narrower wording or reason |
|---|---|---|
| §3: 'in the classical code attention is the guest's due' (Pitt-Rivers 2012: 515–517) | LICENSED-NARROWER | At p. 516 'which is their due' modifies 'precedence', not attention. Narrower: *precedence is the guest's due; failing to attend to guests and to show concern for their needs infringes the law of hospitality, and 'Failure to offer the best is to denigrate the guest' (p. 516)*. Note also p. 513: the dissatisfied guest 'has no recourse but to retire from his role altogether by walking out'. |
| §3: a duty owed to someone is that person's claim (Wenar and Cruft §2.1.2) | LICENSED | Displayed definition; §2.2.3, para. 1. |
| §3: theories divide on whether a claim includes the standing to demand (§2.2.2) | LICENSED-NARROWER | §2.2.2 frames the dispute as one over function: control (will), interests (interest), authority to demand (demand theories). Say that. |
| §3: the guest's position is a claim on one family of theories and none on another | LICENSED-NARROWER | No source states it. Present it as the authors' reading. |
| §4: the guest's legal claims follow from the host's legal duties | LICENSED-NARROWER | Only for duties owed to the guest: *where a legal duty of the host is owed to the guest, the guest holds the correlative claim*. |
| §4: the argument does not depend on the dispute | LICENSED | The authors' structural claim; no source contradicts it. |
| §5: Fox, two dimensions; 'soft face' | LICENSED | p. 665; p. 668 ('One could call …'). |
| §5: answering 'is owed to the person affected' (Duff) | LICENSED-NARROWER | Shown in one example ('answer to you as the owner', ts p. 4); in criminal law one answers to the court. |
| §6: a duty that can no longer be performed leaves a duty to do the next-best thing | LICENSED-NARROWER | Add 'normally' or 'all else being equal' (Ripstein §4.3, para. 3: 'the normal response'; Gardner ts pp. 39–40: 'often', 'If all else is equal'). |
| §6: repair never equals performance, so what can be corrected while performance is possible should be | LICENSED-NARROWER | First clause: Gardner ts p. 42, n. 56 (version of record needed). Second clause: the authors' inference. |
| §6: the channel serves performance and near-performance, accountability serves repair | NOT-LICENSED | No source read says this. It is the authors' framing and may be offered only as such. |

All 'may not say' sentences in the R3 report are correct. One rests on an overstatement: 'that the continuity thesis yields a duty … to explain' is right, but because the thesis is silent on explanation, not because Gardner excludes it.

---

## The nine central conclusions

**(a) On the standard account a duty owed to A is equivalent to A's claim, and no text read describes a competent adult who is owed a duty yet may not demand it. NARROWED.** The first half is CONFIRMED. Wenar and Cruft §2.1.2: "A has a claim that B φ if and only if B has a duty to A to φ"; §2.2.3, para. 1 calls this 'the standard account'; Herstein §3.1.1, para. 1 says the same. The second half fails as the brief words it. De Kenessey describes a competent adult who is owed a duty in the constraint sense and who may not fittingly demand its performance: "What they can't fittingly do is demand that you not break into the cabin in the first place or resent you for doing this" (§2.1, EV p. 9, after P1–P2–C). His hostage has warrant to demand and 'ought not make this demand' (§1.2, p. 6). The conclusion holds only in R3's own narrower form (statement 9): no text read describes a competent adult owed a duty that is *not overridden* whom a *rule of role* forbids to demand it. Even that form excludes the customary source R3 rechecked. Pitt-Rivers says 'even though a diffuse obligation exists towards the beggar, he is not endowed with any corresponding right' (p. 509), and that the dissatisfied guest 'has no recourse but to retire from his role' (p. 513).

**(b) The theories of rights disagree on whether standing to demand is part of a claim, and agree on the ordinary case. NARROWED.** The disagreement is CONFIRMED. 'Which theory offers the better account of the functions of rights has been the subject of spirited dispute, literally for ages' (Wenar and Cruft §2.2.2, para. 1). The will theory makes every right include 'a Hohfeldian power over a claim' (para. 2), and demand theories make rights 'what the right-holder may demand' (para. 17). Herstein adds 'The debate remains unsettled' (§4, para. 7), and Sreenivasan calls it 'a clear mistake to make standing to demand pivotal to the analysis of claim-rights'. No text states that the theories agree on the ordinary case. The agreement is R3's inference from three things: no text disputes it; two authors affirm it in passing ('usually', de Kenessey EV p. 2; 'typically', p. 14; 'I see no reason to deny that a property owner also has standing to demand', Sreenivasan); and demand theories' admitted difficulty is confined to 'parties incapable of demanding' (Wenar and Cruft §2.2.2, para. 17). Wording the texts bear: *the theories record no disagreement about the ordinary case.*

**(c) Fox makes answerability a part ('soft face') of accountability, following Schedler. CONFIRMED.** "two dimensions of accountability: on the one hand, the capacity or the right to demand answers (what Schedler calls 'answerability') and, on the other hand, the capacity to sanction (1999)" (p. 665); "One could call answerability the 'soft face', while the 'hard face' includes answerability plus the possibility of sanctions" (p. 668). The term and the two dimensions follow Schedler; the 'soft face' label is Fox's own. On the same page Fox reports that 'For many, however, answerability without consequences falls short of accountability'.

**(d) The continuity thesis grounds a duty of repair after breach and says nothing of a duty to be reachable or to explain. CONFIRMED, with two corrections.** The thesis grounds a secondary obligation 'to do the next-best thing' (ts p. 40). That obligation is wider than repair: it includes belated performance, the beach tomorrow or a late delivery (ts pp. 34–35, 53). Reparation for losses is its 'normal' application (ts pp. 40, 45). The thesis is silent on reachability: no passage in ts pp. 33–60 addresses it, and the words 'reachab' and 'contact' never occur. Ripstein's criticism agrees: reference to the wronged party 'is not essential' (§4.3, para. 4). It is also silent on explanation. Every use of 'explain' in the eprint concerns explaining tort law. Gardner places only expressions of emotion ('confessing or apologizing') outside correction (n. 57); he does not expressly exclude explanation.

**(e) No legal instrument read requires both a route from the affected person and a person with power over the single decision. REFUTED as worded; holds in R6b's narrower form.** The platform work directive requires both, for persons performing platform work. It gives the route: 'the right to request the digital labour platform to review the decisions' (art. 11(2)) and access to a contact person (art. 11(1)). It also requires persons with 'the competence, training and authority necessary to exercise that function, including for overriding automated decisions' (art. 10(2)), a human being to take the gravest decisions (art. 10(5)), and the platform to 'rectify that decision' (art. 11(3)). What it does not do is make the reachable person the one with power: the contact person's function is 'to discuss and to clarify'. The Spanish finance regime lets entities designate (**'podrán … designar'**) a Defensor de la Clientela whose favourable decision 'vinculará a la entidad' (new art. 29(1)–(2), Ley 44/2002). That is optional, not required. The AI Act's art. 27(1)(f) asks some deployers for 'complaint mechanisms' without linking them to the overseer. The form that survives is R6b's statement 15: no instrument read requires, *for a consumer or guest*, a channel from the person affected *to* a person with power over the single case, available before the effect.

**(f) The platform work directive, arts 10–11, requires human review of significant decisions with stated time limits and covers workers only. NARROWED.** The time limits are CONFIRMED: reasons 'at the latest on the date on which it takes effect' (art. 11(1)); a review reply 'within two weeks of receipt of the request' (art. 11(2)); rectification 'within two weeks of the adoption of the decision' (art. 11(3)). The rest needs correction. Art. 11 is headed 'Human review', but its operative text does not require a human reviewer. What is human is the taking of the gravest decisions (art. 10(5)) and the overseers (art. 10(2)). Explanation and review cover 'any decision taken or supported by an automated decision-making system', not only significant ones. The protected class is 'persons performing platform work', employed or not (arts 1(2), 2(1)(c)), not 'workers' in the employment sense. Self-employed business users under Regulation (EU) 2019/1150 are excluded from art. 11 (art. 11(5)), and recipients of the service get nothing.

**(g) The UK Data (Use and Access) Act 2025 replaced the general prohibition with safeguards, and from what date. CONFIRMED, with a caveat.** Section 80(1): 'For Article 22 of the UK GDPR … substitute—' Articles 22A–22D. Art. 22B forbids a solely automated significant decision only where it rests on special-category data, unless a stated condition is met, or relies on Article 6(1)(ea). Art. 22C otherwise requires safeguards about decisions 'taken'. Commencement: 'S. 80 in force at Royal Assent for specified purposes' and 'S. 80 in force at 5.2.2026 in so far as not already in force by S.I. 2026/82, reg. 2(j) (with reg. 5)'. Reg. 5 saves decisions taken before 5 February 2026. The caveat: 'general prohibition' describes the EU Article 22 as *SCHUFA* reads it (para. 52). Nobody in this batch read the former UK Article 22.

**(h) *Mathews v Eldridge* did not require a hearing before the deprivation, and its three-factor test in the Court's words. CONFIRMED, narrowed to 'evidentiary hearing'.** "We conclude that an evidentiary hearing is not required prior to the termination of disability benefits and that the present administrative procedures fully comport with due process" (424 U.S. at 349). The Court also held that 'some form of hearing is required before an individual is finally deprived of a property interest' (at 333), and it relied on the prior notice, reasons and written reply (at 324, 346). The test, at 334–335: "identification of the specific dictates of due process generally requires consideration of three distinct factors: First, the private interest that will be affected by the official action; second, the risk of an erroneous deprivation of such interest through the procedures used, and the probable value, if any, of additional or substitute procedural safeguards; and finally, the Government's interest, including the function involved and the fiscal and administrative burdens that the additional or substitute procedural requirement would entail."

**(i) The date from which AI Act arts 14 and 26 apply to Annex III systems. CONFIRMED: 2 December 2027.** Regulation (EU) 2026/1744, point (40)(b), replaces art. 113, third paragraph, point (c): "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III". In the OJ text art. 14 sits in Chapter III, Section 2 (arts 8–15) and art. 26 in Section 3 (arts 16–27). Both texts were re-fetched from the Publications Office on 11 Nov 2026. Before the amendment those duties applied from 2 August 2026, the general date: the original point (c) deferred only 'Article 6(1) and the corresponding obligations', to 2 August 2027.

---

## Table: every FAIL, every quotation that is not MATCH, and every 'may say' sentence that is not LICENSED

| Item | Card or report | Finding | Correction |
|---|---|---|---|
| FAIL | — | None. | — |
| Quotation not MATCH | — | None of 589 quotations. 7 AI Act search strings are reported correctly. | — |
| May say (3) | `es2025clientela` | LICENSED-NARROWER | Supervisor *or quality department*; call-back the same working day if transfer within three minutes fails (art. 8(3)). |
| May say (4) | `es2025clientela` | LICENSED-NARROWER | Add 'selling mainly to consumers in Spain' (art. 2(2)). |
| May say (6) | `es2025clientela` | LICENSED-NARROWER | Add the safety and sector-rule exceptions (art. 4(4)). |
| May say (3) | `uk2025datause` | LICENSED-NARROWER | 'For any solely automated significant decision based on personal data', not 'for other' (art. 22C(1)). |
| May say (4) | `mathews1976eldridge` | LICENSED-NARROWER | The holding rests on all three factors (at 340–349), not only on retroactive relief and the written reply. |
| May say (1) | `eu2024aiact` | LICENSED-NARROWER | 'Provided … so that [overseers] are enabled, as appropriate and proportionate' (art. 14(4)). |
| May say (3) | `eu2024aiact` | LICENSED-NARROWER | 'May result in … a risk'; 'provider or distributor' (art. 26(5)). |
| May say (4) | `eu2024aiact` | LICENSED-NARROWER | Art. 86(1) limits: Annex III except point 2; legal or similarly significant adverse effect; art. 86(3). |
| May say (6) | `eu2024aiact` | LICENSED-NARROWER | 'The duties in arts 14 and 26'; arts 85–86 are in Chapter IX. |
| May not say (2), support | `eu2024aiact`; R6b items 12, 35 | Caveat missing | Art. 27(1)(f) and recital 96 require some deployers to set out complaint mechanisms (not read by R6b). |
| Where it bears, K6 | `sreenivasan2019rights` | LICENSED-NARROWER | He affirms the standing of 'a property owner'. |
| Critical note 4 | `gardner2011what` | Paraphrase overstates | n. 57 names 'confessing or apologizing'; explanation is not mentioned, so the thesis is silent on it, not expressly exclusive. |
| Critical note 5; Where it bears | `gardner2011what` | LICENSED-NARROWER | n. 53 concerns acts 'both necessary and sufficient'. |
| Where it bears, K7 | `gardner2011what` | LICENSED-NARROWER | 'The sooner … the closer' is the card's inference; closeness is fixed by the reasons (ts p. 46). |
| Where it bears, K7 | `ripstein2026theories` | LICENSED-NARROWER | 'On the theories reported, the remedy is mainly damages after the wrong'; injunctions 'in a limited range of cases'. |
| Where it bears, K7 | `fox2007uncertain` | LICENSED-NARROWER | 'Transparency offered instead of accountability' (p. 664). |
| R3 §3 | `WS_P3_R3.md` | LICENSED-NARROWER | 'Their due' attaches to precedence (Pitt-Rivers p. 516). |
| R3 §3 (two sentences) | `WS_P3_R3.md` | LICENSED-NARROWER | The dispute is over function; the guest's status is the authors' reading. |
| R3 §4 | `WS_P3_R3.md` | LICENSED-NARROWER | Only duties owed to the guest yield the guest's claims. |
| R3 §5 (Duff) | `WS_P3_R3.md` | LICENSED-NARROWER | Owed to the owner in Duff's example; to the court in criminal law. |
| R3 §6 (two sentences) | `WS_P3_R3.md` | LICENSED-NARROWER | Add 'normally'; the second clause is the authors' inference. |
| R3 §6 (channel/repair) | `WS_P3_R3.md` | NOT-LICENSED | No source; the authors' framing only. |
| Conclusion (e) | brief | REFUTED as worded | Use R6b's statement 15 form (consumer or guest; route *to* the person with power; before the effect). |

Written by a Claude (Opus 5.5) verifier subagent (CV-D) from the saved source texts and records re-fetched on 11 November 2026, run rr-2026-11-k.

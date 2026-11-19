<!-- Independent verification of cards, batch CV-E, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-E (run rr-2026-11-k)

I am verifier CV-E. I did not write these seventeen cards, and I edited none of them. Nine come from reader R1 (`WS_P1_R1.md`) and eight from reader R2 (`WS_P2_R2.md`). I checked each card against its saved source under `manuscript/revision_2026-11/research/sources/` and against a record I fetched again myself. Nothing was committed: the run brief forbids it, although the repository's `AGENTS.md` asks every session to commit and push. I use the first person only for my own checks, as the run brief and the sibling file `VERIFY_CARDS_A.md` do.

**Verdicts.** 5 PASS, 12 PASS-WITH-NOTES, 0 FAIL.

**Quotation tally.** A script extracted about 900 quoted strings from the seventeen cards, counting repeats and short phrases. Every quotation offered as evidence in the 'Key facts' sections is a MATCH at the stated locator. Five strings elsewhere on the cards are not. Three are PARAPHRASED-AS-QUOTE: one in O'Gorman 2007's critical notes, one in Hindriks's hold rationale and one in Dogru's 'Where it bears'. A fourth is a word quoted from the wrong part of the entry (Dagger). The fifth is correct words given the wrong speaker (Jeske, about Dowie's report of Hardimon). Two further problems affect strings that do match. Brandt's quotations match the accepted manuscript, but the manuscript's wording differs from the version of record in at least one place I could check. The Kant card names the wrong publisher for the 1903 edition.

**'May say' sentences.** Of 83, 76 are LICENSED and 7 are LICENSED-NARROWER. None is NOT-LICENSED. All 85 'may not say' items are justified prohibitions. One of them (Dagger) supports itself with a misplaced quotation.

**Seven central conclusions.** (a), (b), (c), (d), (e) and (g) are CONFIRMED and (f) is NARROWED. Details are in the section near the end.

## How I checked

- **Records.** On 11 Nov 2026 I re-fetched the Crossref records for the nine cards that have DOIs (`api.crossref.org/works/<doi>`) and compared authors, title, venue, volume, issue, pages and dates. I re-fetched the three Stanford Encyclopedia entries and their citation pages; all three live pages are byte-identical (SHA-256) to the saved HTML. The OHCHR PDF and the Delaware slip opinion re-fetched byte-identical too. I queried Crossref for O'Gorman 2005 and found no record, and the ISSN 1447-6770 has no 2005 records at all. I re-fetched the Strathprints (5843, 5986, 5988, 4977), Bournemouth (836) and Lancaster (82486) repository pages for their version labels. I asked Unpaywall about seven DOIs and the Internet Archive catalogue about the 1903 Kant edition. That catalogue returned four records, all 'London, Swan Sonnenschein, 1903'. I then read the OCR text of one scan (`perpetualpeaceap00kantuoft`) to compare page breaks. Two attempts were refused and I did not repeat them: Wiley's open PDF of Brandt's version of record (HTTP 403) and CourtListener's search (credentials required). I met no login or bot check.
- **Quotations.** The read-only script `qcheck.py` (scratchpad) listed every quoted string on each card. It searched the saved text after normalising whitespace, line-end hyphens and ligatures (including the 'Þ' and 'ß' that stand for 'fi' and 'fl' in the Morrison PDF), and it reported the page, or the section and paragraph, where each string falls. I extracted every PDF afresh with `pdftotext` and mapped each one's pages to its printed pages: Hemmington pp. 1-19, O'Gorman 2005 pp. 141-151, the UN Guiding Principles (PDF p. n = printed p. n-5), *Marchand* (PDF p. n = slip op. p. n-2), Hindriks ('Page n of 18') and Brandt (manuscript pp. 1-18). I split the Stanford Encyclopedia HTML into paragraphs by R2's own convention, under which a block quotation or list belongs to the paragraph that introduces it. Every R2 section-and-paragraph locator I tested holds under that convention. I counted the 53 blocks of Benveniste's chapter 7 after 'Text' as R1 did, and his paragraph numbers hold. I read every miss by hand. Most were page breaks with a running head or footnotes between the two halves of the quotation, and each was confirmed on both sides of the break.
- **Second-hand passages.** I opened every carrier text that R1 and R2 list and checked each quoted passage with the same script. That covers Telfer T1-T16, Derrida D1-D15, Hardimon H1-H10, Simmons S1, Goodin G1-G4 and Scanlon Sc1-Sc4. The results are in the section on second-hand notes.

---

## morrison2008hospitality

**PASS-WITH-NOTES**

1. **Identity.** Crossref 10.1016/j.ijhm.2007.07.028 matches the card: Alison Morrison and Kevin O'Gorman, 'Hospitality studies and hospitality management: A symbiotic relationship', *International Journal of Hospitality Management* 27(2): 214-221, issued June 2008. Crossref has no abstract.
2. **Read depth.** The saved PDF is 15 unpaginated pages (SHA-256 7f5edad6…), the file the card describes. Strathprints 5988 labels it 'Accepted Author Manuscript', as the card says, but Unpaywall classes the same file as `submittedVersion`. The version of record was not seen, and the DOI resolves to an Elsevier page. So whether Figure 2 carries the sentence on safety in the published article, and under what figure number and on what page, is unverified. The card already says no journal page can be given.
3. **Quotations.** 66 strings, all MATCH at the stated AM pages. I confirmed the negative claims. 'Safety' and 'security' occur only in the Figure 2 bullet (AM p. 15). Figure 1 (AM p. 14) has 24 verses, and none of them mentions guests' health, safety or security; the one 'protect' is v. 5, 'to protect from the deceptions of the devil'. Figure 2 has 33 bullets, and none of them states when a responsibility begins. The statement on businesses' responsibility is the fourth of six 'Business Principles', as the card says.
4. **May say.** (1) LICENSED. (2) LICENSED-NARROWER. The method section says the principles 'emerged as clear divisions of both the Rule and contemporaneous monastic practice', and the authors drew on modern commentaries and on Wolter's (1880) collection of medieval texts (AM p. 6). It does not say they came from the Rule alone. (3), (4), (5) LICENSED.
5. **May not say.** All five are justified. The prohibition on citing the Rule for a safety duty rests on Figure 1, which I read whole.

## hemmington2007

**PASS-WITH-NOTES**

1. **Identity.** Crossref 10.1080/02642060701453221 matches: Nigel Hemmington, 'From Service to Experience: Understanding and Defining the Hospitality Business', *The Service Industries Journal* 27(6): 747-755, September 2007.
2. **Read depth.** The saved PDF matches the card: 19 pages, running head 'The Service Industries Journal, September 2007, Volume 27, Number 6', created 14 Feb 2007 (pdfinfo). Unpaywall classes it as `submittedVersion`. 'Author's version', the card's term, is accurate. A version made before publication may differ from the published text, which the card already warns of.
3. **Quotations.** 61 strings, all MATCH at the stated AV pages. Three run across a page break: AV pp. 12-13, 15-16 and 16-17. Telfer's sentence on safety is on AV p. 15 with no Telfer page. Figure 1's three rows and footnote 10 are on AV p. 10.
4. **May say.** (1), (2), (4), (5) LICENSED. (3) LICENSED-NARROWER. Hemmington writes that security 'should, therefore, focus on guest security – the security of strangers'. He then adds: 'This does not mean that financial security should be ignored, but that from the guest's perspective their personal security is clearly visible and seen as the dominant concern rather than the security of the hotel's resources and procedures' (AV pp. 15-16). 'And not on the firm's goods' overstates the contrast. Suggested sentence: 'Hemmington argues that security in hospitality "should ... focus on guest security", which guests see as the dominant concern over the security of the hotel's resources and procedures (AV pp. 15-16).'
5. **May not say.** All five are justified.
6. **Status.** The card's `status: cited` and R1's note that `DRAFT_v6.md` does not mention Hemmington are for the authors to decide. I did not check them.

## kant1795perpetual

**PASS-WITH-NOTES**

1. **Identity: one mismatch.** The Project Gutenberg transcription's title page reads 'London: George Allen & Unwin Ltd.', followed by 'First Edition, 1903 / Second Impression, February 1915 / Third ″ February 1917'. These are the publisher and impressions of the 1917 printing. The 1903 first edition was published by **Swan Sonnenschein**, London. Four Internet Archive catalogue records give 'London, (Swan) Sonnenschein, 1903', and the scanned title page of `perpetualpeaceap00kantuoft` reads 'SWAN SONNENSCHEIN & CO., LIM.' and '1903'. The card's venue line ('London: George Allen & Unwin (first edition 1903; third impression 1917)') and R1's BibTeX entry (publisher Allen & Unwin, year 1903) pair the later publisher with the earlier year. The entry should cite either Swan Sonnenschein 1903 or Allen & Unwin 1917 (third impression). The citekey year, 1795, is the original date, not the edition cited; R1 says so in a note.
2. **Translation and locator stability.** The translation is M. Campbell Smith's. In the 1903 OCR the Third Definitive Article opens on p. 137, and the page breaks after 'the stranger can lay' and before 'claim—', exactly as in the 1917 transcription. The printed pages 137-139 are therefore stable across both printings. The Akademie locators are independent of edition, and I confirmed them on the saved Bonn pages: the article heading at 8:357.19-21, the definition at 8:357.22-358.05, 'kein Gastrecht ... sondern ein Besuchsrecht' at 8:358.05-08, and the limit of the right at 8:358.23-25. Nisbet's translation (Cambridge University Press 1991, p. 105) is reachable only as Westmoreland quotes it (2008: 4, n. 17), which I confirmed.
3. **Read depth.** The card claims the Third Definitive Article, and the saved HTML has it whole between the markers for pp. 137 and 142. The claim is honest.
4. **Quotations.** 39 strings, all MATCH. Two run across a page break, pp. 137-138 ('lay | claim') and pp. 140-141. The German quotations match the Bonn text. Kyslan's 'Besuchsrecht (right to visit)' is on Kyslan p. 77 and '8: 357–360' on p. 78; his 'duty on both sides' reading is on p. 79.
5. **May say / may not say.** All four 'may say' sentences are LICENSED and all four 'may not say' items are justified.

## benveniste1973indoeuropean

**PASS-WITH-NOTES**

1. **Identity.** The Center for Hellenic Studies book page (saved; fetched 11 Nov 2026) reads: 'Translated from the French by Elizabeth Palmer, this online edition has been revised and updated by Jeremy Lin, Jacqueline Lewandowski, and Vergil Parson', and 'Originally published in 1973 by University of Miami Press as Miami Linguistics Series no. 12'. The card matches. Bulley (2015, AM p. 8, confirmed) cites the London Faber printing, 'Benveniste 1973: 71' and ': 74'. That printing's place and publisher differ from the Miami printing's.
2. **Translation and locator stability.** The translator is Elizabeth Palmer. The 'para. n' locators are R1's count of text blocks in a revised online edition. They are not stable, and nobody in this run has checked a printed page. The card says this.
3. **Quotations.** 49 strings, all MATCH at the stated paragraph count (paras 2, 22-24, 30-36, 38, 45, 50, 53; summary points 2-3).
4. **May say.** (1), (2), (3) LICENSED. (4) LICENSED-NARROWER. In context, 'The one who receives is not the "master" of his guest' is a claim about the compounds *atithi-pati* and *hospes*, backed by 'As we have seen, -pot- did not have originally the meaning of "master"' (para. 34). Para. 2 had given 'the guest-master' as the literal sense before revising it. Suggested sentence: 'Benveniste argues that in *hospes* the element *-pot-* did not originally mean "master", so that the one who receives "is not the 'master' of his guest" (ch. 7, para. 34).'
5. **May not say.** All four are justified.

## ogorman2005modern

**PASS**

1. **Identity.** There is no DOI. A Crossref bibliographic query on 11 Nov 2026 returned no match, and Crossref holds no 2005 records for ISSN 1447-6770. Strathprints 5843 gives 'Journal of Hospitality and Tourism Management, 12 (2). pp. 141-151. ISSN 1447-6770'. The running foot reads 'Volume 12 Number 2 August 2005 pp. 141 – 151'.
2. **Read depth.** The repository labels the file 'Accepted Author Manuscript', but the PDF is the typeset article with printed pp. 141-151. The card's journal-page locators are right.
3. **Quotations.** 61 strings, all MATCH at the stated journal pages. Two run across a page break, pp. 142-143 and 143-144. The Schmitz passage the card compares is on p. 621 of the saved LacusCurtius transcription.
4. **May say / may not say.** All four 'may say' sentences are LICENSED. For sentence (1), the Roman duties to protect and represent (p. 145) rest on Schmitz (1875), and the Greek ones rest on the *proxenos* and on *philoxenos* (pp. 143-144). All four 'may not say' items are justified.

## ogorman2007phenomenon

**PASS-WITH-NOTES**

1. **Identity.** Crossref 10.1108/17506180710817729 matches: Kevin D. O'Gorman, 'The hospitality phenomenon: philosophical enlightenment?', *IJCTHR* 1(3): 189-202, issued 14 Aug 2007. Unpaywall: closed.
2. **Read depth.** Strathprints 5986 labels the file 'Accepted Author Manuscript'. It has 25 pages numbered 1-25, which the card's AM locators use. The 2006 magazine version (Strathprints 4977, 'Final Published Version', *The Hospitality Review* 8(4): 50-57) carries the Telfer 1996: 82 and 101 quotations and Derrida p. 77 on p. 51, and Derrida pp. 25 and 59f on p. 52. Its text layer is garbled in two columns ('he' for 'The', 'ofer'), but the words are present.
3. **Quotations.** 62 strings. Every 'Key facts' quotation is a MATCH at the stated AM page. One is not a MATCH. In the critical notes the card writes that the commercial context has "'its own different sets of laws'", but the article says 'each with **their** own different sets of laws' (AM p. 22). This is PARAPHRASED-AS-QUOTE. The 'Key facts' and 'may say' sections quote it correctly.
4. **May say / may not say.** All four 'may say' sentences are LICENSED and all five 'may not say' items are justified. The card is right that O'Gorman's summary of Kant (AM pp. 9-10, 'a universal right to shelter') conflicts with Kant's text (p. 137, 'may send him away again').

## westmoreland2008interruptions

**PASS**

1. **Identity.** Crossref 10.3860/krit.v2i1.566 matches: Mark W Westmoreland, 'Interruptions: Derrida and Hospitality', *Kritike* 2(1), issued 8 Sept 2008, with no page field. The article head reads 'KRITIKE VOLUME TWO NUMBER ONE (JUNE 2008) 1-10'.
2. **Read depth.** The saved journal PDF is the whole article, pp. 1-10, with the notes. Westmoreland cites *Of Hospitality* in Rachel Bowlby's translation (n. 3).
3. **Quotations.** 53 strings, all MATCH. 'GrecoRoman' in the text layer is a hyphen lost at a line end. The footnote pages for Derrida agree with R1's table: nn. 6 (p. 29), 15 (p. 25), 19 (*Adieu* 83 with *Of Hospitality* 147), 27 (p. 15), 31 (p. 55), 32 (p. 25), 35 and 38 (p. 125), 43 (p. 77) and 44 ('See Ibid., 79').
4. **May say / may not say.** All four 'may say' sentences are LICENSED and all four 'may not say' items are justified.

## koo2026three (abstract only)

**PASS**

1. **Identity.** Crossref 10.1108/ijchm-10-2025-1555 matches: Chulmo Koo and Jookyung Kwon, *IJCHM* 38(8): 2471-2486, online 24 July 2026 and print 3 Aug 2026. Unpaywall: closed.
2. **Read depth.** The card claims the abstract only. Every statement in it rests on the structured abstract, which I re-fetched. Nothing beyond the abstract is attributed to the article. The negative claims hold: the abstract does not use 'host', 'guest', 'duty', 'obligation' or 'organization'.
3. **Quotations.** 15 strings, all MATCH against the re-fetched abstract.
4. **May say / may not say.** Both 'may say' sentences are LICENSED and all three 'may not say' items are justified.

## dogru2025service (abstract only)

**PASS-WITH-NOTES**

1. **Identity.** Crossref 10.1108/ijchm-02-2025-0249 matches the five authors, the title and *IJCHM* 37(12): 4101-4121, online 29 Oct 2025. Unpaywall: closed.
2. **Read depth.** Only the abstract is claimed, and nothing beyond it is attributed. The negative claim holds: the abstract does not use 'host', 'guest', 'duty', 'obligation' or 'responsibility'.
3. **Quotations.** 15 strings. All abstract quotations MATCH. One is not a MATCH. Under 'Where it bears' the card writes that "'hospitality at the organizational level'" is a named topic. The abstract's words are 'practiced at the organizational level' and 'organization-level hospitality virtue'. This is PARAPHRASED-AS-QUOTE.
4. **Wrong refuter number.** The card calls the refuter on 'hospitableness scholars who already assign the host's duty to an organization' K2's *second*. In `CLAIMS_FIXED.md` it is the third bullet, and R1's report (section (a), 'The gap statement') also calls it the third.
5. **May say / may not say.** Both 'may say' sentences are LICENSED and all three 'may not say' items are justified.

## jeske2019special

**PASS-WITH-NOTES**

1. **Identity: one mismatch.** The live entry's metadata give Jeske, Diane, 'Special Obligations', issued 2002-10-17 and modified 2019-08-06. The citation page reads: 'The latest version of the entry may be cited via the earliest archive in which it appears: Jeske, Diane, "Special Obligations", The Stanford Encyclopedia of Philosophy (Winter 2021 Edition), Edward N. Zalta (ed.)'. The citekey and the card carry 2019; the recommended citation is Winter 2021. R2 flagged this, and the authors should pick one.
2. **Read depth.** The saved HTML holds the whole entry, the notes page and the bibliography. The card claims all three.
3. **Quotations.** 76 strings, all MATCH at the stated section and paragraph. That includes §2 para. 6, §3 paras 1-2, §4 paras 2-24, §6.2 para. 2, §6.3, §6.4 para. 4 (the last), §7 paras 2-3, §8 paras 4-5 and note 3. The negative claims hold. 'Goodin' does not occur in the entry. 'Vulnerable' occurs once, of pets, at §9 para. 3. The bibliography lists Simmons 1979 and 1996 ('Associative Political Obligations') and not 'External Justifications'.
4. **Positions stated versus reported.** The card separates Jeske's own arguments (§4 paras 10, 18-19; §6.4; §8 para. 5) from views she reports, and marks each reported view with its section. Hardimon's are at §4 paras 16-17, Simmons's at §4 para. 6, Archard's at §6.2 para. 2 and Scanlon's 'Profligate Pal' at §7 para. 3. Macleod, Dworkin, Scheffler and Sandel are treated the same way. Two lapses:
   - Under 'Where it bears', point 2, the card says that 'even the voluntarist's opponents grant promise and contract (§4, para. 2)'. The text says that 'the voluntarist will grant that special obligations are acquired through promises and contracts'. It says nothing there about the voluntarist's opponents.
   - The critical notes report that Dowie 'quotes Hardimon as saying that contractual role obligations are "acquired by signing on for the roles from which they derive" (p. 337)'. Dowie's sentence is: 'Hardimon explains that the standard view of roles is that they are either contractual or non-contractual, that contractual role obligations are "acquired by signing on ..."'. In Dowie's account, then, the words state the *standard view* as Hardimon explains it. R2's statement 7 makes the same slip.
5. **May say.** (1)-(5), (7) and (8) LICENSED. (6) LICENSED-NARROWER. At §4 para. 19 Jeske puts the sufficiency of the justice condition as a question ('Is this justice or morality condition, however, sufficient?'). She answers it with the case of a reading group whose members are made members by others' description. Suggested sentence: 'Jeske argues that Hardimon's test reduces to a condition of justice, and doubts, by the case of a reading group whose membership others impose, that the condition suffices (§4, paras 18-19).'
6. **May not say.** All seven are justified.

## dagger2021political

**PASS-WITH-NOTES**

1. **Identity.** The metadata give Dagger, Richard and Lefkowitz, David, 'Political Obligation', issued 2007-04-17 and modified 2021-03-15. The citation page gives the Summer 2021 Edition, minor correction, edited by Zalta. This matches the card and the citekey.
2. **Read depth.** The card claims the preamble and §§2, 4 and 5. The saved HTML holds them, and the card says §§1 and 3 were not read.
3. **Quotations.** 55 strings, all MATCH at the stated section and paragraph (§2.1; §2.2 para. 3; §2.3 para. 8, the last; §4 para. 1; §4.1 paras 1 and 4; §4.2 paras 1 and 4; §4.3 paras 1-11; §4.4 paras 1, 5 and 6; §5 paras 2-3). One word is quoted from the wrong place. A 'may not say' item argues that 'The entry reports a dispute that "remains" open'. 'Remains' comes from §5 para. 3, 'Whether a plurality of principles is necessary or even desirable ... remains one of many open questions', which concerns pluralism and not the associative dispute.
4. **Positions stated versus reported.** The card distinguishes them. Simmons, Wellman, Horton, Scheffler, Dworkin, Renzo and Hart are all marked 'as quoted' or 'citing', with their sections. The card also notes, correctly, that Dagger is himself among the critics cited at §4.3 para. 8.
5. **May say.** (1)-(4) and (6) LICENSED. (5) LICENSED-NARROWER. At §4.1 para. 1 the entry says the *critics* of consent theory 'typically believe that it can' be a source of obligations, and that their claim is that 'too few people' have given it. 'Widely accepted' and 'the dispute in political philosophy is over how many people have given it' go further than that. Suggested sentence: 'Even critics of consent theory typically accept consent as a source of obligation; their objection is that too few people have given the actual consent needed to ground a general obligation to obey the law (§4.1, para. 1).'
6. **May not say.** All five are justified. The 'remains' quotation should be replaced by §4.3 paras 9-11, where the three replies stand unanswered, or by the preamble ('none now commands widespread assent', which concerns political obligation generally).

## habib2022promises

**PASS-WITH-NOTES**

1. **Identity.** The metadata give Habib, Allen, issued 2008-10-10 and modified 2022-06-17. The citation page gives the Winter 2022 Edition, edited by Zalta and Nodelman. This matches the card.
2. **Read depth.** The sections claimed (introduction, §§2.3, 3, 4, 5.1, 6.2) are in the saved HTML.
3. **Quotations.** 41 strings, all MATCH at the stated section and paragraph. Principle F is at §3.1 para. 3 with '(Scanlon 1998: 304)'. The entry itself names it 'the Principle of Fidelity, or Principle F', so the card's 'Principle of Fidelity' is the entry's term.
4. **Positions stated versus reported.** The card marks the views of Scanlon, Thomson, Kolodny and Wallace, Mason, Leonard, Darwall, and Fuller and Perdue as reported by Habib, each with a section.
5. **May say.** (1)-(6) LICENSED. (7) LICENSED-NARROWER. The entry reports that Fuller and Perdue 'pointed out' that court damages are 'best understood as being proportional to the harm the plaintiff suffered in relying on the promise' (§6.2, para. 4). 'Courts measure some contract damages by the loss ...' turns a reported academic interpretation into a statement of law, and guard 3 bars any statement of law taken from a secondary description. Suggested sentence: 'Fuller and Perdue argued that the damages courts award for a broken promise are best understood as proportional to the plaintiff's reliance loss (as reported in Habib 2022: §6.2, para. 4).'
6. **May not say.** All six are justified.

## brandt2017transfer

**PASS-WITH-NOTES**

1. **Identity.** Crossref 10.1111/japp.12251 matches: Reuven Brandt, *Journal of Applied Philosophy* 34(5): 665-678, online 3 Nov 2016, print Nov 2017, licence CC BY 4.0 for the version of record. The citekey year is the print year. The Lancaster eprint page labels the file 'preprint.pdf - Accepted Version', and the PDF is headed 'Accepted: Journal of Applied Philosophy, 21/08/2016'. Unpaywall classes the same file as `submittedVersion`. The repository's label and the PDF's header support the card's 'accepted manuscript'.
2. **Read depth.** The whole manuscript (18 pp., notes 1-38) is saved, and the card claims it. The version of record is open (Unpaywall, `publishedVersion` at Wiley) but refused an automated fetch, as it did for R2 (HTTP 403).
3. **Quotations.** 61 strings, all MATCH at the stated manuscript pages. Two of them, on ms pp. 3-4 and 4-5, run across a page break with footnotes between. The negative claim holds: 'monitor', 'oversight', 'oversee' and 'check' do not occur, and 'supervision' occurs once, on ms p. 1. **One problem with the version.** The manuscript's wording differs from the publisher's. Crossref carries the publisher's abstract, which reads 'In this **article** I reject the claim ...' and 'in **defence** of'. The card's first quotation, from the manuscript, reads 'In this **paper** I reject ...', and the manuscript has 'in defense of'. Every Brandt quotation should therefore be checked against the version of record before it enters the paper. The card says this in general terms; the abstract shows the risk is real.
4. **May say / may not say.** All six 'may say' sentences are LICENSED. For sentence (4), the rejection is argued on the prank case (n. 34, ms p. 18), and the parental cases are treated as delegation (ms p. 5). All six 'may not say' items are justified.

## un2011guiding

**PASS**

1. **Identity.** The saved PDF is the OHCHR publication HR/PUB/11/04 (SHA-256 96b69f97…). The note on p. iv gives Human Rights Council resolution 17/4 of 16 June 2011 and the Special Representative's report. This matches the card. I re-fetched the PDF from ohchr.org on 11 Nov 2026 (HTTP 200, application/pdf), and it is byte-identical to the saved copy.
2. **Read depth.** The principles claimed are present. Printed page = PDF page minus 5, which I mapped page by page.
3. **Quotations.** 83 strings, all MATCH at the stated printed pages: iv, 1, 13-15, 17-28 and 31-35. The 'C-level' hits in the raw script output come from a control character (`\a`) that the text layer puts after each list letter, '(a)', '(b)' and so on. The negative claim holds: 'consumer', 'customer', 'guest', 'hotel', 'algorithm' and 'automated' do not occur, and 'clients' occurs once.
4. **May say / may not say.** All seven 'may say' sentences are LICENSED and all seven 'may not say' items are justified.

## hindriks2025moral

**PASS-WITH-NOTES**

1. **Identity.** Crossref 10.1007/s11229-025-04983-y matches: Frank A. Hindriks, *Synthese* 205(4), article 145, published 28 Mar 2025, CC BY 4.0.
2. **Read depth.** The saved PDF is the Springer version of record ('Synthese (2025) 205:145', 'Page n of 18'), and the card claims it.
3. **Quotations.** 74 strings. All 'Key facts' quotations MATCH at the stated pages. Two of them, on pp. 4-5 and 14-15, run across a page break with footnotes between. The slips the card reports are in the text: '(@)' in n. 27 and 'prone to do violate' on p. 14. One string is not a MATCH. The hold rationale puts 'ought implies put yourself in a position to' in quotation marks. Hindriks does not write this; his words are 'if an agent ought to do something, it ought to put itself in the position that it can do it' (p. 4). This is PARAPHRASED-AS-QUOTE. The negative claims hold for 'complaint', 'customer', 'client', 'stakeholder', 'victim' and 'feedback'. 'Channel' occurs only in 'the English Channel' (p. 4).
4. **May say / may not say.** All six 'may say' sentences are LICENSED. For sentence (4), the broken arm and the nurse are at p. 15, in context. All six 'may not say' items are justified.

## marchand2019barnhill

**PASS-WITH-NOTES**

1. **Identity.** The saved PDF (SHA-256 4c8c306c…) is the Delaware Supreme Court's slip opinion, No. 533, 2018, decided 18 June 2019 and corrected 19 June 2019, Strine CJ for the Court en banc. Slip op. p. n is PDF p. n+2. I re-fetched it from courts.delaware.gov on 11 Nov 2026 (HTTP 200), and it is byte-identical to the saved copy. The reporter citation is unverified: CourtListener asked for credentials, and I add none from memory.
2. **Read depth.** The whole opinion, slip pp. 1-37 with footnotes, is saved.
3. **Quotations.** 58 strings, all MATCH at the stated slip pages. Several run across a page break with footnotes between: pp. 2-3 (the Court of Chancery quotation, which also appears at p. 23), 8-9, 22-23 (repeated at 34 n. 110) and 30-31.
4. **One inference stated as fact.** The critical notes say that 'The consumers who died have no claim under *Caremark*'. R2's statement 31 says the duty 'is owed to the corporation'. The opinion shows that 'a stockholder brought a derivative suit' (slip op. at 1). It does not discuss consumers' standing, and it nowhere says to whom the duty is 'owed'. Both points may well be right in Delaware law, but they come from no text read in this run. They should be framed as an inference from the derivative form of the suit.
5. **May say.** (1), (2), (4), (5), (6) LICENSED. (3) LICENSED-NARROWER. The Court held that the complaint's particularized facts 'support a reasonable inference that the Blue Bell board failed to implement any system to monitor' food safety (slip op. at 4), and that the plaintiff 'has met his onerous pleading burden and is entitled to discovery' (slip op. at 37). 'If proved, would show a breach' goes past a ruling on demand futility. Suggested sentence: '... and the Court held that these allegations supported a reasonable inference that the board had not made the good-faith effort *Caremark* requires, so that the claim survived dismissal (slip op. at 4, 33, 37).'
6. **May not say.** All seven are justified as prohibitions. The third ('That the duty is owed to consumers, or that consumers can enforce it') is prudent, but the opinion is silent on the point rather than denying it.

## collins2019group (abstract only)

**PASS**

1. **Identity.** Crossref 10.1093/oso/9780198840275.001.0001 matches: 'Group Duties', subtitle 'Their Existence and Their Implications for Individuals', Stephanie Collins, Oxford University Press, print 4 July 2019 and online 22 Aug 2019, with the three ISBNs the card gives. Crossref types the record 'edited-book', as the card notes. Chapters .003.0001-.003.0007 return records with pp. 1-26, 27-59, 60-95, 96-125, 126-152, 153-180 and 181-206; .003.0008 returns none. Unpaywall lists a green `submittedVersion` at PhilPapers.
2. **Read depth.** Only the abstracts are claimed, and nothing beyond them is attributed.
3. **Quotations.** 30 strings, all MATCH against the re-fetched book and chapter abstracts. Hindriks cites 'Collins (2019b), *Group duties*' at p. 2 n. 4 and p. 4 n. 8, and lists it on p. 17, as the card says.
4. **May say / may not say.** All three 'may say' sentences are LICENSED, at abstract depth. All four 'may not say' items are justified.

---

## Second-hand notes, passage by passage

For each passage I opened the carrier text, found the quoted words by script, and checked the page the quoting author gives against that author's own pages. 'Agree' means that two different quoting authors print the same words. Carriers: Slattery 2002 (JoHLSTE 1(1): 19-28; PDF p. 3 is p. 21); Lynch et al. 2011 (author version, *Hospitality & Society* 1(1): 3-24, 'Please consult the final published version'); Petie et al. 2025 (peer-reviewed version; PDF p. 4 is MS p. 3); Blain and Lashley 2014 (pp. 2-3); Lugosi 2008 (PDF p. 3); Varley et al. 2018 (PDF p. 4); Hemmington 2007 (AV); Pijls et al. 2017 (p. 127); Kunwar 2017 (p. 59); O'Gorman 2007 (AM) and 2006 (pp. 51-52); Golubovskaya et al. 2017 (p. 1286); Westmoreland 2008; Shryock 2012 (p. S22); Kekstaite 2022 (MS pp. 3-4); Moysidou 2023 (MS p. 4); Bulley 2015 (AM p. 4 is PDF p. 5); Jeske 2019; Dowie 2024 (Europe PMC, unpaginated); the Simmons SSRN abstract (Crossref); Moreau ms (p. 6); Renzo and Green (SEP §5.3); Soofi 2026 (Europe PMC); Zaklaki 2019; Habib 2022; Jonker 2017 (PDF p. 20 is p. 10).

### Telfer

| # | Result |
|---|---|
| **T7, the commercial host** | **Both wordings confirmed.** Slattery (2002: 21) prints, as a block quotation keyed '(Lashley and Morrison (eds.), 2000:45)': "if a commercial host looks after his guests well out of genuine concern for their happiness and charges them reasonably, rather than extortionately, for what he does, his activities can be called hospitable." Lynch et al. (2011, author version PDF p. 8), keyed 'Telfer (2000: 45)', print: 'if a commercial host looks after his guests well out of **a** genuine concern for their happiness and charges them reasonably, rather than extortionately'. The one-word difference is the article 'a' before 'genuine concern'. Lynch et al. also stop at 'extortionately'. Both give p. 45, and the two quoting sources are independent. Which wording is Telfer's cannot be settled without her p. 45. Lynch's copy is an author version, and its published text was not seen. |
| T1 | Confirmed. Slattery 2002: 21 and Petie et al. 2025: MS p. 3 both give p. 39 and **agree word for word**. |
| T2, T4, T6 | Confirmed in Blain and Lashley 2014: 2, 3, 2, with Telfer pp. 39, 40, 42; 'ides' and 'a duty help' are as printed. One source each. Lynch et al. (PDF p. 8) quote 'an "appropriate" motive' from p. 42 and paraphrase the list. |
| T3 | Confirmed in Lugosi 2008, PDF p. 3, both phrases, Telfer p. 39. One source. |
| T5 | Confirmed in Varley et al. 2018, PDF p. 4, Telfer p. 40. One source. |
| T8, safety | Confirmed in Hemmington 2007: AV p. 15, no Telfer page. One source. Petie et al. paraphrase it at MS pp. 3 and 12, without quotation marks or a page. |
| T9 | Confirmed in Hemmington AV p. 9; Lynch et al. use the terms without quotation marks. |
| T10 | Confirmed in Pijls et al. 2017: 127. The script missed it because the two-column layout splits the phrase. One source. |
| T11 | Confirmed in Kunwar 2017: 59. One source. R1 marks it not for use, and I agree. |
| T12-T16 | Confirmed in O'Gorman 2007: AM pp. 6-7. T12 and T15 are also in O'Gorman 2006: 51, identical. That makes one author twice, not two sources. |
| Golubovskaya paraphrase | 'being a good host and being hospitable are different phenomena' is confirmed at p. 1286, as Golubovskaya et al.'s own words. |

### Derrida, *Of Hospitality* (trans. Bowlby)

| # | Result |
|---|---|
| D1 | Confirmed at Westmoreland p. 5 (n. 27, p. 15) and at O'Gorman 2007 AM p. 18, keyed '2000:21'. The wordings differ, and R1's 'not settled' stands. |
| D2 | Confirmed at O'Gorman AM p. 18 ('2000b:16'). One source. |
| D3a | Confirmed. O'Gorman AM p. 9 and Shryock p. S22 **agree word for word**, apart from 'Absolute' against '[A]bsolute'. Westmoreland (p. 6, n. 32) omits the parenthesis without an ellipsis, as R1 says. |
| D3b | Confirmed. O'Gorman AM p. 9 and Shryock p. S22 (with an ellipsis) **agree** where they overlap. |
| D3c | Confirmed at Westmoreland p. 3 (n. 15, p. 25). One source. |
| D4 | Confirmed at Shryock p. S22. One reference, '(Derrida 2000 [1997]: 25, 27)', covers D3a, D3b and D4 together. One source. |
| D5, D7, D12, D13 | Confirmed at Westmoreland pp. 2, 6, 6-7 and 4. D13 is cited jointly to *Adieu* 83 and *Of Hospitality* 147. One source each. |
| D6 | Confirmed at Blain and Lashley 2014: 3. One source. |
| D8, D10a | Confirmed at O'Gorman AM pp. 8-9 and 8, and at 2006: 51-52. One author. |
| D9 | Confirmed at Kekstaite MS p. 3 (pp. 69-70). One source. |
| D10b | Confirmed at Westmoreland p. 8 (n. 43, p. 77). With D10a, **two independent sources agree that p. 77 places rights and duties in the plural laws**, in different sentences. Kekstaite's paraphrase is at MS p. 4. |
| D11 | Confirmed at Moysidou MS p. 4 (p. 81). One source. |
| D14 | Confirmed at Bulley AM p. 4 (p. 149); 'pp. 77-91' and 'both entirely distinct and yet impossible to separate' are on the same page. One source. |
| D15 | Confirmed at O'Gorman AM p. 20 ('2000:132'). The key matches no single entry in his reference list. Not usable as *Of Hospitality*. |

### Hardimon (1994)

| # | Result |
|---|---|
| **H3, the definition, as quoted in the Stanford Encyclopedia** | **Confirmed exactly** at Jeske 2019, §4 para. 16: 'A role obligation, according to Hardimon, is "a moral requirement, which attaches to an institutional role, whose content is fixed by the function of the role, and whose normative force flows from the role" (334).' The page given is **334**. One source; R2 found no second. |
| H1, H2, H4 | Confirmed at Jeske §4 para. 16 (pp. 334, 334, 348). H2 is also in Dowie, 'Hardimon's view of roles as contractual', para. 1, with p. 334. Jeske and Dowie **agree** on the shared words; Jeske's '[constellation]' marks her change to the singular. |
| H5 (p. 337) | The words are confirmed in Dowie, para. 1. Dowie introduces them as Hardimon's account of **the standard view** ('Hardimon explains that the standard view of roles is ... that contractual role obligations are "acquired by signing on ..."'). |
| **H6 (p. 335) and H7 (p. 354): his own view or one he reports?** | The words are confirmed in Dowie, paras 2-3. **The open texts do not settle whose view these are, and three things point to reported views.** (i) Dowie presents H6 as what 'Hardimon stipulates, in agreement with John Rawls', and H7 as what 'Hardimon says'. (ii) Dowie's own framing one sentence earlier makes the 'signing on' language that of the standard view (H5). (iii) H6's two conditions, a just institution and voluntary acceptance of its benefits, have the shape of the principle of fair play that Dagger and Lefkowitz report from Hart and Rawls (§4.2, para. 1). And Simmons's own abstract says that Hardimon 'defends an account ... that he takes to be clearly superior to the "standard" voluntarist view' and that this view 'leaves out' of 'even contractual role obligations an "absolutely vital factor"'. So p. 335 probably states the voluntarist view Hardimon goes on to criticise. Whether p. 354 is his own account of contractual roles cannot be told. **Neither may be cited as Hardimon's own position** without his article. |
| H8 / S1 | Confirmed in the Simmons abstract (Crossref 10.2139/ssrn.1344466, re-fetched, posted 2009, author given as 'Alan Simmons'). No pages. |
| H9 | Confirmed at Moreau ms p. 6. This is an unpublished manuscript with no bibliographic record. |
| H10 | Confirmed as a term in Renzo and Green §5.3. |

### Goodin

| # | Result |
|---|---|
| 1985 *APSR* abstract | Confirmed by re-fetch (Crossref 10.2307/1956843, 79(3): 775-787): 'it is the beneficiary's vulnerability rather than any voluntary commitment as such on the part of the benefactor that generates these special responsibilities.' This is the author's abstract of the article, not the book. |
| G1, G2, G3 | Confirmed in Soofi 2026, Europe PMC text, with pp. 111, 111 and 114; G3 is in n. 10 with no page. One source each. 'A mere middleman' (Panitch and Horne 2016: 102) is confirmed there too. |
| G4 | Confirmed in Zaklaki 2019, with the ellipsis and no page. One source. G2 and G4 are different sentences, so neither confirms the other. |
| 2012 *Analysis* | 'a curable compulsion excuses failure only for as long as it would take to cure.' Confirmed at Hindriks p. 4. |

### Scanlon (1998, ch. 7)

| # | Result |
|---|---|
| Sc1, Principle F | Confirmed at Habib §3.1 para. 3, '(Scanlon 1998: 304)'. One source. Jonker's 'Roughly put' paraphrase is at his p. 11. |
| Sc2 | 'unfairly manipulate' is confirmed at Habib §3.1 para. 2, with no page. |
| Sc3 | Confirmed at Jonker p. 10 n. 15 (p. 316). One source. |
| Sc4 | Habib §3.3 para. 8 gives 'Profligate Pal (Scanlon 1998: 312)'; Jeske §7 para. 3 names it without a page. The two **agree** on the name and on what the case shows. |

### What may safely be cited 'as quoted in'

- **Telfer 2000: 45 (T7):** as quoted in Slattery 2002: 21, which has journal pagination and the full sentence, with a note that Lynch et al. 2011 print 'a genuine concern'.
- **Telfer 2000: 39 (T1):** as quoted in Slattery 2002: 21, with Petie et al. agreeing.
- **Telfer 1996: 82 and 101 (T12, T15):** as quoted in O'Gorman 2006: 51. This is the published version with a journal page; the 2007 article is an author manuscript.
- **Telfer 2000, safety (T8):** only as quoted in Hemmington 2007, with no Telfer page and no journal page.
- **Derrida p. 25, D3a and D3b:** as quoted in Shryock 2012: S22, with O'Gorman agreeing.
- **Derrida p. 77, rights and duties in the plural laws:** as quoted in Westmoreland 2008: 8 and in O'Gorman 2006: 51.
- **D4, 'not that it condemns':** only with its single carrier, Shryock S22, named, and with the compound page reference '25, 27'.
- **Hardimon's definition (H3):** as quoted in Jeske 2019, §4, p. 334.
- **Hardimon on roles (H2):** as quoted in Jeske and in Dowie.
- **Not citable as Hardimon's own view:** H5-H7.
- **Simmons:** only for the thesis of his abstract, marked as abstract depth.
- **Goodin:** the 1985 abstract as an abstract, and G1-G4 only as quoted by their single carriers.
- **Scanlon's Principle F:** as quoted in Habib 2022, §3.1, from a single carrier.

---

## The readers' seven central conclusions

**(a) Morrison and O'Gorman (2008) on businesses' responsibility: CONFIRMED, as to the text and its derivation.** The sentence is 'Businesses have a responsibility for the health, safety and security of the guests'. It is the fourth of six 'Business Principles' in **Figure 2**, captioned 'Taxonomy of hospitality principles derived from a hermeneutical analysis and evaluation of St Benedict's Rule' (AM p. 15). The version read is the Strathprints file, labelled 'Accepted Author Manuscript' by the repository and `submittedVersion` by Unpaywall; the version of record was not seen. The figure is derived from a reading of chapter 53 of the Rule 'and contemporaneous monastic practice', with commentaries and Wolter's medieval texts, 'translated into more modern business terminology' (AM p. 6). The principle is **asserted, not argued**: the body says only 'This taxonomy is presented in Fig. 2' (AM p. 7). Figure 1 (AM p. 14) has no verse on guests' safety.

**(b) Kant's right of hospitality: CONFIRMED.** Kant writes: 'It is not a right to be treated as a guest to which the stranger can lay claim—a special friendly compact on his behalf would be required to make him for a given time an actual inmate—but he has a right of visitation' (trans. Campbell Smith, pp. 137-138). The German at AA 8:358.05-08 reads 'Es ist kein Gastrecht ... sondern ein Besuchsrecht'. The right is 'to be treated by its owner without hostility', and 'The latter may send him away again, if this can be done without causing his death' (p. 137; AA 8:357.22-358.04). Its limit is 'a permission to make an attempt at intercourse with the original inhabitants' (p. 139; AA 8:358.23-25).

**(c) UN Guiding Principle 29: CONFIRMED, with the wording and scope made exact.** The Principle says: 'To make it possible for grievances to be addressed early and remediated directly, business enterprises should establish or participate in effective operational-level grievance mechanisms for individuals and communities who may be adversely impacted' (**p. 31**). The word 'channel' is the Commentary's, not the Principle's: 'a channel for those directly **impacted** by the enterprise's operations to raise concerns when they believe they are being or will be adversely impacted'. So is the second function, 'for adverse impacts to be remediated early and directly by the business enterprise, thereby preventing harms from compounding and grievances from escalating' (**p. 32**). The impacts are **adverse human-rights impacts**, although a grievance 'need not ... amount to an alleged human rights abuse' before it can be raised (p. 32). The enterprises are 'all business enterprises, both transnational and others, regardless of their size, sector, location, ownership and structure' (p. 1). The Principles create no 'new international law obligations' (p. 1), and the responsibility is 'distinct from issues of legal liability' (p. 14).

**(d) Hindriks's duty of control: CONFIRMED.** His statement of it: 'collective agents have "a duty of control" to prevent or close control gaps' (p. 2). And: 'The duty of control, I propose, is the obligation to secure a proper level of moral control. It requires agents to prevent or close control gaps' (p. 4). His argument has three steps. Control gaps raise the risk to others; agents with gaps are prone to violate their obligations; and 'agents should be in a position to fulfill their moral obligations and maintain the risks they pose to others at a morally acceptable level' (p. 4). The third step rests on 'if an agent ought to do something, it ought to put itself in the position that it can do it', supported by Goodin (2012: 18) (p. 4). The duty is 'a second-order obligation' requiring 'the prerequisites for fulfilling first-order obligations' (pp. 4-5). Two limits: he does not say to whom the duty is owed, and the collective learns of its gaps from its own structure and its members' excuses (pp. 13-15).

**(e) Brandt on delegation: CONFIRMED.** A delegator keeps a duty to step in: Peter 'has an obligation to either complete the page layout himself or find someone else to do it' (ms p. 3). In general, the one who delegates 'still has the obligation to ensure that the responsibility gets fulfilled' (ms p. 3), 'even in the absence of blame' (ms p. 4). Parents must act 'If it becomes clear that a doctor or a teacher is failing' (ms p. 5). Brandt states **no duty to monitor**. The words 'monitor', 'oversight', 'oversee' and 'check' do not occur, and 'a mechanism for finding out' appears only as something policy might offer gamete providers who 'so wish' (ms p. 15). One nuance: a delegator 'might be to blame' for choosing a delegate with 'good reason to distrust' (ms p. 3). That is a duty of care in choosing, not a duty to watch. All of this is from the accepted manuscript; see the version note on the card.

**(f) *Marchand v. Barnhill*: NARROWED.** The standard is an **effort**, not a system that in fact informs. The Court says: 'to satisfy their duty of loyalty, directors must make a good faith effort to implement an oversight system and then monitor it' (slip op. at 30). It adds: 'the board must make a good faith effort—i.e., try—to put in place a reasonable board-level system of monitoring and reporting' (slip op. at 30-31). It quotes *Caremark*'s requirement that the system be 'adequate to assure the board that appropriate information will come to its attention in a timely manner' (slip op. at 29 n. 100), and adds that 'we are not examining the effectiveness of a board-level compliance and reporting system after the fact' (slip op. at 31). **Who can sue:** here, 'a stockholder brought a derivative suit' (slip op. at 1). The opinion says nothing about consumers' standing, so R2's 'the consumers harmed have no claim under it' is an inference.

**(g) The Stanford Encyclopedia on whether roles bind by themselves: CONFIRMED.** Dagger and Lefkowitz report both views. On the external-principle side, critics hold that the duty 'to perform the (conventional) duties that constitute the role ... ultimately depends either on an agent's exercise of will ... or a natural duty', and that justification 'bottoms out not in the fact of association but in a moral principle external to it' (§4.3, para. 8). On the other side, associative obligations attach 'merely in virtue of their occupying a role', and 'it makes no difference' whether the role was entered voluntarily (§4.3, paras 1-2). Horton holds that constitutive obligations 'do not stand in need of moral justification in terms of a set of basic moral principles', and Dworkin that association 'is in itself pregnant of obligation' (§4.3, para. 4). The replies at §4.3 paras 9-11 stand unanswered. Jeske reports Hardimon's 'whose normative force flows from the role' (§4, para. 16) and argues against it in her own voice (§4, paras 10, 18-19). Hardimon's view as Jeske reports it also carries a condition of reflective acceptability (§4, paras 16-17), so the cleanest statement of 'binds by itself' is Horton's at Dagger §4.3 para. 4.

---

## Table: every FAIL, every quotation that is not MATCH, every 'may say' sentence that is not LICENSED

There are no FAILs.

| Card | Where on the card | Item | Finding | Correction |
|---|---|---|---|---|
| ogorman2007phenomenon | Critical notes ('Person, role or organization') | "its own different sets of laws" | PARAPHRASED-AS-QUOTE | The text reads 'each with their own different sets of laws' (AM p. 22) |
| hindriks2025moral | hold_rationale | 'ought implies put yourself in a position to' | PARAPHRASED-AS-QUOTE | Hindriks: 'if an agent ought to do something, it ought to put itself in the position that it can do it' (p. 4) |
| dogru2025service | Where it bears (K2) | 'hospitality at the organizational level' | PARAPHRASED-AS-QUOTE | The abstract: 'practiced at the organizational level'; 'organization-level hospitality virtue' |
| dagger2021political | May not say (1) | 'remains' (open) | Quoted from the wrong part of the entry | §5 para. 3, about pluralism; cite §4.3 paras 9-11 or the preamble instead |
| jeske2019special | Critical notes; also WS_P2_R2 statement 7 | "acquired by signing on for the roles from which they derive" | Words MATCH (Dowie); wrong speaker | Dowie gives them as the standard view as Hardimon explains it |
| brandt2017transfer | Key facts (all) | Manuscript quotations | MATCH against the manuscript; the version of record differs | VoR abstract: 'In this article', 'defence'; check every quotation against the VoR |
| kant1795perpetual | venue; R1 BibTeX | 'George Allen & Unwin ... first edition 1903' | Identity mismatch | 1903 = Swan Sonnenschein; Allen & Unwin = 1917 third impression |
| morrison2008hospitality | May say (2) | 'derive their principles from St Benedict's Rule' | LICENSED-NARROWER | 'from the Rule and contemporaneous monastic practice', with commentaries (AM p. 6) |
| hemmington2007 | May say (3) | security 'should' centre on the guest 'and not on the firm's goods' | LICENSED-NARROWER | 'should ... focus on guest security', seen as dominant over the hotel's resources and procedures; financial security not to be ignored (AV pp. 15-16) |
| benveniste1973indoeuropean | May say (4) | 'is not the "master" of his guest' | LICENSED-NARROWER | A claim about the original sense of *-pot-* in *hospes* and *atithi-pati* (para. 34) |
| jeske2019special | May say (6) | 'the condition is not sufficient' | LICENSED-NARROWER | Jeske asks whether it suffices and doubts it, by the reading-group case (§4, para. 19) |
| dagger2021political | May say (5) | 'Consent is widely accepted ...; the dispute ... is over how many' | LICENSED-NARROWER | 'Even critics of consent theory typically accept consent as a source ...; too few have given it' (§4.1, para. 1) |
| habib2022promises | May say (7) | 'Courts measure some contract damages by the loss ...' | LICENSED-NARROWER | 'Fuller and Perdue argued ... (as reported in Habib §6.2, para. 4)'; no statement of law from this source |
| marchand2019barnhill | May say (3) | 'these allegations, if proved, would show a breach' | LICENSED-NARROWER | 'supported a reasonable inference that the board had not made the good-faith effort *Caremark* requires; the claim survived dismissal' (slip op. at 4, 33, 37) |
| marchand2019barnhill | Critical notes; WS_P2_R2 statement 31 | 'consumers ... have no claim'; duty 'owed to the corporation' | Inference stated as fact | The opinion records a stockholder derivative suit (slip op. at 1) and is silent on consumers |

Verification written by a Claude (Opus 5.5) subagent, verifier CV-E, from the saved sources and records re-fetched on 11 Nov 2026, run rr-2026-11-k. No card or other file was edited, and nothing was committed.

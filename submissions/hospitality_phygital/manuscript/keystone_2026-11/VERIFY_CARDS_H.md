<!-- Independent verification of cards, batch CV-H, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-H (run rr-2026-11-k)

**Scope.** Eleven items. From reader R9: the new cards `kekstaite2022beyond` and `ogorman2007discovering`, and the sections headed 'rr-2026-11-k: bearing on the keystone (R9)' in `lynch2011theorizing`, `bulley2015ethics`, `petie2025exploring`, `germannmolz2018scale` and `moysidou2023theorizing`. From reader R11: the new cards `kiesewetter2015instrumental`, `baum2026anticipatory` and `pettit2007responsibility`, and the 'rr-2026-11-k addendum (R11)' in `herstein2023legal`. I wrote none of them. I edited no card and no other file.

**Method.** I re-fetched every record that was openly reachable and compared each saved file with a fresh download where one could be had. I extracted every double-quoted string from each card or section (290 segments, split at ellipses and bracketed insertions) and searched the saved text with a script of my own, allowing only whitespace, line-end hyphenation, quotation-mark and ligature differences; I then mapped each hit to the card's page system and compared it with the locator. Three texts needed more than a script. For O'Gorman (2007) the text layer drops ligature glyphs and interleaves columns, so I read all nine page images. For Kiesewetter the text layer renders φ, ψ and parentheses as 'J', 'w' and 'ð Þ', so I substituted them back. For Herstein I parsed the HTML into paragraphs from its `<p>` and `<blockquote>` tags. I rendered page images for Lynch et al. PDF p. 9 and for O'Gorman pp. 44-52. Scripts and extracts are in the session scratchpad, not the project.

**Records re-fetched on 11 Nov 2026.**
- Crossref `works/{doi}` for all nine DOIs (Lynch, Bulley, Petie, Germann Molz, Moysidou, Kekstaite, Kiesewetter, Pettit, Baum): every author, title, volume, issue and page range matches its card. Crossref bibliographic query for O'Gorman 2007: no match.
- Ghent biblio file 8751332.pdf (Kekstaite): HTTP 200, byte-identical to the corpus copy (SHA-256 916c9e74…a126c1d). Ghent record page read for its version label.
- Strathprints 5846 (O'Gorman): HTTP 200; the record's fields match the saved record.
- arXiv abs/2609.24242 and pdf/2609.24242v1 (Baum et al.): HTTP 200; only [v1] listed, no journal reference; PDF byte-identical to the saved copy (SHA-256 6c779bca…1745f).
- Internet Archive captures of 2 Jan 2025 (Pettit, Princeton page) and 18 Mar 2025 (Kiesewetter, PhilArchive KIEINI): both exist and both re-downloads are byte-identical to the saved PDFs.
- plato.stanford.edu/entries/legal-rights/ (Herstein): HTTP 200, byte-identical to the saved HTML.
- Unpaywall (`email=research@example.org`): Pettit closed; Kiesewetter bronze at the publisher; Lynch et al. green, submitted version only.
- The corpus PDF for Bulley is byte-identical to `sources/bulley2015ethics/oa0.pdf`.

**Verdicts.** PASS 2 (`bulley2015ethics`, `germannmolz2018scale`); PASS-WITH-NOTES 9; FAIL 0.

**Quotation tally.** 290 quoted segments. Two are dossier phrases quoted on the Kiesewetter card ("must keep a channel from the guest", "part of the duty it already has"), not source text. Of the 288 source quotations, all are MATCH with a correct locator. Six sit, correctly attributed, in another text: two Westmoreland sentences on the Kekstaite card (`westmoreland2008interruptions`, p. 8), one O'Gorman 2005 clause on the 2007 card (`ogorman2005modern`, p. 146), Crossref's title on the Petie section, and the red team's paraphrase on the Herstein addendum (REDTEAM_PHIL, S1). Fourteen needed a manual step: page images for O'Gorman, symbol mapping for eight Kiesewetter strings, three Baum strings broken by line-end hyphenation or a page break, one Moysidou string with a missing space in the source ("2009).Yet"), and the Kekstaite p. 77 paraphrase that crosses AM pp. 3-4. No quotation is LOCATOR-WRONG, NOT-FOUND, PARAPHRASED-AS-QUOTE or OCR-DOUBT.

**The hard checks, in brief.**
- *Herstein.* The preamble files §§1-2 and 6-10 under features "unique or particularly salient to legal rights"; that places §§1 and 8 under legal rights without denying them to moral rights. The dependence sentence does run against its *Griswold* example, as R11 says.
- *Kiesewetter.* The article transmits 'ought' to necessary means only (pp. 922, 925; n. 2 reports Way's concession); p. 937 concerns an agent's own likely failure; pp. 945-946 argue through incompatible alternatives. All confirmed.
- *Baum et al.* The arXiv v1 page numbers are right, and the quotations at pp. 11, 20, 22-23 and 25 match.
- *Pettit.* The p. 195 sentence matches; his unincorporated collection is a collection of individuals (pp. 194-195).
- *Lynch et al.* The sentence 'enable contestation and conflict' carries no citation. It does not close its paragraph, as R9 says; Friese's "also" follows it at once.
- *Bulley.* 'Merely laws' is Bulley's own sentence, referenced to Derrida 2003: 129, which is the Borradori dialogue.
- *Moysidou and Stanley.* The complaint to Workaway is Pauline's (p. 10); the authors' gloss on p. 14 credits Alice. R9 is right.
- *Petie et al.* Both passages match at MS p. 12 and MS p. 11.
- *O'Gorman 2007.* The page images confirm that the article names no innkeeper's duty.
- *Kekstaite.* The forename is Julija; the Ghent record calls the file the accepted manuscript.

---

## 1. kekstaite2022beyond (R9, new card)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref matches the card: Julija Kekstaite, H&S 12(2), pp. 185-203, issued 1 June 2022, doi 10.1386/hosp_00049_1, title with 'illegalized'. The saved file gives no forename (header 'Kekstaite, 2022§') and spells 'illegalised'; the Ghent record page gives 'Julija'. On version, the Ghent record lists this file as "Final version before copy editing.pdf full text (Accepted manuscript) | open access" and the published version as "UGent only". Unpaywall's 'submittedVersion' is therefore the outlier. The card reports only the conflict between Unpaywall and the corpus log, and should add the repository's own label. A version of record exists and was not seen, as the card says.
   - *Stale note.* The critical note "Bibliography error" is out of date: `references.bib` line 1090 now reads 'Kekstaite, Julija' with the rr-2026-11-k note. The same holds for note 3 in `WS_P1_R9.md`.
2. **Read depth.** The saved file holds the abstract, sections 1-7 (with 2.1 and 2.2) and the reference list on 16 pages, and the re-download is byte-identical. Honest.
3. **Quotations.** 32 segments, all MATCH: 30 in Kekstaite at the stated AM pages, and two Westmoreland strings in `westmoreland2008interruptions`, p. 8 (his n. 43 gives *Of Hospitality*, 77). The p. 77 paraphrase runs across AM pp. 3-4, as stated. Speaker attributions check out: John (AM p. 9), Daniel (AM p. 10, block quotation) and George (AM p. 12).
   - *Derrida as Kekstaite quotes him.* She quotes *Of Hospitality*, by her citations, at pp. 69-70 ("cosmopolitan right to universal hospitality") and pp. 16-17 ("we don't know what hospitality is because we do not know what 'welcome' means, perhaps no one welcomed is ever completely welcome"). By 'ibid.' she attributes "ethics itself" to the same book (AM p. 3). She paraphrases p. 77 without quotation marks (AM pp. 3-4), uses "the pact of hospitality ... (ibid.: 25)" unquoted (AM p. 4), and takes "giving something determinate" from "Derrida 2003: 129, as quoted in Bulley 2017" (AM p. 4). She quotes nothing from pp. 25-27, 53-59 or 75-83.
4. **Design.** 17 semi-structured interviews with 18 respondents affiliated with the Citizens' Platform, 1 March to 8 April 2020; 6 men and 12 women (AM p. 6); hosts only (AM p. 7). The respondents "mostly lived in Brussels and its surroundings, although some were from other Belgian cities" (AM p. 6), so the Summary's "eighteen Brussels residents" should read "18 respondents, mostly living in Brussels and its surroundings".
5. **May say / may not say.** May say 1-3: LICENSED. May not say 1-3: LICENSED. On may-not 1, she does quote the book elsewhere (pp. 16-17, 69-70), but not p. 77 or p. 25.
6. **Bearing on K7 and K9.** Agree. Kekstaite's own gloss of Rosello spreads responsibility to both parties: "both hosts and guests bear a shared responsibility to mitigate structural injustices" (AM p. 6). The guest's agency in the article is negotiation, not a route the host keeps. There is no K9 bearing.
7. **Reader's inferences.** The card marks none. The inference in R9's report §1(c), that no text frames the guest's voice as consumer complaint, is supported for this article.

## 2. ogorman2007discovering (R9, new card)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** The live Strathprints 5846 record matches the card: O'Gorman, Kevin D., 'Discovering commercial hospitality in ancient Rome', *Hospitality Review* 9(2), pp. 44-52, 2007, ISSN 1464-9101, refereed. The running foot runs from "the hospitality review 44 april 2007" to 52. My Crossref bibliographic query returned no match, and the article carries no DOI.
2. **Read depth.** Nine PDF pages, journal pp. 44-52, in typeset layout. The standfirst, all sections, Table 1, Figures 1-4 and notes 1-46 are present, and the card's account of what was read is honest. The text layer is unreliable, so the card's reading from page images was necessary.
3. **Quotations.** 33 segments, all MATCH. I read each on the page images; 32 are in this article, and one ("bedbugs, discomfort, violence and danger") is `ogorman2005modern`, p. 146, as the card says. Locators are correct.
   - The duties-of-protection sentence (p. 45) carries no note; note 4 belongs to the Livy block quotation before it.
   - Note 22 is Balsdon (1969) and note 29 is Codex Iustinianus IIII:lvi:3.
   - One precision: "(p. 44; repeated p. 47)" is loose. Page 47 repeats the sentence without "Extensive".
   - *Derrida.* The article does not cite him.
4. **Design, and the silence.** The article is a descriptive history drawn from literary sources, the 1950s typology and Pompeian archaeology. I read every page image. It mentions no innkeeper's duty or liability to a guest, and no edict, *receptum*, Ulpian, Digest, complaint or redress. Law appears four times:
   - p. 44: "The Roman citizen could travel throughout the Empire and be protected by one legal system", a general statement about citizens travelling, not about inns;
   - p. 45: the *ius hospitia* of private hospitality;
   - p. 48: Justinian on a sold slave girl, and Theodosius protecting serving girls;
   - p. 50: the claim that female bar workers were prostitutes, "supported in a few places in contemporaneous Roman law".

   The card's "'protect' and 'safety' in a commercial setting occur only for serving girls" holds. It should still name the p. 44 sentence, so that no reader takes it for a traveller's protection at inns. The critical note on the 2005 article is confirmed: there p. 145 gives the guest-friendship duties "According to Schmitz (1875)", and p. 146 gives the 'lower classes' sentence to DeFelice (2001), with the bedbugs clause.
5. **May say / may not say.** May say 1-3: LICENSED. "Complex and sophisticated" is the standfirst's summary of his argument ("argues Kevin O'Gorman"). May not say 1-3: LICENSED.
6. **Bearing.** Agree: the article is a rival by silence for a commercial host's duty in K1, and has no K7 or K9 bearing.
7. **Reader's inferences.** None is marked. The statement that the article fits only the first half of the counter-history is supported (p. 47).

## 3. lynch2011theorizing (R9 section only)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref matches: Lynch, Germann Molz, McIntosh, Lugosi and Lashley, 'Theorizing hospitality', H&S 1(1), pp. 3-24, 2011. The saved copy is a pre-publication version, not the accepted manuscript:
   - its first page reads "Please consult the final published version if citing";
   - its PDF title is "DRAFT 2";
   - Unpaywall lists the Bournemouth file as a submitted version.

   The free Intellect link on the first page now redirects to the publisher's home page, and I found no open version of record. R9 calls the file a "repository copy" and advises citing without pinpoint. That is adequate for locators, but the wording of the 'contestation' sentence itself is unchecked against the version of record.
2. **Read depth.** 22 pages, body and references. Honest.
3. **Quotations.** 21 segments, all MATCH, at PDF pp. 2, 3, 4, 5, 8, 8-9, 9 and 13 as stated.
   - **Error.** The section says the 'contestation' sentence "closes a paragraph that begins on PDF p. 8 and ends on PDF p. 9" (repeated in `WS_P1_R9.md` §1(c)). It does not. On PDF p. 9 the same paragraph goes on with no break: "... enable contestation and conflict to occur. Friese (2004) also argues for the opening up of spaces of hospitality ...", then Grit (2010) and Valentine (2008), ending on "manifestations of power that occur" (checked on the page image).
   - *Attribution.* The sentence carries no citation, as R9 says. But the "also" in the next sentence ties Friese's argument back to Dikeç's "opening those boundaries", so the 'Indeed' sentence sits inside a run of reported views. It may be the editors' gloss on Dikeç or their own step; the text does not decide. R9's rule, to attribute it only to Lynch et al. until Dikeç is read, is right.
   - *Derrida.* The editorial quotes no sentence of *Of Hospitality*. It cites Derrida by year only (PDF pp. 2, 4-6, 10, 12) and reports Ben Jelloun's reading (PDF p. 8).
4. **Design.** An editorial; there is no design to check. "Hospitality as social control" is a section heading on PDF p. 3, one of the two themes the editors name.
5. **May say / may not say.** The section has no list. Its 'Bearing' bullet is LICENSED with the attribution caveat it already states.
6. **Bearing.** Agree. The editorial reports power after the threshold, for example Robinson and Lynch's "the highly regulated experience may cause a loss of free will" (PDF p. 8), and assigns no duty among micro-hosts and macro-hosts.
7. **Reader's inferences.** "It may be their own extension" is open. Reading Dikeç (2002) would settle it (Crossref re-fetched: *Theory, Culture & Society* 19(1-2): 227-247; HAL hal-01274367), together with the version of record's wording.

## 4. bulley2015ethics (R9 section only)

**Verdict: PASS**

1. **Identity.** Crossref matches: Dan Bulley, 'Ethics, power and space: International hospitality beyond Derrida', H&S 5(2) (the DOI says 2-3), pp. 185-201, 2015. The saved author manuscript, from Queen's University Belfast, is byte-identical to `sources/bulley2015ethics/oa0.pdf`.
2. **Read depth.** 25 PDF pages; the footers confirm AM p. = PDF p. − 1. Honest.
3. **Quotations.** 18 segments, all MATCH at the stated AM and PDF pages: AM pp. 2, 4, 5, 10, 13, 14, 15, 16 and 18.
   - *'Merely laws'.* The sentence is Bulley's own and ends "(Derrida 2003: 129)" (AM p. 4 [PDF p. 5]). His reference list gives Derrida 2003 as 'Autoimmunity: Real and Symbolic Suicides – A Dialogue with Jacques Derrida', in G. Borradori, *Philosophy in a Time of Terror*, pp. 85-136. R9 is right that it is not *Of Hospitality*. The clause "will always be contraventions, annulments of the Law" is Bulley's too, two sentences after "(Derrida and Dufourmantelle 2000: 77-91)".
   - *Derrida from* Of Hospitality. Bulley quotes one sentence, "answering for a dwelling place, for one's identity, one's space, one's limits" (Derrida and Dufourmantelle 2000: 149; AM p. 4). Elsewhere he cites pp. 41, 47-9, 47-79, 77-91 and 149 without quotation. The block quotation on AM p. 9 comes from 'Hostipitality' (Derrida 2000: 14). R9 has all of this right.
4. **Design.** Theory, with a camp case built from secondary sources. The 'compounds' sentence cites Hyndman "(2000: 115)", the rations Agier (2011: 152-3), and the fences Hyndman (2000: 128).
5. **May say / may not say.** The section has no list. Its last bullet is LICENSED.
6. **Bearing.** Agree.
7. **Reader's inferences.** "The nearest statement ... to the keystone's problem" is a judgement, supported within the seven texts R9 read.

## 5. petie2025exploring (R9 section only)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref matches: Petie, Phillimore and Allsopp, '... in hotel accommodation for asylum seekers in the United Kingdom', H&S 15(1), pp. 23-44, 1 March 2025. The cover sheet ("... in accommodation for asylum seekers in the UK", PDF p. 1) and the manuscript's title page ("... in hotel accommodation for asylum seekers in the UK", PDF p. 2) read as R9 says.
2. **Read depth.** An accepted manuscript of 25 PDF pages; MS p. = PDF p. − 1. Honest.
3. **Quotations.** 27 segments, all MATCH at the stated MS pages, with Crossref's title matched in the Crossref record. Both hard-check passages match: "dealt with appropriately" at MS p. 12 and "lacked the knowledge needed to act" at MS p. 11. "Requires knowledge and skills ..." runs across MS pp. 4-5, and the 'Hostipitality' quotation across MS pp. 10-11, as stated.
   - *Narrower.* "Telfer is paraphrased, not quoted, three times (MS pp. 3, 12, 13)" holds for the claim about responsibility for the guest's welfare. The article does quote Telfer once, for its definition: "'the giving of food, drink and sometimes accommodation to people who are not regular members of a household' (Telfer 2000: 39)" (MS p. 3). It also cites Telfer for food as "a core aspect of hospitality" (MS p. 11).
   - *Derrida.* The article quotes only 'Hostipitality' (cited as Derrida 2010: 14; the reference list gives *Angelaki* 5(3): 3-18), at MS pp. 10-11, and paraphrases it at MS p. 4. It quotes nothing from *Of Hospitality*.
4. **Design.** A conceptual framework applied to two case studies, Glasgow (Park Inn) and Knowsley, built from inquiry, evaluation, NGO and news reports (Methodology, MS p. 8). The article reports no statistics.
   - *The contrary passage, read in full.* The Government evaluation found that "the queries lodged by Badreddin at the Park Inn were dealt with appropriately" (MS p. 12, citing Laing 2020). Just before that, on the same page, the article reports from news accounts that the two men's mental health declined and "no actions were taken to help them". MS p. 11 adds that staff told the night before "lacked the knowledge needed to act". R9's "The single queries were handled" states the evaluation's finding as fact. It should be attributed to the evaluation and set beside the news reports.
5. **May say / may not say.** The section has no list. In the 'Bearing' bullet, "the queries that reached the hotel were handled (MS p. 12)" is LICENSED-NARROWER (see the table). The rest of the bullet is LICENSED.
6. **Bearing.** Agree, with that narrowing. I add a passage that belongs beside it: "All parties tried to support asylum seekers but did so without a uniting framework and without any form of safety needs assessment" (MS p. 12).
7. **Reader's inferences.** That a channel derived from the duty to perform what the host undertook does not reach placed guests is supported as to the payer: "it is the Home Office who are paying customers" (MS p. 4). It is open as to what grounds the operator's duty. The article speaks of "hosts' responsibility to protect asylum seekers and their contractual obligations" (MS p. 12) without saying to whom the contract runs.

## 6. germannmolz2018scale (R9 section only)

**Verdict: PASS**

1. **Identity.** Crossref matches: Germann Molz, H&S 8(3), pp. 229-251, 2018. The card's title differs only in capitalisation.
2. **Read depth.** The version of record, 24 PDF pages; journal p. = PDF p. + 228. Honest.
3. **Quotations.** 20 segments, all MATCH at pp. 231, 233, 236, 237, 243, 244 and 245.
   - The Dredge passage is Germann Molz's bulleted summary of Dredge (2017), with an inner quotation of Dredge (2017: 43-44), so R9's "Dredge, as reported" is right.
   - Chesky's remark is "cited in Botsman and Rogers 2010: xiii".
   - The Veijola and Jokinen quotation carries "(original emphasis)", which R9 notes.
   - *Derrida.* The article does not cite him.
4. **Design.** Critical discourse analysis with illustrative examples (p. 235), as R9 says. The negative claim holds: the only complaints in the article are local residents' complaints about Airbnb, and I found no grievance, refund, cancellation or redress route for a guest.
5. **May say / may not say.** The section has no list. Its 'Bearing' bullet is LICENSED.
6. **Bearing.** Agree (S6).
7. **Reader's inferences.** "The platform's route is not a route to correction" is supported (pp. 236-237, 244).

## 7. moysidou2023theorizing (R9 section only)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref matches: Moysidou and Stanley, H&S 13(3), pp. 241-263, 2023. The saved copy is the accepted manuscript from Edinburgh Napier.
2. **Read depth.** 21 pages; manuscript page = PDF page. Honest.
3. **Quotations.** 15 segments, all MATCH. The pp. 4-5 quotation matches apart from a missing space in the source.
   - *Alice or Pauline.* Pauline made the complaint. The excerpt "I wrote this back to him and I also complained to Workaway" is signed "(Pauline from Scotland, Serbia, 2017, Study One)" (p. 10). Alice's only excerpt (p. 8) describes her host mother's racism; its "she also complained about racism" refers to the host mother. On p. 14 the authors credit "complaining to the homestay-organising agency (Alice)". The gloss misattributes, as R9 says.
   - *Derrida.* The article quotes *Of Hospitality* once, p. 81 (on its own p. 4). It cites Derrida 1999 (p. 5) and 2000 (p. 12) without quotation.
4. **Design.** 50 semi-structured interviews (26 hosts, 24 guests), reached through au pair agencies, WWOOF organisations and snowball sampling (pp. 5-6). R9 relies on excerpts and on the authors' glosses, not on any statistic.
5. **May say / may not say.** The section has no list. The 'Bearing' sentence on S6 is LICENSED-NARROWER. The one complaint to an intermediary in the data came from an applicant the host refused before arrival: "potential guests are rejected before they even set foot in the homestay ... the host rejects Pauline and her partner outright" (p. 10). It shows a route at admission, the pre-reception case K9 names, not a route during a stay. The 'Emergency Help Plan' (p. 16) is the organisation's offer, not something a guest in the data used.
6. **Bearing.** Agree otherwise. The p. 12 sentence belongs to the authors' quadrant of guests' "intangible affordances". Its second clause ("feeling that the complaint will be acted upon") presupposes someone who acts on the complaint, which is a thin hook for K7.
7. **Reader's inferences.** The inference that the data support routing the household guest's complaint to the platform or agency is supported only for refusal at admission. A complaint during a stay to an intermediary, by any guest in the article, would settle it; I found none.

## 8. kiesewetter2015instrumental (R11, new card)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref matches: *Ethics* 125(4), pp. 921-946, July 2015. Both saved PDFs have SHA-256 cc645578…c1e389f, and my re-download of the PhilArchive capture is identical. The publisher's download stamp is present. Unpaywall (re-queried) lists the article as bronze at the publisher, so the text is open and K-D12 applies without difficulty.
2. **Read depth.** 26 pages, pp. 921-946, with notes 1-52. Honest.
3. **Quotations.** 24 source quotations, all MATCH at pp. 922 (the principle and n. 2), 923, 924 (n. 7), 925, 932, 934, 937, 938, 940, 943-944, 945-946 and 946. Eight needed the symbol mapping. The two remaining strings are the dossier's phrases.
   - *Note 2, read whole.* The note speaks of Way: "Way's argument is officially based on a more liberal transmission principle which is not restricted to necessary means, but he mentions himself that his principle is open to objections that do not apply to a transmission principle restricted to necessary means, and that his argument could also be framed in terms of such a more restricted principle (see Way, 'Transmission,' 496 n. 14)." The key-fact bullet attributes it correctly. May-say 2 does not.
4. **The argument, checked where the card relies on it.**
   - p. 922: 'ought' "transmits to necessary means". Page 925: the principle "states only that 'ought' transmits to necessary means".
   - p. 937: the passage answers Jackson and Pargetter's objection to the wide-scope account. Kiesewetter says the agent's own likely failure "could still make a difference to the normative situation, for example, by providing second-order reasons to adopt additional measures that ensure his conformity". He then says the likelihood does not mean "that ... you stand under obligations different from those of people who are unlikely to drink", and "it is not necessary to assume that it also makes a difference to what obligations you are under with respect to accepting and writing itself". He does not say that such measures can never be obligatory, and the case is the agent's own expected failure, not a failure by others.
   - pp. 945-946: reason transmission works through incompatible alternatives; the sentence "If buying is a necessary means ..." begins at the foot of p. 945.
5. **May say / may not say.**
   - May say 1: LICENSED.
   - May say 2: LICENSED-NARROWER. The concession is Way's, reported by Kiesewetter.
   - May say 3: LICENSED-NARROWER. Confine it to the agent's own likely failure, and to "could" (see the table). The same narrowing applies to `WS_P3_R11.md` §1(b), first bullet set.
   - May not say 1-3: LICENSED.
6. **Bearing.** Agree: the article narrows P3 to C to necessary means and gives nothing on directedness. My passage is p. 925's "states only".
7. **Reader's inferences.**
   - *Disjunctive means.* Supported in principle. Kiesewetter defines a means as "a type of action ψ that helps to bring about" an end (p. 924), and his argument applies to any incompatible alternative (p. 945). It is open whether a disjunctive act type counts as "a type of action" for him; he leaves "the kind of necessity" unspecified (p. 924, n. 7). Way (2012: 496, n. 14), the reply by White (2017) or Kiesewetter's later work would settle it; none was read.
   - *Low-probability channel.* Open. The Unlucky verdict weighs a definite $20 cost against a .1 chance of saving $100 (p. 943). It is a weighing, not a rule that low-probability means are never required.

## 9. baum2026anticipatory (R11, new card)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref (10.2139/ssrn.7497218) gives posted content on SSRN, deposited 22 Sep 2026, with the title and four authors as on the card. The arXiv abstract page gives the same, submitted 21 Sep 2026; only v1 exists and there is no journal reference. Note 9 is redacted for review. No version of record exists, and the SSRN version was not seen; the card says both.
2. **Read depth.** 37 pages; the printed page equals the PDF page; notes 1-21. Honest.
3. **Quotations.** 44 segments, all MATCH at the stated pages, including the hard checks at pp. 11, 20, 22-23 and 25. Three needed a manual step: the abstract crosses pp. 1-2, "trajectory-level" is hyphenated at a line end (p. 11), and the p. 27 string has a space after an em dash.
   - *Precision.* Note 11 (p. 19) cites Duff [27], Kiener [28] and Van de Poel [26]; the card names Duff and Van de Poel only. The Duff principle itself sits at p. 20 with n. 13, as R11's report says.
4. **The argument.** The three premises are at p. 20, and strict answerability is Kiener's account as the authors adopt it ("As Kiener argues", p. 22; "Kiener's reply", p. 23). Two passages the card leaves out bear on K7.
   - (a) *Contestability by affected parties.* The agenda "must be contestable" (p. 14). "Inspection generates occasions for contestation: cases in which other reasonable parties affected by the deployment may legitimately object to what the agent did", and inspection "is the practice through which the principal learns from experience" (pp. 15-16). Contestability, "that reasonable parties affected by the deployment can challenge the agent's action in terms they can engage with", "is what the contestability requirement ... demands of the regime as a whole" (p. 17). The authors therefore require a route by which affected parties challenge the agent's action, and they treat those objections as the principal's way of learning. The route sits in the inspection phase and runs to the principal. Within a session only the agent flags actions for review ("an agent might flag a candidate action for principal review", p. 16).
   - (b) *Directedness.* The agenda represents "the obligations to others her position generates" (p. 20). Standing is "grounded in the role obligations of the principal" (p. 22), and the student has an "entitlement to an answer" (p. 22).
5. **May say / may not say.**
   - May say 1: LICENSED. It would be closer to the text with their triad "specifying, monitoring, and refining" (p. 20); monitoring is the part K7 needs.
   - May say 2-3: LICENSED.
   - May not say 1: LICENSED as worded, but the card should record (a).
   - May not say 2: LICENSED-NARROWER (see the table).
   - May not say 3-4: LICENSED.
6. **Bearing.** I agree with the P3 reading. The C reading and the critical note "No real-time route from the affected party" understate the source. The paper requires a route from affected parties, after the fact and to the principal, and makes it part of how she learns (pp. 14-17). That is the nearest published premise for a means of learning fed by the people affected. The novelty difference the card names, a route during performance to someone with power over the single case, still stands. The paper should add that Baum et al. already make affected parties' contestation part of the principal's oversight. On K9: the within-session flag comes from the agent, not from the affected party (p. 16).
7. **Reader's inferences.** "The guest would be such a party" is supported conditionally, since standing goes to "whose interests the agenda was meant to protect" (p. 22). It stays open because institutional principals are outside the account (p. 27).

## 10. pettit2007responsibility (R11, new card)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref matches: *Ethics* 117(2), pp. 171-201, January 2007. The saved PDF is an Acrobat Distiller file of 30 Jan 2007, 31 pages, carrying "© 2007 by The University of Chicago. All rights reserved." The Internet Archive capture of 2 Jan 2025 exists, and my re-download is byte-identical.
   - *K-D12 edge case.* Unpaywall (re-queried) lists the article as closed, with no open location. The copy is the author's institutional posting of a publisher-closed text. K-D12 admits "a copy a repository serves without charge" and excludes captures of paywalled texts; a personal page at the author's university falls between the two. The card records the facts honestly. The lead should record whether K-D12 covers author-page copies.
2. **Read depth.** 31 pages, pp. 171-201, with notes 1-42. Honest.
3. **Quotations.** 29 segments, all MATCH (p. = PDF p. + 170). 'Duty' and 'duties' do not occur in the article, and 'obligation' occurs only in n. 11's cited title and in n. 38, as the card says.
4. **The argument at p. 195.** The unincorporated collection Pettit discusses is made of "individuals who do not incorporate as a group agent but combine to have a common effect or, on a one-off basis, form a joint intention and perform a joint action" (pp. 194-195). His examples are a firing squad and a group of speeding drivers. He does not discuss incorporated firms that contract with one another. The card flags its application to brand, operator and platform as its own ('application mine'), which is right.
5. **May say / may not say.** May say 1-3: LICENSED. Under may say 3, the paper should add that Pettit's collections are collections of individuals. May not say 1-3: LICENSED.
6. **Bearing.** Agree. The backups passage (p. 192) is an internal fall-back with no route from the people affected.
7. **Reader's inferences.**
   - That the step from responsibility to duty is the paper's own is supported.
   - The application to a brand, an operator and a platform is open. A franchise or management system with a common procedure might meet Pettit's test of "maintaining a constitution for the formation and enactment of its attitudes" (p. 192). Applying his criteria (pp. 179-180, 192) to the actual contracts would settle it.

## 11. herstein2023legal (R11 addendum only)

**Verdict: PASS-WITH-NOTES**

1. **Identity.** The live entry is byte-identical to the saved HTML ("First published Fri Jan 27, 2023"). The bibliography gives *Griswold* as 381 U.S. 479 (1965), Wellman 1995 as *Real Rights* (Oxford University Press), Nickel 2007 as *Making Sense of Human Rights*, 2nd edn (Blackwell), and Raz 1986 with doi 10.1093/0198248075.001.0001. All match the addendum.
2. **Read depth.** My parse of the `<p>` and `<blockquote>` tags agrees with R11's count: preamble 1 paragraph; §1 nine paragraphs (block quotations after paras 3 and 8); §2 one; §8.4 two; §9.3 three. The red team's locators (§1, paras 7-8; §8.4, para. 2) are correct. As R11 notes, the frontmatter `source_basis` still lists §§1 and 8.4 as unread.
3. **Quotations.** 25 segments: 24 MATCH in the entry, and one is the red team's paraphrase, which matches REDTEAM_PHIL, S1. 'Dynamic aspect' does not occur in the entry, as R11 says.
4. **What the entry reports, against the addendum.**
   - *Are §§1 and 8 confined to legal rights?* Not quite. The preamble gives Sections 3-5 to "features common to all rights (legal, moral, or otherwise)" and Sections 1-2 and 6-10 to "some features and types of rights unique or particularly salient to legal rights". Section 1 is headed "The Legal Validity and Justification of Legal Rights" and section 8 "Legal Rights as Reasons". The entry thus files both under legal rights. But "particularly salient" does not deny the features to moral rights. Section 8.4, para. 1 and the first two sentences of para. 2 speak of "rights" and a "claim-right" without qualification and cite Raz 1986. R11's heading, "features particular to legal rights", says more than the preamble does; the quotation that follows it is exact.
   - *The dependence sentence.* R11 reads it correctly. Literally, "the latter" (the justified right) depends on "the former" (the justifying right). In the *Griswold* quotation the specific (core) rights "would be less secure" without the peripheral rights they include, so there the core depends on the derived. The red team's paraphrase follows the example, not the sentence.
   - *§8.4, paras 1-2.* As quoted, including "in the absence of countervailing reasons" and Kramer's reply that dynamic rights are "only inchoate rights".
   - *§9.3.* R11 omits para. 3, which adds that "moral rights can count in favor and even justify legal arrangements that do not take the form of any legal right" (compulsory schooling, after Waldron 1999). That still runs from moral rights to law, so R11's "nothing of moral rights justifying further moral rights or duties" stands.
5. **May say / may not say.** The addendum has no list; I judged its 'Where this bears' sentences.
   - "It does not report either for moral rights": LICENSED.
   - "by its own preamble §§1 and 8 concern features 'unique or particularly salient to legal rights'": LICENSED.
   - "Cite Herstein for the structure as reported in legal theory, with the theorist named, and do not cite the entry for a moral claim": LICENSED.
   - The contrary heading "The entry places §§1 and 8 among features particular to legal rights": LICENSED-NARROWER (see the table).
6. **Bearing.** Agree with the two routes and with the conclusion that the moral use rests on unread sources. My passage: "This dynamism arguably cuts against the seemingly more frozen view ... implied by Hohfeldian correlativity" (§8.4, para. 2). The "arguably" and the Kramer reply make Route B contested in the entry itself.
7. **Reader's inferences.**
   - Two routes, not one: supported (§1, para. 8; §8.4, para. 2).
   - "Dependence strength appears only in Route A": supported. Section 8.4 names no dependence; its trigger is "changes in factual circumstances".
   - On the Hohfeldian reply, a new duty implies a new or inchoate right: supported as an inference from correlativity and Kramer as reported. Kramer (1998: 41-48) would settle it; it was not read.
   - The reading of "Relatedly" (that duties justified dynamically are correlative): open. Raz (1986: 171, 185-186) would settle it; it is closed in this run.

---

## Table: every FAIL, every quotation not MATCH, every sentence not LICENSED

| # | Card | Item | Finding | Narrower wording or fix |
|---|---|---|---|---|
| — | all | FAIL | None | — |
| — | all | Quotations not MATCH | None of 288 source quotations | — |
| 1 | lynch2011theorizing | R9 section, bullet 1 (and `WS_P1_R9.md` §1(c)) | Error: the 'contestation' sentence does not close its paragraph | "The sentence sits mid-paragraph; the paragraph continues 'Friese (2004) also argues for the opening up of spaces of hospitality', then Grit and Valentine (PDF p. 9)." Attribution stays with Lynch et al. |
| 2 | lynch2011theorizing | Read depth / version | The saved copy is a pre-publication version ('DRAFT 2'; Unpaywall: submitted version; first page asks readers to consult the final version) | Check the wording of 'enable contestation and conflict' in the version of record before quoting it |
| 3 | petie2025exploring | R9 'Contrary' bullet and 'Bearing' ("The single queries were handled"; "the queries that reached the hotel were handled") | LICENSED-NARROWER | "The Government evaluation found that Badreddin's queries at the Park Inn 'were dealt with appropriately' (MS p. 12, citing Laing 2020); the same page reports from news accounts that 'no actions were taken to help them', and MS p. 11 that staff told the night before 'lacked the knowledge needed to act'." |
| 4 | petie2025exploring | R9 'host's responsibility' bullet ("Telfer is paraphrased, not quoted, three times") | Narrower | "Telfer's claim about responsibility for welfare is paraphrased (MS pp. 3, 12, 13); Telfer is quoted once, for the definition of hospitality (MS p. 3, Telfer 2000: 39)." |
| 5 | moysidou2023theorizing | R9 'Bearing', last sentence (S6) | LICENSED-NARROWER | "The one complaint to an intermediary in the data came from an applicant refused before arrival (Pauline, p. 10); it shows a route at admission, not during a stay. The Emergency Help Plan is the organisation's offer (p. 16)." |
| 6 | kekstaite2022beyond | Critical note 'Bibliography error' (and `WS_P1_R9.md` note 3) | Stale | `references.bib` line 1090 now reads 'Kekstaite, Julija'; drop the note |
| 7 | kekstaite2022beyond | Summary ("eighteen Brussels residents"); `source_basis` on version | Narrower | "18 respondents, mostly living in Brussels and its surroundings" (AM p. 6); add that the Ghent record labels the file 'Accepted manuscript' |
| 8 | ogorman2007discovering | Key fact "(p. 44; repeated p. 47)"; the silence note | Precision | p. 47 repeats the sentence without "Extensive"; name p. 44's "protected by one legal system" (citizens travelling, not inns) |
| 9 | kiesewetter2015instrumental | May say 2 | LICENSED-NARROWER | "He states the principle for necessary means (pp. 922, 925) and reports Way's own concession that a principle not so restricted is 'open to objections that do not apply to a transmission principle restricted to necessary means' (p. 922, n. 2)." |
| 10 | kiesewetter2015instrumental | May say 3 (and `WS_P3_R11.md` §1(b)) | LICENSED-NARROWER | "Discussing an agent's own likely failure to conform, he says the likelihood 'could' supply 'second-order reasons to adopt additional measures that ensure his conformity' without changing the agent's first-order obligations (p. 937)." He does not say such measures can never be obligatory. |
| 11 | baum2026anticipatory | May not say 2 | LICENSED-NARROWER | "That they say in terms that the role-grounded prospective obligation is owed to the affected parties. They describe the agenda as representing 'the obligations to others her position generates' (p. 20) and ground standing in 'the role obligations of the principal' (p. 22), which leaves directedness open." |
| 12 | baum2026anticipatory | 'Where it bears', K7 C; critical note "No real-time route" | Narrower reading | Add: the authors require that affected parties can "challenge the agent's action in terms they can engage with" (p. 17), that the agenda be "contestable" (p. 14), and that their objections at inspection be how the principal "learns from experience" (pp. 15-16). The route is after the fact and to the principal. |
| 13 | baum2026anticipatory | Key fact on n. 11 | Omission | n. 11 also cites Kiener [28] |
| 14 | herstein2023legal | Addendum, first contrary heading ("features particular to legal rights") | LICENSED-NARROWER | "The preamble files §§1-2 and 6-10 under features 'unique or particularly salient to legal rights'; it does not deny them to moral rights, and §8.4 paras 1-2 open with unqualified 'rights' and 'claim-right', citing Raz 1986." |
| 15 | herstein2023legal | Frontmatter `source_basis` | Stale (R11 flagged it) | Add the preamble, §§1, 2 (para. 1), 8.4 and 9.3 as read (R11) |
| 16 | pettit2007responsibility | `source_basis`, K-D12 | Edge case for the lead | Publisher-closed (Unpaywall: closed; 'All rights reserved'); the copy is the author's institutional posting, archived 2 Jan 2025. Record whether K-D12 covers author-page copies |

<!-- Independent verification of cards, batch CV-F, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. -->

# Verification of cards, batch CV-F (run rr-2026-11-k)

**Scope.** Ten cards. Reader R7 wrote five: `rudyhiller2022epistemic`, `globaltech2011seb`, `manifest2001unipolaris`, `page1972sloan` and `hormio2018culpable`. Reader R8 wrote the other five: `gelbrich2011metaanalysis`, `schumacher2016case`, `xu2024disciplined`, `lee2025robot` and `min2020angry`. I wrote none of them, and I edited no card and no other file.

**Method.** I extracted the text of every saved source myself rather than relying on the readers' extractions. I used `pdftotext` for the PDFs and my own parser for the HTML. The parser rebuilt three locator schemes: paragraph and speaker for *The Star Sea*, CAP page labels for the two American cases, and section and paragraph for the encyclopedia entry. A script of mine pulled every double-quoted string off each card, split it at ellipses and bracketed insertions, and searched the source with only whitespace, line-end hyphenation, ligature, quotation-mark and dash differences allowed. It then mapped each hit to its page or paragraph. I read every non-match and every borderline match by hand. I also checked the multi-word single-quoted phrases on the cards; all of them occur in the sources. Where OCR was in doubt I rendered the scanned page and read it. Scripts, extractions and downloads are in the session scratchpad, not in the project.

**Records re-fetched on 11 Nov 2026.**
- Byte-identical to the saved copies: the Stanford Encyclopedia entry (live page); the CAP HTML of 563 U.S. 754 and 281 N.C. 697; and the Internet Archive captures of the Gelbrich and Roschk PDF and the Min and Kim PDF.
- Crossref, re-queried for each DOI: Gelbrich and Roschk; Schumacher and Komppula; Xu and Greiffenhagen; Lee et al. and its correction; Min and Kim; Hormio's SocArXiv DOI; Min, Joireman and Kim (2019); Min and Kim (2019).
- Additional records: the House of Lords' own text of *The Star Sea*, through Internet Archive captures of publications.parliament.uk (2006); CAP's scanned case PDF of *Page v. Sloan*; the distributor's record of *Acta Philosophica Fennica* 94 (tiedekirja.fi); and the PolyU repository handle for Xu (HTTP 200).
- Refused, and not bypassed: publications.parliament.uk (403, bot check); PhilArchive (Cloudflare 403); the TAMU catalogue (403). supremecourt.gov returned 404 for the *Global-Tech* slip PDF.

**Verdicts.** PASS 1; PASS-WITH-NOTES 9; FAIL 0.

**Quotation tally.** I checked 341 quoted segments. One of them, on the *Global-Tech* card, quotes reader R5a's report, not a source; it matches `WS_P4_R5a.md`. Of the other 340, 337 are MATCH with a correct locator. One is PARAPHRASED-AS-QUOTE (*The Star Sea*: "no special steps"). Two are OCR-DOUBT (*Page*: "depending,on", where the printed page has no comma). Nine MATCHes needed a manual step:
- three quotations run across a page break or a page number (Hormio, pp. 20-21; Schumacher, p. 123);
- three differ only in spacing (two at "§ 271 (b)" in *Global-Tech*; one in Rudy-Hiller, "indirect )");
- two have an initial letter whose case the card changed (Rudy-Hiller "while", Min "Complain");
- one is the *Page* repair "[loquitur]", which the printed page confirms.
No quotation is LOCATOR-WRONG or NOT-FOUND.

---

## 1. rudyhiller2022epistemic

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - The live entry, re-fetched, is byte-identical to the saved HTML (SHA-256 aff5a352...). Its header reads "First published Wed Sep 12, 2018; substantive revision Tue Oct 4, 2022".
   - The saved citation page directs citation to the Fall 2025 Edition (minor correction), eds Zalta and Nodelman, and says the entry was "last modified on Sep 12, 2025". The Fall 2025 archive URL resolves.
   - The card and citekey carry 2022, but R7's bibliography entry and the encyclopedia's own recommended citation carry 2025. The card discloses this; the lead must choose one year. No DOI exists.
2. **Read depth.** The saved files hold the preamble, §§1.1-4, notes 1-15 and the bibliography, as the card says. This is a direct fetch, not an archive capture.
3. **Quotations.** 44 segments, all MATCH. My paragraph count matches R7's at every locator I checked (§1.1 ¶1 to §4 ¶3, notes 9, 11 and 12). The slips the card reproduces ("avoid thinking", "whenever isn't reasonable", "her wife's tea") are in the source.
4. **Attribution (the entry has no holding or statistic).** Nearly every substantive sentence reports a named philosopher, as the card says. The card says Pleasants (2008) and Wieland (2017c) are "not discussed in the body". That is accurate, but note 9 cites both as critics of Moody-Adams' affected-ignorance thesis.
5. **May say / may not say.**
   - May say 1: LICENSED-NARROWER. The entry says it is "widely—although not universally (cf. Holly Smith 2017; Ross 1939: 163–4)—accepted that culpable ignorance fails to exculpate (at least completely)" (§2 ¶2). Holly Smith (2017) is cited against the view, so "reporting Holly Smith and others" misattributes. Write: "it is widely, though not universally, accepted that culpable ignorance fails to exculpate, at least completely (Rudy-Hiller 2022: §2 ¶2, citing Holly Smith 2017 and Ross 1939 against)".
   - May say 2, 3 and 5: LICENSED.
   - May say 4: LICENSED-NARROWER. This is the dispositionalists' argument against occurrentism, and the thinking avoided concerns "the moral status of one's action" (§1.2 ¶7). Write: "dispositionalists argue that on the occurrentist view 'one could shield oneself from blame simply by' not thinking about 'the moral status of one's action' (§1.2 ¶7, reporting Guerrero, Timpe, Robichaud and Levy)".
   - May say 6: LICENSED-NARROWER. Rudy-Hiller draws the distinction with citations to Rosen (2004, 2008), H. Smith (2014) and Wieland (2017a), in reporting capacitarianism (§3.4 ¶7). Write: "Rudy-Hiller, following Rosen, H. Smith and Wieland, distinguishes ...".
   - May not say 1-4: LICENSED. The hold rationale's "says nothing on ... law" overstates a little: the entry cites Husak on legal ignorance (§2 ¶7) and "the moral and legal category of negligence" (note 11).
6. **Bearing on K7 and K9.** I agree that the entry gives P3 its vocabulary and does not establish it. One precision matters for R7's synthesis. The entry defines duties of inquiry as "obligations to undertake information-gathering actions" and says that the norms of awareness capacitarians rely on "aren't duties of inquiry" (§3.4 ¶7). P3 as a duty of inquiry therefore belongs to the tracing account (Rosen's "procedural epistemic obligation", §2 ¶4). The capacitarian route reaches the host through a norm of awareness, a different form. I agree that the entry has no bearing on K9.
7. **Reader's own inferences.**
   - "In the entry's terms P3 is a duty of inquiry": supported (§3.4 ¶7).
   - That volitionists would excuse a host without awareness: supported as a reading of §2 ¶5-¶6, but open as applied to firms, because the entry treats only individuals.

## 2. globaltech2011seb

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - The CAP HTML, re-fetched, is byte-identical to the saved copy. The CAP JSON gives No. 10-6, decided 2011-05-31, pp. 754-775, and the citations 563 U.S. 754, 131 S. Ct. 2060 and 179 L. Ed. 2d 1167.
   - The header reads "Argued February 23, 2011 — Decided May 31, 2011". Alito J delivered the opinion of the Court, joined by Roberts CJ and Scalia, Thomas, Ginsburg, Breyer, Sotomayor and Kagan JJ; Kennedy J dissented (756). All of this matches the card.
   - The OCR misreadings the card lists are present. The supremecourt.gov slip PDF returned 404 to me as well.
   - **Error in `source_basis`.** The card says the only differences from the LII slip text were "the spacing of '§' and line-break hyphens". There are two wording differences. The U.S. Reports read "its chief executive officer and president" (770) where the slip reads "its CEO and president", and "(1) The defendant" (769) where the slip reads "(1) the defendant". The card's quotations follow the U.S. Reports, which is right; only the cross-check statement is wrong.
2. **Read depth.** The opinion (757-771) with notes 1-10 and the dissent (772-775) are present. The text is an OCR copy with CAP page labels, as disclosed.
3. **Quotations.** 47 segments. 46 are source quotations, all MATCH. One ("removes every route by which a guest could tell it") quotes R5a's report and matches it.
   - Footnote locators are correct. Note 6 begins on 766 and the quoted words fall on 767; Florez is in n. 9 (769); the refusal to remand is n. 10 (770).
   - The majority quotes *Spurr* as "purposely" (767); the dissent's quotation reads "purposefully" (773). The card quotes only the continuation from the dissent, and correctly.
4. **Holding and dissent.** I confirmed every element the card relies on:
   - knowledge that the induced acts infringe is required (766);
   - "deliberate indifference to a known risk" is not the standard (766);
   - the two requirements (769) and the scope that "surpasses recklessness and negligence" (769);
   - the definitions of the reckless and the negligent defendant (770);
   - the evidence was sufficient, through Sham's acts (770-771); the judgment was affirmed (771).
   Eight Justices joined; Kennedy J dissented (772-775).
5. **May say / may not say.** May say 1-6: LICENSED. May not say 1-5: LICENSED.
6. **Bearing on K7.** I agree. The Court's own line excludes the host without a high-probability belief: "a negligent defendant is one who should have known of a similar risk but, in fact, did not" (770).
7. **Reader's own inferences.**
   - That withholding the fact from the attorney is "closer to designing a channel so that it cannot carry the decisive information than to having no channel": supported as analogy (771). It is not a legal proposition.
   - That a host with no such belief is outside the doctrine: supported (769-770).

## 3. manifest2001unipolaris

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - The BAILII header in the capture gives [2001] UKHL 1, [2001] 2 WLR 170, [2003] 1 AC 469, [2001] 1 All ER 743 and [2001] 1 Lloyd's Rep 389, with the date 18 January 2001. These match the card.
   - The official site refused me (403). I therefore fetched the 2006 Internet Archive captures of the House of Lords' own text (publications.parliament.uk/.../jd010118/manife-1 to manife-6.htm), dated "18 JANUARY 2001". In that text, para 3 is in Lord Clyde's speech and paras 24-27 are in Lord Hobhouse's. Lord Scott's speech begins on manife-4, and paras 116-119 fall within it on manife-5. The paragraph numbers agree with BAILII. **The card's attributions of paras 3, 24-27 and 112-119 are correct.**
   - The report citations were not checked against the printed reports, as the card says.
2. **Read depth.** The capture holds all 120 paragraphs; I parsed every number. "Blind" does not occur in paras 37-80 or 90-111, as the card says. The source is an archive capture, as disclosed.
3. **Quotations.** 50 segments. 49 are MATCH with correct paragraph and speaker.
   - **PARAPHRASED-AS-QUOTE:** "no special steps" (critical notes, "paras 30-31"). Para 31 reads "the managers of the fleet did not take any special steps".
   - One attribution slip: the para 112 bullet says Lord Scott quotes Lord Blackburn "..., adding 'I think that is dishonesty'". The words are Lord Blackburn's ("Lord Blackburn added 'I think that is dishonesty'", para 112). The quoted words are right; the participle reads as Lord Scott's.
4. **Holding, dictum and composition.**
   - The House unanimously dismissed the appeal on both issues (paras 1, 2, 8, 36, 120). On s. 39(5) it held that the Court of Appeal was right to reverse the finding of privity (Lord Hobhouse para 36; Lord Scott para 120; Lord Clyde para 3).
   - Lord Steyn agreed with Lords Clyde, Hobhouse and Scott (para 1); Lord Hoffmann with Lords Hobhouse and Scott (para 2). Lord Scott's reasons therefore carry three Lords.
   - On the insurers' concession, privity had to extend to both defects (para 115; Lord Hobhouse para 34), so failure on the master sufficed. The dampers point (Lord Scott paras 118-119; Lord Clyde "in any event", para 3) is an additional ground.
   - **Para 117.** Lord Scott said the earlier losses "did not put [the four individuals] in a position in which they were bound to enquire into the competence of every other master". The sentence follows "I can see no sufficient basis for attributing to any of the four individuals blind-eye knowledge". "Bound to enquire" thus belongs to the privity test: whether the earlier losses created a targeted suspicion. It is not a ruling on any duty of care.
   - The same speeches call the managers' conduct fault or negligence. Lord Hobhouse wrote "the managers were at fault" (para 32). He quoted Leggatt LJ: "Negligence there may have been in failing to ensure that the master was instructed" (para 33). Lord Scott wrote of the dampers findings that "These findings go to negligence, perhaps gross negligence" (para 119).
   - "Some system should have been in place" is the trial judge's view as Lord Scott reports it (para 118).
   - Three phrasings on the card overread these passages:
     - the key-facts heading "No general duty to enquire arose from the earlier losses";
     - the hold rationale's "All of that was held to be negligence, even gross negligence". No Lord held the managers negligent; the case decided privity;
     - R7's report, (iv): "earlier failures across a fleet did not oblige the managers to enquire into every master".
5. **May say / may not say.**
   - May say 1, 2, 3 and 5: LICENSED.
   - May say 4: LICENSED-NARROWER. Write: "The House held that the managers lacked blind-eye knowledge although, after two similar losses, they took 'no steps to check' the master's knowledge (para 30, Lord Hobhouse). Lord Scott said that the trial judge's findings on the dampers, including that 'some system should have been in place', 'go to negligence, perhaps gross negligence' but are 'no basis for a finding of blind-eye knowledge' (paras 118-119)."
   - May not say 1: LICENSED-NARROWER. The prohibition stands, but the reason "The House held the contrary" should read "Lord Scott, whose reasons Lords Steyn and Hoffmann adopted, said such findings are no basis for blind-eye knowledge (paras 1-2, 118-119)".
   - May not say 2: LICENSED-NARROWER. The first sentence stands. Replace the second with: "Lord Scott said the earlier losses did not put the individuals 'in a position in which they were bound to enquire' (para 117), in deciding whether blind-eye knowledge could be attributed; the speeches treat the failures as fault or negligence (paras 32-33, 119)."
   - May not say 3: LICENSED.
   - May not say 4: LICENSED. Lord Scott did consider the four "individually or collectively" (para 119), so the House found nothing to aggregate; it did not rule aggregation out.
6. **Bearing on K7 (P3).** I agree that the case decides against the knowledge route for an untargeted suspicion (paras 116, 119). I disagree that it is a rival to P3 understood as a claim about care. On the duty to check, the speeches point the other way: failing to check after two similar losses was "at fault" (para 32) and went "to negligence, perhaps gross negligence" (para 119). By analogy that supports a care-based P3. It refutes only a knowledge-based one.
7. **Reader's own inference.** That a host with no channel and no particular suspicion "stands where these managers stood": supported for the knowledge question (paras 116, 119), but open as to care, since no Lord decided what care required. A court's ruling on a duty of care to check would settle it.

## 4. page1972sloan

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - The CAP HTML, re-fetched, is byte-identical (SHA-256 1c6a2e17...). It shows No. 10, filed 31 July 1972; Huskins J for the Court (702); certiorari to the Court of Appeals, 12 N.C. App. 433 (701); and summary judgment by Long J, 18 January 1971 Session, Moore Superior Court (698). No dissent is printed. All of this matches the card.
   - I also downloaded CAP's scanned case PDF (static.case.law/nc/281/case-pdfs/0697-01.pdf, 13 pp.) to settle the OCR questions.
2. **Read depth.** The headnotes, statement of the case and opinion (697-709) are present.
3. **Quotations.** 46 segments.
   - **The '[loquitur]' repair is right.** The printed page 708 reads "*res ipsa loquitur*"; the CAP OCR reads 'loquilv/r'.
   - **OCR-DOUBT (two segments):** "Thus, depending,on the evidence ..." (key facts, 703) and "depending,on the evidence offered at the trial" (critical notes). On the scan of p. 703 a stray speck sits between "depending" and "on"; it is not a printed comma. The card's "(703; so in the text)" describes the OCR, not the report. Quote "depending on".
   - The other 44 segments are MATCH with correct pages. Phrases also printed in the reporter's headnotes occur in the opinion at the pages cited (702-704).
   - **Error in `source_basis`.** 'Testate' (699, 703) is printed so in the report, as the scan of p. 703 shows; it is not an OCR misreading.
4. **Holding, and whether non-delegability was one of three alternative bases on review of summary judgment.** Confirmed.
   - At 702 the court states the standard of care and calls the duties non-delegable, quoting 40 Am. Jur. 2d § 81. It grounds the rule on the duty being "so important to the public", and quotes Restatement § 425 with its hotel illustration (702-703).
   - At 703-704: "depending on the evidence offered at the trial, defendants in this case could be liable on any of the following bases": (1) negligent selection, (2) the non-delegable duty, (3) res ipsa loquitur.
   - The holding is at 706: "We hold that defendants have failed to carry the movant's burden of proof." Paragraph [7] on 708 lists triable issues, among them "Was the plumber negligent in making the repairs?", which matters under basis (2). Paragraph [8] says res ipsa was not shown inapplicable, and which theory goes to the jury is left to the trial judge (708). The judgment was "Affirmed" (709).
   - Non-delegability is the court's statement of the governing law. It is one of three alternative bases and no finding of liability.
   - The card's account of the authority omits one item: the court also cites "Prosser on Torts (4th ed. 1971), § 71 at p. 470" (702). It still cites no earlier North Carolina decision for the rule. One of the out-of-state cases is a hotel case, *Blackhawk Hotels Co. v. Bonfoey* (OCR 'Bowfoey'), cited for "A like result" (703).
5. **May say / may not say.** May say 1-5: LICENSED. May not say 1-5: LICENSED.
6. **Bearing on K8 and K7.** I agree. Basis (2) makes the owners liable "as if they had made the repairs themselves" (704), and their answer pleaded that defects "could not have been known to them" (699).
7. **Reader's own inferences.**
   - That under basis (2) "arranging not to know would gain such a holder nothing": supported by the structure at 704. The court never addresses the plea under that basis.
   - The contrast with *Maguire*: open. I did not re-read *Maguire*.

## 5. hormio2018culpable

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - Crossref, re-queried, lists DOI 10.31235/osf.io/85nbu as posted-content (SocArXiv, Hormio, 11 Dec 2018) and no journal version. The PDF's hash matches the card (61bdb27e...). Page 1 reads "Forthcoming in Acta Philosophica Fennica 94 (2018), pp. 7-34."
   - **Version of record.** The volume exists. Its distributor (tiedekirja.fi, fetched 11 Nov 2026) lists *Acta Philosophica Fennica* 94, *Action, Value and Metaphysics*: eds Jaakko Kuorikoski and Teemu Toppinen, Helsinki, Philosophical Society of Finland, 2018, 189 pp., ISBN 978-951-9264-89-9, ISSN 0355-1792.
   - That page gives no table of contents, so Hormio's article and its pp. 7-34 rest on the preprint's own statement. The preprint thanks the audience at the "Philosophical Society of Finland Colloquium 2018" (p. 21), which fits this volume.
   - PhilArchive (Cloudflare 403) and the TAMU catalogue (403) refused me. **The journal version was not seen.**
2. **Read depth.** The 22-page preprint is complete, and printed page numbers equal PDF page numbers.
3. **Quotations.** 54 segments, all MATCH with correct pages. One runs across pp. 20-21 with the page number between, as the card's "pp. 20-21" says.
4. **(Not a case or empirical study.)** The card says the paper lacks "wilful blindness as a legal doctrine". That is accurate, but p. 11 discusses individual "wilful ignorance" (quoting Isaacs 2011).
5. **May say / may not say.**
   - May say 1, 2 and 5: LICENSED.
   - May say 3: LICENSED-NARROWER. Hormio states it of her example, on a condition about the firm's ethos (p. 17). Write: "In Hormio's example, a supplier whose ethos puts price competitiveness above all else runs 'a risk that falls within known risks' and, having 'gotten away without adequate safety checks', 'could not justify this way of operating by appealing to ignorance' (p. 17)."
   - May say 4: LICENSED-NARROWER. She says it of the category of "knowable recognised unknowns": "With this category, I think that we should keep in mind that organisations have less excuses ..." (p. 5).
   - May not say 1-4: LICENSED.
6. **Bearing on K7 (P3) and K9.** I agree, including the two limits. For design-produced ignorance, Hormio places negligence after a harm: "When this has happened, and there is a harmful outcome, ... the organisation should look at its design ... If they do not, I argue that they are blameworthy for being negligent" (p. 15). The known-risk route is the one stated on p. 17. Her algorithm example (p. 20) bears on K9.
7. **Reader's own inference.** That Smith's known-risk limit "is easily met" for a host: open. On Hormio's report, Smith requires that "the unwitting wrongful act falls within the known risks of the earlier act" (p. 19). The application needs a stated benighting act (designing out the channel) and a stated wrongful act (a guest's harm left unaddressed). It would be settled by a published application, or by the authors stating both acts and arguing the risk was known.

## 6. gelbrich2011metaanalysis

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - Crossref, re-fetched, gives *Journal of Service Research* 14(1): 24-43, by Katja Gelbrich and Holger Roschk, online 3 Dec 2010, print February 2011. This matches the card.
   - I re-fetched the Internet Archive capture (web.archive.org/web/20260113213110id_/...ilm1-2014210204.pdf; HTTP 200, application/pdf). It is byte-identical (SHA-256 1a9f529a...).
   - **The file is the published SAGE article, not an author version.** Page 2 is SAGE's cover sheet ("Version of Record - Dec 29, 2010"; "Downloaded from jsr.sagepub.com at Technische Universität Ilmenau on October 14, 2014"). Pages 24-43 carry the journal's typesetting. Page 1 is TU Ilmenau's deposit sheet (URN, "Published OpenAccess: October 2014", Alliance and national licence).
2. **Read depth.** Journal pp. 24-43 are complete. The source is an archive capture of the repository deposit, as disclosed.
3. **Quotations.** 26 segments, all MATCH with correct pages, including "(pp. 39-40)" for the unexamined moderators, which run from p. 39 to p. 40.
4. **Design and statistics: all confirmed.**
   - The search covered 1980 to June 2009 and found 142 articles; 55 were excluded, leaving 87 studies with 95 samples, N = 28,826, 477 effects and a mean N per relationship of 3,667 (p. 28).
   - The model ran in AMOS on the median N of 241, with zero correlations assumed among the responses (p. 29).
   - Fit: χ²(22) = 29.670, p = .127, AGFI .942, CFI .995, RMSEA .038 (p. 31; Figure 3, p. 32).
   - Indirect effects: .35/.20/.26 on transaction-specific satisfaction, .38/.34/.36 on cumulative satisfaction and .31/.25/.28 on loyalty (p. 32, Table 3).
   - γ = .53, .59 and .51 (p. 36; Table 4, p. 33). β = .41, .31 and .19 on cumulative satisfaction (p. 36).
   - Of the 37 moderator samples, 28 were service, 4 non-service and 5 mixed (p. 34). Interactional justice had β = .46 in services against .25 in non-services, **on cumulative satisfaction** (p. 34; Table 6, p. 35). Industry did not moderate transaction-specific satisfaction (p. 34).
5. **May say / may not say.**
   - May say 1 and 3: LICENSED.
   - May say 2: LICENSED-NARROWER. Write the second clause as: "and, for cumulative satisfaction, fair treatment weighed more in the 28 service samples than in the 4 non-service samples (β = .46 vs .25); industry did not moderate transaction-specific satisfaction (Gelbrich and Roschk 2011: 34)".
   - May not say 1-4: LICENSED.
6. **Bearing on K7 (P4) and K9.** I agree with "consistent, not shown" and with "no bearing" on K9, with one correction. The card, and R8's report, say "the employee's manner weighs more in services (pp. 32, 34, 36)". The services moderator acts on interactional justice, the complainant's perception of fair treatment, as it bears on cumulative satisfaction (p. 34). It does not act on favourable employee behaviour itself. Write "fair treatment weighed more in services".
7. **Reader's own inference** (R8's report): that the remedies "could in principle be delivered by rule". Open. The meta-analysis codes no handler (Figure 2, p. 26), so only a study that coded who handled complaints, and with what authority, would settle it.

## 7. schumacher2016case

**Verdict: PASS**

1. **Identity.** Crossref, re-fetched, gives EJTHR 7(2): 117-127, Schumacher and Komppula, doi 10.1515/ejthr-2016-0014. Page 117 reads "EJTHR 2016; 7(2):117-127", received 30 June 2015, accepted 20 July 2015. The PDF's hash matches (fb017382...).
2. **Read depth.** All 11 pages are present.
3. **Quotations.** 23 segments, all MATCH with correct pages. In the extracted text of F1's line (p. 123) the page number falls mid-sentence; the wording is exact.
4. **Design and findings.**
   - Design: one small Helsinki hotel; semi-structured interviews with seven reception staff, the frontline manager and the hotel manager, about an hour each; six women and three men (p. 121).
   - The hotel "relies mainly on customer feedback" (p. 121).
   - The frontline manager reports that staff "usually resolve the service failures themselves" (p. 121).
   - "the easiest thing to do is to change the room for a better one" (pp. 121-122).
   - There is "no set amount" of compensation, and staff are reluctant beyond 10-20% (p. 122).
   - The hotel uses gift vouchers as compensation (p. 121), but reception does not write them (p. 122), which is consistent with the card.
   - The staff are unclear about the limits of their authority (p. 123).
5. **May say / may not say.** May say 1-3: LICENSED; for may say 2, the source of the statement is the frontline manager (p. 121). May not say 1-4: LICENSED.
6. **Bearing on K7 (P4) and K9.** I agree: "relies mainly on customer feedback ... It is not a normal procedure that frontline employees would ask" (p. 121), set against "may either spot the service failures themselves or be informed about them by customers" (p. 120).
7. **Reader's own inference.** That the graded empowerment "matches the abstract" of Hewagama et al. (2019): open. That paper is closed and I did not check it.

## 8. xu2024disciplined

**Verdict: PASS-WITH-NOTES**

1. **Identity.** Crossref, re-fetched, gives *New Media & Society* 26(9): 5013-5038, Xu and Greiffenhagen, online 30 Aug 2024, print September 2024. The PDF is the version of record (journal pagination; "Special Issue: Automating Communication"). The PolyU handle 10397/112592 resolves (HTTP 200). The hash matches (256d9888...).
2. **Read depth.** All 26 pages are present.
3. **Quotations.** 20 segments, all MATCH with correct pages. Note 1 is attached to the Figure 2 caption (p. 5020), as the card says.
4. **Design and the counts R8 relies on.**
   - Design: two GoPro cameras in two hotels of one chain over 15 months, with 674 cases recorded (pp. 5015, 5020). The kiosk was down on two days, and those 51 customers were met by the worker (p. 5021). That left 623 customers who used the kiosk (p. 5021).
   - **The 13 (note 4, p. 5035).** Three kiosks were turned off, one could not read the ID card, eight could not find the reservation and one froze: 13 in all. "In all of these cases, upon encountering the problem, customers looked for a service worker who manually checked them in."
   - **The 86 of 610 (Figure 11, p. 5027).** The first attempt's cycles succeeded for 102, 228 and 194 customers (524). Attempts 2-4 succeeded for 63, 12, 2, 4, 2, 1 and 2 (86). The total is 610. R8's count is correct, and 524/610 = 85.9% agrees with the paper's "86%".
   - The key-facts heading "Failures the guest fixed alone" overstates, as does R8's report ("without any person"). The paper says "Occasionally, bystanders (e.g. other customers or service staff) would offer explicit verbal advice" during recognition (p. 5025), and it counts neither form of help among the 86.
5. **May say / may not say.** May say 1-4: LICENSED. For may say 4 the safer wording adds that bystanders, staff among them, occasionally advised (p. 5025). May not say 1-4: LICENSED.
6. **Bearing on K7 (P4) and K9.** I agree. Note 4 (p. 5035), the outage (p. 5021) and "In rare cases when customers approach the service worker, they will be redirected towards the self-registration kiosk" (p. 5022) bear the reading of demotion rather than removal.
7. **Reader's own inferences.**
   - The 86 of 610: supported (computed above).
   - "Power over the output is my gloss": open. The text says only "manually checked them in" (p. 5035). An account of what the worker could override would settle it.

## 9. lee2025robot

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - Crossref, re-fetched, gives *PLOS One* 20(11): e0333616, 4 Nov 2025, and the correction e0340212 in 21(1), 2 Jan 2026.
   - Crossref deposits the family names "Helen Lee" and "Grace Chan". PLOS's own citation line on p. 1 agrees with Crossref: "Helen Lee WH, Grace Chan SH, Tang BM, Song Z (2025)". The card's author field follows the byline instead. The publisher's form is the likelier one; the authors should choose.
   - The hash matches (13ff4cf5...).
2. **Read depth.** All 22 pages and the correction notice are present.
3. **Quotations.** 19 segments, all MATCH with correct pages.
4. **Design and statistics.**
   - Design: a retrospective cross-sectional survey, judgmental sampling through WeChat, in Macau (pp. 7-8); a seven-point scale (p. 6). Of 461 questionnaires sent, 330 were valid, 71.5% (p. 9).
   - Switching-intention item means are 2.870, 2.867 and 2.664 (Table 2, p. 10). Of the respondents, 245 of 330 were aged 18-30 (Table 3, p. 11).
   - H1: β = 0.136, p > 0.05 (p. 9); t = 1.959 (Table 6, p. 13). The R² of switching intention is 0.196 (Table 9, p. 16).
   - **The sign of H3.** I read the rendered p. 9. The text prints "(βCS→SW = 0.212, p<0.001)". Table 6 (p. 13) prints "−0.212***". The correlation in Table 5 (p. 12) is +0.254. The Discussion reads the effect as negative: "customers' positive satisfaction to robot service negatively reduces their switching intention" (p. 13). So does p. 11 ("the negative effects ... are realised through customer satisfaction"). The card is right on the text, the table and the correlation; it should add the Discussion.
   - Two of the card's "reporting faults" overstate. The H2a coefficient on p. 9 is legible in print; only its subscript wraps across a line ("βCT→CS = −0.228"). And t = 1.959 is non-significant at the 1.96 threshold, which makes it borderline, not a reporting fault.
   - The card misses one fault: the text says demographics are in Table 2 and descriptives in Table 3 (p. 9), but the tables are the other way round. The card cites them by their actual titles, correctly.
5. **May say / may not say.**
   - May say 1: LICENSED-NARROWER. Write: "In a judgmental WeChat sample of 330 people in Macau recalling a 'robot service' failure (a category that included telephone self-service, hotel check-in and financial recommendations, p. 8), Lee et al. (2025: 9, 13) found no significant direct effect of the failure on intention to switch to human-staffed service (β = 0.136, t = 1.959)".
   - May say 2: LICENSED.
   - May not say 1-3: LICENSED.
6. **Bearing on K9 and K7 (P4).** I agree: Lee et al. are a weak rival on K9 and give no evidence on P4. The outcome items ask about switching to human-staffed service (Table 1, p. 8), not about whom the respondent turned to during the failure.
7. **Reader's own inferences.** None beyond the critique.

## 10. min2020angry

**Verdict: PASS-WITH-NOTES**

1. **Identity.**
   - Crossref, re-fetched, gives DOI 10.61701/481433.50, *ICHRIE Research Reports* 5(1), 2020, by Min and Kim.
   - I re-fetched the Internet Archive capture of 9 Jul 2025 (HTTP 200, application/pdf). It is byte-identical (SHA-256 abe25cd9...). The cover sheet gives Volume 5, Issue 1, Article 2, 2020; the running head reads "Vol. 5, Iss. 1 [2021]". This matches the card.
   - **The authors' 2019 journal article (record only).** Endnote 1 (printed p. 3) reads: "This research report is based on the study conducted by Min, Joireman, and Kim (2019)". That study is "Understanding why anger predicts intention to complain among high but not low power customers: A test of competing models", *Journal of Business Research* 95: 93-102 (February 2019), doi 10.1016/j.jbusres.2018.10.017 (Crossref, 11 Nov 2026). I did not see it.
   - The report also cites a different article by the same two authors: Min and Kim (2019), "When service failure is interpreted as discrimination: Emotion, power, and voice", *International Journal of Hospitality Management* 82: 59-67, doi 10.1016/j.ijhm.2019.03.017 (Crossref verified). It is not the source the endnote names. Do not swap in the wrong one.
2. **Read depth.** All four PDF pages are present. The source is an archive capture, as disclosed.
3. **Quotations.** 12 segments, all MATCH. "Complain less in public" carries a capital that the card added; the source has "complain".
4. **Sample and statistics.** I confirm that the summary gives none. It has no N, no description of participants, no procedure beyond the three menu slogans and no test statistic or effect size. It says only "Through experimental designs using a failed service in the restaurant" (p. 1) and "Our experiment (restaurant name: Atena)" (p. 2).
5. **May say / may not say.**
   - May say 1: LICENSED-NARROWER. The source says "reducing an opportunity", not that the operator "lost the chance". Write: "Min and Kim (2020: 2) report that in their restaurant experiment participants in the low-power condition complained less in public, 'reducing an opportunity for the service provider to hear from customers'; the report gives no sample or statistics."
   - May not say 1-3: LICENSED.
6. **Bearing on K7 (P4).** I agree that it narrows. Passage: "customers feeling powerless are not comfortable making face-to-face complaints in the restaurant although they are very upset" (p. 2).
7. **Reader's own inference.** That "complain less in public" measured a stated intention: supported, so far, only by the title of the underlying article ("intention to complain", Crossref). Reading the article would settle it.

---

## Table: every FAIL, every quotation not MATCH, every sentence not LICENSED, and other errors to fix

| # | Card | Item | Finding | Fix |
|---|---|---|---|---|
| — | all | FAIL | None | — |
| 1 | manifest2001unipolaris | Quotation "no special steps" (critical notes, paras 30-31) | PARAPHRASED-AS-QUOTE | Para 31: "did not take any special steps" |
| 2 | page1972sloan | Quotation "depending,on the evidence ..." (key facts, 703) | OCR-DOUBT: the ',' is a speck on the scan, not print | Quote "depending on"; drop "so in the text" |
| 3 | page1972sloan | Quotation "depending,on the evidence offered at the trial" (critical notes) | OCR-DOUBT, as #2 | As #2 |
| 4 | rudyhiller2022epistemic | May say 1 | LICENSED-NARROWER: Holly Smith 2017 is cited against the view | "widely, though not universally, accepted ... at least completely (§2 ¶2, citing Holly Smith 2017 and Ross 1939 against)" |
| 5 | rudyhiller2022epistemic | May say 4 | LICENSED-NARROWER | Dispositionalists against occurrentism; the object is "the moral status of one's action" (§1.2 ¶7) |
| 6 | rudyhiller2022epistemic | May say 6 | LICENSED-NARROWER | "Rudy-Hiller, following Rosen, H. Smith and Wieland, distinguishes ..." (§3.4 ¶7) |
| 7 | manifest2001unipolaris | May say 4 | LICENSED-NARROWER: "held ... were negligent" | No Lord held negligence; Lord Scott said the dampers findings "go to negligence, perhaps gross negligence" (paras 118-119) |
| 8 | manifest2001unipolaris | May not say 1 (reason) | LICENSED-NARROWER | "Lord Scott, whose reasons Lords Steyn and Hoffmann adopted, said ..." (paras 1-2, 118-119) |
| 9 | manifest2001unipolaris | May not say 2; key-facts heading on para 117; hold rationale; R7 report (iv) | LICENSED-NARROWER and overreading: "bound to enquire" belongs to the privity test | Para 117 is about blind-eye knowledge; the speeches call the failures fault or negligence (paras 32-33, 119) |
| 10 | hormio2018culpable | May say 3 | LICENSED-NARROWER: stated of her example | Keep the ethos condition and the example (p. 17) |
| 11 | hormio2018culpable | May say 4 | LICENSED-NARROWER | Said of "knowable recognised unknowns" (p. 5) |
| 12 | gelbrich2011metaanalysis | May say 2 (second clause) | LICENSED-NARROWER | Cumulative satisfaction only; 28 service vs 4 non-service samples; no industry effect on transaction-specific satisfaction (p. 34) |
| 13 | gelbrich2011metaanalysis | K7 reading; R8 report | "employee's manner weighs more in services" conflates the response with the perception | "fair treatment (interactional justice) weighed more in services" (p. 34) |
| 14 | lee2025robot | May say 1 | LICENSED-NARROWER | Add the sample frame, the scope of "robot service" (p. 8) and β = 0.136, t = 1.959 |
| 15 | min2020angry | May say 1 | LICENSED-NARROWER: "lost the chance" | "'reducing an opportunity for the service provider to hear from customers'" (p. 2) |
| 16 | globaltech2011seb | `source_basis` cross-check claim | Two wording differences between the slip and the U.S. Reports were missed | "CEO" vs "chief executive officer" (770); "(1) the" vs "(1) The" (769); the quotations stand |
| 17 | page1972sloan | `source_basis` OCR list; authority note | 'testate' is printed so; Prosser § 71 is also cited (702) | Remove 'testate' from the OCR list; add Prosser |
| 18 | manifest2001unipolaris | Para 112 bullet | "adding 'I think that is dishonesty'" reads as Lord Scott's | "Lord Blackburn added ..." |
| 19 | xu2024disciplined | Key-facts heading "Failures the guest fixed alone"; R8 report "without any person" | Overstated: bystanders, staff among them, occasionally advised (p. 5025) | "mostly by the guest's own retrying; the paper gives no count of help" |
| 20 | lee2025robot | Author field; "reporting faults" | PLOS's own citation is "Helen Lee WH, Grace Chan SH"; the H2a "garble" is a line wrap; t = 1.959 is borderline, not a fault; the Discussion (p. 13) reads H3 as negative; the text swaps Tables 2 and 3 (p. 9) | Authors choose the name form; amend the critical note |
| 21 | hormio2018culpable | Version of record | The volume exists (APF 94, 2018, 189 pp.); the article and its pp. 7-34 are unverified and unseen | Keep "preprint" locators; no journal pages |
| 22 | rudyhiller2022epistemic | Year | Card 2022 vs R7's bibliography entry and the encyclopedia's citation, 2025 | The lead picks one |
| 23 | min2020angry | Swap target | Two 2019 articles exist | Swap for *JBR* 95: 93-102 (doi 10.1016/j.jbusres.2018.10.017), not *IJHM* 82: 59-67 |

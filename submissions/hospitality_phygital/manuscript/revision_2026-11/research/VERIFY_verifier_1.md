# Verification report: verifier_1 (rr-2026-11)

Date: 2026-11-08. Scope: 31 cards. What I checked:

- **Identity.** I re-fetched every Crossref record on 2026-11-08. For the AI Act I used EUR-Lex.
- **Abstracts.** I pulled them from OpenAlex, Semantic Scholar and Crossref, plus Consensus for Ariffin and Li et al.
- **Quotations.** I matched every quoted string, normalised for case, punctuation and line-break hyphenation, against the saved sources. Page locators come from pdftotext page breaks. Darwall's come from the OSO "(p.NN)" markers. Hohfeld's use journal page = PDF page + 15.
- **v4 sentences.** Every v4 sentence the cards quote is in `submitted.md`, word for word.

I edited no card. My working copies are in the session scratchpad.

---

## alfrink2023contestable
**PASS-WITH-NOTES**
- Identity: Crossref gives *Minds and Machines* 33(4), 613–639, online 13 Aug 2022. That matches the card. `references.bib` has no `number = {4}`, which is a minor gap.
- Depth: `article.txt` is the full article (about 11k words, §§1–8). The full-text claim is honest.
- Quotes: all 11 source quotes MATCH, with the right sections. §6.1.3, §6.1.4 ×3, §6.2.1 ×2, §6.2.5, §6.3 ("primarily performed by system developers", "During business and use-case development…") and §7 ("assumes no context", "duty of care…") all check out.
- Missing locators: the first and third bullets ("responsive to human intervention…", "contestability protects human self-determination…") carry no locator. The first is in the abstract and the third is in the front matter before §4.
- Support: I agree that Alfrink supports the content of stages 2–4 but not their order, and nothing in it supports stage 5. §6.3 says the practices "are primarily performed by system developers".

## ariffin2013generic
**PASS**
- Identity: Crossref gives IJHM 35, 171–179, Dec 2013. Card and bib match.
- Quotes: all 4 MATCH the abstract (Consensus record). OpenAlex and Semantic Scholar have no abstract, as the card says.
- Nothing is attributed beyond the abstract. I agree with the hold rationale.

## beatty2016compliance
**PASS**
- Identity: Crossref gives JSR 19(2), 158–173, online 30 Dec 2015. Matches.
- Quotes: all 4 MATCH the abstract (Crossref/OpenAlex).
- Support: I agree with YES for s.6 (employees assess requests, with "policy or legal" as a deterrent). I also agree with PARTIAL for s.2: the abstract covers the exception request only, not "turn down", "demand an explanation" or "challenge".

## bendoly2013realtime
**PASS-WITH-NOTES**
- Identity: Crossref gives JOM 31(1–2), 62–71, online 30 Jun 2012, print Jan 2013. Matches. Crossref now lists the publisher as Wiley.
- Quotes: all 3 MATCH the abstract.
- **Drafters' check (front-desk "sense of control"): I agree, NOT SUPPORTED at abstract level.** The abstract describes "a laboratory experiment" on "reservation agents" and their latitude "to accept rate bids below the pricing prescriptions". It is about how feedback regimes change that deviation and about agents' "perceptions of how their actions will be viewed by higher levels of management". It does not mention front-desk staff, guests, a guest's sense of control, or small acts of discretion toward guests.
- OpenAlex and Unpaywall list the paper as closed with no repository copy, so I could not check the full text. On present evidence the second v4 use ("Skilled front-desk employees often manufacture a guest's sense of control…") should be treated as a mis-citation until the full text shows otherwise. The first use (sanctioned latitude) is fully supported.

## bitner2000technology
**PASS-WITH-NOTES**
- Identity: Crossref gives JAMS 28(1), 138–149, 2000. Matches.
- Depth: metadata only, which is honest. Semantic Scholar says "the publisher elided the abstract". Its machine-generated TLDR describes technology "as an enabler of both employees and customers" in customising, recovering from failure and delighting. That fits the "tool" reading, but it is a TLDR, not an abstract, and cannot be cited. NOT CHECKABLE stands.

## brotherton1999towards
**PASS-WITH-NOTES**
- Identity: matches IJCHM 11(4), 165–173, 1999. **Factual error in `source_basis`:** it says Crossref gives "no issue in the returned fields", but Crossref returns `issue: 4`. There is no bib entry, which is fine because the card is rejected.
- Quotes: both MATCH the OpenAlex/Crossref abstract. The figure of 287 OpenAlex citations is confirmed.

## bulley2015ethics
**PASS-WITH-NOTES**
- Identity: Crossref gives *Hospitality & Society* 5(2), 185–201, 2015. The bib and the accepted manuscript give 5(2–3), as the card already notes.
- Depth: `oa0.pdf` is the full accepted manuscript (25 pp.). The full-text claim is honest.
- Quotes: all 4 MATCH with the right PDF pages (p. 3, p. 11 ×2, p. 15).
- Support for "…and so does what the host owes": I agree with PARTIAL, with one qualification. I searched for owe, duty, obligation and responsib. Besides international moral duties (p. 4), Bulley treats hospitality as ethics: "ethical responsibility-taking for others" (p. 7), and the abstract calls hospitality "a practice that continues once the guest crosses the threshold". So the ethics runs past the threshold in Bulley. A continuing *host obligation* in the commercial sense does not. The "owes" half is weakly grounded, not absent.

## chathoth2013coproduction
**PASS**
- Identity: Crossref gives IJHM 32, 11–20, Mar 2013. Crossref spells the authors "Prakash" and "Robert James" where the card has initials; this is trivial.
- Quotes: all 3 MATCH the abstract in the saved `ucf.html`. The figure of 481 OpenAlex citations is confirmed.

## christou2020tourists
**PASS-WITH-NOTES**
- Identity: Crossref gives IJCHM 32(11), 3665–3683, 2020. Matches.
- Quotes: all 5 MATCH the structured abstract.
- One point goes slightly past the abstract. The "Critical notes" say responses were given "during COVID-19 quarantine deployments", but the abstract names COVID-19 as the occasion, not as the setting of the interviews. I agree with PARTIAL support.

## coeckelbergh2019artificial
**PASS-WITH-NOTES**
- Identity: Crossref gives SEE 26(4), 2051–2068, online 24 Oct 2019, print Aug 2020. Matches. There is no bib entry, which is fine because the card is rejected.
- Quotes: all MATCH the abstract.
- **New finding that resolves the card's open question:** the full text is open access at Europe PMC (PMC7417397). I fetched the XML and searched it. It contains no "Darwall", "Strawson", "Hohfeld" or "second-person", and 12 uses of "answerab…". The gap statement ("none found that applies second-personal standing or Hohfeldian correlativity…") therefore holds for this paper. The card could be upgraded to full text from PMC.

## costanzachock2020design
**PASS-WITH-NOTES**
- Identity: Crossref gives type edited-book, MIT Press, 3 Mar 2020, and the title "Design Justice" only. The card already notes this.
- Quotes: quote 1 MATCHES. Quote 2 MATCHES, but its opening quotation mark is wrong: the card has `"Design justice' is…"` where the source has `“Design justice” is…`. Fix the punctuation before reuse.
- The book is OA (hybrid) but was not read. I agree that support is NOT CHECKABLE.

## darwall2013bipolar
**PASS-WITH-NOTES**
- Identity: Crossref gives a book chapter in *Morality, Authority, and Law* (OUP, 21 Mar 2013), pp. 20–39. Matches. There is no bib entry; the card is held.
- Depth: the full chapter is in the PDF. Honest.
- Quotes: all 15 MATCH with correct print pages. The pp. 31–32 quote straddles the "(p.32)" marker, which is correct. "cannot exist by itself" is on p. 27, also correct.
- **Earlier printing (card asked):** Crossref 10.1093/acprof:oso/9780199653492.003.0011 is "Bipolar Obligation" by Darwall, *Oxford Studies in Metaethics* vol. 7, issued 28 Jun 2012, pp. 333–358. It is the first printing; the 2013 collection reprints it. Choose one and use page loci from the version cited.
- Threats 1–2 (conferral; reachability is the authors' claim, not Darwall's): I agree on the text. Darwall p. 31 is the apology-in-the-diary passage.

## didomenico2007host
**PASS**
- Identity: Crossref gives *Leisure Studies* 26(3), 321–338, 2007. Matches; Crossref spells the name "Marialaura".
- Quotes: all 5 MATCH the OpenAlex abstract. The card notes the chapter title "Commercial Home Enterprises…" as not read.

## eu2024aiact
**PASS-WITH-NOTES, with one finding the authors must act on**
- Identity and depth: the OJ text of Reg. (EU) 2024/1689 is saved in full (144 pp.).
- Quotes: all 11 MATCH on the PDF pages given (pp. 54, 110, 123, 127). The card's reading of the *original* Art. 113 is accurate.
- **Drafters' check (amendments): the dates HAVE been amended.** The amending act is **Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI), OJ L, 2026/1744, 24.7.2026**, which entered into force on the third day after publication. Source: EUR-Lex, https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng, fetched 2026-11-08 (status "In force"). The changes that matter here:
  - Amendment point (40) replaces Art. 113(c): "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) **2 December 2027** as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and (ii) **2 August 2028** as regards … Article 6(1) and Annex I".
  - Point (40) also replaces Art. 113(a), adding new Art. 5 prohibitions from 2 Dec 2026. It adds point (d): Arts 102–110 apply from 27 July 2026.
  - **Art. 86 is not amended.** No amendment point mentions Article 86 or Chapter IX, and Chapter IX is not among the exceptions. On the text, Art. 86 still falls under the general date of **2 August 2026**.
  - Annex III is not amended. Art. 6(3) is not amended. Art. 6 gains new paras 1a–1c on safety components, which are irrelevant here.
  - **Interpretive caveat for the authors, not settled by me:** Art. 6, the classification rule, sits in Chapter III Section 1, which now applies to Annex III systems from 2 Dec 2027. Whether the Art. 86 right can be exercised for Annex III systems before the classification rules apply is therefore open. The manuscript should not say flatly that the right to explanation "applies from 2 August 2026" without a qualifier.
  - The card's "Article 6(1) … shall apply from 2 August 2027" is now superseded (2 Aug 2028).
- I did not see a consolidated text. The card's `check-amendments` flag was right; it can now be resolved as above.

## filippas2022inflation
**PASS-WITH-NOTES**
- Identity: Crossref gives *Marketing Science* 41(4), 733–745, 2022. Matches.
- Quote: the one-sentence abstract MATCHES.
- **Goes beyond the abstract (rule 5):** "the platform studied (a labour marketplace, not lodging)" is not in the one-sentence abstract. Remove it or source it.

## fuller1991consumers
**PASS**
- Identity: Crossref gives WES 5(1), 1–16, 1991. Matches.
- Quotes: both MATCH the abstract.
- Support: I agree that the "sense of control" sentence is NOT CHECKABLE and doubtful at abstract level.

## garcia2026strategic
**PASS-WITH-NOTES**
- Identity: Crossref gives *Management Science* 72(1), 609–626, Jan 2026. Matches the card and bib.
- Depth: the CESifo WP 10849 (Dec 2023) is saved in full. Line 105 reads "accepted for publication in Management Science".
- Quotes: all 7 source quotes MATCH on the WP PDF pages given (p. 4 ×2, p. 5, p. 7 ×2, p. 14 ×2).
- **Drafters' check (working paper vs published version):**
  - The version of record is open access under CC BY. Unpaywall and OpenAlex give an OA date of **16 Apr 2024** (Articles in Advance) and list SSRN 4676767 as the accepted version.
  - pubsonline.informs.org served a Cloudflare challenge and I did not bypass it.
  - The two abstract quotes ("price setting frictions…", "in equilibrium…") appear verbatim in the version-of-record abstract that Crossref holds. The body quotes (35 days, 0.72, "final decision right", footnote 5) remain unchecked against the version of record.
  - Inconsistency in the card: `read_depth: full-text` sits beside the flag `abstract-only-debt`. The correct state is full text of the working paper, version of record not read.
  - The year is right: print 2026 (online 2024).
- Support: I agree with YES, YES and WEAK. The manager "retain[s] the final decision right" (PDF p. 5), so the source does not back "sets the price".

## goodwin1992consumer
**PASS-WITH-NOTES**
- Identity: Crossref gives JBR 25(2), 149–163, Sep 1992. Matches. **Crossref has no abstract**; the abstract comes from Semantic Scholar. The `source_basis` wording "publisher-deposited record (Crossref/…)" is inaccurate for this source.
- Quotes: all 3 MATCH the Semantic Scholar abstract.
- **Drafters' check:** I agree that Goodwin does NOT support "Voice offered after a decision was taken, with the decision explicitly unchanged, still raised… both procedural and outcome fairness".
  - The design manipulates outcome × apology × voice × service type. It manipulates neither the timing of voice relative to the decision nor an explicitly fixed decision.
  - Voice raised fairness "in the 'favorable outcome' condition". "When no tangible offering was made, apology and voice had lesser effect and in some instances were associated with lower perceptions".
- I disagree with the flag `claim-contradicted`. The study does not test the v4 claim's condition, so "not supported" is the accurate label, not "contradicted".
- The card says Goodwin supports the next v4 sentence ("An invitation to speak that was never going to bear on anything lowers those judgments instead of raising them"). That holds only in part. The abstract says "lesser effect" and only "in some instances" lower, and "no tangible offering" is not the same as voice that "was never going to bear on anything".

## golubovskaya2017meaning
**PASS**
- Identity: Crossref gives IJCHM 29(5), 1282–1304, 2017. Matches.
- Quotes: all 3 MATCH the structured abstract.
- The two CORE files are 5,439-byte challenge pages, which confirms the card's account.

## gursoy2026reconceptualizing
**PASS-WITH-NOTES**
- Identity: Crossref gives JHMM 35(2), 151–165, online 6 Jan 2026. Matches. Crossref has no abstract; the quotes MATCH the Semantic Scholar abstract (boilerplate `source_basis` again).
- Support: I agree with YES and YES at abstract level.

## hohfeld1913fundamental
**PASS**
- Identity: Crossref gives YLJ 23(1), first page 16, Nov 1913. The 44-page scan supports pp. 16–59.
- Quotes: all MATCH the Wabash transcription. In the Commons scan they sit on the journal pages the card gives (pp. 30, 31, 32, 33). The PDF misses are OCR noise only ("isunder", straight vs curly quotes).
- Governor note: I agree that Hohfeld gives correlativity, not reachability.

## introna2010measure
**PASS-WITH-NOTES**
- Identity: Crossref gives *AI & Society* 25(1), 93–102, online Nov 2009, print Apr 2010. Matches.
- Depth: metadata only, which is honest; OpenAlex and Semantic Scholar elide the abstract. The machine TLDR mentions "decentering … anthropocentric ethics". That is not usable as an abstract, but it is consistent with the machine-as-guest reading. NOT CHECKABLE stands.

## ivanov2019ultimate
**PASS**
- Identity: Crossref gives ZfTW 11(1), 25–43, 2019. Matches. There is no bib entry; the card is held.
- Quote: MATCHES the Crossref abstract. I agree with conjecture-only.

## jung2019undermining
**PASS**
- Identity: Crossref gives JSTP 29(2), 213–231, 2019. Matches.
- Quotes: all 3 MATCH. Support: I agree with YES.

## kong2026delegation
**PASS**
- Identity: Crossref gives *AI and Ethics* 6(5), art. 518, online 14 Sep 2026. Matches. There is no bib entry; the card is held.
- Quotes: all MATCH the Crossref abstract.

## kropf2026blame
**PASS-WITH-NOTES**
- Identity: Crossref gives IJSR 18(2), art. 30, Feb 2026, authors Kropf, Spöck, Werner. Matches.
- Quotes: all 5 MATCH the Crossref abstract.
- The card does not assess the sentence v4 already prints. Section 2 reads: "Kropf et al. (2026) argue that a robot can hold the role responsibility of a carer without being a moral agent, and even they hold that recognizing this narrows the responsibility gap without displacing human accountability." It is supported at abstract level.

## lariviere2017service
**PASS-WITH-NOTES**
- Identity: Crossref gives JBR 79, 238–246, Oct 2017, eight authors. Matches.
- Second-hand quotes: both MATCH `sources/odekerken2021service/oa1.pdf`, PDF p. 3.
- Semantic Scholar lists the paper as BRONZE OA on ScienceDirect, but it returned 403 to me. Its TLDR ("changing interdependent roles of technology, employees, and customers") is consistent with the card. Support verdicts stand.

## lee2019procedural
**PASS-WITH-NOTES**
- Identity: Crossref gives PACM HCI 3(CSCW), 1–26, 2019, with the short title. Matches.
- Quotes: 4 MATCH.
- **One PARAPHRASED-AS-QUOTE:** the card has "brings human elements into final decision-making", but the source reads "by bringing human elements into final decision-making".
- Support: I agree with PARTIAL. The abstract supports control by the group itself ("adjust the algorithmic allocations as a group"), not a reachable person who can reverse the decision.

## li2021systematic
**PASS**
- Identity: Crossref gives IJHM 95, 102930, May 2021. Matches.
- Quotes: all 4 MATCH the abstract (Consensus record).
- Support: I agree with YES for both sentences.

## lind1990voice
**PASS-WITH-NOTES**
- Identity: Crossref gives JPSP 59(5), 952–959, 1990. Matches. Crossref has no abstract; it comes from Semantic Scholar.
- Quotes: all 4 MATCH. The source's "preand" is a hyphenation artefact.
- The Figshare record is confirmed to be metadata only (`files: []`).
- **Drafters' check:** the support is PARTIAL, as the card says.
  - The abstract supports post-decision voice producing "higher fairness judgments than no voice".
  - "Explicitly unchanged" is not in the abstract.
  - Nor does the abstract say that *both* procedural and distributive judgments rose under post-decision voice. "distributive and procedural fairness judgments" names the dependent measures in the study description, and the result sentence says only "higher fairness judgments". The card cites that phrase as if it were a result, which overstates it slightly.
  - The full text is needed for the "explicitly unchanged" condition and the per-measure results. A web search found secondary descriptions but none confirming the instruction given to post-decision subjects.
- Combined verdict on the v4 sentence: as cited to Lind et al. 1990 and Goodwin and Ross 1992, it is supported only in part, by Lind alone, at abstract level. Goodwin should come off this sentence.

## liu2026hospitableness
**PASS**
- Identity: Crossref gives IJHM 135, 104640, May 2026. Matches. Crossref has no abstract; the quotes MATCH the OpenAlex abstract, which the card labels correctly.
- Support: I agree with YES, and with the point that "test" is off for an interview-based construct study.

---

## Summary table: FAILs and quotes that are not MATCH

| Card | Item | Status | Note |
|---|---|---|---|
| (none) | — | FAIL | No card failed. |
| lee2019procedural | "brings human elements into final decision-making" | PARAPHRASED-AS-QUOTE | Source: "bringing human elements into final decision-making" |
| costanzachock2020design | "Design justice' is an approach…" | MATCH (punctuation wrong) | Source: “Design justice” is an approach… |
| alfrink2023contestable | "responsive to human intervention…", "contestability protects human self-determination…" | LOCATOR MISSING | In the abstract and the front matter before §4 respectively |

Other matters for the drafters, outside the table:
- eu2024aiact: Reg. (EU) 2026/1744 moved the Annex III high-risk dates to 2 Dec 2027. Art. 86 itself is unamended.
- Remove Goodwin and Ross 1992 from the "explicitly unchanged" sentence.
- The Bendoly front-desk citation is unsupported.
- Errors and inconsistencies inside cards: the Brotherton `source_basis` wrongly says Crossref gives no issue; the Garcia read_depth contradicts its flag; the Filippas card goes beyond the abstract; the `source_basis` for Goodwin, Lind and Gursoy wrongly names Crossref as the source of the abstract.

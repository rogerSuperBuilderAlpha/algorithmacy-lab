<!-- Drafted by Claude (Opus 5.5), verification agent, run rr-2026-11-h, 10 Nov 2026. None of this is the authors' wording. No card or other file edited; nothing committed. -->

# VERIFY_H_v3: verification of the H1 cards and the H1 synthesis

Verifier: Claude (verification agent), 10 November 2026. I followed `VERIFY_BRIEF.md` with the run-specific changes I was given. I edited no card and committed nothing. This report is the only file I wrote.

**Scope.** I checked 18 new cards in full. For the 4 upgraded cards I checked only the material added in rr-2026-11-h. I also checked every quotation and locator that `WS_H1_origin.md` (WS) attributes to a source, and whether each synthesis claim follows from the cited text. v4 = `manuscript/DRAFT.md`; PO = `manuscript/revision_2026-11/PITCH_AND_OUTLINE.md`.

**Method.**
- *Quotations.* A normalising matcher ignores whitespace, hyphenation, ligatures, case, punctuation and the long s. I read every hit in context and mapped it to the printed page from the running heads (Bogen: HeinOnline footers; Sandoval-Strausz: running heads; Maese: running heads; Shryock: `paged.txt`).
- *Old reports, against page images.* I fetched the Internet Archive page images for Calye's Case (Coke 1777, leaves n262, n264, n265) and Lane v Cotton (12 Mod 1769, leaves n499, n500) and read the quoted passages on the scans. The scans are in the session scratchpad (`vh3/img/`), not in `sources/`.
- *Statutes.* legislation.gov.uk returned HTTP 202 with an empty body to me too, so I could not confirm the live text. For HPA 1956 s 1, I fetched an independent capture of the **as-enacted** text (Wayback, 9 Sep 2023). Its s 1(1)–(3) wording is identical to the card's revised-version capture. To test two legal statements in WS, I also read UCTA 1977 s 2, CRA 2015 s 65 and HPA 1956 s 2 from Wayback captures.
- *Heart of Atlanta.* The LoC U.S. Reports PDF and Justia returned 403, and CourtListener's API needs authentication. I re-located every quotation in the saved CAP text using its star paging (`*260`, `*261`, `*284`, `*285`), which comes from the official reports, and in the saved LII text. I did not reach a U.S. Reports page image.
- *Identity.* I re-fetched Crossref for every DOI and OpenAlex for Bogen, Ganesh and the Lashley chapter. The *In Search of Hospitality* year comes from Open Library edition records. Calye's Case in the English Reports (77 E.R. 520) was **not** read, because CommonLII returned a Cloudflare challenge. Bogen n. 131 (p. 75) cites it as "77 Eng. Rep. 520, 521 (1584)", which agrees with the card.

**Totals (22 cards).** 10 PASS, 12 PASS-WITH-NOTES, 0 FAIL. One quotation has a wrong locator (Lane, "If the Inn be full", p. 485, not p. 484). The synthesis has three substantive problems; see §C.

---

## A. New cards

### uk1956hotel: PASS-WITH-NOTES
- **Identity.** Hotel Proprietors Act 1956 c. 62, s 1. The text of s 1(1)–(3) matches both the card's capture (8 Jun 2026, revised) and my independent as-enacted capture (9 Sep 2023). The as-enacted rendering garbles s 1(3) ("held out by-the as offering"); the revised text reads "held out by the proprietor as offering", as the card has it. The live site was unreachable (HTTP 202) to me as well.
- **Quotations.** All 4 MATCH. The s 1(1) wording "and shall not attach to any other person" is exact.
- **Note on use.** In context, s 1(1) deems a hotel, "and any other establishment shall not", to be an inn. "Shall not attach to any other person" therefore excludes keepers of other establishments from innkeeper status. It does not allocate the duty among owner, brand and operator, which the card's critical note itself concedes. WS §5 reads more into the clause; see §C, S8.
- **Not read: HPA s 2.** Section 2(3) caps the proprietor's strict liability for goods (£50 per article, £100 in aggregate) unless the property was lost through the default of the proprietor or a servant, or was deposited for safe custody. This bears on WS's "no negotiated exception" (S3).

### calye1584case: PASS-WITH-NOTES
- **Quotations.** All 6 MATCH, and I confirmed each on the page images. The folios are right:
  - 32a: "if a man be lodged with another…", on the opening page of the case, headed "Part VIII. 32".
  - 32b: "passengers and wayfaring men".
  - 33a, headed "33": "bound in law to keep them safe…", "default in him or his servants", "the fault is in the guest".
  - 33b, the verso of 33: "the innholder ought to keep the goods and chattels of his guest, and not his person".
- **OCR repair.** The print has a damaged "un'eſs". The card's "[unless]" is the right repair.
- **ER not read.** Bogen n. 131 (p. 75) cites the case as "77 Eng. Rep. 520, 521 (1584)".
- **Scope of "and not his person" (the brief's main question).** On the scan, the passage is a construction of the writ against hostelers. The words *bona et catalla* "restrain the latter words to extend only to moveables". The report continues: "therefore by the latter words, if the guest be beaten in the inn, the innkeeper shall not answer for it… and yet in such case of battery, *hospiti damnum evenit*, but that is restrained by the former words" (33b).
  - What Calye holds is that the strict, custom-of-the-realm liability enforced by that writ covers the guest's moveables and not injury to the person.
  - It does not hold that the innkeeper owed no duty for the guest's person under any other action.
  - Two of H1's own held sources say innkeepers were answerable for the guest's person:
    - Bogen p. 82 n. 160: "While innkeepers were liable for third-party injuries done to their guests…".
    - Maese p. 499, citing Beale 1906: the innkeeper was obliged to "exercise reasonable care in the protection of the guest" and "protect the guest from injury by third parties". Her n. 166 adds that he "was not the insurer of his guest's safety", but had "the duty to protect his guests… through reasonable means".
  - The card's critical note ("In 1584 it did not [include a duty to take reasonable care for the guest's safety]") and its summary ("only goods, not the guest's person") therefore state Calye's holding on the writ as a general rule. The hold_rationale states it correctly ("confines the innkeeper's *strict* duty to goods").
  - Suggested wording: "the innkeeper's strict liability under the custom of the realm extended to the guest's goods, 'and not his person' (fol. 33b)".

### lane1701cotton: PASS-WITH-NOTES
- **Whose opinion.** Every quotation is Holt CJ's, and Holt was dissenting. The report gives the majority first: "Turton, Powis and Gould were of Opinion the Action did not lie against the Master" (12 Mod 481). Holt's opinion then opens "Holt C. J. cont." (contra). The card says so in its Summary and Critical notes. Its `title` ("…, Holt CJ") and `authors` ("Holt, John") still present the report as Holt's. Readers of the frontmatter alone would miss the dissent.
- **Quotations.** I checked all 5 against the scans.
  - "[eo ipso]": MATCH. The scan reads *eo ipso*, so the repair is right.
  - "where his House is not full": MATCH. The scan reads "his"; "bis" is an OCR error.
  - The smith ("made Profession of a Trade…") and "denied by Mr. Attorney and my two Brothers": MATCH, p. 484.
  - **"If the Inn be full, or the Carrier's Horses loaden, the Action would not lie… to serve the Publick": LOCATOR-WRONG.** On the scan, p. 484 ends at "refuse to take in a Letter, or any", and p. 485 (headed "Term. Pasch. 13 W. III. 1701. 485") begins "any other Thing proper to be sent by Post?…". "If the Inn be full…" follows on p. 485. WS §4 repeats "p. 484" for this quotation.
- **Year.** The report heads the term "Pasch. 13 W. III. 1701". Bogen n. 9 (p. 52) cites the case as "88 Eng. Rep. 1458, 1462-65 (1702)". The card's 1701 follows the report; the ER date was not checked.
- **"1 Ld Raym 646"** is unverified; the card labels it not read.

### heartofatlanta1964motel: PASS-WITH-NOTES
- **Identity.** 379 U.S. 241 (1964). Clark J wrote for the Court; Black, Douglas and Goldberg JJ concurred.
- **Quotations.** All 3 MATCH in both the CAP and the LII text.
  - p. 260: the Civil Rights Cases quotation (CAP `*260` precedes it, `*261` follows).
  - p. 261: "These laws but codify…" (after `*261`).
  - p. 284: "must stick to his bargain", in Douglas J's concurrence quoting S. Rep. No. 872 (between `*284` and `*285`).
- **Caveat.** Pages are confirmed by CAP star paging only. The official U.S. Reports PDF was not reachable.
- **Cross-reference.** The card's pointer to Sandoval-Strausz pp. 89–91 checks out: the travel rationale and Heart of Atlanta are discussed on pp. 89–91 (n. 53 cites 379 U.S. 252–53, 256, 260–).

### us1964civilrights: PASS-WITH-NOTES
- **Quotations.** All 3 MATCH against LII § 2000a(a)–(b).
- **Missing condition.** The § 2000a(b) chapeau makes an establishment that "serves the public" a place of public accommodation only "if its operations affect commerce, or if discrimination or segregation by it is supported by State action". The card's Summary and the WS §4 "Into public-accommodation law" paragraph omit that condition. Add it in any sentence stating scope.

### uk1957occupiers: PASS-WITH-NOTES
- **Quotations.** All 3 MATCH (s 2(1), 2(2), 2(4)(b)).
- **Legal statement broader than the authority.** The card says s 2(1) "allows the duty to be varied 'by agreement'", and WS calls this "a general power". Section 2(1) applies only "in so far as he is free to" vary the duty. Two statutes limit that freedom:
  - UCTA 1977 s 2(1): a person "cannot by reference to any contract term or to a notice… exclude or restrict his liability for death or personal injury resulting from negligence".
  - CRA 2015 s 65(1) bars the same in consumer contracts. Section 65(4)(c) names "the common duty of care imposed by the Occupiers' Liability Act 1957".

  For a hotel guest, then, the safety duty cannot be contracted out of for personal injury.

### uk2010equality: PASS
All 2 quotations MATCH, s 29(1) and s 29(7)(a), from the Wayback capture of 1 Nov 2026. The critical notes are fair.

### uk2015payment: PASS-WITH-NOTES
- **Quotations.** All 4 MATCH. The bracketed "[United Kingdom]" is the amended text (F1, SI 2019/661), and the elided list of grounds is correctly marked.
- **Wyman citation.** The quotation from wyman1904law p. 156, "sell or not as one pleases", MATCHes.
- **Overstatement.** "Statute now gives consumers a regulated claim to be served" goes beyond regs 18–19, which forbid discrimination and fix the features of a basic account. The card's next bullet concedes as much. Keep the second bullet and drop the first phrase.

### us1986emtala: PASS
- **Quotations.** Both MATCH (§ 1395dd(a), (b)(1)).
- **Note for WS §4 Q4.** WS writes "a US hospital emergency department must screen". The duty binds participating (Medicare) hospitals, which the card's Summary says.

### bogen1996innkeeper: PASS-WITH-NOTES
- **Identity.** OpenAlex gives the title, the author (David Skillen Bogen), *Utah Law Review* 1996(1) and DOI 10.63140/561cf826ek. The DOI resolves to `dc.law.utah.edu/ulr/vol1996/iss1/2`. The printed pages are 51–92 (HeinOnline footers).
- **Quotations.** All 11 MATCH, at the right pages:

  | Quotation | Page |
  |---|---|
  | "no express promise…", "element of the status", "product of duties imposed", "tautology" | 52 |
  | "concern for criminal activity" | 53 |
  | "not the innkeeper's express commitment" | 75 |
  | "heirs to a medieval tradition…", "not free" | 76 |
  | Chamberlaine paraphrase | 88 |
  | "innkeeping was not a monopoly" | 89 n. 192 |
  | Eyre J in Newton v Trigg | 90 |
  | "incidental…", "main significance…" | 91 |

  "Holt's characterization came at least a century after…" is at p. 52 n. 9.
- **Minor.** The Chamberlaine passage is anchored at n. 183, "Id. at 843", that is 81 Eng. Rep. 843; the case begins at 842 (1623). The card says "81 Eng Rep 842".
- **Not used by the card.** Bogen p. 82 n. 160, "innkeepers were liable for third-party injuries done to their guests", matters for the Calye point above.

### sandovalstrausz2005travelers: PASS
- **Identity.** Crossref matches (LHR 23(1), 53–94, 2005).
- **Quotations.** All 10 MATCH at the stated pages.
  - The cross-page quotation "Underlying all common law protections… special legal status" runs from p. 62 to p. 63, with n. 14 and the page foot intervening. MATCH.
  - "bed, board, and hearth", "not at liberty", "(This rule was not absolute…" and n. 15 (Singer) are all on p. 63.
  - "answerable not only…" is on p. 65, "not 'rights'" and "Innkeeping is defined…" on p. 66, "travelers enjoyed privileges…" on p. 68, and "its duties and privileges had to be turned into rights" on p. 54.
- **Gloss.** The card's "hearth is custody of property (p. 65)" is accurate: "safeguard the property of guests (that is, to offer them a metaphorical 'hearth')".

### burdick1911origin: PASS-WITH-NOTES
- **Identity.** Crossref matches (Colum. L. Rev. 11(6), 514; the text ends at p. 531).
- **Quotations.** All 7 MATCH.
  - The cross-page quotation ("It was because a person held himself out… lack of care") begins on p. 515 and ends on p. 516, with footnotes 7–11 between. MATCH.
  - Blackstone p. 518; "safe to believe" p. 522; "now attached only…" p. 523; "Generally speaking…" p. 524; Schouler at p. 524 n. 45. All correct.
- **Misdating.** The card's critical note says p. 523 shows the position "by the twentieth century". In context, Burdick's "now" refers to the period after the action of assumpsit developed. That is when "the liability of the common surgeon, the common tailor, the common farrier, etc., was no longer recognized" (p. 523), not 1911. WS quotes the line correctly but should not date it.

### wyman1904law: PASS
- **Identity.** Crossref matches (Harv. L. Rev. 17(3), 156; the text ends at p. 173).
- **Quotations.** All 5 MATCH: p. 156; p. 159 ×3, with "[shall]" and "[choose]" correctly repaired; p. 161.

### maese2015rethinking: PASS
- **Identity.** I ran the Crossref query that the drafter skipped. Crossref gives Maese, *Texas A&M J. Prop. L.* 2(3), 481–509, April 2015, which matches the card.
- **Quotations.** All 4 MATCH: p. 501 ×2 and p. 503 ×2.
- **For the Calye question.** Maese p. 499 (with n. 166, citing Beale) states a historical duty to protect the guest from third parties. The card does not use it.

### ogorman2009origins: PASS
- **Identity.** Crossref matches (IJCHM 21(7), 777–790).
- **Quotations.** All 5 MATCH at the stated author-version pages: pdf p. 4 and pdf p. 11 ×4.
- **Critical note confirmed.** On pdf p. 11 the "protection, sanctuary and security" sentence follows sentences on revenue and status and cites nothing.

### ganesh2018wirtbarkeit: PASS-WITH-NOTES
- **Identity.** Crossref matches (*Legal Theory* 24(3), 159–190).
- **Quotations.** Both MATCH the OpenAlex abstract.
- **Beyond the abstract.** The Summary says Ganesh reads Kant "by analogy to the Roman and common law of innkeepers". The abstract names the *Digest of Justinian* and "the private law of innkeeping". "Common law" is not in it. Write "Roman and private law" until the article is read.

### king1995what: PASS
- **Identity.** Crossref matches (IJHM 14(3–4), 219–234).
- **Quotations.** Both MATCH the abstract (Consensus record, re-fetched).
- **Note for WS.** The abstract says health-care organisations prompted the paper. The paper itself "reviews the literature of hospitality and proposes a model of hospitality" with implications "in a customer service organization". The card states this correctly. WS §4 Q4 goes further; see S9.

### telfer1995hospitableness: PASS
Crossref matches the article (*Philosophical Papers* 24(3), 183–196) and the chapter (pp. 38–55, Crossref 2001). The card attributes nothing to Telfer.

## B. Upgraded cards (rr-2026-11-h material only)

### lashley2000towards: PASS-WITH-NOTES
- **Identity.** Crossref and OpenAlex confirm DOI 10.1016/b978-0-7506-5431-9.50005-6, pp. 1–17 and issue year 2001.
- **Lashley year (2000 vs 2001).** Both dates are real. Open Library has two works: the first edition (ISBN 0750645628, Butterworth-Heinemann, first published 2000) and a 2001 printing (ISBN 0750654317). The DOI's ISBN stem, 0-7506-5431-9, is the 2001 printing. The card's year 2000 is right for the first edition, but the DOI and the pages 1–17 come from the 2001 record. Pick one edition:
  - 2000 without this DOI, with the pages checked in that edition; or
  - 2001 with the DOI and pp. 1–17.

  Then apply the same choice to the Telfer and Brotherton chapters.
- **Stale page ranges.** `references.bib` (`pages = {1--16}`) and the v4 reference list (DRAFT.md l. 296, "pp. 1–16") still carry 1–16.
- **The two warnings.** I agree with both: the PO §2.1 "Lashley (2000) holds…" sentence is second-hand, and the summary and `four-criteria` are unsupported.

### germannmolz2026: PASS
- **Identity.** Crossref re-fetched: H&S 16(1), 63–82, 1 Mar 2026. Crossref files the author under family name "Molz", given name "Jennie Germann". The card's "Germann Molz" is the standard form.
- **Quotations.** All 3 new quotations MATCH the Crossref abstract.
- **Note on v4.** v4 l. 17 ("visible, disciplined, and finally dispensable") paraphrases the abstract's "visibilizing, (self-) disciplining and erasing hosts". It omits the second, positive reading that the card flags.

### shryock2012breaking: PASS-WITH-NOTES
- **Quotations.** All 5 new quotations MATCH.
  - S22 (Pitt-Rivers); S23 ("True hospitality is not political"); S31 ("never confuse karam…"; "right of temporary sojourn").
  - The cross-page quotation: "reluctant to sort out…" is on S30, the page foot intervenes, and "depersonalized, formulaic, monetized…" is on S31. MATCH.
- **The upgrade note overstates.** It says Shryock "characterises the host-guest relations of that sphere as 'depersonalized…'". The sentence's subject is "Philosophers and storytellers, who… have been reluctant to sort out the details of commerce and nationalist politics as modern platforms for hospitality, *perhaps because* the relations… in these spheres are depersonalized…". So the characterisation:
  - is hedged ("perhaps because");
  - is offered as a reason for the philosophers' reluctance;
  - covers commerce and nationalist politics together.

  The quotation itself is reproduced with "perhaps" intact; only the gloss overstates.
- **Truncated quotation (earlier run, but WS relies on it).** The S30 quotation "The answers, obvious to us now, are provided by the hospitality industry (the market in hotels, restaurants, and other sites of temporary accommodation)" stops mid-sentence. Shryock continues "and the government bodies that control immigration and naturalization…". He hands the care of strangers to the industry *and* the state. The card and WS §4 Q5 drop the state without an ellipsis. PO §2.1 ("The modern holder is the industry… (S30)") inherits the narrowing.

### brotherton1999towards: PASS
Crossref confirms the chapter: "Hospitality and hospitality management", *In Search of Hospitality*, pp. 134–156, 2001, single author "BROTHERTON, B". The note is accurate.

---

## C. WS_H1_origin.md: quotations, locators and inferences

**Quotations.** Every quotation WS attributes to a carded source MATCHes, with one locator wrong: Lane "If the Inn be full…" is at 12 Mod **485**, not 484 (WS §4 Q1). I did not check the Q5 abstract-level quotations from uncarded sources (Blain & Lashley, Lashley 2014/2015/2008, Poulston, Ramdhony), nor liu2026hospitableness or golubovskaya2017meaning, which are outside my list.

**Inferences and legal statements**

| # | WS location | Claim | Finding |
|---|---|---|---|
| S1 | §2 Calye row; §4 Q1 "What the old duty left out"; §5 "Thin in content"; §5 Net | "The 1584 duty did not include the guest's safety"; "It did not cover the guest's body"; "A duty to protect the guest's person is a later addition"; "do not claim the legal duty was a duty… of personal safety" | **Broader than the authority, and contradicted by held sources.** Calye construes the writ's strict liability as reaching moveables only (fol. 33b, "restrained by the former words"); it is not a general rule about the person. Bogen p. 82 n. 160: "innkeepers were liable for third-party injuries done to their guests". Maese p. 499 (citing Beale): duty to "exercise reasonable care in the protection of the guest" and "protect the guest from injury by third parties". Maese p. 503 describes modern US law and does not say the duty is "later". Fair form: the innkeeper's *strict* liability covered goods, not the person (Calye, fol. 33b). Whether, and since when, a negligence-based duty to protect the person existed is a separate question, which Bogen and Maese answer yes for at least the medieval and Beale-era law |
| S2 | §5 Position C | duties "fixed by law rather than by contract" [bogen1996innkeeper, pp. 52, 90; maese2015rethinking, p. 501] | **Misattributed quotation.** The phrase is Maese's (p. 501). Bogen p. 90 has Eyre J's "do not deal upon contracts as others do"; p. 52 has "element of the status". Cite the phrase to Maese only |
| S3 | §4 Q4 | "The innkeeper's duty contains no negotiated exception." | **Contradicted.** Calye fol. 33a: if the innkeeper asks the guest to lock goods in a chamber "and then he will warrant them, otherwise not", and the guest does not, "the innkeeper shall not be charged, for the fault is in the guest" (card quotes this). HPA 1956 s 2(3) caps liability for goods unless the goods were deposited, or offered for deposit, for safe custody. Both are conditions the host can set, close to a negotiated exception |
| S4 | §4 Q4 | Occupier's power to vary "by agreement" is "a general power" | **Legal statement broader than the authority.** OLA s 2(1) applies "in so far as he is free to"; UCTA 1977 s 2(1) and CRA 2015 s 65(1), (4)(c) bar excluding liability for death or personal injury from negligence, including the common duty of care |
| S5 | §4 Q1 | "On one point the four agree… the duty belonged to a status" | **Inference presented as the sources' claim.** Only Bogen says it (p. 52; p. 90 via Eyre J). Burdick, Wyman and Sandoval-Strausz do not state it in the passages read |
| S6 | §4 Q1 | "By the eighteenth century the courts stated the activation as a profession or holding-out. Holt CJ put it…"; "Holt said 'If the Inn be full…'" | **Dissent presented as the court's.** Both quotations are from Holt CJ dissenting (§2 of WS says so; §4 does not). Write "Holt CJ, dissenting" |
| S7 | §4 Q5 | Shryock "hands the care of strangers to 'the hospitality industry'… then describes host–guest relations in that sphere as 'depersonalized…'" | **Truncation and hedge dropped.** S30 continues "and the government bodies that control immigration and naturalization"; the S30–S31 sentence is a hedged ("perhaps because") account of why philosophers avoid commerce *and nationalist politics*. The karam sentence (S31) is accurate |
| S8 | §5 Position A | HPA s 1(1) shows "Control and holder can come apart" | **Inference beyond the text.** s 1(1) moves innkeeper status to hotel proprietors and away from keepers of other establishments; it says nothing about control of premises or about owner/brand/operator splits (uk1956hotel card concedes "who is 'the proprietor' is a question the Act does not settle") |
| S9 | §4 Q4 | King 1995 is "the field's most cited source for the host's obligation" and "was written about hospitals adopting hospitality" [abstract] | **Beyond the abstract.** The abstract says health-care organisations *prompted* the question. The paper reviews "the literature of hospitality" and proposes a general model. "Most cited source for the host's obligation" is not shown by anything read |
| S10 | §2 Sandoval row; §4 Q1 | Sandoval-Strausz "disagrees with Singer's public-calling ground [p. 63 n. 15]" | **Overstated.** n. 15: "I agree with Singer's normative argument and recognize the existence of public callings, but the historical record indicates that travelers and strangers did indeed have a special status." He disputes the history, not the public-calling ground as such |
| S11 | §6 table, R3.10 | "lien" from uk1956hotel; sandovalstrausz2005travelers p. 63 | **Not in the cited text.** HPA s 1 and Sandoval p. 63 say nothing of a lien. A lien appears at Maese p. 503 and in Eyre J at Bogen p. 90 ("detain the persons of the guests… till payment"); HPA s 2(2) mentions the lien only to exclude vehicles and animals from it |
| S12 | §4 Q4 item 1 | Burdick p. 523 "now attached only…" | Quotation accurate. If the paper dates it, "now" is the post-assumpsit period (early modern), not 1911 |
| S13 | §4 Q1 | "the guest's presenting… the parties' rights… 'at once fixed by law'" from Maese | Accurate, but Maese is a student note relying on Beale (1906); WS says so. No change needed |

**Claims confirmed** (sample of those the brief named):
- Bogen p. 52, "not so much a theory as a tautology", is aimed at the undertaking theory (n. 7 cites Burdick pp. 515–16), as WS says.
- Bogen p. 91 conclusions.
- The Burdick pp. 515–516, 522 and 523 locators.
- Wyman p. 159.
- Sandoval-Strausz pp. 54, 62–63, 63, 65.
- Heart of Atlanta at 261.
- The § 2000a(b)(1) lodging clause listed first.
- The statutory comparators in Q4: EqA s 29(1), PAR reg 18(1), § 1395dd(a), OLA s 2(2).
- The gap statement's search record.

The pitch l. 21 repair also holds: HPA s 1(3) attaches conditions to the traveller, so "simply because they walked in the door" is wrong in law.

---

## D. Table: FAILs and every quotation that is not MATCH

No card FAILs.

| Card / file | Quotation | Verdict | Correct |
|---|---|---|---|
| lane1701cotton | "If the Inn be full, or the Carrier's Horses loaden, the Action would not lie… to serve the Publick." | LOCATOR-WRONG | 12 Mod **485** (page image n500), not 484 |
| WS_H1_origin §4 Q1 | same quotation, "p. 484" | LOCATOR-WRONG | 485 |
| WS_H1_origin §5 | "fixed by law rather than by contract" cited to bogen1996innkeeper pp. 52, 90 | NOT-FOUND in Bogen (misattributed) | Maese p. 501 only |
| shryock2012breaking (rr-2026-11 quote, used by WS §4 Q5 and PO §2.1) | "The answers, obvious to us now, are provided by the hospitality industry (…)" | MATCH, but truncated mid-sentence without an ellipsis; the omitted continuation ("and the government bodies that control immigration and naturalization…") changes the sense | Add "and the government bodies…" or mark the cut |

Every other quotation on the 22 cards (82 checked) is MATCH.

# R1. Citation and quotation audit

*Agent-drafted review. The author has not seen it.*

Manuscript: `../AUTHOR_DRAFT_v2.md`. Seat R1. Method: each reference was checked against `../literature/references.bib`, then Crossref (by DOI and by `query.bibliographic`, anonymous requests only), then the publisher or an archive copy. Each quotation was checked against the arm's facet files and audits, then the local full texts in `~/iit-playground/berthon_ethics_local/pdfs/`, then official online copies (American Presidency Project for Cleveland; ijoc.org for Rosenblat and Stark; archive.org for Simmel's German text). No Chrome, no git, no e-mail addresses used. Quotations below are in the source's words; I supply no replacement prose for the draft.

## 1. Verdict

The reference list is not safe to submit: of 89 entries, 17 carry wrong details and 1 cannot be found at all, and the wrong ones include four journal articles whose titles and venues do not exist as given (Cameron, Rahman, Kolt, Zong and Matias) plus an Almeida Cabrejas entry whose journal, title and pages are invented around a real article. Of about thirty quotations and locators, thirteen are altered or not in the source at the cited place, and the worst is the Moody-Adams "myth of culture as an engine of moral blindness", which appears nowhere in her article. The single most serious problem is that several quoted or attributed sentences (Moody-Adams, Kamperman and Graff on Street, Graff on employers, Delgamuukw para. 98, Valuev via Moser) cannot be found where the draft says they are, and the earlier fact-check's corrections were reversed or lost in places (sworn notaries, Marshall para. 14, "aloud", Rosenblat and Stark "ledger").

## Counts

| Part | Result |
| --- | --- |
| A. Reference entries (89) | MATCHES 69; DETAILS WRONG 17; NOT FOUND 1 (Hsieh); NOT CHECKED 2 (Monteiro; Phule's publisher) |
| B. In-text citations | (i) cited, not listed: 4 named works (Levin 2016, Waitangi Tribunal 2014, Akrich, Mumford) plus 2 primary documents (Cleveland 1897 veto, Wilson 1917 veto), 1 unattributed framework (HIAG), and about 11 statutes or instruments; (ii) listed, never cited: 12 |
| C. Quotations and locators (30 items) | VERBATIM 8; ALTERED or NOT IN SOURCE 13 (C27 is mixed); partly supported 8; COULD NOT CHECK 1 (plus the Milton page, C8, and the Kousser phrase, C30) |
| D. Text artifacts | 47 span pairs (94 tokens) on 22 lines in 7 sections; plus unrendered LaTeX and broken table rows |
| E. Regressions (60 rows) | Corrected 13; old error persists 25; changed but still wrong or unsupported 14; passage gone 8 |

## 2. Ten most serious findings, one line each

1. Moody-Adams "the myth of culture as an engine of moral blindness" (2.2, p. 304) is not in her article; p. 304's nearest sentence is "A culture-independent of agents who perpetuate culture-cannot be an 'agent' of anything."
2. Reference list: Cameron (2024), Rahman (2021), Kolt (2025), Zong and Matias (2024), Qadri et al. (2026), Almeida Cabrejas (2019) and Hsieh (2008) give titles or venues that Crossref and the arm's bib do not support; the real works are listed in Table A.
3. Kamperman and Graff (2026) are said (2.1) to cite Street's "autonomous model of literacy"; the article never mentions Street or the autonomous model.
4. Delgamuukw para. 98 is presented as a holding that "common law had systematically erred"; para. 98 is a warning about the trial judge's reasoning, and "equal footing" is para. 87.
5. Marshall para. 14 is again made a finding about "Mi'kmaq signatories" who were "non-literate" and about "Crown scribes"; the paragraph speaks of "the Indian parties" in general and never says non-literate (error A8/A9 returned).
6. Graff pp. 302-321 does not say industrial employers championed literacy to produce a "disciplined, punctual, and obedient factory workforce"; none of "employers", "punctual" or "obedien" occurs in ch. 7.
7. Valuev: "no separate Little Russian language ever existed, exists, or can exist" is in quotation marks and attributed to Moser (2017) but is not Moser's wording, and the listed Moser book is a different work from the 2017 Introduction the arm read.
8. Douglass's "horrible pit" sentence is altered in both places (3.2 and 4.2): the source reads "but to no ladder upon which to get out", not "but offered no ladder".
9. Milton: the source has "tickets and statutes and standards", not "brocards"; "p. 18" has no edition behind it.
10. "Sworn notaries", "non est factum ... restrained human scribes", the Pragmática "read ... aloud" and "to curb scribe dominance", and Rosenblat and Stark's "closed ledger" are all flagged errors from the earlier check (A3, A4, C12, C14, A12) that remain.

## 3. Part A. The reference list

Verdicts: MATCHES / DETAILS WRONG / NOT FOUND / NOT CHECKED. "Bib" = `../literature/references.bib`. "CR" = Crossref.

### 3.1 Details wrong, not found, or not checked (19 entries)

| Entry as in the draft | Verdict | Correct details and source |
| --- | --- | --- |
| Almeida Cabrejas (2019), *Journal of Legal History and Notarial Studies* 44(1), 18-35, "The evolution of the Spanish notarial institution..." | DETAILS WRONG | The article is "'No firmó porque dijo no saber': alfabetizados y analfabetos en documentos notariales de CODEA de los siglos XVI y XVII", *Philologia hispalensis* 33(1), 21-41, doi 10.12795/ph.2019.v33.i01.02 (bib `almeida2019firmo`; CR; local PDF `pdfs/G/almeida.txt`). Page 24 is inside the real article and does carry the Pragmática quotation. |
| Bakos, Marotta-Wurgler and Trossen (2009), *J. Legal Studies* 43(1), 1-35 | DETAILS WRONG | Journal version is 2014, doi 10.1086/674424 (CR; bib `bakos2014does`). The 2009 version is an NYU working paper with a different subtitle ("Testing a Law and Economics Approach to Standard Form Contracts"; bib `bakos2009does`). The draft mixes the two. |
| Cameron (2024), "Making sense of algorithmic management: The role of worker communities and collective resistance", *Academy of Management Annals* 18(1), 89-124 | DETAILS WRONG | Cameron, L. D. (2024), "The Making of the 'Good Bad' Job: How Algorithmic Management Manufactures Consent Through Constant and Confined Choices", *Administrative Science Quarterly* 69(2), 458-514, doi 10.1177/00018392241236163 (CR; bib `cameron2024making`). The draft's title and venue returned nothing in CR. |
| Douglass, M. (1854) title "...who was imparted thirty days in the common jail of Norfolk..." | DETAILS WRONG | Title page (`pdfs/C/md.txt`): "Educational Laws of Virginia. The Personal Narrative of Mrs. Margaret Douglass, a Southern Woman, Who Was Imprisoned for One Month in the Common Jail of Norfolk, under the Laws of Virginia, for the Crime of Teaching Free Colored Children to Read." Boston: John P. Jewett and Co.; Cleveland: Jewett, Proctor and Worthington, 1854. Bib `douglass1854educational`. |
| Dubal (2023), *Columbia Law Review* 123(7), 1927-2000 | DETAILS WRONG (minor) | Volume and issue confirmed on columbialawreview.org. Bib gives the first page as 1929, and the facet cites p. 1984 in Columbia pagination. Start 1927 does not match; end page I could not confirm. |
| Engerman and Sokoloff (2001), *J. Economic History* 65(4), 891-921 | DETAILS WRONG | The journal article is 2005 (CR doi 10.1017/S0022050705000343; bib `engerman2005evolution`). 2001 is the NBER working paper 8512 (bib `engerman2001evolution`), the version the arm actually read. |
| Hagedorn (1988), "...the interpreter as cultural broker in eighteenth-century Anglo-Iroquois diplomacy" | DETAILS WRONG | Title is "'A Friend to go between Them': The Interpreter as Cultural Broker during Anglo-Iroquois Councils, 1740-70", *Ethnohistory* 35(1), 60-80, doi 10.2307/482433 (bib `hagedorn1988friend`; CR). Volume, issue, pages are right. |
| Johansson (1985), *History of Education Quarterly* 25(1/2), 61-72 | DETAILS WRONG | Bib `johansson1985popular`: *Historical Social Research* 10(2), 60-64, doi 10.12759/hsr.10.1985.2.60-64 (SSOAR urn:nbn:de:0168-ssoar-34824). I found no HEQ article of this title in CR; I could not reach CR or SSOAR for the HSR record this session, so the correction rests on the arm's earlier DOI check (`audit/AUDIT_02.md` X11, X24). |
| Kolt (2025), "Algorithmic agency and the law of principals", *Stanford Technology Law Review* 28(2), 145-202 | DETAILS WRONG | Kolt, N., "Governing AI Agents", *Notre Dame Law Review* 101 (bib `kolt2025governing`; CR doi 10.2139/ssrn.4772956, SSRN 2024, arXiv 2501.07913). The draft's title and venue were not found. The claim cited to it (4.5 "instrument of its principal") is not checked against the paper; the arm read Kolt only for the loyalty roadmap (`M2_algorithm_studies.md:138`). |
| Lake (2006), "The white man under siege: New histories of race in the Pacific and the British Empire", *History Workshop Journal* 61(1), 146-162 | DETAILS WRONG | Two real Lake items. "The White Man under Siege: New Histories of Race in the Nineteenth Century and the Advent of White Australia", *History Workshop Journal* 58(1), 41-62 (2004), doi 10.1093/hwj/58.1.41 (CR). And the one the arm used for the literacy test: "From Mississippi to Melbourne via Natal: the invention of the literacy test as a technology of racial exclusion", in Curthoys and Lake (eds), *Connected Worlds* (ANU Press, 2006), doi 10.22459/cw.03.2006 (bib `lake2006mississippi`). The draft's entry matches neither. |
| Moser (2017), *New contributions to the history of the Ukrainian language*, CIUS Press | DETAILS WRONG | Open Library lists the book as 2016 (CIUS Press); I did not open it. The work the arm read is Moser (2017), "Introduction", *East/West: Journal of Ukrainian Studies* 4(2), 3-7, doi 10.21226/T2DK9B (bib `moser2017introduction`). Year, and which work holds the Valuev wording, are both unsettled (see C10). |
| Qadri, Prabhakaran and Denton (2026), "Temporal pitfalls in sociotechnical AI critique...", *Big Data & Society* 13(1), 1-16 | DETAILS WRONG | Bib `qadri2026ai`: "'AI is (not) the new ..': A Diagnostic Analogy Framework for Generative AI's Cultural Impacts", a poster at the ICML 2026 workshop "Culture x AI"; Google Research page and ICML page opened; no DOI; abstract only (`X_counter_case.md:100`). No *Big Data & Society* article found. |
| Rahman (2021), "The invisible hand of the platform...", *Yale Law Journal* 130(4), 984-1062 | DETAILS WRONG | Rahman, H. A. (2021), "The Invisible Cage: Workers' Reactivity to Opaque Algorithmic Evaluations", *Administrative Science Quarterly* 66(4), 945-988, doi 10.1177/00018392211010118 (CR; bib `rahman2021invisible`). |
| Scherer, Neesham, Schoeneborn and Scholz (2023), *Business & Society* 62(8), 1539-1572 | DETAILS WRONG | The 2023 paper by these four authors is the Guest Editors' Introduction "New Challenges to the Enlightenment: How Twenty-First-Century Sociotechnological Systems Facilitate Organized Immaturity and How to Counteract It", *Business Ethics Quarterly* 33(3), 409-439, doi 10.1017/beq.2023.7 (CR). Not in the arm's bib. |
| UNESCO Institute for Statistics (2026), *Literacy rates among adults and youth: Global report on trends and data*, UNESCO Publishing | DETAILS WRONG | Bib `uis2026adult`: "Adult illiterate population and adult literacy rate, 15+ years ... February 2026 Data Release", UIS data browser (databrowser.uis.unesco.org). It is a data release, not a published report; I found no report of the draft's title. The figures (see C26) are for 2024. |
| Viljoen (2021), "A relational theory of data" | DETAILS WRONG | Title is "A Relational Theory of Data Governance", *Yale Law Journal* 131(2), 573-654 (bib `viljoen2021relational`; CR lists the SSRN version). Volume, issue and pages are right. |
| Zong and Matias (2024), "Bartleby in the algorithmic age: The right to refusal in platform labor", *ACM TOCHI* 31(2), 1-28 | DETAILS WRONG | The 2024 Zong and Matias paper in CR is "Data Refusal from Below: A Framework for Understanding, Evaluating, and Envisioning Refusal as Design", *ACM Journal on Responsible Computing* 1(1), 1-23, doi 10.1145/3630107. Their separate "Bartleby" paper (2022) is on research-ethics systems, *Social Media + Society* 8(1). The draft's title and venue match neither. The claim it supports (a legal guarantee that the non-algorithmic route carries no penalty, 5.2) is not what a design framework for data refusal says; I read only the CR records. |
| Hsieh (2008), "Employment discrimination, commodification, and agency", *Business Ethics Quarterly* 18(4), 513-539 | NOT FOUND | Searched CR by author plus title phrase, by author within BEQ (ISSN 1052-150X) for 2008, and by title; no such article. Hsieh's 2008 items in CR are a book review in BEQ 18(1) and "Survey Article: Justice in Production", *Journal of Political Philosophy* 16(1), 72-100. His republican-workplace paper is "Rawlsian Justice and Workplace Republicanism", *Social Theory and Practice* 31(1), 115-142 (2005). The draft's description (republican framework against managerial power) fits the 2005 paper, but I cannot say which the author means. Not in the arm's bib. |
| Monteiro (2017), "A designer's code of ethics", *Dear Design Student* | NOT CHECKED | Site unreachable this session. Uncited in the text. |
| Phule (1882), *Memorial addressed to the Education Commission*, Government Central Press | NOT CHECKED (publisher) | Title and year match bib `phule1882memorial` (online reprint only). The bib gives no publisher; I found none. |

### 3.2 Matches (69 entries, listed with the check used)

Alabama Constitutional Convention (1901) (bib; Knox address pp. 7-10 confirmed in the archive.org scan). Angwin et al. (2016) (ProPublica page opened, title and 23 May 2016; author list not re-read; uncited). Arber (1875) (bib). Aristotle (2011) (CR, Bartlett and Collins, Chicago). Balkin (2016), Citron (2008), Delacroix and Lawrence (2019), Khan and Pozen (2019), Edwards and Veale (2017) (bib). Ben-Shahar and Schneider (2011) (bib: vol. 159, 647-749; issue 3 not confirmed). Berthon, Ferguson, Pitt and Wang (2023) (CR). Berthon, Pitt and Campbell (2019) (CR, doi 10.1177/0743915619859852; text read). Berthon et al. (2024) (bib). Bhargava and Assadi (2024) (CR: online 2023, BEQ 34(2), 201-230). Bhargava and Young (2022) (CR: online 2021, BEQ 32(4), 519-545; subtitle "An Institutional Complementarities Approach" omitted). Blevis (2007) (CR doi 10.1145/1240624.1240705, pp. 503-512; subtitle not in CR). Bommasani et al. (2026) (CR doi 10.1145/3805689.3812400, pp. 6351-6382; not in the arm's bib; text not opened). Bourdieu (1984) (Open Library lists the Harvard UP edition). Brandt (1998) (bib, doi). Burns (2010) (bib). Butterfield (1931) (bib). Clanchy (1979) (Open Library: 1979, Harvard UP and Edward Arnold; bib holds the 2013 reprint; uncited). Delgamuukw [1997] 3 S.C.R. 1010; *R. v. Marshall* [1999] 3 S.C.R. 456; *Gaston County* 395 U.S. 285; *Katzenbach* 383 U.S. 301; *Hill v. Gateway* 105 F.3d 1147; *Foster v. Mackinnon* (1869) L.R. 4 C.P. 704 (bib: 704-712). Douglass (1845) (bib). Floridi and Cowls (2019) (CR; volume and issue not in the record); Floridi and Taddeo (2016) (CR, 374(2083), 20160360). Fricker (2007), Pettit (1997) (bib). Giesler and Veresiu (2014) (CR). Graff (1979) (bib `graff1991literacy`, year 1979). Hirschman (1970) (Open Library, Harvard UP). Human Rights and Equal Opportunity Commission (1997) (bib). Jobin, Ienca and Vayena (2019) (CR). Kamperman and Graff (2026) (CR; text read). Kim and Routledge (2022) (CR: online 2021, BEQ 32(1), 75-102). Kousser (1974) (bib). Leonard (1992) (bib). Martela and Steger (2016) (CR). Messick (1993) (CR). Milton (1644) (bib; publisher "Privately printed" unverified; no edition named). Mittelstadt (2019) (bib). Moody-Adams (1994) (bib, doi 10.1086/293601). Muldoon and Raekstad (2023) (bib). Newland (2022, 2024) (bib; the draft omits "Vol. I"). Pasquale (2015) (bib). Rosenblat and Stark (2016) (PDF opened; IJOC 10, 3758-3784). Sap et al. (2019) (CR, pp. 1668-1678). Stark and Vanden Broeck (2024) (CR doi 10.1177/26317877241257213, *Organization Theory* 5(2); CR has no page range, so "1-24" is unverified). Street (1984), Street (2003) (bib; 2003 pages 77-91 not in the bib record). Truth and Reconciliation Commission (2015); UNESCO (2015) (bib). Vallor (2016) (Open Library, OUP). Vee (2013) (bib, doi). Verbeek (2005) (CR). Walzer (1988) (see note). Washington (1901) (bib; original Doubleday edition). Williams, H. A. (2005) (bib; uncited). Williams, J. (2018) (bib, doi). Winner (1980) (bib). Wolff (1950) (bib). Yeung (2016) (bib: online 2016; the issue is dated 2017). Young (2006) (bib).

Note on Walzer: *The Company of Critics* (Basic Books, 1988) is a real book (CR review records; Open Library). The arm's bib key `walzer1988interpretation` is a different work, *Interpretation and Social Criticism* (Tanner Lectures, delivered 1985; Harvard UP 1987), the one the arm quoted for "the connected critic" (`M4_ethical_frameworks.md:138`). The draft's entry matches the year the arm used, not the book it read. The author should say which he means.

## 4. Part B. In-text citations against the reference list

### (i) Cited in the text, absent from the list

| Cited as | Where | Note |
| --- | --- | --- |
| Levin, 2016 | 2.3 matrix, last row | No entry. Not in the arm's bib. I cannot identify the work. |
| Waitangi Tribunal, 2014, pp. 355-358 | 3.3 | No entry. Bib `waitangi2014declaration` (Wai 1040, stage 1). |
| Akrich | 6.2 ("Madeleine Akrich's concept of the 'script'") | No year, no entry. |
| Mumford | 6.2 ("Lewis Mumford's distinction") | No year, no entry. |
| Cleveland 1897 veto; Wilson 1917 veto | 3.1 | Quoted and paraphrased with no citation at all. |
| "Human Identity and Autonomy Gap (HIAG) framework" | 5.3 and the 7.2 table | Presented as an existing framework that "formalized" the dynamics; no author, year or entry. The arm's files contain no such framework. |
| Statutes and instruments with no entry | 3.1-3.5, 5.3-5.4 | Immigration Restriction Act 1901 and Natal Act 1897 (only via Lake); Voting Rights Act 1965; Saraiva Law 1881; Negro Act 1740 and the Virginia 1831 statute; Pragmática 1503; Licensing Act 1662; Star Chamber decrees 1586 and 1637; Jomtien (1990) and Dakar (2000) documents; GDPR Art. 22; EU Platform Work Directive; Computer Fraud and Abuse Act; C2PA. |
| Short forms that do not match an entry | 2.3 and 4.1 matrices; 5.5, 6.1 | "Alabama Convention, 1901"; "Rosenblat, 2016" (the entry is Rosenblat and Stark); "Waitangi, 1840"; "Berthon et al., 2019" (the entry is three authors and the text elsewhere names them). |

### (ii) Listed, never cited in the body (12)

Angwin et al. (2016); Aristotle (2011); Berthon, Ferguson, Pitt and Wang (2023); Berthon, Yalcin, Pehlivan and Rabinovich (2024); Blevis (2007); Bourdieu (1984); Citron (2008); Clanchy (1979); Floridi and Cowls (2019); Floridi and Taddeo (2016); Monteiro (2017); Williams, H. A. (2005).

## 5. Part C. Quotations and locators

Legend: V = VERBATIM; A = ALTERED (source's words given); N = NOT IN SOURCE AT THAT LOCATOR; P = partly supported; X = COULD NOT CHECK.

| # | Where and what | Verdict | Source's words and evidence |
| --- | --- | --- | --- |
| C1 | Intro and 3.1: Knox, "And what is it that we want to do? Why it is, within the limits imposed by the Federal Constitution, to establish white supremacy in this State." p. 8 | A (one comma) | `pdfs/D/al_v1.txt` lines 503-506: "Why it is within the limits imposed by the Federal Constitution, to establish white supremacy in this State." No comma after "Why it is". Page 8 is right (printed page header "8" precedes it). |
| C2 | 3.1: Knox "acknowledged that the Fourteenth and Fifteenth Amendments prohibited direct racial exclusions, but assured the delegates that an administrative literacy requirement, combined with discretionary property and character clauses, would achieve the identical result" | P | The address runs beyond pp. 7-10 (the arm read only those). It discusses educational and property qualifications and quotes a California case on the Fourteenth and Fifteenth Amendments (al_v1.txt lines 690-840). I found no "character clause" and no assurance of "the identical result". This is a characterization, not Knox's words. |
| C3 | Intro: Auld, literacy would "forever unfit him to be a slave" (Douglass 1845, p. 33) | V | `pdfs/C/douglass.txt` 2013; facet C entry 11 gives p. 33 (DocSouth page marks). |
| C4 | 3.2: Auld block quote, "Learning would spoil the best nigger in the world. Now," said he, ... "no value to his master." (p. 33) | V | douglass.txt 2010-2015. The quotation opens mid-speech: the sentence before it ("If you give a nigger an inch, he will take an ell. A nigger should know nothing but to obey his master") is omitted. The slur is reproduced from the source; the facet replaced it with brackets. For the author to decide. |
| C5 | 3.2 and 4.2: "It opened my eyes to the horrible pit, but offered no ladder upon which to get out." (ch. VII) | A | Source (douglass.txt 2277-2278, Chapter VII): "It opened my eyes to the horrible pit, but to no ladder upon which to get out." The first sentence of the 3.2 quote ("I would at times feel that learning to read had been a curse rather than a blessing. It had given me a view of my wretched condition, without the remedy.") is verbatim. |
| C6 | 3.1: Cleveland 1897, "It is said that the quality of recent immigration is undesirable. The time is quite within recent memory..." | A (one word) | American Presidency Project, Cleveland, Veto Message, 2 March 1897: "It is said, however, that the quality of recent immigration is undesirable. The time is quite within recent memory when the same thing was said of immigrants who, with their descendants, are now numbered among our best citizens." The draft drops "however,". "Betrayal of democratic principles" is the author's characterization; Cleveland's stated ground is departure from the national policy of welcome. |
| C7 | 3.1: Wilson 1917 "argued that the test measured opportunity rather than character or capability" | P | `pdfs/D/wilson17.txt`: "It is not a test of character, of quality, or of personal fitness, but would operate in most cases merely as a penalty for lack of opportunity in the country from which the alien seeking admission came." Wilson's lead objection is "a radical change in the policy of the Nation which is not justified in principle". "Capability" is not his word; "measured opportunity" inverts "penalty for lack of opportunity". The 1917 Act became law over the veto (facet D line 469); the draft does not say so. |
| C8 | 3.4: Milton, "Truth and understanding are not such wares as to be monopoliz'd and traded in by tickets and statutes and brocards." (p. 18) | A; locator X | Gutenberg text (`pdfs/B/areopagitica.txt`, modernised spelling): "Truth and understanding are not such wares as to be monopolized and traded in by tickets and statutes and standards." "Brocards" is not in this sentence. No edition is named, so I cannot check "p. 18"; the arm's copy has no page numbers (`B_print_1450_1800.md:23`). |
| C9 | 3.2: Valuev circular, "no separate Little Russian language ever existed, exists, or can exist" (Moser, 2017) | A / N | The arm's source (Moser 2017, Introduction, p. 3, audited in `AUDIT_05.md` M5-19, M5-20): the directive's ground, in Moser's translation, was that "a [distinct] Little Russian ... language did not, does not and cannot exist". The draft's sentence is a paraphrase placed in quotation marks. It is also cited to a book (see Table A, Moser) the arm did not read. The audit also corrected the speaker: "as the Valuev Directive put it", not the censors. |
| C10 | 2.2: Moody-Adams (1994, p. 304) "the myth of culture as an engine of moral blindness" | N | No "myth" and no "engine" occur anywhere in the article (`pdfs/library/txt/MoodyAdams-...txt`). p. 304's sentence, line 746-748: "A culture-independent of agents who perpetuate culture-cannot be an 'agent' of anything." The paraphrase after the quotation (diffuse cultural forces obscure human decisions) fits her argument (pp. 304-305). Remove the quotation or find where it comes from; if from a secondary source, cite that. |
| C11 | 2.3: Moody-Adams (1994, pp. 293-296) "affected ignorance": "the deliberate refusal to attend to moral considerations that one has the capacity to know, driven by an unacknowledged desire to preserve one's material advantage" | A | Her definition (line 309, p. 296): "Affected ignorance-choosing not to know what one can and should know"; elsewhere "choosing not to be informed of what we can and should know". "Deliberate", "unacknowledged desire" and "material advantage" are not in the definition. The Greek slavery passage notes that the institution "benefited nonslaves in various ways" (p. 295), but she does not build that into the definition. The text then applies it to "scribes, administrators, and judges"; her case is persons and a culture, not institutional procedure (earlier row B8). |
| C12 | 2.1: Brandt (1998, p. 166) "sponsors"—"agents, institutions, and forces that subsidized, acquired, and exerted control over the literacy of others" | P | The word "sponsors" is hers. The gloss is not her wording. Her definition, as quoted in `M1_literacy_studies.md:69`: "Sponsors ... are any agents, local or distant, concrete or abstract, who enable, support, teach, or model, as well as recruit, regulate, suppress, or withhold literacy and gain advantage by it in some way." The arm read it from a report, not the journal, and could not check p. 166 against CCC. "Always" is not in that sentence. |
| C13 | 2.1: Simmel in Wolff (1950, p. 154), "der Unparteiische" and "tertius gaudens" | P | German terms confirmed in Simmel, *Soziologie* (1908; archive.org `soziologieunters00simm_0`): "1. Der Unparteiische und der Vermittler" and "2. Der Tertius gaudens". English edition: "The Non-Partisan and the Mediator" begins p. 145; "The Tertius Gaudens" begins p. 154 (contents list; text shows "154 The Triad § 3. The Tertius Gaudens"). So p. 154 cites the second term only; the first sits at pp. 145-153. |
| C14 | Intro: Berthon, Pitt and Campbell (2019, p. 457) "information is necessary, but not sufficient to change behavior" | V | `pdfs/library/txt/berthon-et-al-2019-...txt`, p. 457 (between the 456 and 458 running heads): "empirical research suggests that information is necessary, but not sufficient to change behavior (e.g., Worsley 2002)". The authors report this as a finding they cite; the draft attributes it to them as an observation. |
| C15 | Intro: Williams (2018, p. 101), "Nor will 'media literacy' alone lead us out of this forest." | V | Facet H line 177; `AUDIT_03.md` H19 CONFIRMED. |
| C16 | Intro: Kamperman and Graff (2026, p. 36) repeat "the nineteenth-century myth that individual literacy guarantees economic security" | V (paraphrase) | p. 36, Myth #2: "Literacy is a certain or guaranteed path to economic security"; p. 35: "19th- and early 20th-century print literacy campaigns". Error A7 is corrected. |
| C17 | 2.1: Kamperman and Graff "caution against extending literacy metaphors indiscriminately, noting that Brian Street's (1984, 2003) critique of the 'autonomous model of literacy' applies with equal force" | N | The article contains no "Street", no "Brian", no "autonomous", no "ideolog". It says AI-literacy initiatives "use literacy uncritically as a metaphor" (p. 35) and cites New Literacy Studies in general (p. 36). The Street attribution is the draft's own and should be marked as such or cited to Street alone. |
| C18 | Intro and 4.1: Rosenblat and Stark (2016, p. 3762): about fifteen seconds, no destination or fare | V (paraphrase) | ijoc.org PDF, journal p. 3762: "they have about 15 seconds to accept it or reject it ... drivers are not shown destination or fare information before they accept a ride." |
| C19 | Intro and 4.1: Rosenblat and Stark (p. 3771): workers who contest "automated deactivations or pay deductions are met with template replies from a closed ledger" | P | p. 3771: "Drivers can make inquiries and usually receive template responses". The passage concerns inquiries to support staff (CSRs), not deactivations or deductions, and nothing there is a ledger. "Closed ledger" and "inaccessible ledger" are the draft's own (the origin is Claude's introduction, per `AUTHOR_DRAFT_CHECK.md` A12). Deactivation is discussed elsewhere in the article (pp. 3762, 3766, 3775). |
| C20 | Intro and 3.3: *Marshall* para. 14: Mi'kmaq signatories "non-literate" and unable to "create their own written record"; "Crown scribes to overwrite oral covenants" | A / N | Para. 14 (`pdfs/A/marshall.txt`): "The Indian parties did not, for all practical purposes, have the opportunity to create their own written record of the negotiations." The paragraph discusses treaty-making in general (its examples are treaties with Cree and Dene nations). "Non-literate" occurs nowhere in the judgment; "Crown scribes" occurs nowhere. |
| C21 | 3.3: *Marshall* para. 40 | P | Para. 40: "the Nova Scotia judgments erred in concluding that the only enforceable treaty obligations were those set out in the written document of March 10, 1760". This supports "written instruments could not be interpreted in isolation". It contradicts the introduction's reading that the Crown overwrote oral covenants. |
| C22 | 3.3: *Delgamuukw* para. 98: Lamer held "that Canadian common law had systematically erred by discounting Indigenous oral histories ... mandating ... equal evidentiary footing" | A | Para. 98 (`pdfs/A/delgamuukw.txt`): "I fear that if this reasoning were followed, the oral histories of aboriginal peoples would be consistently and systematically undervalued by the Canadian legal system". This is a warning about the trial judge's reasoning. The "equal footing" language is para. 87: "the laws of evidence must be adapted in order that this type of evidence can be accommodated and placed on an equal footing with the types of historical evidence that courts are familiar with". |
| C23 | 3.3: Waitangi Tribunal (2014, pp. 355-358) cited for Williams's overnight translation, *kawanatanga* as "newly coined", over 500 signatories, and immediate enforcement of the English text | P | Printed pp. 354-355 (`pdfs/A/w1.txt`) are the 5-6 February negotiation: Hobson addressed the chiefs with Williams "interpreting sentence by sentence". The facet places the "more than 500" and "39 signed the English" figures at p. 386, and the Tribunal's view of Williams at pp. 414-422 and 514, where it neither convicts nor clears him (`G_third_parties.md:235, 260`). "Newly coined" and "overnight" are not in what I read. "Whose textual ambiguities served Crown expansion" is stronger than the Tribunal. |
| C24 | 3.3: Almeida Cabrejas (2019, p. 24): notaries "required ... to undergo public examination, keep an unalterable bound register (protocolo), and read all legal instruments aloud in the simultaneous presence of the parties and independent witnesses"; "recognizing that scribes routinely defrauded illiterate citizens" | P | p. 24 (`pdfs/G/almeida.txt`): notaries must record deeds "en un protocolo o libro de asiento", and the law says "los dichos escrivanos las lean presentes las partes e los testigos". "Lean" is "read", not "aloud" (the audit removed "aloud", C12); "public examination", "unalterable" and "independent" are not on p. 24; no purpose of curbing fraud is stated. |
| C25 | 3.3: Hagedorn (1988, p. 61): "indigenous leaders insisted on having second, independent interpreters present to cross-check imperial translations in real time" | A | p. 61: "When doubts about an interpreter's integrity or ability arose on either the Indian or the English side, others were employed, formally or informally, to 'assist' and check the accuracy of his translations." Either side, not Indigenous leaders; "insisted" and "real time" are not there. |
| C26 | 3.5: Graff (1979, pp. 302-321): "Industrial employers championed basic literacy ... to cultivate a disciplined, punctual, and obedient factory workforce" | N | In ch. 7 (`chapter7.txt`, printed pp. 269-322) none of "employers", "punctual", "obedien", "docile" occurs. The nearest sentence (p. 321): literacy "was more central to the training, discipline, morality, and habits it accompanied and advanced than to the specific skills it represented". Graff also writes that literacy was "more valuable to the society's goals and needs than to those of most individuals within it" and that "Possession of literacy ... guaranteed neither success nor a rise from poverty" (p. 320). A 20-page range is too wide a locator for a specific claim. |
| C27 | 3.5: Dakar "committed ... to a 50 percent improvement in adult literacy levels by 2015"; "explicit mandates to eradicate adult illiteracy" (Jomtien and Dakar) | V / A | Dakar Framework (`pdfs/F/dakar_hrlib.txt`): "Achieving a 50 per cent improvement in levels of adult literacy by 2015". V. But neither Jomtien (a proposal to halve the 1990 rate) nor Dakar speaks of eradicating; "eradicate" overstates (earlier rows B10, C18). UNESCO (2015): "the Dakar target of halving illiteracy was not achieved" (rate fell from 18% to an estimated 14%). |
| C28 | 3.5: UIS (2026): "739 million adults remain non-literate worldwide, 63 percent of them women" | V | UIS February 2026 release (`F_promise_and_campaigns.md` line 33, from the data browser): 739,139,712 people aged 15 and over in 2024; 466,257,152 women (63.1%). The draft omits that the year is 2024. |
| C29 | Intro: Jobin et al.: 84 sets of guidelines, non-maleficence "named in 60 and beneficence in 41" | V | Matches the arm's record (`AUDIT_01`; AUTHOR_DRAFT_CHECK A5) and the paper's counts as I know them from the arm; I did not re-open Jobin this session. |
| C30 | 3.1: Registrars were to evaluate whether an applicant could read and "correctly explain" clauses (Kousser, 1974) | X | The phrase is not in *Katzenbach* (`pdfs/D/us383_301.txt`). Kousser (1974) is not held in full text; the arm did not open it. Also 3.1: *Gaston County* "grossly underfunded school systems that deliberately withheld literacy": the opinion says "separate and inferior schools"; "deliberately", "withheld" and "underfunded" do not occur. |

Also checked: Engerman and Sokoloff cited (3.1) for the Saraiva Law and for "indigenous and Afro-descendant majorities". The working paper the arm read (NBER 8512) does not mention the Saraiva Law and has no "indigenous" or "Afro" (`M5_wider_cases.md:51, 213`); the arm took the Saraiva Law from Nicolau, and it conditioned enrolment, not citizenship. The 2005 JEH version was not opened by anyone. Qadri et al. (4.5): the abstract the arm has says imprecise analogies produce imprecise governance and separates structural from contingent consequences; it says nothing of "historical fatalism" or "political coalitions".

## 6. Part D. Text artifacts

**Span tags.** 47 start tags and 47 end tags, paired by id (`span_54` to `span_230`; 94 tokens in all), on 22 lines. By section:

| Section | Lines | Pairs |
| --- | --- | --- |
| 4.1 mapping table | 256, 262 | 5 |
| 5 intro, duties table | 350 | 1 |
| 5.4 diagram | 423 | 1 |
| 6.1 Martela and Steger table | 455, 456, 461, 466, 467 | 14 |
| 6.2 diagram | 483, 486, 489, 492 | 6 |
| 7.1 four-layer table | 527, 532, 536, 540 | 7 |
| 7.2 paradigm-shift table | 566, 570, 573, 574, 578 | 13 |

Every one sits inside a table cell or a diagram label, so the surrounding box borders are broken as well (rows at 255-256, 261-262, 349-350, 455-467, 526-540 and 565-578 no longer align). Line 455 also has a quotation mark placed inside the tag run (`"folk theories[span_111]...[span_113](start_span)"[span_111](end_span)...`).

**Other artifacts.**
- Unrendered LaTeX in 5.3: line 401 (`$$dA_t = \mu(I_t) A_t dt + \sigma_A A_t dW_t^A$$`) and line 403 (`I_t \in [0, I_{\max}]`, `\sigma_A > 0`, `W_t^A`, `I_t > I^*`, `\mu(I_t)`).
- The same diagram uses `I_t < I* Regime` in plain text (line 389), different from the LaTeX notation.
- Table row at line 463 is broken: "3. Significance The evaluative sense" runs the first two cells together with no border.
- Italic asterisks left raw inside table cells (`*R. v. Marshall*`, `*Katzenbach*`, `*Gaston County*`, `*Waitangi*`, `*non est factum*`, `*Moral Attention*`, `*Coherence*`).
- `⚬` used as the bullet character in lists and in all 89 reference lines.
- Seven ASCII or box-drawing diagrams (2.1, 3.4, 4.4 twice, 5.3, 5.4, 6.2) will not survive a Word or PDF conversion without redrawing.
- Line 1 is an HTML comment from the arm, not part of the author's text.
- Typo at 2.1: "by an dispatch algorithm".
- Reference list entry for Douglass, M. (1854) carries a garbled word ("imparted") that looks like a machine error rather than a typo.

## 7. Part E. Regressions against `../AUTHOR_DRAFT_CHECK.md`

Key: OK = corrected; STILL = old error present; CHG = changed but still wrong or unsupported; GONE = passage no longer in the draft.

| Row | Status | Where in v2 |
| --- | --- | --- |
| A1 economic standing | OK | Abstract now says "civic and legal standing"; but 3 intro says "legal, commercial, and civic standing". |
| A2 "amplify" | OK | Word gone; but 4.4 "more dangerous" and 7.3 "unprecedented speed, opacity, and scale" are unsourced. |
| A3 "sworn notaries" | STILL | Abstract, contribution 3, 4.4 ("sworn notary"), 5.4, 7.3. |
| A4 *non est factum* "restrained scribes" | STILL | Abstract, contribution 3, 3.3, 7.3. *Foster* (1869) is cited for an "emerging" doctrine; the misdescriber there was the other party. |
| A5 Jobin counts | OK | "named in 60 ... 41". |
| A6 Williams | OK | Quotes "Nor will 'media literacy' alone ...". |
| A7 Kamperman and Graff | OK | "economic security", "nineteenth-century". But see C17 (new error). |
| A8 *Marshall* para. 14 / Mi'kmaq | STILL | Intro, 3.3 ("non-literate" added). |
| A9 "overwrite oral covenants" | STILL | Intro ("Crown scribes to overwrite"), 2.3 matrix. |
| A10 "deliberate" deployments | CHG | "Deliberate" gone from the intro; 2.3 ("They chose not to see") and 3.3 (Williams "served Crown expansion") attribute intent. |
| A11 Bommasani 4% of ten | STILL | Now "systematic exclusion across every employer using it" and "dozens of independent employers". |
| A12 "closed ticketing / ledger" | STILL | Intro, 4.1 ("closed ledger", "inaccessible ledger"). |
| A13 third criterion | OK | "outcomes fell systematically short of stated promises". |
| A14 "texts were passive" | STILL | 2.1 ("remained passive"), 4.3 ("static"); 3.4 itself names the Company as an owner. |
| A15 platforms "stripped" of safeguards | STILL | Abstract, 4.4 ("collapse", "complete absence"); no source. |
| A16 Lange and Pfarrer | OK | Not in the list. |
| B1 "irreducible" triadic | STILL | 2.1 ("irreducible intermediaries"). |
| B2 K&G critique | CHG | Now "caution against extending literacy metaphors", with the invented Street link. |
| B3 Graff "until institutions introduced textual hurdles" | GONE | Replaced by the 3.5 employer claim (C26). |
| B4 Clanchy oral oaths | GONE | Passage removed; Clanchy remains in the list, uncited. |
| B5 optional vs mandatory | GONE | 2.3 states it as the author's own ("The historical evil was not literacy..."). |
| B6 "cannot be judged by contemporary standards" | STILL | 2.3 (Butterfield, whiggism) beside Moody-Adams, who argues against it (pp. 298, 308). |
| B7 absence of protest | CHG | Now "does not imply moral innocence"; softer, but cited to nothing and set against Moody-Adams p. 294. |
| B8 affected ignorance as institutional | STILL | 2.3 applies it to "scribes, administrators, and judges"; definition altered (C11). |
| B9 "denied standing to protest" | GONE | Not in v2. |
| B10 UNESCO "failed mandates" | CHG | Now "mandates to eradicate adult illiteracy" (C27). |
| B11 Johansson 1981 | OK | Year now 1985 (reference details still wrong). |
| B12 pursued literacy "because ... real economic ... agency" | STILL | 2.3: "Marginalized groups recognized this value and fought to acquire it". |
| C1 Alabama "civic competence" | STILL | 2.3 matrix ("claiming civic competence"). |
| C2 *Gaston* "underfunded or outlawed schools" | CHG | "grossly underfunded ... deliberately withheld literacy" (C30). |
| C3 vetoes under the voting gate | CHG | Now says immigration tests, but still inside 3.1 "The Gate", followed by a VRA sentence; Wilson's phrase misdescribed (C7). |
| C4 VRA 1965 dismantled | STILL | 3.1 ("federal preemption through the Voting Rights Act of 1965"); no 1970 amendments, no Australia 1958 or Brazil 1985. |
| C5 Saraiva Law | STILL (unverified) | Name right; text not opened; cited to Engerman and Sokoloff, who do not mention it. |
| C6 statutes in four states | STILL | 3.2 ("Identical measures followed in Alabama, Georgia, and North Carolina"). |
| C7 "formal declarations" | CHG | Auld's private speech now presented as "the institutional rationale". |
| C8 Williams 2005 | GONE | Not cited in the text (still listed). |
| C9 Margaret Douglass "civil disobedience" | OK | Now "arrested, indicted, and sentenced"; 1854 date right. Reference title wrong. |
| C10 *Delgamuukw* "contract interpretation" | CHG | "Contract" gone; replaced by "held ... systematically erred" (C22). |
| C11 Waitangi translator | CHG | Williams named, *kawanatanga* identified; but "interested institutional intermediary whose textual ambiguities served Crown expansion" goes beyond the Tribunal, which does not decide. |
| C12 Pragmática "public readings"/"aloud" | STILL | 3.3 ("read all legal instruments aloud ... independent witnesses"; "public examination"). |
| C13 "dual-interpreter requirements" | CHG | "insisted on having second, independent interpreters" (C25). |
| C14 "designed to curb scribe dominance" | STILL | 3.3 ("Recognizing that scribes routinely defrauded"); Andrien reports circumvention. |
| C15 charter 1556/1557 | CHG | 1557 given with no note on Arber's 1556. |
| C16 journeymen petitions | STILL | 3.4 ("Junior printers ... journeymen printers to wage dependency"); the record is the Company's own 1643 petition against eleven patentees. |
| C17 print "defined by enclosure" | STILL | 3.4 closing sentence generalizes from one kingdom. |
| C18 Jomtien and Dakar "wide margins" | CHG | "roundly missed (UNESCO, 2015)"; the 2015 report supports Dakar only. |
| C19 UNESCO 2026 figures | OK | 739 million, 63 percent (year 2024 omitted). |
| C20 Graff "social discipline" | CHG | Now the "obedient factory workforce" claim (C26). |
| C21 Persepolis | GONE | Not in v2. |
| C22 TRC for US schools | OK | Newland (2022, 2024) now cited for the US. |
| D1 Knox for discretion | OK | Discretion now from *Katzenbach* and Kousser (but see C30). |
| D2 "uninterpretable scores (Rosenblat & Stark)" | STILL | 4.1 matrix "black-box scoring (Rosenblat, 2016)"; Rosenblat and Stark treat the fifteen-second offer. |
| D3 unsourced present-day cells | CHG | Promise row now cites Kamperman and Graff; record and monopoly cells still uncited and carry span tags. |
| D4 tense of "restricted" | GONE | |
| D5 digital identity platforms | GONE | |
| D6 "zero leverage" | STILL | 4.2 ("grants them zero power"). |
| D7 Yeung "pricing" | OK | Now feedback loops and choice architecture. |
| D8 early modern protections | STILL | 4.4 and 7.3 treat *Foster* (1869) and the Iroquois councils as early modern legal buffers. |
| D9 "strips these protections" | STILL | 4.4. |
| D10 Berthon et al. for antitrust | STILL | 5.5 ("antitrust enforcement, public utility regulation ... (Berthon et al., 2019; ...)"); a full-text search of that paper finds no such term. |

Totals over the 60 rows: OK 13, STILL 25, CHG 14, GONE 8.

## 8. What works and should be protected

The reference list is mostly sound where it relies on works the arm already verified (69 of 89 match). The Berthon, Pitt and Campbell, Williams, Kamperman and Graff (Myth #2), Jobin and UIS figures are accurate as now worded, and the corrections of A5-A7, A13, C9, C19, C22 and D7 held. The Dakar "50 percent" and the Auld block quotation are verbatim. The German Simmel terms are right. The Knox page locator is right.

## 9. What I could not check

Johansson in CR or SSOAR this session (relied on the arm's earlier DOI check); Monteiro (site unreachable); Phule's publisher; the Moser book (not opened); the end page of Dubal; Kousser (1974) and the "correctly explain" phrase; Bommasani et al. (2026) text (only the Crossref record); Kolt and Zong and Matias contents beyond their records; Jobin's counts (taken from the arm, not re-opened); Milton "p. 18"; Waitangi Tribunal pages beyond 354-355 in this session (relied on facet G for 386, 414-422, 514); the Cleveland and Wilson "identical legislation" and "successive presidents" claims beyond the two messages; Statutes of 1740, 1831 and 1503 (not re-opened; see facets C and G).

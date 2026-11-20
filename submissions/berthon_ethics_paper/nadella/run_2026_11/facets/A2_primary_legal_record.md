# A2 — The primary legal and official record: facet report

Agent-drafted. The author has not reviewed it and none of the text is his.

Written 2026-11-18 from `A2_primary_legal_record.log.md`. Cap of 10 cards reached; six targets not attempted.

## 1. Counts by read status

| source_basis | n | cards |
|---|---|---|
| full-text | 6 | louisiana1965louisiana, davis1949davis, guinn1915guinn, uscongress1982voting, uscongress1975voting, hansard1807parochial |
| partial-text | 4 | usccr1961voting, eci1955report, yorta2002members, saunders1971anglia |
| abstract | 0 | |
| secondary | 0 | |

Blocked routes, each followed by a clean route that worked: AustLII (challenge page), BAILII (bot wall noted in
references.bib), the Commission on Civil Rights' own path (404), govinfo and House U.S. Code pages for 52 U.S.C.
10508 (not found), CourtListener API (needs a key). No target was lost to a block. The six untried targets were
skipped at the cap.

## 2. Entries

| citekey | record verified by | read status | bearing by STRUCTURE section |
|---|---|---|---|
| louisiana1965louisiana | govinfo details page, official U.S. Reports PDF | full-text, 380 U.S. 145-156 | 3.2 supports and narrows; 4.4-contest; 7-D02 |
| davis1949davis | Caselaw Access Project volume metadata; affirmance confirmed in *Louisiana* at 153 | full-text (OCR of the reporter; recheck quotations against a page image) | 3.2 supports and narrows; 4.4-record; 4.4-contest; 7-D02 |
| guinn1915guinn | official U.S. Reports PDF (govinfo); key in references.bib | full-text, opinion pp. 354-368 | 3.2 narrows; 7-D02 (a prohibition evaded) |
| usccr1961voting | document's own title page and GPO imprint; law-library-hosted scan | partial-text, pp. 58-67, 133-142 | 3.2 supports; 4.4-record; 7-D02; 7-D04; counter |
| uscongress1982voting | official Statutes at Large print (govinfo) | full-text, 96 Stat. 131-135 | 3.1; 7-D04 supports; 7-D07 weak |
| uscongress1975voting | official Statutes at Large print (govinfo) | full-text, 89 Stat. 400-406 | 3.1, 7-D07 support; 7-D02; 3.2; 3.7 |
| eci1955report | scan title page; Crossref review record (Tinker 1956, 10.2307/2941789) | partial-text, pp. 10-11, 80-92 | 3.1, 7-D07 support; 7-D04 contests or narrows; counter |
| hansard1807parochial | Historic Hansard header; key in references.bib | full-text, cc. 798-806 | 3.3 supports; new-category (reading without writing); counter |
| yorta2002members | AustLII header in an Internet Archive capture; 214 CLR 422 matches scout | partial-text, paras 58-69, 96-125, 134-136, 143-146 | 3.4 supports with care; 4.4-record; counter |
| saunders1971anglia | BAILII header in an Internet Archive capture; key in references.bib | partial-text, Lord Reid and Lord Wilberforce in full | 3.4 supports; 4.4-loss; 7-D06 |

## 3. Corrections found in the record

| correction | form (question 3) | card | duty it could stand behind |
|---|---|---|---|
| Injunction against Louisiana's interpretation test; reregistration of all voters before a new test; monthly reports to the court | prohibition, plus equal exposure and a reporting duty | louisiana1965louisiana | 7-D02 |
| Boswell Amendment ("understand and explain") enjoined; the court named a uniform test producing a record for review as the acceptable alternative | prohibition; record for review named | davis1949davis | 7-D02; 7-D04 (record) |
| Oklahoma's 1866 exemption void; literacy test falls only by severability | prohibition, evaded by a discretionary test (*Louisiana* at 148, 151) | guinn1915guinn | 7-D02 (as a cautionary case) |
| Six completed grades suffice wherever a literacy or understanding test applies (Recommendation 2, a proposal) | check moved off the examiner onto an objective proxy | usccr1961voting | 7-D02 |
| Voting assistance by a person of the voter's choice, not the employer or union | helper owed to the weaker party, chosen by that party | uscongress1982voting | 7-D04 |
| All election materials and ballots in the minority language, or orally where the language is unwritten; permanent ban on tests or devices | work moved onto the instrument; prohibition | uscongress1975voting | 7-D07; 7-D02 |
| Ballot box per candidate with pictorial symbols; no mark needed; official helper rejected to keep the secret ballot | work moved onto the instrument | eci1955report | 7-D07 |
| *Non est factum* for those who cannot read or understand through no fault of their own, conditioned on care; notary named as the absent check | narrow shift of risk; check of understanding named, not provided | saunders1971anglia | 7-D06 |

## 4. What each STRUCTURE section in scope can rest on

- **3.1 (the correction):** uscongress1975voting (full-text: the state's materials in the voter's language);
  eci1955report (partial-text: symbols on the ballot boxes); uscongress1982voting (full-text: a helper the voter
  chooses). Three modern statutory or official instances.
- **3.2 (the gate):** louisiana1965louisiana (full-text), davis1949davis (full-text, OCR), usccr1961voting
  (partial-text), guinn1915guinn (full-text). All four condemn discretion or racial purpose; none condemns literacy
  as a qualification. *Guinn* and *Davis* affirm the state's power to require it.
- **3.3 (withheld competence):** hansard1807parochial (full-text) only, for 1807 England; this facet carded no
  anti-literacy statute.
- **3.4 (record over voice):** yorta2002members (partial-text); saunders1971anglia (partial-text). *Tilden* not
  carded.
- **3.5 (monopoly):** UNSUPPORTED from this facet. Locke's memorandum and the Stamp Act 1712 were skipped at the cap.
- **3.6 (promise):** UNSUPPORTED from this facet. Persepolis and the EWLP assessment were skipped at the cap.
- **3.7 (standard):** uscongress1975voting (full-text) only, on language; Macaulay's Minute was skipped at the cap.
- **7-D02:** louisiana1965louisiana, davis1949davis, usccr1961voting, uscongress1975voting.
- **7-D04:** uscongress1982voting (supports); eci1955report (contests: helper as a threat to secrecy).
- **7-D06:** saunders1971anglia (the notary as a named but absent check).
- **7-D07:** uscongress1975voting, eci1955report.

## 5. Claims in STRUCTURE.md, ARGUMENT_AND_OUTLINE.md or the ledger that these sources contradict or strain

- **STRUCTURE §5, "intent (the 1901 tests) versus position (agents)":** the record condemns more than intent.
  *Davis* held the Boswell Amendment void under the Fourteenth Amendment for arbitrary power alone (81 F. Supp. at
  878). USCCR Finding 12 calls such practices arbitrary "whether or not they are clearly racially discriminatory"
  (p. 138). *Louisiana* quotes an 1898 delegate objecting to the registrar's unreviewable power (380 U.S. at 152).
  This supports ruling 6's position-based reading and weakens the disanalogy as STRUCTURE states it.
- **ARGUMENT_AND_OUTLINE A2 (work moved onto the artifact *or* onto a party owed to the weaker side):** the Election
  Commission of India rejected the second course because an official helper ends the secret ballot (eci1955report,
  p. 80). The two courses are not interchangeable where secrecy matters; s. 208's voter-chosen helper (1982) is the
  form that survives that objection.
- **ARGUMENT_AND_OUTLINE D04 precedents (Easton 1757; Appeals Centre Europe):** not contradicted, but s. 208 of the
  Voting Rights Act (uscongress1982voting) is a working U.S. legal precedent the row omits.
- **A3 ("recognised as a failure in its own time"):** supported for the gate (1898 delegate; 1946 Alabama lawyer in
  *Davis*) and for 1807 (Whitbread). It is strained for *Guinn*, where the Court named the exemption, not the
  reading test, as the wrong. USCCR's dissenters (p. 140) show the case for the test was also made openly in 1961.
- No claim was found that *Saunders* or *Yorta Yorta* contradicts, though both are narrower than their usual
  summaries (see cards).

## 6. Gaps and blocks

| item | status | where a library user would find it |
|---|---|---|
| Tilden Rent-A-Car Co. v. Clendenning (1978) (reporter citation not verified in this run) | not attempted (cap) | Ontario Reports in a law library; CanLII |
| Locke's memorandum on the Licensing Act (1694-95) | not attempted (cap); scout record is an EEEO dataset entry dated 1695 | Electronic Enlightenment (subscription); printed Locke correspondence editions |
| Stamp Act 1712 (10 Anne c. 19) | not attempted (cap) | Statutes of the Realm / Statutes at Large, law library |
| Declaration of Persepolis (1975) | not attempted (cap); scout has the chapter DOI 10.1016/b978-0-08-021385-9.50026-1 | Bataille (ed.), *A Turning Point for Literacy* (Pergamon 1976); UNESDOC |
| UNESCO/UNDP, *The Experimental World Literacy Programme: A Critical Assessment* (1976) | not attempted (cap); scout NOT FOUND under that title | UNESDOC; university library |
| Macaulay, Minute on Education (1835) | not attempted (cap); scout copy on disk at `A2/macaulay1835/` | Sharp (ed.), *Selections from Educational Records*, Part I (1920) |
| S. Rep. 97-417; H.R. Rep. 94-196; S. Rep. 94-295 (VRA committee reports) | not opened | Congressional Serial Set; government-documents library |
| Olney J's trial judgment in Yorta Yorta (citation not verified in this run) | not opened | Federal Court of Australia reports |
| 52 U.S.C. 10508 current text | govinfo and House Code pages failed | U.S. Code in print or a law library database |
| Davis v. Schnell page images | text is OCR | Federal Supplement vol. 81, law library |

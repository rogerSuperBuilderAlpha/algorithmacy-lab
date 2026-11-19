# Adjudication of the N-round audits

*Written by Claude (the lead) on 2026-10-24. Lead-written record of decisions; not paper prose. The audits are
`AUDIT_N7a.md` (history: N2, N3 and legacy history-side cards) and `AUDIT_N7b.md` (present and method: N1, N4, N5).
N6's eight cards were audited by the lead (§4).*

## 1. Rates as reported

| Audit | Rows | VERIFIED | WRONG | OVERSTATED | NEEDS LIBRARY CHECK | COULD NOT CHECK | Legacy sample disagreement |
|---|---|---|---|---|---|---|---|
| N7a | 84 | 60 (49 verbatim, 11 paraphrase) | 4 | 16 | 4 | 0 | 2 of 9 (22%) |
| N7b | 131 | 112 (97 verbatim, 15 paraphrase) | 6 | 11 | 1 | 1 | 0 of 5 (0%) |
| Lead, N6 | 8 cards, 41 quotations | 8 cards verified | 0 | 0 | 0 | 0 | — |

Hashes: every new card's `sha256` matched its file (35 of 35 in N7a's scope, 61 of 61 in N7b's, 8 of 8 in N6).
No DOI in scope carries a Crossref update or retraction notice.

## 2. How the lead decided

The lead accepted every fix the two audits give. Before doing so the lead reopened the source for the WRONG rows and
for the overstatements that change a premise:

| Row | Source reopened | Finding |
|---|---|---|
| N7a N3-9 (Jones v. Meehan rent) | `pdfs/V3/cap_jones_meehan.html` | Approved 27 Dec. 1894 "upon condition ... that the annual rent should be four hundred dollars": audit right |
| N7a N2-13 (*Supplication* and the 1543 Act) | `N2/supplications/asupplicacyonfo02cowpgoog.txt` | The petition's "lawe" bars having "the Scripture in his house, onlesse he maye spend x. pound": a possession test by income, not the Act's reading bar by rank and sex; identification is probable, not shown |
| N7a N3-13 (Cuban counts) | arithmetic | 120,632 + 147,788 = 268,420: the counts reconcile |
| N7a N3-22 (grade cards) | `N3/simon2005/simon2005.pdf` | "was associated with a 13.1 percent decrease": association, not a clean causal result |
| N7b `anthropic2026thinking` and the N1 C4 row | `N1/ant_thinking_overview/page.html` | "In rare cases where you need access to full thinking output, contact Anthropic sales": audit right |
| N7b `palod2026evaluating` | `N1/arx_palod2026/page.pdf`, Table 3 | Misjudgment 54.0 (trace) against 54.2 (solution only): audit right |
| N7b `euomnibus2026` | `N4/omnibus/32026R1744.txt` | "By way of derogation from Article 73": audit right |

The remaining OVERSTATED rows turn on readings the audits quote from the source; the lead accepted them as written.

## 3. Card decisions

**New cards (106).** The 32 corrections below were applied to the card bodies under the lead's instruction, each
exactly as the audit words it; every new card then received an `## S2 adversarial verification` block and its
`verified` value.

- `corrected` (32): N2: boretius1883capitularia, commons1803journal, cranmer1846miscellaneous, furnivall1871four,
  reusch1883index, starchamber1637decree, statutesrealm1819vol4. N3: alvord1868fifth, jones1899meehan, kempf2014cuban,
  lely1883judicature, parker1877south, tam2015participants. N1, N4, N5: anthropic2026thinking, google2026agentic,
  shavit2023practices, palod2026evaluating, parikh2025powering, euomnibus2026, kingston2026social, luchs2026taking,
  vonsamson2025immanent, gornet2024european, microsoft2026enabling, openai2026reasoning, anthropic2026usage,
  anthropic2026measuring, frontiermodelforum2026information, bartha2019analogy, celikates2023critical,
  lovett2026republicanism, corporateeurope2025bias.
- `true` (74): the other 66 audited cards (N7a's 24 and N7b's 42 "mark true" lists) and N6's 8.
- `pending`: none.

**Legacy cards.** Cards in `berthon_ethics_course/`, `dxd_foundation/` and `algorithmacy_design_ethics/` are
byte-identical copies of other arms' cards (`../../PROVENANCE.md`); editing them here would break provenance. Their
verdicts are recorded here only and should be applied in the origin arms:

| Card | Verdict | Fix for the origin arm |
|---|---|---|
| pike1873history, statute1827criminal, roberts1835memoirs | confirmed | mark `true` |
| willis2008against | corrected | the Summary's "rests on the abstract only; the repository returned 403" is stale: the draft was read |
| almeida2019firmo | corrected | p. 29 quotation begins "y la consiguiente firma", not "con la" |
| graff1991literacy | keep pending | pages are from the 1991 reissue; the 1979 pages need a library copy |
| nussbaum2011creating | keep pending | p. 20 confirmed one way only; no local copy |
| havelock1963 | keep pending | read from an unauthorised upload; wording confirmed on the 1963 lending scan, pages need a library copy |
| burnyeat1997postscript, delgamuukw1997, holmes1975kousser, israeli2022requerimiento, knox1968silent, mccord1840statutes, unesco2000dakar, balkin2016information, claassen2024wealth, microsoft2025ai, microsoft2025responsible, nadella2026models | confirmed as recorded | none (burnyeat's basis is secondary; the coverage matrix's "partial+verified" label overstated it) |

## 4. The lead's audit of N6's cards

| Card | Record | sha256 | Quotations and locators | Verdict |
|---|---|---|---|---|
| moffatt2024air | Tribunal decision header: 14 Feb 2024, SC-2023-005609, Christopher C. Rivers | match | 9 of 9 present; paras 26-29 confirmed by paragraph order | true (copy from the Internet Archive's capture of the Tribunal's URL; see §5) |
| cedillo2026from | EJLT article page: vol. 17(1), 2 Jul 2026; no Crossref record | match | 8 of 8 present; "censor" absent, as the card says | true |
| gowans2026moral | SEP page: first published 19 Feb 2004, revised 28 Jun 2026; §7 "Mixed Positions" | match | 6 of 6 present | true |
| lindman2023big | JIT 38(2) 144-159 (read in full by the lead earlier this session) | match | 5 of 5 present; pages from running heads | true |
| calo2012against | NDLR 87(3) 1027-1072; printed page = PDF page + 1026 (PDF p. 23 = 1049) | match | 9 of 9 present on the stated pages | true |
| cinar2025understanding | Crossref: JIPLP 20(10) 681-691, 3 Sep 2025; no updates | match (record file) | abstract only, paraphrase | true (abstract depth) |
| lastowka2012walled | Crossref: IDP no. 15, 31-49, 31 Dec 2012 (Catalan title) | match (record file) | abstract only, paraphrase | true (abstract depth) |
| mahardhika2026gutenberg | Crossref: SSRN 10.2139/ssrn.7277362 (2026) | match (record file) | abstract only, paraphrase | true (abstract depth) |

**N6 facet text.** Two items in `N6_counter_case_and_gap_search.md` are quoted from WebFetch summaries, not from
opened text (Microsoft's Copilot Copyright Commitment post; Pillitteri's blog). They carry no card and may not be
quoted in any draft until a page is opened and carded.

## 5. Rulings for the author

1. **Internet Archive copies of blocked pages.** Two cards rest on Internet Archive captures of pages whose live
   sites refused scripted requests: `moffatt2024air` (the Tribunal's own document URL) and N7b's reading of OpenAI's
   Service Terms §14 (no card yet; snapshot 20261006184704). The lead treats the public archive as a permitted route
   (earlier facets used archive.org throughout) but it is the author's call. If not permitted, Moffatt drops to the
   CanLII or Tribunal text by hand, and "four vendors" stays at three.
2. **Saenger p. 11.** Located only in the unauthorised copy; still unquotable. N2's facet entry repeats the wording
   without quotation marks; the draft must not use it until a clean route confirms the page.
3. **SB 53.** N4 read the bill from the Legislature's official bulk download after leginfo served a challenge page.
   The lead treats the official bulk route as permitted.

## 6. Premise rows the audits changed

These replace the "Round-1 findings" wording in `../COVERAGE_PREMISES.md` (applied there as v2).

| Premise | As stated after audit |
|---|---|
| A1 | The four design questions are the author's ruling; Lovett and Hamilton support only the fourth (who may contest) |
| A2, A3 (1543) | The 1546 *Supplication* objects to "a lawe" keeping Scripture from the poor; its identification with the 1543 Act is probable, not shown. The Act's own preamble and Cranmer's 1540 prologue carry the broken-standard route |
| A2 (disclosure) | Restaurant grade cards were *associated with* a 13.1% fall (Simon 2005, ecologic design, named confounds); diners read the letter (Jin and Leslie, abstract). The failure the record supports remains disclosure that leaves the reading to the person bound |
| A3 (literacy) | The 2015 GMR attributes most gains to cohort replacement and casts "considerable doubt" on adult programmes' impact; no source shows Jomtien blaming the learner |
| A4 (chain of thought) | No API setting returns the raw chain of thought (OpenAI, Anthropic, Google); Anthropic offers full thinking output through sales |
| A4 (responsibility) | Three carded vendors put responsibility for actions on the user (Microsoft, Anthropic; Google's terms bind the API developer); OpenAI §14 says the same but is uncarded |
| A4, M2 | EU harmonised standards, once cited in the OJ, form part of EU law and bind in practice through the presumption of conformity, though compliance is not compulsory (CJEU C-588/21 P, paras 70-75) |
| A4, M9, O02 | Notice without standing holds for AI Act art. 73, SB 53 and NIS2 art. 23; GDPR (arts. 79, 82) and the Product Liability Directive give remedies |
| A4, M4 | Microsoft's customer-facing audit log missed a Copilot file access that Microsoft's internal logs captured: a record kept by one side (M4(a)), not an absent record |
| A4, M8 | Shavit et al. give shutdown to the user and, redundantly, to the deployer and data-centre operator, and ask when a third party may terminate an agent |
| A5 | Holds for Nadella's post and Microsoft's agent controls. AP2 (user-signed mandates checked by merchants, with only the closed mandates' constraints shared) is a partial counter-instance to a general form of A5, not to A5 as written |

# AUDIT_00: citation audit, batch 0 (odd positions, 60 keys)

Audit date 2026-10-01. Method: every .bib entry with a DOI was resolved against Crossref (authors, year, title, venue, volume, issue, pages) and checked for corrections or retractions via Crossref `updated-by`; arXiv records checked for the three preprints; each citing sentence in DRAFT.md was compared with the facet notes, and quotations were re-checked against source text where I could open it (Perseus for Plato; HAL for Mirault et al.; arXiv for Tankelevitch, He et al., Kazemitabaar et al., Cabrera et al.; Cambridge OA PDF for Hansen; PMC for Padilla, Maier et al., Bastani correction). Where I could not open the source, the row says "facet only".

No retraction was found for any key. Corrections or errata exist for four: Bastani (affiliation only), Padilla (Table 2 formatting only), Gerlich (a Table error; Gerlich is not relied on), Budzyn (Lancet erratum 2025-11, content not retrievable; see row).

Cross-batch flag: "Bansal, Nushi, et al., 2019" in DRAFT.md names two different papers with the same first three authors (Beyond Accuracy, HCOMP 2019 = bansal2019beyond; Updates in Human-AI Teams, AAAI 2019 = bansal2019updates). APA needs 2019a (Beyond) and 2019b (Updates). The error-boundary sentence in the "display the declared operating envelope" list item cites Beyond Accuracy and is left for batch 1.

| key | bib status | claim status | fix |
|---|---|---|---|
| adler1996two | OK (Crossref match; end page 89 from standard citation, Crossref gives 61 only) | OK; "better to master their tasks" is from the abstract; abstract only | none |
| alfrink2023contestable | OK (online-first 2022, vol 33(4) is 2023) | OK ("sandboxing"); card-based | none |
| attewell1987deskilling | OK | OK at abstract depth ("catalogued" is slightly strong for "series of criticisms") | none |
| bagger2023digital | OK (no pages; article-number journal) | OK; quote "opting out ... is generally not perceived as an option" and "mandating digital participation" p. 3 per full-read facet | none |
| bainbridge1983ironies | OK | OK; all four quotations and pp. 775-777 confirmed by the library card's S2 check. "Backward-compatible updates" is not Bainbridge's; her p. 777 point is pace and criteria the operator can follow | none (the later text already says the update requirement rests on the human-AI evidence and Bainbridge) |
| bansal2019updates | OK (Crossref match) | Content supported (update lowering team performance, facet read in full). Citation form ambiguous with bansal2019beyond | 2019b disambiguation, three places (below) |
| bastani2025generative | OK. Correction 10.1073/pnas.2518204122 changes one author affiliation only | OK: 48%, 17%, "crutch", "do not perceive any reduction", "though we still do not observe a positive effect" all match the facet read | none |
| belland2017synthesizing | OK (online 2016) | OK (144 studies, g = .46, scaffold change did not moderate); abstract only | none |
| braverman1974labor | Not verifiable (book; Open Library gives 1975, 1974 is the usual year) | Paraphrase only, via secondary abstracts; no quote | none; confirm year against a copy |
| brynjolfsson2025generative | OK | OK; outage inference is the authors' own and "noisy" | none |
| budzyn2025endoscopist | OK. A Lancet erratum exists (10.1016/S2468-1253(25)00294-8, Nov 2025); I could not retrieve its content | 28.4% to 22.4% and "might reduce" confirmed against the Europe PMC abstract | bib note so the erratum is checked before figures are quoted in a final |
| cabrera2023improving | OK (Crossref pp. 1-21, article 136) | OK; "p. 2" is the arXiv pdf page, which equals 136:2 in the published layout; learning-slope claim matches facet | none |
| cameron2024good | OK | OK; abstract only, and the draft hedges it | none |
| casner2014retention | OK | OK; quote matches abstract | none |
| chiang2022exploring | OK | OK; abstract only | none |
| costin2020meaning | OK | OK | none |
| dellacqua2026navigating | OK (Crossref spells "Lifshitz") | OK; used only as a performance study | none |
| dorrestijn2013technology | OK (no DOI; Twente PDF) | OK; quotations pp. 52, 53 match the facet | none |
| eslami2015always | OK | CONTRADICTED. Abstract: "algorithmic awareness led to more active engagement with Facebook and bolstered overall feelings of control"; 83% reported changed behaviour at follow-up (F5). "Awareness without agency" is not what the paper reports. The same claim is in the live Part 1 (lines 136-138); flag for the author | text fix below |
| fernandes2026ai | OK (published title; arXiv title differs) | OK | none |
| gavrilov1997techniques | OK | Abstract only. "Closed the question" is Johnson's (2000) characterisation, not read first-hand | none; limitation already stated |
| gerlich2025ai | OK. A Correction (10.3390/soc15090252) fixes a Table error | OK: draft says it is not relied on | bib note |
| gray2018dark | OK | MISCHARACTERISED. Gray et al. is a qualitative content analysis of 118 artifacts producing a five-strategy taxonomy, not an audit (Mathur et al. 2019 is the audit) | text fix below |
| hansen2016definition | OK | OK. Verified in the OA PDF: the "easy or cheap to avoid" passage cites Nudge p. 8 footnote (fn 12); p. 158 "cognitive boundaries, biases, routines and habits" | none |
| he2025conversational | OK | Quote verified in arXiv text (6.1 Key Findings). It belongs to the LLM-agent condition; the draft reads as if it covers the whole conversational interface | text fix below |
| heintzelman2013encounters | OK | OK | none |
| hirschman1970exit | OK | OK; pp. 33, 34, 40 quotations match the scan-based facet | none |
| hutchins1985direct | OK | OK; "to minimize cognitive effort" p. 318 per facet | none |
| kahneman2009conditions | OK | OK; abstract sentence verified in facet | none |
| kazemitabaar2024improving | OK | Quote verified in arXiv text; n = 18 | none |
| kim2024notsure | OK | OK | none |
| kosmyna2025brain | arXiv 2506.08872v2 confirmed; no journal record | Draft says "a published critique"; the critique (Stankovic et al., arXiv 2601.00856) is itself an unrefereed preprint | text fix below |
| kulesza2012tell | OK | OK | none |
| lave1991situated | OK (book; metadata only) | Presupposition of an old-timer is the card's reading; book unread | none |
| lehmann2024ai | Bib year is 2025 (v2); DRAFT cites 2024 | Two defects: year mismatch; the "sign depending on substitution" result comes from exploratory analyses and a field study, not from the two preregistered experiments | text fix below |
| leutner2000double | OK | Overstated: Experiment 2 found the approach "less effective", not that it failed | text fix below |
| lukoff2021how | OK | OK | none |
| maier2022noevidence | OK. It is a PNAS Letter re-analysing Mertens et al. (2022); a reply exists | "Indistinguishable from zero" is stronger than the letter: it finds no evidence for an overall effect, evidence undecided for "structure" interventions, and heterogeneity implying "some nudges might be effective" | text fix below |
| martela2023role | OK (online 2022, vol 18(4) 2023) | OK; abstract only | none |
| mekler2019framework | OK (Paper 225 not in bib) | OK per card; locators pp. 5, 10 | none |
| mirault2019reading | OK | Quote "with ease" is NOT verbatim. HAL text p. 22: "the ease with which skilled readers can read text presented without spacing". 40-70% confirmed ("slower by about 40% to 70%") | text fix below |
| nissenbaum2011contextual | OK | OK; pp. 35, 43 per card (full read) | none |
| obar2020biggest | OK (online 2018, 23(1) is 2020) | OK (N = 543, 74%, 97%) | none |
| ong1982orality | Bib year 2002, origdate 1982; Part 1 cites "Ong (1982/2002)" | In-text form differs from Part 1 and from the bib | text fix below |
| padilla2018decision | OK. Correction 10.1186/s41235-018-0126-3 concerns Table 2 formatting only | Quotation "was not observed with textual representations of the same data" verified in PMC text; it is Padilla et al. reporting Grounds, Joslyn and Otsuka (2017) | none |
| parasuraman2010complacency | OK | OK; quote is in the abstract | none |
| peters2006numeracy | OK | Mild overstatement: the paper shows numeracy effects on framing and affect-laden judgments "not due to general intelligence", and says high numeracy "may sometimes lead to worse decisions"; "predicts decision quality" generalises | text fix below |
| plato1925phaedrus | OK | All four quotations verified verbatim against Perseus (Fowler): 275a (three) and 275d | none |
| ratner2016effects | OK | OK | none |
| reiser2004scaffolding | OK | OK; abstract only | none |
| rintakahila2023vicious | OK | Both quotations match the abstract (abstract only) | none |
| robertson2023diverse | OK | OK (52.9% chose the human) | none |
| saenger1997space | OK (book; no volume or pages) | One error: p. 77 says pagination or foliation of Greek codices in scriptura continua is documented by the third century, not that "the codex itself" is. The p. 69 date for scriptura continua (late 2nd or 3rd c.) is from a snippet whose subject was not visible; re-check in context. p. 8 Ambrose quotation and p. 11 quotation match the facet | text fix below |
| shen2026skill | arXiv 2601.20245 confirmed; no journal record | OK (52 developers, 17%); Anthropic affiliation is disclosed | none |
| sinha2021when | OK | OK | none |
| speekenbrink2010learning | OK | Incomplete: the facet says to cite both halves; the paper's participants tracked abrupt and gradual change | text fix below |
| street1984literacy | Not verifiable (book unread; secondary via Armer 1992) | Paraphrase only; "dismantled" is the author's Part 1 register | none |
| susser2019technology | OK | OK; p. 7 quotation per facet | none |
| tankelevitch2024metacognitive | OK | Quote verified in arXiv v3; it is on pdf p. 6; "metacognitive monitoring" supported | none |
| tetzlaff2025cornerstone | OK | OK (d = 0.505, -0.428, asymmetry) | none |
| treisman1980feature | OK | OK; the strict feature/conjunction split has since been contested (facet), which the draft does not claim | none |
| vaccaro2020facebook | OK (Crossref title reads "Does What ItWants", a Crossref spacing artefact) | Quote verified in facet (5.1); vignette study | none |
| vallor2016technology | OK (book) | OK; pp. 161, 164 quotations match the facet (snippet depth) | none |
| vasconcelos2023explanations | OK | OK; p. 129:3 per card | none |
| viljoen2021relational | OK | MISREAD. Viljoen argues population-level (horizontal) data relations need collective institutions, and her card says individual or client-side agents "leave the population-level relation untouched". The draft calls her proposals "relational data-governance ... at the level of one relation" | text fix below |
| wood2019good | OK (online 2018, 33(1) is 2019) | OK | none |
| zamfirescupereira2023why | OK | Facet: "most" participants declared success after one improved utterance; the draft implies all. Not checked against the paper (ACM PDF blocked) | text fix below |

## Items for the author

1. Eslami et al. (2015) in Part 1 (published text, lines 136-138): the paper reports raised felt control and engagement after FeedVis, so "neither cultivated ... meaningful agency" needs a source check. Not changed here.
2. Peters et al. (2006) in Part 1 line 122 ("proved that numeracy predicts resistance to framing") is accurate; only the Part 2 gloss "decision quality" is loose.
3. Budzyn erratum content could not be read; confirm the 28.4% to 22.4% figures against the corrected article before the final.

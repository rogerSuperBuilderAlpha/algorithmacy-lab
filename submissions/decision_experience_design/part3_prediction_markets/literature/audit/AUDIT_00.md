# AUDIT_00: citation audit of the load-bearing set (Part 3)

Audit date 2026-10-03, by Claude, after the eight-seat research run. Not author text.

**Scope.** No draft exists, so the audit covers the sources that `ARGUMENT_MAP.md` and `OUTLINE.md` rest on,
not all 518 facet entries. I opened each record below myself (Crossref `/works/<DOI>`, the arXiv API, or the
document) and compared it with the facet .bib. The other entries carry only the facet agents' own Crossref or
OpenAlex checks; they need this audit before any of them enters a draft. I found no correction or retraction
notice on the 28 Crossref records where I checked the `update-to` field (all but `hanson2007logarithmic`).

## Metadata: 32 records opened; 30 match outright, 2 carry known Crossref quirks (`hanson1999decision`, `hanson2007logarithmic`)

| key | record opened | result |
|---|---|---|
| wolfers2004prediction | Crossref 10.1257/0895330041371321 | match: JEP 18(2), 107–126 |
| manski2006interpreting | Crossref 10.1016/j.econlet.2006.01.004 | match: Economics Letters 91(3), 425–429 |
| cowgill2015corporate | Crossref 10.1093/restud/rdv014 | match: RES 82(4), 1309–1341 |
| choo2022manipulation | Crossref 10.1287/mnsc.2021.4213 | match: Management Science 68(9), 6716–6732 |
| chen2011decision | Crossref 10.1007/978-3-642-25510-6_7 | match: LNCS, 72–83 (Crossref gives no volume; bib has 7090) |
| wolfers2006interpreting | Crossref 10.3386/w12200 | match: NBER working paper |
| kalda2021smartphone | Crossref 10.3386/w28363 | match: NBER working paper, four authors |
| chapkovski2024gamification | Crossref 10.1287/mnsc.2022.02650 | match: Management Science 72(1), 32–56, 2026. The key says 2024 (online-first year) |
| rockloff2026direct | Crossref 10.1111/add.70369 | match: Addiction 121(7), 1907–1919, six authors |
| seru2010learning | Crossref 10.1093/rfs/hhp060 | match: RFS 23(2), 705–739 |
| gigerenzer1995frequency | Crossref 10.1037/0033-295x.102.4.684 | match |
| peters2006numeracy | Crossref 10.1111/j.1467-9280.2006.01720.x | match: Psychological Science 17(5), 407–413, six authors |
| fiedler2019myopia | Crossref 10.1002/bdm.2109 | match: JBDM 32(3), 317–333 |
| westwood2020projecting | Crossref 10.1086/708682 | match: JOP 82(4), 1530–1544 |
| stout1999 | Crossref 10.2307/1373070 | match on author, year, title, Duke Law Journal 48(4); Crossref gives first page 701 only, bib has 701–786 (end page unconfirmed) |
| diercks2026kalshi | Crossref 10.17016/FEDS.2026.010 | match: FEDS 2026-010, three authors |
| smith2006p2p | Crossref 10.1111/j.1468-0335.2006.00518.x | match: Economica 73(292), 673–689 |
| dana2019are | Crossref 10.1017/s1930297500003375 | match: JDM 14(2), 135–147 |
| hanson1995gambling | Crossref 10.1080/02691729508578768 | match: Social Epistemology 9(1), 3–33 |
| hanson1999decision | Crossref 10.1109/5254.769877 | DOI is the department article (Hearst, "Hunson" [sic], Stork; pp. 16–20), as facet H records |
| hanson2003combinatorial | Crossref 10.1023/A:1022058209073 | match: ISF 5(1), 107–119 |
| hanson2007logarithmic | Crossref 10.5750/jpm.v1i1.417 | vol. 1(1), 3–15 confirmed; Crossref issued-date 2012-12-13 and title misspelled, as facet H records. The year 2007 rests on the volume number and facet H's read; not confirmed by me against the journal |
| hanson2013vote | Crossref 10.1111/jopp.12008 | match: JPP 21(2), 151–178 |
| hanson2006information | Crossref 10.1016/j.jebo.2004.09.011 | match: JEBO 60(4), 449–459 |
| hanson2009manipulator | Crossref 10.1111/j.1468-0335.2008.00734.x | match: Economica 76(302), 304–314 |
| hanson2006terrorism | Crossref 10.1007/s11127-006-9053-9 | match: Public Choice 128(1–2), 257–274 |
| arrow2008promise | Crossref 10.1126/science.1157679 | match: Science 320(5878), 877–878, 22 authors |
| burgi2026makers | Crossref 10.65864/s9kc4p0b7t | match: CESifo Working Papers, three authors |
| macey2026 | Crossref 10.67929/ecgi-law-955-2026 | match on authors and title |
| rasooly2025manipulable | arXiv 2503.03312 | match: two authors, 2025-03-05 |
| sah2026visualizations | arXiv 2608.16814 | match: four authors, 2026-08-17 |
| cardozo2026flb | arXiv 2609.12878 | match: two authors, 2026-09-11 |

`hanson2008insider` has no Crossref or OpenAlex record (facet H); its volume and pages rest on Hanson's CV.

## Claims: 11 checked against the source text, 11 confirmed

| claim | source opened | result |
|---|---|---|
| "Over 90% of Kalshi's trades in 2025, representing 95% of its revenue, were sports related" | Ninth Circuit opinion, cdn.ca9.uscourts.gov, No. 25-7516 | verbatim. The court's record citation for the figure is not traced |
| Kalshi "advertises itself as 'the first app for legal sports betting in all 50 states'"; "Kalshi has a gambling problem" | same | verbatim |
| "The classic example is a contract on the outcome of a sporting event"; games "are unlikely to serve any 'commercial or hedging interest'" | Kalshi appellee brief, D.C. Cir. No. 24-5205, RECAP copy | verbatim |
| Risk-mitigation analysis "is included in Confidential Appendices C, D, and E" | Kalshi self-certification, cftc.gov ptc01222514045.pdf | verbatim |
| Sports 80% of Kalshi volume, 39% of Polymarket, since July 2024; notional taker volume | Pew short read, 2026-05-27 | verbatim |
| Makers −9.64%, takers −31.46% average return per contract | Bürgi, Deng and Whelan, karlwhelan.com/Papers/Kalshi.pdf | verbatim |
| 23% fewer bets, 39% less money, 67% fewer harms; n = 227; "not pre-registered and so should be considered exploratory" | Rockloff et al., Europe PMC PMC13291081 | verbatim |
| Sports longshot return +2.43% [−0.93, 5.79], favorite −0.230%; "Sports is the clearest exception" | Cardozo and Rivero-Wildemauwe, arXiv PDF | confirmed in the table and text |
| Morale markets: "trade on topics that ordinary employees find fun and interesting" | Hanson, insiderbet.pdf (author preprint) | verbatim |
| Safe harbor "would presumably not include contracts on the outcomes of sports events" | Arrow et al., Science PDF on Hanson's archive | verbatim |
| Mansour's M.Eng. thesis is on deep learning | MIT DSpace record 1721.1/121680 | title confirmed: "Deep neural networks are lazy: on the inductive bias of deep learning" |

## Not audited by me

Everything else in the facets, including: Mansour's interview quotations (facet M checked them against page
text); the Overcoming Bias and transcript quotations in facet H; the Third and Sixth Circuit opinions; the
CFTC documents in facet L; facet D's API computations (scripts are outside the repo, in the session
scratchpad, and two of three Kalshi passes hit a page cap); the UK Gambling Commission figures; Dana et al.,
Smith et al. and Manski page-level numbers.

## Cross-facet inconsistencies

- Facet A lists `arrow2008promise` as not obtained; facet H read it in full and I confirmed a quotation from it.
- The Sixth Circuit ruling is `ca6_2026schuler` in facet L and `ca62026orgel` in facet M (consolidated cases, one opinion).
- The Ninth Circuit ruling is `ca9_2026assad` (L) and `ca92026assad` (M); the Third Circuit ruling likewise has two keys.
- Facet D cites Diercks et al. by an SSRN DOI under `diercks2026macro`; facets M and X use the FEDS DOI.
- Facet X's entries for Cardozo, Sah, Bürgi and Pew lack the DOIs or URLs the other facets carry.

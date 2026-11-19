# Premise coverage: which cards carry each premise

*Written by Claude on 2026-10-24. v0, before the N1–N7 research runs (`facets/BRIEF.md`). Lead-maintained; the
table below is generated from `ARGUMENT_AND_OUTLINE.md` (the Support column's ledger IDs), the ledger's card column
(`../consolidation/CONCEPT_LEDGER.md`) and `../literature/CARD_INDEX.md`. "full+verified" and "partial+verified" mean
the card's own `verified` field or S2 verdict is true, corrected, S2 confirmed or S2 corrected; a partial card carries
a quotation only for the pages in its `pages_read`.*

## v0 matrix (ledger-derived)

| Premise | Ledger rows | Cards by class (v0) | Cards |
|---|---|---|---|
| A1 | H24 | full+verified 1; full, writer-grounded 1 | california2025civil (full, writer-grounded), lestrange1934graucob (full+verified) |
| A2 | H01, H04, H07, H11, H13, H19, H24, H26 | full+verified 21; full, writer-grounded 3; no card 1; partial+verified 16; partial, writer-grounded 3 | alabama1832acts (full+verified), alabama1901official (partial+verified), arber1875transcript (partial+verified), badger1996 (full+verified), burnyeat1997postscript (partial+verified), california2025civil (full, writer-grounded), delgamuukw1997 (full+verified), douglass1845narrative (full+verified), gaston1969gaston (full+verified), gavrilov1997techniques (partial+verified), georgia1830acts (partial+verified), giesler2014creating (full+verified), graff1991literacy (partial, writer-grounded), havelock1963 (partial+verified), hill1997gateway (full, writer-grounded), holmes1975kousser (full+verified), johns2002how (full+verified), johnson2000toward (no card), kamperman2026ai (full+verified), katzenbach1966south (full+verified), knox1968silent (full+verified), lestrange1934graucob (full+verified), margo2005williams (full+verified), marshall1999 (partial+verified), mccord1840statutes (partial+verified), messick1993calligraphic (partial+verified), milton1644areopagitica (partial, writer-grounded), mirault2019reading (full+verified), morales2008sun (full+verified), northcarolina1831acts (partial, writer-grounded), parkes1992pause (partial+verified), rayner1998unspaced (partial+verified), saenger1997space (partial+verified), specht2002netscape (partial+verified), statutesrealm1819vol5 (full+verified), uis2026adult (full+verified), unesco2000dakar (partial+verified), unesco2015efa (partial+verified), upton1875tribilcock (full+verified), virginia1831acts (full, writer-grounded), washington2004bailey (full+verified), wcefa1990world (partial+verified) |
| A3 | H01, H13, H18 | full+verified 8; partial+verified 6; partial, writer-grounded 1 | alabama1901official (partial+verified), gaston1969gaston (full+verified), giesler2014creating (full+verified), graff1991literacy (partial, writer-grounded), helps1855spanish (partial+verified), holmes1975kousser (full+verified), israeli2022requerimiento (partial+verified), kamperman2026ai (full+verified), katzenbach1966south (full+verified), lascasas1876historia (full+verified), oviedo1853historia (full+verified), uis2026adult (full+verified), unesco2000dakar (partial+verified), unesco2015efa (partial+verified), wcefa1990world (partial+verified) |
| A4 | E14 | full+verified 4; partial+verified 2 | microsoft2022responsible (full+verified), microsoft2024responsible (partial+verified), microsoft2025ai (full+verified), microsoft2025responsible (partial+verified), microsoft2026application (full+verified), smith2025microsoft (full+verified) |
| A5 | — | none via ledger |  |
| A6 | — | none via ledger |  |
| A7 | — | none via ledger |  |
| A8 | E15, K12, O01, O06 | full+verified 8; full, unverified 1; no card 6; partial+verified 1; reviews/secondary, corrected 1 | bagger2023digital (no card), bainbridge1983ironies (full+verified), bommasani2026algorithmic (full+verified), brevoort2015credit (no card), calo2017taking (no card), elish2019moral (full+verified), green2022flaws (full+verified), lindblom2019consent (partial+verified), maffie2023becoming (no card), nadella2026models (full+verified), obermeyer2019dissecting (no card), pettit1997republicanism (reviews/secondary, corrected), robertson2023diverse (no card), rosenblat2016algorithmic (full+verified), sudjianto2026when (full+verified), williams1965walker (full+verified), wood2019good (full, unverified) |
| B1 | H10, H23, H26, N07 | full+verified 11; no card 1; partial+verified 13 | almeida2019firmo (partial+verified), andrien2012burns (full+verified), balkin2016information (partial+verified), burnyeat1997postscript (partial+verified), claassen2024wealth (full+verified), foster1869mackinnon (full+verified), gavrilov1997techniques (partial+verified), hagedorn1988friend (full+verified), havelock1963 (partial+verified), johnson2000toward (no card), jones1899meehan (partial+verified), khan2019skeptical (partial+verified), knox1968silent (full+verified), marchant2015expedicion (partial+verified), mirault2019reading (full+verified), parkes1992pause (partial+verified), rayner1998unspaced (partial+verified), saenger1997space (partial+verified), spain1862ley (partial+verified), spain1944reglamento (partial+verified), sudore2006use (full+verified), uinl2005ethics (full+verified), uinl2005function (full+verified), uk1987noncontentious (full+verified) |
| B2 | D01 | full+verified 3 | garciaruiz2026can (full+verified), gaston1969gaston (full+verified), jobin2019global (full+verified) |
| B3 | — | none via ledger |  |

## What the ledger cannot show (from the gap audit, 2026-10-24)

| Premise | Gap | Facet |
|---|---|---|
| A1, A7 | No card for internal or immanent critique as a method, or for any structural-model paper (Luchs, Diamantis, Kugelberg and Kugelberg, Sharon and Gellert, Seele and Schultz, Kingston and Carnovale); Pettit 1997 secondary only | N5 |
| A2 (first moment) | Saenger 1997 card partial, content second-hand; p. 11 not yet confirmed by a clean route | N2 |
| A2, A3 (second moment) | No card for the 1543 Act (`statutesrealm1817vol3`), the Tridentine Index (`manuzio1564index`), Villers-Cotterêts, Siebert, Darnton, Febvre and Martin; Eisenstein 1979 secondary; no contemporary objector to 1543 found yet | N2 |
| A2, A3 (third moment) | Anti-literacy acts writer-grounded; Requerimiento, Jomtien and Dakar cards partial; no card for Frahm et al. or for the Pragmática of 1503 as a primary text | N3 |
| A4 | No cards for vendor terms, admin controls, chain-of-thought visibility in products, standards bodies, AI Act art. 73 beyond its opening, or skilling-effect evidence | N1, N4 |
| A5 | Rests on facet G's own inference (C7); needs Microsoft agent-platform documents showing to whom the envelope is declared | N1 |
| A6 | Seele and Schultz 2022 uncarded | N5 |
| A8 | K12 rests mainly on `nocard:` keys; objections O01–O08 in their strongest published form mostly at abstract depth | N1, N6 |
| B3, CB | Follow from CA and the D rows; no separate gap | — |

Writer-grounded or pending legacy cards the argument cites (for N7a): `virginia1831acts`, `northcarolina1831acts`,
`milton1644areopagitica`, `graff1991literacy`, `hill1997gateway`, `pike1873history`, `california2025civil`,
`willis2008against`, `nussbaum2011creating`, `statute1827criminal`, `roberts1835memoirs`, `helberger2018governing`.

## v1 after round 1 (2026-10-24): new cards by premise

All 98 new cards in `../literature/cards/berthon_ethics_paper/` are `verified: pending` until N7a, N7b and the lead's
adjudication. Bases: full 41, partial 53, abstract 3, secondary 1. Generated from each card's `premises:` field.

| Premise | New cards (basis, facet) |
|---|---|
| A1 | hamilton2025digital (full, N5); lovett2026republicanism (full, N5); luchs2026taking (full, N5) |
| A2 | alvord1868fifth (partial, N3); boretius1883capitularia (partial, N2); commons1803journal (full, N2); cranmer1846miscellaneous (partial, N2); deazley2008commentary1586 (full, N2); deazley2008commentary1637 (full, N2); frahm2022fixing (full, N3); furnivall1871four (partial, N2); hall1809chronicle (partial, N2); hill1997gateway (full, N3); isambert1828recueil (partial, N2); israeli2022requerimiento (full, N3); jin2003effect (abstract, N3); jones1899meehan (full, N3); kempf2014cuban (partial, N3); lely1883judicature (partial, N3); luchs2026taking (full, N5); manuzio1564index (partial, N2); milton1644areopagitica (partial, N2); nishimura2013improving (full, N3); northcarolina1831acts (full, N3); parker1877south (full, N3); pennsylvania1851minutes (partial, N3); reusch1883index (partial, N2); seed1995ceremonies (secondary, N3); simon2005impact (full, N3); spain1805novisima (partial, N3); starchamber1637decree (partial, N2); statutesrealm1817vol3 (full, N2); statutesrealm1819vol4 (partial, N2); tam2015participants (full, N3); tamariz2013improving (abstract, N3); unesco2015education (partial, N3); virginia1831acts (full, N3); wcefa1990world (partial, N3) |
| A3 | brinklow1874complaynt (partial, N2); commons1803journal (full, N2); cranmer1846miscellaneous (partial, N2); deazley2008commentary1586 (full, N2); foxe1838acts (partial, N2); frahm2022fixing (full, N3); furnivall1871four (partial, N2); hall1809chronicle (partial, N2); hill1997gateway (full, N3); israeli2022requerimiento (full, N3); kempf2014cuban (partial, N3); manuzio1564index (partial, N2); milton1644areopagitica (partial, N2); northcarolina1831acts (full, N3); parker1877south (full, N3); pennsylvania1851minutes (partial, N3); reusch1883index (partial, N2); seed1995ceremonies (secondary, N3); starchamber1637decree (partial, N2); statutesrealm1817vol3 (full, N2); statutesrealm1819vol4 (partial, N2); tam2015participants (full, N3); tyndale1848doctrinal (partial, N2); unesco2015education (partial, N3); virginia1831acts (full, N3); wcefa1990world (partial, N3) |
| A4 | anthropic2025commercial (partial, N1, Anthropic); anthropic2025consumer (partial, N1, Anthropic); anthropic2026configure (partial, N1, Anthropic); anthropic2026measuring (full, N1, Anthropic); anthropic2026thinking (partial, N1, Anthropic); anthropic2026usage (partial, N1, Anthropic); california2025transparency (full, N4); chiang2022exploring (full, N4); cjeu2024publicresource (partial, N4); corporateeurope2025bias (full, N4); elmergawi2026introducing (full, N1); eu2012standardisation (partial, N4); eu2016gdpr (partial, N4); eu2022nis2 (partial, N4); eu2024aiact (partial, N4); euomnibus2026 (partial, N4); europeancommission2025reply (full, N4); felt2012android (partial, N1); feng2025regulatory (full, N1); frahm2022fixing (full, N3); frontiermodelforum2026information (full, N4, Anthropic); google2026agentic (partial, N1); google2026gemini (partial, N1); gornet2024european (partial, N4); laux2024three (full, N4); microsoft2025multistage (full, N1); microsoft2026audit (full, N1); microsoft2026connect (partial, N1); microsoft2026copilot (full, N1); microsoft2026enabling (full, N1); microsoft2026microsoft (full, N1); microsoft2026overview (full, N1); microsoft2026responsible (partial, N1); microsoft2026tracing (full, N1); microsoft2026use (partial, N1); nist2024artificial (partial, N4); openai2026agent (partial, N1); openai2026reasoning (partial, N1); palod2026evaluating (partial, N1); parikh2025powering (full, N1); park2025critical (partial, N1); sharon2024regulating (full, N5); shavit2023practices (full, N1); tabassi2023artificial (partial, N4); veale2021demystifying (partial, N4); zhang2026hansel (partial, N1); zhao2026agentgui (partial, N1) |
| A5 | anthropic2025commercial (partial, N1, Anthropic); anthropic2026configure (partial, N1, Anthropic); anthropic2026usage (partial, N1, Anthropic); boretius1883capitularia (partial, N2); elmergawi2026introducing (full, N1); feng2025regulatory (full, N1); google2026agentic (partial, N1); lovett2026republicanism (full, N5); microsoft2026audit (full, N1); microsoft2026connect (partial, N1); microsoft2026enabling (full, N1); microsoft2026microsoft (full, N1); microsoft2026overview (full, N1); microsoft2026responsible (partial, N1); microsoft2026tracing (full, N1); microsoft2026use (partial, N1); openai2026agent (partial, N1); parikh2025powering (full, N1); shavit2023practices (full, N1); tyndale1848doctrinal (partial, N2); zhang2026hansel (partial, N1) |
| A6 | bartha2019analogy (partial, N5); ketokivi2017reasoning (partial, N5); seele2022greenwashing (full, N5); sharon2024regulating (full, N5) |
| A7 | bartha2019analogy (partial, N5); celikates2023critical (partial, N5); diamantis2025danger (full, N5); hamilton2025digital (full, N5); kugelberg2026practice (full, N5); lovett2026republicanism (full, N5); microsoft2026responsible (partial, N1); vonsamson2025immanent (full, N5); walzer1988interpretation (partial, N5) |
| A8 | anthropic2025consumer (partial, N1, Anthropic); anthropic2026measuring (full, N1, Anthropic); anthropic2026thinking (partial, N1, Anthropic); anthropic2026usage (partial, N1, Anthropic); california2025transparency (full, N4); chiang2022exploring (full, N4); connellpensky2026can (abstract, N4); diamantis2025danger (full, N5); eu2016gdpr (partial, N4); eu2022nis2 (partial, N4); eu2024aiact (partial, N4); eu2024productliability (partial, N4); euomnibus2026 (partial, N4); felt2012android (partial, N1); google2026gemini (partial, N1); kugelberg2026practice (full, N5); microsoft2025multistage (full, N1); microsoft2026copilot (full, N1); microsoft2026microsoft (full, N1); microsoft2026responsible (partial, N1); microsoft2026use (partial, N1); openai2026agent (partial, N1); openai2026reasoning (partial, N1); palod2026evaluating (partial, N1); park2025critical (partial, N1); puppart2025brief (partial, N4); shavit2023practices (full, N1); veale2021demystifying (partial, N4) |
| B1 | alvord1868fifth (partial, N3); isambert1828recueil (partial, N2); israeli2022requerimiento (full, N3); jin2003effect (abstract, N3); jones1899meehan (full, N3); kempf2014cuban (partial, N3); lely1883judicature (partial, N3); nishimura2013improving (full, N3); pennsylvania1851minutes (partial, N3); simon2005impact (full, N3); spain1805novisima (partial, N3); statutesrealm1817vol3 (full, N2); tamariz2013improving (abstract, N3) |
| B2 | kingston2026social (full, N5) |
| CB | kingston2026social (full, N5) |
| CA | luchs2026taking (full, N5) |

Cards missing a premises field: none

## Round-1 findings that narrow or change a premise (lead's summary of the facets' (c) and (d); pending audit)

| Premise | Finding | Facet |
|---|---|---|
| A2 | "Disclosure in place of understanding" fails in its strong form (restaurant grade cards cut hospitalisations 13.1%, but an inspector does the reading). The failure the record supports is disclosure that leaves the reading to the person bound | N3 |
| A2, A3 | 1543 Act: a contemporary objector found (*A Supplication of the Poore Commons*, 1546); the Act breaks its own preamble's standard; repealed 1547, so brief. Rule IV of the Index unenforced in Germany and France. Villers-Cotterêts reads partly as a correction. Parliament itself objected to the Stationers' custody (1695) | N2 |
| A2 (first moment) | Saenger p. 11 located only in the unauthorised copy; clean confirmation still needed; unquotable | N2 |
| A3 | Jomtien's halving was optional; the broken promise is Dakar's, and UNESCO's 2015 report names the overselling. Cuba and Nepal are counter-instances to "withheld, then oversold" | N3 |
| A4 | All four vendors put responsibility for actions on the user; no vendor shows anyone the raw chain of thought; approval gates thinned or handed to models | N1 |
| A4, M2 | "Standards bind no implementer" wrong for EU harmonised standards once cited in the OJ; holds for ISO/IEC 42001, NIST, the Frontier Model Forum | N4 |
| A4, M4(b) | Enterprise traces do mark commitments for their enterprise readers; the claim holds only for the person acted on | N1 |
| A4, M9, O02 | "Notice without standing" holds for AI Act art. 73 and SB 53 only; GDPR art. 34 and the Product Liability Directive give remedies | N4 |
| A5 | Holds for Microsoft (boundaries defined by the organisation's security or compliance team); refuted as a general claim by Google's AP2 Intent Mandate, which binds both sides | N1 |
| A6 | Holds only in Bartha's stricter form: the shared property must be the one the historical verdict turned on, with no critical disanalogy | N5 |
| A7 | Internal critique alone does not carry the bridge. Two narrower supports: the present actor's own professions (P3, P9, Microsoft's Standard v2, since "re-engineered") and republican non-domination, which conflicts with ledger N04's "describe, not condemn" | N5 |
| B1 | Fails on its second half: most corrections moved the work or the record (Pragmática 1503, Jones v. Meehan, the Easton clerk 1757); only the 1883 jurat rule, art. 193, teach-back and probate r. 13 checked understanding | N3 |
| D04 | New precedent: Teedyuscung's own clerk at Easton, 1757 | N3 |
| Outline | Luchs's shares measure 17.6 / 41.9 / 30.3 / 10.3 per cent (body 6,591 words); BEQ's 12,000-word cap includes footnotes, no "Introduction" heading, abstract ≤ 150 words | N5 |

> **Superseded by v2 below.** The "Round-1 findings" table above is pre-audit; its corrected wording is in
> `facets/ADJUDICATION.md` §6.

## v2 after the audit (2026-10-24)

All 106 new cards are verified (74 `true`, 32 `corrected`; `facets/ADJUDICATION.md`). Counts of verified new cards
naming each premise (the legacy cards in the v0 table still stand):

| Premise | Verified new cards: full / partial / abstract or secondary | Anthropic-authored among them |
|---|---|---|
| A1 | 3 / 0 / 0 | 0 |
| A2 | 16 / 17 / 6 | 0 |
| A3 | 12 / 15 / 1 | 0 |
| A4 | 21 / 29 / 1 | 7 |
| A5 | 10 / 11 / 0 | 3 |
| A6 | 2 / 2 / 0 | 0 |
| A7 | 7 / 4 / 2 | 0 |
| A8 | 10 / 20 / 2 | 4 |
| B1 | 5 / 6 / 2 | 0 |
| B2 | 1 / 0 / 0 | 0 |
| CA, CB | 1 / 0 / 0 each | 0 |

### Status of each premise

| Premise | Status | What carries it, and what the author must rule on |
|---|---|---|
| A1 | **UNSUPPORTED as a sourced claim** | The four design questions are the author's ruling; Lovett and Hamilton carry only "who may contest" |
| A2 | Carried, narrowed | First moment: Saenger p. 11 unquotable until a clean route confirms it. Second: 1543 Act, Star Chamber 1637, Stationers (Deazley, Commons 1695), Index Rule IV (unevenly enforced). Third: duty to read, jurat, Requerimiento (Israeli full), anti-literacy acts. "Disclosure in place of understanding" must read "disclosure that leaves the reading to the person bound" |
| A3 | Carried, narrowed | The 1546 *Supplication* is a probable objector; the 1543 Act's own preamble is a broken professed standard; Dakar (not Jomtien) is the broken promise; Easton 1757 is a contemporary objection. M7 meets no historical standard (N6): it rests on Microsoft's T1.3 and A5.4 as a present profession |
| A4 | Carried for the second party only | Microsoft and vendor documents (N1), standards and incident regimes (N4) as restated in ADJUDICATION §6. The author must concede the enterprise reading (N6 rank 1): Nadella's moves protect the deploying organisation against the provider; CA holds for the people its agents act on |
| A5 | Carried for Nadella and Microsoft | Microsoft's runtime controls answer to the organisation's security or compliance team (`elmergawi2026introducing`); AP2 is a partial counter-instance to a general form only |
| A6 | Carried in a stricter form | Bartha (`bartha2019analogy`): the shared property must be the one the historical verdict turned on, with no critical disanalogy |
| A7 | **Narrowed; author's ruling needed** | Internal critique alone does not bind a present actor (Walzer p. 69; SEP; von Samson; Williams via Gowans). Two routes: the actor's own professions (P3, P9, Microsoft Standard v2, since "re-engineered"), and republican non-domination, which conflicts with ledger N04 ("describe, not condemn") |
| A8 | Carried in part | O02 partly succeeds (GDPR arts. 79, 82; PLD; Moffatt v. Air Canada, after the harm only); "AI changes the practice" is the strongest changed-condition objection, answered by Walzer p. 70 |
| B1 | Narrowed | Most corrections moved the work or the record (Pragmática 1503, Jones v. Meehan, Easton 1757); only the 1883 jurat rule, art. 193, teach-back and probate r. 13 checked understanding |
| B2, B3, CB | Carried by the legacy D rows | New precedents: Easton 1757 for D04; AP2 mandates for D03 (partial); Kingston and Carnovale's working-precedent move |

## Library request list for the next draft

Blocked or paywalled this round; each facet's section (e) gives the location.

- **History:** Saenger 1997 pp. 10-13 and 83-91 (library copy or De Gruyter e-book; clean confirmation of p. 11);
  Arber's *Transcript* vols. II and IV (2: 807, 770-805; 4: 528); *Statutes of the Realm* vol. 4 pp. 18-22 (clean
  copy); Johns 1998, Stationers chapters; Siebert 1965 pp. 60-63, 92-95; Febvre and Martin 1976; Eisenstein 1979
  pp. 303-450; Darnton 1995; McKitterick 1989 chs. 4, 6; the Foxe Variorum; Seed 1995 ch. 3; Graff 1979 at its
  original pages; Burns 2005 and *Into the Archive*; Muldoon 1980; Faudree 2012, 2015; Merrell 1999; Fleming 2016;
  Palacios Rubios 1954; the 1503 *Libro de las Bulas y Pragmáticas*; Re Longstaff (Weekly Notes 1884); Huberman and
  Sweezy 1969; a Korea literacy-campaign source; Havelock 1963 and Nussbaum 2011 pages.
- **Present case:** OpenAI Terms of Use and Service Terms (live site), ChatGPT agent and Operator system cards;
  Microsoft's re-engineered Responsible AI Standard and the Copilot Cowork application card (not found published);
  Tariq et al. 2025; Mackworth 1948; Warm et al. 2008; AP2 linked files; the Commission's draft Art 73 guidance and
  template; ISO/IEC 42001; the JTC 21 member list; Connell Pensky 2026 full text; Microsoft's Copyright Commitment
  post and Pillitteri's blog (open and card before quoting).
- **Frame and objections:** Fraser 2023; Jaeggi 2018 and 2015; Pettit 1997 pp. 52, 62, 73-74, 107, 186-7;
  Lovett 2010; Bartha 2010; Gädeke 2020; Maas 2022, 2023; Walzer 1987 (Harvard UP); King and Lenox 2000; Ogus 1995;
  Abbott and Snidal 2009; Moog et al. 2015; Cinar 2025; Lastowka 2012; Mahardhika 2026; Grote and Paulo 2025;
  Scherer and Palazzo 2011; Hunt 2002; Skinner 1969; Fricker 2010; Williams 1985 ch. 9; Khong 1992; Neustadt and
  May 1986; Sunstein's Storrs Lectures; Napoli and Adi 2025.
- Consensus searches to rerun after 1 November (quota exhausted).

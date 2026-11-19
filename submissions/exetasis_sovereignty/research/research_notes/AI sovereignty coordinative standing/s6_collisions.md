# S6: Collision and novelty check, "coordinative sovereignty" (run 2026-10-24)

Scope: this run extends the 2026-08-23 collision map (`coordinative_sovereignty/reviews/2026-08-23/LITERATURE_GAPS.md` C1–C8, and `strand_reports/07_adjacent_constructs_term_ownership.md`). It does not repeat that work. Items already in C1–C8 or strand 07 are only named here when this run adds something: a new reading, a correction, or a post-August hit.

Source-status tags: **[full text read]**, **[abstract only]** (abstract retrieved this session from OpenAlex or the publisher), **[record only]** (bibliographic record seen, no abstract), **UNVERIFIED** (content not confirmed).

## Q1. Does anyone already use "coordinative sovereignty" or the neighbouring terms, and in what sense?

### Takeaway
I found no use of the exact phrase "coordinative sovereignty" in OpenAlex titles or abstracts, the top 100 Crossref title matches, arXiv, or the open web, searched 2026-10-24. The near-homonyms belong to other fields: "coordinated sovereignty" (state–tribe law), "cooperative sovereignty" (space and international law) and "coordination sovereignty" (noise). Every neighbouring term is owned by a different sense, almost always the state's sovereignty or the platform's, never the coordinated actor's standing inside the mediation. The one correction to the August map: "platform sovereignty" *is* a title-term, but it means the platform's own sovereignty.

### Search log (all searches run 2026-10-24)

**Databases reached:** OpenAlex API, Crossref API, arXiv API, WebSearch (general web).
**Databases not reached. Absence must not be inferred for these:**
- Semantic Scholar API: HTTP 429 on all 7 queries (`"coordinative sovereignty"`, `coordinative sovereignty platform`, `exit voice platform dependence sovereignty`, `Shapley value platform power political philosophy`, `sovereignty triadic mediation algorithm`, `algorithmic literacy sovereignty`, `bypass intermediary sovereignty voice`).
- PhilPapers: HTTP 403 for `"coordinative sovereignty"`, `"platform sovereignty"`, `"algorithmic sovereignty"`.
- SSRN (papers.ssrn.com): HTTP 403 (abstract page 6907425). SSRN items appear below only through OpenAlex and Crossref records.
- Scholar Gateway: `ACCESS_DENIED`.
- Consensus: monthly quota exhausted (resets 1 Nov 2026).
- Google Scholar: not queried directly; WebSearch is a general web index, not Scholar.
- OpenAlex: three late queries errored (no `meta` in the response, probably rate limiting): `Shapley + domination`, `"cooperative game" + platform + workers + bargaining`, `"exit" + "voice" + platform + complementors`.

**Caveat on OpenAlex.** The quoted `search=` parameter covers full text and stems words, so "coordinative" matches "coordinated". The `title_and_abstract.search` counts are the meaningful ones. Zenodo deposits inflate many counts; one author alone ("el-rakhawi") has more than 15 "algorithmic sovereignty" deposits from Sept–Oct 2026.

| # | Database | Exact query string | Hits | Relevant hits |
|---|---|---|---|---|
| 1 | OpenAlex `search=` (full text, stemmed) | `"coordinative sovereignty"` | 33 | 0 literal. Top hit: Fay 2026 "Coordinated Sovereignty" (stem match) |
| 2 | OpenAlex `title_and_abstract.search` | `"coordinative sovereignty"` | 5 | 0 literal. Chovančík et al. 2026 *European Security*; Fay 2026 (SSRN + *Wisconsin L. Rev.*); Weinert 2007 *Democratic Sovereignty*; one Zenodo physics deposit. All are stem matches |
| 3 | Crossref `query.bibliographic` | `coordinative sovereignty` | 42,276 (ranked); exact phrase in title among top 100: **0** | none |
| 4 | arXiv API | `all:"coordinative sovereignty"` | **0** | none |
| 5 | WebSearch (extended) | `"coordinative sovereignty"` | 9 results, 0 exact | "cooperative sovereignty" (arXiv 1511.05615; arXiv 2602.08853), "disaggregated", "reciprocal sovereignty" (CEPR VoxEU) |
| 6 | OpenAlex TA | `"coordination sovereignty"` | 6 | none relevant (FATCA, blockchain disaster networks, Vegas 2025 "sovereign interoperability") |
| 7 | Crossref | `coordination sovereignty` | 223,342; exact in title top 100: 0 | none |
| 8 | OpenAlex TA, from 2018 | `"relational sovereignty"` | 77 | Aruleswaran 2026 (AI governance); Tran Quoc Hung 2026 (relational digital sovereignty); Mendoza 2026 (trust cultures, unrelated) |
| 9 | Crossref | `relational sovereignty` | 106,975; exact in title top 100: 17 | Aruleswaran 2026 SSRN; others Indigenous / humanitarian / IR |
| 10 | OpenAlex TA, from 2017 | `"functional sovereignty"` | 47 | Hao 2026 (functional AI sovereignty); Florea & Huang 2025 ISQ |
| 11 | OpenAlex TA | `"functional sovereignty"` AND `platform` | 8 | Pasquale 2023 "Two visions for data governance" (OUP chapter); Ranchordás & Goanță 2019 CLSR; Lopes Damame 2025; Hao 2026 |
| 12 | Crossref | `functional sovereignty` | 953,039; exact in title top 100: 4 | Florea & Huang 2025; Mwololo 2026 SSRN; Dederer 2015; Riphagen 1975 |
| 13 | WebSearch | `Pasquale "functional sovereignty" platforms territorial to functional` | 9 | Pasquale 2017 LPE blog (fetched, see below) |
| 14 | OpenAlex TA | `"platform sovereignty"` | 36 | Heylen 2023; Anning-Dorson 2025; van Es & Becker 2026; Arı 2026 (Zenodo); Tokuda 2026 |
| 15 | Crossref | `platform sovereignty` | 307,217; exact in title top 100: 6 | Heylen 2023 NM&S; Anning-Dorson 2025 *Electronic Markets*; Tobing et al. 2025; Lockhart 2025; Gawel 2025 |
| 16 | arXiv | `all:"platform sovereignty"` | 2 | none relevant (LLM engineering) |
| 17 | OpenAlex TA | `"algorithmic sovereignty"` | 205 | mostly geopolitics / Zenodo noise; Hu & Rong 2026 arXiv 2602.14951 "infrastructural sovereignty" in decentralized AI |
| 18 | Crossref | `algorithmic sovereignty` | 77,894; exact in title top 100: 24 | Brown et al. 2023 (Māori, CrimRxiv); Kera 2021; Al Mashai 2025 SSRN; Warnier 2025; all state, Indigenous or AI-governance senses |
| 19 | OpenAlex TA | `"networked sovereignty"` | 104 | none on coordinated actors |
| 20 | Crossref | `networked sovereignty` | 81,978; exact in title top 100: 2 | Gagliardone 2024 *Liinc* (Africa, AI lock-in) |
| 21 | OpenAlex TA, from 2020 | `"digital self-determination"` | 83 | Verhulst & Zable 2026 SSRN (data spaces); Macpherson & Veit 2026 *Computers & Security* |
| 22 | Crossref | `digital self-determination` | 3.2M; exact in title top 100: 14 | Verhulst 2023; Verhulst & Marcucci 2025; Marcucci & Verhulst 2025; Remolina & Findlay 2021; Musiani 2025 |
| 23 | OpenAlex TA | `"sovereignty-as-a-service"` | 54 (stemmed) | Grohmann & Costa Barbosa 2025 |
| 24 | Crossref | `sovereignty-as-a-service` | exact in title top 100: 2 | Grohmann & Costa Barbosa 2025 MCS; AoIR 2024 paper by the same authors |
| 25 | OpenAlex TA, from 2020 | `"intermediary power"` | 32 | Lazar 2024 arXiv lecture; Yang & Liu 2026 (Wanghong economy) |
| 26 | Crossref | `intermediary power` | exact in title top 100: 7 | Yang & Liu 2026; older non-platform works |
| 27 | OpenAlex TA, from 2019 | `"coordination rights"` | 20 | Foster & Thelen 2024 CPS |
| 28 | Crossref | `coordination rights` | exact in title top 100: 2 | Foster & Thelen 2024; Hawley 2024 (bank failure) |
| 29 | OpenAlex `cites:` Paul 2020 (W2924548562), from 2026-06-01 | — | **0** | none (Paul 2020 has 80 citations overall in OpenAlex) |
| 30 | OpenAlex TA, from 2019 | `"infrastructural power"` AND `platform` | 168 | da Rosa & de Oliveira 2026 (Brazil electoral regulation); Addaquay 2026 *Convergence* |
| 31 | Crossref | `infrastructural power` | exact in title top 100: 38 | none new on platforms beyond Valdez / Rahman & Thelen |
| 32 | OpenAlex TA | `"contested relational structures"` | 1 | Schüßler et al. 2021 only |
| 33 | OpenAlex `search=` | `"contested relational structures"` | 63 | Schüßler, Maric & Dobusch 2026 *Information & Organization*; Beyer 2026 *Digital Society* |
| 34 | OpenAlex TA, from 2020 | `"data sovereignty"` AND `worker` | 66 | none theorising worker data sovereignty as standing |
| 35 | Crossref | `data sovereignty workers` | exact "data sovereignty" in title top 100: 45 | Chowdhury 2026 SSRN (migrant workers, Malaysia); the rest Indigenous data sovereignty |
| 36 | OpenAlex `search=` | `"worker data sovereignty"` | 4 | Fallah 2026 SSRN (record only) |
| 37 | OpenAlex `search=` / Crossref | `algorithmacy` | 1 (1995, irrelevant) / 0 | coinage still clear |

### Cited Findings: exact phrase
- No title or abstract in OpenAlex contains "coordinative sovereignty". All 5 hits are stem matches on "coordinated" or "coordination". The closest is Fay, "Coordinated Sovereignty: Federal Tools for Resolving State-Tribe Conflict" (2026), about federal–tribal jurisdiction. **[record only]** — [SSRN DOI](https://doi.org/10.2139/ssrn.6890738); [Wisconsin L. Rev. DOI](https://doi.org/10.59015/wlr.ezir1188)
- Crossref: 0 titles with the exact phrase among the top 100 ranked results. arXiv: 0 results. — [Crossref API](https://api.crossref.org/works?query.bibliographic=coordinative+sovereignty); [arXiv API](https://export.arxiv.org/api/query?search_query=all:%22coordinative%20sovereignty%22)
- Web: no exact-phrase use. Nearest homonyms are "cooperative sovereignty" (inter-state, space law) and "reciprocal sovereignty" (EU constitutional logic). **[record only]** — [arXiv 1511.05615](https://arxiv.org/pdf/1511.05615); [arXiv 2602.08853](https://arxiv.org/pdf/2602.08853); [CEPR VoxEU](https://cepr.org/voxeu/columns/reciprocal-sovereignty-third-constitutional-logic-europe)

### Cited Findings: neighbouring terms (who, when, in what sense, how close)
Closeness scale: **0** = different sense; **1** = same object (platforms), different bearer of sovereignty; **2** = same bearer or same structural move, different conclusion; **3** = anticipates the position.

- **Functional sovereignty (Pasquale).** The platform is the sovereign. Firms become "market makers" that replace "the logic of territorial sovereignty with functional sovereignty". This is the opposite bearer from the position. Closeness 1. **[full text read via fetch; quotations extracted]** — [Pasquale, LPE Project blog, dated 12.06.17 on the page](https://lpeproject.org/blog/from-territorial-to-functional-sovereignty-the-case-of-amazon/). A second-hand page attributes a 2018 Pasquale & Cockfield discussion. UNVERIFIED; do not cite. — [P2P Foundation wiki](https://wiki.p2pfoundation.net/Frank_Pasquale_on_the_Shift_from_Territorial_to_Functional_Sovereignty)
- **Functional sovereignty (other senses).** Florea & Huang (2025, ISQ) use it for de facto states' graded control over license plates, currency, passports, post and domains. Closeness 0, but the term is now contested by ISQ. **[abstract only]** — [doi:10.1093/isq/sqaf069](https://doi.org/10.1093/isq/sqaf069). Riphagen 1975 is the origin in international law. **[record only]** — [doi:10.1017/s0167676800004906](https://doi.org/10.1017/s0167676800004906)
- **Functional AI sovereignty (Hao 2026, new since August).** "Ownership is neither a sufficient nor universally necessary condition of sovereign control." AI sovereignty is "the capacity of public authorities to govern the dependencies through which critical AI capabilities are produced, accessed and sustained". Its six dimensions include *substitutability*. Closeness 2: the same anti-independence move (sovereignty inside dependence), but the bearer is the state and the instrument is orchestration and procurement, not voice. This is the strongest new structural neighbour. Published 2026-10-12. **[abstract only]** — [Hao, *Discover Artificial Intelligence*, doi:10.1007/s44163-026-02447-x](https://doi.org/10.1007/s44163-026-02447-x)
- **Platform sovereignty.** *Correction to strand 07*, which said it is "not an established title-term". It is a title-term, but for the platform's own sovereignty: Heylen (2023, NM&S) on Google and Facebook's response to Australia's News Media Bargaining Code, where their strategies "protect, strengthen and enforce platform sovereignty". Closeness 1. **[abstract only]** — [doi:10.1177/14614448231166057](https://doi.org/10.1177/14614448231166057). Also Tokuda (2026, "Platformer-Defined Sovereignty", the platformer's sovereignty over the mobility industry; repository working paper). **[abstract only]** — [doi:10.34382/0002007519](https://doi.org/10.34382/0002007519). Anning-Dorson (2025, *Electronic Markets*, "Digital platform sovereignty through Ubuntu", AI-enabled work in Africa); content UNVERIFIED. **[record only]** — [doi:10.1007/s12525-025-00864-x](https://doi.org/10.1007/s12525-025-00864-x). Also van Es & Becker (2026, *Convergence*, public broadcaster VoD platform). **[record only]** — via OpenAlex TA query #14.
- **Algorithmic sovereignty.** Confirms strand 07: state geopolitics plus Indigenous data (Brown et al., "Māori algorithmic sovereignty", CrimRxiv 2023). Closeness 0. **[record only]** — [doi:10.21428/cb6ab371.8974a07c](https://doi.org/10.21428/cb6ab371.8974a07c); Kera 2021 **[record only]** — [doi:10.14361/9783839457603-004](https://doi.org/10.14361/9783839457603-004). Hu & Rong (2026, arXiv) "infrastructural sovereignty" for decentralized AI agents. Closeness 0. **[record only]** — [doi:10.48550/arxiv.2602.14951](https://doi.org/10.48550/arxiv.2602.14951)
- **Relational sovereignty.** Strand 07 assigned it to Bannerman (already cited). New this run: Tran Quoc Hung (2026-08-12, *Philosophies*) ends with "a relational account of digital sovereignty incorporating autonomy/interdependence". The bearer is the state (US/EU/China models, applied to Vietnam). Closeness 1. **[abstract only]** — [doi:10.3390/philosophies11040142](https://doi.org/10.3390/philosophies11040142). Aruleswaran (2026, SSRN), "Relational Sovereignty as a Fourth Pillar of AI Governance"; content UNVERIFIED. **[record only]** — [doi:10.2139/ssrn.6061996](https://doi.org/10.2139/ssrn.6061996). Mendoza (2026, Routledge) uses it in a trust-cultures sense; closeness 0. **[record only]** — [doi:10.4324/9781003771494-4](https://doi.org/10.4324/9781003771494-4)
- **Networked sovereignty.** No coordinated-actor sense. Gagliardone (2024, *Liinc*), "Lock-out, lock-in, and networked sovereignty" (Africa, AI). Closeness 1. Note that its lock-in framing touches the bypass idea at state scale. **[record only]** — [doi:10.18617/liinc.v20i2.7319](https://doi.org/10.18617/liinc.v20i2.7319)
- **Digital self-determination.** Verhulst's programme continues: Verhulst & Marcucci 2025 (SSRN, comparison with other governance approaches); Marcucci & Verhulst 2025 (AI governance); Verhulst & Zable 2026 (data spaces). Musiani (2025) treats it as "infrastructure-embedded practices". Closeness 1–2. It concerns agency over data, not standing inside a coordinating intermediary. **[record only]** — [doi:10.2139/ssrn.5198669](https://doi.org/10.2139/ssrn.5198669); [doi:10.2139/ssrn.5343658](https://doi.org/10.2139/ssrn.5343658); [doi:10.2139/ssrn.7381898](https://doi.org/10.2139/ssrn.7381898); [doi:10.3389/fcomm.2025.1562072](https://doi.org/10.3389/fcomm.2025.1562072). Strand 07 also flagged Pisani (2024, CLSR) "The right to self-determination in the digital platform economy". It is still unopened and no abstract is in OpenAlex: **UNVERIFIED content, must read before submission.** **[record only]** — [doi:10.1016/j.clsr.2024.105964](https://doi.org/10.1016/j.clsr.2024.105964)
- **Sovereignty-as-a-service (Grohmann & Costa Barbosa).** Already in strand 07. This run adds the verbatim formulation the paper can turn: "Rather than sovereignty being exercised over platforms, it is now provisioned by them, on their terms." The position is a third option: sovereignty exercised *within* the platform through voice. Closeness 1. **[abstract only]** — [MCS, doi:10.1177/01634437251395003](https://doi.org/10.1177/01634437251395003); the earlier AoIR version **[record only]** — [doi:10.5210/spir.v2024i0.13948](https://doi.org/10.5210/spir.v2024i0.13948)
- **Intermediary power (Lazar).** C1 already. The arXiv lecture version is confirmed: Lazar introduces "the Algorithmic City" and "the intermediary power by which it is governed", and asks about "the justification of authority" and "procedural legitimacy". The bearer is the intermediary, viewed from its legitimacy. Closeness 2. **[abstract only]** — [arXiv 2410.20720](https://doi.org/10.48550/arxiv.2410.20720); PPA version [doi:10.1111/papa.12279](https://doi.org/10.1111/papa.12279) (22 citations in OpenAlex)
- **Coordination rights (Paul).** C7 already. This run found that the construct has been taken up in comparative political economy: Foster & Thelen (2024, CPS) build a "comparative coordination rights framework" on Paul (2020). The August map missed this. It strengthens the case that "coordination rights" is a live term the abstract must distinguish from. OpenAlex shows no new citers of Paul since 2026-06-01. Closeness 1. **[abstract only]** — [doi:10.1177/00104140241259461](https://doi.org/10.1177/00104140241259461)
- **Infrastructural power.** No new platform-specific owner beyond Valdez and Rahman & Thelen (strand 07). Recent applications are da Rosa & de Oliveira (2026, Brazilian electoral regulation) and Addaquay (2026, *Convergence*, genre classification). Closeness 1. **[record only]** — via OpenAlex TA query #30.
- **Contested relational structures (Schüßler et al. 2021).** C6 already; still the only title-and-abstract use. Schüßler, Maric & Dobusch (2026, *Information & Organization*) carry the programme to social media and democratic publics. **[record only]** — [doi:10.1016/j.infoandorg.2026.100612](https://doi.org/10.1016/j.infoandorg.2026.100612); original [doi:10.1093/ser/mwab038](https://doi.org/10.1093/ser/mwab038)
- **Data sovereignty, worker or user sense.** No literature theorises worker data sovereignty as standing. The Crossref title hits are dominated by Indigenous data sovereignty. Chowdhury (2026, SSRN, "From Data Sovereignty to Data Justice: Migrant Workers… Relational Rights in Malaysia") is the only worker-sense title; content UNVERIFIED. **[record only]** — [doi:10.2139/ssrn.6777362](https://doi.org/10.2139/ssrn.6777362)

### Inferences
- The phrase is free to claim within the reached databases. Because OpenAlex stems, I checked literal presence by title and abstract. Fay's "Coordinated Sovereignty" (2026) is a near-homonym a referee could raise; one clause in Key Terms would pre-empt it.
- Across every neighbouring term the bearer of sovereignty is the state, the platform, or a people or community over its data. The novelty to stake is the *bearer*: the coordinated actor inside a mediation it cannot bypass. The wording should not claim novelty for "sovereignty without independence" as such. Hao (2026) makes that move at state level, and Edler et al. (2023, already in the map) make it for industrial sovereignty.

### Gaps
- Semantic Scholar, PhilPapers, SSRN full-text search, Google Scholar, Scholar Gateway and Consensus were not reached. A rerun after 1 Nov (Consensus reset) and a manual Google Scholar and PhilPapers check of `"coordinative sovereignty"` are needed before the abstract may say "no prior use".
- Crossref title checks covered only the top 100 ranked results per query; Crossref offers no phrase search.
- No Wiley or Elsevier full-text search was possible (Scholar Gateway denied).

## Q2. Has anyone combined Hirschman's exit/voice with platform dependence to argue that voice is the sovereign move where exit is foreclosed?

### Takeaway
Two works apply Hirschman to platform workers and online communities, and a 2026 review lists contest, exit and collective rule-shaping as freedom conditions. In the reached sources I found no work that argues voice *replaces* exit as the locus of sovereignty where exit is foreclosed. The nearest new work, Dahlan (2026), goes the other way and lists "viable exit" as a requirement.

### Search log (2026-10-24)
| # | Database | Query | Hits | Relevant |
|---|---|---|---|---|
| 38 | OpenAlex TA | `"exit"` + `"voice"` + `platform` + `sovereignty` | 8 | 0 (Duarte & Bastos 2026 M/C Journal on Twitter capture is the only platform item; not on point) |
| 39 | OpenAlex TA | `Hirschman` + `platform` + `dependence` | 5 | Kumpf 2026 SSRN "Blockchain-based dispute resolution… Exit, voice and the state" (tangential) |
| 40 | OpenAlex TA | `Hirschman` + `algorithmic` | 181 | dominated by the "discrete Hirschman transform" (signal processing); none relevant in top 9 |
| 41 | OpenAlex TA, from 2026-06-01 | `"exit"` + `"voice"` + `platform` | 19 | Dahlan 2026; Starostin 2026 (Zenodo, pickup-point agents); Kisielov 2026 (state legitimacy); Yoganandan & Monisha 2026 (consumer brand hate) |
| 42 | OpenAlex TA | `bypass` + `intermediary` + `voice` | 15 | 0 |
| 43 | OpenAlex TA | `sovereignty` + `"voice"` + `gig` | 3 | 0 |
| 44 | arXiv | `all:Hirschman AND all:platform` | 5 | "Effective Voice: Beyond Exit and Affect in Online Communities" (2009.12470) |
| 45 | arXiv | `all:sovereignty AND all:platform AND all:exit` | 0 | — |
| 46 | WebSearch (extended) | `Hirschman exit voice platform workers lock-in "voice" when exit impossible digital platforms political theory` | 9 | Frapporti & Pirone 2023 ELRR; a 2026 Springer article on digital Taylorism in India |
| — | OpenAlex TA (errored) | `"exit"` + `"voice"` + `platform` + `complementors` | ERR | not reached |

### Cited Findings
- Frapporti & Pirone (2023, *Economic and Labour Relations Review*) "adapt" Hirschman's exit, voice and loyalty "to frame the various strategies that platform workers may adopt" (Uber, Airbnb, Helpling, Deliveroo; Bologna, PLUS project). The paper is descriptive and union-focused, with no sovereignty claim. Closeness 2. Not in the August map. **[abstract only]** — [doi:10.1017/elr.2023.45](https://doi.org/10.1017/elr.2023.45)
- Dahlan (2026-09-10, *Journal of Economic Epistemology and Philosophy*) is a systematic review of 95 studies. It separates "first-order discretion (choosing when to work and which tasks to accept)" from "second-order control (the capacity to know, contest, exit, and collectively shape the rules)". It reports that republican non-domination, the capability approach and Islamic contract ethics "converge… on four requirements: knowable rules, contestability, viable exit, a[…]" (the abstract is truncated in OpenAlex). Closeness 2, and *contrary*: it keeps exit as a requirement, whereas the position holds that only voice works under necessary mediation. The venue is new and low-profile; check its standing before giving it weight. **[abstract only]** — [doi:10.55942/jeep.v1i2.2297](https://doi.org/10.55942/jeep.v1i2.2297)
- "Effective Voice: Beyond Exit and Affect in Online Communities" (arXiv 2020) is a community-governance paper. Authors not recorded this session. **[record only]** — [arXiv 2009.12470](https://arxiv.org/abs/2009.12470)
- A web-surfaced review of Hirschman argues that voice becomes viable mainly when exit is blocked. This is the classical root of the position, not a platform work; the review's author and year were not confirmed (UNVERIFIED). — [ResearchGate "Hirschman and Voice"](https://www.researchgate.net/publication/268485669_Hirschman_and_Voice)
- A 2026 Springer article on digital Taylorism in India reportedly applies Hirschman to employment relations as collective representation. Authors not recorded; UNVERIFIED. **[record only]** — [doi:10.1007/s44282-026-00496-2](https://link.springer.com/article/10.1007/s44282-026-00496-2)
- Kisielov (2026-08-28, SocArXiv), "Legitimacy Without Exit", is about the durable legitimacy of states and de facto states, not platforms. Closeness 0, but the title is a near-match a referee might search. **[abstract only]** — [doi:10.31235/osf.io/p8qek_v1](https://doi.org/10.31235/osf.io/p8qek_v1)
- From the August map, still relevant here: Loh & Elsas-Nicolle (2026, SMJ) find that when exit opens, many complementors do not take it; Lehdonvirta (2022) discusses voice institutions; Aytac (2024) ties digital domination to absent exit. Already logged as contests or neighbours — see `LITERATURE_GAPS.md` §3 and §2.

### Inferences
- The specific claim, that voice is the sovereign move *because* exit is foreclosed, with a bypass counterfactual separating the two regimes, has not surfaced in the reached sources. Dahlan (2026) is the most important new foil: it bundles exit and voice as joint freedom conditions, and the position can be stated as a denial that viable exit is necessary under necessary mediation.

### Gaps
- Hirschman-plus-platform searches in Semantic Scholar, PhilPapers and Google Scholar were not reached. The complementor-side query errored. The organisation-studies literature on complementor voice (IS and SMJ) remains unchecked this run.

## Q3. Has anyone put "sovereignty" together with "triadic" or "third-party" mediation, or with "algorithmacy" or "algorithmic literacy"?

### Takeaway
No. The "triadic" plus "sovereignty" hits use "triad" in unrelated senses: a state-territory triad, a nuclear triad, a dependency/openness/agency triad. The "algorithmic literacy" plus "sovereignty" hits treat literacy as an epistemic-inequality or attention issue. "Algorithmacy" still has zero scholarly hits.

### Search log (2026-10-24)
| # | Database | Query | Hits | Relevant |
|---|---|---|---|---|
| 47 | OpenAlex TA | `triadic` + `sovereignty` | 429 | Verhulst & González Otero 2026; Weatherill 2026 (Zenodo); none on triadic mediation |
| 48 | OpenAlex TA | `"third party"` + `sovereignty` + `platform` + `algorithm` | 35 | Barbutev 2026 SSRN (sovereignty index for platform-dependent news markets); van Es & Becker 2026 |
| 49 | OpenAlex TA | `"algorithmic literacy"` + `sovereignty` | 18 | Bracho-Fuenmayor 2025; Patrissia & Ekadyasa 2026 ("attention sovereignty") |
| 50 | OpenAlex `search=` / Crossref | `algorithmacy` | 1 irrelevant / 0 | — |

### Cited Findings
- Verhulst & González Otero (2026, SSRN), "The Triad of Tech Sovereignty and Europe's Package: Dependency, Openness, and Agency". The title signals agency within dependency at EU level. The abstract was unavailable (OpenAlex has none; SSRN returned 403). **UNVERIFIED content; read before submission.** Possible closeness 2 at state scale. **[record only]** — [doi:10.2139/ssrn.6907425](https://doi.org/10.2139/ssrn.6907425)
- Barbutev (2026, SSRN), "Adjusted Volatility Index (AVI*) Quantifying Digital Sovereignty and Resilience in Platform-Dependent News Markets". This is a measurement of sovereignty under platform dependence (publishers), relevant to the "standing can be measured" claim. Content UNVERIFIED. **[record only]** — [doi:10.2139/ssrn.6385919](https://doi.org/10.2139/ssrn.6385919) (OpenAlex query #48)
- Bracho-Fuenmayor (2025), "Algorithmic literacy and epistemic inequality: the risk of a new cognitive colonization with AI". This links literacy to epistemic domination, not sovereignty-as-standing. Closeness 1. **[record only]** — [doi:10.62486/978-9915-9851-9-0.ch01](https://doi.org/10.62486/978-9915-9851-9-0.ch01)
- Patrissia & Ekadyasa (2026, conference proceeding), "Algorithmic Communication and Digital Trance: … Conditional Autonomy and Attention Sovereignty". Closeness 0–1. **[record only]** — via OpenAlex query #49.
- Roumbanis (2025, EJST) treats algorithms as mediating third parties (Sartre), already in strand 07 #21 and the closest "third-party" framing. **[not re-read this run]** — [doi:10.1177/13684310251319677](https://doi.org/10.1177/13684310251319677)

### Inferences
- The triadic-mediation framing of sovereignty and the coupling of sovereignty with algorithmacy appear open in the reached sources. The coupling is the most defensible novelty element for the abstract.

### Gaps
- No full-text search of Wiley, Sage or T&F (Scholar Gateway denied). Semantic Scholar was not reached for `sovereignty triadic mediation algorithm` or `algorithmic literacy sovereignty`.

## Q4. Has anyone measured standing with the Shapley value or the core in a political-philosophy argument about platforms?

### Takeaway
Not in the reached sources. The Shapley value and the nucleolus have been applied to two-sided platform games in economics, and the Shapley–Shubik index is standard in voting-power theory. I found no political-philosophy work that reads an actor's standing or sovereignty on a platform through Shapley pivotality or core membership.

### Search log (2026-10-24)
| # | Database | Query | Hits | Relevant |
|---|---|---|---|---|
| 51 | OpenAlex TA | `Shapley` + `platform` + `power` | 121 | Parker, Petropoulos & Van Alstyne 2020 SSRN "Digital Platforms and Antitrust" (only non-engineering hit in the top 9) |
| 52 | OpenAlex TA | `Shapley` + `sovereignty` | 21 | Gallardo et al. 2016 "A Shapley measure of power in hierarchies"; river-sharing papers (Ni & Wang 2006) |
| 53 | OpenAlex TA | `Shapley` + `"two-sided"` + `platform` | 12 | Huang & Xie 2022 SSRN |
| 54 | WebSearch (extended) | `Shapley value pivotality platform power legitimacy political philosophy standing cooperative game "core" platform workers` | 9 | technical sources only |
| — | OpenAlex TA (errored) | `Shapley` + `domination`; `"cooperative game"` + `platform` + `workers` + `bargaining` | ERR | not reached |
| — | Semantic Scholar (429) | `Shapley value platform power political philosophy` | — | not reached |

### Cited Findings
- Huang & Xie (2022, SSRN), "The Shapley Value and the Nucleolus of a Two-sided Platform Game". This is the economics precedent for computing cooperative solution concepts on a platform triad. The paper should cite it as the formal antecedent and say its own use is normative (standing), not distributive. **[record only]** — [doi:10.2139/ssrn.4039043](https://doi.org/10.2139/ssrn.4039043)
- Gallardo, Jiménez & Jiménez-Losada (2016, *Information Sciences*), "A Shapley measure of power in hierarchies", and Alarcón, Gallardo & Jiménez-Losada (2024, ITOR), "rethinking the weight of intermediary power" in graph-restricted cooperative games. Both are formal measures of an intermediary's power in a network. The second is a direct formal neighbour of "standing read through pivotality" under mediation. **[record only]** — [doi:10.1016/j.ins.2016.08.025](https://doi.org/10.1016/j.ins.2016.08.025); [doi:10.1111/itor.13573](https://doi.org/10.1111/itor.13573) (DOI from the OpenAlex record, query #25)
- Parker, Petropoulos & Van Alstyne (2020, SSRN), "Digital Platforms and Antitrust", surfaced on Shapley + platform + power; whether it uses the Shapley value is UNVERIFIED. **[record only]** — [doi:10.2139/ssrn.3608397](https://doi.org/10.2139/ssrn.3608397)
- The Shapley–Shubik index scores each player by the probability of being pivotal across orderings. One paper shows that the Shapley value equals pivot probability under random-order roll calls if and only if players' cooperation decisions are exchangeable. That caveat matters if the paper equates Shapley value with pivotality. **[record only]** — [arXiv 1808.02696](https://arxiv.org/pdf/1808.02696); [Shapley–Shubik index (Wikipedia)](https://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index)

### Inferences
- The Shapley/core reading of standing looks open in political philosophy. The formal tools have platform and intermediary precedents in economics and OR (Huang & Xie 2022; Alarcón et al. 2024), and the paper should name them so that a referee does not think the formal move itself is new.
- The roll-call result (arXiv 1808.02696) means "Shapley pivotality" should be stated with its exchangeability assumption, or replaced by "pivot probability".

### Gaps
- Two OpenAlex queries errored and Semantic Scholar returned 429. The voting-power literature (Felsenthal & Machover and successors) was not checked against platforms this run. PhilPapers, which would be decisive for the political-philosophy claim, returned 403.

## Q5. Nearest neighbours a referee will expect, extending C1–C8 (new since August or missed)

### Takeaway
None of the new items collides head-on. Four should be positioned against in the abstract or the paper's first section: Hao (2026), Dahlan (2026), Donahue, Stone & Jayaram (2026) and Foster & Thelen (2024). Kwok (2026) and Frapporti & Pirone (2023) earn a sentence each. The August verdict holds: Lazar (C1), Paul (C7) and Schüßler et al. (C6) remain the main collisions.

### Cited Findings
- **N1, Hao (2026-10-12).** Functional AI sovereignty: governing dependencies, not owning the stack, with substitutability as a dimension. *Position against:* the same rejection of independence, at state scale. Coordinative sovereignty moves the bearer to the coordinated actor and the instrument to voice. **[abstract only]** — [doi:10.1007/s44163-026-02447-x](https://doi.org/10.1007/s44163-026-02447-x)
- **N2, Dahlan (2026-09-10).** Second-order control includes exit; viable exit is a convergent requirement. *Position against:* the bypass counterfactual says exit cannot be a requirement under necessary mediation. **[abstract only]** — [doi:10.55942/jeep.v1i2.2297](https://doi.org/10.55942/jeep.v1i2.2297)
- **N3, Donahue, Stone & Jayaram (2026-06-01, *Philosophy & Technology*).** An "Interference Conception" of platform legitimacy: rights violations and inappropriate governance undermine legitimacy, mere harms do not. This is the Lazar-side question (the intermediary's legitimacy). It cites Lazar 2025 (OpenAlex `cites:` query). *Position:* their question is what licenses public interference with platforms; the paper's question is what standing the governed actor has inside one. **[abstract only]** — [doi:10.1007/s13347-026-01118-0](https://doi.org/10.1007/s13347-026-01118-0)
- **N4, Kwok (2026-10-11, *Media Technology and Governance*).** The Algorithmic Empowerment Principle: gatekeeping platforms owe disadvantaged groups a fair share of visibility and must "justify their choices to affected communities". It cites Lazar 2025. *Relation:* visibility as an allocated good parallels standing; one sentence. **[abstract only]** — [doi:10.1177/29777984261494012](https://doi.org/10.1177/29777984261494012)
- **N5, Foster & Thelen (2024, CPS).** The coordination-rights framework carried into comparative political economy. *Relation:* it extends C7. If coordinative sovereignty is a subset of coordination rights, say so against both. **[abstract only]** — [doi:10.1177/00104140241259461](https://doi.org/10.1177/00104140241259461)
- **N6, Frapporti & Pirone (2023, ELRR).** Hirschman applied to platform workers. One sentence for Q2's precedent. **[abstract only]** — [doi:10.1017/elr.2023.45](https://doi.org/10.1017/elr.2023.45)
- **N7, Manoli (2026, *Annals of Tourism Research*).** "Platform-mediated local power": platforms decide who can credibly claim local legitimacy through ranking, review and recommendation (visibility, credibility, convertibility). This is relevant to the OTA case in the earlier chapter. **[abstract only]** — [doi:10.1016/j.annals.2026.104151](https://doi.org/10.1016/j.annals.2026.104151)
- **N8, Verhulst & González Otero (2026).** Dependency/openness/agency triad. Content UNVERIFIED; read it. **[record only]** — [doi:10.2139/ssrn.6907425](https://doi.org/10.2139/ssrn.6907425)
- **N9, Pisani (2024, CLSR).** Self-determination in the platform economy. Flagged in August, still unopened, UNVERIFIED. **[record only]** — [doi:10.1016/j.clsr.2024.105964](https://doi.org/10.1016/j.clsr.2024.105964)
- **N10, Heylen (2023) and Tokuda (2026).** "Platform sovereignty" as the platform's sovereignty. These belong in Key Terms (bearer contrast) and correct strand 07. **[abstract only]** — [doi:10.1177/14614448231166057](https://doi.org/10.1177/14614448231166057); [doi:10.34382/0002007519](https://doi.org/10.34382/0002007519)
- **N11, Florea & Huang (2025, ISQ).** "Functional sovereignty" now has a mainstream IR owner beside Pasquale. Key Terms only. **[abstract only]** — [doi:10.1093/isq/sqaf069](https://doi.org/10.1093/isq/sqaf069)
- **N12, Huang & Xie (2022) and Alarcón et al. (2024).** Formal Shapley/nucleolus and intermediary-power precedents (Q4). **[record only]** — [doi:10.2139/ssrn.4039043](https://doi.org/10.2139/ssrn.4039043)
- Other works citing Lazar 2025 since June 2026, none colliding: Burnside 2026, Manuali 2026 (LLMs and democratic autonomy), Edenberg 2026 (algorithmic fairness and institutional justice), Kwok 2026b (generative AI and epistemic justice). **[record only]** — [doi:10.1177/01914537261454425](https://doi.org/10.1177/01914537261454425); [doi:10.1007/s13347-026-01184-4](https://doi.org/10.1007/s13347-026-01184-4); [doi:10.1007/s13347-026-01157-7](https://doi.org/10.1007/s13347-026-01157-7); [doi:10.1007/s13347-026-01225-y](https://doi.org/10.1007/s13347-026-01225-y)

### Inferences
- *Philosophy & Technology* has published three Lazar-citing platform-legitimacy pieces since June 2026. A referee from that venue will know the "legitimacy of the intermediary" frame well, so the abstract should state in one sentence that coordinative sovereignty is about the governed party's standing, not the governor's legitimacy.
- Safe novelty wording, given the sources reached: "I found no work that locates sovereignty in a coordinated actor's standing inside a mediation it cannot bypass, or that reads that standing through Shapley pivotality or core membership (OpenAlex, Crossref, arXiv and web, searched 24 October 2026)." Do not extend the claim to Semantic Scholar, PhilPapers, SSRN or Google Scholar until they are checked.

### Gaps
- Before the abstract goes out, three items need reading: Verhulst & González Otero (2026), Pisani (2024) and the full text of Dahlan (2026), whose fourth requirement is truncated.
- A cited-by trail on Schüßler et al. (2021) and Savolainen & Ruckenstein (2024) was not run.
- Recommended rerun after 2026-11-01: Consensus, Semantic Scholar (off-peak), and manual Google Scholar and PhilPapers for `"coordinative sovereignty"`, `"sovereignty" "bypass" platform voice`, and `Shapley "standing" platform`.

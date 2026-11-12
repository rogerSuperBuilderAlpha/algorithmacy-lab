<!-- Scout report, run rr-2026-11-k, written by a Claude (Opus 5.5) subagent on 11 Nov 2026. Candidates and leads only; nothing here is a verified source until read and carded. -->

# P5 scout: novelty check (K7, K9; claims A–F)

**Scope.** I searched for published work that already makes, names or anticipates the six parts of the paper's argument listed in the P5 brief: A (the authority–answerability split), B (the six-question test), C (the timing boundary), D (interruptible hospitality), E (K7: a duty of oversight that requires a channel from the affected person to someone with power over the single case) and F (K9: mediation leaves the duty and removes the path). I wrote no cards. Where I quote, I read the passage in a copy saved under `manuscript/revision_2026-11/research/sources/`; where I read only an abstract, the entry says so.

**The short answer.** Every one of A–F has a close relative in print outside hospitality, and two collide hard. Dan Davies's 'accountability sink' (2024) states A as a law of accountability. The White House OSTP *Blueprint for an AI Bill of Rights* (2022) and Canada's *Directive on Automated Decision-Making* (2019, amended to June 2025) between them state most of C, D's guest-side fallback and E's channel, and the Canadian directive ties the need for a human final decision to whether the impact is reversible. What I did not find in print is the hospitality application of any of them, the six-question test as an assembled instrument, the phrase 'interruptible hospitality', or a derivation of the channel from a holder's duty of oversight. The paper can keep those and must credit the rest.

---

## Part 1. Search log

All searches ran on 11 Nov 2026. Quotations marked 'abstract' for Brennan et al., Kong & Chang, Nguyen et al., Besio et al., Sposato, Wagner, Binns, Torrecilla-Pinero, Dwivedi et al. and Morosan & Dursun-Cengizci come from the abstract deposited in each Crossref record (`api.crossref.org/works/<doi>`, fetched 11 Nov 2026); I saved no copy of those records. 'Inspected' means I read the titles and, for anything plausible, the abstract. Consensus summaries and web-search summaries were used as leads only; every source listed in Part 3 has a record I fetched (Crossref, arXiv, OpenLibrary, the issuing body's own site, or the publisher PDF).

### 1.1 Consensus (`mcp__claude_ai_Consensus__search`, no filters)

| # | Query (exact) | Returned | Kept |
|---|---|---|---|
| C1 | accountability sink: decisions delegated to rules or algorithmic systems so that the person affected cannot reach anyone with authority to change the decision | 50 | Elden 2026 (×2), Sposato 2026, Torrecilla-Pinero 2026, Besio et al. 2025, Kong & Chang 2026, Brennan et al. 2026, Adensamer et al. 2021, Wieringa 2020, Cobbe et al. 2021 |
| C2 | human intervention required before an automated decision takes effect when its effects are irreversible; reversibility criterion for human oversight of AI | 50 | Enqvist 2023, Koulu 2020, Laux 2023, Herrmann 2025, Shu & Wei 2026 (arXiv), Baum et al. 2026 (SSRN), Haitsma & Brink 2025 |
| C3 | artificial intelligence ethics accountability responsibility in hospitality and tourism guests automated service | 50 | Binesh & Syah 2026, Koo & Kwon 2026, Dwivedi et al. 2026, Zhu et al. 2023, Ivanov & Umbrello 2021, Tlili et al. 2024, Hassan & Saleh 2026, Zhang 2026 |
| C4 | customers trapped by chatbots or automated customer service unable to reach a human agent with authority to resolve the problem | 40 | Castillo et al. 2021, Martijn et al. 2026, Dada et al. 2025, Chacon & Martínez 2026 |
| C5 | interruptibility of automated systems: users able to interrupt, stop or redirect an algorithmic process and appeal to a human | 40 | Perez 2026, Herrmann 2025, Cohen et al. 2023, McFarlane & Latorella 2002, Fanni et al. 2023 |
| C6 | individual justice and discretion in automated decision-making: human review to consider the particular case, exceptions to rules | 40 | Binns 2022, Cen & Raghavan 2023, McCann 2023, Cohen et al. 2023 |
| C7 | hotel or short-term rental guests unable to reach staff with authority when automated or self-service systems fail; unstaffed hotels, self check-in, service recovery | 40 | Xu & Greiffenhagen 2024 (already carded), Chen & Tussyadiah 2021, Liu et al. 2026, Najmudin et al. 2026 |
| C8 | algorithmic management of frontline hotel employees reduces discretion and authority to resolve guest complaints | 30 | Oezdemir et al. 2026, Spektor et al. 2023 and Jianu et al. 2025 (both already carded) |

### 1.2 OpenAlex (`api.openalex.org/works?search=`), top results inspected

| Query | Count | Outcome |
|---|---|---|
| `"accountability sink"` | 39 | Brennan, Edgar & Gorman 2026 (AAAJ); Nguyen et al. 2026 (AIES); a 2026 *Journal of Bentham Studies* piece; the rest grey (Zenodo, SSRN) or incidental |
| `contestability hotel` | 99,515 (top 8) | nothing on algorithmic contestability |
| `contestability hospitality` | 52,174 (top 8) | migration and border hospitality only (incl. Zare & Ye 2025, *Hospitality & Society* 15: 45–66) |
| `interruptibility service customer` | 156,549 (top 8) | all electricity supply or queueing theory |
| `"accountability sink" hotel` | 1 | irrelevant (mapping) |
| `algorithmic accountability hospitality guest` | 2,157 (top 8) | bias and transparency pieces; Pigac et al. 2026 (*CQ* 67: 283–297; already cited in v6) |
| `"right to a human" customer service` | 2,388 (top 8) | one grey Zenodo paper; nothing peer-reviewed |
| Works citing Alfrink et al. 2022, filtered `hospitality` / `hotel` / `tourism` | 1 / 1 / 4 | none in hospitality |
| Works citing Elish 2019, same filters | 5 / 4 / 8 | Moradi et al. 2025 (self-checkout in retail); none in hospitality |
| Works citing Bovens & Zouridis 2002, same filters | 4 / 15 / 15 | public administration only |
| Works citing Baum & Laux 2026, same filters | 0 / 0 / 0 | — |

### 1.3 Web search and catalogue checks

| Tool | Query (exact) | Returned | Outcome |
|---|---|---|---|
| WebSearch | `"interruptible hospitality"` | 18 | none uses the phrase; all business-interruption insurance or front-office interruptions |
| WebSearch | `Dan Davies "accountability sink" definition excerpt Unaccountability Machine` | 19 | led to Brown 2024 (blog quoting Davies p. 17) and to Brennan et al. 2026 |
| WebSearch | `Directive on Automated Decision-Making Appendix C human intervention final decision must be made by a human impact level reversible irreversible` | 10 | led to the Treasury Board text (read) and an EDPS checklist of May 2026 (refused, 403) |
| WebSearch | `ISO 10002:2018 complaints handling scope "provides guidance on the process of complaints handling" preview` | 18 | iso.org served a bot check (stopped); official sample pages via iTeh (read) |
| WebSearch | `"Law of Stop" interruptibility injunctions agentic AI Perez SSRN` | 10 | Perez 2026 (arXiv, read in part); Singapore Consensus 2026 (read p. 84) |
| WebSearch | `"Human Alternatives, Consideration, and Fallback" hotel OR hospitality OR "service encounter" scholarship 2023 2024 2025` | 10 | no scholarly use in hospitality; trade press only |
| WebSearch | `Huq "A Right to a Human Decision" Virginia Law Review 106 611 pdf` | 10 | journal PDF (read in part) |
| WebSearch | `Binns "Human judgment in algorithmic loops" individual justice pdf ora.ox.ac.uk OR arxiv OR reubenbinns` | 10 | no repository copy; Wiley copy refused automated fetch |
| OpenLibrary | `unaccountability machine davies` | 2 | Davies 2024, Profile Books / University of Chicago Press, ISBN 9781788169547 |
| OpenLibrary | `organisierte unverantwortlichkeit gegengifte` | 1 | Beck, *Gegengifte* (Suhrkamp 1988; Polity) |
| Crossref (`query.bibliographic`) | title-and-author queries for every named lead and candidate (Huq; Crootof, Kaminski & Price; Kaminski & Urban; Citron; Kluttz et al.; Rubel et al.; Peeters & Widlak; Wieringa; Thompson; Enqvist; Cummings; Orseau & Armstrong; Soares et al.; Lyons et al.; Ranchordás; Laux; Leo & Huh; Davies; Matthias; Adams & Balfour; Hansen et al.; Morosan & Dursun-Cengizci) | top 5 each | records in Part 3; Citron 2008 and Soares et al. 2015 not found by one query each and not pursued |

### 1.4 Snowballing

- **From Huq 2020** (n. 190, p. 649): the Public Voice *Universal Guidelines for AI* (2018) and its memorandum, which Huq quotes on inserting 'a human decision prior to an automated decision'. The site returned HTTP 500; lead only.
- **From Brennan et al. 2026**: back to Davies 2024 (the concept they 'operationalise').
- **From Binesh & Syah 2026**: forward to Morosan & Dursun-Cengizci 2024 (hotel guests' 'technology agency'; abstract read) and Tussyadiah 2020.
- **From Elden 2026a**: his companion papers (Elden 2026b, *AI and Ethics*, doi 10.1007/s43681-026-01359-x; 'The diffuse void', *AI Ethics* 6: 228), records only.
- **Forward from Alfrink, Elish, Bovens & Zouridis and Baum & Laux** (OpenAlex, table 1.2): no hospitality uptake.

### 1.5 Fetch failures (open in principle, closed to me)

Wiley (Binns 2022; Wagner 2019; Vogl et al. 2020), Emerald (Brennan et al. 2026), ScienceDirect (Adensamer et al. 2021), MDPI (Kong & Chang 2026; also refused WebFetch), Springer (Torrecilla-Pinero 2026; Fanni et al. 2023), the ACM DL (Wieringa; I used the Utrecht repository instead), the Vanderbilt repository PDF (Crootof et al. 2023), the EDPS checklist, and iso.org returned 403 or a bot check. The AAAI site (Nguyen et al. 2026) served a CAPTCHA, and I stopped. I made no attempt to get around any of these.

### 1.6 Copies saved by the stopped Fable attempt

The Fable P5 scout stopped at about 17:15 without writing a report, but it had saved files. I used them only after checking identity: the OSTP Blueprint (byte-identical to the copy I fetched from the archived White House site), the UN Guidelines for Consumer Protection (byte-identical to UNCTAD's), and Cen & Raghavan, Kaminski & Urban, Kiener, Goetze, Alkhatib & Bernstein, Castillo et al., CFPB 2023, Orseau & Armstrong and Elden 2026a (title and author checked against the record). Two faults:

- **`sources/huq2020right/fulltext.pdf` is the wrong article.** It holds Huq, 'Standing for the Structural Constitution' (a 2013 typescript). I saved the right one, 106 Va. L. Rev. 611, beside it as `p5_fulltext_106VaLRev611.pdf`.
- `sources/orseau2016safely/` holds a revised version dated 28 Oct 2016, not the UAI 2016 proceedings PDF, which is at auai.org and differs.

---

## Part 2. Outcome of every P5 lead

| Lead (LEADS.md) | Status | Outcome |
|---|---|---|
| [R] Binns, 'Human judgment in algorithmic loops' | **Verified; abstract only** | *Regulation & Governance* 16(1): 197–211 (2022), doi 10.1111/rego.12358. Open (hybrid), but Wiley refused automated fetch. Crossref abstract read. |
| [R] Huq, 'A right to a human decision' | **Verified; read in part** | 106 Va. L. Rev. 611 (2020); journal PDF saved. Read pp. 611–618, 648–650, 666–668. A defeater for D and E (Part 4). |
| [R] Kiener 2022 | **Verified; read in part** | *Ethical Theory and Moral Practice* 25(4): 575–593, doi 10.1007/s10677-022-10313-9. Abstract and §3 opening read. Kiener proposes a 'normative power of taking Retrospective Answerability'. It bears on K3's voluntary assumption, not on A–F; tier 3. |
| [R] Alfrink et al. 2022 | Already carded | Not repeated. |
| [M] 'accountability sink' | **Record exists; book closed** | Davies, *The Unaccountability Machine* (Profile Books 2024; ISBN 9781788169547). Not read. Quoted at p. 17 by Brown 2024 (a blog; saved). Taken up in Brennan, Edgar & Gorman 2026 (AAAJ; abstract only). **The collision for A.** |
| [M] 'moral crumple zone' (Elish) | **Verified; read in part** | *Engaging Science, Technology, and Society* 5: 40–60 (2019), doi 10.17351/ests2019.260. Abstract and introduction read. |
| [M] 'the problem of many hands' | **Verified; not read** | Thompson, *APSR* 74(4) (1980), doi 10.2307/1954312. Bovens 2007 and Cobbe et al. 2023, both carded, already carry it. |
| [M] Wagner 2019 | **Verified; abstract only** | *Policy & Internet* 11(1): 104–122, doi 10.1002/poi3.198. Defines 'quasi-automation'. |
| [M] Green 2022 | **Verified; read in part** | *Computer Law & Security Review* 45: 105681. Abstract and introduction read. |
| [M] Crootof, Kaminski & Price 2023 | **Record exists; abstract only** | 76 Vand. L. Rev. 429 (repository landing page); SSRN 10.2139/ssrn.4066781. PDF refused (403). |
| [M] Kaminski & Urban 2021 | **Verified; searched** | 121 Colum. L. Rev. (No. 7) (Nov 2021). Saved copy searched for timing and due process; they cite *Goldberg* and *Mathews* but do not tie contest to reversibility in the passages I found. |
| [M] Citron 2008 | **No record found** | One Crossref query returned nothing matching; not pursued. |
| [M] Matthias 2004 | **Verified; closed** | *Ethics and Information Technology* 6(3): 175–183. Not read. |
| [M] Goetze 2022 | **Verified; abstract read** | FAccT '22, pp. 390–400; open on PhilPapers. 'Moral entanglement'; tier 3. |
| [M] Coeckelbergh 2020 | Already carded (rejected) | Not repeated. |
| [M] Widder & Nafus 2023 | **Verified; not read** | *Big Data & Society* 10(1); open; saved by another agent. 'Dislocated accountabilities'; tier 3. |
| [M] Busuioc 2021 | **Verified; not read** | *PAR* 81(5): 825–836; open. |
| [M] Novelli, Taddeo & Floridi | **Verified; not read** | *AI & Society* 39(4): 1871–1882 (2024; online 2023). |
| [M] Lazcoz & de Hert 2023 | **Verified; not read** | *CLSR* 50: 105833. |
| [M] Kluttz et al. 2020 | **Record exists in other versions** | SSRN 2019 (10.2139/ssrn.3311894) and a 2022 reprint (10.1201/9781003278290-62); the 2020 chapter's DOI was not found. |
| [M] Henin & Le Métayer 2022 | **Verified; not read** | *AI & Society* 37(4): 1397–1410; open at HAL. |
| [R] Binesh & Syah 2026 | **Verified; read in part** | *Frontiers in AI* 9, doi 10.3389/frai.2026.1913343. Crossref gives the first author as Nasim Binesh; Consensus gives Fatemeh. I read the epistemic reading of autonomy (PDF p. 10) and the risk table. **The nearest hospitality statement of D and part of F.** |
| [R] Sharma & Mattila 2025 | Already carded | Not repeated. |
| (P1 lead) Koo & Kwon 2026 | **Closed** | Unpaywall (11 Nov 2026) reports closed with no repository copy; the abstract is carded (`koo2026three`). No open full text found. |

---

## Part 3. Candidates

Tier 1: a claim rests on it, or it could refute or pre-empt one. Tier 2: it strengthens or narrows. Tier 3: peripheral. The 'Bears on' column gives the claim and direction: **=** states it already (credit it), **≈** a near neighbour, **−** refutes or narrows, **+** supports.

### 3.1 Tier 1

| Source | Record | Type | Open copy | Read | Bears on |
|---|---|---|---|---|---|
| **Davies 2024**, *The Unaccountability Machine* | OpenLibrary OL37568651W; ISBN 9781788169547 | book | **closed** | quotations only, at second hand (Brown 2024) | **A =**, F ≈, K7-P3 ≈ |
| **OSTP 2022**, *Blueprint for an AI Bill of Rights*, 'Human Alternatives, Consideration, and Fallback', pp. 46–52 | bidenwhitehouse.archives.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf (fetched; SHA-256 ab34b52e…) | US federal soft law (white paper, non-binding) | open; `sources/ostp2022blueprint/` | pp. 46–52 in full | **C =, D ≈, E =, B(6) =** |
| **Treasury Board of Canada**, *Directive on Automated Decision-Making* (in force 1 Apr 2019; page modified 24 Jun 2025) | tbs-sct.gc.ca/pol/doc-eng.aspx?id=32592 | government directive (binding on federal institutions only) | open; `sources/tbscanada2019directive/` | §§1–6, App. B, App. C | **C =, E =** |
| **UN Guiding Principles on Business and Human Rights** (OHCHR 2011, HR/PUB/11/04), Principles 29, 31 | ohchr.org PDF (re-fetched; SHA-256 96b69f97… identical to the saved copy) | soft law | open; already carded (`un2011guiding`) | General principles; 28–31 with commentary | **E =**, K7-P3 =, E **−** (31(h)) |
| **Bovens & Zouridis 2002**, 'From street-level to system-level bureaucracies', *PAR* 62(2): 174–184 | doi 10.1111/0033-3352.00168 | article | open author manuscript, Utrecht repository; `sources/bovens2002street/` | §§3–5 searched and read in part | **A ≈** (public administration), E ≈ |
| **Elden 2026a**, 'When responsibility fails to arise', *AI and Ethics* 6(4) | doi 10.1007/s43681-026-01204-1 | article | open; HTML saved by the stopped attempt (`sources/elden2026responsibility/`) | abstract, §§1, 3, 4.4, 7.3, 8 | **C =, D ≈**, F **−** |
| **Huq 2020**, 'A right to a human decision', 106 Va. L. Rev. 611 | journal PDF, virginialawreview.org | article | open; `sources/huq2020right/p5_fulltext_106VaLRev611.pdf` | pp. 611–618, 648–650, 666–668 | D **−**, E **−**, C ≈ |
| **Binesh & Syah 2026**, 'AI ethics in hospitality and tourism', *Frontiers in AI* 9 | doi 10.3389/frai.2026.1913343 | scoping review | open; `sources/binesh2026ai/` | PDF p. 10 and risk table | **D ≈, B ≈, F ≈ (hospitality)** |
| **Koo & Kwon 2026**, IJCHM 38(8): 2471–2486 | doi 10.1108/ijchm-10-2025-1555 | conceptual article | **closed** | abstract (carded) | **F ≈ (hospitality)**; open |
| **Elish 2019**, 'Moral crumple zones' | doi 10.17351/ests2019.260 | article | open; `sources/elish2019moral/` | abstract, introduction | **A ≈** (the blame-side inverse) |
| **Kong & Chang 2026**, 'Displacement, dilemma, and exit', *Social Sciences* 15(9): 593 | doi 10.3390/socsci15090593 | article | open but MDPI refused fetch | Crossref abstract only | **A ≈, F ≈** |

### 3.2 Tier 2

| Source | Record | Type | Open copy | Read | Bears on |
|---|---|---|---|---|---|
| Brennan, Edgar & Gorman 2026, 'Accountability sinks, accountability gaps and technological injustice', AAAJ | doi 10.1108/aaaj-11-2025-8532 | case study (Post Office/Horizon) | open but Emerald refused fetch | Crossref abstract | A = (applies Davies) |
| Nguyen, Späthe, Lins & Sunyaev 2026, 'No one to blame', AIES 9(3): 1908–1919 | doi 10.1609/aies.v9i3.43277 | qualitative study | CAPTCHA; not reached | Crossref abstract | A ≈, B ≈ (a 20-question diagnostic) |
| Perez 2026, 'The Law of Stop', arXiv 2609.22882 v2 | arXiv abstract page | preprint | open; `sources/perez2026law/` | abstract, contents, pp. 11, 15, 81, 85 | D ≈, C ≈ |
| Casper et al. 2026, Singapore Consensus, arXiv 2608.14611 | arXiv abstract page | consensus report | open; `sources/casper2026singapore/` | p. 84 (Principle 8) | D: owns the AI-safety sense of the term |
| Orseau & Armstrong 2016, 'Safely interruptible agents', UAI 2016 | auai.org/uai2016/proceedings/papers/68.pdf (HTTP 200) | conference paper | open; saved copy is a revised version | abstract | D: origin of the term in AI safety |
| McFarlane & Latorella 2002, *Human–Computer Interaction* 17(1): 1–61 | doi 10.1207/s15327051hci1701_1 | article | closed | record only | D: the HCI sense (the human is interrupted) |
| Westmoreland 2008 (already carded) | doi 10.3860/krit.v2i1.566 | article | open | p. 1 searched | D: 'interruption' in hospitality theory |
| Cen & Raghavan 2023, 'The right to be an exception to a data-driven rule' | doi 10.21428/2c646de5.a15f7255 | case study / essay | open (arXiv 2212.13995v1 saved) | abstract | D ≈ ('treated as an exception') |
| Cohen et al. 2023, 'putting humans in the loop only on appeal', *npj Digit. Med.* 6: 160 | doi 10.1038/s41746-023-00906-8 | perspective | open; `sources/cohen2023appeal/` | p. 2 | C ≈; synchronous human **−** |
| Alkhatib & Bernstein 2019, 'Street-level algorithms', CHI '19 | doi 10.1145/3290605.3300760 | conference paper | saved by the stopped attempt | abstract | C ≈, D ≈ |
| Binns 2022 | doi 10.1111/rego.12358 | article | open but refused | Crossref abstract | E ≈ (the single case) |
| Wagner 2019 | doi 10.1002/poi3.198 | article | open but refused | Crossref abstract | 'quasi-automation' (rubber-stamping) |
| Green 2022 | doi 10.1016/j.clsr.2022.105681 | article | open | abstract, introduction | E **−** (oversight as legitimation) |
| Crootof, Kaminski & Price 2023 | 76 Vand. L. Rev. 429 | article | PDF refused | abstract | E **−** ('MABA-MABA trap') |
| Wieringa 2020, 'What to account for when accounting for algorithms', FAT* '20 | doi 10.1145/3351095.3372833 | systematic review | open, Utrecht repository; `sources/wieringa2020what/` | §§2–3 searched | B ≈ (five elements after Bovens) |
| Sposato 2026, 'Delegated but not absolved', *The Bottom Line* | doi 10.1108/bl-04-2026-0109 | conceptual | closed | Crossref abstract | E ≈, F ≈ (organizations) |
| Besio et al. 2025, 'Algorithmic responsibility without accountability', *Systems Research and Behavioral Science* 42(3): 739–755 | doi 10.1002/sres.3028 | conceptual | open, not fetched | Crossref abstract | A ≈ (Luhmann) |
| Dwivedi et al. 2026, 'corporate digital responsibility in tourism and hospitality', JHTI | doi 10.1108/jhti-03-2026-0339 | critical reflection | closed | Crossref abstract | E ≈, F ≈ (hospitality) |
| CFPB 2023, 'Chatbots in consumer finance' (issue spotlight, 6 Jun 2023) | consumerfinance.gov (verified by WebFetch) | regulator report | open; saved by the stopped attempt | section 'Failure to provide meaningful customer assistance' | F (consumer finance) = |
| Castillo, Canhoto & Said 2021, *Service Industries Journal* 41(13–14): 900–925 | doi 10.1080/02642069.2020.1787993 | qualitative study | open (Brunel accepted manuscript) | AAM p. 25 | F (service evidence) + |
| ISO 10002:2018, *Guidelines for complaints handling in organizations* | iso.org/standard/71580 (bot check); official sample via iTeh | international standard | sample of cl. 0–4 only; `sources/iso2018complaints/` | Introduction; cl. 1, 4 | E ≈ |
| OECD *Guidelines for Multinational Enterprises on Responsible Business Conduct* (2023) | doi 10.1787/81f92357-en | soft law | open; saved by the stopped attempt | Commentary on Ch. IV para 51; Ch. VIII para 3 and commentary para 99 | E ≈ |
| UN *Guidelines for Consumer Protection* (UNCTAD 2016; GA res. 70/186) | UNCTAD/DITC/CPLP/MISC/2016/1 (byte-identical to UNCTAD's copy) | soft law | open | para. 11(f) | E ≈ |
| EU AI Act, art. 7(2)(g) and (i) (library card `eu2024aiact`) | Regulation (EU) 2024/1689 | statute | open | art. 7(2) | C ≈, B(6) ≈ |
| *Mathews v Eldridge* (library card `mathews1976eldridge`) | 424 U.S. 319 | case | open | card only | C = (government) |
| Torrecilla-Pinero 2026, 'Judgment cannot be delegated', *Philosophy & Technology* 39(3) | doi 10.1007/s13347-026-01140-2 | conceptual | open but Springer refused | Crossref abstract | C ≈ ('theorems for … reversibility') |
| Herrmann 2025/2026, 'Intervenability as a design requirement', arXiv 2607.10322 | doi 10.1007/978-3-031-83512-4_9 | chapter preprint | open; `sources/herrmann2025intervenability/` | abstract; pp. 144, 148 searched | D ≈ (operator side) |
| Morosan & Dursun-Cengizci 2024, IJCHM 36(3): 946–974 | doi 10.1108/ijchm-08-2022-1041 | survey (n = 400 hotel guests) | closed | Crossref abstract | F (hospitality evidence) |
| Brown 2024, 'Accountability sinks' (blog, A Working Library, 16 Oct 2024) | aworkinglibrary.com/writing/accountability-sinks | grey | open; `sources/brown2024accountability/` | whole page | A in a hotel example (grey) |

### 3.3 Tier 3 (records fetched; not read unless stated)

Matthias 2004; Thompson 1980; Kiener 2022 (read in part); Goetze 2022; Widder & Nafus 2023; Busuioc 2021; Novelli et al. 2024; Lazcoz & de Hert 2023; Henin & Le Métayer 2022; Kaminski & Urban 2021 (searched); Lyons et al. 2022 (CHI, doi 10.1145/3491102.3517606), 2023 (FAccT, 10.1145/3593013.3594041) and 2025 (PACM HCI, 10.1145/3757468); Enqvist 2023 (*LIT* 15(2): 508–535); Laux 2023 (*AI & Society*, 10.1007/s00146-023-01777-z); Koulu 2020; Butler 2025 (*OJLS* 45(3): 727–752); Fanni et al. 2023 (*AI & Society* 38(2)); Vogl et al. 2020 ('algorithmic bureaucracy', *PAR* 80(6)); Adensamer, Gsenger & Klausner 2021 ('"Computer says no"', *JRT* 7–8: 100014; no Crossref abstract, content unread); Peeters & Widlak 2018 ('The digital cage', *GIQ* 35(2), closed); Rubel, Castro & Pham 2019 ('Agency laundering', *ETMP* 22(4)); Adams & Balfour, *Unmasking Administrative Evil* (1998; 2019 ed., 10.4324/9780429432293); Beck, *Gegengifte* (1988); Zhu et al. 2023 (PLoS ONE, roboethics review); Ivanov & Umbrello 2021; Tlili et al. 2024; Hassan & Saleh 2026; Liu et al. 2026; Oezdemir et al. 2026 (FAccT); Moradi, Levy & Cheyre 2025 ('pseudo-automation' in retail).

---

## Part 4. Answers to the seven questions

### Q1. Published names for A

A says that the party able to change a decision, or the rule behind it, is not a party the affected person can reach. Five published names come close, and one of them is A.

**'Accountability sink' (Davies 2024) is A.** The book is closed to me, so everything below reaches it through Mandy Brown's blog, which quotes two passages and gives p. 17 for both. Davies, as Brown quotes him: 'For an accountability sink to function, it has to break a link; it has to prevent the feedback of the person affected by the decision from affecting the operation of the system.' He also states what he calls 'The fundamental law of accountability: the extent to which you are able to change a decision is precisely the extent to which you can be accountable for it, and vice versa.' That law is the authority–answerability split stated as a principle, and the 'broken link' is K7's channel stated as its absence. Brown illustrates it with a hotel: a manager far off cuts the cleaning staff, the room is not ready, the clerk 'can offer a voucher, but what you need is a room', and 'There's no one to call to complain'. The scenario is hers, not Davies's. Brennan, Edgar and Gorman (2026) carry the concept into an accounting journal and read the Post Office Horizon scandal through it: 'digitisation creates accountability sinks, whereby decision-making is delegated to computer systems so that humans are not responsible or in control. The accountability feedback loop is broken' (abstract). **Nearness to A: identical in structure. Hospitality appears in grey literature only.**

**'System-level bureaucracy' (Bovens & Zouridis 2002) states A for public administration, twenty-four years earlier.** In their author manuscript the system-level bureaucracy keeps three groups of staff, the third being 'the 'interfaces' between citizens and the information system, such as public information officers, helpdesk members and the legal staff charged with handling the complaints … The hundreds of individual case-managers have all vanished' (ms p. 14). Discretion has moved: 'The system designers, legal policy staff and IT experts are to be regarded in particular as the new equivalents to the former street-level bureaucrats' (ms p. 16). The citizen reaches a helpdesk, and the designers hold the rule. They also ask whether 'an expert system that leaves no room for *Einzelfallgerechtigkeit*' (individual-case justice) can 'still be regarded as just' (ms p. 17), which is E's 'single case'. Their pages are the manuscript's, not *PAR*'s. **Nearness: close, for citizens and the state.** v6 already makes the same move ('authority over the rule drifts towards whoever designs, configures or controls it') and does not cite them.

**'Moral crumple zone' (Elish 2019) is A seen from the blame side.** Elish introduces it 'to describe how responsibility for an action may be misattributed to a human actor who had limited control over the behavior of an automated or autonomous system' (p. 40). The reachable person lacks control and takes the blame. A is about the claim that cannot travel, not about blame misplaced, but the configuration is the same: the person in reach is not the person with power. **Nearness: partial; the inverse register.**

**'Accountability anchor displacement' (Kong & Chang 2026)** 'names the condition in which distributed architectures dissolve or functionally bypass the subject to whom the demand for an account must be addressed' (abstract). The paper works from blockchain governance to AI and draws on Hirschman. I read only the abstract; MDPI refused the fetch. **Nearness: close to A and to F, by the abstract.**

**Other names.**
- Nguyen et al. (2026) coin 'constitutive AI unaccountability' and build 'a diagnostic instrument of 20 questions' (abstract). That makes them a neighbour of B as well. Not read; CAPTCHA.
- Besio et al. (2025) separate responsibility from accountability after Luhmann. In their abstract, algorithms 'can indeed take responsibility but cannot be made accountable for errors'. A neighbour.
- Sposato (2026, abstract): treating algorithms as delegates 'removes accountability without removing authority'. Close in wording; a short managerial piece.
- 'Responsibility gap' (Matthias 2004; four gaps in Santoni de Sio and Mecacci, carded) concerns whether anyone is responsible, not whether the responsible party can be reached. Not A.
- The 'problem of many hands' (Thompson 1980; Bovens 2007 and Cobbe et al. 2023, carded) concerns dispersal. Not A.
- 'Street-level algorithms' (Alkhatib & Bernstein 2019) concerns when criteria are refined, 'only after the decision is made' (abstract). Nearer C and D than A.
- 'Algorithmic bureaucracy' (Vogl et al. 2020), 'organized irresponsibility' (Beck 1988), 'administrative evil' (Adams & Balfour) and '"Computer says no"' (Adensamer et al. 2021): records only. I read none and do not characterise them.

### Q2. Contestability and the right to a human decision (B–E)

The contestability literature is carded (Alfrink, Lyons, Vaccaro, Sterz, Baum & Laux). The new material falls into three groups.

**Guest-side human fallback is already stated in soft law.** The OSTP Blueprint opens its fifth principle: 'You should be able to opt out, where appropriate, and have access to a person who can quickly consider and remedy problems you encounter' (p. 46).
- **Cost of refusing (B6).** People should be able to 'conveniently opt out of an automated system and will not be disadvantaged for that choice' (p. 47).
- **Authority to change (E).** The fallback must be 'Effective', so that 'if the human decision-maker charged with reassessing a decision determines that it should be overruled, the new decision will be effectively enacted' (p. 50).
- **Timing (C).** In 'time-critical systems, this mechanism should be immediately available or, where possible, available before the harm occurs' (p. 50).
- **Examples.** It offers 'a building manager who can open a door in the case an automated card access system fails' and companies that 'retain the option of dialing zero to reach an operator' (p. 47).

This principle states B's sixth question, E's authority to change, C's timing and the fallback half of D, though not for hospitality and not as a duty of a host. The Canadian Directive requires recourse that is 'timely, effective, and easy to access' (6.4.1.1). It also requires monitoring that documents 'client feedback, unexpected impacts, human overrides … and other system failures' and uses them 'to identify issues and take corrective actions' (6.3.4–6.3.4.1). That is K7's P3 (a holder must be able to learn of failure) in administrative form.

**Oversight and its failure modes.** Wagner (2019, abstract) defines 'quasi-automation' as 'inclusion of humans as a basic rubber-stamping mechanism in an otherwise completely automated decision-making system'. Green (2022) argues that human oversight policies 'provide a false sense of security in adopting algorithms and enable vendors and agencies to shirk accountability for algorithmic harms' (abstract), and proposes 'institutional oversight' instead. Crootof, Kaminski and Price (2023, abstract) name 'the MABA-MABA trap' and conclude that 'policymakers should regulate the human-in-the-loop system'. These support v6's line that presence is not authority (already carried by Baum & Laux and Sterz). They also count against any reading of D that equates a reachable human with a remedy.

**A right to a human decision, and individual justice.**
- **Huq (2020) argues against the right.** He finds that such claims 'are better understood to turn on the timing, and not the sheer fact, of such involvement' (p. 618). He thinks 'human review seems generally to increase net error rates' (p. 667), and he expects that 'wealth or epistemic resources or social class will predict the tendency to appeal' (p. 668). In place of the right he proposes 'a justiciable "right to a well-calibrated machine decision"' (p. 612).
- **Binns (2022, abstract) argues for the human.** He holds that individual justice, each case 'assessed on its own merits', 'can only be meaningfully served through human judgment', and warns of 'inequities in individual justice' from 'uneven application of human judgment'.
- **Cen and Raghavan (2023, abstract)** argue 'that individuals have the right to be an exception to a data-driven rule', weighted by individualisation, uncertainty and harm. That is D's 'treated as an exception', stated as a right of the decision subject.

How these bear on B–E:
- **B.** The components are in print: Lyons and Alfrink's four specify questions (carded); Wieringa's five elements after Bovens (actor, forum, relationship, account, consequences; FAT* '20, §2–3); OSTP's opt-out; and the AI Act's own high-risk criterion, 'it is not reasonably possible to opt-out from that outcome' (art. 7(2)(g)). The six questions in this order, with the cost of refusing as a condition of standing, I did not find.
- **C.** See Q3.
- **D.** See Q4.
- **E.** The channel to someone with authority is in print in soft law (Q6) and in OSTP and the Canadian directive. Huq and Green narrow it.

### Q3. Timing (C)

C is in print in at least five places outside hospitality. The strongest is government policy.

- **Canada's Directive on Automated Decision-Making** ties human involvement to reversibility. Appendix B grades impact. Level I covers decisions with 'little to no, easily reversible, and brief impacts', Level II 'moderate, likely reversible and short-term impacts', Level III 'high, difficult to reverse and potentially ongoing impacts', and Level IV 'very high, irreversible and perpetual impacts'. Appendix C, 'Ensuring human involvement', then allows that at Levels I–II 'The system may make decisions and assessments without direct human involvement', and requires at Levels III–IV that 'The final decision must be made by a human.' The directive applies 'to any automated decision system in production used to make an administrative decision or a related assessment about a client' (5.1). It binds Canadian federal institutions only. It states a human-before-effect rule indexed to reversibility, which is C's structure.
- **OSTP (2022)**: 'In time-critical systems, this mechanism should be immediately available or, where possible, available before the harm occurs' (p. 50), and for sensitive domains, 'automated systems should not be allowed to directly intervene in high-risk situations … without human consideration' (p. 51).
- **Elden (2026a)** proposes 'deliberative apertures': 'Institutionally mandated moments must exist at which algorithmic determinations surface for human deliberation before becoming effective'. The pause holds the determination 'for some external party, whether a reviewing officer, an affected person, or a designated public role, to see it and respond before it is enforced. The width of the aperture is a design parameter and should reflect the stakes of the determination' (§7.3). He contrasts them with 'appeals processes, which operate after the decision has taken effect' (§7.3); appeals 'are downstream' (§4.4). This is C, stated for public administration, with the stakes setting the width. Elden does not use reversibility as the test; v6 does.
- **Due process law.** *Mathews v Eldridge* (carded by P4) states the principle and the limit: a prior hearing turns on whether later relief is full, and a later hearing usually suffices. Kaminski and Urban cite *Goldberg* and *Mathews* in the same vein.
- **Cohen et al. (2023)** argue for 'humans only on appeal rather than involving them to validate every AI/ML decision' (p. 2). Their own exception is irreversibility, without the word: a patient with few eggs left may want to appeal the ranking of embryos, 'since accepting the AI/ML decision may mean they never reproduce at all' (p. 2).
- **Neighbours on timing**:
  - Huq on 'the timing, and not the sheer fact' (p. 618).
  - The EU AI Act counts 'the extent to which the outcome … is easily corrigible or reversible' among the criteria for adding high-risk uses (art. 7(2)(i)). It uses reversibility to classify a use, not to time a human.
  - The *Universal Guidelines for AI* memorandum (2018), quoted by Huq at n. 190: when it is not 'possible or practical to insert a human decision prior to an automated decision'. A lead only; the site returned HTTP 500.
  - Torrecilla-Pinero (2026, abstract) derives 'governance theorems for … reversibility'. Not read.
  - Perez (2026) builds a law of stop on the analogy of injunctions. I did not reach a reversibility test in the parts I read.
  - The Singapore Consensus (2026, p. 84) gives irreversibility as the reason interruptibility matters ('actions may be irreversible').

**Verdict on C.** In print for another domain. Baum & Laux remain the cleanest conceptual source for timing relative to effect ('whether intervention can occur before the token output becomes effective', 2026: 120, as carded). The Canadian directive is the cleanest source tying it to reversibility, and v6 should cite it, or at least know it. The hospitality typology (v6 Table 1) is new.

### Q4. Interruptibility (D)

Three literatures already own the word, each in a different sense, and none puts the interruption in the guest's hands with a counterparty to receive it.

- **AI safety (the operator interrupts the agent).** Orseau and Armstrong (2016, abstract) frame the problem as the moment when 'it may be necessary for a human operator to press the big red button to prevent the agent from continuing a harmful sequence of actions'. Their worry is that a learning agent will learn to avoid interruption. The Singapore Consensus (2026) fixes the current definition: 'Interruptibility means that human operators can safely pause, redirect, stop, and reverse an AI agent's actions at any point, and that the agent cannot tamper with these mechanisms' (Principle 8, p. 84). Three of v6's four verbs ('stop', 'redirect' and, in effect, 'pause') are already there, held by operators. Perez (2026) widens the term into a legal 'theory of stop' with four dimensions. One of them, 'epistemic standing', 'asks whose knowledge counts in initiating, validating, or contesting an interruption' (p. 11). He comes nearest to D when he proposes 'a clearly marked manual control that anyone present can use to initiate a safe stop, without credentials or technical knowledge' (p. 85). But that is for physical hazards, and it has no counterparty. The EU AI Act's 'stop' button (art. 14(4)(e)) is already cited in v6.
- **HCI (the system interrupts the human).** McFarlane and Latorella (2002) study 'human interruption' in interface design: when a system may break into a person's task. That is the reverse direction (record only). Herrmann (2025/2026) proposes 'intervenability' for users and operators. He calls it a phenomenon 'not covered by emergency shutdowns, workarounds, or the reconfiguration of automated systems' (abstract) and extends it to 'AI-based discrete case-related decision-making' (abstract). It sits on the operator side, not the subject side.
- **Hospitality theory (the guest interrupts the host).** Westmoreland (2008, carded) opens with Derrida's question, 'Is not hospitality an interruption of the self?' (p. 1), and builds the guide around 'interruption'. A reader of *Hospitality & Society* may hear that sense first.
- **Neighbours that put the move with the affected person.**
  - Elden's deliberative aperture gives 'an affected person' time to 'respond before it is enforced' (§7.3).
  - OSTP's human 'fallback and escalation' (pp. 46–50).
  - Cen and Raghavan's right to be an exception.
  - Binesh and Syah call for 'real human override at the service encounter' (PDF p. 10).
- **'Seamful design'** (Chalmers & Galani, carded) is v6's interface neighbour. I found no newer source that changes the picture.

**Verdict on D.** The phrase 'interruptible hospitality' is not in print (WebSearch, 18 results; OpenAlex and Consensus, none). The word 'interruptibility' belongs to AI safety, and v6 should say that it moves the term from the operator to the guest and adds the counterparty. The guest-side content (stop, ask, redirect, be an exception, with someone there) is in print for other domains in pieces, and assembled nowhere I found.

### Q5. Hospitality, tourism and services (F)

**Koo and Kwon (2026).** I confirmed the abstract against Crossref and found no open full text (Unpaywall closed; no repository copy). The card records what the abstract says: the machine age 'relocates ethical responsibility within socio-technical design'. Whether they say the guest loses a path to authority cannot be told. **Still open; still the decisive closed source for F in hospitality.**

**Binesh and Syah (2026)** come closest in print. Reviewing 32 studies, they read hotel personalisation as acting on 'inferred beliefs about guests … without the guest's knowledge or ability to contest them'. They write that the 'off-the-loop' condition reported by Morosan and Dursun-Cengizci 'worsens the harm because neither guests nor employees can override the system', and they conclude that protecting autonomy 'requires contestability, meaning ways for guests to see, question, and correct the inferences held about them, plus real human override at the service encounter' (PDF p. 10). That is B's 'who can see' and 'who can override', and D's override at the encounter. It is grounded in guest autonomy, not in a host's duty, and it says nothing of who must answer or of timing. The authors should read the whole article before v7 claims that hospitality research has not asked for a reachable override.

**Other hospitality candidates.**
- Dwivedi et al. (2026, JHTI, closed) define corporate digital responsibility in tourism and hospitality as 'the auditable duties of care for the design, deployment, and governance of digital and AI systems that shape stakeholders' welfare, rights, and the distribution of value'. They organise it around 'the service-ecosystem structure that links firms to platforms, vendors, and partners' (abstract). That is a hospitality claim about duties across an ecosystem of firms, near K8 and F. Abstract only.
- Gursoy (2026) and Shabnam et al. (2026) are carded and already in v6.
- Morosan and Dursun-Cengizci (2024, abstract) measure how far hotel guests would let AI decide for them. That is evidence, not argument.
- Xu and Greiffenhagen (2024) are carded, and narrow K9: the chain kept a worker on site.

**Service research on customers trapped by automation.**
- **CFPB (2023).** In its section 'Failure to provide meaningful customer assistance', the Bureau finds that chatbots may 'lead them in continuous loops of repetitive, unhelpful jargon or legalese without an offramp to a human customer service representative', and calls these '"doom loops"'. The Bureau notes that the spotlight 'is not intended to impose any obligations or define any rights'. This is F's mechanism in consumer finance, from a regulator.
- **Castillo, Canhoto and Said (2021)** found that under a 'chatbot first, agent second' policy customers 'have to pass through the chatbot first and instruct the chatbot to transfer the conversation on to a human', and that in 'urgent, emotional situations' they may miss the option (AAM p. 25).
- **Digital captivity** (Wilson-Nash et al.) is carded.

**Verdict on F.** The general thesis is in print. Kong (2026, carded) holds that answerability is conserved. Davies, CFPB and Bovens & Zouridis describe the path being cut. For hospitality, the conjunction (the duty stays, the path is cut) is not in any text I could read; Binesh and Syah state half of it and Koo and Kwon may state the other. **New for hospitality, provisionally**, until Koo and Kwon are read.

### Q6. Operational grievance mechanisms (E)

**UN Guiding Principles on Business and Human Rights (OHCHR 2011)**, read from the official PDF (byte-identical to OHCHR's copy, re-fetched today).

- **Principle 29 (p. 31), exactly:** 'To make it possible for grievances to be addressed early and remediated directly, business enterprises should establish or participate in effective operational-level grievance mechanisms for individuals and communities who may be adversely impacted.'
- **Commentary (pp. 31–32).** Such mechanisms 'are accessible directly to individuals and communities who may be adversely impacted by a business enterprise'. They 'do not require that those bringing a complaint first access other means of recourse'. They 'perform two key functions':
  - 'First, they support the identification of adverse human rights impacts as a part of an enterprise's ongoing human rights due diligence. They do so by providing a channel for those directly impacted by the enterprise's operations to raise concerns when they believe they are being or will be adversely impacted.'
  - 'Second, these mechanisms make it possible for grievances, once identified, to be addressed and for adverse impacts to be remediated early and directly by the business enterprise, thereby preventing harms from compounding and grievances from escalating.'
- **Principle 31 (pp. 33–34).** Non-judicial grievance mechanisms, 'both State-based and non-State-based', should be legitimate, accessible, predictable ('providing a clear and known procedure with an indicative time frame for each stage'), equitable, transparent, rights-compatible and 'A source of continuous learning'. Operational-level mechanisms should also be '(h) Based on engagement and dialogue'.
- **Commentary on 31 (pp. 34–35).** Among other things: 'The eighth criterion is specific to operational-level mechanisms that business enterprises help administer' (p. 34). And under (h): **'Since a business enterprise cannot, with legitimacy, both be the subject of complaints and unilaterally determine their outcome, these mechanisms should focus on reaching agreed solutions through dialogue. Where adjudication is needed, this should be provided by a legitimate, independent third-party mechanism'** (p. 35).
- **To whom they apply.** 'These Guiding Principles apply to all States and to all business enterprises, both transnational and others, regardless of their size, sector, location, ownership and structure' (General principles, p. 1). Principle 29 is addressed to business enterprises, for 'individuals and communities who may be adversely impacted'. Their subject is human-rights impacts, and 'Nothing in these Guiding Principles should be read as creating new international law obligations' (p. 1).

**What this means for E.** The first function is K7's P3 (a holder learns of failure from those affected), and the second is E's early correction. Both are stated for human-rights due diligence. The commentary on 31(h) cuts against one reading of E. A firm's own officer 'with power over the single case' is the thing the UNGP says cannot legitimately decide a complaint against the firm alone. Read strictly, E needs either agreement through dialogue or an independent adjudicator beyond the firm's own reviewer. R2 has already carded the instrument (`un2011guiding`, flag `must-engage`); this commentary should be added to the card's threats if it is not there.

**Other soft-law and standards sources stating parts of E.**
- **OECD Guidelines for Multinational Enterprises (2023).**
  - Commentary on Ch. IV, para 51 (p. 27): 'operational-level grievance mechanisms for those potentially impacted by enterprises' activities can be an effective means of providing for such processes when they meet the core criteria of: legitimacy, accessibility, predictability, equitability, compatibility with the Guidelines, transparency, rights-compatibility, being a source of continuous learning, and are based on dialogue and engagement with a view to seeking agreed solutions'.
  - For consumers, Ch. VIII para 3 (p. 43): enterprises should 'Provide consumers with access to fair, easy to use, timely and effective non-judicial dispute resolution and redress mechanisms, without unnecessary cost or burden'.
  - Commentary para 99 (p. 45) ties para 3 to the OECD Recommendation on Consumer Dispute Resolution and Redress [OECD/LEGAL/0356] (not fetched).
- **UN Guidelines for Consumer Protection (2016), para. 11(f) (p. 10):** 'Businesses should make available complaints-handling mechanisms that provide consumers with expeditious, fair, transparent, inexpensive, accessible, speedy and effective dispute resolution without unnecessary cost or burden.'
- **ISO 10002:2018**, read from the official sample pages (cl. 0–4 only; iso.org served a bot check).
  - Scope: 'guidelines for the process of complaints handling related to products and services within an organization' (cl. 1).
  - It 'does not apply to disputes referred for resolution outside the organization' (cl. 1).
  - Accessibility: 'A complaints-handling process should be easily accessible to all complainants' (4.5, p. 3).
  - Accountability: 'The organization should establish and maintain accountability for, and reporting on, the decisions and actions with respect to complaints handling' (4.12, p. 4).
  - Timeliness: 'Complaints should be handled as expeditiously as feasible given the nature of the complaint and of the process used' (4.15, p. 4).
  - Clause 5.4, 'Responsibility and authority', is listed in the contents but is not in the sample; whether it requires authority to resolve the single case is **closed**.
- **OSTP Blueprint** and the **Canadian Directive**: see Q2 and Q3.
- **Not reached.** The EDPS 'Checklist on human intervention of ADM' (May 2026; 403); the OECD AI Recommendation [OECD/LEGAL/0449], whose page rendered empty to a script; the Council of Europe Framework Convention (not searched).

### Q7. What survives

| Claim | Status | Nearest sources | Gap statement |
|---|---|---|---|
| **A.** Authority–answerability split | **(ii) In print for another domain; new for hospitality in scholarly work.** The name is new; the concept is not. | Davies 2024 ('accountability sink'; 'fundamental law of accountability', p. 17, quoted by Brown 2024); Bovens & Zouridis 2002 (ms pp. 14, 16); Kong & Chang 2026 (abstract); Brennan et al. 2026 (abstract); Elish 2019 (inverse) | I found no peer-reviewed work that names or analyses a split between the party with authority over a decision affecting a hotel, restaurant or rental guest and the party the guest can reach, in Consensus (C1, C3, C7, C8), OpenAlex (`"accountability sink"`, 39; `"accountability sink" hotel`, 1; `algorithmic accountability hospitality guest`, top 8 of 2,157) and WebSearch, 11 Nov 2026. The one hospitality illustration is a blog (Brown 2024). Koo & Kwon 2026 and Dwivedi et al. 2026 are closed. |
| **B.** Six-question test | **(iii) Not found as a test; its parts are in print (ii).** | Lyons et al. 2021 and Alfrink et al. 2022 (four questions, carded); Wieringa 2020 (five elements); Nguyen et al. 2026 (20-question diagnostic, abstract); OSTP 2022 (opt-out without disadvantage, p. 47); AI Act art. 7(2)(g); Binesh & Syah 2026 (see, question, correct, override) | I found no work that offers an ordered set of questions for a service touchpoint combining who decided, anticipation, visibility, override, the duty to answer and the cost of refusing the automated route, in Consensus (C1, C3, C5, C6), OpenAlex and WebSearch, 11 Nov 2026. Nguyen et al.'s 20 questions are unread (CAPTCHA). |
| **C.** Timing boundary | **(ii) In print for another domain; new for hospitality.** | Canada DADM, App. B–C (human final decision at Levels III–IV, defined by reversibility); OSTP p. 50 ('before the harm occurs'); Elden 2026a §7.3; *Mathews* (carded); Baum & Laux 2026 (carded); Cohen et al. 2023, p. 2 | I found no work that ties the need for a reachable person with authority before effect to whether a hospitality decision (admission, access, room, price) can be undone in time, in Consensus (C2, C5, C7), OpenAlex and WebSearch, 11 Nov 2026. |
| **D.** Interruptible hospitality | **(ii) The term and the operator-side concept are in print** (Orseau & Armstrong 2016; Singapore Consensus 2026, p. 84; Perez 2026); **the guest-side concept with a counterparty is (iii) not found as such**; its parts are in print (OSTP fallback; Elden's apertures; Cen & Raghavan; Binesh & Syah's 'real human override at the service encounter'). | as listed | I found no use of 'interruptible hospitality', and no work that defines interruptibility as a capacity of the affected service user that requires a counterparty with authority, in WebSearch (`"interruptible hospitality"`, 18 results), OpenAlex (`interruptibility service customer`, top 8 of 156,549) and Consensus (C5, 40), 11 Nov 2026. |
| **E.** K7: oversight requires a channel to someone with power over the single case | **(ii) In print in soft law and government policy; new for hospitality.** The derivation from a holder's duty of oversight under delegation was not found (P2 scout's gap stands). | UNGP 29 and commentary (pp. 31–32); OECD MNE Guidelines 2023; UNGCP 11(f); ISO 10002 (cl. 4); Canada DADM 6.3.4, 6.4; OSTP pp. 46–50; Binns 2022 (individual justice, abstract); Bovens & Zouridis (*Einzelfallgerechtigkeit*) | I found no work that derives a duty to keep a channel from the affected person to someone with power over the single case from the duty of a party that performs through systems to oversee that performance, in a commercial-service setting, in Consensus (C1, C4, C6), OpenAlex and WebSearch, 11 Nov 2026. UNGP derives it from human-rights due diligence; the Canadian directive from monitoring and procedural fairness; OSTP from rights. |
| **F.** K9: mediation leaves the duty and removes the path | **(ii) In print for other domains; provisionally new for hospitality; open** pending Koo & Kwon. | Davies 2024; CFPB 2023; Bovens & Zouridis 2002; Kong 2026 (carded; answerability conserved); Kong & Chang 2026 (abstract); Binesh & Syah 2026 (half of it, for hotels); Koo & Kwon 2026 (abstract: responsibility 'relocated') | I found no readable work in hospitality that argues both that the host's duty persists under algorithmic mediation and that mediation removes the guest's path to anyone with authority, in Consensus (C3, C7, C8), OpenAlex (`algorithmic accountability hospitality guest`; citing-work filters) and WebSearch, 11 Nov 2026. Koo & Kwon 2026 (closed) and Dwivedi et al. 2026 (closed) may; neither was read beyond the abstract. |

---

## Part 5. Defeaters

1. **UNGP, commentary on Principle 31(h) (p. 35).** A business 'cannot, with legitimacy, both be the subject of complaints and unilaterally determine their outcome'; where adjudication is needed it should come from 'a legitimate, independent third-party mechanism'. That narrows E: a reachable officer of the host with power over the case may satisfy correction but not legitimacy. The paper should either confine E to correction during performance (K7's interruptibility) and leave adjudication to others, or answer the point.
2. **Huq 2020.** He finds no general case for a right to a human decision. Human review 'seems generally to increase net error rates' (p. 667), and appeals select by 'wealth or epistemic resources or social class' (p. 668). That counts against reading D or E as a right to a human as such. It is consistent with v6's insistence on authority rather than presence, and with C's reliance on timing (Huq too says the issue is 'the timing', p. 618).
3. **Green 2022; Crootof, Kaminski & Price 2023; Wagner 2019.** Human oversight requirements can legitimise flawed systems ('a false sense of security', Green, abstract) or produce rubber-stamping. A reachable person is not a remedy unless the institution behind the person can act. That supports v6's 'institutional' principles and narrows any interface-level reading of D.
4. **Elden 2026a.** He rejects the 'persistence assumption' that responsibility 'persists under conditions of sociotechnical complexity' (abstract), and argues that it may instead fail to arise ('does not merely become hidden but fails to arise', abstract). That contradicts F's first half for publicly attributable responsibility. The paper's reply is available: K9 concerns a role-holder's duty, not attributable responsibility for an act. But the paper must make that reply. He also holds that appeals 'are downstream' (§4.4), which presses C: for some decisions a later appeal is structurally too late.
5. **Cohen et al. 2023.** '[I]ncluding a human during the initial decision-making stage can often make decisions worse' (p. 2). That supports C's default (appeal) and counts against extending synchronous authority beyond the irreversible cases.
6. **Already carded and still live.** *Mathews* (a later hearing usually suffices); Xu & Greiffenhagen 2024 (an automated hotel kept a worker on site); Vaccaro et al. 2020 (an appeal with no change in outcome did not raise perceived accountability); Gursoy 2026 (friction as a cost).
7. **Binns 2022 (abstract).** Uneven human judgment produces 'inequities in individual justice'. That narrows E's 'single case' power: discretion in the single case can itself be unfair.

## Part 6. Gaps (summary)

The gap statements sit in the Q7 table. In short:
- the hospitality application of A, C and E is unwritten in what I could read;
- the six-question test is new as an instrument;
- 'interruptible hospitality' and a guest-held interruptibility with a counterparty are new as terms;
- the derivation of E from a holder's duty of oversight is not in print (consistent with the P2 scout).

The decisive closed items:
- **Davies 2024**: the book itself, p. 17 and the chapter around it. The authors need a library copy before v7 coins 'authority–answerability split' without crediting 'accountability sink'.
- **Koo & Kwon 2026**: full text, for F in hospitality.
- **ISO 10002 cl. 5.4**, 'Responsibility and authority', for E.

## Files saved by this scout

New folders under `manuscript/revision_2026-11/research/sources/`:
- `tbscanada2019directive/` (directive HTML and text, fetched 11 Nov 2026)
- `iso2018complaints/` (official sample, cl. 0–4)
- `brown2024accountability/` (blog page quoting Davies)
- `bovens2002street/p5_fulltext.*` (Utrecht author manuscript)
- `wieringa2020what/` (Utrecht repository copy)
- `perez2026law/` (arXiv v2)
- `herrmann2025intervenability/` (arXiv preprint)
- `casper2026singapore/` (arXiv)

Added to existing folders:
- `huq2020right/p5_fulltext_106VaLRev611.*` (the correct Huq article)
- `ostp2022blueprint/official_refetch_2026-11-11.pdf` (hash check)

I wrote no cards and edited no other file.

*Written by a Claude (Opus 5.5) subagent, scout for P5, from the records and saved texts named above, on 11 Nov 2026, run rr-2026-11-k.*

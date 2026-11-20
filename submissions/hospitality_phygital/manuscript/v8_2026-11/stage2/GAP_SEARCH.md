<!-- DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026, as a v8 Stage 2 literature scout. Every work listed came from a search result seen on 13 Nov 2026. Quotations are verbatim and kept short; each carries a printed page where the version read had one, or a section locator where it did not (HTML full text). Suggested wording for the manuscript is marked "Suggested (Claude)". Nothing here edits references.bib, a card or a manuscript file. Uncommitted. -->

# Gap search: who owes phygital safeguards, and which firm?

## The claim tested

The manuscript ("Who Hosts the Guest?", *Hospitality & Society* SI on phygital hospitality) wants to say:

> Phygital research prescribes safeguards for trust, fairness and well-being, but says neither to whom they are owed nor which of several firms owes them.

A work counts against the claim if it does any of three things: (T1) says to whom phygital, hybrid, AI, robot or self-service safeguards in hospitality and tourism are owed; (T2) says which of several firms (hotel, platform, technology vendor, channel manager, management company, brand) owes them; (T3) allocates responsibility or accountability across the firms behind a hospitality touchpoint. I also tracked (T4), work that prescribes a timely route by which a failure in the guest's case reaches someone able to correct it, because the manuscript's third duty claims that ground.

**Verdict.** Phygital research proper does not answer T1–T3; it prescribes safeguards and addresses them to "hotels" or "managers". Hospitality AI-governance work published in 2026 does take up T2–T4, so the claim as worded is too broad. Section 3 gives the final statement and what to cite or narrow.

## 1. Search log

All searches ran on 13 Nov 2026. "Hits" is what the source reported; "Screened in" counts the records I took past the title to abstract or full text (known and held works are counted). OpenAlex `title_and_abstract.search` takes boolean syntax; Crossref ranks by relevance, so I screened its top 40.

**Source availability.** Consensus failed on every call: five `search` calls (connection reset, timeout, internal server error) and one `get_full_text` call (timeout). Scholar Gateway failed on all five `semanticSearch` calls (timeouts, internal server error). I therefore have **no Consensus or Scholar Gateway results to report**. I ran the search on OpenAlex, Crossref, Semantic Scholar (abstract lookups), web search, and the publishers' or repositories' open-access full text.

### 1a. Failed sources

| Source | Query | Date | Hits | Screened in |
|---|---|---|---|---|
| Consensus `search` (×2) | phygital hospitality responsibility accountability | 13 Nov 2026 | failed (reset/timeout) | 0 |
| Consensus `search` | who is responsible when a hotel service robot or AI fails: responsibility attribution among hotel, platform and technology provider | 13 Nov 2026 | failed (timeout) | 0 |
| Consensus `search` | accountability allocation among multiple actors in AI-enabled service ecosystems | 13 Nov 2026 | failed (500) | 0 |
| Consensus `search` | responsibility allocation among hotel, platform and technology vendor for AI service failures affecting guests | 13 Nov 2026 | failed (500) | 0 |
| Consensus `search` | accountability allocation among multiple firms in AI-enabled hospitality service ecosystems | 13 Nov 2026 | failed (timeout) | 0 |
| Consensus `get_full_text` | DOIs of Suh 2026, Wirtz 2023, Parhi 2026 | 13 Nov 2026 | failed (timeout) | 0 |
| Scholar Gateway (×3) | Who is responsible or accountable for guest safeguards when hotel service is delivered through combined physical and digital (phygital) touchpoints run by several firms? (2018–) | 13 Nov 2026 | failed (timeout/500) | 0 |
| Scholar Gateway | How is responsibility or accountability for AI, robot or self-service technology failures allocated among the hotel, the booking platform and the technology vendor in hospitality? (2018–) | 13 Nov 2026 | failed (timeout) | 0 |
| Scholar Gateway | Which party owes duties to hotel guests when hosting tasks such as pricing, check-in and messaging are delegated to algorithmic systems supplied by several firms? (2018–) | 13 Nov 2026 | failed (timeout) | 0 |

### 1b. OpenAlex (api.openalex.org/works, generic User-Agent)

| Source | Query | Date | Hits | Screened in |
|---|---|---|---|---|
| OpenAlex `search` (full text) | phygital responsibility; + accountability, liability, governance, hospitality, obligation, redress, complaint (8 queries, 2018–) | 13 Nov 2026 | 1,771 for the first; matching ran on full text | 0 (superseded by title/abstract runs) |
| OpenAlex title/abstract | phygital responsibility (2018–) | 13 Nov 2026 | 29 | 3 (Gombar 2026; Lim et al. 2026 SIJ; Swaminathan 2026, no abstract) |
| OpenAlex title/abstract | phygital accountability | 13 Nov 2026 | 9 | 0 new |
| OpenAlex title/abstract | phygital liability | 13 Nov 2026 | 0 | 0 |
| OpenAlex title/abstract | phygital governance | 13 Nov 2026 | 80 | 7 (Gustafsson 2026; Batat 2026 PSR editorial; Duy 2026; Tonin 2026; Pesce 2026; known: Batat 2026 HFPV, Shabnam 2026) |
| OpenAlex title/abstract | phygital obligation / redress / complaint / recourse / duty | 13 Nov 2026 | 1 / 3 / 2 / 1 / 1 | 0 |
| OpenAlex title/abstract | phygital human-in-the-loop | 13 Nov 2026 | 7 | 0 new |
| OpenAlex title/abstract | phygital escalation | 13 Nov 2026 | 9 | 1 (Suh et al. 2026) |
| OpenAlex title/abstract | phygital hospitality | 13 Nov 2026 | 19 | 3 (Suh 2026; Hanni-Vaara 2024; known: Mameli 2026) |
| OpenAlex title/abstract | phygital ethics | 13 Nov 2026 | 21 | 1 (Shwartz Altshuler et al. 2025) |
| OpenAlex title/abstract | phygital trust fairness | 13 Nov 2026 | 6 | 0 new |
| OpenAlex title/abstract | phygital well-being | 13 Nov 2026 | 101 | 4 (Anderson et al. 2026; Erdoğan 2026; Berthon, DesAutels et al. 2026; held: Brochado 2026) |
| OpenAlex title/abstract | (hotel OR hospitality) AND (robot OR "artificial intelligence" OR chatbot) AND (responsibility OR accountability OR liability) AND (allocation OR attribution OR "who is") (2020–) | 13 Nov 2026 | 23 | 3 (Liu & Wang 2025; Almeida 2026; held: Belanche 2020) |
| OpenAlex title/abstract | (hotel OR hospitality OR tourism) AND "responsibility attribution" AND (robot OR AI OR "self-service") | 13 Nov 2026 | 3 | 0 new |
| OpenAlex title/abstract | (hotel OR hospitality) AND chatbot AND liability | 13 Nov 2026 | 3 | 0 |
| OpenAlex title/abstract | "self check-in" AND (failure OR responsibility) | 13 Nov 2026 | 6 | 1 (Yang et al. 2025) |
| OpenAlex title/abstract | "smart hotel" AND (rights OR privacy OR responsibility) | 13 Nov 2026 | 43 | 3 (Kumar et al. 2026; Garcia 2024; Gajić et al. 2026) |
| OpenAlex title/abstract | (hospitality OR tourism) AND "responsible AI" AND governance | 13 Nov 2026 | 51 | 5 (Parhi 2026; Kunz & Wirtz 2026; Ma & Jiao 2026; Pokkakillath 2026; Whitford 2026) |
| OpenAlex title/abstract | (hospitality OR hotel) AND (vendor OR "technology provider" OR "third-party") AND (liability OR accountability OR responsibility) AND (AI OR algorithm OR software) | 13 Nov 2026 | 16 | 1 (Dwivedi et al. 2026) |
| OpenAlex title/abstract | (platform OR Airbnb OR "online travel agency" OR OTA) AND (host OR hotel OR provider) AND (blame OR "responsibility attribution") AND "service failure" (2018–) | 13 Nov 2026 | 2 | 2 (Kittur et al. 2025; Castillo et al. 2022, no abstract) |
| OpenAlex title/abstract | (Airbnb OR "peer-to-peer accommodation" OR "short-term rental") AND (liability OR "duty of care") AND (platform OR host) AND (guest OR safety) | 13 Nov 2026 | 12 | 0 |
| OpenAlex title/abstract | "service ecosystem" AND (accountability OR responsibility) AND ("artificial intelligence" OR algorithmic OR AI) AND (actors OR multi-actor) | 13 Nov 2026 | 6 | 1 (Sposato et al. 2026) |
| OpenAlex title/abstract | "distributed responsibility" AND (service OR hospitality OR tourism) AND (AI OR algorithm OR automation) | 13 Nov 2026 | 29 | 2 (Hanslik 2026; held: Cobbe et al. 2023) |
| OpenAlex title/abstract | (hotel OR hospitality) AND ("human-in-the-loop" OR "human handoff" OR "human escalation" OR "escalation to human") AND (chatbot OR AI OR robot) | 13 Nov 2026 | 31 | 4 (Ariyogi et al. 2026; Kuraa 2026; Aransyah et al. 2026; held: Ivanov & Webster 2023) |
| OpenAlex title/abstract | (hotel OR hospitality) AND ("algorithmic pricing" OR "dynamic pricing" OR "revenue management") AND (fairness OR responsibility OR accountability) AND (algorithm OR AI) | 13 Nov 2026 | 38 | 2 (van der Rest et al. 2022; Tyagi & Tyagi 2026, no abstract) |
| OpenAlex title/abstract | (hospitality OR hotel OR tourism) AND "duty of care" AND (digital OR technology OR AI OR algorithm) | 13 Nov 2026 | 11 | 0 |
| OpenAlex title/abstract | "corporate digital responsibility" AND ("service ecosystem" OR ecosystem OR "multi-actor") (2019–) | 13 Nov 2026 | 35 | 3 (Wirtz et al. 2023; Samadi et al. 2026; Kunz & Wirtz 2023) |
| OpenAlex title/abstract | "corporate digital responsibility" AND (hospitality OR tourism OR hotel) | 13 Nov 2026 | 35 | 2 (Yu & Wang 2025; Lee et al. 2025 editorial, no abstract) |
| OpenAlex title/abstract | (hospitality OR hotel OR tourism) AND (accountability OR responsibility) AND ("multiple actors" OR "multi-actor" OR "many hands" OR "several firms" OR ecosystem) AND (AI OR algorithm OR automation OR digital) | 13 Nov 2026 | 218 (top 50 screened) | 2 (Su et al. 2026; Mota et al. 2026, no abstract) |
| OpenAlex title/abstract | (hotel OR hospitality OR guest) AND (complaint OR redress OR recourse OR grievance) AND (algorithm OR AI OR chatbot OR automated) AND (responsibility OR accountability) | 13 Nov 2026 | 20 | 0 |
| OpenAlex title/abstract | (Airbnb OR "home sharing" OR "short-term rental" OR "peer-to-peer accommodation") AND ("platform liability" OR "intermediary liability" OR "liability of platforms" OR "consumer protection") AND (host OR guest) (2017–) | 13 Nov 2026 | 7 | 1 (Tran 2025) |
| OpenAlex title/abstract | (hotel OR hospitality) AND ("management company" OR franchisor OR franchise OR "brand standards") AND (technology OR AI OR data OR cyber) AND (liability OR accountability OR responsibility) | 13 Nov 2026 | 25 | 0 |
| OpenAlex title/abstract | ("unmanned hotel" OR "contactless hotel" OR "hostless" OR "staffless hotel" OR "autonomous hotel") AND (responsibility OR accountability OR failure OR recovery) (2019–) | 13 Nov 2026 | 13 (mostly battery chemistry) | 0 |
| OpenAlex, journal-restricted by ISSN (2020–) | (responsibility OR accountability OR liability OR obligation OR duty OR redress OR governance) AND ("artificial intelligence" OR AI OR robot OR robots OR algorithm OR algorithmic OR chatbot OR "self-service" OR phygital OR automation OR automated) | 13 Nov 2026 | *Hospitality & Society* 2; IJHM 9; IJCHM 12; *Tourism Management* 9; *Annals of Tourism Research* 4; JSR 9; *J. Services Marketing* 8; JOSM 15; *J. Strategic Marketing* 3 | 13 (known: Germann Molz 2026; von Richthofen & Culiberg 2025; Lee et al. 2026 IJCHM; Lim 2026 *Annals*, no abstract; Manoli 2026; Yoganathan et al. 2025; Lahiri & Dastidar 2026; Lee, Bart & Cauffman 2025; Tiron-Tudor & Deliu 2025; Breidbach & Maglio 2020; Lee et al. 2026 IJHM, no abstract; Huang et al. 2025 TM, no abstract; Wirtz 2023 again) |
| OpenAlex, *Hospitality & Society* only | (algorithm OR algorithmic OR digital OR platform OR technology OR robot OR AI) AND (host OR hosting OR obligation OR responsibility OR ethics OR duty) (2020–) | 13 Nov 2026 | 5 | 2 (known: Germann Molz 2026; held: Paloniemi 2024) |
| OpenAlex DOI lookups | abstracts and open-access locations for every screened-in record | 13 Nov 2026 | — | — |

### 1c. Crossref, Semantic Scholar, web

| Source | Query | Date | Hits | Screened in |
|---|---|---|---|---|
| Crossref `query.bibliographic` (2020–) | phygital responsibility accountability governance | 13 Nov 2026 | 291,971 (top 40) | 0 |
| Crossref | phygital hospitality safeguards | 13 Nov 2026 | 48,572 (top 40) | 2 (Lim 2025 *J. Strategic Marketing*; Nosi 2025, no abstract) |
| Crossref | hotel artificial intelligence responsibility allocation vendor platform | 13 Nov 2026 | 1,183,128 (top 40) | 1 (Pantano & Scarpi 2025, no abstract) |
| Crossref | service robot hotel failure who is accountable | 13 Nov 2026 | 800,294 (top 40) | 2 (Ryoo et al. 2024, no abstract; Ho et al. 2020) |
| Crossref + OpenAlex | chapter list of Vatankhah, Duan & Rahimi (eds), *The Ethics of AI in Hospitality and Tourism*, Routledge 2026 (10.4324/9781003643951) | 13 Nov 2026 | 11 records | 3 (Kunz & Wirtz; Ma & Jiao; Balawardhana & Stoica) |
| Semantic Scholar API | abstract lookups: Ryoo 2024; Ho 2020; Lee 2026 IJHM; Huang 2025 TM | 13 Nov 2026 | 4 | 1 abstract found (Ho 2020) |
| Web search | phygital hospitality accountability responsibility "who is responsible" AI hotel journal article | 13 Nov 2026 | 10 | 2 (Balawardhana & Stoica 2026; Zencirli, Hospitality Net, grey) |
| Web search | hotel technology vendor liability guest harm AI system property management channel manager responsibility academic paper | 13 Nov 2026 | 10 | 0 scholarly (trade and law-firm pages only) |
| Web search | "phygital" service ecosystem governance accountability multi-actor responsibility 2026 Journal of Services Marketing | 13 Nov 2026 | 10 | 1 (Samadi et al. 2026) |
| Web search | law review Airbnb platform liability host guest injury safety allocation of responsibility short-term rental duty of care | 13 Nov 2026 | 10 | 0 scholarly (practitioner pages only) |
| Web search | "phygital" hospitality guest "duty" OR "obligations" OR "owed" safeguards hotel platform vendor scholarly | 13 Nov 2026 | 10 | 0 new |
| Web search | hotel self check-in kiosk smart lock failure guest locked out who is responsible operator software provider research article tourism | 13 Nov 2026 | 10 | 0 scholarly |
| Web search (verification) | Ryoo et al. 2024 title; Lee et al. 2026 IJHM title | 13 Nov 2026 | 10 + 10 | abstracts not found |
| WebFetch | Bedfordshire research portal (Balawardhana & Stoica); hospitalitynet.org/news/4135116 (Zencirli) | 13 Nov 2026 | 2 pages | 2 |
| WebFetch, blocked | Sage, Taylor & Francis, Emerald full-text pages; SSRN 7563639; centaur.reading.ac.uk | 13 Nov 2026 | 403/404 or bot check | read instead in the browser where open access (see 2) |

## 2. Candidates and verdicts

**Read depth.** *Full* means I read the whole text. *Targeted full text* means I read the open-access version of record and located the relevant passages by searching its whole text for responsibility, accountability, liability, vendor, platform, escalation, redress and owner, then read those passages in context. *Abstract only* means only the abstract was reachable, and the verdict rests on the abstract alone. No verdict rests on a title.

**Bib status** uses `grep -i` on `literature/references.bib` (13 Nov 2026).

### 2a. Works that do part of it (PARTLY), closest first

**1. Parhi, A. (2026). AI governance and digital transformation in hospitality firms: a PRISMA-based systematic review and bibliometric analysis. *Cogent Social Sciences*, 12(1), 2742601.** https://doi.org/10.1080/23311886.2026.2742601 — Open access. Read depth: targeted full text (T&F HTML, no pagination; §§6.3.2, 6.6 and the ADAPT-H overview read in context). Not in bib.
**Verdict: PARTLY. T3 yes; T4 partly; T1 and T2 no.** Parhi names the multi-firm problem outright and allocates governance across the firms, but as a shared, contractual obligation, not a duty bound to one party.
- §6.6: franchise and management-contract models "diffuses accountability for AI governance across at least three parties", namely "the brand owner (franchisor), the property operator (franchisee), and the technology vendor (third party)".
- §6.6: "None of these parties individually possesses the authority, information, or incentives".
- §6.3.2 (Ecosystem and Vendor Governance pillar): "treat AI governance as a shared obligation embedded contractually across the franchise and vendor network".
- §6.3.2: a brand-wide incident protocol "requiring franchisees and vendors to disclose algorithmic harms within a defined window".

What it does not do: it never says the obligation is owed to the guest. It spreads the obligation across all three parties rather than binding it to one, and it offers no ground such as holding out, reliance or control. Caution: Parhi supports the claim that franchise templates lack multi-party AI clauses by citing Arif et al. (2026, *iScience* 29(3), 115134, https://doi.org/10.1016/j.isci.2026.115134). That abstract covers ethics training and governance maturity, not franchise agreements (abstract only). Cite Parhi for the paradox, not for the empirical gap.

**2. Ariyogi, D., Mulyawan, U., & Junita, M. (2026). From AI disclosure to human handoff: Transparency, trust, and accountability in automated hospitality services—A structured evidence review. *Global Review of Tourism and Social Sciences*, 3(1), 77–90.** https://doi.org/10.53893/grtss.v3i1.550 — CC BY 4.0. Read depth: **full** (publisher PDF, printed pages). Not in bib.
**Verdict: PARTLY. T2 partly (one bearer named); T4 yes; T3 no.** It names one bearer among several firms, the branded organisation the guest deals with, and it prescribes the route-to-correction feature that the manuscript's third duty claims.
- p. 77: "accountability requires a service organization capable of answering for what happens next".
- p. 78: "The guest evaluates the branded service organization through its interfaces and staff, even when technical components are supplied elsewhere."
- p. 79: "The present framework therefore assigns recovery ownership at organizational level"; also "Psychological blame is not a legal determination."
- p. 82: "An effective response must connect the failure explanation to an identifiable service obligation."
- p. 85 (P4): "identifiable organizational recovery ownership will improve responsibility clarity and recovery evaluation".
- p. 86: "Managers should also identify who can authorize corrective action." Also "Responsibility for system limitations should remain traceable within the organization", and "a modest and dependable escalation pathway may be more feasible".

What it does not do: it grounds recovery ownership in the guest's evaluation of the brand and in recovery effectiveness, not in a role, holding out, reliance or control of space. It does not resolve brand versus operator versus vendor. Its authors call it an "access-limited synthesis" without independent screening (abstract, p. 77). It cites Sharma & Mattila (2026), which the project holds as `sharmamattila2025rights`.

**3. Kuraa, R. (2026). AI- and robot-mediated traveler well-being infrastructure: A conceptual framework for tourism and hospitality journeys. SocArXiv preprint, May 2026.** https://doi.org/10.31235/osf.io/6mztq_v1 — **Preprint, not peer-reviewed**; the PDF file name says it targets *Tourism Review*. Read depth: targeted full text (OSF PDF, 57 pp.). Not in bib.
**Verdict: PARTLY. T1 yes; T2 partly; T4 yes; T3 no.**
- p. 6: the framework "places responsibility on the tourism and hospitality brand, not on the AI tool alone".
- p. 29: travellers "experience it as the responsibility of the brand that deployed the model".
- p. 30: "Travelers need a clear route to challenge AI-mediated decisions, request explanations and receive corrective action."
- pp. 30–31: governance should "specify who owns AI-mediated outcomes, who can override automated decisions".

What it does not do: it grounds the brand's responsibility in traveller perception. It lists "A hotel, airline, platform or destination organization" (p. 30) without choosing among them when several stand behind one touchpoint. Cite it only if the authors accept preprints.

**4. Suh, T., Nasta, L., Pirolo, L., & Magnanelli, B. S. (2026). Phygital customer experience and the adoption of immersive technologies in hospitality: an exploratory study with a value co-creation perspective. *Journal of Services Marketing*, online first, pp. 1–18.** https://doi.org/10.1108/JSM-07-2025-0445 — Open access. Read depth: targeted full text (Emerald HTML, no pagination; §2.3 and §6 read in context). Not in bib (the bib holds a different Suh 2026, `suh2026conceptualizing`).
**Verdict: PARTLY on the claim's first half. It names guests as the protected party and hotels as the implementers, but does not argue why the safeguards are owed or address several firms.** It is the closest phygital-hospitality work and the one a reviewer will check first.
- §2.3: "A seventh principle, ethical safeguards, is necessary to preserve the human-centric orientation of PH-CX."
- §2.3: equity and privacy safeguards are stated for guests ("guest control over the deletion of sensitive or biometric information").
- §6 (implementation roadmap): "Hotels should collect only data required for a clearly specified service purpose"; "AI concierge systems should provide a visible route to human assistance and establish escalation procedures".
- §6: "Policymakers have a role to play in promoting inclusive infrastructure".

Implication: the manuscript's phrase "says neither to whom they are owed" does not survive Suh literally, because Suh names guests and hotels. What Suh lacks is a ground ("why owed") and any treatment of platform, vendor or brand. Page numbers need the PDF; the HTML had none.

**5. Wirtz, J., Kunz, W. H., Hartley, N., & Tarbit, J. (2023). Corporate digital responsibility in service firms and their ecosystems. *Journal of Service Research*, 26(2), 173–190.** https://doi.org/10.1177/10946705221130467 — Open access. Read depth: targeted full text (Sage HTML, no pagination; first half read in full, Table 2 rows read). **Not in bib** (no CDR entry at all is in the bib).
**Verdict: PARTLY. T2 and T3 in general service, not hospitality.** Wirtz et al. make the focal service firm the orchestrator and governor of CDR across its vendors and partners.
- "Origins of CDR Issues": "in addition to the focal service firm often several other players are involved".
- "The Nature of Digital Service Ecosystems": "the service firm in the center ... governing the ecosystem of customers, complementors, and external business partners".
- "Complementing Partners": "CDR risks need to be discussed between service firms and these partners."
- "service firms have effectively become private regulators of their ecosystems".
- Table 2: "Transparent shared policies on CDR responsibilities need to be disseminated across the ecosystem"; "Formalize compensation to affected consumers when ethics, privacy, or fairness violations occur".

It uses hotel biometrics as an example ("providing guests access to hotel facilities using biometrics"). The paper rests the focal firm's position on orchestration and power, not on holding out or control of a space.

**6. Samadi, S., Ahmed, T., McCullough, A. E., Durán-López, E., Tóth, Z., & Heirati, N. (2026). Digitalization strategy in service ecosystems: managing the interplay of tensions and empowerment. *Journal of Service Management*, 37(6), 50–77.** https://doi.org/10.1108/JOSM-03-2025-0151 — Open access. Read depth: targeted full text (Emerald HTML). Not in bib.
**Verdict: PARTLY. T3 in general service.**
- Introduction: "responsible digitalization is not enacted by a single firm".
- CDR discussion: "inconsistencies in transparency and digital literacy across an ecosystem can engender ambiguous accountability".
- Discussion: "Hub firms can address potential tensions" through data governance.

It names the hub firm as orchestrator, not as the bearer of duties owed to customers.

**7. Dwivedi, Y. K., Helal, M. Y. I., Mansour, N. M., Abdulkareem, Z. O., Raman, R., & Elshawarbi, N. N. (2026). A critical reflection on corporate digital responsibility in tourism and hospitality: stakeholder value implications in artificial intelligence intensive service ecosystems. *Journal of Hospitality and Tourism Insights*, online first, pp. 1–19.** https://doi.org/10.1108/JHTI-03-2026-0339 — **Abstract only** (paywalled; the Emerald page shows "Purchase"). Not in bib.
**Verdict on the abstract: PARTLY. T3 framing; duty vocabulary.** The abstract organises CDR around "the service-ecosystem structure that links firms to platforms, vendors, and partners". It defines CDR as "auditable duties of care for the design, deployment, and governance of digital and AI systems", and recommends "improving third-party oversight". The abstract does not say which firm owes the duties. This is the most likely place for a reviewer to find duty-of-care language applied to the multi-firm hospitality ecosystem. **Read the full text before submission** (abstract-only debt).

**8. Shwartz Altshuler, T., Aridor-Hershkovitz, R., Mikulinsky, R., & Müller, B. (2025). Governing phygital spaces: Human rights by design meets speculative design. *Internet Policy Review*, 14(4).** https://doi.org/10.14763/2025.4.2048 — Open access. Read depth: targeted full text (PDF, printed pages). Not in bib.
**Verdict: PARTLY, outside hospitality.** It is the one *phygital*-labelled work that names governing parties. On smart glasses and AR it states: "Phygital spaces operate under two overlapping governance systems" (p. 19). One system is the authorities managing physical spaces, building owners among them; the other is "the digital platforms that control the augmented layers of these spaces" (p. 19). It also argues for "broadening developer responsibilities" (p. 11). The work concerns regulation and governance, not safeguards a firm owes a guest.

**9. Sposato, M., Dittmar, E. C., & Vargas Portillo, J. P. (2026). Navigating the dark side of AI in service ecosystems: an ethical leadership framework for risk mitigation. *The Service Industries Journal*, online first, pp. 1–31.** https://doi.org/10.1080/02642069.2026.2643384 — **Abstract only** (a repository copy exists at hdl.handle.net/10115/363637 but returned only a JavaScript shell). Not in bib.
**Verdict on the abstract: PARTLY, general service.** The authors specify "multi-actor governance structures for service ecosystems where no single actor controls ethical outcomes" and argue for "polycentric governance". There is no hospitality case and no bearer is named.

**10. Kittur, P. V., Goswami, R., & Chatterjee, S. (2025). Service recovery strategy in platform economy. *European Journal of Marketing*, 60(1), 297–335.** https://doi.org/10.1108/EJM-05-2024-0426 — **Abstract only.** Not in bib.
**Verdict on the abstract: PARTLY, descriptive.** It studies aggregator (platform) recovery when the "actual service provider" caused the failure, and claims to advance "triadic responsibility attribution". This is customer perception, not who owes what; the abstract names no hospitality setting.

**11. Tran, T. N. (2025). Civil liability in Airbnb transactions and the legal gaps in consumer protection in Vietnam. *International Journal on Consumer Law and Practice*.** https://doi.org/10.55496/rwiq1433 — **Abstract only.** Not in bib.
**Verdict on the abstract: PARTLY, legal scholarship.** It addresses "complex legal issues concerning the allocation of civil liability" between the Airbnb platform and hosts. This shows that legal writing, outside phygital research, already allocates liability between platform and host.

**12. Cobbe, J., Veale, M., & Singh, J. (2023). Understanding accountability in algorithmic supply chains. FAccT '23.** https://doi.org/10.1145/3593013.3594073 — **Held** (`cobbe2023understanding`); not re-read. Its abstract names "challenges for allocating accountability stemming from distributed responsibility for systems between actors" (general AI, not hospitality). Hanslik (2026, AIES doctoral abstract, https://doi.org/10.1609/aies.v9i4.43370, abstract only, not in bib) extends the same point: "no single actor has full control over or visibility into the resulting system".

**Grey literature (not peer-reviewed).** Zencirli, B. T., "When the Hotel's AI Acts, Who Is Accountable? Building a Hospitality Agent Governance Architecture", *Hospitality Net* opinion, 27 October (year not shown on page), https://www.hospitalitynet.org/news/4135116. It lists owner, management company, brand, technology vendor and oversight manager as candidates without choosing among them. It argues responsibility "should be allocated before deployment rather than litigated after an incident". Practice has posed the multi-firm question, but this is not research.

### 2b. Near neighbours that pose the question but do not answer it (NO; worth citing as support)

| Work | Read depth | Verdict and evidence | Bib |
|---|---|---|---|
| Lim, W. M., Chuah, C., Koay, K. Y., Ma, L., Soon, P.-S., & Luo, X. (2026). Phygital research fit. *Service Industries Journal*, online first, pp. 1–30. https://doi.org/10.1080/02642069.2026.2749471 | Targeted full text (T&F HTML) | **NO**: poses the question as an agenda item, "responsible phygital governance, which asks who controls and can contest digital decisions" (section on transformative and sustainable lenses). Supports the gap. | not in bib |
| Batat, W. (2026). Advancing phygital service research (PSR): key streams and future research directions. *J. Services Marketing*, online first. https://doi.org/10.1108/JSM-09-2026-1070 | Abstract only | **NO**: lists "expanding analytical scope to multiactor and ecosystem governance" as a *future* trajectory. The SI editor's own editorial names the gap. Different from the held `batat2026psr` (JSM-09-2025-0600). | not in bib |
| Gustafsson, A. (2026). Unmanned, not unmanaged. *J. Services Marketing*, online first, pp. 1–17. https://doi.org/10.1108/JSM-09-2025-0693 | Targeted full text (Emerald HTML) | **NO on T1–T3; YES on T4 (retail)**: prescribes "One-tap escalation" and holds that escalation SLAs "are critical". Its "responsibility for shared space can diffuse" concerns customers as stewards, not firms. | not in bib |
| Anderson, K. C., Hass, A., Wallach, K. A., Mertz, B. A., Shamayleh, G., & Laverie, D. A. (2026). The phygital well-being paradox in the service ecosystem. *J. Services Marketing*. https://doi.org/10.1108/JSM-04-2026-0342 | Abstract only | **NO**: "balance benefits and burdens across stakeholders"; no bearer. | not in bib |
| Almeida, S. (2026). AI as a mediating quasi-stakeholder: rethinking coopetition in hotel marketing consortia. *Current Issues in Tourism*, 1–8. https://doi.org/10.1080/13683500.2026.2747409 | Abstract only | **NO**: multi-hotel and AI governance among consortium members; accountability is listed as a principle, with no guest-facing allocation. | not in bib |
| Belanche, D., Casaló, L. V., Flavián, C., & Schepers, J. (2020). *JOSM*. https://doi.org/10.1108/JOSM-05-2019-0156 | Held; abstract re-seen | **NO (descriptive)**: "Customers thus attribute responsibility to the firm rather than the frontline robot." Firm versus robot, not firm versus firm. | `belanche2020` |
| Leo, X., & Huh, Y. E. (2020). Who gets the blame for service failures? *Computers in Human Behavior*. https://doi.org/10.1016/j.chb.2020.106520 | Abstract via search snippet only | **NO (descriptive)**: people assign more responsibility to the firm when a robot fails. Ariyogi et al. lean on it. | not in bib |

### 2c. Screened, verdict NO (abstract unless marked)

| Work (DOI) | Why NO |
|---|---|
| Shabnam et al. 2026, TPSR, JSM (10.1108/JSM-09-2025-0679) | **Known**, not re-read; the abstract names "ambiguities ... around agency, governance" but allocates nothing. |
| Berthon, DesAutels, Rabinovich & Weinberg 2026, 4E cognitive ecology, JSM (10.1108/JSM-06-2026-0516) | Cognition and design; no bearer. Not the held `berthon2026accesship`. |
| Erdoğan 2026, JSM (10.1108/JSM-11-2025-0826) | Well-being design framework; no bearer. |
| Brochado et al. 2026, JSM (10.1108/JSM-09-2025-0709) | Held; review; no bearer. |
| Hanni-Vaara et al. 2024, DRS (10.21606/drs.2024.1345) | Museum or heritage touchpoint design. |
| Gombar, Boban & Pejić Bach 2026, *World* (10.3390/world7050086) | Users' "algorithmic responsibility perception" of platforms (survey construct). |
| Lim 2025, *J. Strategic Marketing* (10.1080/0965254X.2025.2595087) | Bright and dark sides of GenAI for PH-CX; no bearer. |
| Pesce et al. 2026, JHTM (10.1016/j.jhtm.2026.101470) | Trade-fair platformisation; "multi-stakeholder orchestration" of business governance, not guest safeguards. |
| Duy 2026, OSF (10.17605/osf.io/y7f5b); Tonin et al. 2026, IntechOpen (10.5772/intechopen.1015457) | Autonomy and override as design mechanisms; retail accessibility checklist. |
| Kunz & Wirtz 2026, Routledge chapter (10.4324/9781003643951-4); Kunz & Wirtz 2023, JRIM (10.1108/JRIM-06-2023-0176) | CDR addressed to the T&H firm; "equitable power dynamic between service firms and their partners" (2023), with no allocation. |
| Ma & Jiao 2026, Routledge chapter (10.4324/9781003643951-5) | Lists governance models ("multi-stakeholder frameworks"); no bearer. |
| Balawardhana & Stoica 2026, Routledge chapter (10.4324/9781003643951-6) | Repository summary only (not verbatim): the E3R framework includes "Responsibility Mapping", undescribed. **Undetermined**; read if the authors want certainty. |
| Pokkakillath 2026, RHM (10.1080/22243534.2026.2726013) | Adoption maturity and governance; no allocation. |
| Whitford 2026, FIU (10.25148/fiuir.32844) | Employee trust in AI surveillance. |
| Kumar et al. 2026, Emerald chapter (10.1108/978-1-83608-602-420261011) | Smart-hotel privacy law and ethics; no allocation. |
| Garcia 2024, Zenodo (10.5281/zenodo.17729265) | Not peer-reviewed; interdependent smart-hotel systems; no allocation. |
| Gajić et al. 2026, *Technologies* (10.3390/technologies14090548) | Benefit–risk survey. |
| Liu & Wang 2025, *Tourism Review* (10.1108/TR-11-2024-0998); Yang et al. 2025, CIT (10.1080/13683500.2025.2550645); Ho et al. 2020, IJHM (10.1016/j.ijhm.2020.102501) | Customer attribution or failure classification; no firm allocation. |
| van der Rest et al. 2022, JHTI 5(4) 771–781 (10.1108/JHTI-08-2021-0216) | Calls for research on algorithmic-pricing ethics and CSR. |
| Aransyah et al. 2026, Cogent B&M (10.1080/23311975.2026.2613599) | Review; "hybrid human handoff" as a design lever. |
| Yu & Wang 2025, CIT (10.1080/13683500.2025.2571437); Yoganathan et al. 2025, JSR (10.1177/10946705251345097) | Customer responses to CDR; firm versus government regulation (state, not firms). |
| von Richthofen & Culiberg 2025, IJCHM 37(11) 3708–3728 (10.1108/IJCHM-12-2024-1883) | Targeted full text: "Another area that platforms are accountable for is equality" ("Equality" subsection). Platform-only accountability; no platform–host split. |
| Lee, Bart & Cauffman 2025, JSM (10.1108/JSM-03-2025-0179); Breidbach & Maglio 2020, JOSM (10.1108/JOSM-03-2019-0073); Tiron-Tudor & Deliu 2025, JOSM (10.1108/JOSM-04-2024-0205) | Vulnerability, value-network ethics, CDR decision framework; no bearer. |
| Su, Liao & So 2026, *Sustainability* (10.3390/su18115562); Manoli 2026, *Annals* (10.1016/j.annals.2026.104151); Lee et al. 2026, IJCHM (10.1108/IJCHM-01-2026-0006); Lahiri & Dastidar 2026, JSR (10.1177/10946705261481651); Webster & Cain 2024, JHTR (10.1177/10963480241229233) | Destination trust, platform power, DT 2.0, frontline AI compliance, regulation and competitiveness. |

### 2d. Known or held, recorded and not re-read

Batat 2024 (PH-CX); Batat 2024 QMR editorial; Batat 2026 HFPV (seen in results, 10.1177/02761467261450501); Batat 2026 PHIVE; Batat & Hammedi 2023; Shabnam 2026 (seen); Mameli 2026 (seen, 10.1007/s40558-026-00362-6); Zheng 2025; Gursoy 2026; Mosca 2025 and 2026; Liu 2026; Sharma & Mattila 2025/2026 (cited inside Ariyogi et al.); Germann Molz 2018 and 2026 (*Guests without hosts*, seen, 10.1386/hosp_00107_1); Riordan 2024; Weaver 2026; Gao et al. 2026; Binesh & Syah 2026; Berthon et al. 2026 (accesship). Also held, beyond the brief's list: Belanche et al. 2020; Cobbe et al. 2023; Ivanov & Webster 2023; Paloniemi 2024.

### 2e. Not screened (no abstract reachable; no verdict given)

Ryoo, Jeon & Kim 2024, "The blame shift: Robot service failures hold service firms more accountable", JBR 171, 114360 (10.1016/j.jbusres.2023.114360). Lee, Mohamed, Lehto & Lehto 2026, "When technology fails hospitality", IJHM (10.1016/j.ijhm.2026.104811). Huang et al. 2025, *Tourism Management* (10.1016/j.tourman.2025.105315). Lim 2026, "From disclosure to accountability under generative and agentic AI in tourism research", *Annals* (10.1016/j.annals.2026.104228). Mota, Portugal & Portugal 2026, SSRN 7563639 (10.2139/ssrn.7563639; SSRN returned 403). Lee, Lee, Back & Li 2025, IJCHM CDR guest editorial (10.1108/IJCHM-11-2025-292). Castillo, Canhoto & Said 2022 (10.1007/978-3-030-95346-1_56). Tyagi & Tyagi 2026, JRPM (10.1057/s41272-026-00600-w). Swaminathan 2026, SSRN (10.2139/ssrn.7527865). Nosi 2025, SSRN (10.2139/ssrn.5158227). Pantano & Scarpi 2025, Springer encyclopedia (10.1007/978-3-031-75316-9_6-1). Ryoo et al. and Lee et al. (IJHM) bear most directly on firm accountability after a technology failure and are worth a library pull.

## 3. Final statement

**These works do part of what the claim says no one does.** I searched OpenAlex (title/abstract, 2017–2026, including nine named journals by ISSN), Crossref (2020–2026), Semantic Scholar abstract lookups, web search, and open-access full text, all on 13 Nov 2026. Consensus and Scholar Gateway were unreachable all session.

- **Which of several firms (T2/T3), in hospitality.** Parhi (2026) names the accountability diffusion across franchisor, franchisee and technology vendor, and treats AI governance as "a shared obligation embedded contractually" across them (§6.3.2). Dwivedi et al. (2026, abstract only) frame CDR in T&H as "auditable duties of care" across firms, platforms, vendors and partners.
- **One bearer named, and a route to correction (T2/T4).** Ariyogi et al. (2026) assign recovery ownership to the branded service organisation the guest deals with, "even when technical components are supplied elsewhere" (p. 78). They also specify escalation with decision authority (pp. 79, 85–86). Kuraa (2026, preprint) places responsibility on the deploying brand and requires a redress route (pp. 6, 29–31).
- **To whom (T1), inside phygital research.** Suh et al. (2026, JSM, phygital hospitality) address safeguards to hotels for guests, including a "visible route to human assistance" (§6). The claim's "neither to whom" therefore fails on its face for this paper, though Suh gives no ground for the obligation and says nothing about several firms.
- **General service and phygital governance.** Wirtz et al. (2023) and Samadi et al. (2026) make the focal or hub firm the governor of ecosystem-wide CDR. Shwartz Altshuler et al. (2025) split phygital-space governance between physical-space controllers and platforms (p. 19).

**What survives.** No work found grounds who owes the guest which duty in the role of host. None binds the duty to a particular firm through holding out, reliance or control of the guest's space. None states the in-stay route to correction as a duty of that role rather than a design feature, a governance pillar or a proposition. Parhi spreads the obligation; Ariyogi and Kuraa rest the bearer on guest attribution to the brand. Lim et al. (2026, SIJ) and Batat's (2026) PSR editorial both list "who controls and can contest" and "multiactor and ecosystem governance" as open agenda items. That supports the gap once it is narrowed.

**What the paper must do.**
1. **Cite** Parhi (2026) and Ariyogi et al. (2026) at the gap sentence, and Suh et al. (2026) where the paper says phygital research prescribes safeguards. Cite Wirtz et al. (2023) when the paper introduces the several-firms problem. None is in `references.bib`.
2. **Read Dwivedi et al. (2026) in full before submission.** Its abstract uses duty-of-care language for multi-firm T&H ecosystems, and the full text may come closer than the abstract shows.
3. **Narrow the claim.** Drop "neither to whom they are owed" as an absolute (Suh names guests and hotels). Restrict "which of several firms" to phygital research, or acknowledge the hospitality AI-governance work that diffuses (Parhi) or brand-assigns (Ariyogi; Kuraa) the obligation without grounding it in the host role.
4. **Position the third duty against Ariyogi et al.** Ariyogi et al. already propose a dependable escalation pathway with clear recovery authority, and Suh and Gustafsson prescribe escalation routes. The manuscript's novelty there is the ground (a duty of the host role during the stay) and the binding party, not the route itself.
5. **Optional:** cite Lim et al. (2026, SIJ) and the Batat (2026) PSR editorial as the field naming its own open question. If the authors want to show that law already allocates platform and host liability for short-term rentals, Tran (2025) is the only scholarly hit, read at abstract level.

**Suggested (Claude) narrowed gap sentence, yours to accept or rewrite:** "Phygital research prescribes safeguards for trust, fairness and well-being and addresses them to hotels, but does not say why the guest is owed them. Where hospitality research does take up the several firms behind a touchpoint, it spreads the obligation across them by contract (Parhi, 2026) or assigns it to the brand the guest blames (Ariyogi et al., 2026), rather than deriving it from the role of host."

# Scout B log, Phase B (run 2026-11-18)

Agent-drafted. Consolidated at the end of the pass; the brief asked for appends as I went, and I did not keep that discipline. Times are not recorded per line. Order below follows the work.

## Searches and records

- Crossref bibliographic lookups, 40 queries (`scout_tools/B/crossref_B_1.txt`, `crossref_B_2.txt`). Generic client `research-fetch/1.0`.
- OpenAlex search: rate-limited (429, "retry in 33-39s"); results not usable. OpenAlex DOI lookups were not retried. Gaps are recorded as NOT FOUND or unsearched, not as absences.
- Semantic Scholar search: 429 on every attempt across three tries each, then stopped (PLAN 8.2). Logged as BLOCKED.
- arXiv API: used for Gabriel 2024, South 2025, Dark Patterns GUI Agents, Et Tu Brute, AI Literacy power-knowledge, Riedl 2025. Three records not found (personal agents 2024, Echoes of Urgency via arXiv, Domination 2024 via arXiv); the Crossref route answered Echoes and Domination.
- WebSearch, discovery only: CSRB report, Anthropic framework, IMDA framework, Narayanan and Kapoor, Agent 365 (November 2026), Nadella commentary, Frontier Governance Framework, Copilot Copyright Commitment, cloud logging 2023, shared responsibility AI, Google secure agents, AWS scoping matrix, Ashkenazi, Amsterdam drivers judgments. Each URL was then fetched with curl; no quotation comes from a search summary.

## Fetches (open copies)

- DONE B1: `ms2026sharedresp`, `ms2023copilotcopyright`, `ms2023cloudlogging`, `ms2026servicesagreement`: HTML saved, text extracted.
- DONE B0: `nadella_blog_home` (snscratchpad home page; latest entry 10 Oct 2026), `nadella_commentary_tnw`, `aiact_official` (EUR-Lex OJ text of Reg. 2024/1689), `gdpr_official` (EUR-Lex OJ text of Reg. 2016/679), captured 2026-11-18.
- DONE B2: `anthropic2025safeagents`, `owasp2025agentic`, `acp2025agentic_commerce` (docs home only: partial), `aws2025scoping_matrix`, `google2025secure_agents` (PDF, 18 pp), `kasirzadeh2025agents` (arXiv PDF), `south2025authenticated` (arXiv PDF), `riedl2025agents` (arXiv PDF), `priyanshu2026etTu` (arXiv PDF).
- DONE B3: `susser2019technology` (PDF), `lund2026powerknowledge` (arXiv PDF), `edpb2023deceptive` (PDF, 74 pp).
- DONE B5: `kleinberg2018human` (NBER w23180 PDF, 76 pp), `narayanan2025normal` (Knight Institute essay, HTML).
- Removed as bot challenges (HTTP 403, Cloudflare "Just a moment" text): ananny2018seeing, bhatt2020explainable, longmagerko2020, mathur2021dark, widder2023dislocated, adamsprassl2023regulating, almada2019human, cobbe2023accountability, maas2022neorepublican (ScienceDirect captcha).
- Other blocked or missing: CSRB PDF (404 twice), Frontier Governance Framework (404 at guessed URL), WEF "AI Agents in Action" (403 at guessed URL), OpenAI Terms of Use (403), Sparks and Jayaram (De Gruyter, empty 202), SSRN (403, tested on 4612468), Anderson Private Government (no open copy).

## Disk

- Disk matches confirmed on the first page: Stamboliev 2023, Hoeksema 2025, Creel and Hellman 2022, Burrell 2024, Wachter et al. 2017, Gabriel et al. 2024, Edwards and Veale 2017, Tang et al. 2025 (GUI agents), Microsoft Entra page, Feng et al. 2025 (arXiv 2512.00742, new row). Hashes in `DISK_INVENTORY.tsv`.
- Mismatches on disk: `pdfs/M4/anderson1999.pdf` is "What Is the Point of Equality?" (Anderson 1999), not Private Government. `pdfs/nadella/R7/lazar2025governing/` is the arXiv 2410.20720 preprint of Lecture I, not the 2025 P&PA article.

## Step 5 (citing-work searches and new rows)

- Not run: the twenty-most-cited lists for the anchor works (Long and Magerko 2020, Edwards and Veale 2017, Kolt 2025, Shavit 2023). OpenAlex was rate-limited and Semantic Scholar was blocked. Only one new disk-found row was added (Feng et al. 2025). Gap for the lead.

## Step 6 (Scout B extras)

- (a) Nadella posts after 10 Oct 2026: none on the snscratchpad home page at 18 Nov 2026. Other outlets not checked.
- (b) Commentary on "Models as Insider Risks" dated 24 Oct to 18 Nov 2026: none found. One news report (TNW) saved, date not read and probably earlier.
- (c) Microsoft November 2026 agent-governance announcements: none found. Agent 365 GA on 1 May 2026 is the nearest (secondary sources only).
- (d) Official texts: AI Act (Reg. 2024/1689) and GDPR (Reg. 2016/679) saved from EUR-Lex. These are the original OJ texts; amendments (Omnibus 2026) are in `pdfs/nadella/R2/omnibus` and were not compared.

## Not located or not searched

- IMDA Model AI Governance Framework for Agentic AI: official PDF not found.
- Ashkenazi "Solving the No-Reading Problem with AI": no record found.
- Empowering Consumers with Personal AI Agents (2024): no record found.
- UNESCO AI competency framework: official page not fetched.
- OECD AI-literacy framework: Crossref candidate (10.1787/65cd27d4-en) does not confirm the framework named in the lead.
- Amsterdam Court of Appeal 2023 drivers judgments: primary text not reached; press only.
- Not searched at all: ChatGPT agent help page; WEF via search; Microsoft Frontier Governance Framework via search beyond one query.

## Tally

- Rows in `SOURCES_B.tsv`: 71. record_status: OK 55; NOT FOUND 12; MISMATCH 4 (Entra page title; Anderson disk file and the Private Government record; Bayamlioglu year; Arbel year and venue). Note: Anderson's row is MISMATCH for the disk file, not the record.
- access: full 31; blocked 19; unsearched 16; library 3; partial 2.
- Cards written: 0 (Scout B writes no cards).
- Blocked: ananny2018seeing, bhatt2020explainable, longmagerko2020, mathur2021dark, widder2023dislocated, adamsprassl2023regulating, almada2019human, cobbe2023accountability, maas2022neorepublican, sparks2022rule, csrb2024exchange, ms2025frontiergov, openai2026terms, wef2025ai_agents, imda2026agentic (not located), ayres2024risky, maas2023analogy (SSRN).

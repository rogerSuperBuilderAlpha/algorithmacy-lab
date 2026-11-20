# B1 facet report — Nadella's texts and Microsoft's own record

Agent-drafted. The author has not reviewed it and none of the text is his.

(B1, Opus 5.5, 2026-11-18. Log: `B1_nadella_and_microsoft.log.md`. Table: `../synthesis/NADELLA_MOVES.md`. Budget cut
in force: cap 8 cards; 5 written.)

## 1. Counts by read status

| source_basis | Cards |
|---|---|
| full-text | 4 (nadella2025positive, jakkal2023expanding, smith2023microsoft, microsoft2026artificial) |
| partial-text | 1 (microsoft2026services: clauses read by search) |
| abstract | 0 |
| secondary | 0 |

Targets not carded: 7 (1 already carded, 5 scout rows not OK, 1 failing the date test). All `verified: pending`.

## 2. Entries

| Citekey | Record verified by | Read status | Bearing (STRUCTURE section) |
|---|---|---|---|
| nadella2025positive | Publisher page: saved HTML title, canonical URL, datePublished 2025-11-15 | full-text | 4.3 (control allocated to firms); 7-D08 (no skilling pledge to individuals); counter (concedes a cost of the last platform wave). Person acted on: nothing |
| jakkal2023expanding | Publisher page: heading, byline, datePublished 2023-07-19 | full-text | 4.4-record (log types and retention set by Microsoft by licence tier until CISA pressure); 7-D04. Person acted on: no record |
| smith2023microsoft | Publisher page: title, byline, published 2023-09-07 | full-text | 4.4-loss: counter-instance (provider carries copyright loss for paying commercial customers, conditioned on its own filters); 7-D06 precedent of form. Person acted on: no loss cover |
| microsoft2026services | Publisher page: Published 2026-07-30, Effective 2026-09-30 | partial-text | 4.4-loss (user "solely responsible" for third-party claims; §13 cap); 4.4-record (Microsoft stores inputs and outputs for abuse monitoring); 4.4-contest (§15 arbitration); 6-responsibilization (oversight duty on account holder) |
| microsoft2026artificial | Publisher page (Microsoft Learn): heading, ms.date 2026-08-24 | full-text (diagram not read) | 4.3 and 4.4-loss (tasks split only between Microsoft and the customer); 4.2 and 6-responsibilization ("educate users") |

## 3. What each STRUCTURE section in scope can rest on

| Section | Cards (read depth) |
|---|---|
| Intro (P2, P3, P5, P11, P21) | nadella2026models (full, existing card); NADELLA_MOVES rows 2, 3, 5, 11, 21 |
| 4.3 Nadella's architecture; "already runs in Agent 365" | microsoft2026overview (full, existing); microsoft2026artificial (full); nadella2025positive (full). "Microsoft's agent-policy specification": UNSUPPORTED, no card in `CARD_INDEX.md` matches |
| 4.4 medium / envelope (P3, P5, P11, P17) | nadella2026models; microsoft2026overview; microsoft2026connect (partial). Entra agent identities: on disk, not carded (scout MISMATCH) |
| 4.4-record (P15) | microsoft2026audit, microsoft2026tracing, microsoft2026responsible (existing); jakkal2023expanding (full); microsoft2026services §14(s)(v) (partial). CSRB 2024: UNSUPPORTED, not reached |
| 4.4-stop (P19) | microsoft2026use, microsoft2026enabling, microsoft2025multistage (existing). No new card |
| 4.4-contest (P20) | microsoft2026microsoft (existing); microsoft2026services §15 (partial) |
| 4.4-loss | microsoft2026services §§13, 14(s)(viii) (partial); microsoft2026copilot (existing); smith2023microsoft as counter (full); microsoft2026artificial (full) |
| 7-D08 / ruling 23 (scaffold) | nadella2025looking (existing); nadella2025positive (full); smith2025microsoft (existing) |

## 4. Claims the sources contradict or narrow

| Claim (where) | Source and locator | Effect |
|---|---|---|
| §4.4 row 1 pairs P5/P17 with "Monopoly; custody by an interested party" (STRUCTURE §4.4; ARGUMENT A4) | nadella2026models P5, P14, P17; nadella2026reverse ("Choice"); nadella2025positive para. 10 | Narrower: these moves separate supply from control and spread it to the deployer against the provider; the monopoly property holds only for the deployer's custody toward outsiders, which the text leaves silent, not for the architecture as a whole |
| §4.4 loss row: terms make the user "solely responsible" (STRUCTURE §4.4; A4 "the loss rests on the person") | smith2023microsoft paras 3, 5, 8 | Narrower, not contradicted: Microsoft does carry a loss for paying commercial customers (copyright only, conditioned on its filters). The person acted on still gets no cover |
| P3 placed on the loss row | nadella2026models P3 | P3 keeps responsibility with the deployer, the stronger party; the loss row rests on Microsoft's terms (microsoft2026services, microsoft2026copilot), not on P3 |
| §4.4 record row: "evidence for the deployer (P15)" | nadella2026models P15 | Narrower: P15 names no reader ("human readable"); the exclusion of the person acted on is in the products (microsoft2026audit, microsoft2026tracing), not in the sentence |
| §4.4 stop row: brake held by "an authorized person" | nadella2026models P19, P17 | Holds, but the authoriser is undefined in P19; the reading needs P17 |
| A4 "standards are written by industry bodies" | nadella2026models P6, P19 | Holds as stated in the text; who takes part is not said |
| A4 falsifier ("a move shown to give the second party the record, the brake, the envelope or standing") | microsoft2026services §14(s)(ix)(1) | Not met. The closest is a duty on the account holder to keep "appropriate human oversight" over consequential decisions about "any person"; it gives that person no right |

## 5. Gaps and blocks

| Source | Status | Where a library user would find it |
|---|---|---|
| Cyber Safety Review Board, Review of the Summer 2023 Microsoft Exchange Online Intrusion (2024) | Scout NOT FOUND (CISA PDF 404 twice); not carded | CISA publications listing or DHS press release of 2 Apr 2024; government-documents collection |
| Microsoft Frontier Governance Framework (2025) | Scout NOT FOUND (404); not carded | Microsoft's 2025 Responsible AI Transparency Report and its On the Issues blog; web archive of microsoft.com |
| "What are agent identities?" (Microsoft Entra Agent ID) | Scout MISMATCH; page on disk at `pdfs/nadella/R2/ms_entra_agentid/`; not carded | Microsoft Learn (open) |
| Nadella posts after 10 Oct 2026 | Scout NOT FOUND on snscratchpad; other outlets (X, LinkedIn) unchecked | Author's X and LinkedIn accounts |
| Microsoft agent-governance announcements, Nov 2026 | Scout NOT FOUND. The saved cloud-logging page lists two Microsoft Security Blog posts: "Security for the agentic era, powered by Microsoft Perception" (17 Nov) and "What's new in Microsoft Security: November 2026" (5 Nov); not fetched | Microsoft Security Blog (open) |
| Commentary on the post dated after 24 Oct 2026 | None found; TNW report is dated 12 Oct 2026 and is news | — |
| "AI agent shared responsibility model" (Microsoft Learn), linked from microsoft2026artificial | Not a scout row; not fetched | Microsoft Learn (open) |
| Microsoft product terms behind the Customer Copyright Commitment | Not opened | Microsoft Product Terms site (open) |

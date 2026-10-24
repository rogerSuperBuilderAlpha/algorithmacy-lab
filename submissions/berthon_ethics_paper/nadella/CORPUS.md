# Corpus for the Nadella analysis

*Written by Claude on 2026-10-24.* Everything the research can start from, in four groups: Nadella's own texts,
reports on the X article, the lab's earlier analyses of it, and the cards behind those analyses.

## 1. Nadella's texts (full text held locally, not in this repo)

The repo is public and the X capture is marked for local use only, so the full texts sit in
`~/iit-playground/berthon_ethics_local/nadella/` (its README lists each file). Cite paragraphs as P1–P21, the
capturer's locators, which the lab's earlier work (facet G; MANUSCRIPT_v4's "para.") already uses. The X text and the
blog text match paragraph for paragraph.

| Text | Date | Local file | Card |
| --- | --- | --- | --- |
| **Models as Insider Risks in the Super Intelligence Era** (X article; also on the blog) | 2026-10-10 | `x/nadella_2026-10-10_models_as_insider_risks.txt`; `posts/2026-10-10_models-as-insider-risks.txt` | `../literature/cards/berthon_ethics_course/nadella2026models.md`; `../literature/cards/dxd_foundation/nadella2026models.md` |
| The Reverse Information Paradox | 2026-07-12 | `posts/2026-07-12_reverse-information-paradox.txt` | `dxd_foundation/nadella2026reverse.md` |
| A frontier without an ecosystem is not stable | 2026-06-14 | `posts/2026-06-14_frontier-ecosystem.txt` | `dxd_foundation/nadella2026frontier.md` |
| Looking Ahead to 2026 | 2025-12-29 | `posts/2025-12-29_looking-ahead-2026.txt` | `berthon_ethics_course/nadella2025looking.md` |
| Positive Sum Future (began on X) | 2025-11-15 | `posts/2025-11-15_positive-sum.txt` | none yet |

**The X article, paragraph by paragraph** (labels only; read the local text before quoting):

| P | What it does |
| --- | --- |
| 1–2 | Old software could be traced to a code path; frontier models cannot be, yet they get "our most sensitive data" and "mission-critical actions on our behalf" |
| 3 | A new "trust architecture"; responsibility cannot be outsourced; a provider's assurances do not relieve "us" |
| 4–5 | Not nested black boxes to accept or reject: contained systems to observe, test and contain; "separate the supply of intelligence from the authority over it" |
| 6 | Alignment set aside; deterministic design, human controls, operating procedures, industry standards |
| 7–8 | Models as insider risks, not malicious but able to err or be compromised; enterprise practice (identity, least privilege, logging, containment) |
| 9 | Chain-of-thought transparency "non-negotiable" but "not sufficient or dependable" |
| 10 | Models checking models end in nested black boxes |
| 11–12 | Controls outside the model (a 1970s security principle); model separate from harness and action space |
| 13 | "Principles of observability" |
| 14 | Model diversity |
| 15 | Observe everything: "tamper-proof human readable evidence" |
| 16 | Verifiability: continuous testing, including failures |
| 17 | Independent controls: "Orgs" decide access and actions |
| 18 | Independent auditability |
| 19 | Containment: an emergency brake that "An authorized person" can pull |
| 20 | Incident disclosure "to those affected" and to industry |
| 21 | The most trustworthy system "enables us to trust the model the least" |

## 2. Reports on the X article

| Report | Card | Local copy |
| --- | --- | --- |
| Kumari, Business Standard, 12 Oct 2026 | `dxd_foundation/kumari2026nadella.md` | `commentary/kumari2026nadella.html` |
| Constantin, 12 Oct 2026 | `dxd_foundation/constantin2026nadella.md` | `commentary/constantin2026nadella.html` |
| Sudjianto, Substack, 10 Oct 2026 (the first substantive commentary found) | `berthon_ethics_course/sudjianto2026when.md` | — |

Facet G found no expert critique of the post in its first two days (`sources/dxf_facet_G_nadella_lineage.md`, C9).

## 3. The lab's earlier analyses of the post

| Where | What it concluded | Copy here |
| --- | --- | --- |
| `dxd_foundation` facet G, "The Nadella post and its lineage" (57 sources) | The fairest statement (C1); lineage in the reference monitor, Saltzer and Schroeder, CERT, zero trust (C2); chain-of-thought monitoring is fragile, and the AI-safety work almost never tests the human reader (C3); the three human tasks the post creates (reconstruct from logs, notice and halt, hold responsibility) and what the human-factors evidence says of each (C4); observability vs transparency (C5); real convergences (C6); the three counts tested against the text (C7); **scope cautions** (C8); claims tested (C9) and claims the sources contradict (C10) | `sources/dxf_facet_G_nadella_lineage.md` + `.bib` |
| `berthon_ethics_course` facet V1, "Nadella's post and the disclosure paradigm" | The post move by move; Microsoft's own record (Responsible AI Standard, transparency reports, Copilot note, AI literacy guide, Elevate); the EU AI Act; commentary; for, narrows, against | `sources/bec_facet_V1_nadella_disclosure_paradigm.md` + `.bib` |
| `berthon_ethics_course` facets V2, V4–V6 | Oracy to literacy; disclosure and burden; scaffolding; prior work and objections (the v4 research) | `sources/bec_facet_V*.md` |
| MANUSCRIPT_v4, §§1, 4, 5 | The essay's ethical design toward people "stops at legibility"; three echoes (burden, medium, missing scaffold); v4 notes on where it departs from the author's framing | `../sources/08_MANUSCRIPT_v4.md`; `../sources/notes/berthon_v4_*.md` |
| `dxd_foundation` drafts v1–v4, claim, argument map, outline, review | Word separation moved work from reader to page; Nadella's post offers a record to read and a brake, and is silent on the people the model acts upon | `sources/dxf_*.md` |
| `dxd_foundation` facets E, H, L, S, T, X, Z | The human-factors frame, candidate moves, disclosure and choice, read-to-check in HMI, adjudication, the counter-case, the gap search | `sources/dxf_facet_*.md` |
| This arm's ledger | Rows E13 (the essay), E14 (Microsoft's practice), E15 (oversight without capacity), E16 (AI literacy in law), O06–O07, D06–D08; conflict X07 (sufficient or insufficient) | `../consolidation/` |

## 4. Cards

`CARDS.md` lists the 61 cards behind facets G and V1, now copied into `../literature/cards/` (and indexed in
`../literature/CARD_INDEX.md`), and the 7 facet-G sources that have no card (Above Security, Ananny and Crawford,
Endsley 1995, Lin and Zainescu, Mackworth, Tariq, Warm).

## 5. The two transitions

| Transition | Lab research (copied into `sources/`) | Its verdicts, in brief |
| --- | --- | --- |
| *Scriptio continua* to word spacing | `dxf_facet_A_the_record` (what changed, where, when, by whom); `B_the_dispute` (Saenger's thesis and its critics); `C_spacing_to_literacy` (did spacing spread reading?); `D_reading_science` (what a space does for a reader); `F_parallel_moves`; `J_who_holds_the_convention`; `K_training_and_cause`; `O_custody_of_conventions`; `W_spacing_oracy_literacy`; adjudication `dxf_facet_T_adjudication` | Spacing lowered a cost, not a cause of literacy (C, verdict 5); it came as a complex of conventions over centuries (T §4); ruler and church held the page's conventions (O; T §10); readers used to spaces lose a third to a half of their speed without them (README) |
| Print and mass literacy | `bec_facet_B_print_1450_1800` (who was shut out, by what rule, 1450–1800); the consolidation's rows H11–H13, H17, H24 | Four print-era failures: corporate monopoly of the press, the 1543 bar on reading the English Bible by rank and sex, Tridentine licensing, language bars at law; then the oversold promise of mass literacy (H13) |

The lab's ledger rows on the scribal analogy are H26 and H27 (`../consolidation/CONCEPT_LEDGER.md`).

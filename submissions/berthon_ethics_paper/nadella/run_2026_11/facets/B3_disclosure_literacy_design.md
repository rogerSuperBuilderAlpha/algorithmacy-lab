# B3 facet report: disclosure, AI literacy, responsibilization, dark patterns

Agent-drafted. The author has not reviewed it and none of the text is his.

Written 2026-11-18 by agent B3 (sonnet). Cap 6 cards under the PLAN section 10 budget cut (cuts 1-5); dark patterns limited to two cards. Log: `B3_disclosure_literacy_design.log.md`.

## 1. Counts by read status

| Read status | Cards |
|---|---|
| full-text | 0 |
| partial-text | 6 |
| abstract | 0 |
| secondary | 0 |

All six were read in part (pages named in each card's `pages_read`); none was read end to end, to stay within the forty-page rule and the cap. Blocked, not carded: 5. Skipped at the cap: 5. Ran `tools/precheck.py B --no-net` once at the end; all quoted strings of my six cards were located (see lead note in the return).

## 2. Entries

| Citekey | Record check | Read status | Bearing (STRUCTURE) |
|---|---|---|---|
| lund2026powerknowledge | arXiv API (title, date 2026-07-30); authors from PDF | partial-text (pp. 1-7 of 8) | narrows: 1.2, 4.1, 4.2, 7-D08, counter |
| stamboliev2023postcritical | Crossref (title, author, 2023, Media Theory 7(1) 201-232) | partial-text (pp. 201-202, 215-219) | narrows: 1.2, 4.1, 4.2, counter |
| wachter2017right | Crossref (3 authors, IDPL 7(2) 76-99) | partial-text (author manuscript pp. 1, 4-9, 11-12, 15-16, 19, 31-32, 36-37, 41, 43) | supports: 4.2, 4.4-contest, 4.4-stop, counter |
| susser2019technology | Crossref (3 authors, 30 Jun 2019, IPR 8(2)) | partial-text (pp. 1, 4, 6-8, 13) | supports and contests: 4.2, 4.4-contest, new-category |
| edpb2023deceptive | Publisher's own PDF read (title page, version history); v1.0 not compared | partial-text (pp. 1-4, 11-13 of 75) | supports: 4.2, 4.4-contest, new-category |
| tang2025darkgui | arXiv API (title, date 2025-09-12); authors from PDF | partial-text (pp. 1, 3, 10, 13-16, 19 of 44) | supports: 4.3, 4.4-stop, 4.4-record, 4.4-loss, 6-responsibilization, new-category |

## 3. What each STRUCTURE section can rest on

- **1.2 (why literacy, not as a metaphor):** lund2026powerknowledge (partial, pp. 4, 7), stamboliev2023postcritical (partial, pp. 217-219). Kamperman and Graff (2026) are not in this facet; not re-opened.
- **4.1 (the promise: "AI literacy" sold as the remedy):** lund2026powerknowledge p. 4 (four public frameworks read by the authors as consumer training; I did not open them), stamboliev2023postcritical p. 218 ("overpromise"). UNESCO and OECD/EC frameworks themselves: UNSUPPORTED here (not fetched; see section 6).
- **4.2 (remedies on offer: disclosure, training, law's narrow rights):** wachter2017right (art. 22(3), recital 71, "right to be informed", pp. 7, 12, 36, 41), susser2019technology p. 13 (notice insufficient), stamboliev2023postcritical p. 216 (XAI would not have changed much for those affected; the author's own speculation). Existing cards edwards2017slave, anannycrawford2018 (abstract) were not re-read.
- **4.4-contest, 4.4-stop, 4.4-record, 4.4-loss:** tang2025darkgui pp. 15-16 (audit trails, automation boundaries, ex-ante liability; recommendations, not practice). Wachter p. 36 (contest right limited to contract and consent cases).
- **6-responsibilization:** tang2025darkgui p. 16 ("responsibility defaults to end users"). The responsibilization literature itself (Shamir 2008; Draper and Turow 2019): UNSUPPORTED, both blocked by paywall.
- **7-D08 (scaffold duty):** lund2026powerknowledge pp. 5-6 (its own three-part framework, still on the user's side). Evidence that training or disclosure helps (question 6): UNSUPPORTED; Tully, Longoni and Appel (2025), Ng et al. (2021) not opened (see section 6).
- **Dark-patterns definition (question 5):** edpb2023deceptive p. 3 (regulator's definition, social media, GDPR); susser2019technology p. 7 (design that exploits decision-making vulnerabilities). Extension to conversational AI: no source in hand says it; tang2025darkgui extends to GUI agents, not conversational AI. Mathur et al. (2021) and Luguri and Strahilevitz (2021) are UNSUPPORTED here.
- **AI Act art. 4 (question 3):** UNSUPPORTED by a new card. The OJ text is already carded (eu2024aiact); the Omnibus status of art. 4 was not checked (scout note: see disk pdfs/nadella/R2/omnibus).

## 4. Sources that already make the paper's argument or part of it

| Source | Claim (exact words or close paraphrase) | Locator |
|---|---|---|
| lund2026powerknowledge | The competency model "is a sophisticated version of the banking model of education: institutions deposit AI skills into users so that users can more efficiently participate in the knowledge economy". | p. 4 |
| lund2026powerknowledge | The omission of power "reflects the interests of the institutions that produce AI literacy curricula, which are typically the same institutions that create AI systems". | p. 4 |
| stamboliev2023postcritical | "Teaching skills seems to be the pragmatic solution to a complex problem", and "it is advertised as such"; "media literacy may overpromise". | p. 218 |
| stamboliev2023postcritical | For those affected in the Dutch case, "XAI would not have altered much" (author flags it as speculation); the harmed "are powerless to stop, alter, or intervene". | p. 216 |
| stamboliev2023postcritical | Transparency in XAI feeds "an illusion that we democratise AI by explaining it". | p. 217 |
| susser2019technology | "merely notifying someone that they are the target of manipulation is not enough to neutralise its effects". | p. 13 |
| tang2025darkgui | "Without such frameworks, responsibility defaults to end users least able to manage the risk." | p. 16 |
| wachter2017right | The GDPR gives a "right to be informed" about system functionality, "restricted by the interests of data controllers"; a right to explanation of a specific decision is not mandated. | p. 41 |

None of the six uses the literacy-myth literature (Graff) or the word responsibilization. Lund and Stamboliev make the critique of AI literacy as consumer or skills training; they do not argue it repeats the history of literacy. The paper's historical argument is therefore not pre-empted by these sources, but part of its present-day critique is (see ADJUDICATION ruling 17 and the Kamperman and Graff point in STRUCTURE 1.2).

## 5. Claims in STRUCTURE.md, ARGUMENT_AND_OUTLINE.md or the ledger that these sources contradict

- None contradicted outright.
- CONFLICTS X07 mentions "the empirical case against disclosure (E08)". Nothing in these six is an empirical test of disclosure; Wachter is doctrinal, Susser and Stamboliev are conceptual, Lund is theoretical. The empirical case must rest on other cards.
- CONFLICTS X08 says the duty to scaffold "is not itself new". Lund's Participatory Governance and Stamboliev's "seat at the table" (p. 219) are also user-side remedies and so also stand exposed to the responsibilization objection; neither addresses it.
- STRUCTURE 4.2 says disclosure and AI-literacy training are "necessary, not sufficient" (Berthon, Pitt and Campbell 2019). Susser (p. 13) and Stamboliev support "not sufficient"; no source here tests "necessary".

## 6. Gaps and blocks

| Source | Status | Where a library user would find it |
|---|---|---|
| Ananny and Crawford, "Seeing without knowing" | BLOCKED (SAGE bot challenge, per scout); existing abstract-level card stands | New Media and Society 20(3), 2018; DOI 10.1177/1461444816676645 |
| Bhatt et al. 2020 | BLOCKED (ACM bot challenge, per scout) | FAT* 2020; DOI 10.1145/3351095.3375624 |
| Long and Magerko 2020 | BLOCKED (ACM, per scout); existing abstract card stands | CHI 2020; DOI 10.1145/3313831.3376727 |
| Mathur, Mayer and Kshirsagar 2021 | BLOCKED (ACM, per scout) | CHI 2021; DOI 10.1145/3411764.3445610 |
| Shamir 2008 | BLOCKED (no open route; OpenAlex is_oa false) | Economy and Society 37(1); DOI 10.1080/03085140701760833 |
| Draper and Turow 2019 | BLOCKED (no open route) | New Media and Society 21(8); DOI 10.1177/1461444819833331 |
| Ng et al. 2021 | BLOCKED (ScienceDirect 403 challenge; HKUST repository redirect loop) | Computers and Education: Artificial Intelligence 2; DOI 10.1016/j.caeai.2021.100041; listed in DOAJ |
| Hoffman et al. 2026 "Echoes of Urgency" | SKIPPED, cap reached | AERA proceedings; DOI 10.3102/2281796 |
| Tully, Longoni and Appel 2025 | SKIPPED, cap reached (preprint at OSF 10.31234/osf.io/t9u8g is an untried open route) | Journal of Marketing; DOI 10.1177/00222429251314491 |
| Luguri and Strahilevitz 2021 | SKIPPED, cap reached and dark-patterns limit of two | Journal of Legal Analysis; DOI 10.1093/jla/laaa006 |
| OECD AI-literacy framework | NOT FOUND in scout (candidate DOI resolves to a different OECD title); SKIPPED | oecd.org |
| UNESCO AI competency framework | NOT FOUND in scout; SKIPPED | unesco.org (official page not fetched) |

Other notes for the lead:
- Questions 3 and 6 (art. 4 on the official text; evidence that disclosure or training helps) are unanswered by new cards. The strongest-evidence-for-training source (Tully et al.; the Ng review) and the art. 4 Omnibus status need a later pass if the cap is lifted.
- Disk copies of Stamboliev (2023), Wachter (2017) and Tang (2025) have no recorded origin beside the file, or none beyond a SOURCE_URL; the verifier should confirm the Wachter text against the version of record, since it is an author manuscript with its own pagination.
- Lund and Teel (2026) is an arXiv preprint, no journal venue; scout recorded it as a single "second author", and the PDF shows Brady D. Lund and Zoë Abbie Teel.

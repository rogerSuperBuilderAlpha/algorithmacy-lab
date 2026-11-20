# run_2026_11 status

*Kept by the lead (Claude). Updated 2026-11-19.*

| Stage | State | Commit |
|---|---|---|
| Plan (Fable 5.2) | done: `PLAN.md` | 610df212 |
| A0 scout, A1 drafting | done: 38 cards, five facet reports | 376b80e2 |
| A2 verify, A3 Fable read, A4 gap report | done: 5 true, 30 corrected, 3 pending (Levine, Sandiford, Yılmaz: no saved source); `synthesis/GAP_REPORT.md` Part A | 659b4abc |
| Author stop after A4 | skipped on the author's instruction to run everything at once; Phase B proceeds on the default "no sixth failure" | — |
| B0–B4 | done (workflow `wf_2ce86abf-1d7`, cut to 30 cards per PLAN §10 cuts 1–5): scout, five facets, 27 cards, `NADELLA_MOVES.md`, precheck, verifiers V-B-1/V-B-2, Fable reads B | see below |
| B3 Fable read, remainder | done 2026-11-19 (seven cards the cut-off sitting missed; all corrected) | 595d044e |
| B4 Synthesis (SB, opus) | done: `EVIDENCE_MAP.md` (152 rows: 51 carried, 69 narrower, 18 contested, 14 UNSUPPORTED), `COUNTER_EVIDENCE.md` (51), `GAP_REPORT.md` Part B, `CONFLICTS_FOR_LEAD.md` (54) | e5d30984 |
| C Indexer (haiku) | done: 62 cards to `../../literature/cards/run_2026_11/`; CARD_INDEX 728 -> 790; `INDEX_DELTA.md` | 1ac3e4e9 |
| C Adjudication (fable) | done: `synthesis/ADJUDICATION.md`, 54 rulings (29 upheld, 15 narrowed, 6 overruled, 4 left for the author); 15 calls for the author; verifier error rates | this commit |

| Follow-up F (lead's card list) | done: sources saved for levine, sandiford, yilmaz; new cards microsoft2026copilot (upgrade), euaiact2026dates, uscongress1975section201; gadeke2020mugger corrected; verifier V-F, Fable read F; all seven `corrected`; ADJUDICATION erratum to ruling 1 (AI Act art. 111(2)); index 796 | this commit |

Held back from the index: none.

## Open after the run

- **Author's calls: ruled.** The author delegated all fifteen on 19 Nov 2026; the rulings are in
  `synthesis/AUTHOR_CALLS_RULED.md`, each reversible.
- **Narrowings carried (19 Nov 2026):** `ARGUMENT_AND_OUTLINE.md` to v4; `STRUCTURE.md` (each change tagged with
  its ruling or call); concept ledger N04, N05, L04, E07; `references.bib` notes for guinn1915guinn and
  saunders1971anglia; `NADELLA_MOVES.md` row 8; `EVIDENCE_MAP.md` and `COUNTER_EVIDENCE.md` (ruling 4's "no duty
  to fact-check", ruling 5's indemnity); `COVERAGE_PREMISES.md` A7. This line also clears CONF-21.
- **Still open:** the pending library cards (Lazar ×2, Lassiter, CPPA, Colorado, arbel2025how); s. 201 of the
  Voting Rights Act as it stood in 1975; version-of-record page checks (Wachter, Yeung, *Saunders*, Kleinberg).
- **Next:** DRAFT_v2 on the restored structure (call 15).
- **Erratum:** read ruling 1 and call 8 in `ADJUDICATION.md` with its appended erratum.

## Spend

The lead cannot read dollar spend from inside Claude Code. Subagent tokens so far: planning about 0.37M, Phase A
drafting about 0.90M, Phase A verification about 1.55M. Check the Console billing page for the true figure.


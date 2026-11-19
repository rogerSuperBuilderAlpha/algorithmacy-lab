# run_2026_11 status

*Kept by the lead (Claude). Updated 2026-11-18.*

| Stage | State | Commit |
|---|---|---|
| Plan (Fable 5.2) | done: `PLAN.md` | 610df212 |
| A0 scout, A1 drafting | done: 38 cards, five facet reports | 376b80e2 |
| A2 verify, A3 Fable read, A4 gap report | done: 5 true, 30 corrected, 3 pending (Levine, Sandiford, Yılmaz: no saved source); `synthesis/GAP_REPORT.md` Part A | 659b4abc |
| Author stop after A4 | skipped on the author's instruction to run everything at once; Phase B proceeds on the default "no sixth failure" | — |
| B0–B4, C | running (workflow `wf_2ce86abf-1d7`), Phase B cut to 30 cards (PLAN §10 cuts 1–5) because actual spend could not be read from inside the session | — |

## Spend

The lead cannot read dollar spend from inside Claude Code. Subagent tokens so far: planning about 0.37M, Phase A
drafting about 0.90M, Phase A verification about 1.55M. Check the Console billing page for the true figure.

## To resume in a later session

If the Phase B workflow was cut off, relaunch it from the main session with
`Workflow({scriptPath: "~/.claude/projects/-Users-ludwitt/0061aa16-14b1-46d5-ab52-9b8b50eb3b24/workflows/scripts/berthon-run-phase-b-wf_2ce86abf-1d7.js", resumeFromRunId: "wf_2ce86abf-1d7"})`
in the same session, or in a new session re-run each unfinished brief in `PLAN.md` §11 (every agent reads its own
log first and skips sources marked DONE or BLOCKED). Then commit.

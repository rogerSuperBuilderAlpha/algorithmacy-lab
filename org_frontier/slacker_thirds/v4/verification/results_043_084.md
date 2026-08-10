# Verification results — V-043 through V-084

**Scope check performed before any verification work:** `claim_map.md`'s Retrievable column was
read for every row in this batch (confirmed by direct grep against the file, not by eye). Result:
all 42 rows, V-043 through V-084 inclusive, carry Retrievable = `author` (17 rows) or `internal`
(25 rows). Zero rows in this range carry Retrievable = `agent`. Per task instructions — "Skip rows
whose Retrievable? column says `author`... or `internal`... Record them as `not-attempted`" — no
row in this batch was eligible for source retrieval, and none was attempted.

Only `claim_map.md` was read to produce this table, as instructed.

| ID | Verdict | Source text quoted | What is wrong, if anything | Suggested minimal correction |
|---|---|---|---|---|
| V-043 | not-attempted | — | Retrievable = `internal`: rests on the project's own coder tables (`handoff_census.md` and coder files), not a source a web/library check can reach. | — |
| V-044 | not-attempted | — | Retrievable = `internal`: census/kappa figures from the author's own coding tables. | — |
| V-045 | not-attempted | — | Retrievable = `internal`: census count. | — |
| V-046 | not-attempted | — | Retrievable = `internal`: methodological note about the project's own transcript instrument. | — |
| V-047 | not-attempted | — | Retrievable = `internal`: census count. | — |
| V-048 | not-attempted | — | Retrievable = `internal`: the project's own definitional/coding rule. | — |
| V-049 | not-attempted | — | Retrievable = `internal`: census list. | — |
| V-050 | not-attempted | — | Retrievable = `author`: film dialogue quotation, needs the Criterion disc per Note 1's disclaimer. | — |
| V-051 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-052 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-053 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-054 | not-attempted | — | Retrievable = `internal`: claim about what the two codings jointly show. | — |
| V-055 | not-attempted | — | Retrievable = `internal`: census count. | — |
| V-056 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-057 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-058 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-059 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-060 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-061 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-062 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-063 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-064 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-065 | not-attempted | — | Retrievable = `internal`: self-referential drafting-history claim, checkable only against the project's own prior-draft record. | — |
| V-066 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-067 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-068 | not-attempted | — | Retrievable = `internal`: census count. | — |
| V-069 | not-attempted | — | Retrievable = `internal`: census count. | — |
| V-070 | not-attempted | — | Retrievable = `author`: self-referential `[DISC:T2]`-flagged seam claim, needs the disc. | — |
| V-071 | not-attempted | — | Retrievable = `author`: self-referential `[DISC:T3]`-flagged seam claim. | — |
| V-072 | not-attempted | — | Retrievable = `author`: film dialogue quotation, `[DISC:T4]`-flagged. | — |
| V-073 | not-attempted | — | Retrievable = `author`: self-referential `[DISC:T6]`-flagged film-content claim. | — |
| V-074 | not-attempted | — | Retrievable = `author`: self-referential `[DISC:T11]`-flagged claim about the transcript's end. | — |
| V-075 | not-attempted | — | Retrievable = `internal`: self-referential claim checkable only against `scene_ledger.md`/transcript. | — |
| V-076 | not-attempted | — | Retrievable = `author`: self-referential `[DISC:T5]`-flagged film-content claim. | — |
| V-077 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-078 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-079 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-080 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-081 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-082 | not-attempted | — | Retrievable = `author`: film-content claim. | — |
| V-083 | not-attempted | — | Retrievable = `author`: film dialogue quotation. | — |
| V-084 | not-attempted | — | Retrievable = `author`: film-content claim. | — |

## Summary

- Rows assigned: V-043–V-084 (42 rows).
- Verified: 0.
- Not-attempted: 42 (17 `author`, 25 `internal`).
- Verdict counts: `not-attempted` × 42. No `verbatim-confirmed`, `paraphrase-faithful`,
  `overreach`, `contradicted`, `locator-wrong`, or `unretrievable` verdicts apply, since no row
  in this range was eligible for source retrieval.
- No `overreach` or `contradicted` findings in this batch.

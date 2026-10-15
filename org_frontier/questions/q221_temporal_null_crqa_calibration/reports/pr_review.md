# Self-review of draft PR #842 (2026-10-15)

## Scope and conventions

- **Base.** `rogerSuperBuilderAlpha:contrib` at `44f9b491`, which is an ancestor of the head.
- **Changed paths** (134 files vs contrib): only
  - `org_frontier/questions/q221_temporal_null_crqa_calibration/**`;
  - the generated `README.md` and `MAP.md`;
  - `ci/reproduce.json`, where entries were inserted textually and the existing format is preserved.
- **Untouched:** q161, q220 and #841.
- **Generated indexes current:** `tools/build_index.py --check`, `tools/build_map.py --check`,
  `build_research_index.py --check` and `build_cards_index.py --check` all exit 0.
- **Large file.** `identifiability/results/pair_search.json` is 716 KB (about 107k lines). It is the
  full-enumeration record behind the screen counts. It could be compressed or trimmed before a non-draft
  merge, at the maintainer's discretion.

## Correctness checks run

| check | result |
|---|---|
| q221 fast tests | 16 pass |
| q221 expensive tier (`Q221_SLOW=1`) | 6 pass |
| q220 tests | 73 pass |
| `ci/reproduce.py --changed-file` | 13/13 pass |
| slow reproduce checks (q161; q220 ×5; q221 exact screen, structural baselines and null extension) | 9/9 pass, 827 s |

## Scientific review

**Strengths.**
- Exact arithmetic throughout.
- A proved proposition, checked exhaustively.
- Isomorphism control.
- Frozen specs before the held-out and null analyses.
- The q161 target audit and the exact process-law decision.
- Honest negative results:
  - the A/B pair is ineligible;
  - Hassan's matched pair is isomorphic;
  - q220 is at chance.

**Problems that block coming off draft:**
1. **The structural target (B) depends on the convention** (`TARGET_AUDIT.md`). Narrative files written before
   the audit (`IDENTIFIABILITY_NOTE.md`, `SEARCH_RECORD.md`, parts of `paper.md` and `hypotheses.md`) still
   lead with "different q161 targets". The audit note is prepended or appended, but the main narrative should
   be rewritten around target A.
2. **No confirmatory evidence.** Everything is exploratory or pilot work.
3. **Baselines not run:** transfer entropy, SHREC (Gilpin 2025, the strongest competing approach), JRP/MdCRQA,
   false-pair surrogates.
4. **The PR description is stale.** It lists the bounded search, the literature review and the pilot as
   pending, but all are done.
5. **Novelty is narrow.** The competing interpretation, that this is a textbook consequence of pairwise
   blindness plus a target-definition artefact, is largely accepted in `literature/NOVELTY_MATRIX.md`.

## Recommendation

**Keep #842 as a draft.** Do not request review yet. A mergeable version would:
- retitle the study around target A (a pairwise recurrence identifiability limit with a proof for the affine
  class, plus measured q220 null FPRs);
- drop the IIT-bottleneck framing, or demote it to a convention-sensitivity note;
- update the PR description.

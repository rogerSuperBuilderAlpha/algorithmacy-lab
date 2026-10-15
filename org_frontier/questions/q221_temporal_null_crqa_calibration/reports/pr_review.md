# Self-review of draft PR #842 (2026-10-15)

## Scope and conventions

- **Base.** `rogerSuperBuilderAlpha:contrib` at `44f9b491`, which is an ancestor of the head.
- **Changed paths** (counts change as the draft evolves):
  - `org_frontier/questions/q221_temporal_null_crqa_calibration/**`;
  - the generated `README.md` and `MAP.md`;
  - `ci/reproduce.json`, where entries were inserted textually and the existing format is preserved.
- **Untouched:** q161, q220 and #841.
- **Generated indexes current:** `tools/build_index.py --check`, `tools/build_map.py --check`,
  `build_research_index.py --check` and `build_cards_index.py --check` all exit 0.
- **Large file: resolved.** `pair_search.json` (716 KB) is replaced by a deterministic 24 KB `.gz`, with a raw-content SHA-256 check and a restore command (`identifiability/results/PAIR_SEARCH_STORAGE.md`).

## Correctness checks run

| check | result |
|---|---|
| q221 fast tests (including Hassan's) | 21 pass, 3 skipped (the slow tier) |
| q221 expensive tier (`Q221_SLOW=1`) | 6 pass |
| q220 tests | 73 pass |
| `ci/reproduce.py --changed-file` | 14/14 pass |
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

**Status of earlier review items (updated 2026-10-15, round 2):**
1. **Target B depends on the convention.** The narrative is now led by target A: `paper.md` headline and
   title, `FINDINGS.md` heading, folder `README.md`. Hassan's original text is retained below the headline.
   The maintainer question is in `OPEN_QUESTION_FOR_MAINTAINER.md`.
2. **Comparators: done.** Spec `311a6477`. TE, JRP and SHREC separate the survivors. The MdRQA rate and
   false-pair q220 do not. CCM and TTS were not run.
3. **Large file: resolved.** See above.
4. **PR description:** replaced on 2026-10-15 with Hassan's approval. A comparator update is proposed in
   `/workspace/algorithmacy-q221-briefs/pr842_body_v2.md` but not applied.

**What still argues for keeping the PR as a draft:**
- **Confirmatory evidence is narrow.** It covers only the preregistered 4-node target-A study (family F4); everything else is exploratory or pilot work.
- **Novelty is narrow.** The competing interpretation, that this is a textbook consequence of pairwise
  blindness plus a target-definition artefact, is largely accepted in `literature/NOVELTY_MATRIX.md`.
- **The q161 convention question** is open with the maintainer.
- **Older narrative files** (`IDENTIFIABILITY_NOTE.md`, `SEARCH_RECORD.md`, Hassan's `hypotheses.md` and
  `methods.md`) still describe the earlier IIT-target framing. They carry audit notes but have not been
  rewritten. They are kept as a historical record.

## Recommendation

**Keep #842 as a draft.** The four-node target-A study is the only reported preregistered confirmatory component; its scope is one synthetic family. The q161 target-convention question remains undecided, and the broader IIT/organizational conclusions are not confirmed. These are scientific review questions, not packaging failures. A non-draft version would need the maintainer's answer
on the q161 convention and a decision on whether exploratory-only work is in scope for `contrib`.

## Round 3 update (2026-10-15): preregistered 4-node study

- **Preregistration:** `2ad11e69`, pushed before any study run. The scripts are frozen at `89118627` and
  `11d34a7c`.
- **H1 (exact):** 1,872 non-isomorphic orbit pairs.
- **H2:** supported; the R classifier is at chance.
- **H3:** all predictions met. C2 and C4 are unresolved.
- **Deviations:** D1–D3, none outcome-affecting.
- **Recommendation unchanged.** Keep #842 as a draft. The q161 convention question is still open with the
  maintainer, and the confirmatory scope is a single synthetic family.

# Q221 — Pairwise recurrence summaries do not identify the transition law of noisy Boolean networks

**Status: provisional draft.** Draft PR #842. Everything is exploratory **except** the preregistered 4-node study
of target A (`confirmatory_4node/`, prereg commit `2ad11e69`). That study's H2 and H3 are confirmatory within
their stated scope.

**Headline (target A).**
- **Claim:** population pairwise categorical recurrence summaries do not identify the multivariate transition
  law. The summaries are the marginals and the auto- and cross-match profiles at every lag.
- **Proof:** for invertible GF(2)-affine noisy networks (`THEORY.md`), checked exhaustively at n = 3.
- **Instances:** three non-isomorphic 3-node pairs from an exact screen of the lab's existing candidate space.
- **Not observationally equivalent:** the full and bivariate (X,Y) and (Y,H) laws differ, decided exactly.
- **What separates the pairs:** transfer entropy, joint recurrence and SHREC do. The MdRQA full-vector
  recurrence rate does not; it is exactly equal.
- **4-node study (preregistered).**
  - **Exact:** 1,872 non-isomorphic recurrence-equal, law-different orbit pairs among 322,560 four-node affine
    systems.
  - **Confirmatory:** the R classifier is at chance on 40 held-out pairs (TOST). Likelihood separates 40/40,
    TE 36/40 (population TE 25/40). MdRQA (8/40) and false-pair q220 (1/40) generally fail. JRR (23/40) and
    SHREC (28/40) were unresolved. A preregistered follow-up on 600 fresh pairs resolved both as **generally
    separates**: JR 347/600 [0.533, 0.623]; SHREC 363/600 [0.560, 0.649].
  - See `confirmatory_4node/RESULTS.md`.

**Other targets.**

| target | result |
|---|---|
| B: q161 bottleneck target | convention-dependent (`TARGET_AUDIT.md`, `OPEN_QUESTION_FOR_MAINTAINER.md`) |
| C: Φ / major complex | identical (negative) |
| D: q220 on held-out families | at chance (exploratory) |
| Temporal-null pilot | the shuffle null gives q220 prominence a false-positive rate of 27–43% under persistence |

**Where to read.**

| file | contents |
|---|---|
| `paper.md` | report |
| `FINDINGS.md` | evidence by category |
| `GATES.md` | gates A–H |
| `THEORY.md` | proofs |
| `protocol.md` | frozen specs |
| `confirmatory_4node/` | preregistration, deviations, results of the 4-node study |
| `MANIFEST.json` | hashes and versions |
| `results/checksums.sha256` | checksums |
| `TECHNICAL_REPORT.md`, `REVIEW_HANDOFF.md`, `independent_audit/` | Hassan's work |
| `reports/` | executor reports |

**Reproduce.** The bounded-search record is stored compressed; see
`identifiability/results/PAIR_SEARCH_STORAGE.md`.
```
pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration
Q221_SLOW=1 pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration/identifiability/test_invariants_extra.py
python ci/reproduce.py --changed-file <changed.txt>
```

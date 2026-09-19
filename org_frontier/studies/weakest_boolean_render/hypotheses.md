# weakest_boolean_render — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #13).** What is the **weakest Boolean
render** of a real coordination log that still recovers the conjunctive
Φ=n−1 signature V2 #45 found only under a forced hub — role counts
alone, activity thresholds, or institutional elicits?

**Already known (cited, not reopened).**
- V2 #45 `conjunctive_law_real_render/` —
  **LAW_ONLY_UNDER_STRONG_MODEL**: institutional OSS elicits and
  activity fits miss the scaling signature; forced `#116` hub on the
  same role counts recovers Φ=n−1 at n=3,4.
- Probe `#116`: conjunctive hub Φ=n−1 with full core.
- V2 #44 Wageman / #43 Thompson: pointers only.

**Gap.** #45 established that *some* strong model works and off-the-shelf
elicits/fits fail. #13 asks for the **weakest** recovering class among
the three named render families.

**Instrument.** Exact binary IIT-4.0 (stock pin). Major-complex Φ.
In-silico on committed `org_frontier/recurrence/` public OSS CSVs
(PyPhi / sklearn / k8s pipelines + weekly activity). No new scrapes.

**Signature (law at size n).** Φ ≈ n−1 (±1e−6) **and** |core|=n.
Scaling bar for a render class: signature at **n≥4**, or at **two**
distinct sizes.

**Weakness ladder (fixed order, weak→strong information).**

| class | render recipe | info used |
|---|---|---|
| A. role counts alone | n from public role schema / actor inventory; Boolean form from n only (identity, cycle-copy, k-of-n threshold, **conjunctive hub**) | cardinality n |
| B. activity thresholds | weekly activity CSVs → fit / threshold dynamics (no hub rewrite) | time series |
| C. institutional elicits | committed v9/v10/v11 governance Boolean forms | elicited rules |
| (ref) forced hub | `#116` `single_hub(n)` on role counts | counts + hub template |

**Datasets.** `recurrence/event_series`, `review_heavy`, `bot_merged`,
`real_series/activity_core.csv` (n=3), `activity_recent.csv` (n=4).

## H1 — institutional elicits miss the scaling bar

v9/v10/v11 as a class fail the scaling bar (same claim as #45 H1 null).

## H2 — activity-threshold / fit renders miss the scaling bar

Fitted activity and pure threshold (k-of-n) forms fail the scaling bar.

## H3 — role-count→hub recovers the scaling bar

`single_hub(n)` at n=3 and n=4 (counts only; no activity, no elicit)
shows the signature at both sizes.

## H4 — weaker role-count forms fail the scaling bar

Identity, cycle-copy, and k-of-n threshold forms built from n alone
fail the scaling bar (n=3 triad-match alone does not count).

## H5 — panel closed

H1–H4 resolve: the weakest recovering class is role-count→hub.

## Reading keys

- **ROLE_COUNTS_HUB_WEAKEST:** H1∧H2∧H3∧H4 — hub-from-counts is the
  weakest recovering render; activity and elicits fail; weaker
  count-only wirings fail scaling.
- **ACTIVITY_THRESH_WEAKEST:** activity class recovers; role-count
  forms without richer series fail.
- **ELICIT_WEAKEST:** institutional elicits recover; weaker classes fail.
- **NONE_RECOVER:** no class on the panel recovers the scaling bar.
- **CONTROLS_FAIL:** `#116` control fails.

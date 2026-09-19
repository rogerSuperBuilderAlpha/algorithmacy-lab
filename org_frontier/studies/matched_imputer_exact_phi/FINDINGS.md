# Topology-matched imputer under exact Φ — findings

**Verdict: MATCHED_RETAINS_COPY_RANKS.** Topology-matched imputers
**retain** native Φ under hide-party (hub exact=1.000 on hub triadics;
ring exact=1.000 on ring triadics) and beat mismatched priors on
magnitude, but they do **not** restore exact-Φ **ranking** on the
hub∪ring panel (matched AUC 0.551). **Copy-A** remains the ranking
screen that works (mediation 0.896). Matching is not a ranking fix.

In-silico; exact binary IIT-4.0 via `classify_rules`. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V4 #5. Extends V4 #4
`COPY_RESTORES_RING_FAILS` and V3 #15 `IMPUTER_RESTORES_AUC`.

**Validation gap.** Structural rule-swap is the exact-Φ analogue of
trajectory imputation on designed Boolean forms, not a field
missing-data model. Ring prior here is neighbor-AND (canonical ring
generative), distinct from V4 #4’s `C'=S` (≡ hub on mediation).

## Already known

| prior | result |
|---|---|
| V3 #15 | IMPUTER_RESTORES_AUC — ring restores MI; hub does not; copy-W also |
| V4 #4 | COPY_RESTORES_RING_FAILS — copy-W restores Φ; ring (`C'=S`) does not |
| V4 #1–#3 | exact-Φ joint / phase / zero-duty–retain |

## Panels

| panel | screen | AUC / rate |
|---|---|---:|
| mediation | Φ full | **1.000** |
| mediation | Φ copy-A | **0.896** |
| mediation | Φ ring (neighbor-AND) | 0.883 |
| mediation | Φ hub (`B'=M`) | 0.806 |
| hub∪ring | Φ full | **1.000** |
| hub∪ring | Φ matched | **0.551** |
| hub∪ring | Φ mismatched | 0.542 |
| hub∪ring | Φ copy-A | 0.630 |
| hub-native triadic | matched exact retention | **1.000** |
| hub-native triadic | mismatched exact | **0.000** |
| ring-native triadic | matched exact retention | **1.000** |
| ring-native triadic | mismatched exact | **0.000** |

Restore bar: AUC ≥ 0.85 or within 0.10 of full. Retention bar: exact
rate ≥ 0.95.

## Hypotheses

| H | result |
|---|---|
| H1 hub-matched retains hub triadics | **SUPPORTED** |
| H2 ring-matched retains ring triadics | **SUPPORTED** |
| H3 matched beats mismatched retention | **SUPPORTED** |
| H4 copy-A restores mediation ranking | **SUPPORTED** |
| H5 matched fails hub∪ring ranking | **SUPPORTED** |
| H6 full holds; const0 fails mediation | **SUPPORTED** |

## Reading

Knowing the topology and filling the hidden party with that topology’s
canonical update **preserves** Φ on native carriers (matched is
identity there) and destroys it under mismatch. That answers the
magnitude half of #5. It does not answer the ranking half: on the
pooled hub∪ring panel, matched AUC stays near chance (0.551), below
copy-A (0.630) and far below the restore bar. On mediation, copy-A
still restores ranking (0.896); hub fails (0.806); neighbor-AND ring
is soft (0.883). Practice: topology-matched completion is a retention
tool, not a substitute for the party-echo ranking screen that V4 #4
identified.

## Best next (V4)

**#6** — does V3 #14’s W+n → landmark rule survive when W is taken from
a fielded / survey-style instrument?

## Reproduce

```
python org_frontier/studies/matched_imputer_exact_phi/analyze_matched.py
```

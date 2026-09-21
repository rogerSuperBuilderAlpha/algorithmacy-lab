# Anti-correlated duty on logged structure — findings

**Verdict: CLIFF_RECREATES_ON_LOGGED.** Anti-correlated (never-joint)
party admission recreates the exact-Φ joint-observation cliff on the
lab’s logged-structure panel (phi_full 1.000 → phi_alt **0.591**).
Synthetic multifamily still cliffs as in V4 #1 (1.000 → **0.660**).
Logged wiring does **not** soften the cliff; if anything the logged
panel drops further.

In-silico; exact binary IIT-4.0 via `classify_rules`. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V4 #7. Extends V4 #1
`TRANSFER_PARTIAL_EXACT_PHI` and V3 #16 `ALTERNATION_RECREATES_CLIFF`
from designed multifamily onto committed OSS Boolean renders.

**Validation gap.** The logged panel is Boolean forms whose size or
wiring comes from committed recurrence OSS renders (institutional
elicits, activity fits, public role counts) — not a live collaboration
graph crawl, and not measured Φ on real organizations. The alt screen
is an induced-subsystem score (mean Φ on mediator–party pairs), same
as V4 #1.

## Already known

| prior | result |
|---|---|
| V3 #16 correlated party duty | ALTERNATION_RECREATES_CLIFF — MI alt ≈ chance; phase holds |
| V4 #1 joint-obs exact Φ | TRANSFER_PARTIAL_EXACT_PHI — multifamily phi_alt 1.000→0.660 |
| V4 #2 / #3 | PHASE_RESTORES_JOINT; RETAIN_FAILS_WITH_ZERO |
| V3 #13 / V2 #45 | OSS role counts + elicits + activity fits = logged renders |

## Panel AUCs

| panel | screen | AUC |
|---|---|---:|
| multifamily (synthetic) | phi_full | **1.000** |
| multifamily (synthetic) | phi_alt | **0.660** |
| logged structure | phi_full | **1.000** |
| logged structure | phi_alt | **0.591** |

Cliff: AUC < 0.70 or drop ≥ 0.20 from phi_full. Hold: AUC ≥ 0.85.
Logged panel: 15 forms (11 triadic / 4 dyadic) — institutional v9/v10/v11,
activity fits, role-count templates at n∈{3,4}.

## Hypotheses

| H | result |
|---|---|
| H1 multi alt cliffs (#1 control) | **SUPPORTED** |
| H2 multi full holds | **SUPPORTED** |
| H3 logged alt cliffs (recreates) | **SUPPORTED** |
| H4 logged full holds | **SUPPORTED** |
| H5 phase ≡ full both panels | **SUPPORTED** |

## Reading

The joint-observation failure mode is not an artifact of the designed
multifamily catalog. On the lab’s closest logged-structure panel —
institutional OSS elicits, activity-fitted Boolean models, and
role-count templates at public role cardinalities — exact-Φ ranking
under anti-correlated party admission still cliffs (1.000→0.591), at
least as hard as synthetic multifamily (→0.660). Institutional triadics
collapse to alt=0 under the mediator–party split; only k-of-n=1
templates retain residual pair Φ. Practice: do not treat “both parties
logged half the time” as safe on logged graphs either — if their duty
cycles never co-occur, the exact-Φ screen fails the same way as on
synthetic forms.

## Best next (V4)

**#8** answered (`SCALE_BLOCKS_EXACT_PHI`). **#9** — does V3 #10’s
parity-hub law Φ=2^(2−n) continue for **n>8**?

## Reproduce

```
python org_frontier/studies/logged_alt_duty_exact_phi/analyze_logged.py
```

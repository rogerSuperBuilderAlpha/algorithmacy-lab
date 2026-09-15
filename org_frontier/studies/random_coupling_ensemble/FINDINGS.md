# Random coupling ensemble — findings

**Verdict: DISCRETE_LANDMARKS.** Across 224 random conjunctive couplings at
n=4 (ER / fixed-k / WS / BA-style), **every** core Φ lands on the discrete
atoms {2, 4, 6, 12} from the ring–pool / #19 landmark set — **no continuous
fill** of the gap. Triadic rate **tracks the generator** (sparse ER low →
fixed_k=2 high → fixed_k=3 = pool at 100%). WS shows higher clustering than ER
as a structural descriptor; that does **not** invent a new Φ law.

In-silico; binary exact IIT-4.0; primary n=4 N=32/ensemble; n=5 follow-on
N=92 (see below). Hypotheses fixed in `hypotheses.md` / `hypotheses_n5.md`.
Extends `interior_ring_pool` (#19); cites q147 (different axis: random
truth-tables). Ternary / residual-cascade noted only.

## Already known

| prior | result |
|---|---|
| #19 interior ring–pool | discrete Φ steps; no log/√n law |
| q147 random truth-tables | cycle density → triadicity; not this sampling |
| q146 / #17 small-world | WS from ring collapses / PICK_ONE |

## Distribution (n=4, 224 samples)

| Φ atom | count | share | note |
|---:|---:|---:|---|
| 2.0 | 137 | 61% | local / chain-like complex |
| 6.0 | 44 | 20% | #19 interior atom (only between-band value) |
| 12.0 | 32 | 14% | pool (all from fixed_k=3) |
| 4.0 | 11 | 5% | ring atom |
| other | **0** | **0%** | — |

**on_landmark = 1.000.** Between (4, 12): only 6.0.

## Triadic rate by ensemble

| ensemble | triadic rate | Φ mass |
|---|---:|---|
| ER p=0.3 | 0.375 | all at 2.0 |
| ER p=0.5 | 0.500 | 2.0 + rare 6.0 |
| fixed_k=2 | 0.875 | 2 / 4 / 6 |
| fixed_k=3 | **1.000** | all **12** (= pool) |
| WS p=0.25 | 0.938 | 2 / 4 / 6 |
| WS p=0.5 | 0.844 | 2 / 4 / 6 |
| BA m=2 | **0.000** | all 6.0 (local complex; whole dyadic) |

Thin n=5 fixed_k=2 (N=8): on_landmark=1.0; Φ all at 2.0; tri=0.75.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 control + ring/pool poles | **SUPPORTED** |
| H2 Φ ≥90% on landmarks | **SUPPORTED** (100%) |
| H3 triadic ER < k2 < k3 | **SUPPORTED** |
| H4 between-band only atom 6 | **SUPPORTED** |
| H5 WS clustering > ER | **SUPPORTED** (0.76 > 0.58) |

## Reading

**Match a standard network ensemble as a Φ law?** No. Generators differ in
**triadic rate** and **clustering** (WS vs ER descriptor holds), but they
share the same **Φ atoms**. Random coupling does not paint a continuous
spectrum between ring and pool; it resamplees the discrete steps #19 already
named.

**BA note.** Preferential-attachment AND graphs at n=4 are always dyadic at
the whole-system cut while leaving a Φ=6 major complex — landmark mass without
triadicity.

**vs q147.** Random truth-tables vary the Boolean *functions*; this study
fixes AND and varies the *wiring*. Both are in-silico; they answer different
questions.

## n=5 follow-on (N=92)

**Verdict: PARTIAL_N5.** Discrete landmarks **mostly** hold (≥90% on
L5={2,3,4,6,8,12,20}), but **new atoms appear**: Φ=**5.0** (3×) and Φ=**9.0**
(1×), all from `fixed_k=3`. H1 SUPPORTED; H2 SUPPORTED; H4 REFUTED (between-band
not only {6,8,12}).

| Φ | count | in L5? |
|---:|---:|---|
| 2.0 | 55 | yes |
| 6.0 | 30 | yes |
| 4.0 | 3 | yes |
| **5.0** | **3** | **no** |
| **9.0** | **1** | **no** (known at n=6 chord, not in fixed L5) |

| ensemble | N | triadic | note |
|---|---:|---:|---|
| ER p=0.4 | 20 | 0.450 | 2 / 6 |
| fixed_k=2 | 20 | 0.850 | 2 / 4 |
| fixed_k=3 | 16 | 1.000 | 6 / **5** / **9** |
| WS p=0.3 | 20 | 0.950 | 2 / 4 |
| BA m=2 | 16 | 0.000 | all 6 |

Triadic rate still tracks generator (ER < k2). Denser fixed_k=3 is where the
new atoms show — the n=4 “only {2,4,6,12}” picture is **not** exact at n=5.

### n=5 hypotheses

| hypothesis | result |
|---|---|
| H1 ≥90% on L5 + poles | **SUPPORTED** (0.957) |
| H2 new Φ values appear | **SUPPORTED** (5, 9) |
| H3 triadic ER < fixed_k2 | **SUPPORTED** |
| H4 between-band ⊆ {6,8,12} | **REFUTED** |

## Limits

n=4 primary N=32/ensemble; n=5 N=92 (~9 min). Conjunctive AND only. No
organization measured.

## Best next experiment

**Expand L5 / denser n=5 fixed_k** to map whether 5 and 9 are stable new atoms
or rare — or **#42 scale blur** of HMC/CMC discriminants. Ternary IIT-4.0
tooling remains blocked.

## Reproduce

```
python org_frontier/studies/random_coupling_ensemble/analyze_ensemble.py
python org_frontier/studies/random_coupling_ensemble/analyze_ensemble_n5.py
```
(~3.5 min n=4; ~9 min n=5)

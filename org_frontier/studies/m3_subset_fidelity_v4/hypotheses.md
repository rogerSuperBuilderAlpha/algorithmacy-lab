# m3_subset_fidelity_v4 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #12).** Does **M3 subset-Φ fidelity**
on `third_party/pyphi_iit4_mv` change any V4 #1–#3 verdict, or is
exact binary Φ already decisive?

**Already known (cited, not reopened).**
- V4 #1 `joint_obs_cliff_exact_phi/` — **TRANSFER_PARTIAL_EXACT_PHI**.
  family_n3 seed 41: phi_full 1.000, phi_alt 0.812, phi_zero 0.792.
  multifamily: phi_full 1.000, phi_alt 0.660.
- V4 #2 `phase_lock_exact_phi/` — **PHASE_RESTORES_JOINT**.
  multifamily phi_alt 0.660, phi_phase = phi_full = 1.000.
  family_n3 seed 42: phi_phase 1.000. MI and duty are cited controls.
- V4 #3 `zero_duty_retain_exact_phi/` — **RETAIN_FAILS_WITH_ZERO**.
  multifamily: phi_full 1.000, phi_zero 0.592, phi_retain 0.592,
  phi_omit_M 0.559. family_n3 seed 43: phi_full 1.000, phi_zero 0.750,
  phi_retain 0.750.
- Overlay M2 matches stock full-system Φ=2 on the faithful triad.
  Overlay proper-subset Φ is recorded as inflated on binary XOR dyads
  (`BEYOND_BINARY_ARC.md`, `PR739_PACKAGE.md`,
  `parity_radix_blindspot/`). That caveat is the M3 object. V4 #11 is
  out of scope.

**Scope.** In-silico. Exact IIT-4.0 on the same Boolean forms as
#1–#3 (n≤4). Evidence about those models. No claim about a firm.

## Universe

Same constructors as V4 #1 (`analyze_transfer.py`):
`build_family_n3` and `build_multifamily`. Roles `(A, M, B)` from
`roles_for`. Family samples use the seeds those cells already used:

| cell | family seed | multifamily |
|---|---|---|
| #1 | 41 | deterministic constructor |
| #2 | 42 | same constructor |
| #3 | 43 | same constructor |

Labels stay the stock full-form structure bit (`triadic`), not an
overlay relabeling.

## Two estimands

Keep-sets, per form: **full** (all nodes); **MA** = `(M, A)`;
**MB** = `(M, B)`; **zero** = `V \ {B}`; **omit** = `V \ {M}`.

1. **Induced (I).** The published screen. Omitted nodes are clamped
   at 0 and the smaller Boolean system is scored
   (`induce` + max Φ over its reachable states). Stock engine:
   `classify_rules`. Overlay engine: `MultivaluedNetwork` on that
   induced SBS, `sia` at each reachable state, max Φ.
2. **Background subset (S).** Proper-subset Φ inside the full
   network. External nodes stay at the current full-system state
   (probe 56 / `pyphi.Subsystem(nodes=keep)`). Stock engine:
   `new_big_phi.sia`. Overlay engine: `MultivaluedSubsystem` +
   `sia_mv.sia`. Score = max over reachable states of the **full**
   system. On `keep = full` the two estimands are the same system.

Screens, both estimands, both engines:

- `phi_full` = Φ(full)
- `phi_MA`, `phi_MB` = Φ of those pairs
- `phi_alt` = mean of `phi_MA` and `phi_MB`
- `phi_phase` = `phi_full` (published identity; joint slots admit
  the full form)
- `phi_zero` = Φ(zero); `phi_retain` = Φ(MA); `phi_omit` = Φ(omit)

Agreement tolerance: absolute gap ≤ **1e-6**. A state that raises
`StateUnreachableError` is skipped. If every state on a keep-set
fails, that score is non-finite.

## Bars (copied from #1–#3)

Hold: AUC ≥ **0.85** or within **0.10** of that screen’s `phi_full`.
Cliff: AUC < **0.70** or drop from `phi_full` ≥ **0.20** (non-finite
counts as a cliff when `phi_full` itself holds). AUC is **oriented**
ROC-AUC, the same `oriented_auc` as #1.

MI (#1 H1, #2 H4) and the duty match (#2 H5) are **cited as
holding**. They are not subset-Φ and are not recomputed.

## Reading-key replay

**#1.** `h_mi` cited true. `h2` = cliff(`phi_alt` family, `phi_full`
family) and family `phi_full` ≥ 0.85. `h3` = cliff(`phi_alt`
multifamily, `phi_full` multifamily). `h4` = both `phi_full` ≥ 0.85.

- ¬`h_mi` or ¬`h4` → `CONTROLS_FAIL`
- `h2` ∧ `h3` ∧ `h4` → `TRANSFER_HOLDS_EXACT_PHI`
- ¬`h2` ∧ `h3` ∧ `h4` → `TRANSFER_PARTIAL_EXACT_PHI`
- ¬`h2` ∧ ¬`h3` ∧ `h4` → `EXACT_PHI_ROBUST_MI_ONLY`
- `h2` ∧ ¬`h3` ∧ `h4` → `FAMILY_N3_ONLY`
- else → `UNCLASSIFIED`

**#2.** `h1` = cliff(multifamily `phi_alt`, multifamily `phi_full`).
`h2` = hold(`phi_phase`, `phi_full`) with `phi_phase := phi_full`.
`h5` cited true. Under that identity, `h2` is true whenever
`phi_full` is finite.

- ¬`h1` → `NO_ALT_CLIFF`
- `h1` ∧ ¬`h2` → `PHASE_FAILS_EXACT_PHI`
- `h1` ∧ `h2` ∧ `h5` → `PHASE_RESTORES_JOINT`
- else → `UNCLASSIFIED`

**#3.** `h1` = cliff(multifamily zero, multifamily full). `h2` =
hold(multifamily retain, multifamily full). `h5` = both full AUCs
≥ 0.85 and, on that cell’s family sample, `|phi_zero − phi_retain|
< 1e-9` on every form.

- ¬`h5` → `CONTROLS_FAIL`
- ¬`h1` → `ZERO_DUTY_SOFT`
- `h1` ∧ `h2` → `RETAIN_SAVES_ZERO_DUTY`
- `h1` ∧ ¬`h2` → `RETAIN_FAILS_WITH_ZERO`

Published targets: #1 `TRANSFER_PARTIAL_EXACT_PHI`; #2
`PHASE_RESTORES_JOINT`; #3 `RETAIN_FAILS_WITH_ZERO`.

## Anchor check (stock induced only)

Recomputed stock-induced oriented AUCs must sit within **0.010** of
the published anchors listed above. Anchors used:

- #1 family seed 41: full 1.000, alt 0.812, zero 0.792; multifamily
  full 1.000, alt 0.660.
- #2: multifamily full 1.000, alt 0.660, phase 1.000; family seed 42
  phase 1.000.
- #3: multifamily full 1.000, zero 0.592, retain 0.592, omit 0.559;
  family seed 43 full 1.000, zero 0.750, retain 0.750.

## Witnesses (fixed forms)

**W_xor.** n=2, `A' = A XOR B`, `B' = A XOR B`. No external nodes, so
I and S coincide. Inflation = overlay max Φ − stock max Φ.

**W_parity.** n=3, `W' = S`, `S' = W XOR C`, `C' = S`. Report stock
and overlay max Φ on each size-2 background subset. Descriptive; not
a reading key.

## H1 — stock replay recovers #1–#3

On estimand I, stock engine, each cell’s reading key equals its
published key, and every anchor above is within 0.010. Null: any key
misses or any anchor misses. A miss here is a harness failure
(`REIMPLEMENT_FAIL`), not an overlay result.

## H2 — overlay subset Φ matches stock

On estimand S, for every decision keep-set of every form in the three
family samples and the multifamily panel, `|Φ_overlay − Φ_stock| ≤
1e-6` and both are finite. Null: any larger gap or a one-sided
non-finite score.

## H3 — XOR-dyad inflation reproduces

On W_xor, overlay max Φ exceeds stock max Φ by ≥ **0.1**. Null:
overlay does not exceed stock by 0.1.

## H4 — induced replay does not move a key

On estimand I, each cell’s overlay reading key equals that cell’s
stock reading key. Null: any cell differs.

## H5 — subset replay does not move a key

On estimand S, each cell’s overlay reading key equals that cell’s
stock reading key. Null: any cell differs.

A stock-subset key that differs from the published induced key is an
**estimand shift**. Record it. It does not by itself select
`M3_FLIPS_VERDICT`. Fidelity is overlay versus stock on one estimand.

## Incomplete screens

A decision screen is incomplete when any form has a finite stock score
and a non-finite overlay score on a keep-set that enters that screen.
Incomplete screens select `M3_BLOCKED`. They are not fed through the
flip rule.

## Reading keys (this study)

Precedence: `M3_BLOCKED` > `REIMPLEMENT_FAIL` > `M3_FLIPS_VERDICT` >
`EXACT_BINARY_DECISIVE`.

- **M3_BLOCKED:** the overlay errors out of the decision keep-sets, or
  a decision screen is incomplete. Partial AUCs may be printed. Missing
  AUCs are not filled in.
- **REIMPLEMENT_FAIL:** ¬H1.
- **M3_FLIPS_VERDICT:** H1, and (¬H4 or ¬H5).
- **EXACT_BINARY_DECISIVE:** H1 ∧ H4 ∧ H5. H2 and H3 may go either
  way. Exact binary Φ already decides #1–#3: neither overlay engine
  moves a reading key on its estimand.

## Instrument gate

Before any panel number is trusted: stock faithful triad
(`W'=S`, `S'=W∧C`, `C'=S`) reads triadic at Φ=2, and overlay max Φ
on that same form is within 1e-6 of 2. Failure aborts. No verdict.

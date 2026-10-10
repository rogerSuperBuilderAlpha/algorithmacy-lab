# graded_channel_exact_phi — hypotheses (fixed before computing)

**Question (Ergodicity × not reopened; V4 agenda #11, strand E).** The exact-Φ
joint-observation arc ran on hard binary observation masks: V4 #1
(`studies/joint_obs_cliff_exact_phi/`, TRANSFER_PARTIAL_EXACT_PHI) found the
party-mediator pair screen collapse when W and C are never jointly observed;
V4 #2 (`studies/phase_lock_exact_phi/`, PHASE_RESTORES_JOINT) found that
phase-locked duty — parties in duty together half the time — restores the
screen at matched mean duty δ=0.5; V4 #7
(`studies/logged_alt_duty_exact_phi/`, CLIFF_RECREATES_ON_LOGGED) found the
cliff recreate on logged structure. Question #11 asks whether that cliff
survives a **graded channel**: the mediating system reads each party through a
lossy channel, correct with probability q and otherwise returning the default
value 0, while party duty stays perfectly correlated (both always in duty).
Does the Φ screen hold under channel degradation, or does degradation cliff
like anti-correlated duty?

**Already known (cited, not reopened).**
- V4 #1 TRANSFER_PARTIAL_EXACT_PHI: multifamily full Φ=1.000, alternation
  cliffs to 0.660; logged full 1.000, alt 0.591. HOLD_AUC=0.85, HOLD_GAP=0.10,
  CLIFF_AUC=0.70, CLIFF_DROP=0.20 inherited.
- V4 #2 PHASE_RESTORES_JOINT: at matched δ=0.5, phase-locked duty restores
  the multifamily screen (1.000) where alternation cliffs (0.660); joint
  observation, not mean duty, carries the screen.
- `studies/commit_noise_phase/` SMOOTH_DECAY: node-level flip noise on
  conjunctive and parity hubs gives smooth Φ decay with no verdict flip. That
  cell degrades commitment, not the party-to-mediator channel; this cell does
  not reopen it.

**Construction (fixed).** For a form with rules, node set {W, S, C} at n=3
(roles family-dependent per V4 #1 `roles_for`; at n=4 the mediator is node 0),
the graded channel acts on the two party→mediator edges only: with probability
1−q the mediator's next value is computed with both party reads replaced by
the default 0. The mixed TPM row is q·full_row + (1−q)·garbled_row; both
component maps are deterministic, so the mixture is a proper stochastic TPM.
Party outputs (W' = f_W, C' = f_C) are never garbled. q=1 recovers the
deterministic full form; q=0 is a hard mechanism-side omit of both party reads.
Whole-form Φ is exact binary IIT-4.0 via `max_phi_float` (max over reachable
states), the same engine the foundations arc uses for stochastic TPMs.

**Panel (frozen before computing).** The V4 #1 multifamily synthetic panel
(24 forms, chain/pool/hub/or_hub/parity/broadcast/majority/ring/two_hub at
n=3,4 plus the n=3 mediation enumeration) and the V4 #7 logged panel (15
forms: 3 institutional, 2 activity fits, 10 role-count, 11 triadic / 4 dyadic).
Whole-form triadic labels from `classify_rules`, confirmed at run time.

**Instrument gate.** Faithful memoryless triad (S = W ∧ C) whole-form triadic
Φ=2.000; sticky whole-form dyadic. Abort the comparison if either gate fails.

**Screen and rules.** Per form, the score is whole-form Φ under the channel.
Panel AUC against the triadic label, oriented per V4 #1 `oriented_auc`. Holds:
AUC ≥ 0.85 or within 0.10 of the q=1 reference. Cliffs: AUC < 0.70 or drop
≥ 0.20 from the q=1 reference.

## H1 — controls replicate the arc anchors

Instrument gate passes; multifamily and logged q=1 AUCs hold (≥0.85);
multifamily alternation-cliff and logged-cliff anchors stay in their prior
bands (alternation AUC < 0.70 or drop ≥ 0.20). Controls failing abort with
CONTROLS_FAIL.

## H2 — graded channel holds at correlated duty

At q=0.5 symmetric graded channel, multifamily AUC holds relative to the q=1
reference.

Null: cliffs like anti-correlated duty at the same 0.5 duty.

## H3 — graded degradation is smooth

Multifamily AUC is monotone non-increasing along q = 1.0 → 0.75 → 0.5 → 0.25;
no interior condition cliffs (every q>0 holds, or the single failure is at the
q=0 endpoint, which is a known mechanism-side omit, not a graded interior).

Null: an interior q cliffs while a milder q holds.

## H4 — grading beats hard alternation at matched duty

At q=0.5 (mean party information 0.5, matching the δ=0.5 alternation and phase
conditions), the graded AUC exceeds the V4 #1 alternation AUC by ≥ 0.10 on
the multifamily panel.

Null: no lift; graded q=0.5 performs like hard alternation.

## H5 — the logged panel replicates the multifamily result

The logged panel reproduces the H2/H3/H4 signed conclusions. This is the
arc's standing logging discipline (V4 #7); a logged-panel divergence is
reported, not smoothed.

**Primary verdict word.**
- H1 and H2 hold with H3 → `GRADED_HOLDS` (the cliff is a duty-correlation
  artifact; channel quality does not carry it in this family)
- H1 and H2 hold but H3 fails → `GRADED_HOLDS_ROUGH`
- H1 holds, H2 fails, q=0.5 ≥ alternation + 0.10 → `GRADED_PARTIAL`
- H1 holds, H2 fails, q=0.5 within the alternation band → `GRADED_CLIFFS`
- H1 fails → `CONTROLS_FAIL`

**Scope.** Exact binary IIT-4.0; designed Boolean forms; a default-zero garbling
channel. In-silico. Evidence about models, not about real organizations. No
numbers until `analyze_graded.py` exists, is committed after this file, and is
run.

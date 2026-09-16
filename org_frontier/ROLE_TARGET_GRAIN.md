# Role-target grain — working picture

A short synthesis of the role-target arm on the omit-atom thread
(PR #739). Exact binary IIT-4.0 Φ; in-silico. Parent arc:
[`OMIT_ATOM_ARC.md`](OMIT_ATOM_ARC.md). Residual / cascade / ternary
noted only.

## Verdict in one line

**Role-target grain generalizes.** Which role’s omit targets purify a
mixed indeg is **fingerprint-morphic**. Joint fingerprints need the
right role cut — not irreducible multi-role fog.

## Three laws

| indeg | study | verdict | purifying grain |
|---|---|---|---|
| `(0,0,1,1,2,2)` | [`indeg_002122_grain/`](studies/indeg_002122_grain/) | **ROLE_TARGETS_LAW** | **hubs / t_targets**: `(1,1)→Φ=12`; on `(3,)`, **z_targets=(2,2)→Φ=8**; else Φ=6 |
| `(0,0,1,1,1,3)` | [`indeg_001113_grain/`](studies/indeg_001113_grain/) | **Z_TARGETS_LAW** | **zeros / z_targets**: `(1,1)→Φ=6`; `(3,)→Φ=6`; else Φ=12. **t_targets constant** |
| `(0,0,0,1,2,3)` | [`indeg_000123_grain/`](studies/indeg_000123_grain/) | **JOINT_TZ_LAW** | **both t and z vary**; `(tt,zt)=((2,),(1,2,3))→Φ=6` else Φ=12; **t alone insufficient**; **z-cut sufficient** |

Already-pure under cycle type alone: `(0,1,1,1,1,2)` —
[`same_indeg_band_n6/`](studies/same_indeg_band_n6/) BAND_DISCRIMINANT
(no role-target needed).

## Working picture

1. **Cycle type is sometimes too coarse.** On dual-hub and triple-hub
   fingerprints, a (cycles, recip) class can mix discrete Φ until omit
   **targets of a role class** (hubs or zeros) are fixed.

2. **The purifying role morphs with the fingerprint.** Dual omitted-hubs
   `(0,0,1,1,2,2)` need hub targets (and zero targets on 3-cycles).
   Single triple-hub `(0,0,1,1,1,3)` has constant t_targets — zeros
   purify. When **both** roles have degrees of freedom
   `(0,0,0,1,2,3)`, joint `(tt×zt)` subtypes are pure; the predictive
   cut can collapse to z, but t alone would mis-read the `tt=(2,)`
   slice.

3. **Not a continuum; not irreducible mix.** Within a joint role-target
   subtype, uniformity samples stay Φ-pure. Softness is across grains,
   not inside them — same discreteness lesson as the omit-atom arc, at
   finer motif resolution.

4. **Scope.** Conjunctive AND; n=6 fixed_k=4; dense subtype samples.
   Construct / encoding ladder arm is separate (see
   [`encoding_ladder_n5/`](studies/encoding_ladder_n5/),
   [`hmc_algo_boundary/`](studies/hmc_algo_boundary/)).

## Best next

CMC / AI-MC ladders done:
[`construct_ladders_n5/`](studies/construct_ladders_n5/) BOUNDARY_TRANSFERS.
Next: another multi-role indeg, or n=6 construct ladders. Skip residual /
cascade / ternary unless tooling lands.

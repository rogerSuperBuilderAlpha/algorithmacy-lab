# indeg_000123_grain — hypotheses (fixed before computing)

**Question.** On indeg **(0,0,0,1,2,3)** — where **both** t_targets and
z_targets vary — does a joint role-target law still yield pure Φ classes,
or does multi-role interaction create irreducible mix?

**Already known.**
- `indeg_002122_grain` ROLE_TARGETS_LAW: (0,0,1,1,2,2) — hubs
  (t_targets) purify; z_targets needed on (3,).
- `indeg_001113_grain` Z_TARGETS_LAW: (0,0,1,1,1,3) — t_targets
  constant; zeros (z_targets) purify.
- Exploratory catalog/smoke on (0,0,0,1,2,3) (pre-registered here):
  t_targets ∈ {(1,),(2,)}; z_targets ∈ {(1,2,3),(1,3,3),(2,2,3),
  (2,3,3),(3,3,3)}. Cycle ((2,),1) mixes Φ=6/12 across joint subtypes;
  smoke suggests Φ=6 iff (tt,zt)=((2,),(1,2,3)), else Φ=12.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6 fixed_k=4.
Roles: Z×3 (indeg 0), O×1 (indeg 1), M×1 (indeg 2), T×1 (indeg 3).
Subpartition by (cycles, recip, t_targets, z_targets). Dense N_U;
candid ~45 s/cell.

**Proposed joint law.**
```
(t_targets, z_targets) = ((2,), (1, 2, 3))  → Φ=6,  n_core=3
else                                       → Φ=12, n_core=4
```
(Equivalently: z_targets=(1,2,3)→6, which only co-occurs with tt=(2,).)

## H1 — joint (tt,zt) subtypes are Φ-pure

Every tested (cycles, recip, t_targets, z_targets) subtype is Φ-pure and
matches the proposed law. Null: some subtype mixes, or misses the law.

## H2 — t_targets alone is insufficient

Under t_targets=(2,), both Φ=6 and Φ=12 appear (depending on z_targets).
Null: tt=(2,) is already pure without z.

## H3 — z_targets alone matches the cut

z_targets=(1,2,3) ⇒ Φ=6; every other observed z_targets ⇒ Φ=12.
Null: some other z yields Φ=6, or (1,2,3) yields Φ=12.

## H4 — cycle alone is insufficient

Class ((2,),1) contains both Φ=6 and Φ=12 subtypes. Null: cycle type
already pure.

## H5 — multi-role grain generalizes (no irreducible mix)

Joint role-target grain dissolves mix on this fingerprint (H1∧H2∧H4).
Compared to priors: both roles have degrees of freedom (unlike 001113);
neither role alone is the full story without checking the other for the
t-slice (H2), while the z-cut is sufficient for prediction (H3). Null:
MIX persists after (tt×zt) grain.

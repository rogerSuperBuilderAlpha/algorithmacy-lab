# indeg_001113_grain — hypotheses (fixed before computing)

**Question.** On a new indeg fingerprint **(0,0,1,1,1,3)** (not
(0,0,1,1,2,2) and not the pure (0,1,1,1,1,2) band), does role-target
grain dissolve mix / yield a pure law analogous to ROLE_TARGETS_LAW?

**Already known.**
- `same_indeg_band_n6`: indeg (0,1,1,1,1,2) pure under cycle type (8 vs 9).
- `indeg_002122_grain` ROLE_TARGETS_LAW: indeg (0,0,1,1,2,2) —
  t_targets=(1,1)→Φ=12; (3,)+z_targets=(2,2)→Φ=8; else→6.
- Exploratory smoke on (0,0,1,1,1,3) (pre-registered here): t_targets is
  **constant** (1,) — uninformative. Cycle class ((2,),1) **mixes**
  Φ=6/12 until split by **z_targets**: (1,1)→6 (n_core=3);
  (1,3)→12 (n_core=4). Classes (3,)→6; (2,2)/(4,)→12 in smoke.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6 fixed_k=4.
Roles: Z×2 (indeg 0), O×3 (indeg 1), T×1 (indeg 3). Dense N_U per
subtype; candid ~45–75 s/cell.

**Proposed law.**
```
z_targets=(1,1)  → Φ=6, n_core=3     (only in cycle (2,))
cycles=(3,)      → Φ=6, n_core=3
else             → Φ=12, n_core=4
```

## H1 — z_targets dissolves the (2,) mix

In ((2,),1): every tested form with z_targets=(1,1) has Φ=6, n_core=3;
every tested form with z_targets=(1,3) has Φ=12, n_core=4. Null:
counterexample either way.

## H2 — (3,) stays Φ=6

Class ((3,),0) (only z_targets=(1,3) available) yields Φ=6, n_core=3.
Null: Φ=12 appears.

## H3 — (2,2) and (4,) stay Φ=12

Classes ((2,2),2) and ((4,),0) (z_targets=(3,3)) yield Φ=12, n_core=4.
Null: Φ=6 or mix.

## H4 — subtypes pure / MIX dissolved

All tested (cycles, recip, z_targets) subtypes are Φ-pure. Null: some
subtype still mixes.

## H5 — role-target grain generalizes (not t_targets clone)

t_targets is constant on this fingerprint; the purifying grain is
**z_targets** (zeros’ omit targets). Role-target grain still dissolves
mix, but the operative role morphs vs ROLE_TARGETS_LAW. Null: no pure
role-target law (irreducible mix), or t_targets alone would have
sufficed (it does not — it is constant).

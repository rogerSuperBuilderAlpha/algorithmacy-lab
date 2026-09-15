# indeg_002122_grain — hypotheses (fixed before computing)

**Question.** Within MIX indeg **(0,0,1,1,2,2)** at n=6 fixed_k=4, what
finer grain separates Φ=6 (full-core) from Φ=12 (n_core=4)? Is there a pure
discriminant, or an honest irreducible mix?

**Already known (`indeg_002122_n6` MIX).**
- Cycle classes ((2,2),2) and ((4,),0) mix Φ=6/12; ((2,),1) and ((3,),0)
  looked pure Φ=6 at N_U=3.
- Role partition of omit-indeg: Z×2 (never omitted), O×2 (once), T×2
  (twice = hubs).
- Exploratory feature hunt (pre-registered here, not the registered Φ run):
  **t_targets** = sorted omit-indegrees of the two T-hubs’ omit targets.
  Known witnesses: Φ=12 had t_targets=(1,1); Φ=6 had (2,2) or (1,2).
- Ternary / residual noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6 fixed_k=4.
Sub-partition mixed classes (and the (2,) (1,1) slice) by t_targets.
Dense N_U per subtype; candid ~45s/cell.

## H1 — t_targets=(1,1) ⇒ Φ=12 in mixed cycle classes

In classes ((2,2),2) and ((4,),0), every tested form with t_targets=(1,1)
has core Φ=12 and n_core=4; every tested form with t_targets≠(1,1) has
Φ=6 and n_core=6. Null: some counterexample in either direction.

## H2 — law extends to cycle class ((2,),1)

In ((2,),1), which also has a t_targets=(1,1) subclass (size 360), those
forms also yield Φ=12 (n_core=4). Null: (2,) forms with t_targets=(1,1)
stay Φ=6 (law cycle-restricted).

## H3 — ((3,),0) stays flat Φ=6

Class ((3,),0) has only t_targets=(1,2); tested forms all Φ=6 full-core.
Null: Φ=12 appears.

## H4 — pure discriminant (not irreducible mix)

H1 holds (and H3 holds): the MIX dissolves into a pure t_targets law on the
previously impure classes. Null: even after t_targets split, some subtype
still mixes Φ.

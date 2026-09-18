# shared_mediator_ternary — hypotheses (fixed before computing)

**Question.** Does the shared-mediator AND merger from `two_triad_shared_member`
(five-node major complex, Φ=4.0, binary IIT-4.0) survive when nodes take a
**ternary** alphabet {0,1,2}?

**Already known.** Shared-mediator AND merges under binary exact IIT-4.0; shared
worker/counterpart do not (`two_triad_shared_member/`). Residual/cascade arc
closed (`foundations/RESIDUAL_AND_CASCADE.md`); not reopened.

**Primary lift (min-AND).** Honest graded conjunction: on {0,1,2},
`min(a,b)` extends binary AND (`min` on {0,1} = `∧`). Architecture
`(W1,C1,W2,C2,S)`:

- `W*' = S`, `C*' = S`
- `own1 = min(W1,C1)`, `own2 = min(W2,C2)`
- `S' = min(own1, own2)`  (shared-mediator AND)

**Secondary lift (threshold-AND, documented only unless primary is
computable).** `t(x)=(1 if x≥2 else 0)`; then binary AND on thresholds. Not
primary — it collapses graded state before dynamics.

**Instrument.** Lab default is exact **IIT-4.0** (`pyphi.new_big_phi`) on the
`feature/iit-4.0` pin. Multivalued nodes require a nonbinary PyPhi API
(`num_states_per_node`) that this pin does not expose (WAVE10 #5 / parked
agenda). Hypotheses below separate the binary control from the ternary claim
so a tooling gap is reportable without faking Φ.

## H1 — binary control

Shared-mediator AND under binary IIT-4.0 still spans both exclusive leaf pairs
with core Φ = 4.0 (replicates `two_triad_shared_member`).

## H2 — IIT-4.0 multivalued capability

The installed IIT-4.0 PyPhi accepts a 5-node ternary TPM (or equivalently
exposes a documented multivalued Network API usable with `new_big_phi`).

Null: capability absent → H3–H5 are **not testable** on this instrument.

## H3 — ternary min-AND still merges (spans both)

If H2 holds: under ternary min-AND, the major complex spans both `{W1,C1}` and
`{W2,C2}`.

## H4 — ternary core is not a local leaf pair

If H2 holds: ternary major complex is not confined to a single exclusive pair
(or empty).

## H5 — Φ magnitude moves or membership differs from binary

If H2 holds: either core membership ≠ all five nodes, or core Φ differs from
4.0 by more than PHI_EPS (graded state changes the binary reading).

Null for H5: identical five-node core at Φ=4.0 (merge fully survives).

# Instrument decision — agenda #1 (ternary pivotality)

Fixed **before** computing any scientific claim about multivalued
pivotality. Paths evaluated against the lab pin
`pyphi @ git+…@feature/iit-4.0` and WAVE10 parked #5.

## Options

| path | meaning |
|---|---|
| **(A)** | Patch/port multivalued support onto the IIT-4.0 pin so `Network` + `new_big_phi` accept k-ary TPMs |
| **(B)** | Defensible embedding/proxy that still answers whether the two-condition account survives ternary parties |
| **(C)** | Honest **NOT_TESTABLE** with a minimal reproduce case |

## Decision: **(C)**

### Why not (A) this turn

Multivalued IIT (Gomez et al. 2021) needs a nonbinary Network API
(`num_states_per_node`) and a `new_big_phi` that is defined on
mixed-radix state spaces. The installed pin’s `Network.__init__` has
no such parameter; SBS shapes `3^n × 3^n` are rejected (broadcast
against `2^n`). Porting that stack is a pin-level engineering project,
not a study-sized patch. Not attempted here.

### Why not (B)

Candidate embeddings (threshold collapse; bit-expansion of each ternary
node into two binary bits; stochastic binary proxies) change the
*question*:

- Threshold collapse grades state **before** dynamics — WAVE10 #5 marks
  this secondary, not primary.
- Bit-expansion makes “party in core” and ternary **influence**
  definitional (which bits? how is sensitivity aggregated?). Exact Φ
  on the expanded system is not Φ on the ternary system.
- Proxies that only check connectivity/influence without major-complex
  Φ do not test the two-condition *account* as validated in probes
  #11–#12.

None of these is a defensible stand-in for “exact IIT-4.0 Φ on ternary
parties.” Preferring exact Φ → reject (B) for #1.

### What (C) delivers

1. **Binary control:** two-condition account still holds on designed
   binary forms (bidirectional pivotal parties in core; non-bidirectional
   out) — instrument health, not a ternary answer.
2. **Minimal reproduce:** n=3 ternary min-AND triad SBS `(27,27)`
   rejected by `Network` on this pin (same class of failure as
   `shared_mediator_ternary/`).
3. **Scientific status:** H3–H5 on ternary pivotality are
   **NOT_TESTABLE** here — tooling gap, not a null on graded state.

Prior pointer: `studies/shared_mediator_ternary/` (merge survival;
same pin limit). This study targets agenda **#1** / WAVE10 **#5**
(two-condition under ternary parties).

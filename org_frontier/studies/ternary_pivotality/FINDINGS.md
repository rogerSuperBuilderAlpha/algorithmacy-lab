# Ternary pivotality — findings

**Verdict: NOT_TESTABLE.** Exact IIT-4.0 on this lab’s PyPhi pin
**rejects** ternary n=3 SBS `(27,27)`. Path **(C)** stands for science.
Path **(A)** M1 landed (`third_party/pyphi_iit4_mv` → **M1_GREEN**):
ternary Network constructs and SBS is preserved, but exact Φ is still
blocked at M2 (`backward_tpm`). CI-off remains a corrupt shim;
`pyphi@nonbinary` rejected. Path **(B)** embeddings remain rejected for
#1. Binary two-condition control **holds**. Ternary pivotality (H3–H5)
remains **open**, not a scientific null.

In-silico. Hypotheses fixed after the instrument decision. Cited:
probes #11–#12; WAVE10 #5; `shared_mediator_ternary/` pointer;
`multivalued_iit4_port/INSTRUMENT_GAP.md`. PE / AI / formal / stoch /
estimation / construct-omit closed.

## Instrument

| path | decision |
|---|---|
| (A) multivalued IIT-4.0 port | **M1_GREEN** / Φ still M2 (see port study) |
| (B) embedding/proxy | rejected — does not answer party-level exact Φ |
| **(C) NOT_TESTABLE** | **stands for #1 science** |

Capability error: no `num_states_per_node`; SBS `(27,27)` fails binary
convert/CI. Same pin class as `shared_mediator_ternary/`.

## Hypotheses

| H | result |
|---|---|
| H1 binary two-condition control | **SUPPORTED** |
| H2 IIT-4.0 accepts ternary n=3 | **REFUTED** |
| H3 ternary non-bidir stays out | **NOT_TESTABLE** |
| H4 ternary bidir parties in | **NOT_TESTABLE** |
| H5 graded changes pivotality | **NOT_TESTABLE** |

## Binary control (witnesses)

| form | core | reading |
|---|---|---|
| faithful | {W,S,C} Φ=2 | bidirectional triad |
| W_sticky / W_omitted | {S,C} | non-bidirectional W out |
| C_sticky | {W,S} | non-bidirectional C out |

## Reading

Agenda #1 / WAVE10 #5 needs a vendored multivalued IIT-4.0 pin before
any claim that ternary idle/engaged/overcommitted parties change (or
preserve) pivotality. The binary two-condition account is healthy; the
graded question is instrument-blocked, not answered.

## Best next

**Engineering:** `multivalued_iit4_port/INSTRUMENT_GAP.md` **M2**
(SBS-native `backward_tpm` / repertoire). **#2–#4** stay blocked.

## Reproduce

```
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```

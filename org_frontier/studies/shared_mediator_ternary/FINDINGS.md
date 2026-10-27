# Shared-mediator ternary — findings

**Verdict: TOOLING_GAP (partial).** The binary shared-mediator AND merger
**replicates** (five-node core, Φ=4.0, spans both leaf pairs). The primary
**min-AND** ternary lift is well-defined and agrees with binary AND on the
{0,1}^5 cube. Exact **IIT-4.0** on this lab's PyPhi pin **cannot** ingest a
ternary TPM (`Network` has no `num_states_per_node`; 3^5 SBS is rejected).
H3–H5 (merge survival under ternary) are therefore **NOT_TESTABLE** here —
not a scientific null on graded state, a confirmed instrument limit (WAVE10 #5).

In-silico scope. Hypotheses fixed in `hypotheses.md` before computing. Extends
`two_triad_shared_member/`. Residual/cascade not reopened
(`foundations/RESIDUAL_AND_CASCADE.md`).

## Ternary lift (primary)

On alphabet {0,1,2}, `min(a,b)` extends binary conjunction. Shared-mediator AND:

- leaves copy S: `W*'=S`, `C*'=S`
- `S' = min(min(W1,C1), min(W2,C2))`

Unit check: on every state in {0,1}^5, the ternary next-state equals the binary
construction. Secondary threshold-AND was documented but not run (primary
blocked).

## Results

| check | result |
|---|---|
| H1 binary control (merge, Φ=4.0, full core) | **SUPPORTED** |
| H2 IIT-4.0 accepts ternary / multivalued API | **REFUTED** |
| H3 ternary spans both | **NOT_TESTABLE** |
| H4 ternary core not local-only | **NOT_TESTABLE** |
| H5 membership/Φ differs from binary | **NOT_TESTABLE** |

Capability error on this pin: SBS shape (243,243) rejected (binary expects
powers of two). `pyphi@nonbinary` (2021) exposes `num_states_per_node` but is
IIT-3.0-era, lacks `new_big_phi`, and does not import cleanly on Python 3.12
without invasive patches — not used as a substitute instrument.

## Reading

Merge survival under true ternary IIT-4.0 remains **open**. The binary shared-
mediator AND result stands. The min-AND lift and 243×243 TPM builder are ready
for a future multivalued IIT-4.0 pin. Do not treat this tooling gap as evidence
that graded state splits (or preserves) the complex.

## Best next experiment

**Done next:** `mediator_hierarchy_census/` (agenda #15) — recurrent trees span
all levels (Φ flat in depth / grows with breadth); feedforward hub chains are
top-local. Follow-on: spanning mediator atop multi-hub (#20), or small-world
vs hierarchy (#17).

## Scope of the tooling gap

The `TOOLING_GAP` line is the stock pin `feature/iit-4.0` at `b78d0e342d37175cbd55cf35a6d52ae035b4c50f`, the build this study ran, prior to the `third_party/pyphi_iit4_mv` M1+M2 overlay. `Network` there has no `num_states_per_node`, and the 3^5 state-by-state matrix is rejected. The hypotheses in `hypotheses.md` and the registered `shared-mediator-ternary` output are the record of that run.

Later paths ingest the same mixed-radix TPM. The M1+M2 overlay `third_party/pyphi_iit4_mv` does, and so does the fork branch `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339a`, pull request `rogerSuperBuilderAlpha/pyphi#1`). Upstream PyPhi 2.0 does too: `wmayner/pyphi` `main` at `134a8f31` (`v2.0.0rc4`) takes arbitrary `num_states_per_node` on `FactoredTPM`. `wmayner/pyphi#147`, which carried this overlay, closed on 25 October 2026 after Will Mayner noted that `feature/iit-4.0` is superseded by that release candidate.

## Reproduce

```
python org_frontier/studies/shared_mediator_ternary/analyze_ternary.py
```

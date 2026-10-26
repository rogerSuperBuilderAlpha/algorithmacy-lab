# Shared-mediator ternary (beyond-binary)

Does the shared-mediator AND five-node merge (Φ=4.0) survive a ternary alphabet?

## Run

```
python org_frontier/studies/shared_mediator_ternary/analyze_ternary.py
```

## Result in one line

**TOOLING_GAP:** binary merge replicates; min-AND lift is ready; exact ternary
IIT-4.0 is not available on this PyPhi pin (H3–H5 NOT_TESTABLE).

That gap is the stock pin `feature/iit-4.0` at `b78d0e342d37175cbd55cf35a6d52ae035b4c50f`, the build this study ran, prior to the `third_party/pyphi_iit4_mv` M1+M2 overlay. `Network` on that commit has no `num_states_per_node`, so the 3^5 state-by-state TPM is rejected. The overlay, the fork branch `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k`, and upstream PyPhi 2.0 `FactoredTPM` (`wmayner/pyphi` `main` at `134a8f31`) each ingest mixed-radix TPMs. The hypotheses in `hypotheses.md` and the registered `shared-mediator-ternary` output stay the record of this run.

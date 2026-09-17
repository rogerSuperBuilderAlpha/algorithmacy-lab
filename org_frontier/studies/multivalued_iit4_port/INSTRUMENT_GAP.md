# INSTRUMENT_GAP — multivalued IIT-4.0 on the lab pin

**Status: M1_GREEN (SBS-native ingest); Φ still INSTRUMENT_GAP (M2).**
Stock `pyphi @ feature/iit-4.0` still rejects ternary SBS. Vendored
overlay `third_party/pyphi_iit4_mv` constructs ternary Networks and
preserves SBS without `int(log2(...))`. Exact ternary IIT-4.0 Φ is
**not** runnable yet. #1 science remains **NOT_TESTABLE**.

## 1. Minimal failing case (stock pin)

From `ternary_pivotality/`: deterministic ternary min-AND triad SBS
shape `(27, 27)`.

```
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
python third_party/pyphi_iit4_mv/smoke_m1.py
```

**Stock path (CI validation on):** `ExplicitTPM.__init__` →
`conditionally_independent` →
`convert.state_by_state2state_by_node` assumes `N = int(log2(S))` →
broadcast error `(27,27)` vs `(16,16)`.

## 2. M1 landed (vendored overlay)

Package: `third_party/pyphi_iit4_mv/`

| check | result |
|---|---|
| `MultivaluedNetwork` `(9,9)` / `(27,27)` | **green** |
| SBS bit-exact preserve | **green** |
| Mixed-radix CI (no binary SBN round-trip) | **green** |
| CI-off `int(log2)` trap | **not used** |
| Exact Φ on ternary | **blocked** |

Enable: insert `third_party` on `sys.path`, then
`from pyphi_iit4_mv import MultivaluedNetwork`. Stock binary Φ unchanged.

## 3. Φ blocker locus (past ExplicitTPM → M2)

Full-system `Subsystem(net, state)` on an M1 network fails at:

1. `Subsystem.__init__`
2. `tpm.backward_tpm`
3. `probability_of_current_state` — treats the SBS `(∏k, ∏k)` matrix as
   binary state-by-node (`len(state)` must equal `shape[-1]`; `# TODO
   extend to nonbinary nodes` in stock `tpm.py`)

Further M2 gates already known: non-empty `condition_tpm` (binary SBN
indexing), `validate.node_states` (zeros/ones only), `node.py` ON/OFF
stack, `repertoire.py` `[2]*n` shapes, `new_big_phi`.

## 4. Trap: CI-off is still a fake shim (rejected)

With `VALIDATE_CONDITIONAL_INDEPENDENCE=False`, a `(9,9)` ternary SBS
is mis-parsed as a corrupt 3-node binary TPM. **Not used** by M1.

## 5. Upstream survey (unchanged)

| source | finding |
|---|---|
| Lab pin `feature/iit-4.0` | Binary only |
| Branch `nonbinary` (2021) | IIT-3.0-era; no `new_big_phi`; 3.12 import break |

**Do not** install `pyphi@nonbinary` as the lab instrument.

## 6. Milestone status

| milestone | scope | status |
|---|---|---|
| **M1** | SBS-native `ExplicitTPM` + `MultivaluedNetwork` | **GREEN** |
| M2 | Repertoire + `Subsystem` for k-ary (backward TPM, condition) | **next** |
| M3 | `new_big_phi.maximal_complex` smoke on 2-node ternary | blocked on M2 |
| M4 | Binary regression + n=3 ternary #1 panel | further |
| M5 | Optional pin policy / requirements wiring | later |

## 7. Recommended next engineering step (M2)

1. SBS-native `backward_tpm` / `probability_of_current_state` for
   mixed radix (do not coerce SBS→binary SBN).
2. Mixed-radix `condition_tpm` for background nodes.
3. Categorical node / repertoire shapes over `∏ k_i`.
4. Only then attempt deterministic 2-node ternary `new_big_phi` smoke.

## 8. What this does *not* claim

- Does not claim ternary pivotality is false or true.
- Does not ship threshold/bit-expansion proxies as Φ.
- Does not use `pyphi@nonbinary`.
- Does not claim exact ternary Φ is available (M1 only).

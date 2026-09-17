# INSTRUMENT_GAP — multivalued IIT-4.0 on the lab pin

**Status: INSTRUMENT_GAP (path A blocked after survey + probe).**
Exact ternary IIT-4.0 Φ is still not runnable on
`pyphi @ feature/iit-4.0`. No fake shim shipped. #1 science remains
**NOT_TESTABLE**.

## 1. Minimal failing case (reproduce)

From `ternary_pivotality/`: deterministic ternary min-AND triad SBS
shape `(27, 27)`.

```
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```

**Default path (CI validation on):** `ExplicitTPM.__init__` →
`conditionally_independent` →
`convert.state_by_state2state_by_node` assumes `N = int(log2(S))` →
broadcast error `(27,27)` vs `(16,16)` (binary 2³=8 → round-trip 16? —
actual error uses binary conversion of a mis-sized intermediate).

Locus stack:

1. `pyphi.network.Network.__init__` → `ExplicitTPM(tpm, validate=True)`
2. `pyphi.tpm.ExplicitTPM._validate_shape` → `conditionally_independent`
3. `pyphi.convert.state_by_state2state_by_node` / `state_by_node2state_by_state`
   hardcode `2**n` and shape `[2]*N`

Also: `Network.num_states` is `2**self.size` (`# TODO extend to
nonbinary nodes`).

## 2. Upstream survey

| source | finding |
|---|---|
| Lab pin `feature/iit-4.0` | Binary only; many `# TODO extend to nonbinary` |
| Branch `nonbinary` (2021) | Has `num_states_per_node`; **IIT-3.0-era**; **no** `new_big_phi` |
| `nonbinary` on Python 3.12 | **Import fails**: `collections.Iterable` removed |
| `develop` / `feature/iit-4.0` | Same binary TODOs; no multivalued API |

**Do not** install `pyphi@nonbinary` as the lab instrument: wrong IIT
version, broken on 3.12, no IIT-4.0 SIA.

## 3. Trap: CI-off is a fake shim (rejected)

With `VALIDATE_CONDITIONAL_INDEPENDENCE=False`, a `(9,9)` ternary SBS
is not rejected — but `state_by_state2state_by_node` does
`N = int(log2(9)) = 3` and builds a **corrupted 3-node binary** TPM
shape `(2,2,2,3)`. Labels for 2 nodes then fail validation. This is
not multivalued IIT-4.0. **Not used.**

## 4. Why a “smallest patch” is not small

Hot-path binary assumptions (non-exhaustive):

| module | issue |
|---|---|
| `convert.py` | SBS↔SBN uses `log2`, `[2]*n`, `2**n`; SBN = P(ON) per node |
| `tpm.py` | Shape validation; CI round-trip; `number_of_units` via `log2` |
| `network.py` | `num_states = 2**size` |
| `repertoire.py` | `np.empty([2]*len(purview))` |
| `distribution.py` | Uniform over `2**n` |
| `subsystem.py` | Conditioning / repertoire caches assume binary TPM layout |
| `new_big_phi/` | Entire SIA stack on binary `Subsystem` |
| `metrics/distribution.py` | Distances assume binary repertoires |

SBN form itself is binary-specialized (one ON probability per node).
Ternary needs categorical next-state distributions (or SBS-only
pipelines). Porting `nonbinary`’s Network API onto IIT-4.0 means
rebuilding convert + TPM + repertoire + subsystem + `new_big_phi`, not
a Network kwargs patch.

**LOC in immediate hot path alone:** ~3.5k lines
(`new_big_phi` + `subsystem` + `repertoire` + `convert` + `tpm` +
`distribution` + `node`). Full parity likely larger.

## 5. Effort estimate (honest)

| milestone | scope | effort |
|---|---|---|
| M1 | Mixed-radix `ExplicitTPM` + convert (SBS-native, no binary CI shim) | large (days–weeks) |
| M2 | Repertoire + `Subsystem` for k-ary states | large (weeks) |
| M3 | `new_big_phi.maximal_complex` smoke on 2-node ternary | large (weeks after M2) |
| M4 | Match binary Φ on `{0,1}` restriction; n=3 ternary #1 panel | further weeks |
| M5 | CI + lab pin / vendored fork policy | days |

**Order of magnitude:** multi-week engineering for a trustworthy
2–3 node ternary Φ smoke; multi-month for a pin-quality replacement
of the binary API. Not a study-turn patch.

## 6. Recommended next engineering step

1. **Vendor a fork** of `wmayner/pyphi@feature/iit-4.0` under
   `third_party/pyphi-iit4-mv/` (or a dedicated repo), do **not**
   monkeypatch site-packages.
2. Milestone M1: SBS-only multivalued `ExplicitTPM` that never calls
   binary SBN conversion; `num_states_per_node` on `Network`.
3. Milestone M2–M3: port repertoire shapes to `∏ k_i` and wire
   `new_big_phi` for deterministic systems only first.
4. Gate lab CI on: binary regression suite + 2-node ternary Φ smoke
   (known analytic or cross-check).
5. Only then reopen `#1` / `#2`–`#4` science.

## 7. What this does *not* claim

- Does not claim ternary pivotality is false or true.
- Does not ship threshold/bit-expansion proxies as Φ.
- Does not use `pyphi@nonbinary`.

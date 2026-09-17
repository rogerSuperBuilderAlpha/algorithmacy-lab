# pyphi_iit4_mv — vendored IIT-4.0 multivalued pin (M1)

Isolated overlay for the lab’s stock `pyphi @ feature/iit-4.0`. **Does not**
replace the binary pin. Adds SBS-native TPM ingest for ternary / mixed-radix
alphabets without the `int(log2(...))` corruption trap.

## Enable

From the repo root (or any script that already inserts the repo root on
`sys.path`):

```python
import os, sys
ROOT = os.path.abspath("...")  # algorithmacy-lab root
sys.path.insert(0, os.path.join(ROOT, "third_party"))

from pyphi_iit4_mv import MultivaluedNetwork, SBSNativeExplicitTPM
```

Stock binary Φ continues to use `import pyphi` from site-packages.

## M1 status

| capability | status |
|---|---|
| Ternary / mixed-radix `Network` construct | **green** |
| SBS preserved (no log2 collapse) | **green** |
| Mixed-radix CI (no binary SBN round-trip) | **green** |
| Exact IIT-4.0 Φ | **blocked** — M2 |

Φ blocker locus (first stock call on full-system Subsystem):
`Subsystem.__init__` → `tpm.backward_tpm` →
`probability_of_current_state`, which treats the SBS matrix as binary
state-by-node (expects `len(state) == shape[-1]`). Non-empty background
conditioning and ternary digits in `validate.node_states` are further M2
gates. See `phi_blocker.probe_exact_phi_blocker`.

## Limitations (M1)

- Alphabet: any `k_i >= 2`; smoke covers ternary `k=3`.
- n ceiling: practical limit is `∏ k_i` for SBS memory (smoke uses n≤3).
- No SBN form, no repertoire, no `new_big_phi` on multivalued nets.
- Do **not** set `VALIDATE_CONDITIONAL_INDEPENDENCE=False` as a substitute —
  that is the rejected CI-off shim.

## Smoke

```
python third_party/pyphi_iit4_mv/smoke_m1.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```

## Next (M2)

Categorical / SBS conditioning + repertoire shapes over `∏ k_i`, then wire
`new_big_phi` for deterministic systems. See
`org_frontier/studies/multivalued_iit4_port/INSTRUMENT_GAP.md`.

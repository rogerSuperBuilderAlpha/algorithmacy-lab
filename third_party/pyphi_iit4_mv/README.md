# pyphi_iit4_mv — vendored IIT-4.0 multivalued pin (M1+M2)

Isolated overlay for the lab’s stock `pyphi @ feature/iit-4.0`. **Does not**
replace the binary pin. Adds SBS-native TPM ingest and exact IIT-4.0
system Φ for ternary / mixed-radix alphabets without the `int(log2(...))`
corruption trap.

## Enable

```python
import os, sys
ROOT = os.path.abspath("...")  # algorithmacy-lab root
sys.path.insert(0, os.path.join(ROOT, "third_party"))

from pyphi_iit4_mv import MultivaluedNetwork, exact_phi, maximal_complex
```

## Status

| capability | status |
|---|---|
| Ternary / mixed-radix Network | **M1 green** |
| SBS preserved (no log2 collapse) | **M1 green** |
| Exact IIT-4.0 system Φ | **M2 green** |
| Binary regression vs stock | **match** (Φ=2 triad) |
| `maximal_complex` | **M2 green** |

## Limitations

- Alphabet `k_i >= 2`; practical n from `∏ k_i` SBS size.
- GID repertoire distance only (lab default).
- CI-off trap never used.

## Smoke

```
python third_party/pyphi_iit4_mv/smoke_m1.py
python third_party/pyphi_iit4_mv/smoke_m2.py
```

# ΦID-based integrated information (Φ_R, CCS) vs exact IIT-4.0 Φ

The [`candidate_audit`](../candidate_audit/) computed integration measures
*exactly* from each network's TPM. This experiment asks the **practical**
question: when integrated information is estimated the way it actually is on data
— via Integrated Information Decomposition (ΦID) on a finite time series, using
the [`phyid`](https://github.com/Imperial-MIND-lab/integrated-info-decomp)
package — does it still track exact IIT-4.0 Φ?

It bridges the two projects this repo's author has contributed to: PyPhi (exact
Φ) and phyid (ΦID).

## The measure (`phiid_measure.py`)

**Φ_R** — the revised whole-minus-sum integrated information
([Mediano, Rosas, Carhart-Harris, Seth & Barrett 2019](https://arxiv.org/abs/1909.02297)).
For a bipartition (A, B), from `phyid`'s 16 ΦID atoms between the two parts'
integer-coded time series:

```
TDMI  = Σ all 16 atoms
I_A   = rtr + rtx + xtr + xtx      I_B = rtr + rty + ytr + yty
Φ_WMS = TDMI − I_A − I_B           Φ_R = Φ_WMS + rtr
```

Φ_R corrects Φ_WMS's double-counting of redundancy (Φ_WMS goes *negative* for
purely redundant systems; Φ_R adds the double-redundancy atom back). We use the
**CCS** redundancy (common change in surprisal) rather than **MMI**: MMI assigns
*spurious synergy* to independent variables, which we confirmed breaks the
measure (independent systems scored as highly synergistic); CCS does not.

The system's integrated information is the **minimum Φ_R over bipartitions** (the
minimum-information-partition analog).

### Validation

The measure is checked before use:

| System | Φ_WMS | Φ_R | meaning |
|--------|------:|----:|---------|
| independent | 0.00 | **0.00** | no integration ✓ |
| redundant (copies) | −0.39 | **0.00** | Φ_WMS double-counts; Φ_R corrects it ✓ |
| coupled / swap | +1.42 | **+1.44** | genuinely integrated ✓ |

The atom bookkeeping (`I_A`, `TDMI` from atoms) was verified to match
directly-estimated mutual informations exactly.

## Reproduce

```bash
python -m foundations.phiid_vs_phi.run 15 3     # -> results/phiid.csv
python -m foundations.phiid_vs_phi.analyze       # -> summary.csv, phiid_vs_phi.png
```

See [`FINDINGS.md`](FINDINGS.md) for results.

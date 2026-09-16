# Encoding ladder — gate family robustness

Does FULL_JOINT_FLIP / Φ=n−1 survive OR, XOR, majority, mixed gates?
Extends `encoding_ladder_n5` / `encoding_ladder_n6`.

## Run

```
python org_frontier/studies/encoding_ladder_gates/analyze_gates.py
```

## Result in one line

**GATE_SPLITS_LADDER.** AND/OR/NAND: Φ=n−1; XOR/XNOR: flip Φ=0.125;
MAJ/MIXED: no flip.

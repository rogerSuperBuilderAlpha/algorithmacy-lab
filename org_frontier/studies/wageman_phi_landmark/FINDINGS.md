# Wageman W × Φ landmark — findings

**Verdict: W_N_PREDICTS_LANDMARK.** A survey-style Wageman index paired
with form size n predicts the Φ landmarks ring-4 / hub-(n−1) / pool.
At n=4, W alone orders hub < ring < pool. Across sizes, W alone
collides (acc=0.70) and needs n (acc=1.0). Dyadic/triadic verdict hold
from V2 #44 remains intact (AUC=1.0).

In-silico; exact binary IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers RESEARCH_AGENDA_V3 #14. Extends V2 #44
`WAGEMAN_PREDICTS_VERDICT` from class to landmark.

**Validation gap.** W is the CM-only survey echo from #44, not a fielded
questionnaire; landmarks are designed Boolean forms, not measured teams.

## Already known

| prior | result |
|---|---|
| V2 #44 Wageman TI → verdict | WAGEMAN_PREDICTS_VERDICT — AUC=1 for class; not Φ magnitude |
| Hub / ring / pool landmarks | Φ=n−1 / Φ=4 / Φ=n(n−1) |
| V3 #13 weakest Boolean render | ROLE_COUNTS_HUB_WEAKEST (pointer) |

## Panel

### N4 landmark triad

| form | W | Φ | landmark |
|---|---:|---:|---|
| hub4 | 0.500 | 3 | HUB |
| ring4 | 0.667 | 4 | RING4 |
| pool4 | 1.000 | 12 | POOL |

Order hub < ring < pool with gaps ≥0.05; nearest-prototype acc=3/3.

### Cross-n landmarks

W-alone vs n4 prototypes: **7/10 = 0.70** (misses hub3→RING4,
ring5→HUB, ring6→HUB). (W, n) prototypes: **10/10 = 1.00**.

### Verdict hold (#44)

AUC(W→triadic)=1.000 on independent / feed / handoff / AND / XOR / OR
chains (XOR shares W with AND; Φ differs — same #44 limit).

## Hypotheses

| H | result |
|---|---|
| H1 n=4 W separates hub<ring<pool | **SUPPORTED** |
| H2 W alone fails cross-n (acc<0.85) | **SUPPORTED** |
| H3 (W,n) recovers landmark cross-n | **SUPPORTED** |
| H4 W→triadic verdict hold | **SUPPORTED** |
| H5 panel closed | **SUPPORTED** |

## Reading

The Wageman CM echo can be paired with an in-silico form to read
**landmark**, not only verdict — but the pairing must carry size.
Connectivity intensity alone is enough at the named ring-4 comparison;
across n it confuses hubs and rings whose W values cross. Within one
CM, W remains blind to gate family (XOR vs AND), so landmark prediction
here is topological, not algebraic.

## Best next (V3)

**#15** topology-aware imputer under role-gated collapse. Alternate
**#16** correlated party duty cycles vs δ=0 cliff.

## Reproduce

```
python org_frontier/studies/wageman_phi_landmark/analyze_wageman_landmark.py
```

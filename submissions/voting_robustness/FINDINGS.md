# Probe 462 — Voting/Quorum Robustness to Update Schedule and Temporal Grain: Findings

## Summary Table

| Hypothesis | Claim | Verdict | Key Evidence |
|------------|-------|---------|--------------|
| **H1** | Baseline reproduces Probes 67/122 | **SUPPORTED** | All 10 rules match expected structure, Φ, core at k=1 |
| **H2** | 2-step grain collapses all to dyadic | **SUPPORTED** | 10/10 rules dyadic Φ=0.0 at k=2 |
| **H3** | Sequential update collapses all | **SUPPORTED** | Inferred from Probe 62 (all 24 canonically-triadic collapse) |
| **H4** | No differential robustness | **SUPPORTED** | AND/OR collapse identically to majority/weighted |
| **H5** | 3-step grain restores some rules | **EXPLORATORY** | AND/OR/parity recover; majority/weighted do not |

## Detailed Findings

### Baseline (k=1, synchronous)
All 10 rules reproduce Probes 67/122 exactly:
- Extreme rules (AND, OR): triadic, Φ=3.0, core {W,C1,C2}
- Parity (XOR): triadic, Φ=0.25, core {W,C1,C2}
- All others: dyadic, Φ=0.0

### 2-Step Grain (k=2)
All 10 rules collapse to dyadic Φ=0.0. The cores of the extreme rules (which contain all three parties at k=1) survive as sets but with Φ=0.0 — integration vanishes.

### Sequential Update
All 10 rules collapse (inferred from Probe 62: all 24 canonically-triadic forms collapse under all 6 sequential orders).

### 3-Step Grain (k=3) — Differential Recovery
| Rule | Structure | Φ | Core |
|------|-----------|---|------|
| unanimity (AND) | triadic | 3.000 | {W,C1,C2} |
| any (OR) | triadic | 3.000 | {W,C1,C2} |
| parity (XOR) | triadic | 0.250 | {W,C1,C2} |
| majority (2of3) | dyadic | 0.000 | — |
| veto (W blocks) | dyadic | 0.000 | {W} |
| weighted 2-1-1, t=2 | dyadic | 0.000 | {W} |
| weighted 2-1-1, t=3 | dyadic | 0.000 | {W} |
| weighted 3-1-1, t=3 | dyadic | 0.000 | {W} |
| weighted 3-1-1, t=4 | dyadic | 0.000 | {W} |
| 2-of-3 excluding W | dyadic | 0.000 | {C1,C2} |

**AND, OR, parity recover triadic; majority/weighted do not.**

## Numbers Registered in CI
Check `probe-voting-robustness` in `ci/reproduce.json` passes.
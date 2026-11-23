# The matching rule holds for AND and OR platforms but not for XOR

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `08791fd6` before computation. Control passed: orP_or_from_P reproduces `or_gate_source`
(whole Φ = 2.000000).

## Setup

P reads R1, R2; R1' = P; R2' = C1; C1' = gate(P, G); G' = the named member.

| form | platform | gate | G copies | reachable states | whole Φ | states with whole φ > 0 | top φ | full bound | pooled top ties |
|---|---|---|---|---:|---:|---:|---:|---|---|
| orP_or_from_P | OR | OR | P | 12 | 2.000000 | 2 | 2.000000 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| orP_or_from_R1 | OR | OR | R1 | 18 | 2.000000 | 4 | 2.000000 | yes | PR1, PR2C1, PR1R2C1, PR1R2C1G |
| orP_or_from_R2 | OR | OR | R2 | 18 | 2.000000 | 1 | 2.000000 | yes | PR1, PR2C1, R2C1G, PR1R2C1, PR1R2C1G |
| orP_or_from_C1 | OR | OR | C1 | 12 | 2.000000 | 1 | 2.000000 | yes | C1G, PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| orP_and_from_R1 | OR | AND | R1 | 18 | 0.000000 | 0 | 2.000000 | no | PR1 |
| xorP_xor_from_P | XOR | XOR | P | 16 | 0.500000 | 16 | 0.500000 | yes | PR1R2C1, PR1R2C1G |
| xorP_and_from_P | XOR | AND | P | 12 | 0.500000 | 4 | 0.500000 | yes | PR1R2C1, PR1R2C1G |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** OR–OR with G copying R1, R2 or C1: whole Φ = 2.000000 each.
- **H2 SUPPORTED.** OR–AND with G copying R1: whole Φ = 0.
- **H3 SUPPORTED.** XOR–XOR: whole Φ = 0.500000.
- **H4 REFUTED.** XOR–AND: whole Φ = 0.500000, not 0.
- **Matching rule REFUTED** as a general rule (H4 fails).

## Reading

For AND and OR platforms the pattern from `or_gate_source` held on all five new forms: every matched form
(OR–OR, four drivers counting the control) binds the whole group at 2.0 and the mismatched OR–AND form
does not. Combined with the earlier studies that is 14 inside-driven AND/OR forms with no exception. The XOR platform
does not follow it. With an XOR gate or a mismatched AND gate, the whole five-member group is bound at
0.5, the same value as the ungated XOR loop in `relay_flips`, and the whole ties for top. So the
rule as stated is wrong in general. It may hold only for platforms whose output can be fixed by a single
input (AND, OR), unlike XOR. That narrower version has not been tested.

## What it means

For "both" and "either" platforms, a switch-dependent go-between stays bound with the platform when it
combines the message and the switch the same way the platform does. For a platform that says "go" when
exactly one of two people is in, how the go-between combines them did not matter in the two cases tried.
The whole group stayed bound either way, though only at Φ = 0.5.

## Limits

Binary, deterministic, synchronous; n = 5; two XOR forms; one mismatched OR form. Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/gate_match_test/run.py --quick   # CI subset, ~14 s
python org_frontier/studies/gate_match_test/run.py --write   # full run, ~55 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.

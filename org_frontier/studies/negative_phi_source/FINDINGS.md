# The published negative φ is the effect-side signed GID, with no floor: 0.6569999999999999 × log2(0.6569999999999999 / 0.7549999999999999) = −0.13178321094580336

The published negative φ of −0.13178321094580336 is the effect-side value of PyPhi's signed GID formula, selectivity × log2(forward / partitioned) = 0.6569999999999999 × log2(0.6569999999999999 / 0.7549999999999999) = −0.13178321094580336, with no floor. Cause-side φ is 0.33979877901916944. The minus is not from a later combination of distinctions or relations.

Hypotheses were committed (`421311cf`) before computing. The published value is the OR3, η = 0.3, {S, P1} at 0000 entry from `negative_phi_survey` (disclosed in `hypotheses.md`). The SIA recovered that value exactly.

## Scores

- **H1 SUPPORTED.** System φ equals effect-side φ and equals the published −0.13178321094580336. Cause-side φ is 0.33979877901916944, which is positive.
- **H2 SUPPORTED.** Effect-side informativeness is log2(0.6569999999999999 / 0.7549999999999999) = −0.20058327389011169. Selectivity is 0.6569999999999999, which is positive. Their product equals effect-side φ and system φ exactly (−0.13178321094580336; relative error 0). The sign is already in that product. The specified effect state is (1, 0), not the current state 0000.
- **H3 SUPPORTED.** {S, P2} at 0000 has the same system φ and the same effect φ (−0.13178321094580336). Cause-side φ is 0.3397987790191687, within 2.2e-15 of the {S, P1} value.

## Exact numbers

The MIP of {S, P1} is a two-part cut recorded by PyPhi as `[[0 0], [1 0]]`. The cause-side product is also exact: selectivity 0.7 × log2(0.23548000000000024 / 0.16820000000000013) = 0.33979877901916944.

| subset | side | specified state | selectivity | forward | partitioned | informativeness | product = φ |
|---|---|---|---:|---:|---:|---:|---:|
| {S, P1} | cause | (0, 0) | 0.7 | 0.23548000000000024 | 0.16820000000000013 | 0.4854268271702421 | 0.33979877901916944 |
| {S, P1} | effect | (1, 0) | 0.6569999999999999 | 0.6569999999999999 | 0.7549999999999999 | −0.20058327389011169 | −0.13178321094580336 |
| {S, P2} | cause | (0, 0) | 0.6999999999999997 | 0.23548000000000024 | 0.16820000000000024 | 0.4854268271702412 | 0.3397987790191687 |
| {S, P2} | effect | (1, 0) | 0.6569999999999999 | 0.6569999999999999 | 0.7549999999999999 | −0.20058327389011169 | −0.13178321094580336 |

System φ is the minimum of the two sides, so it equals the effect value.

## What it means

The minus sign is already in PyPhi's implemented formula for this MIP: selectivity times a signed log ratio, with no floor and no absolute value, taken from the effect side because that side is smaller. The partitioned effect repertoire at the specified state (0.7549999999999999) is larger than the intact forward repertoire (0.6569999999999999), so the log ratio is negative. The survey's stored system φ is this number, not a sum of distinction or relation φ. That is a fact about the code path. This study does not re-open the earlier finding that negative φ is outside what IIT 4.0 defines.

## Limits

One form, one rate, two two-node subsets, one current state. The same PyPhi path computes every other SIA in these studies; this run traces only the backlog's chosen value.

## Reproduce

```sh
python org_frontier/studies/negative_phi_source/run.py --quick   # CI subset, ~4 s
python org_frontier/studies/negative_phi_source/run.py --write   # full run, ~4 s
```

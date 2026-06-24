# q182 — findings

An adversary restricted to evidence-permitted readings forces the point verdict at will, and the
agreement-weighted Φ confidence interval does not contain the forced estimate often enough to count
as a defense. Results are on synthetic coder panels.

## Instrument control

The faithful triad `[x1, x0&x2, x1]` reads `triadic` with max Φ_MIP = 2.000000. PASS.

## Controls

| control | panel | adversary flip available | CI |
|---|---|---|---|
| A honest consensus | `['AND']*4` | no | — |
| B unique reading | `['copyW']*3` | no | degenerate `[0.000, 0.000]` |

A unanimous panel offers no opposite-kind reading, so the adversary is powerless. A unique reading
gives a degenerate CI, as the bridge specifies.

## Population attack

| quantity | value |
|---|---|
| accounts generated | 200 |
| tied (no consensus) | 42 |
| powerless (unique pool) | 57 |
| attacked | 101 |
| forced-flip rate | 1.000 (threshold > 0.40) |
| CI-containment rate | 0.218 (threshold > 0.90) |

Every account that offered an opposite-kind defensible reading was flipped. The dyadic/triadic
split is categorical: any defensible triadic reading reads triadic and any dyadic reading reads
dyadic, so a single permitted swap moves the point verdict. The CI built over the whole panel
brackets the adversary's extreme forced estimate in only 22 of 101 attacks. When the adversary
forces triadic by picking an `AND` or `OR` reading at Φ=2.0 while the panel leans dyadic, the CI
sits low and misses the forced point.

## Verdicts

- **H1 (forced flip): SUPPORTED.** Forced-flip rate 1.000 > 0.40.
- **H2 (CI defense): NOT SUPPORTED.** CI-containment rate 0.218, far below 0.90. Propagating coder
  disagreement into a CI does not bracket an adversary who selects the extreme defensible reading.
  The CI exposes width, but the adversarial point lands outside it most of the time.

## Reading

The point verdict is fragile: when the evidence permits both a dyadic and a triadic reading of the
mediator, a determined coder picks whichever serves the target. The agreement-weighted CI does not
neutralize this. A CI centered on the consensus mean with bootstrap-t width tracks the panel's bulk,
and the adversary's chosen reading is by construction the panel's extreme, which the interval often
fails to cover. Robustness here comes from the pool composition, not from the CI: accounts with a
unique defensible reading (57 of 200) and tied panels (42 of 200) resist the adversary outright,
while contested accounts fall every time.

## Scope

Synthetic coder panels of Boolean rules. No worker state is measured. The empirical numbers
describe the bridge on synthetic codings.

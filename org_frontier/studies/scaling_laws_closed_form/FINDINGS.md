# Scaling laws closed-form — findings

**Verdict: PARTIAL_PROOFS** (cut formulas); MIP identity **closed by
#49** for pool/hub, parity residual on general-$n$ $I=1$ uniqueness.
See [`../mincut_mip/`](../mincut_mip/) and `FORMAL_THEORY_ARC.md`.

The three zoo laws follow from IIT-4.0 GID on an explicit MIP cut:
conjunctive/parity on the hub-preserving atomic cut, pool on the
complete atomic cut. Exact Φ smoke matches every grid cell.

In-silico; candid N. Hypotheses fixed in `hypotheses.md`. Proofs in
`PROOFS.md`. Cited: #115, #116, #132; agenda #47, #49. Stoch–temporal /
estimation / construct / omit closed.

## Status per law

| claim | cut / selectivity | MIP identity | status |
|---|---|---|---|
| C1 hub Φ = n−1 | proved: $p_{\mathrm{part}}=2^{1-n}$ ⇒ φ = n−1 | **proved** (#49 T2) | **proved** |
| C2 pool Φ = n(n−1) | proved: $p_{\mathrm{part}}=2^{-n(n-1)}$ | **proved** (#49 T1) | **proved** |
| C3 parity Φ = 2^(2−n) | proved: sel$_c$ = 2^(2−n), informativeness = 1 | partial (#49 T3, $n\le 5$) | **partial** |

## Verification table (exact Φ)

Instrument control: faithful triad Φ = 2. Grid: major-complex Φ vs
closed form; all-1s SIA φ agrees.

| form | n | Φ | law | hold |
|---|---:|---:|---:|:---:|
| conjunctive_hub | 3 | 2 | 2 | YES |
| conjunctive_hub | 4 | 3 | 3 | YES |
| conjunctive_hub | 5 | 4 | 4 | YES |
| conjunctive_hub | 6 | 5 | 5 | YES |
| pool | 3 | 6 | 6 | YES |
| pool | 4 | 12 | 12 | YES |
| pool | 5 | 20 | 20 | YES |
| parity_hub | 3 | 0.5 | 0.5 | YES |
| parity_hub | 4 | 0.25 | 0.25 | YES |
| parity_hub | 5 | 0.125 | 0.125 | YES |

GID checks at all-1s: hub/pool sel = 1, $p_{\mathrm{part}}$ as in
`PROOFS.md`; parity sel$_c$ = 2^(2−n), $p_{\mathrm{part}}$ = 1/2.

## Reading

The scaling laws are not numeric accidents. Under GID they are the
information cost of noising the severed inputs on the MIP candidate:
$n-1$ AND-inputs for the hub broadcast, $n(n-1)$ AND-inputs for the
pool, and a selectivity floor $2^{2-n}$ for the XOR preimage with a
fair parity bit after the cut. What remains is to prove that those
cuts are always the MIP — the same seam question #49 asks.

## Limits

Boolean exact Φ; `SET_UNI/BI` only; major-complex at reachable states;
no organization measured. MIP uniqueness beyond the smoke grid is
conjecture.

## Best next

**#48** — conjunctive hub uniqueness at the $2(n-1)$ edge floor.
Then **#50** — lattice of kinds. (#49 done: `../mincut_mip/`.)

## Reproduce

```
python org_frontier/studies/scaling_laws_closed_form/verify_laws.py
```
(~30 s)

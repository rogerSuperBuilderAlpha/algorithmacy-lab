# Min-cut MIP — findings

**Verdict: NORMALIZED_CUT.** Graph min-cut ≡ Φ-seam is **REFUTED**
(Q49 H5). For the #47 families a *normalized GID cut-weight* theorem
places the MIP at the named cuts: pool **PROVED** (MIP = $A$ all $n$),
conjunctive hub **PROVED** (MIP ∈ $\{H,H'\}$ all $n$), parity
**PARTIAL** (MIP = $H$; $I\ge 2$ dominated for all $n$; $I=1$
uniqueness exhausted $n\le 5$).

In-silico; candid N. Hypotheses in `hypotheses.md`. Proofs in
`PROOFS.md`. Cited: #26, #33, Q49 #140–#144, #47. Stoch–temporal /
estimation / construct / omit closed.

## Status

| claim | status | note |
|---|---|---|
| T0 graph min-cut | **REFUTED** | Q49; worker-unique seam also refuted |
| T1 pool MIP = $A$ | **PROVED** | $\varphi=n_{\mathrm{cut}}$ ⇒ max-cut among density-1 |
| T2 hub MIP = $H$/$H'$ | **PROVED** | star weight + phantom bound $\Rightarrow\varphi_{\mathrm{norm}}\ge 1/(n-1)$ |
| T3 parity MIP = $H$ | **PARTIAL** | $I\ge 2$ all-$n$; $I=1$ unique max cut $n\le 5$ |

## #47 gaps

| law | after #49 |
|---|---|
| conjunctive Φ = n−1 | MIP identity **proved** |
| pool Φ = n(n−1) | MIP identity **proved** |
| parity Φ = 2^(2−n) | MIP = $H$ on $n\le 5$; general $I=1$ uniqueness residual |

## Smoke table

Instrument control: faithful triad Φ = 2. Exhaustive `SET_UNI/BI`
evaluation at all-1s.

| family | n | Φ | law | named MIP | cell |
|---|---:|---:|---:|:---:|:---:|
| pool | 3..5 | n(n−1) | n(n−1) | $A$ | PASS |
| hub | 3..5 | n−1 | n−1 | $H$/$H'$ | PASS |
| parity | 3..5 | 2^(2−n) | 2^(2−n) | $H$ unique | PASS |

## Reading

The MIP is not the connectivity min-cut of #26/#33’s graph reading.
On AND-all-to-all (pool) every cut has density 1, so the MIP is the
*maximum* cut $A$. On the hub star, phantoms pad $n_{\mathrm{cut}}$
at most $(n-2)$ per star edge, forcing density $\ge 1/(n-1)$ with
equality at the commit/broadcast interface $H$/$H'$. Parity keeps the
same interface but is selectivity-limited: any cut with
informativeness $\ge 2$ loses on normalized φ to $H$.

## Limits

Boolean exact Φ; `SET_UNI/BI` only; all-1s; parity $I=1$ uniqueness
beyond $n=5$ not exhausted. No organization measured.

## Best next

**#48** — conjunctive hub uniqueness at the $2(n-1)$ edge floor.
Then **#50** — lattice of coordination kinds.

## Reproduce

```
python org_frontier/studies/mincut_mip/verify_mip.py
```
(~15 s)

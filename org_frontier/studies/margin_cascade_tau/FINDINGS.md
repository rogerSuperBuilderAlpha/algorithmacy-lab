# Margin-cascade τ vs top-B% — findings

**Verdict: nested τ ≈ top-B%; lab default = B=10% top-B% (recompute ranks per panel).**
On n=4, nested cal-fold τ-matching at B=10% yields the same FN|tri as top-B%
(**3.7%**, |Δ|=0.00 pp). On-panel, τ\*(B=10%)=**0.2876** is identical to top-10%.
Frozen τ\* transferred to n=5 with call rate **13.8%** (inside [5%, 15%]) but FN|tri
**7.1%** vs top-10%'s **10.6%** (|Δ|=3.5 pp > 3 pp) — H2 REFUTED because the frozen
threshold spends more budget, not because it fails to find errors. Prefer **top-B%**
whenever the exact-Φ call count must stay fixed across panel sizes.

In-silico; unc k=2. Hypotheses fixed in `hypotheses.md` before computing.
`margin_cascade_phi` WIN, size series 4.8→7.5→9.0, F28, and FN-redesign null are cited,
not reopened.

## Rules compared

| rule | selection | call rate |
|---|---|---|
| top-B% | `round(B·N)` smallest \|p−0.5\| | fixed by construction |
| fixed τ | \|p−0.5\| < τ | data-dependent |
| nested τ-calibrated | τ set on other folds to hit ≈B; apply held-out | ≈B in expectation |

OOF RF probs only (5-fold `cross_val_predict`). Exact Φ = cached `triadic`.

## n=4 curves (selected)

| B / τ | call% | FN\|tri | miss |
|---|---|---|---|
| top-B% 10% | 10.0% | **3.7%** | 3.2% |
| τ=0.25 | 8.2% | 4.0% | 3.3% |
| τ=0.30 | 10.6% | 3.7% | 3.2% |
| nested τ @10% | 10.0% | **3.7%** | — |
| nested top @10% | 10.0% | **3.7%** | — |

## n=5 transfer

| rule | call% | FN\|tri |
|---|---|---|
| top-B% 10% | 10.0% | 10.6% |
| frozen τ\*=0.2876 (from n4@10%) | **13.8%** | **7.1%** |
| τ=0.20 on n5 (≈10% calls) | 10.4% | 10.6% |

Frozen τ overshoots the budget and therefore undercuts FN relative to hard top-10%.
A τ that hits ~10% *on n5* is ≈0.20 — not the n4 τ\*.

## Hypotheses

| hypothesis | result | detail |
|---|---|---|
| H1 nested \|Δ\| ≤2 pp @ B=10% | **SUPPORTED** | 0.00 pp |
| H2 frozen τ transfers (rate∈[5,15]% and FN within 3 pp) | **REFUTED** | rate OK; FN gap 3.5 pp |
| H3 stable lab default | **SUPPORTED** | B=10% top-B% |

## Recommended lab default

**B = 10% top-B% ranking** on OOF `|p−0.5|`, recomputed per panel.
Document on-panel equivalent `τ*(n=4, B=10%) = 0.2876` for prose; do **not** freeze τ
across sizes when the Φ budget is hard. Use a fixed τ only when variable call rate is
acceptable and the threshold is re-checked on a same-size calibration set.

## Best next experiment

**Done next:** `org_frontier/cascade/` adopts B=10% top-B% as the lab-default tooling
(`python -m org_frontier.cascade.run`). Follow-on: wire cascade@10% into the next large unc
sweep as dual residual (always-cheap + cascade), with exact-call count logged.

## Reproduce

```
python org_frontier/studies/margin_cascade_tau/analyze_tau_vs_b.py
```

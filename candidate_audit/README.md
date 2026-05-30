# Candidate-measure audit: do the published "candidate Φ" measures track exact IIT‑4.0 Φ?

**Question.** A family of *practical* integrated‑information measures is used on
real data and compared in
[Mediano, Seth & Barrett (2019), *Measuring Integrated Information: Comparing
Candidate Measures*](https://www.mdpi.com/1099-4300/21/5/525) — Φ whole‑minus‑sum,
Φ*, stochastic interaction, causal density, decoding‑Φ, geometric Φ, and the
ΦID/synergy measures of the Mediano–Rosas lineage. Those papers compare the
candidates **to each other**, on small or Gaussian systems, because the exact
IIT Φ they approximate was intractable to compute.

This experiment closes that loop: it compares the candidate measures **against
exact IIT‑4.0 Φ** (via [PyPhi](https://github.com/wmayner/pyphi)) on the same
ensemble of small networks used in the sibling [`proxy_audit/`](../proxy_audit/)
experiment.

It is a companion to the proxy audit: that one asked about *empirical* proxies
(LZ complexity, correlation); this one asks about the *theoretically motivated*
candidate Φ measures.

## Measures compared (`measures.py`)

All are computed exactly from the time‑lagged joint `J[s,s'] = π(s)·P(s'|s)`
under the stationary distribution π — no sampling, no Gaussian assumption.

| Measure | Source | Definition (bits) |
|---------|--------|-------------------|
| Time‑delayed MI | — | `I(Xₜ₋₁; Xₜ)` (whole‑system temporal integration) |
| Φ whole‑minus‑sum | Balduzzi & Tononi 2008; Barrett & Seth 2011 | `I(Xₜ₋₁;Xₜ) − Σ_k I(M^k_{t-1};M^k_t)` over the min‑information bipartition |
| Stochastic interaction | Ay 2001 | `Σᵢ H(X^i_t\|X^i_{t-1}) − H(Xₜ\|Xₜ₋₁)` |
| Causal density | Seth 2008 | mean pairwise transfer entropy `I(X^i_{t-1};X^j_t\|X^j_{t-1})` |
| Integrated synergy | co‑information / ΦID lineage | `min_bipartition [ I(Xₜ₋₁;Xₜ) − I(A_{t-1};Xₜ) − I(B_{t-1};Xₜ) ]` |
| Total correlation | — | instantaneous multi‑information (baseline) |

`phi_wms` and `integrated_synergy` are signed (may be negative), as is standard
for whole‑minus‑sum / interaction‑information quantities.

**Deferred** (need numerical optimisation or external packages): geometric Φ
(Φ_G), Φ*, decoding‑Φ, full ΦID, and M‑information
([Liardi et al. 2025](https://arxiv.org/abs/2506.18498)). Adding these is the
natural next extension.

## Ground truth and ensemble

Reused, unchanged, from [`proxy_audit/`](../proxy_audit/): 270 random Boolean
networks (`n ∈ {3,4}`), exact IIT‑4.0 Φ via `pyphi.new_big_phi.sia`, summarized
as the mean over reachable states (negative = reducible, clamped to 0).

## Reproduce

```bash
python -m candidate_audit.run 15 1     # -> results/audit.csv
python -m candidate_audit.analyze       # -> summary.csv, candidate_vs_phi.png
```

## Validation

The measures are unit‑checked on known systems: independent self‑copy nodes give
0 for every coupling measure; a deterministic XOR network gives zero *pairwise*
causal density (the classic "XOR carries no pairwise information"). See the test
at the bottom of `measures.py`'s history / `FINDINGS.md`.

See [`FINDINGS.md`](FINDINGS.md) for results.

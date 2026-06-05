# Findings: estimating Φ from data (via ΦID) roughly halves how well it tracks exact Φ

**TL;DR.** The whole-minus-sum family is the best cheap stand-in for Φ when
computed *exactly* from a network's TPM (the [candidate audit](../candidate_audit/)
found ρ ≈ 0.47). But integrated information is never computed that way on real
data — it is *estimated* from a finite time series, typically via Integrated
Information Decomposition (ΦID). When we do exactly that — compute the revised
Φ_R with CCS redundancy from a simulated trajectory using the `phyid` package —
its tracking of exact IIT-4.0 Φ **roughly halves**. There is a large estimation
gap between "works in principle" and "works on data."

## The measure was done carefully

Φ_R (Mediano et al. 2019) corrects Φ_WMS's double-counting of redundancy; we use
**CCS** redundancy because **MMI assigns spurious synergy to independent
variables** (we confirmed this breaks the measure — independent systems scored as
highly synergistic). The measure passes controls before use:

| System | Φ_WMS | Φ_R |
|--------|------:|----:|
| independent | 0.00 | 0.00 |
| redundant (copies) | −0.39 | 0.00 |
| coupled / integrated | +1.42 | +1.44 |

and the atom bookkeeping was verified against directly-estimated mutual
informations. So the result below is not an artifact of a broken measure.

## The estimation gap (same 270 networks, exact vs data-style)

| Measure | how computed | Spearman ρ(Φ) | AUC(Φ>0) |
|---------|--------------|------:|------:|
| Φ_WMS | **exact**, from the TPM | **0.283** | **0.669** |
| Φ_R (CCS) | **estimated**, ΦID on a finite time series | 0.124 | 0.560 |

(Exact ρ here is 0.283 rather than the candidate audit's 0.47 because this is a
different random ensemble; the within-ensemble exact-vs-estimated comparison is
the like-for-like one.)

The exact and estimated measures correlate with **each other** at ρ = 0.64 — so
the data-style ΦID is recovering much of the same quantity, just noisily. The
loss in tracking Φ comes from finite-sample estimation plus the bivariate
coarse-graining (each side of a cut is collapsed to one integer-valued channel),
not from measuring something different.

## Interpretation

- **Practical caution.** The best cheap surrogate for Φ is already only moderate
  *in principle*; computed the way it must be on data (ΦID from a time series),
  it loses about half of that. Inferring IIT-style integration from neural-data
  ΦID estimates should be done with this gap in mind.
- **CCS matters.** With MMI redundancy the measure is not merely worse — it is
  *wrong* (independent → high synergy). Anyone computing ΦID-based integration
  should prefer CCS (or verify their redundancy choice on an independent control).
- **It is the same quantity, degraded.** Because exact and estimated agree at
  ρ = 0.64, the gap is an *estimation* problem (sample size, coarse-graining),
  not a conceptual mismatch — encouraging for longer recordings / better
  estimators.

## Caveats

- Small systems (n ∈ {3,4}); a specific Boolean-gate ensemble; trajectory length
  8000. Longer series would narrow the gap.
- ΦID here is bivariate over a coarse two-block cut (each block integer-coded);
  a full multivariate ΦID (e.g. OmegaID's doublet lattice) might track better.
- Φ summarized as mean exact Φ over reachable states; min Φ_R over bipartitions.

## Reproduce

`python -m foundations.phiid_vs_phi.run 15 3 && python -m foundations.phiid_vs_phi.analyze`

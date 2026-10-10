# ergodic_cycle_ordering (Strand G / T8 residual)

Test whether the ordering of party-bit flips around a form's attractors
drives the residual basin-mode Equality-of-Averages gap's association with
whole-form \(\Phi_{\mathrm{MIP}}\), on the frozen 42-form panel.

Hypotheses fixed in [`hypotheses.md`](hypotheses.md) **before** computing.
Prior cells: [`../ergodic_gap_decomposition/`](../ergodic_gap_decomposition/),
[`../ergodic_settling_time/`](../ergodic_settling_time/),
[`../ergodic_eoa_basin/`](../ergodic_eoa_basin/).
Track: [`../../ergodicity/`](../../ergodicity/).

## Mechanisms under test

| id | claim | covariate |
|---|---|---|
| (a) | On-cycle finite-T remainder reproduces the basin gap | `pred_gap_cycle` |
| (a′) | All-start remainder versus the cycle mean | `remainder_allstarts` |
| (b) | Ordering beyond the bit's weight | `order_index`, `order_excess`, `cofilip_sync`, `phase_lag`, `lag1_autocorr` |
| (d)–(f) | Flip rate, coarse oscillation, Bernoulli variance | `hamming_party_rate`, `party_osc_frac`, `mean_cycle_var` |

## Instrument

`org_frontier.ergodicity.eoa` (basin reference) and
`org_frontier.ergodicity.settling` (partition, plus cycle-ordering
summaries). Unit tests, no \(\Phi\):

```
python org_frontier/ergodicity/test_cycle_order.py
python org_frontier/ergodicity/test_settling.py
```

## Run

```
python org_frontier/studies/ergodic_cycle_ordering/analyze_ordering.py
python org_frontier/studies/ergodic_cycle_ordering/analyze_ordering.py --ci
```

No numbers in this README. Results land only from the analysis script
after the hypotheses commit.

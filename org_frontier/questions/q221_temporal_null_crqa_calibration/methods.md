# Q221: methods (DRAFT)

## Instrument and environment

- PyPhi `feature/iit-4.0` @ `b78d0e34`: IIT 4.0, GENERALIZED_INTRINSIC_DIFFERENCE.
- Python 3.12.15, numpy 2.5.4, scipy 1.18.1.
- Targets come from q161 `core_indices` / `bottleneck_set`, computed on the deterministic TPM (rule 8). They
  are cross-checked by an own loop using clamp-to-0 and clamp-to-1.

## Family

- Three nodes, synchronous, with an 8% independent flip on every node: q220's generator
  `org_frontier.recurrence.crqa.trajectory`.
- Forms: 4096 `nsi` (q220 R2) forms and 4096 GF(2)-affine forms.

## Population statistics

Exact rational arithmetic, with flip = 2/25, under each chain's own stationary law:
- channel marginals;
- self-recurrence P(x_i(t) = x_i(t+k));
- cross-recurrence P(x_i(t) = x_j(t+k)).

Equality at every lag follows from equality at enough consecutive lags, via the linear-recurrence argument
(order ≤ 16).

## Finite-sample statistics

- q220 `stage2/observe.py`: `coupling` (timestamp, MIN_PAIRS 30), `centrality` (floor 0.05) and
  `bottleneck_scores` (tie-aware).
- Gate-3 baselines: nearest-centroid on marginals, self-recurrence, cross-recurrence and transition counts,
  plus a transition-likelihood ratio.

## Scripts

See the reproduce block in `FINDINGS.md`. Registered CI checks: the `q221-*` entries in `ci/reproduce.json`.

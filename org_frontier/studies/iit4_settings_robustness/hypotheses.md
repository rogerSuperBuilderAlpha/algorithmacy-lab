# Does the verdict survive other IIT 4.0 settings in the pinned PyPhi?

Fixed before this study's computation.

## Gap

Every verdict in the lab uses PyPhi's default IIT 4.0 system partition scheme (`SET_UNI/BI`). Q215
compared IIT 4.0 with IIT 3.0 on ten forms. Nobody has checked whether the verdict depends on the
*other* IIT 4.0 settings the pinned build (`b78d0e342`) exposes for `new_big_phi.sia`, or done so
across a whole rule family rather than a handful of forms.

Disclosure: before writing this file I ran a feasibility pass on the five classifier regression forms
(`org_frontier/classifier/forms.py`) to see which settings run at all. It showed the two dyads stay at
0 everywhere, the two triads drop to 1.0 under `DIRECTED_BI` and `TEMPORAL_DIRECTED_BI` and to 0 under
`GENERAL`/`GENERAL_BIDIRECTIONAL`, and that the small-φ repertoire distances (`IIT_4.0_SMALL_PHI*`) and
`KLD` raise errors inside `sia`. The hypotheses below are about the full panel, which had not been run.

## Panel

- The 256-form strict-mediation family (`org_frontier.corpus.population.enumerate_family`):
  W' = f(S), C' = g(S), S' = h(W, C), all one- and two-input Boolean functions. Under the default
  settings, 24 are triadic (16 at Φ 2.0, 8 parity forms at 0.5; `template_coverage_census`).
- Q215's ten forms (controls, quorums 1/2/3-of-3, rotation, veto, dispatch pair, maximal wiring).
- The five classifier regression forms with their `EXPECTED` verdicts.

## Settings (each a `pyphi.config.override` around `new_big_phi.sia`)

| id | setting |
|---|---|
| default | `SYSTEM_PARTITION_TYPE = SET_UNI/BI` |
| complete | `SET_UNI/BI` with `SYSTEM_PARTITION_INCLUDE_COMPLETE = True` |
| directed_bi | `SYSTEM_PARTITION_TYPE = DIRECTED_BI` (one-way bipartition cuts) |
| temporal | `SYSTEM_PARTITION_TYPE = TEMPORAL_DIRECTED_BI` |
| general_raw | `SYSTEM_PARTITION_TYPE = GENERAL`, as shipped |
| general_disc | `GENERAL` restricted to cuts that leave the system not strongly connected (the filter `sia` intends to apply but cannot reach: `if partitions == "GENERAL"` sits inside `if partitions is None`) |
| norm_none | `DISTINCTION_PHI_NORMALIZATION = NONE` |

Verdict per form and setting: max Φ over reachable states; triadic if > 1e-9. Control: `default`
reproduces 24/256 triadic and Q215's 4.0 column.

## Outcomes

- H1: no form that factors under `default` becomes triadic under any setting other than `general_raw`.
- H2: all 24 default-triadic family forms stay triadic under `complete`, `directed_bi`, `temporal`,
  `general_disc` and `norm_none`.
- H3: `general_raw` gives Φ = 0 to all 256 family forms (it contains cuts of absent edges, which cost nothing).
- H4: wherever both are positive, the conjunctive-family forms have higher Φ than the parity forms.
- H5: all five classifier forms keep their `EXPECTED` verdict under every setting except `general_raw`.

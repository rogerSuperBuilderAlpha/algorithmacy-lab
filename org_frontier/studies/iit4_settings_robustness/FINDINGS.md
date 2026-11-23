# The verdict survives every working IIT 4.0 setting; the size of Φ does not

Six of seven IIT 4.0 settings in the pinned PyPhi give the identical triadic set (24 of 256 strict-mediation
forms) and the identical verdict on all 15 named forms; the seventh (`GENERAL` as shipped) is degenerate.
Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), max over reachable states. Hypotheses pushed in `8802f1da`
before computation (with a disclosed feasibility pass on the five classifier forms). Control passed:
`default` reproduces 24/256 triadic and Q215's IIT 4.0 column.

## Setup

Panel: the 256 strict-mediation forms (W' = f(S), C' = g(S), S' = h(W, C)), Q215's ten forms, and the five
classifier regression forms. Settings: `default` (`SET_UNI/BI`); `complete` (adds the complete partition);
`directed_bi`; `temporal` (`TEMPORAL_DIRECTED_BI`); `general_raw` (`GENERAL`, as shipped); `general_disc`
(`GENERAL` restricted to cuts that break strong connectivity, the filter `sia` intends but never applies);
`norm_none` (`DISTINCTION_PHI_NORMALIZATION = NONE`).

| setting | triadic / 256 | new vs default | lost vs default | distinct triadic Φ |
|---|---:|---:|---:|---|
| default | 24 | 0 | 0 | 0.5, 2.0 |
| complete | 24 | 0 | 0 | 0.5, 2.0 |
| directed_bi | 24 | 0 | 0 | 0.5, 1.0 |
| temporal | 24 | 0 | 0 | 0.5, 1.0 |
| general_raw | 0 | 0 | 24 | none |
| general_disc | 24 | 0 | 0 | 0.5, 1.0 |
| norm_none | 24 | 0 | 0 | 0.5, 2.0 |

Named forms (max Φ; columns default, complete, directed_bi, temporal, general_raw, general_disc, norm_none):

| form | Φ by setting |
|---|---|
| Q215 E1 quorum 1-of-3, E3 quorum 3-of-3 | 3, 3, 1, 1, 0, 1, 3 |
| Q215 CTRL+, E4 rotation, E6 dispatch; classifier ats_triad_mediator, gig_false_dyad | 2, 2, 1, 1, 0, 1, 2 |
| Q215 CTRL−, E2 majority, E5 veto, E7, E8; classifier chat_dyad, gig_dyadic_model, ats_feedback_factors | 0 in every setting |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** No form that factors under `default` becomes triadic under any other setting.
- **H2 SUPPORTED.** All 24 default-triadic family forms stay triadic under the five non-degenerate settings.
- **H3 SUPPORTED.** `general_raw` gives Φ = 0 to all 256. Its minimum partition for the AND hub at state
  (1,1,1) cuts the edge C→W, which is not in the connectivity matrix, so the cut costs nothing.
- **H4 SUPPORTED.** Conjunctive-family forms stay above parity forms wherever both are positive (2.0 or
  1.0 vs 0.5).
- **H5 SUPPORTED.** All five classifier forms keep their expected verdict in every setting except `general_raw`.

## What it means

The lab's yes/no verdict, whether an arrangement splits into parts or stays whole, does not hinge on which
partition scheme IIT 4.0 uses in this PyPhi build, across the whole three-party mediator family and the
forms the manuscripts lean on. The majority vote's zero, which Q215 found IIT 3.0 does not reproduce, holds
in every IIT 4.0 setting. The size of Φ does depend on the setting: under one-way cuts the conjunctive hub,
the rotation and the any-one/all-of-three quorums all read 1.0. This backs the classifier's rule to use the
verdict and treat the magnitude as at most an ordinal hint. Parity forms are the exception that keeps its
value (0.5) everywhere.

## Limits

Three- and four-node deterministic Boolean forms; one PyPhi build. The small-φ repertoire distances
(`IIT_4.0_SMALL_PHI`, `IIT_4.0_SMALL_PHI_NO_ABSOLUTE_VALUE`) and `KLD` raise errors inside `new_big_phi.sia`
in this build, so the repertoire-distance axis is untested. `general_disc` uses our own filter, written to
match the code `sia` contains but never reaches.

## Reproduce

```sh
python org_frontier/studies/iit4_settings_robustness/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/iit4_settings_robustness/run.py --write   # full run, ~6.6 min
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.

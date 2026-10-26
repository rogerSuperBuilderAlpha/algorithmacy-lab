# Q123 — The verdict is reproducible within IIT-4.0, and version-bound

## Question

The critical review charged that "exact IIT-4.0 Φ" is one config of an unpinned, mutable build, with a
reviewer reading SYSTEM_CUTS = 3.0_STYLE as a sign the verdict is not canonical 4.0 (T6). This pins the build,
records the config, and tests whether the binary verdict is invariant to the contested knobs.

## Method

The classifier verdict recomputed under config overrides over the full 256-form strict-mediation family. The
build is pinned to a PyPhi commit; the verdict-relevant config is read from the live environment. Four
overrides are tested for verdict disagreement against the baseline: SYSTEM_CUTS = CONCEPT_STYLE,
SHORTCIRCUIT_SIA = False, PARALLEL = True, and a rerun. Every registered repertoire-distance measure other
than the 4.0-canonical one is tried on the canonical triad for admissibility.

## Results

The verdict is bit-identical across every override, and no alternative measure is an admissible config cell.

| override | verdict disagreements / 256 |
|---|---|
| SYSTEM_CUTS = CONCEPT_STYLE | 0 |
| SHORTCIRCUIT_SIA = False | 0 |
| PARALLEL = True | 0 |
| rerun | 0 |
| alternative repertoire measures admissible and non-degenerate | 0 of 13 |

| | result |
|---|---|
| H1 SYSTEM_CUTS leaves the verdict unchanged | confirmed |
| H2 the SIA optimization leaves the verdict unchanged | confirmed |
| H3 the verdict is deterministic and parallelism-invariant | confirmed |
| H4 no alternative repertoire measure is an admissible cell | confirmed |

## Interpretation

The build is pinned and the config recorded, the first half of reproducibility. The verdict runs on PyPhi at
commit b78d0e342, the IIT-4.0 system-Φ path, the SET_UNI/BI partitions, and the generalized intrinsic-
difference distance. The manifest the probe writes and checks against the environment replaces the moving
branch of the requirements file with a fixed, inspectable build.

The flagged SYSTEM_CUTS knob is idle on the 4.0 path, and the audit corrects the review there. SYSTEM_CUTS
controls the legacy IIT-3.0 cuts for the old big-Φ computation, and the 4.0 system-Φ path never reads it; toggling it leaves every one of the 256 verdicts unchanged. Its default value of 3.0_STYLE in the config is inert,
not evidence that the verdict is a 3.0-style variant, so the inference the review drew from that flag does not
hold.

The verdict is deterministic and path-stable. Disabling the a-priori-reducibility short-circuit changes no
verdict, and parallelism and a second run change none, so the verdict is a reproducible function of the pinned build, set by neither the fast path nor run-to-run variation.

The substantive measure has no working substitute, which defends and bounds the claim together. Twelve of the
thirteen alternative repertoire distances error on the 4.0 path, and the one that runs, EMD, returns Φ = 0 on
the triad where the canonical measure returns 2.0, so no alternative is an admissible, non-degenerate cell. The verdict avoids being one choice among a menu, which answers the review's picture of a silent dependence on an interchangeable measure. The same fact bounds the claim: the verdict is specific to the 4.0 intrinsic-difference measure, and under EMD the triad reads dyadic, so the triadicity the program studies belongs to IIT-4.0's measure, set by the 4.0 distance.

The net is that T6 is largely answered with one honest concession. The build is pinned, the config recorded,
the verdict invariant to SYSTEM_CUTS, the SIA optimization, parallelism, and reruns, and the SYSTEM_CUTS
inference corrected. The concession is that "exact IIT-4.0" is version-bound: the verdict depends on the 4.0
measure, and whether the genuine IIT-3.0 computation agrees is a separate, untested question.

## Limitations

This study pins one PyPhi commit and one IIT-4.0 config. The invariance grid is for that build. EMD on the
4.0 path is degeneracy (Φ = 0, and errors on larger systems), not a valid IIT-3.0 verdict, which comes from
the separate legacy computation and is untested here. The invariance shown is of the binary verdict, not the
Φ magnitude. Determinism is not external correctness; that rests on PyPhi's own validation.

An October 2026 check of upstream PyPhi 2.0 sits outside that grid. Upstream `wmayner/pyphi` `main` at
`134a8f31` (tag `v2.0.0rc4`, version line `2.0.0rc5.dev0`) under `pyphi.iit4_2023()` reproduces the pinned
binary conjunctive triad at `(1,1,1)` (φ_s = 2.0; Φ = 4.5, 4 distinctions, 10 relations) and the ternary
conjunctive triad (`num_states_per_node=(3,3,3)`, `S' = min(W,C)`) at `(2,2,2)` (φ_s = 1.584963, log₂ 3),
matching `feature/iit-4.0@b78d0e342` and `third_party/pyphi_iit4_mv` to machine precision. The majority triad
at `(1,1,1)` has φ_s = 1.666667. Under the 2.0 default `pyphi.iit4_2026()`, the ii(s) cap of Mayner, Marshall,
and Tononi (2026) leaves the majority triad at φ_s = 1.666667, lowers the binary conjunctive triad to
φ_s = 1.0 with that Φ-structure unchanged, and lowers the ternary state to φ_s = 0.630930. Each verdict stays
positive (φ_s > 0). The cap is φ_s = min{φ_c, φ_e, ii(s)}, with ii(s) the minimum, over cause and effect, of
the minimum of intrinsic differentiation and intrinsic specification. The majority triad in this check is the
PyPhi majority gate. The lab's three-voter rule, which scores Φ_MIP = 0 on the pinned line, is a separate model.

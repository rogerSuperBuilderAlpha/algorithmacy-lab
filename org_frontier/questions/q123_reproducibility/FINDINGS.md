# Q123 findings — the verdict is reproducible within IIT-4.0, and the SYSTEM_CUTS charge is misdirected

All four hypotheses confirmed. With the build pinned and the config recorded, the binary verdict is
bit-identical across every contested knob over all 256 forms: the flagged SYSTEM_CUTS option changes nothing,
the SIA short-circuit changes nothing, parallelism and reruns change nothing, and no alternative repertoire
measure is even an admissible config cell. The reproducibility charge is answered within IIT-4.0. The honest
residue is that the verdict is specific to the 4.0 intrinsic-difference measure, the only one that runs
non-degenerately on this path, so "exact IIT-4.0" is accurate and version-bound at once.

| pinned build | `pyphi @ b78d0e342d37175cbd55cf35a6d52ae035b4c50f` |
|---|---|
| IIT_VERSION | 4.0 |
| SYSTEM_PARTITION_TYPE | SET_UNI/BI |
| REPERTOIRE_DISTANCE | GENERALIZED_INTRINSIC_DIFFERENCE |
| CES_DISTANCE | SUM_SMALL_PHI |
| SYSTEM_CUTS | 3.0_STYLE (legacy; off the 4.0 verdict path) |

| override | verdict disagreements / 256 |
|---|---|
| SYSTEM_CUTS = CONCEPT_STYLE | 0 |
| SHORTCIRCUIT_SIA = False | 0 |
| PARALLEL = True | 0 |
| rerun | 0 |
| alternative repertoire measures admissible and non-degenerate | 0 of 13 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | SYSTEM_CUTS leaves the verdict unchanged | confirmed (0/256) |
| H2 | the SIA optimization leaves the verdict unchanged | confirmed (0/256) |
| H3 | the verdict is deterministic and parallelism-invariant | confirmed (0/256) |
| H4 | no alternative repertoire measure is an admissible cell | confirmed (0 of 13) |

From `probe_reproducibility.py`.

## What it says

The build is now pinned and the config recorded, which is the first half of the answer. The verdict runs on
PyPhi at commit b78d0e342, with the IIT-4.0 system-Φ path, the SET_UNI/BI system partitions, and the
generalized intrinsic-difference repertoire distance. Recording the commit and the config replaces the moving
branch of `requirements.txt` with a reproducible environment, so the "unpinned, mutable build" half of the
charge is addressed by the manifest the probe writes and verifies against the live environment.

The flagged SYSTEM_CUTS knob is a red herring, and the audit corrects the review on it. SYSTEM_CUTS is a
legacy IIT-3.0 option, documented as controlling "traditional IIT 3.0 cuts" for the legacy big-Φ computation,
and the IIT-4.0 system-Φ path never reads it. Toggling it from 3.0_STYLE to CONCEPT_STYLE leaves the verdict
bit-identical on all 256 forms (H1). Its value of 3.0_STYLE in the config is the option's default, idle on the
4.0 path, no sign that the verdict is a 3.0-style variant. The review's specific inference from that flag fails.

The verdict is deterministic and not an artifact of the fast path. Disabling the SIA short-circuit, the
optimization that stops early when a system is a-priori reducible, changes no verdict (H2); enabling
parallelism and recomputing the whole family a second time change none either (H3). The verdict is a
deterministic, reproducible function of the pinned build, invariant to the engineering knobs that could have
introduced run-to-run or fast-path variation.

The substantive measure has no working substitute, which both defends and bounds the claim. Of the thirteen
alternative repertoire-distance measures registered in PyPhi, twelve raise errors on the 4.0 system-Φ path,
and the one that runs, EMD, returns Φ = 0 on the canonical triad, which GENERALIZED_INTRINSIC_DIFFERENCE scores
2.0. So no alternative is an admissible, non-degenerate config cell (H4): the verdict is not one choice among a
menu, and the review's image of a silent dependence on an interchangeable measure misreads it. The same fact
bounds the claim honestly: the verdict is specific to the 4.0 intrinsic-difference measure. Under EMD the
triad reads dyadic, so the triadicity the program studies is a property of IIT-4.0's measure, not of any
distance one might plug in.

The net for the defense agenda: T6 is largely answered, with one honest concession. The build is pinned, the
config recorded, the verdict invariant to SYSTEM_CUTS, to the SIA optimization, to parallelism, and to reruns,
and the SYSTEM_CUTS = 3.0_STYLE inference is corrected. The concession is that "exact IIT-4.0" is exactly that,
version-bound: the verdict depends on the 4.0 measure, and whether the genuine IIT-3.0 computation agrees is a
separate question the agenda still lists.

## Caveats

- **One implementation, one version.** "Pinned" pins this PyPhi commit and this IIT-4.0 config; a different
  PyPhi version or a future 4.x revision is untested, so reproducibility is established for this build, not
  across builds.
- **EMD on this path is degeneracy.** EMD returns Φ = 0 here and errors on larger systems, so it is inadmissible in substance and far from a valid 3.0 reading. The genuine IIT-3.0 verdict comes from
  the separate legacy computation and is untested (agenda #8); this study does not claim a 3.0-versus-4.0
  comparison.
- **The binary verdict only.** The invariance shown is of the triadic/dyadic verdict. The Φ
  magnitude's config dependence is a separate matter, and the program already declines to treat the magnitude
  as a reliable scale.
- **Determinism, set apart from external correctness.** This shows the verdict is a stable, reproducible function of the pinned build, leaving aside whether the build computes IIT-4.0 correctly; that rests on PyPhi's own validation.

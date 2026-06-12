# Q123 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether the verdict is reproducible and config-invariant, answering the critical review's
T6. The review charged that "exact IIT-4.0 Φ" is one config of an unpinned, mutable build, and a reviewer read
SYSTEM_CUTS = 3.0_STYLE as a sign the verdict is not canonical 4.0. This study pins the build, records the
config, and tests the binary verdict's invariance across the contested knobs over the full 256-form family.
Written and committed before the run; the instrument is the classifier, re-run under config overrides.

Two scope notes fixed in advance. First, the build is pinned to a specific PyPhi commit, replacing the moving
branch in `requirements.txt`. Second, the test is of the binary verdict (triadic/dyadic), the object the
program's claims rest on, not the Φ magnitude.

## H1 — The flagged SYSTEM_CUTS knob does not change the verdict

- **Claim:** Toggling SYSTEM_CUTS between 3.0_STYLE and CONCEPT_STYLE leaves the verdict bit-identical on all
  256 forms (zero disagreements).
- **H0:** Some form's verdict changes.
- **Predicted outcome:** zero disagreements. H0 refuted. SYSTEM_CUTS is a legacy IIT-3.0 option that the
  IIT-4.0 system-Φ path does not read, so the review's specific concern is misdirected.

## H2 — The SIA optimization does not change the verdict

- **Claim:** Toggling SHORTCIRCUIT_SIA (the a-priori-reducibility short circuit) leaves the verdict
  bit-identical on all 256 forms.
- **H0:** Some verdict changes.
- **Predicted outcome:** zero disagreements. H0 refuted. The verdict is not an artifact of the fast path.

## H3 — The verdict is deterministic and parallelism-invariant

- **Claim:** Toggling PARALLEL and recomputing the family a second time both leave the verdict bit-identical
  on all 256 forms.
- **H0:** Some verdict varies across runs or parallelism.
- **Predicted outcome:** zero disagreements. H0 refuted. The verdict is a deterministic, reproducible function
  of the pinned build.

## H4 — No alternative repertoire measure is an admissible config cell

- **Claim:** Of the alternative repertoire-distance measures registered in PyPhi, none is both admissible on
  the 4.0 system-Φ path and non-degenerate on the canonical triad: each either raises an error or returns
  Φ = 0.
- **H0:** Some alternative measure runs and gives Φ > 0, a config cell that could carry a different verdict.
- **Predicted outcome:** zero admissible-and-non-degenerate alternatives. H0 refuted. The
  GENERALIZED_INTRINSIC_DIFFERENCE measure is not one cell among many; it is the canonical 4.0 measure with no
  working substitute on this path. This is the study's genuinely uncertain claim: an alternative measure could
  have run and given a non-degenerate, possibly different, verdict. (Whether the genuine IIT-3.0 verdict, from
  the separate legacy computation, agrees is a different question, untested here and left to agenda #8.)

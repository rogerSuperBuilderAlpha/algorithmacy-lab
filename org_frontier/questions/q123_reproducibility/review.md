# Q123 — Stage 1 review: reproducibility and config-invariance of the verdict

## The question

The critical review (CRITICAL_REVIEW_Q111_Q117.md, T6) charged that "exact IIT-4.0 Φ" is one config of an
unpinned, mutable build: the PyPhi pin is a moving branch with no commit, the verdict config is unreported,
and a reviewer read SYSTEM_CUTS = 3.0_STYLE as a sign the verdict is not canonical 4.0. This study pins the
build, records the config, and tests the verdict's invariance to the contested knobs.

## What the lab already knows that bears on this

- **The classifier reads the verdict from `pyphi.new_big_phi` (IIT-4.0 system-Φ), over the MIP.** Which config
  knobs that path reads, and which it ignores, decides the review's SYSTEM_CUTS point.
- **The 256-form family is enumerable and holds both classes (Q93).** It is the natural set on which to test
  whether any knob flips any verdict.
- **Whether IIT 3.0 and 4.0 agree is an open agenda item (#8).** SYSTEM_CUTS and the repertoire distance are
  where a 3.0-versus-4.0 difference could enter, so the audit must separate a config toggle from a genuine
  version change.

## The gap

The program reported verdicts without pinning the build, recording the config, or testing config-invariance.
Whether the verdict is reproducible and which config choices it depends on is untested.

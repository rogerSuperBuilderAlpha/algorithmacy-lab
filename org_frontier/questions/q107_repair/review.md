# Q107 — Stage 1 review: repair

## The question

Q106 cataloged the design operations as three reversible levers. When a triad is broken on one lever, must
the repair restore that lever, or can a different edit route around the damage? The first means coordination
has no repair redundancy; the second means a substitute condition can stand in.

## What the lab already knows that bears on this

- **The design operations are three levers (Q106).** Binding, liveness, requirement, each with a build and
  a break. Repair asks whether a break on one lever needs the build on that same lever.
- **Every edge of the minimal triad is load-bearing (Q104).** No edge whose loss the others absorb. Repair
  is the same question at the level of conditions.
- **Each condition of the law is necessary (Findings).** A necessary condition cannot be compensated by
  another, which predicts lever-specific repair.

## The gap

No study tests whether repair routes around damage. Whether a triad broken on one lever can be restored by
editing another, or whether the broken condition must be the one supplied, is uncomputed.

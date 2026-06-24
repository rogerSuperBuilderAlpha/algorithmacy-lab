# q180 — Review

## What the study claims

Splitting a coded party changes the Phi verdict often (flip rate 0.452), and the rule_to_phi CI
separates function-preserving splits from function-changing ones. H1 is supported; H2 is refuted on
its pre-registered threshold.

## Checks

- Controls pass. The faithful triad reads triadic at max_phi 2.0. Every re-aggregable split merges
  back to the base TPM exactly. A function-changing split of a triadic account reads dyadic.
- Determinism. The run reproduces byte-for-byte across three runs. Coder panels are seeded by a
  function of account, party, and mode.
- Phi is not reimplemented. The probe imports the field bridge and the classifier.

## Weaknesses a reviewer would raise

- Palette size. Seven base accounts at n=3 give 15 triadic cases per mode. The CI crossing rate of
  0.867 versus the 0.90 bar turns on two cases. A larger palette could move the rate either way, so
  the H2 refutation is a statement about this palette, not a general bound.
- The function-changing split is one construction (clamp to 0). Other function-changing
  individuations exist (a sub-node that computes a different but still integrated rule), and those
  would not always drive Phi to 0. The study tests the clamp, which is the clearest load-bearing
  case, and does not survey the space of function-changing splits.
- The re-aggregable flips deserve their own study. Function-preserving individuation that still
  flips the verdict by changing reachability is the most interesting result here, and it is reported
  but not characterized. Which hub rules are fragile under AND-aggregation is left open.
- The coder panel's dissent model is a fixed Bernoulli with one alternative reading. Real coding
  disagreement has more structure. The CI is only as good as the panel model, and the panel is a
  stand-in.

## Verdict on the verdicts

H1 is solid. The flip rate is far from both the threshold and the null, and the function-changing
mechanism is transparent. H2 is honestly refuted: the construct separates the two modes but the
function-changing crossing rate sits below the bar. Reporting the near-miss rather than relaxing
the threshold is the right call.

## Scope

Synthetic data throughout. The validation gap from synthetic rule sets to coded observed
coordination is stated and not crossed.

# Temporal-null calibration and pairwise-recurrence information limits (q221, DRAFT)

> **Target audit (2026-10-15, `TARGET_AUDIT.md`).** The q161 bottleneck-target differences reported here exist only under q161's rule-freeze convention: the frozen node is kept as a perturbed element with its edges retained. Under an IIT background-condition reading, P and Q (and the third survivor pair) have the same target {X,H}; in the second pair, one target becomes ineligible. Major complex and Φ never differ. Pairwise **statistical** non-identifiability (target A) is unaffected.

Code and data: `org_frontier/questions/q221_temporal_null_crqa_calibration/`. Status: draft, exploratory, not
preregistered. The full record is in `FINDINGS.md` and `GATES.md`.

## Abstract

q220 inferred an exact-Φ bottleneck from pairwise categorical cross-recurrence profiles and tested them
against a shuffle null. Q221 asked two questions about that design.

**Information limit.** A bounded exhaustive search over 8192 three-node forms in q220's own family, followed by
an exact screen, found **3** classes of non-isomorphic systems whose marginals, self-recurrence and
cross-recurrence profiles are equal in population at every lag. Their transition laws still differ.
- In the lead pair, the major complex and Φ are identical, but the q161 leave-one-out bottleneck set differs
  ({X,H} vs {H}), but only under q161's rule-freeze convention. Under an IIT background-condition reading, the
  targets are equal (`TARGET_AUDIT.md`).
- The difference enters through a node outside the major complex.
- Transition counts separate the systems perfectly from finite data. So the result is an information limit
  of the pairwise population representation, not finite-sample indistinguishability, not a failure of q220,
  and not an IIT theorem.

**Calibration.** A pilot on zero-lag Pearson correlation for independent binary Markov channels reproduces
the known inflation of naive-shuffle FPR (up to 67%). It makes no CRQA calibration claim.

## Results, methods and limitations

See `FINDINGS.md` §1–4, `methods.md`, and `literature/NOVELTY_ASSESSMENT.md`.

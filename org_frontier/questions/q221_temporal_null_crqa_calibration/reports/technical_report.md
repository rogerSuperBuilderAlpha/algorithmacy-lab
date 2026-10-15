# q221 technical report (2026-10-15)

This report is a short, standalone summary. The detailed sources are:
- `../THEORY.md`: proofs;
- `../FINDINGS.md`: evidence by category;
- `../GATES.md`: gate status;
- `../TARGET_AUDIT.md`: the q161 target;
- `../PYPHI_FORMALISM.md`: the IIT setup;
- `../protocol.md`: frozen specs;
- `../MANIFEST.json`: hashes and versions.

## Claim, in the narrowest defensible form

**Statement.** For noisy Boolean networks, the population pairwise categorical recurrence summaries do not
identify the multivariate transition law. The summaries are the marginals and the auto- and cross-match
profiles at every lag.

**Proof.** Proved for the invertible GF(2)-affine class (Proposition 1 and Corollary). Instantiated by three
non-isomorphic 3-node classes found by an exhaustive exact screen of the lab's existing candidate space.

**What the claim does not include:**
- It is not observational indistinguishability. The full process law differs, and so do two of the three
  bivariate laws. A plug-in transition model separates the pair perfectly.
- It is not a q220 failure claim. On held-out families, q220 is at chance against the q161 target, but this is
  exploratory.
- It is not an IIT result. Major complex and Φ are identical. The q161 bottleneck difference exists only under
  q161's freeze convention and vanishes under a background-condition reading.

## Status of targets A–D

| target | status |
|---|---|
| A | Proved (affine class) |
| B | Convention-dependent |
| C | No difference |
| D | Exploratory: at chance |

## Calibration (gate E)

Under the shuffle null, q220's own prominence statistic has an FPR of 0.27 at stay probability 0.9 and 0.43 at
0.98. Circular-shift, block and fitted-Markov nulls give 0.02–0.07. These are pilot estimates in a known data-
generating process. They re-show Yuan & Shou (2022) for this statistic.

## Main limitations

- n = 3 enumeration only.
- All three survivors are affine. The theorem does not cover non-affine rule families.
- Not run: TE, SHREC, JRP/MdCRQA and false-pair baselines.
- There is no confirmatory study.

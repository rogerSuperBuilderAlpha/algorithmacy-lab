# Holistic residual at n=4 — findings (F26)

**F26 verdict: H1 — the residual rate shrinks.** On a probe_n4_census-matched sample of N=3000
strict-mediation n=4 forms (seed 4), a Probe-125/131 cheap-feature random forest misclassifies
**71 / 3000 = 2.4%**, below the pre-registered hold band [3.3%, 6.3%] and **2.4 pp below** the n=3
baseline of 4.8% (196/4096).

In-silico; exact IIT-4.0 Φ. Hypotheses fixed in `hypotheses.md` before computing.

## Census table

| quantity | n=3 (Probe 131 / template_coverage_census) | n=4 (this study) |
|---|---|---|
| universe | 4096 unconstrained 3-node wirings | 3000 strict-mediation 4-node forms, seed 4 |
| triadic rate | 55.9% | **2.4% (71/3000)** |
| RF miss rate (holistic residual) | **4.8% (196/4096)** | **2.4% (71/3000)** |
| delta vs n=3 | — | −2.4 pp |
| F26 band | — | < 3.3% → H1 shrinks |
| false positives / false negatives | (near-boundary mix) | **0 / 71** |
| miss rate among triadic | — | **100%** |
| miss rate among dyadic | — | **0%** |
| majority-class (always-dyadic) miss rate | — | **2.4%** |
| near-boundary among misses (\|p−0.5\|<0.25) | 0.91 | **0.38** |

## Reading — shrink, with a class-imbalance asterisk

The pre-registered miss-rate comparison supports H1. The secondary majority-class baseline equals the
RF miss rate exactly (71/3000), and every miss is a triadic false negative: the forest never predicts
triadic under 5-fold CV. So the residual *fraction of the sample* shrinks because triadicity itself is
rare at n=4 strict mediation (reproducing probe_n4_census's 2.4%), not because cheap features gained
purchase on the verdict. Relative to the n=3 panel — nearly balanced at 55.9% triadic — the n=4
strict-mediation sample is a different regime. F26 as operationalized answers "does the miss rate
fall?"; the mechanism is the vanishing triadic base rate.

F27 is not reopened: the affine = residual conjecture stays **refuted** in
`org_frontier/studies/template_coverage_census/FINDINGS.md`.

## F28 note (not decisive)

Among the 71 misses, only 38% sit within 0.25 of the decision boundary (mean \|p−0.5\| = 0.287),
against 91% at n=3. That is consistent with confident majority-class errors on rare triadic forms,
not with the n=3 near-boundary scatter. A genuine F28 perturbation test on the n=3 residual set
remains the cleaner next step for phase-boundary structure.

## Scope

Strict-mediation n=4 sampling matches `probe_n4_census` / `multiparty.scaling.sample_form` as the
FINDINGS follow-up specified. It is not the unconstrained 16⁴ analogue of the n=3 4096. Synergy
features generalize Probe 125's pairwise co-input interaction to the mediator's 3-input table;
unary party reads contribute synergy 0. Panel build: ~67s for N=3000 exact Φ on this host.

## Best next experiment

**n=5 unc residual** is answered in `org_frontier/studies/holistic_residual_n5_unconstrained/`:
**9.0% (H0 holds)** near n=4's 7.5%. Series: 4.8% → 7.5% → 9.0%. Next: F28-style perturbations on
n=4/n=5 residual misses, or a feature redesign for the triadic FN tail.

## Reproduce

```
python org_frontier/studies/holistic_residual_n4/analyze_residual_n4.py
python org_frontier/studies/holistic_residual_n4/analyze_residual_n4.py --rebuild  # regenerates panel
```

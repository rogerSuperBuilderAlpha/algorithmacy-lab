# Q74 findings — whole-system verdict versus the maximal complex

All four hypotheses confirmed. The divergence between the whole-system verdict and the maximal complex is
classifiable from the coupling of the excluded elements, which gives a rule for which verdict to report.

| form | whole-system | maximal complex | excluded elements |
|---|---|---|---|
| disclosed | dyadic (Φ=0) | {E, M, R} Φ=2.0 | D read-only |
| delegated | dyadic (Φ=0) | {As, Ar} Φ=2.0 | E, R emit-only |
| monitoring | dyadic (Φ=0) | {E, M, R} Φ=2.0 | T read-only |
| chain | triadic (Φ=2.0) | {A2, R} Φ=2.0 | A1 bidirectional |

| H | Result | Verdict |
|---|--------|---------|
| H1 | spectator/frozen forms whole-dyadic, core-triadic | confirmed |
| H2 | excluded elements non-bidirectional in those | confirmed |
| H3 | chain whole-triadic, proper-subset core, excluded element bidirectional | confirmed |
| H4 | excluded element bidirectional iff whole-system triadic | confirmed |

From `probe_verdict_vs_complex.py`.

## The reporting rule

When the maximal complex differs from the whole-system verdict, the coupling of the excluded elements
decides which reading governs:

- **Every excluded element non-bidirectional (read-only, emit-only, or uncoupled to the core).** The whole
  system is dyadic and the maximal complex is triadic. The excluded elements are genuine spectators
  outside a real core, and the maximal-complex verdict is the one to report. This is the disclosed,
  delegated, and monitoring case, and it is the lab's standing "read the major complex when there are
  spectators" convention, now with a precise condition.
- **An excluded element bidirectionally coupled to the core but not in it.** The whole system is triadic
  and the maximal complex is a proper triadic subset. The exclusion is by non-pivotality (Finding 8: coupling is necessary but insufficient), and both verdicts must be reported: the whole
  system is irreducible, and the core localizes. This is the chain case.

The biconditional (H4) is the operative result: an excluded element is bidirectionally coupled exactly
when the whole system is triadic. So a single connectivity check on the excluded elements classifies the
divergence and selects the reporting.

This hardens the program's earlier claims. Q63's disclosure, Q68's monitoring/gating, and Q69's delegation
are the non-bidirectional case, where the major-complex reading is correct and the whole-system Φ=0 is the
spectator signature. Q65's chain localization is the bidirectional case, where the
whole-system-triadic verdict must be co-reported with the localized core.

## Caveats

- **Confirmatory.** The four predictions held; the contribution is the stated rule.
- **In-silico.** Boolean models, evidence about the models. Φ read ordinally.
- **Four forms.** The rule is established on four representative forms; a broader sweep of divergence cases
  would test its generality.

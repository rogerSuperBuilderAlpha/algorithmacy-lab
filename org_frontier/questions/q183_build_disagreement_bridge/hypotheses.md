# q183 — hypotheses

A bridge module reads two divergent party accounts of one coordination as two rule sets and
reports a spread tuple (verdict_agreement, phi_gap, core_jaccard). Both hypotheses are fixed
before the computation.

**H1 (zero anchor).** When both accounts are the identical rule set, the module returns
verdict_agreement = 1, phi_gap = 0.0, and core_jaccard = 1.0. The spread is a valid
zero-anchored construct: identical accounts score zero divergence.

- H1-null: the spread is nonzero on identical accounts, so the metric does not anchor at zero.

**H2 (symmetry).** Swapping which party is account A versus account B leaves verdict_agreement,
|phi_gap|, and core_jaccard unchanged. The spread is symmetric in the two parties.

- H2-null: relabelling the parties changes at least one spread component, so the construct
  encodes order rather than disagreement.

H2 is tested over a pair that actually diverges; a non-diverging pair would make the symmetry
check vacuous.

# q186 — Review

## What was claimed
The three spread components defined by the q183 bridge vary independently across a synthetic
account-pair census, rather than collapsing onto one axis. H1: not rank-one collinear. H2:
off-diagonal fraction exceeds 10 percent.

## What was run
A census of 43 account pairs (28 at n=3, 8 accounts; 15 at n=4, 6 accounts), each scored on the
three components through the reused classifier, probe library, and q183 bridge. Spearman rank
correlations across the three divergence axes; counts of the two off-diagonal patterns.

## Controls
- Instrument control: faithful triad reads 'triadic' max_phi 2.0. PASS.
- Bridge-agreement check: cached components reproduce `spread()` to 1e-9 on a sample pair. PASS.
- Anchor control: identical-account pairs give (1, 0.0, 1.0). PASS.

## Verdicts
- H1 SUPPORTED: both off-diagonal cells non-empty (14 agree-but-gapped, 1 disagree-but-samecore);
  all three Spearman rho below 1 (+0.23, +0.51, -0.09).
- H2 CONFIRMED: 0.3488 of the census is off-diagonal, far above the < 1 percent noise floor.

## Threats and limits
- Curated palette. The accounts were chosen to span the structure-by-core space, so the off-diagonal
  fraction is not an estimate of any natural population rate. The claim is existence and
  non-collinearity, which a curated palette supports; the 34.88 percent figure is a census property,
  not a prevalence estimate for real accounts.
- One disagree-but-samecore pair. The cell is non-empty, which is what H1 needs, but it is thin. A
  larger n=4 or n=5 palette would firm up that arm. The existence claim stands on the single witness.
- Phi-gap vs core-div correlation is near zero and slightly negative; this is the strongest evidence
  for independence and is not an artifact of the curation, since the two axes are read from disjoint
  parts of the Phi computation (whole-system MIP vs major-complex membership).
- Determinism confirmed: two runs byte-identical.

## Scope
Synthetic, coder-supplied accounts. No worker measured. The empirical question, whether real party
accounts populate the off-diagonal cells, is open.

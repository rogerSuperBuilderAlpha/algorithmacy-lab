# q186 — Methods

## Machinery reused
- `org_frontier.classifier.classifier` for `tpm_from_rules`, `cm_from_rules`, and the whole-system
  verdict.
- `org_frontier.probes.lib.verdict` for the structure label and max Φ_MIP over reachable states.
- `org_frontier.probes.lib.major_complex` for the major-complex core (max-Φ subset over reachable
  states).
- `org_frontier.qualitative.disagreement_phi.spread` for the three-component spread definition.

Φ is not reimplemented. The probe reads the components the q183 bridge defines.

## Account census
An account is a per-node Boolean rule set over labelled nodes. Two curated palettes supply the
accounts:

- n=3 over labels (A, B, C): 8 accounts spanning faithful triads, OR/XOR triads, a chain,
  all-AND and all-OR triads, a dyad, and a single-node self-loop. These span max Φ_MIP from 0 to 6
  and cores from a single node to all three.
- n=4 over labels (A, B, C, D): 6 accounts, including two coupled quads, a whole-system-dyadic
  account whose major-complex core is the three-node ABC subset, a two-node dyad, an account that
  reads triadic yet whose major complex is only the AB pair, and two independent dyads.

The census is every unordered pair of distinct accounts within a node count: 28 pairs at n=3 and
15 at n=4, for 43 pairs total.

## Per-pair components
Each account's (structure, max Φ_MIP, core) is computed once and cached. For each pair the three
components are read from the cache:

- `verdict_agreement` = 1 iff both accounts read the same structure.
- `phi_gap` = absolute difference of the two whole-system max Φ_MIP values.
- `core_jaccard` = Jaccard overlap of the two major-complex cores (two empty cores count as 1.0).

The cached derivation is validated against `disagreement_phi.spread` on a sample pair; the values
match to 1e-9.

## Tests
For collinearity, the three divergence axes are verdict_disagreement (1 − verdict_agreement),
phi_gap, and core_divergence (1 − core_jaccard). All three rise with divergence, so a rank-one
census would make them monotone in one another. Pairwise Spearman rank correlation is computed
across the 43 pairs with `scipy.stats.spearmanr`. The two off-diagonal cells are counted:
agree-but-gapped (verdict_agreement = 1, phi_gap > 0) and disagree-but-same-core
(verdict_agreement = 0, core_jaccard = 1).

## Controls
- Instrument control: the faithful triad `[x1, x0&x2, x1]` reads 'triadic' with max Φ_MIP 2.0.
- Bridge-agreement check: cached components reproduce `spread()` on a sample pair.
- Anchor control: identical-account pairs fix (verdict_agreement, phi_gap, core_jaccard) at
  (1, 0.0, 1.0), the agreement value of every component.

## Determinism
All RNG is seeded with `numpy.random.default_rng(0)`; pyphi parallelism and progress bars are off.
The census and every component are exact. Two consecutive runs produce byte-identical stdout.

## Scope
The accounts are coder-supplied rule sets, not measured worker states. No worker is measured. The
result characterizes the spread construct on a synthetic census; it is in-silico.

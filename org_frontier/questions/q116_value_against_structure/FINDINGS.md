# Q116 findings — strategic value and structural depth rank the parties alike, and coincide only in the small

All four hypotheses confirmed. A party's strategic value (its Shapley value of integration) and its
structural depth (the φ_d its own distinction carries) are the same number on the minimal triad, rank the
parties identically on every form tested, and part company once the coordination grows: the structural
measure concentrates value on the dominant party that the strategic measure spreads outward. Structure
predicts the order of value exactly and its magnitude only in the small.

| form | party | structural φ_d share | strategic Shapley share |
|---|---|---|---|
| triad | E / R | 0.167 | 0.167 |
| triad | M | 0.667 | 0.667 |
| principal | E / R / P | 0.067 | 0.139 |
| principal | M | 0.800 | 0.583 |
| market N=2 | each | 0.250 | 0.250 |
| market N=3 | E / C | 0.286 | 0.258 |
| market N=3 | each agent | 0.143 | 0.161 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | the two coincide on the minimal triad | confirmed (gap 0.000) |
| H2 | the two rank the parties identically on every form | confirmed |
| H3 | the two diverge cardinally on the principal | confirmed (gap 0.217) |
| H4 | structure over-concentrates where they diverge | confirmed |

From `probe_value_against_structure.py`.

## What it says

On the minimal triad the two measures are the same number. Each party's normalized singleton φ_d equals its
normalized Shapley share to three decimals: the mediator carries 0.667 of the structure's depth and captures
0.667 of the strategic value, each outer party 0.167 and 0.167 (H1). Read off the intact cause-effect
structure, with no game over coalitions in sight, the φ_d already encodes what each party is worth in the
coordination game. In the small, structural depth and strategic value are one quantity.

The order of value is structural everywhere. On every form in the panel, the two measures rank the parties
the same way: the party with the deepest distinction is the most strategically valuable, and no pair is ever
ordered oppositely (H2). The mediator outranks the outer parties on both readings; the unique market parties
outrank the agents on both. Whatever else separates strategy from structure, the ranking does not move, so a
party's structural depth fixes where it stands in the distribution of value even when it does not fix the
share.

The magnitudes part once the coordination grows. On the bidirectional principal the two distributions differ
by 0.217 in the mediator's share (H3): structurally the mediator carries 0.800, strategically it captures
0.583. The same gap, smaller, appears in the N = 3 market, where the unique parties hold 0.286 of the
structure but 0.258 of the value. The identity of the triad is a property of the minimal case, and it breaks
as parties are added.

The divergence has a direction: structure over-concentrates. Where the two part, the dominant party's
structural share exceeds its strategic share, and the periphery's strategic share exceeds its structural one
(H4). The reason is in the two definitions. The φ_d localizes depth in each party's own distinction, and
adding a party that the mediator reads enlarges the mediator's purview, inflating its distinction. The
Shapley value instead credits the added party for the marginal contributions it makes across coalitions, so
strategy redistributes outward what structure piles on the center. The strategic value is the structural
depth, smoothed by marginal contribution.

This closes the wave by joining its two halves. The cause-effect structure (Q99-Q104) and the political
economy of value (Q111-Q115) were measuring one thing from two sides. They agree exactly in the minimal
coordination, agree on rank in every coordination, and diverge in magnitude in a way that is itself
structural: the Shapley value is what the φ_d distribution becomes when each party is also credited for the
coordination it lets the others sustain. Structural depth and strategic value are the same order and, in the
small, the same number.

## Caveats

- **Confirmatory.** All four predictions held; the genuinely uncertain claim, H3 (whether the triad identity
  is universal), resolved to divergence.
- **One structural measure.** The structural reading is the singleton φ_d, the party's own distinction. Other
  structural weights (total φ_d a party participates in, relation φ_r) order the parties differently and were
  not the pre-registered measure; the match is to singleton φ_d specifically.
- **Four forms.** The panel spans the triad, one four-party asymmetric form, and the market at two sizes. The
  rank agreement (H2) held on all four; it is not proven for every coordination.
- **Coalition value as subsystem Φ.** As across the wave, the Shapley coalition value is the subsystem Φ at
  the all-ones state. In-silico, exact Φ and φ_d.

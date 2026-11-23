# Extremes don't care where the error is; middles do

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/swap_symmetry_panel/`.*

In the last post, the "any one yes" rule with three voters couldn't tell errors on the way in (the
coordinator misreads a vote) from errors on the way out (a voter misreads the coordinator): swapping the two
error rates left integrated information (Φ, computed exactly with IIT 4.0 in PyPhi) unchanged. The majority
rule could tell. Here we checked five more rules.

## What we ran

The same 25 combinations of input and output error (0 to 20% each) for: all three must agree (AND3), any one
of four (ANY4), all four (ALL4), two of four, and three of four. We predicted that the extreme rules would be
symmetric, the middle ones wouldn't, and the middle ones would get no whole-group Φ from output errors alone.

## What we found

All three predictions held.

- **Extreme rules are symmetric.** AND3, ANY4 and ALL4 give the same whole Φ when the two rates swap, to
  about fourteen decimal places. ANY4 at 2% in and 20% out, or the reverse: 1.024708 both ways.
- **Middle rules aren't.** Two of four and three of four score zero with output errors alone, at every rate.
  With input errors they score up to 0.035822, and output errors barely change that (0.035683 at 20%).
- **Mirror rules match.** Any-of-four and all-of-four give identical tables, as do two-of-four and three-of-four.

## Takeaway

Across seven voting rules, the split is clean. When a rule needs one vote or all votes, IIT treats an error
going in exactly like an error coming out. When it needs something in between, only errors going in create
whole-group integration. This is a pattern over seven cases, not a proof; deriving it is next.

*Reproduce:* `python org_frontier/studies/swap_symmetry_panel/run.py --write`

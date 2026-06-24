# q178 — hypotheses

A coded account often records an action on a graded scale (none / partial / full), then collapses
it to one bit before the rule set is built. The cut point of that collapse is a coding choice.
This study reads the collapsed rule set through the q173 bridge and asks two questions, both fixed
before the computation.

Each synthetic account fixes a graded counterpart-action level `g` in `{0, 1, 2}`. A coder's
threshold `t` in `{1, 2}` collapses `g` to a bit `b = 1[g >= t]`. When `b = 1` the counterpart C
is wired into the system rule (the worker-system-counterpart triad `[x1, x0 & x2, x1]`); when
`b = 0` the counterpart drops out and the account reads as a dyad `[x1, x0, x1]`.

**H1 (the bit cut moves the verdict).** For accounts whose underlying counterpart action is
3-valued, the binarization threshold changes the verdict (dyadic <-> triadic) for more than 20% of
accounts in a balanced panel.

- H1-null: fewer than 5% of accounts flip across all thresholds. The bit cut is verdict-neutral.

**H2 (threshold disagreement widens the CI).** When two coder panels read one threshold-sensitive
account, one panel split between the two cut points and one panel using a single cut, the
split-panel propagated Φ CI width exceeds the single-cut width by a factor greater than 2.

- H2-null: the ratio is at most 1.2. Threshold disagreement contributes negligibly to verdict
  uncertainty.

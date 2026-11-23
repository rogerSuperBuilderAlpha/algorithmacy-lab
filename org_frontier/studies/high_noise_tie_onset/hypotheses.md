# Where does the high-noise tie start on extreme quorums?

Fixed before this study's computation.

## Gap

`tie_set_membership` found that under probe 464 input noise, OR3/AND3 and ANY4/ALL4 have the full group as
the unique top subset up to η = 0.3, but at η = 0.4 and 0.45 the full group ties with every subset
containing S (7 for three parties, 15 for four). `placement_equality` found OR3's whole Φ peaks at state
0000 up to η = 0.2 and at 0111 at η = 0.4. Item 2 of `tie_set_membership/BACKLOG.md`: where between 0.3 and
0.4 does the switch happen? Values already seen: everything in those two studies (η = 0.3 and 0.4 only in
this range).

## Model

OR3 and ANY4 (AND3 and ALL4 are their bit-flip duals and are not rerun), probe 464 `input_tpm`, η from
0.31 to 0.39 in steps of 0.01. Top tie set as in `tie_set_membership` (pooled over top states, 1e-9).

## Outcomes

- H1: for each form there is one switch rate η*: at every grid rate below it the full group is the unique
  top subset, and at every rate from it upward the top tie set is every subset containing S.
- H2: OR3 and ANY4 switch at the same grid rate.
- H3: at the switch, the state where the top occurs changes from all-zero (0000 / 00000) to the state with
  S = 0 and every party 1 (0111 / 01111).

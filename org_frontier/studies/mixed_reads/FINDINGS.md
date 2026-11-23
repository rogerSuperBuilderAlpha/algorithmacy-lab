# Reading the hub backwards changes nothing real; PyPhi's default tie-break still moves 80 verdicts

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), max over reachable states, threshold 1e-9. Hypotheses pushed in
`11b47628` before computation. Control passed: with every party copying S, AND3 Φ = 3.0, MAJ3 Φ = 0, and
50/256 rules triadic (the `consensus_pivotality` values).

## Setup

Nodes P1, P2, P3, S. Read pattern r = 0..7: party i reads NOT S when bit i of r is set. S' = h(P1, P2, P3),
all 256 h, so 2,048 forms. Renaming each NOT-S reader's values turns a form into the copy-read form with
commit h_r(q) = h(q XOR r) (its "aligned twin"). Renaming is an exact symmetry, so twins should agree.

## Results

| measure | value |
|---|---:|
| tie-dependent copy-read rules (r = 0) | 24 |
| default triadic count by read pattern r = 0..7 | 50, 50, 46, 46, 46, 46, 50, 50 |
| mixed forms (r ≠ 0) whose default max Φ differs from the twin | 80 of 1,792 |
| ... of which the verdict differs | 80 |
| ... whose twin is outside the 24 tie-dependent rules | 0 |
| forms whose tie range (min, max over tie choices) differs from the twin | 0 of 2,048 |
| rule R mismatches, "triadic under some tie choice" | 0 of 2,048 |
| tie-dependent forms per read pattern | 24 in each of the 8 |

Mismatches by read pattern: r = 1: 0, r = 2: 4, r = 3: 4, r = 4: 16, r = 5: 16, r = 6: 20, r = 7: 20. In every
mismatch one side is 0 and the other is 0.471679 (48 forms) or 0.25 (32 forms). Example: r = 2 (P2 reads
NOT S) with h = 38 has default Φ 0; its twin, copy-read h = 137, has default Φ 0.471679; both have tie range
[0, 0.471679].

| hypothesis | verdict |
|---|---|
| H1: default tie-break breaks renaming somewhere, only at tie-dependent twins | SUPPORTED (80 forms, 0 outside) |
| H2: tie ranges are renaming-invariant | SUPPORTED (0 of 2,048 differ) |
| H3: rule R exact on all 2,048 when ties are counted | SUPPORTED (0 mismatches) |
| H4: 24 tie-dependent forms per read pattern | SUPPORTED |

## Reading

The alignment trick from `lockstep_symmetry` carries over to three parties: a party that reads NOT S is
the same structure as one that copies S with its values renamed. What does not carry over is PyPhi's
arbitrary tie-break, which depends on the order states are listed. Any count of triadic three-party forms
made under the default setting can be off by up to 4 of 256 for this family depending only on how the
values are labelled. Counting a form as triadic if any tied choice gives Φ > 0 removes that dependence.

Full data: [results/results.json](results/results.json).

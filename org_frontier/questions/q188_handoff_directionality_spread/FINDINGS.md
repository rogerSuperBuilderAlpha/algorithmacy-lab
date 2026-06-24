# q188 — findings

The two narrations of one handoff read as different structures. The outgoing clinician's one-way
note is dyadic; the incoming clinician's reciprocal account is triadic. The spread separates a
conveyed handoff from a bound one, and it scales with how much reciprocity the accounts disagree
about.

## H1 — one-way vs reciprocal account

| account                 | verdict | core      |
|-------------------------|---------|-----------|
| A one-way (outgoing)    | dyadic  | (O,)      |
| B reciprocal (incoming) | triadic | (I, R)    |

verdict_agreement = 0, phi_gap = 2.000000, core_jaccard = 0.000000. The incoming clinician I is in
the core only under the reciprocal account. H1 SUPPORTED.

## H2 — phi_gap vs back-channel strength

| beta | phi_recip | phi_gap  |
|------|-----------|----------|
| 0.00 | 0.000000  | 0.000000 |
| 0.20 | 0.152003  | 0.152003 |
| 0.40 | 0.321928  | 0.321928 |
| 0.60 | 0.514573  | 0.514573 |
| 0.80 | 0.736966  | 0.736966 |
| 1.00 | 2.000000  | 2.000000 |

phi_gap is strictly increasing in beta (min step 0.152003). H2 CONFIRMED.

## Verdicts

- H1 one-way dyadic / reciprocal triadic, I in core only under reciprocal: SUPPORTED
- H2 phi_gap monotone increasing in back-channel strength: CONFIRMED

## Scope

In-silico, synthetic accounts. The result characterizes how the disagreement-as-Phi-spread
instrument reads two narrations of one coordination. It does not measure a real handoff. No
clinician is measured.

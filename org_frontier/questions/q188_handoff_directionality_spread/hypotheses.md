# q188 — hypotheses

Question: in a clinical handoff, the outgoing clinician narrates a one-way note and the incoming
clinician narrates reciprocal coupling through the record. These are two accounts of the same
shift-boundary coordination over the parties O (outgoing), R (record), I (incoming). Does the Φ
spread between the accounts distinguish a conveyed handoff from a bound one?

## H1 (fixed before computing)

The one-way account is dyadic and the reciprocal account triadic, so verdict_agreement = 0. The
incoming clinician I sits in the integrated core only under the reciprocal account, so
core_jaccard < 1.

H1-null: both directionality accounts give the same verdict and the same core. Reciprocity in the
narration then leaves no Φ spread.

## H2 (fixed before computing)

phi_gap grows monotonically as the synthetic back-channel strength beta (the incoming -> record
-> outgoing coupling in the reciprocal account) rises from zero. The one-way account stays at
Φ = 0, so phi_gap(beta) equals the reciprocal account's Φ at back-channel strength beta.

H2-null: phi_gap is flat in beta. The spread then does not track the degree of reciprocity the
accounts disagree about.

## Control

The instrument control validates the classifier on the faithful triad, which reads triadic with
max_phi 2.0. A second collapse control sets the back-channel to zero in both accounts; both then
reduce to the conveyed case and the spread is zero (phi_gap = 0).

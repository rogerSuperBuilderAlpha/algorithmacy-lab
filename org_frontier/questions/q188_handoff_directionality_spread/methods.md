# q188 — methods

## Parties and state

Three parties hold the shift-boundary coordination: O (outgoing clinician), R (handoff record),
I (incoming clinician). The current state is a little-endian Boolean tuple x with x[0] = O,
x[1] = R, x[2] = I. Each account is a per-node rule list over x, turned into a state-by-node TPM
and a connectivity matrix by the classifier.

## The two accounts

One-way account (outgoing clinician's narration). O persists, R copies O, I copies R. The note
flows O -> R -> I with no return path to O.

    ACCOUNT_ONEWAY = [lambda x: x[0], lambda x: x[0], lambda x: x[1]]

Reciprocal account (incoming clinician's narration). O reads I, R = O & I, I copies R. The loop
I -> R -> O closes, so the record couples both clinicians.

    ACCOUNT_RECIP = [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[1]]

## The bridge (H1)

The two accounts go through `org_frontier.qualitative.disagreement_phi.spread`, the bridge built
by study 1 of this line. It runs each account through the exact-Φ classifier and returns
verdict_agreement, phi_gap, core_jaccard, and both_verdicts. The core membership of each account
is read from the bridge's major-complex core set.

## The back-channel dial (H2)

The reciprocal account's only tunable edge is I -> O. Its TPM sets O's next-state probability to
(1-beta)*O + beta*I, with R = O & I and I = R held deterministic. beta = 0 removes the
back-channel; beta = 1 is full reciprocal coupling. Φ is read by `max_phi_float`, which infers
the connectivity numerically and takes the max exact IIT-4.0 Φ over reachable states. The
one-way account stays at Φ = 0, so phi_gap(beta) = Φ of the reciprocal account at strength beta.
H2 tests strict monotonicity of phi_gap over beta in {0.0, 0.2, 0.4, 0.6, 0.8, 1.0}.

## Determinism

All Φ calls seed a fresh `numpy.random.default_rng(0)`, so the table reproduces byte-for-byte on
re-run. Confirmed identical across three runs.

## Controls

Instrument control: the faithful triad [lambda x:x[1], lambda x:x[0]&x[2], lambda x:x[1]] reads
triadic with max_phi 2.0. Collapse control: with the back-channel at zero in both accounts both
reduce to the conveyed case and phi_gap = 0.

## Scope

In-silico. The accounts are synthetic coder-supplied rule sets, not measured clinician behavior.
The construct scored is divergence between two stated narrations of one coordination. No clinician
is measured.

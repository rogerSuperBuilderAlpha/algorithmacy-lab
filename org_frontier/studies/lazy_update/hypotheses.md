# Lazy update: members who sometimes keep their last state instead of acting on new information

Fixed before this study's computation.

## Gap

Timing studies so far changed *when* the mediator acts: `timescale_separation` (hold-for-k and a
probabilistic 1/k commit on the mediator only), #62 sequential update, `commit_response_delay` (buffers),
`continuous_time_invariance` (CTMC embedding on the 24 corpus forms). None put memory on the parties, and
none were run on the noisy quorum hubs (OR3, MAJ3) that the noise studies (`quorum_noise_sweep`,
`noise_placement`, `placement_equality`) use. Every one of those studies lists "asynchronous update" in
its backlog. This study gives each node a self-loop: with probability λ it keeps its last state, otherwise
it updates as usual.

## Model

Mediator S over three parties, rule OR3 or MAJ3; S optionally misreads each party independently with
probability r (probe 464 `input_tpm`). Laziness λ sits in one of three places:

- **mediator**: S keeps its last value with probability λ, else commits; parties copy S exactly.
- **party**: S commits every step; each party keeps its last state with probability λ, else copies S.
- **all**: both.

λ ∈ {0, 0.1, 0.25, 0.5, 0.75}; r ∈ {0, 0.1}; 2 rules × 3 placements × 2 noise levels × 5 λ = 60 cases.
λ = 0.75 under `all` is the per-node marginal of random one-at-a-time update on four nodes (each node is
picked with probability 1/4); the exact one-at-a-time TPM is not conditionally independent and is not
computed here.

For each reachable state, φ of every subset from `new_big_phi.reachable_subsystems`; whole Φ = maximum
full-group φ over states; top tie set = subsets within 1e-9 of the largest subset φ.

Controls: λ = 0 reproduces the deterministic TPM at r = 0 (1e-12) and probe 464's `input_tpm` at r = 0.1
(1e-12); MAJ3 whole Φ at λ = 0, r = 0.1 equals 0.026981 (1e-6, noise_placement mediator value).

## Outcomes (threshold 1e-9)

- H1: noise-free MAJ3 with lazy parties only (`party`, r = 0): whole Φ ≤ 1e-9 at every λ.
- H2: noise-free MAJ3 with a lazy mediator (`mediator`, r = 0): whole Φ > 1e-9 at every λ > 0.
- H3: noise-free OR3 under `all`: whole Φ strictly decreases as λ rises from 0 to 0.75.
- H4: noise-free OR3 under `all` at λ = 0.75 is still triadic (whole Φ > 1e-9).
- H5: MAJ3's full group is never in the top tie set at any λ > 0, any placement, any r.

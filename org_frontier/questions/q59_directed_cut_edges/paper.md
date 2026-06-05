# Q59 — directed cut edges

## Question

Which directed edges in the min-norm partition cut matrices differ between the recipient and non-recipient
outer singletons, and does back-channel cross-edge placement alone account for the invariant 4-versus-2
severed-connection split?

## Panel

Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56. Instrument control: canonical triad
reads triadic, max_phi=2.0, MIP `2 parts: {W,SC}`.

## Methods

Min-norm at-system-Phi partition representatives from Q58. Directed severed edges extracted from
`partition._cut_matrix` (rows/cols W, S, C). Back-channel cross-edge identified from connectivity matrix.
Symmetric difference `only_tied` / `only_excl` compared across recipient and non-recipient outer singleton
cuts.

## Results

### H1 — Cross-edge shared severance

The back-channel cross-edge (W→C on worker topologies, C→W on counterpart) appears in both the tied and
excluded severed-edge sets on 16/16 pairs. Zero pairs show cross-edge exclusive to one cut.

### H2 — Symmetric-difference size

|only_tied|=3 and |only_excl|=1 on 16/16 pairs. Total symmetric difference is four directed edges with zero
spread.

### H3 — Cross-edge subtraction equalizes counts

Removing the cross-edge from each cut's `cut_ones` leaves adj_tied=3 and adj_excl=1 on all 16 pairs.
Adjusted counts equalize on 0/16 pairs. The cross-edge alone does not account for the 4-versus-2 split.

### H4 — Mediator edges in recipient-only difference

Exactly two mediator-incident directed edges appear in `only_tied` on 16/16 pairs. Adjusted ratio
adj_tied/adj_excl is 3.0 with spread 0.

### H5 — Recipient-template gate invariance

Worker-recipient topologies (worker_xor, worker_xnor): only_tied={S→W, W→C, W→S}, only_excl={C→S} on 8/8.
Counterpart-recipient topologies: only_tied={C→S, C→W, S→C}, only_excl={W→S} on 8/8. XOR and XNOR preserve
templates.

## Close-out

The Q51–Q58 back-channel normalization thread ends here. Q58 #190 established the 4-versus-2 count ratio.
The edge inventory shows the cross-edge is shared across both cuts; the residual 3-versus-1 asymmetry after
cross-edge subtraction comes from two mediator-incident edges in the recipient-only difference plus one
outer-party edge in the non-recipient-only difference. Partition tie-breaking follows recipient-class
templates fixed by back-channel direction.

## Validation gap

Deterministic n=3 Boolean models at finest grain with synchronous update. Results hold about the Boolean
models; real organizations remain beyond reach.

## Reproduce

```bash
python -m org_frontier.questions.q59_directed_cut_edges.probe_cross_edge_shared
python -m org_frontier.questions.q59_directed_cut_edges.probe_symdiff_size
python -m org_frontier.questions.q59_directed_cut_edges.probe_cross_subtract_equal
python -m org_frontier.questions.q59_directed_cut_edges.probe_mediator_only_diff
python -m org_frontier.questions.q59_directed_cut_edges.probe_recipient_template
```

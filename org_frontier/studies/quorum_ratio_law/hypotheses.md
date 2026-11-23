# What sets the ratio of the strongest subset to the whole on noisy counting quorums?

Fixed before this study's computation.

## Gap

Under independent input noise (probe 464 `input_tpm`), the largest subset φ of a counting quorum is a
fixed multiple of its whole-group Φ: 4 for MAJ3 and 5 for 2of4/3of4 (`quorum_noise_sweep`), 16 for 3of5
(`five_six_node_quorum_ties`, which refuted a node-count reading). Item 2 of `noise_placement/BACKLOG.md`
asks what sets it.

## Candidate law, fitted before this run (disclosed)

The four known ratios fit, after the fact, R(n, q) = Σ_{k=0}^{m−1} C(n, k) with m = min(q, n − q + 1):
MAJ3 1 + 3 = 4; 2of4 and 3of4 1 + 4 = 5; 3of5 1 + 5 + 10 = 16. The known tie sets also fit |ties| = R − 1
(MAJ3: three pairs; 3of5: 15 subsets). The law was chosen to fit these values, so they are not evidence
for it. The test is the cases not yet computed: 2of5, 4of5, 1of4, 1of5.

## Model

n parties, mediator S commits "at least q of n" over noisy readings, parties copy S. Rates e = 0.1 and 0.2
for 2of5; e = 0.2 for everything else. Cases: MAJ3, 2of4, 3of5 (recomputed controls), 2of5, 4of5, 1of4,
1of5. For each reachable state, φ of every reachable subset (`new_big_phi.reachable_subsystems`). Ratio =
largest subset φ over states / largest full-group φ over states. Tie set = subsets within 1e-9 of the top,
at the state where it occurs.

Controls: MAJ3 whole 0.036624 and 3of5 whole 0.004260 at e = 0.2 (1e-6).

## Outcomes (relative tolerance 1e-6)

- H1: 2of5 ratio = 6 at e = 0.1 and 0.2.
- H2: 4of5 whole Φ and top φ equal 2of5's at e = 0.2.
- H3: 2of5's top tie set is exactly the five pairs {S, Pi}.
- H4: |top tie set| = ratio − 1 for MAJ3, 2of4, 3of5 and 2of5 at e = 0.2.
- H5: 1of4 and 1of5 have ratio 1 at e = 0.2 with the full group in the top tie set (m = 1).

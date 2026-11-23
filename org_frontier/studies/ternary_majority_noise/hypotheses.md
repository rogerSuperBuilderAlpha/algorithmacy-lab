# Three-valued majority: does a middle option change what noise does to a majority vote?

Fixed before this study's computation.

## Gap

Every noisy-quorum study so far (`quorum_noise_sweep`, `quorum_correlated_noise`, `noise_placement`,
`placement_equality`) used yes/no parties. `quorum_noise_sweep` found that a 2-of-3 majority hub (MAJ3)
has whole Φ 0 without noise, a small positive whole Φ at every input-error rate (peak 0.036624 at
η = 0.2), and never has the full group as its major complex. `ternary_pivotality` and
`mixed_radix_mediator` ran the multivalued overlay (`third_party/pyphi_iit4_mv`) only on the
three-node W–S–C triad, deterministically. Item 4 of `placement_equality/BACKLOG.md` asks for a ternary
majority under input noise. O04 in `OPEN_QUESTIONS.md` is closed in the same pull request as this file
(the ternary_pivotality study answers it).

## Model

Mediator S and three parties P1–P3, every node with alphabet {0,1,2} (no / abstain-or-maybe / yes).
S reads each party independently; with probability r it misreads that party as one of the two other
values, chosen uniformly (r/2 each). S commits a rule over its readings; each party copies S exactly.

- **median** (three-valued majority: the middle reading), the ternary analog of MAJ3;
- **min** (the ternary lift of AND3) and **max** (of OR3).

Rates r ∈ {0, 0.05, 0.1, 0.2, 0.4}. Binary controls at the same rates with the same code on the
overlay (alphabet {0,1}, misreading = bit flip): MAJ3, AND3, OR3. Whole Φ = largest full-system φ over
reachable states (exact IIT 4.0 via the overlay, which matches the stock pin on binary input). At every
state that attains the whole Φ we also compute the maximal complex.

Values already seen before this file, in a timing pilot: ternary median at r = 0 had whole Φ 0.0;
at r = 0.2 it had whole Φ 0.033668; binary MAJ3 on the overlay at r = 0.2 gave 0.036624 (matching
`quorum_noise_sweep`). Nothing else has been computed.

## Controls (must pass or the run stops)

- C1: binary MAJ3 at r = 0.2 = 0.036624, binary OR3 at r = 0 = 3.0 and at r = 0.2 = 1.0415
  (`quorum_noise_sweep`), to 1e-4.
- C2: ternary min and max give the same whole Φ at every rate to 1e-6 (value reversal x → 2 − x).

## Outcomes (threshold 1e-9)

- H1: ternary median at r = 0 has whole Φ ≤ 1e-9 (the deterministic majority stays reducible).
- H2: ternary median has whole Φ > 1e-9 at every noisy rate (no threshold, as in binary).
- H3: ternary median never has the full group {S,P1,P2,P3} as its maximal complex at any whole-Φ
  state at any noisy rate (the membership half of the quorum law carries over).
- H4: ternary min at r = 0 has whole Φ greater than binary AND3 at r = 0 (3.0).
- H5: ternary min has the full group as its maximal complex at every whole-Φ state at every rate.
- H6: ternary median whole Φ ≤ binary MAJ3 whole Φ at every noisy rate.

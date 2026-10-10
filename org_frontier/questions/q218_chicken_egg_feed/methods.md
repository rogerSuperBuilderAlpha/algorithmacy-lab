# Q218 — Stage 4 methods

## Scope of the models
Synchronous Boolean networks of 3–4 nodes. One step is one round of a post's circulation. Rules are
encoding choices made for this study and documented below; they are not estimated from any platform's
data. "Celebrity", "feed" and "fans" are labels on nodes of stylized models. Results are evidence about
these models, not about any real platform, account, or audience.

## Shared infrastructure
Whole-system verdict: `classifier.classifier.classify_rules` (max Φ_MIP over reachable states,
PHI_EPS = 1e-9). Major complex: `probes/lib.major_complex`. Exploratory tie table: system Φ of every
subset of ≥ 2 nodes, max over reachable states (PyPhi `new_big_phi.sia`). Causal graph: the
connectivity matrix from `cm_from_rules` (an edge i→j when flipping i can change j's next value); strong
connectivity tested by reachability over that graph.

## Instrument control (run first)
Classifier factoring control dyadic, irreducible control triadic, canonical triad W'=S, S'=W∧C, C'=S
triadic at Φ = 2.000. The probe aborts otherwise.

## Node meanings (1 = active this round)
- **P** celebrity: the post is up / the celebrity posts (again).
- **F** feed: the platform shows the post to the audience this round.
- **A**, **B** two audience members: reacting to / sharing the post this round.

## Forms (¬ not, ∧ and, ∨ or)

| form | nodes | rules | encoding rationale |
|---|---|---|---|
| BROADCAST | P,A,B | P' = P; A' = P; B' = P | the post stays up or down on its own (P' = P: persistence, a self-loop, not a reaction); each fan reacts to the post independently |
| CONTAGION | P,A,B | P' = P; A' = P ∨ B; B' = P ∨ A | word of mouth: a fan reacts if they saw the post or the other fan shared it |
| WOM-REACT | P,A,B | P' = A ∨ B; A' = P ∨ B; B' = P ∨ A | as CONTAGION, but the celebrity posts again when any fan reacts |
| FEED-CHRONO | P,F,A,B | P' = P; F' = P; A' = F; B' = F | chronological feed shows any post regardless of engagement; fans react to what the feed shows |
| FEED-CHRONO-REACT | P,F,A,B | P' = A ∨ B; F' = P; A' = F; B' = F | as FEED-CHRONO, but the celebrity posts again when fans react |
| FEED-ENG | P,F,A,B | P' = P; F' = P ∧ (A ∨ B); A' = F; B' = F | engagement ranking: the feed shows the post only if it is up and drew a reaction last round; fans react to what the feed shows |
| FEED-ENG-REACT | P,F,A,B | P' = F; F' = P ∧ (A ∨ B); A' = F; B' = F | as FEED-ENG, but the celebrity posts again when the post is trending (shown by the feed) |
| FEED-ENG-COUNTS | P,F,A,B | P' = P; F' = P ∧ (A ∨ B); A' = F ∨ B; B' = F ∨ A | as FEED-ENG, but each fan also sees the other's reaction (raw counts) and joins in |
| FEED-ENG-REACT-COUNTS | P,F,A,B | P' = F; F' = P ∧ (A ∨ B); A' = F ∨ B; B' = F ∨ A | both variants |
| CHAIN (control) | P,F,A,B | P' = P; F' = P; A' = F; B' = A | a strictly feedforward relay |
| RING (control) | P,F,A,B | P' = B; F' = P; A' = F; B' = A | a closed cycle of copies |

## Encoding sweeps
The ten two-input Boolean functions that depend on both inputs: a∧b, a∨b, ¬(a∧b), ¬(a∨b), a⊕b, ¬(a⊕b),
a∧¬b, ¬a∧b, a∨¬b, ¬a∨b.
- **S1** FEED-ENG-REACT, feed rule F' = g(P, A ∨ B).
- **S2** FEED-ENG, feed rule F' = g(P, A ∨ B).
- **S3** FEED-ENG-REACT-COUNTS, audience rule A' = g(F, B), B' = g(F, A) (same g for both fans).
- **S4** WOM-REACT, celebrity rule P' = g(A, B).
S1 carries the H5 robustness decision; S2–S4 are reported and enter the H5 connectivity table.

## Decision rules
- **H1:** confirmed iff all three forms dyadic and no subset of ≥ 2 nodes has Φ > 1e-9. Refuted otherwise.
- **H2:** six checks (three verdicts, three cores). Confirmed 6/6; partial 4–5; refuted ≤ 3.
- **H3:** four checks (two verdicts, two full cores). Confirmed 4/4; partial 2–3; refuted ≤ 1.
- **H4:** three verdicts. Confirmed 3/3; partial 2/3; refuted ≤ 1.
- **H5:** three conditions (implication without exception over all 51 forms = 11 + 40 sweep variants;
  converse ≥ 90%; S1 ≥ 8/10). Confirmed 3/3; partial 2/3; refuted ≤ 1.

## Outputs
`results/forms.csv`, `results/sweeps.csv`, `results/run.txt`, `results/chicken_egg.png`.
Script: `probe_chicken_egg_feed.py` (probe #452).

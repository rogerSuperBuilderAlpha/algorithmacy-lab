# Thread — does major-complex membership track Shapley pivotality?

A deep dive into the program's one genuinely novel claim, and the one the committee pressed hardest.
The core-membership study (A) found that a party's place in the IIT-4.0 major complex rises with the
determination's single-node sensitivity to it, called the result an analogue of the Shapley value's
pivotality, and conceded the bridge was "made precise only at the null-player corner." The synthesis
committee added the sharper objection: single-node influence undercounts the higher-order joint effects
the Shapley value is actually defined over, so the moderate AUC (~0.63 unconstrained) may be the proxy's
weakness, not the correspondence's. This thread tests that directly by computing the exact Shapley value.
In-silico, on small Boolean models; reproduce with
`python -m org_frontier.threads.shapley_membership.shapley_membership`.

## Setup

For a coordination form, define a cooperative game on the parties: the value of a coalition S is
v(S) = φ_s(S), the system integrated information of the subsystem on S (maximised over reachable
states; zero for singletons). Each party's Shapley value is its average marginal contribution to
v across all coalitions. The major complex is the subset of parties that maximises φ_s — the argmax
coalition. The question: does a party's Shapley value predict whether it is in that argmax coalition,
and does it beat the single-node influence study A used?

## The arc

**Seed.** On three hand-picked forms the picture is already non-trivial. For the strict mediator
(S = W∧C) all three parties have positive Shapley value and all are in the core; for the factoring form
the decoupled party has negative Shapley and is excluded; but for the canonical irreducible control the
worker has a slightly negative Shapley value yet is in the core, and the core is a pair, not the whole.
The major complex is the argmax coalition, not the grand coalition the Shapley value distributes over —
a subtlety the rest of the thread chases.

**Q2 — Shapley beats influence decisively.** Over 200 random three-node forms, the Shapley value
predicts major-complex membership at rank-AUC 0.888, against 0.643 for single-node influence. The
committee's hypothesis holds: measuring pivotality with the higher-order Shapley value, not the
single-node proxy, sharpens the correspondence from moderate to strong. (The headline reproducible run
on 150 forms gives 0.870 vs 0.632.)

**Q3 — monotone, with categorical extremes.** Inclusion rises 0% → 55% → 100% across integer Shapley
buckets. Negative Shapley means excluded (0/33 in core), high-positive means included (57/57), and the
ambiguity is concentrated near zero. This is the Null Player axiom extended from the zero corner to a
full magnitude relation: a strongly pivotal party is in the core, a strongly anti-pivotal one is out.

**Q4–Q5 — it holds deeper and in the natural domain.** At n = 4 the Shapley advantage persists
(0.80 vs 0.58 for influence); in the strict-mediation family (where influence already does well) Shapley
matches or exceeds it (0.89 vs 0.79). The harder and larger the family — where higher-order effects
matter more — the more the single-node proxy falls behind.

**Q6 — it is a magnitude law, not a sign law.** Sign alone is not enough. In the small-but-nonzero
range |Shapley| ∈ [0.05, 0.2) sign predicts membership at chance (50.9%); only at |Shapley| ≥ 0.5 does it
reach 98.6%. There are genuine counterexamples — 42 parties with clearly positive Shapley (0.2–0.4) that
are excluded. They are the structural residue: a party can contribute on average across coalitions yet
not belong to the single best one, because the major complex is the argmax coalition and the Shapley
value averages over all of them.

**Q7 — the Shapley value specifically is the best predictor.** Among pivotality notions, the Shapley
value (average marginal contribution over all coalitions, AUC 0.870) beats the best-coalition marginal
(0.827), the grand-coalition marginal v(N) − v(N∖{i}) (0.728), and single-node influence (0.632). The
major complex does not merely track "some" pivotality; it tracks Shapley pivotality in particular, more
than the simpler "how much does the party add to the whole" or "to its best coalition."

## What the thread establishes

Major-complex membership tracks the exact Shapley value over the φ_s coalition game at rank-AUC ≈ 0.87
(three nodes), categorically at the extremes and best among pivotality notions — far above the ≈ 0.63
of the single-node influence the core-membership study used. This answers the committee's challenge: the
moderate AUC in study A was the proxy's weakness, not the correspondence's, and the IIT-to-Shapley bridge
holds well past the null-player corner once pivotality is measured properly. It is a candidate to fold
back into study A as the sharpened statement of its pivotality result.

## Limits, honestly

It is not a clean equivalence (AUC ≈ 0.87, not 1.0), and the gap is structural, not noise: the major
complex is the argmax coalition while the Shapley value averages over all coalitions, so positive-Shapley
parties can miss the best coalition. The coalition value v(S) = φ_s(S) is one natural choice; a different
value function (per-capita φ_s, or a coalition-formation solution concept selecting the argmax coalition
directly) might fit better and is the natural next question. Everything is in-silico, on small Boolean
models; the AUCs are over a sampled population of forms and depend on it; exact Shapley is feasible only
at the small sizes exact Φ already restricts the lab to. The result strengthens an analogy between two
formal objects on these models; it does not derive one from the other.

The coalition-structure thread takes up that next question and revises this account of the gap. Scoring
each coalition by its φ_s maximized across all states mixes states the way the major complex does not:
the complex forms at one state. Score the same node-level marginal at that state and it predicts
membership at AUC 0.98, so most of the 0.87 ceiling here is the cost of state aggregation rather than the
argmax-versus-average mismatch this section blamed it on. See
`org_frontier/threads/coalition_structure/THREAD.md`.

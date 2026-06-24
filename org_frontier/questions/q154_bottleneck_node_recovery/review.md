# q154 — Review

## What the study claims

Coupling centrality fails to recover the structural articulation point of a bottleneck form, at 28.3%
on unique-articulation forms against a 25% chance floor and a 70% threshold, and transfer-entropy
throughput beats it at 66.7%. Both hypotheses are refuted. The numbers come from a deterministic probe;
three consecutive runs are byte-identical.

## Strengths

The ground truth is principled and computed, not assigned: leave-one-node-out drop in exact major-complex
Φ. The tie handling is honest. The ats form's all-tied ground-truth set is flagged as carrying no
recovery test rather than counted as a 100% success, so the headline rests on the two forms with a single
articulation point. The control is the right one: a degree-matched form with no articulation point, where
the pickers spread across nodes and invent no bottleneck. The negative result is reported straight.

## Limits

The unique-articulation evidence is two forms. Two forms cannot fix a rate; 28.3% pools 0/30 and 17/30,
which are very different behaviors. The claim that coupling centrality fails should be read as "fails on
these two constructed forms, badly on one," not as a measured failure rate. A broader sweep of
unique-articulation forms would turn the two-point split into a distribution.

The major complex on the joint and degree forms is two nodes wide at base Φ 2.0. The articulation node
is load-bearing for a small complex, and the trajectory's coupling structure is dominated by the wider
set of active nodes. The mismatch between a narrow structural pivot and a broad behavioral signal is real
but may be specific to small complexes; whether it persists as the complex grows is open.

H2 is decided on the same two forms as H1. TE throughput beating coupling centrality is a clean
within-study comparison, but it is not a general claim about the two estimators.

## Verdict

The probe is sound, deterministic, and honestly reported, and the two refutations follow from the
numbers. The evidence base is thin (two unique-articulation forms), so the finding is a bounded negative
result on constructed forms, not a law. A follow-up should sweep many unique-articulation forms and vary
complex size before the claim that behavioral centrality misses the articulation point is stated as
general.

## Scope

In-silico throughout. Exact Φ on small Boolean forms; the empirical arms on synthetic trajectories. No
real coordination is reached, and the recovery rates are baselines on synthetic data.

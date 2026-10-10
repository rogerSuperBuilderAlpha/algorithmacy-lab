# Probe 457 — weighted and noisy quorums: hypotheses (fixed before computing)

## Question

The quorum law holds for clean k-of-n counts: a threshold mediator binds the full party set at the
any-one and unanimity extremes and factors at every interior threshold (probe 117; coordination-logic
atlas, study D). The atlas names the open extension in its limits: "weighted or noisy quorums are untested
and would show whether the extremes-only law survives perturbation"
(`org_frontier/studies/coordination_logic_atlas/FINDINGS.md`). This probe asks whether the law survives
when every weighted threshold rule at three and four parties is enumerated, and when the mediator's
commit is noisy.

## Prior record

- Probes 10 and 67: AND and OR bind all three parties at Φ = 3.0; the 2-of-3 majority factors.
- Probe 116: the conjunctive law, Φ = n−1 with the full node set as the core.
- Probe 117 (`probe_threshold_scaling.py`): at three and four parties only k = 1 and k = all keep the
  full core; every interior k-of-n factors with no core.
- Coordination-logic atlas (study D, landed in PR #110): the same law across four party counts, with
  substitutability named as the mechanism.
- Probe 110 (`probe_ejection_order.py`): one weighted family, S = 1 iff W + C + w_P·P ≥ 2, swept over
  the principal's weight w_P. It is a single one-parameter path through weight space.
- Q215 (`org_frontier/questions/q215_phi_family_robustness/`, run on PR #510 and landed through
  PR #513): the interior-quorum zero is specific to IIT 4.0. The 2-of-3 quorum reads Φ = 0.000 under
  IIT 4.0 and 1.269 under IIT 3.0. Every verdict in this probe is an IIT 4.0 verdict and inherits
  that dependence.

## Relation to open PR #808

Open PR #808 ("Probe 122: weighted voting & supermajority stress test", unmerged at the time of writing)
classifies nine hand-picked rules at three parties, four of them weighted with one privileged party.
This probe differs in four ways. It enumerates every distinct weighted threshold function at three and
four parties up to relabelling of the parties, with a saturation check on the weight range. It reads
membership against each function's relevant set and swing counts. It adds a noisy-commit arm. It
pre-registers decision rules before any form is classified. The weighted rules in #808 fall inside the
enumeration as special cases; the probe reports each of them where it lands, and any disagreement with
the numbers stated in #808 is reported as a finding.

## Form

Nodes: 0 = S (the mediator), 1..n = parties P1..Pn, with n ∈ {3, 4}, so forms have four or five nodes.
Each party copies the mediator, P_i' = S. The mediator commits a weighted threshold of the parties,
S' = f(P) with f(x) = 1 iff Σ w_i·x_i ≥ θ. This is the wiring of `threshold_hub` in probe 117, so the
unweighted rows reproduce probe 117 exactly.

## Enumeration

1. Weights w_i range over the integers 0..5 and the quota θ over 1..Σw_i. Each (w, θ) gives a truth
   table over the 2^n party assignments.
2. Constant functions are dropped.
3. Truth tables are deduplicated, then reduced to one representative per class under permutation of the
   parties: the representative is the lexicographically smallest truth table among the n! relabellings.
   All parties have identical wiring, so relabelling is a symmetry of the form and leaves every reading
   unchanged.
4. Saturation check: the enumeration is repeated with weights 0..6. If the larger range yields any class
   absent from the 0..5 range, the enumeration at that n is incomplete; the probe prints
   `SCOPE_INCOMPLETE` for that n and scores no hypothesis there.
5. The probe prints the number of distinct classes at each n. No count is asserted here in advance.

Four-party classes include three-party functions with one irrelevant party. Those are classified as
five-node forms, since the irrelevant party still copies S.

## Definitions

- **Relevant set R(f).** The parties i for which some assignment of the other parties makes f change
  when x_i flips.
- **Raw swing count β_i.** The number of assignments of the other n−1 parties for which flipping x_i
  changes f. A party is relevant iff β_i > 0.
- **Extreme class.** f equals the AND of the parties in R(f) or the OR of the parties in R(f). With
  |R| = 1 the function is a dictator.
- **Mixed class.** Every other function. A monotone function of two relevant parties is AND or OR, so a
  mixed class has |R| ≥ 3.
- **Readings.** The whole-system verdict is `org_frontier.probes.lib.verdict` (max Φ_MIP over reachable
  states, triadic iff Φ > PHI_EPS = 1e-9). The core is `org_frontier.probes.lib.major_complex`.
  "Parties in the core" means the core minus S.

## Control gate

The probe classifies no enumerated form until every control below passes. A failure stops the run with
no verdict printed.

- **C1a.** The classifier controls of `org_frontier.classifier.validate` pass: the decoupled form reads
  dyadic and the fully coupled form reads triadic.
- **C1b.** The probe 117 anchors reproduce with this wiring: at three parties, AND and OR read triadic
  with Φ = 3.000 and the full node set as the core, and 2-of-3 reads dyadic with no core.
- **C2.** At noise ε = 0 the stochastic-TPM path reproduces the deterministic reading of every class:
  the same core and |Δφ| ≤ 1e-9.
- **C3.** At ε = 0.5 the mediator's next state carries no information about the parties. Every class
  must then read dyadic, with no core containing two or more parties.

C2 and C3 gate the noise arm only. If either fails, H5 and H6 are reported as `NOT_TESTABLE
(instrument)`, and H1 to H4 stand on C1 alone.

## Hypotheses

### H1 — Extreme classes bind their relevant set

- **Claim.** For every extreme class with |R| ≥ 2, the major complex is exactly {S} ∪ R.
- **H0.** Some extreme class with |R| ≥ 2 has a different major complex.
- **Decision rule.** SUPPORTED if the claim holds in every such class at n = 3 and n = 4. REFUTED if any
  class violates it; each violating class is listed.
- **H1b, secondary.** The core's φ equals |R|, extending the conjunctive law Φ = n−1 to the relevant
  subset. SUPPORTED if |φ − |R|| ≤ 1e-6 in every such class; REFUTED otherwise.

### H2 — Irrelevant parties stay out

- **Claim.** No party outside R(f) is in the major complex, in any class.
- **H0.** Some irrelevant party is in a major complex.
- **Decision rule.** SUPPORTED if there are zero violations across all classes. REFUTED otherwise.
- **H2b, secondary.** Every class with an irrelevant party reads dyadic at the whole-system level: the
  copying party is a spectator, as in the atlas spectator forms. SUPPORTED if all such classes read
  dyadic; REFUTED otherwise.

### H3 — Mixed classes never bind more than one party

- **Claim.** For every mixed class, the major complex contains at most one party, or no complex exists.
- **H0.** Some mixed class has two or more parties in its major complex.
- **Decision rule.** SUPPORTED if zero mixed classes at n = 3 and n = 4 have two or more parties in the
  core. REFUTED if any does; each such class is listed with its weights, quota, core, and φ. This is the
  uncertain claim of the probe. Probe 110 found a core of {S, P} on one mixed function, and no prior run
  covers the full mixed space.

### H4 — The surviving party holds the largest swing count

- **Claim.** In every mixed class whose core contains exactly one party, that party has the strictly
  largest raw swing count β_i.
- **H0.** Some such class keeps a party that does not hold the unique maximum β_i.
- **Decision rule.** Classes whose maximum β_i is tied are excluded from scoring and counted. SUPPORTED
  if the claim holds in every scorable class. REFUTED if any scorable class violates it. NOT_TESTABLE if
  fewer than three classes are scorable.

## Noisy quorums

The mediator's commit is flipped with probability ε:
P(S' = 1 | x) = (1 − ε)·f(x) + ε·(1 − f(x)), for ε ∈ {0, 0.05, 0.10, 0.20, 0.30, 0.40, 0.45, 0.50}.
Party rules stay deterministic. Every distinct class at n = 3 and n = 4 runs at every ε. The state-by-node
TPM goes to `org_frontier.classifier.classifier.classify` for the whole-system verdict. The core comes
from a TPM-input copy of `lib.major_complex`, which makes the same `new_big_phi.maximal_complex` call over
reachable states; C2 checks that copy against the deterministic path. Noise on the party inputs, as
opposed to the commit, is outside this pre-registration.

### H5 — Noise preserves extreme-class membership

- **Claim.** For every extreme class with |R| ≥ 2, the core stays {S} ∪ R at every ε < 0.5, and the
  core's φ is non-increasing in ε.
- **H0.** Membership changes at some ε < 0.5, or φ rises between consecutive grid points by more
  than 1e-9.
- **Decision rule.** SUPPORTED if both parts hold in every such class. REFUTED otherwise; each change
  or rise is listed with its ε.

### H6 — Noise does not rescue a mixed quorum

- **Claim.** No mixed class has two or more parties in its core at any ε in the grid.
- **H0.** Some mixed class gains a core with two or more parties at some ε > 0.
- **Decision rule.** SUPPORTED if there are zero such cases. REFUTED otherwise; each case is listed.

## Reporting

Each hypothesis prints one line, `Hk (...): SUPPORTED | REFUTED | NOT_TESTABLE`, followed by the
per-class table: weights, quota, relevant set, class type, whole-system verdict and Φ, core and φ, and
β. Refuted and untestable hypotheses are reported as findings. Any analysis added after this file is
committed is labelled post hoc.

## Scope

Every result is in-silico: exact IIT 4.0 Φ, computed with PyPhi's IIT 4.0 line, on Boolean models of
four and five nodes. The forms are evidence about these models. They are not measurements of any
committee, platform, or organization, and the validation gap to real coordination is unchanged. The
interior-quorum zero depends on the IIT 4.0 measure (Q215); a reading under another member of the Φ
family could differ.

# Wave 10 — designs for the parked projects

Five projects in the research program cannot run on the current toolchain or without new data. They
are not experiments to compute. They are designs to write, so the work that would answer them is ready
when the tool, the dataset, or the subjects exist. This document states each one as a runnable plan.

The numbering matches the agenda (#5, #8, #24, #41, #42) and continues the program's logbook past
Probe 98. None of these has a verdict yet. Each entry states the question, what is missing, and the
exact procedure that would settle it.

## #5 — Multivalued pivotality (tooling absent)

Question. The two-condition account was found on binary parties. Does it hold when a party has more than
two states — a worker who can be idle, engaged, or overcommitted; a counterpart with a graded position?

What is missing. PyPhi on the IIT-4.0 branch represents binary nodes. Multivalued IIT (Gomez et al.
2021) needs the multivalued extension, which is not installed on this branch and does not share the
`new_big_phi` API the classifier uses.

Procedure once the tool exists.
1. Lift the classifier's `tpm_from_rules` to k-valued nodes: a node's update is a function into
   {0,…,k−1}, and the TPM is state-by-node over a mixed-radix state space.
2. Rebuild the n=3 triad with ternary parties (W, C ∈ {0,1,2}) and a ternary commit S = g(W, C).
3. Recompute the major complex and the per-node influence (Boolean sensitivity generalizes to the
   fraction of states where changing a node's value changes another node's next value).
4. Test the two conditions: a non-bidirectional ternary node should stay out of the core, and among
   bidirectional ternary nodes the in-core probability should rise with influence.
Expected discriminator. If the law holds, the verdict and the influence-rank-AUC reproduce the binary
result. If ternary parties break it, the place to look is whether graded states create partial
irreducibility the binary cut hides.

## #8 — IIT-3.0 versus IIT-4.0 on the verdict (tooling absent)

Question. Does the dyadic/triadic verdict depend on the IIT version? The classifier uses 4.0 (the
`new_big_phi` SIA). Would 3.0's big-Φ give the same binary calls on the corpus?

What is missing. An IIT-3.0 configuration. The installed PyPhi is pinned to the 4.0 branch; 3.0 uses a
different Φ definition (earlier EMD-based distance, different partition search) and a different config.

Procedure once the tool exists.
1. Install a 3.0-capable PyPhi in a separate environment.
2. Run both versions over the 256-form corpus, recording each form's big-Φ and the binary verdict
   (Φ over the MIP > ε).
3. Cross-tabulate the two verdicts. Report the agreement rate and characterize every disagreement
   (which forms flip, and whether 3.0 or 4.0 calls them triadic).
Expected discriminator. High agreement supports reading the verdict as version-robust. Systematic
disagreement on a class of forms would say the construct is tied to the 4.0 partition geometry and the
claim must name the version.

## #24 — The verdict from real interaction logs (data needed)

Question. Can the dyadic/triadic verdict be estimated from a real organization's interaction log
(messages, handoffs, decisions over time), not just from a known TPM?

What Wave 7 already settled. The synthetic half of this question is answered. On simulated trajectories
of the corpus, the verdict is recoverable from time series: the Barrett–Seth Φ_AR separates the groups
at AUC 0.925 (Probe 84), and a random forest over cheap features recovers it outright, AUC 1.000
(Probe 85). The ΦID proxy Φ_R fails, and no trajectory length or redundancy/noise setting fixes it
(Probes 86, 87). So estimability is established in principle; what remains needs real data.

Validation protocol for a real dataset.
1. Choose a coordination episode with a clear worker, system/platform, and counterpart, and a logged
   discrete signal per party over time (active/idle, committed/not, present/absent).
2. Discretize each party's signal to a binary (or, with #5, k-valued) time series on a common clock.
3. Compute the Probe-85 feature panel (per-node entropy, pairwise mutual information, transfer entropy,
   O-information) and the Φ_AR estimate (Probe 84) on the log.
4. Score the trained surrogate to get a verdict and a confidence. Where a ground-truth structure is
   known (the platform's documented rule), compare.
5. Report the verdict, the surrogate's confidence, and the features that drove it.
Synthetic stand-in available now. The proxy-bridge pipeline (`proxy_bridge/`) plus the Probe-84/85
estimators are the runnable stand-in: generate a log from a known form, hand it to the estimator blind,
and confirm the recovered verdict. This is the dry run the real-data protocol would follow.

## #41 — Human subjects: the difficulty gap (design only)

Question. Do people coordinating through a triadic interface show a larger learning or error cost than
people coordinating through a dyadic one, holding the task fixed?

What is missing. Human subjects and ethics approval. This is a behavioral experiment, not a computation.

Design sketch (for pre-registration).
- Manipulation. Two interfaces for the same three-party task. Dyadic: each pair coordinates through a
  channel that forwards state (a conveyor). Triadic: a shared commit node both parties jointly set and
  then act on (the Probe-88 joint-commit structure).
- Participants. Triads, randomly assigned to interface, with a within-task practice block.
- Primary outcome. Trials-to-criterion and steady-state error rate.
- Hypothesis (pre-registered). The triadic interface yields more trials-to-criterion and higher early
  error, with the gap shrinking as the algorithmacy is learned.
- Caution from Probe 98. Independent-learner difficulty did not track the verdict for selfish bandit
  agents. The human prediction rests on the joint-commit interface imposing a coordination demand the
  conveyor does not, not on a generic "triadic is harder" claim. The design must make the joint demand
  explicit, or it risks the Probe-98 null.
- Analysis. Mixed-effects model with interface as the fixed effect and triad as a random effect;
  pre-registered effect-size threshold and stopping rule.

## #42 — Inter-rater coding of real organizations (design only)

Question. Can trained coders look at a real coordination arrangement and agree on whether it is dyadic
or triadic, reliably enough to use the construct as a measurement instrument?

What is missing. A coding instrument, coders, and a sample of organizations. This is a measurement-
reliability study.

Design sketch.
- Instrument. A decision sheet that operationalizes the two conditions as observable questions: does
  each party both constrain and respond to the others (bidirectional coupling), and does removing any
  one party change what the others can do (pivotality). Each question has anchored examples.
- Sample. A set of documented coordination arrangements (platform-mediated work, committee decisions,
  broker relationships, escrow and clearing arrangements) spanning the expected range.
- Procedure. At least two independent coders per case, blind to each other and to the hypothesis.
- Reliability. Report Cohen's/Fleiss' κ on the binary verdict and on each sub-question. Pre-set a κ
  threshold for "usable instrument."
- Validation against computation. Where an arrangement can be modeled as a small Boolean form, run the
  classifier and compare its verdict to the coders'. Agreement ties the human instrument to the exact
  measure.

## Status

The runnable program (Lanes R and X) is complete: Probes 54–98 close every computable project in the
agenda. The five projects above are the program's edge — what the construct would need next is a
multivalued tool, a cross-version check, real interaction logs, and two human studies. Each is a written
plan, not an open question of method.

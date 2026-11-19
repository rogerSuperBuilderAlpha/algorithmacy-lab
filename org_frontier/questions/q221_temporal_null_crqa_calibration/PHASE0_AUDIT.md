# Q221 phase-0 audit — repository evidence and reuse map

**Status:** Retrospective source and findings audit. Not a prospective preregistration, and not an amendment to q153, q159, q161 or q220. Source: current PR #842 branch, inspected 2026-10-15.

## Previous studies and what they actually established

| Study | Evidence on current branch | Consequence for Q221 |
|---|---|---|
| q153 triadic/dyadic classifier | 45 synthetic forms; 5-fold held-out accuracy 0.5556 vs majority-class baseline 0.6000; prominence spread strongest standardized feature | Existing four-feature classifier does not exceed majority-class baseline on that corpus; does not establish a universal inability of recurrence to predict Phi |
| q159 length-to-verdict curve | 95 synthetic forms; 92.63% settled at 600 steps relative to the study's reference reading; agreement with exact Phi verdict at 600 steps 0.8000 | Stability of a prediction and accuracy of that prediction must be separated; longer trajectories do not automatically solve structural proxy validity |
| q161 noise-robust verdict | 16 forms; bottleneck agreement varies 0.753 to 0.844 over flip 0.02..0.30, better and flatter than triadic/dyadic verdict | The lab target is the **set of maximizers of leave-one-node-out decrease in major-complex Phi**. This is a lab-defined derived target; the legacy predictor is an argmax centrality *node*, not full-set estimator |
| q220 observation-process robustness | Observed loss, masking, timestamp-aware lag pairing and chance/tie-aware bottleneck scores; Stage-2 R1 reused curated forms, R2 generated new forms. The historical follow-up audit is separately discussed in PR #841 | Pairwise categorical cross-recurrence summary is a narrow measurement. Do not use q221 results to rewrite q220 historical numbers or infer failure on the entire q220 corpus |

## Exact implementation interface

- Ground truth: q161 probe_noise_robust_verdict.py derives exact-phi major complex from deterministic transition rules; bottleneck_set computes base major-complex Phi and the drop after setting each node's *update rule* to the constant zero, retaining the rest of the network. Ties are allowed among maximizing positive drops. A clamp-to-one sensitivity check was independently added in q221.
- Observation: org_frontier/recurrence/crqa.py trajectory samples synchronously updated Boolean systems with independently drawn flips and a fixed warmup. In q220 stage 2 the default is 600 steps, 20 warmup, flip=0.08.
- Estimators: q220 stage2/observe.py computes categorical match-rate profiles at integer time differences. "index" gaps close observations; "timestamp" pairs only genuine lag-separated observations; "segment" further requires a contiguous observed segment.
- Decoder: q220 observe.coupling computes cross-channel profiles for unordered pairs (mirrored prominence and opposite lag on reverse orientation). observe.centrality sets the diagonal to zero and aggregates prominences exceeding 0.05. observe.bottleneck_scores returns tie-aware score |M intersect B|/|M| where M is the maximum-centrality node set. All-zero centrality yields score |B|/n and a no-evidence flag.
- Null: q220 stage2 shuffles **each observed channel independently over time** and passes the shuffled trajectory through the same observation mask/estimator. This preserves individual categorical frequencies but generally destroys serial dependence. It is not a generic causal-null model or a validated exact significance test for the IIT bottleneck.
- Unit of generalization: network **form**, not trajectory seed or surrogate replicate. Within-form seed averaging can characterize performance on a fixed form but does not provide a generalization estimate across unseen forms.

## Critical Q221 inference boundary

Q221's lead pair has equal population auto/cross match profiles and distinct **complete** q161 bottleneck sets B(P)={X,H} vs B(Q)={H}. These targets share node H. Thus no decoder based only on the identical population summaries can reconstruct both *complete sets exactly*, but a single-node selection of H is correct on both (tie-aware score 1). Accordingly:
- Do not claim the counterexample forces the existing q220 single-node decoder to fail.
- Do not claim different maximum Phi or major-complex membership; pinned outputs agree on both.
- Do not claim finite-sample feature distributions or full observed trajectories are equivalent. In recorded tests the full transition-aware baselines distinguish the models.

## Reuse and isolation

Reuse existing q161 target functions and q220 trajectory, observe.coupling, centrality and bottleneck_scores **read-only**. Q221's standalone exact-rational checker independently reconstructs transition kernels and proofs, without importing PyPhi. Keep expensive pinned IIT verification in the separate identifiability scripts and its receipts. Do not alter q153/q159/q161/q220 results or #841's post-merge audit while publishing Q221.

## Remaining methodological limitations

No prospective independent-form calibration study for q221's null has been run. The naive-shuffle pilot tests zero-lag Pearson correlation on binary Markov series, not the q220 decoder. A publication-grade novelty review and external generalization study remain outside this exploratory scope; neither should be represented as completed.

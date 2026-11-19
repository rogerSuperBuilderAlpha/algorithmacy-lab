# O13 (with O09) — the verdict read from a real interaction log: estimating the TPM

Pre-registration, Antonio Mele, 30 Oct 2026. Committed before any data is fetched or any estimate on the full window is computed. Follows
`org_frontier/recurrence/packets/template/PRE_REGISTRATION.md` and `WAVE10_PARKED_DESIGNS.md` #24.
The pilot below used only the CSVs already in `bot_merged/`; no
new data has been fetched.

## Question
Can the dyadic/triadic verdict (Φ>0 with a multi-party major complex vs not) be *estimated*, with calibrated
uncertainty, from a logged real coordination, instead of being read off an elicited Boolean model?
Secondary (O09): does the recurrence instrument (CRQA lead-lag) on the same log agree with the estimated
structure?

## Prior work in the repo
- `org_frontier/designs/WAVE10_PARKED_DESIGNS.md` #24: estimability shown on synthetic trajectories
  (Φ_AR AUC 0.925, Probe 84; random-forest surrogate AUC 1.000, Probe 85; ΦID Φ_R fails, Probes 86-87).
- `org_frontier/recurrence/bot_merged/` (v11): Kubernetes Prow/Tide, 150 PRs, 100% bot-merged; the
  *elicited* Prow model is triadic, Φ=2.0, core {approval, bot, codebase}; bot is a member but a functional
  conduit (collapsing it keeps Φ=2.0). Reproduced on this box.
- `recurrence/event_series` (v9, human merger), `review_heavy` (v10), `real_series` (commit activity).
- `org_frontier/field/rule_to_phi.py` (coding disagreement → CI), `proxy_bridge/`.
- Open PR #842 (q221): pairwise recurrence summaries do not identify the transition law, while transition likelihood does; this plan therefore reads Φ from an estimated TPM, with CRQA only as the H5 cross-check.
- Gap this fills: every Φ so far is on an elicited or synthetic TPM; none estimated from a log.

## Arrangement and data
Primary: **GitHub bot-merged projects via GH Archive** (gharchive.org; hourly JSON.gz of public GitHub events
since 2011; one hour checked = ~21.8 MB compressed; open). Parties per PR-repo, on an hourly (or 4-hour) clock:
- Worker W = contributor activity (PushEvent / PullRequestEvent opened|synchronize by non-maintainers).
- Mediator M = merge bot (k8s-ci-robot / Prow / bors / mergify / github-actions merge, from
  PullRequestEvent closed+merged with bot `merged_by`, or bot IssueCommentEvent).
- Counterpart C = human gatekeepers (PullRequestReviewEvent approved, `/lgtm`/`/approve` comments by
  OWNERS).
- Optional 4th/5th nodes: CI status (CheckRun/Status events are *not* in GH Archive — use bot comments),
  codebase change (push to default branch).
Design contrast (the instrument's lever): projects with a merge bot (kubernetes/kubernetes, rust-lang/rust
via bors) vs matched human-merge projects. Fallback/second site: Wikipedia bot edits (mediawiki_history
dumps; bot flag logged) for a W/bot/patroller triad.

## Encoding
Node bit = 1 if ≥1 qualifying event in the bin. Pre-committed: bin = 1 hour primary; 15 min and 4 h as
robustness. Lag 1 bin (Markov order 1) primary; order-2 tested as a check. Per-repo marginal rates must lie
in [0.05, 0.95] or the bin is changed *before* Φ is computed (pilot below shows daily bins saturate).

## Estimation
1. State-by-node TPM, n ≤ 5 primary (≤ 8 exploratory; exact IIT 4.0 cost limits to ~10-12).
2. Each cell P(x_i,t+1=1 | x_t=s) gets a Beta(a,a) prior (a=1 primary, 0.5 sensitivity) → conjugate posterior.
3. Structural alternative: per-node Boolean/logistic rule over parents with lag; parent sets chosen by BIC
   (or Bayesian model averaging over ≤ 2^(n-1) parent sets); TPM implied by the selected rules + a noise ε.
4. Uncertainty → Φ: draw K=500 posterior TPMs (or block-bootstrap the series, block = 1 day), compute
   max-over-states major complex Φ and core for each; report median, 90% interval, P(multi-node core with
   W, M, C ⊂ core), and core frequency table.
5. Nulls: per-node circular-shift surrogates (keep autocorrelation, break coupling); same pipeline.
6. Identification: unvisited states are prior-filled → report coverage; IIT perturbs all states, so
   Φ on prior cells is assumption-driven; interventional states only identifiable from natural variation
   (bot outages, holiday freezes, policy changes = quasi-experiments). Common drivers (time-of-day) handled
   by detrending/conditioning on hour-of-week, or adding a clock node.

## Hypotheses (each with its null)
- H1 (coverage). With hourly bins ≥ 6/8 states of (W,M,C) are visited ≥ 30 times in a 90-day window.
  Null: coverage fails → the estimate is prior-dominated and no verdict is read.
- H2 (structure). In bot-merged repos the estimated TPM gives a multi-node major complex containing M and C
  in ≥ 80% of posterior draws. Null: core is single-node or excludes M/C (dyadic reading).
- H3 (conduit). Collapsing M (C reads approvals directly) changes posterior median Φ by < 10%, reproducing
  v11's "member but conduit" result on estimated rather than elicited structure. Null: Φ drops ≥ 10%.
- H4 (contrast). Bot-merge repos vs human-merge repos differ in core composition, not in Φ>0 rate.
  Null: no difference in either.
- H5 (instrument agreement, O09). CRQA cross-recurrence of C→M shows a positive lag peak (approval leads
  merge) with prominence above threshold, matching the estimated C→M edge. Null: flat/zero-lag profile.

## Decision rules
- Instrument controls must pass first (`run_study.py`): decoupled → no multi-node complex; coupled cycle → Φ>0
  full core. Note from pilot: a self-loop node alone yields a single-node complex with Φ=1, so the verdict
  is read from the *multi-node* core, not raw Φ>0.
- Verdict "triadic" only if P(multi-node core incl. M & C) ≥ 0.8 AND observed Φ exceeds the 95th percentile
  of the surrogate null. "Dyadic" if ≤ 0.2. Otherwise "undetermined" — reported as a result.
- H1 failing halts H2-H4 for that bin width.
- Estimated-vs-elicited comparison: agreement = same core as the documented Prow model.

## Instrument check on a known case
Simulate logs from the elicited Prow TPM (v11) with ε noise at the empirical marginal rates and series
length; run the identical estimation blind; require core recovery in ≥ 80% of 100 replicate logs before
touching real data. Also feed the v9 human-merge model as a second known case.

## Threats
Binning/aggregation artefacts; non-stationarity (releases, freezes); unobserved parties (CI, Slack, Prow
labels outside GH events — v11 caveat that reviews undercount approvals); bot accounts ambiguous;
sparse states and prior sensitivity; Φ is a max over states (multiple comparisons); order-1 Markov
misspecification; selection of repos. Ethics: public data, report repo/bot level only, no individual
profiling.

## Pilot already run (box, 30 Oct 2026)
Daily bins on the in-repo v11 CSVs (22 days): B=1 on every day, W on 95%; 3 of 8 states visited
(1, 6, 14 transitions). Posterior Φ median 0.48 (90% [0.25, 0.77]), but cores were single nodes in 34/40
draws and a time-shuffle null gives ~0.22 — i.e. prior-dominated and uninformative. Conclusion: finer bins
and a longer window are required (motivates H1).

# Workflow log

A dated record of each step taken in this fork (github.com/dheepakkaran/algorithmacy-lab): the command,
its outcome, and the key numbers. Times are America/New_York. Entries are appended, newest last.

## 2026-10-09 — first setup and validation

**12:26 EDT — clone.** `git clone https://github.com/dheepakkaran/algorithmacy-lab` into
`/workspace/algorithmacy-lab` succeeded over public HTTPS (7,415 files). HEAD is `ae3fb371`
("Merge pull request #805 from rogerSuperBuilderAlpha/contrib"). No `dissertation/` tree is present, so
the two-repo rule in `REPO_LAYOUT.md` has nothing to act on here.

**12:26 EDT — conventions read.** `START_HERE.md`, `CONTRIBUTING.md`, `REPO_LAYOUT.md`, and the house
style in `CLAUDE.md` set the working rules: validate the instrument before any verdict, report nulls as
results, keep forms to 3–5 nodes, and never `git add` `dissertation/`. `WORKFLOW_LOG.md` did not exist and
was created with this entry.

**12:27 EDT — environment.** The box default is Python 3.13.5. The venv uses Python 3.12.15, the version
`START_HERE.md` names, built with `uv venv --python 3.12 venv` (uv downloaded CPython 3.12.15).
`uv pip install -r requirements.txt` finished with exit code 0 and installed numpy 2.5.3,
pyphi 1.2.1.dev1470+gb78d0e342 (the `feature/iit-4.0` branch), and phyid from git. No workaround was
needed. `venv/` is gitignored.

**12:27 EDT — instrument validation.** `python -m org_frontier.classifier.validate` passed every check in
4.5 s and printed `All controls and built-in forms pass. Instrument validated.` The factoring control read
dyadic (Φ_MIP max 0.0000) and the full-coupling control read triadic (Φ_MIP max 0.8301). The five built-in
forms matched their expected verdicts: chat_dyad, gig_dyadic_model, and ats_feedback_factors dyadic at
Φ 0.0000; ats_triad_mediator and gig_false_dyad triadic at Φ 2.0000.

**12:27–12:32 EDT — probe 116, the conjunctive law.** `python -m org_frontier.probes.probe_conjunctive_law`
ran for 5 min 11 s, almost all of it on the n=7 case. The AND-all hub gave Φ = 3, 4, 5, 6 at n = 4, 5, 6, 7,
with the full node set as the core each time; the OR-all hub gave Φ = 3, 4, 5 at n = 4, 5, 6. Every row
reads `law holds True`, which reproduces the **confirmed** entry for #116 in
`org_frontier/probes/PROBES.md`. In plain terms, a commit that needs every member binds all of them into
one whole, and that whole gains one bit of integration per added member.

**12:29 EDT — Phase 3 verdict flip (run while probe 116 computed).** The `verdict()` snippet from `START_HERE.md`, run from the repo root,
gave two answers. With the mediator rule S' = W ∧ C the form is triadic (algorithmacy): max Φ = 2.0 at state
(1,1,1), MIP `{W,SC}`, one of four reachable states irreducible. With S' = W the form is dyadic (literacy):
max Φ = 0.0 across all four reachable states. Removing the mediator's dependence on C collapses the
three-party whole into separable parts. The snippet has to run from the repo root; run as a file from
`/tmp` it fails with `ModuleNotFoundError: No module named 'org_frontier'`.

**12:31 EDT — CI gate, core checks only.** The full `python ci/reproduce.py` manifest holds 514 checks,
42 of them marked slow, so it was not run. `python ci/reproduce.py --changed-file <empty file>` ran the six
core checks (instrument-controls, directory-current, map-current, research-index-current,
cards-index-current, hospitality-citations-agree) and all six passed in 1.9 s. A rerun at 12:32 EDT, after this log was created, still passed all six.

**Scope.** These results are in-silico: exact Φ on small Boolean models, evidence about the models and not
about any real organization. Nothing has been committed or pushed.

## 2026-10-09 — q219 scaffold: who decides an insurance claim? (pre-registration only)

**12:35 EDT — upstream located, read-only.** `GET https://api.github.com/repos/dheepakkaran/algorithmacy-lab`
names the parent `rogerSuperBuilderAlpha/algorithmacy-lab`. A local remote `upstream` was added and
`git fetch upstream main contrib '+refs/pull/*/head:refs/remotes/upstream-pr/*'` pulled branch and pull
request refs for reading. Upstream `main` is `ae3fb371`, the same commit as the fork; `contrib` is
`f7d712bf`. Nothing was written to GitHub; the unauthenticated API calls used under 15 of the 60-per-hour
limit.

**12:35 EDT — format rules read.** The finished question `org_frontier/questions/q63_outreach_coordination/`
holds `review.md`, `literature/deep_research_report.md`, `literature/references.bib`, `hypotheses.md`,
`methods.md`, `forms.py`, five `probe_*.py` scripts, `results/*.csv`, `FINDINGS.md`, and `paper.md`.
`org_frontier/protocol/template/`, `RESEARCH_PROTOCOL.md`, `GETTING_STARTED.md`, and `PUBLISHING.md` fix the
six stages, the rule that `hypotheses.md` is committed before results, registration in
`ci/reproduce.json`, rows in `org_frontier/probes/PROBES.md`, the `tools/build_index.py` refresh, and pull
requests into `contrib`. Upstream PR #811 ("q217: Robot shared control — who really steers? (Grok Bot
Boston Hackathon)") and PR #809 ("Add who_broke_prod and who_broke_prod_phi studies (incident-investigation
simulator)") both target `contrib`, and each opens with a hypotheses-only commit.

**12:36 EDT — question numbers.** `main`, `contrib`, and the fork stop at `q215_phi_family_robustness`;
no `q216` exists anywhere. The eleven open upstream PRs (one page) claim `q217` twice (#811
`q217_robot_shared_control`, #810 `q217_rotating_chair`) and `q218` once (#806 `q218_chicken_egg_feed`).
The highest number found is therefore q218, and this study takes **q219**. Probes on `main` and `contrib`
stop at #451; #810 claims #453–#456 and #806 claims #454, so q219's probes start at #457. PR #807 (V4 #11
graded channel, author `valani9`) adds `studies/graded_channel_exact_phi/` and PR #808 (probe 122 weighted
voting, author `Surbhu200`) edits probe scripts; neither uses a q number.

**12:36 EDT — prior work.** `rg` over the repo found the closest prior in
`org_frontier/studies/hitl_rubber_stamp/` (agenda #39, HUMAN_COMMIT_READ: a human joins the core iff it is
in the commit's determination and reads it). Probes #76 and #21, the delegation thread, q68 triage gating,
q63's liveness result, and the catalog's `insurance_broker` entry also bear on it. No form in the record
models claims adjudication, so the question is open.

**12:37 EDT — scaffold.** `python -m org_frontier.protocol.new_question --id 219 --start-probe 457 --slug
insurance_claim_adjudication --question "Who decides an insurance claim?"` created
`org_frontier/questions/q219_insurance_claim_adjudication/`. The explicit `--id` and `--start-probe` were
needed because the scaffolder's defaults (q216, probe #452) ignore open pull requests.

**12:38 EDT — pre-registration drafted.** `review.md`, `literature/deep_research_report.md` (13 sources,
DOIs checked on Crossref; marked partial against the 15–30 target), `literature/references.bib`,
`hypotheses.md` (H1–H5 with nulls), `methods.md` (exact rules, controls, and one decision rule per
hypothesis), and `forms.py` were written. `FINDINGS.md` and `paper.md` carry a pending status. The five
forms over (C, E, A) are `pipe` (C'=A, E'=C, A'=E), `gated` (C'=E∧¬A, E'=C, A'=E∧C), `loop` (C'=A, E'=C∧A,
A'=E∧C), `loop_nolearn` (E'=C), and `loop_frozen_claimant` (C'=C). `forms.py` passed `py_compile`.
No Φ was computed and no probe was run. `python tools/build_index.py --check` now reports the README
directory out of date; it was left unregenerated. Nothing was committed or pushed, pending approval of
the hypotheses.

## 2026-10-09 — q219 lock, probes #458–#461, write-up

**12:51 EDT — Q11 read before locking.** `org_frontier/questions/q11_oscillatory_scaling/` and
`org_frontier/studies/oscillatory_scaling/` define `rot_ring(n)` as the pure cyclic shift
x_i' = x_{i−1} (node i copies node i−1 mod n). At n=3 the rules are x0'=x2, x1'=x0, x2'=x1. With
C, E, A = x0, x1, x2 this is `pipe` exactly: C'=A, E'=C, A'=E, same direction, same three nodes, same
update. The committed results report it triadic: `q11_rotating_law.csv` gives `rot_ring,3,2.000000,
triadic,3,3` (Φ_MIP 2.0 from `verdict` over reachable states, core size 3), and the study's `sweep.csv`
gives `rot_ring,3,2.00000000,triadic,3,3,"{x0,x1,x2}"` from `major_complex`. The shift is a permutation
of the eight states, so every state is reachable. The committed files do not list the MIP or the
per-state Φ.

**12:52 EDT — H1 decision.** Q11 maps onto `pipe` exactly, so H1 now predicts `pipe` **triadic** with core
{C, E, A} and Φ_MIP = 2.0, and cites Q11 as its prior. The null is a dyadic or partial reading, and the risk
note frames the test as a replication under the claims labels. `review.md` adds Q11 to the prior-work
table, and `methods.md` reverses H1's decision rule to match. The original H1 ("pipe is dyadic") was
never committed. No Φ was computed for any q219 form before this change.

**12:52 EDT — branch and identity.** `git fetch upstream contrib` (read-only) left `upstream/contrib` at
`f7d712bf`. `git log --all` has no commit authored by any "dheepak" or "karan" name or address in
`main`, `contrib`, or the 812 fetched PR refs, so the repo-local identity is the fallback
`Dheepak Karan <dheepakkaran@users.noreply.github.com>`. Local branch `q219-insurance-claim-adjudication`
was created from `upstream/contrib`, with the untracked files carried over.

**12:52 EDT — hypotheses locked.** `git commit` of `hypotheses.md` alone, message
`q219: hypotheses (fixed before computation)`, produced `a8abd0fa197ab4dd079cc8beaca5dedbe9216c03`
(2026-10-09 12:52:08 −0400) on the local branch. Nothing was pushed.

**12:52 EDT — pre-registration completed.** `review.md`, `methods.md`, `forms.py`, `__init__.py`, and the
13-source literature scan were committed as `618da350` ("q219: review, literature scan, methods, and forms
(pre-registration, before computation)"). The unused scaffold file `probe_template.py` was deleted.

**12:52 EDT — probes #458–#461.** `python -m org_frontier.classifier.validate` printed `Instrument
validated`. The first run attempt failed before any probe started, because `results/` did not exist for
`tee` and `/usr/bin/time` and `bc` are not installed; the rerun wrote `results/run_*.txt` and the CSVs.
Every probe's control passed (chat_dyad dyadic Φ=0.000, ats_triad_mediator triadic Φ=2.000), and each
ran in about two seconds. The pre-registered rules gave these verdicts:
- `pipe`: triadic, max Φ_MIP 2.000, MIP three parts, core {C,E,A} 2.000, 8/8 states at 2.000. **H1 confirmed.**
- `gated`: triadic, max Φ_MIP 0.415 at 111 only (1/5), core {C,E} 2.000; E=0 states 000 and 100 read 0.
  **H2 refuted** (adjuster outside the core); the flagged-only clause held.
- `loop`: triadic, max Φ_MIP 1.000 (110: 0.415, 111: 1.000), core {E,A} 2.000. **H3 refuted.**
- `loop_nolearn`: triadic, max Φ_MIP 2.000 (110: 0.415, 111: 2.000; 2/6), core {C,A} 2.000. **H4 refuted.**
- `loop_frozen_claimant`: dyadic, max Φ_MIP 0.000 in 0/5 states, sub-complex {E,A} 2.000. **H5 confirmed.**
Committed as `8672323d`.

**12:53 EDT — literature.** Twenty DOIs were checked against `api.crossref.org/works/<doi>` (all HTTP
200) and `https://doi.org/<doi>` (all HTTP 302). `references.bib` was regenerated from the Crossref
metadata, so authors, titles, and issued years match Crossref exactly (Eling et al. 2021, Binns 2020).
Seven sources were added to the report; every cited key resolves to the bib.

**12:54 EDT — write-up and registration.** `FINDINGS.md`, `paper.md`, and the hackathon `README.md` (results
table, plain-words verdicts, reproduction commands, and a "Workflow & Grok Bot" section quoting both
prompts) were written. `PROBES.md` gained rows #458–#461, and `ci/reproduce.json` gained four checks with
expect strings copied from the run output. A first edit re-serialized the whole JSON file; it was reverted
and the checks were appended without reformatting. `tools/build_index.py`, `tools/build_map.py`, and
`build_research_index.py` regenerated their files, and all four index `--check`s passed.
`python ci/reproduce.py --changed-file <branch diff>` ran 10 checks (six core plus the four q219 checks)
and all passed. Commits `9225d70f` (literature, findings, paper, README) and `04292647` (PROBES rows, CI
checks, README directory, MAP) followed. Nothing was pushed. This log stays uncommitted.

## 2026-10-09 — PR preparation: identity rewrite and log move

**13:02 EDT — identity rewrite.** Dheepak approved the PR but not the push. Repo-local `user.name` /
`user.email` were set to `Dheepak Karan <67942227+dheepakkaran@users.noreply.github.com>`, and
`git filter-branch --env-filter` over `upstream/contrib..HEAD` rewrote author and committer on all five
branch commits to that identity. Order, trees, messages, and author dates were kept, so the
hypotheses-only commit is still first. The new hashes, in branch order:
- `a8abd0fa197ab4dd079cc8beaca5dedbe9216c03` (q219: hypotheses (fixed before computation))
- `618da350e6f89cc4b4b994eb78e7bd152bf82401` (review, literature scan, methods, forms)
- `8672323deb2fecbae310957afcddd2a6fa599ae3` (probes 458–461 and results)
- `9225d70f8536de52f66c2aac052e9b9032e4dd9b` (literature, findings, paper, README)
- `04292647d53e7bfab15fe9d1651c4544dc0ad034` (PROBES rows, CI checks, indexes)

The old hashes were replaced in this log (entries above now cite the new hashes), in `README.md`, and in
`paper.md`, through a final commit `q219: update commit references`, which cannot cite its own hash.
The earlier entry naming the fallback address `dheepakkaran@users.noreply.github.com` records what was
used at the time; no commit on the branch carries it now.

**13:02 EDT — log moved into the study.** This file moved from the repo root to
`org_frontier/questions/q219_insurance_claim_adjudication/WORKFLOW_LOG.md`, is linked from the
"Workflow & Grok Bot" section of the q219 `README.md`, and is now committed with the PR. Earlier
entries that call the log uncommitted describe the state at the time.

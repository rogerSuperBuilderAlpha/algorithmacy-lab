# q219 — Who decides an insurance claim?

A claimant (C) files a claim, an auto-adjudication engine (E) screens it, and a human adjuster (A) may
review it. This study asks which routing design makes the claim decision one irreducible three-party
determination (**triadic**, Φ_MIP > 0 with all three in the major complex) and which lets it factor into
a pair plus a bystander. Each design is a three-node Boolean network read with exact IIT-4.0 Φ, the
lab's standard instrument. Results are in-silico: evidence about these small models, not about any
insurer.

Files: `review.md` (prior work), `literature/` (20 verified sources), `hypotheses.md` (fixed before
computation), `methods.md`, `forms.py`, `probe_458_pipe.py` … `probe_461_liveness.py`, `results/`,
`FINDINGS.md`, `paper.md`, `WORKFLOW_LOG.md` (step-by-step record).

## Hypotheses (committed before any q219 form was computed, commit `a8abd0fa`)

- **H1** — The pass-through pipe (engine only forwards) is triadic through closure alone, as Q11's
  identical three-node rotating ring is.
- **H2** — Threshold auto-approval (small claims auto-approve, adjuster sees flagged ones) is triadic with
  all three in the core, and only flagged states are irreducible.
- **H3** — The fraud-flag loop (adjuster reads the engine's flag, engine learns from adjuster overrides)
  is triadic with all three in the core.
- **H4** — The loop stays triadic with all three in the core when the override learning is removed.
- **H5** — Freezing the claimant (the claimant no longer reads the decision) makes the loop dyadic.

## Results

| form | rules (C', E', A') | verdict (whole) | max Φ_MIP | major complex (Φ) | irreducible states | hypothesis |
|---|---|---|---:|---|---|---|
| `pipe` | A, C, E | triadic | 2.000 | {C,E,A} (2.000) | 8/8 | H1 **held** |
| `gated` | E∧¬A, C, E∧C | triadic | 0.415 | {C,E} (2.000) | 1/5 (111) | H2 **failed** |
| `loop` | A, C∧A, E∧C | triadic | 1.000 | {E,A} (2.000) | 2/5 (110, 111) | H3 **failed** |
| `loop_nolearn` | A, C, E∧C | triadic | 2.000 | {C,A} (2.000) | 2/6 (110, 111) | H4 **failed** |
| `loop_frozen_claimant` | C, C∧A, E∧C | dyadic | 0.000 | {E,A} (2.000) | 0/5 | H5 **held** |

Instrument control passed in every probe: `chat_dyad` dyadic Φ=0.000, `ats_triad_mediator` triadic
Φ=2.000.

## What held and what failed, in plain words

- **H1 held.** When the engine just passes the claim along and the claimant sees the outcome, all three
  are tied together equally, in every state. The loop itself binds them, with no one combining two inputs.
- **H2 failed.** Auto-approval keeps the arrangement as a whole irreducible, but only in the one state
  where a big claim is flagged and approved, and the tightest core is claimant plus engine. The adjuster
  is left outside: structurally a rubber stamp. The "only flagged claims matter" part did hold.
- **H3 failed.** When the engine learns from the adjuster's overrides, engine and adjuster lock into a
  private pair and the claimant is pushed out of the core.
- **H4 failed.** Removing the learning does not bring back a three-way core. It swaps who is left out:
  claimant and adjuster become the core and the engine drops out.
- **H5 held.** If the claimant cannot see the decision, the arrangement falls apart into separable parts.

Short answer to the question: it depends on where the gate sits. The plain pipe binds all three. Each gate
hands the decision to a pair: claimant and engine under auto-approval, engine and adjuster under a learning
fraud loop, claimant and adjuster when the engine stops learning.

## How to reproduce

From the repo root, Python 3.10+ (this run: Python 3.12.15, PyPhi IIT-4.0 line):

```bash
python3.12 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m org_frontier.classifier.validate          # must print "Instrument validated"
python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_458_pipe
python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_459_gated
python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_460_loop
python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_461_liveness
python ci/reproduce.py q219-h1-pipe q219-h2-gated q219-h3-h4-loop q219-h5-liveness
```

Each probe runs in about two seconds and rewrites its CSV under `results/`.

## Workflow & Grok Bot

The full step-by-step record, with commands, outcomes, key numbers, and EDT times, is in
[`WORKFLOW_LOG.md`](WORKFLOW_LOG.md).

### Steps

1. Set up the fork on a box: Python 3.12 venv, `requirements.txt`, `classifier.validate`, probe #116, and
   the `START_HERE.md` `verdict()` exercise.
2. Read the question format from `q63_outreach_coordination/`, the protocol template, `RESEARCH_PROTOCOL.md`,
   `GETTING_STARTED.md`, `PUBLISHING.md`, and upstream PRs #811 and #809.
3. Found the next free question number by scanning `main`, `contrib`, and all open upstream PRs
   (q217 ×2 and q218 taken; q216 unused but skipped) and chose q219, probes from #457.
4. Checked prior work: HITL rubber stamp study #39, the delegation thread, probes #76 and #21, q63, q68,
   the catalog's insurance broker. No claims-adjudication form existed.
5. Scaffolded with `new_question --id 219 --start-probe 457`, wrote review, literature scan, hypotheses,
   methods, and forms. Stopped for approval.
6. Before locking, read Q11: its `rot_ring(3)` is exactly the pipe, reported triadic at Φ = 2.0. H1 was
   changed from "dyadic" to "triadic" and Q11 cited. Then `hypotheses.md` was committed alone.
7. Committed the rest of the pre-registration, wrote and ran probes #458–#461, committed results.
8. Extended the literature to 20 sources with every DOI checked, wrote FINDINGS, paper, this README,
   PROBES.md rows, `ci/reproduce.json` checks, and regenerated the indexes.

### Who did what

- **Dheepak Karan** chose the question, the three parties, and the three variants; asked for the
  prior-work checks against HITL #39, the delegation thread, and Q11; approved the hypotheses; and set the
  requirements (verified literature, this README, nothing pushed without review).
- **Grok Bot** (the AI assistant, working on its own Linux box) read the lab's conventions, found the
  question number, scaffolded the folder, wrote the Boolean forms and hypotheses, ran the probes,
  verified the literature against Crossref and doi.org, and wrote the results up. It made only local
  commits; nothing was pushed or posted.

### Prompts used

Prompt 1:

> None of these. A and B are already open PRs (#808, #807). I want my own question. 1. First read one
> finished question folder on main (e.g. org_frontier/questions/q63_outreach_coordination/) and upstream
> PRs #811 and #809 (same hackathon). Give me the format rules as a short checklist: files, folder layout,
> PR title format, and which base branch they target. 2. Check main and all open upstream PRs for the
> highest qNNN used (q217 and q218 are taken). Pick the next free number. 3. Set up my question the way
> the lab requires (do NOT compute yet): "Who decides an insurance claim?" Parties: claimant,
> auto-adjudication engine, human adjuster. Variants as small Boolean networks: a) engine only routes the
> claim to the adjuster (pipe) b) engine auto-approves small claims; adjuster only sees flagged ones
> c) adjuster reads the engine's fraud flag, and the engine learns from adjuster overrides. Check the lab
> hasn't already answered this (HITL rubber stamp study #39, delegation thread). Then write 5 hypotheses:
> which variants are dyadic vs triadic, and why. Then STOP and wait for my approval.

Prompt 2:

> Approve, with these steps: 1. Before locking: check Q11 / org_frontier/studies/oscillatory_scaling. A
> closed copy ring is a traveling wave, and the lab reported Phi=2.0 there. Tell me if that applies to
> `pipe`. If it does, either update H1 or keep it and cite Q11 as the conflicting prior in review.md. Then
> commit hypotheses.md alone. 2. Run probes #457-460. 3. After results: - Bring the literature to at least
> 15 sources. Every DOI must be real and resolve; no invented references. - Add README.md in the q219
> folder (hackathon requirement): question, hypotheses, results table, which held/failed, how to
> reproduce, and a 'Workflow & Grok Bot' section (steps, what you did vs what I did, prompts used, where
> you got stuck). - Run tools/build_index.py. Show me the results summary before pushing anything.

### Where it got stuck

- **Colliding numbers.** The scaffolder looks only at local folders and `PROBES.md`, so by default it
  picked q216 and probe #452. Open PRs already claim q217 (twice), q218, and probes #453–#456, so the
  folder was made with explicit `--id 219 --start-probe 457`.
- **The `verdict()` snippet outside the repo root.** Saved to a file in `/tmp` and run there, the
  `START_HERE.md` snippet failed with `ModuleNotFoundError: No module named 'org_frontier'`. It works when
  run from the repo root.
- **H1 versus Q11.** The first draft of H1 predicted the pipe dyadic, reasoning from the lab's finding
  that a mediator must read all parties. Dheepak pointed to Q11, whose three-node rotating ring is the
  pipe rule for rule and reads triadic at Φ = 2.0. H1 was reversed before the hypotheses were committed,
  and the probe replicated Q11.
- **Hypotheses that were too confident.** Three of five failed. The predictions expected full three-party
  cores from the conjunctive law and the commit-and-read rule; in the gated forms a two-party subset
  carried more Φ than the whole and took the major complex.
- **Literature shortfall.** The first scan had 13 sources against the protocol's 15–30. Seven more were
  added after the run, each checked on Crossref and doi.org. One DOI (Binns) failed a first Crossref fetch
  and was left out of the first scan, then verified on retry. Crossref's issued years (2021 for Eling et
  al., 2020 for Binns) differ from the print-volume years, and the references follow Crossref.
- **Box tooling.** The first probe run failed because the `results/` folder did not exist yet and
  `/usr/bin/time` and `bc` are not installed on the box; the probes were rerun without them. A repo-wide
  `rg` search timed out until it was limited to Markdown and Python files.
- **Formatting slip.** The first edit to `ci/reproduce.json` re-serialized the whole file (a 1,600-line
  diff). It was reverted and the four checks appended without reformatting.
- **Commit identity.** No commit by Dheepak existed in the repo history, so the first local commits used
  a guessed address, `Dheepak Karan <dheepakkaran@users.noreply.github.com>`. Before the PR, author and
  committer on every branch commit were rewritten to Dheepak's GitHub noreply address
  `Dheepak Karan <67942227+dheepakkaran@users.noreply.github.com>`, which changed every commit hash; the
  hashes cited in this folder were updated to match.

# Graded party channel vs Φ (V4 #11)

Does the exact-Φ joint-observation cliff survive a **graded party channel** —
the mediating system reads each party through a lossy channel, correct with
probability q and otherwise reading the default 0 — while party duty stays
perfectly correlated? The arc to date ran on hard binary observation masks:
V4 #1 found the screen collapse under anti-correlated duty, V4 #2 found
phase-locked duty restore it at matched mean duty, V4 #7 found the cliff
recreate on logged structure. This cell asks whether channel *quality*, at
fixed duty correlation, carries the cliff or not.

Siblings: `../joint_obs_cliff_exact_phi/` (V4 #1),
`../phase_lock_exact_phi/` (V4 #2), `../logged_alt_duty_exact_phi/` (V4 #7).

## Status

**RUN.** Results in `results/` and [`FINDINGS.md`](FINDINGS.md). Verdict
`GRADED_HOLDS`: the q=0.5 graded channel holds the screen where hard
alternation cliffs. Hypotheses fixed in `hypotheses.md` before computing.

## Question (one line)

On the V4 #1 multifamily panel and the V4 #7 logged panel, does the exact-Φ
whole-form screen hold under a symmetric party→mediator channel degrading
smoothly q = 1.0 → 0.25, or does degradation cliff like anti-correlated duty?

## Run

```
python org_frontier/studies/graded_channel_exact_phi/analyze_graded.py
```

## Workflow

The contribution followed the lab's contributor path end to end:

1. **Orient.** Read `AGENTS.md`, `NOW.md`, `OVERVIEW.md`, `CONTRIBUTING.md`,
   and the V4 agenda. Strand E #11 was the open cell: the exact-Φ
   observation arc had closed on hard binary masks (#1 cliff, #2 phase-lock
   restoration, #7 logged recreation), and the graded-channel question was
   listed open.
2. **Set up.** Python 3.12 virtual environment; `pip install -r
   requirements.txt` for the PyPhi IIT-4.0 line plus phyid. Run from the
   repo root so `org_frontier.*` and `foundations.*` resolve.
3. **Reuse, not rebuild.** The channel sweep imports the V4 #1 panel
   builders, AUC/orientation helpers and thresholds unchanged, the V4 #7
   logged-panel builder and role map, and `max_phi_float` from
   `probes/lib.py` (the foundations arc's stochastic-TPM exact-Φ engine).
   Only the mixed-TPM construction is new.
4. **Pre-commit the hypotheses.** `hypotheses.md` and `analyze_graded.py`
   were committed before any run, so the git history shows the questions,
   thresholds, decision rules and nulls fixed ahead of the numbers.
5. **Run.** One command, about 20 seconds, deterministic (seeded). Controls
   replicate the arc anchors: alternation 0.660 multifamily / 0.591 logged,
   matching V4 #1 and #7.
6. **Verify.** `python tools/build_index.py --check`,
   `python tools/build_map.py --check`,
   `python org_frontier/research/build_research_index.py --check`, and the
   new `ci/reproduce.json` entry (`graded-channel-exact-phi`) all pass.
7. **Land.** Pull request into `contrib`.


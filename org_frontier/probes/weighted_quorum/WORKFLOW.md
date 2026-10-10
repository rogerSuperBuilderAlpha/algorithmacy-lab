# Workflow disclosure — probe 457

This probe was produced with an AI agent working under the author's direction. This file records which
tools were used, who decided what, the order of the steps, and what a reviewer should check.

## Tools

- **AI agent:** Grok Bot. The underlying model and its version are not known to the author.
- **Compute:** a Linux machine operated by the agent. Every command below ran there.
- **Python:** 3.12.15 (installed with `uv python install 3.12`), in a repo-root `venv/` created with
  `uv venv --python 3.12 venv` and populated with `uv pip install -r requirements.txt`.
- **Packages:** pyphi 1.2.1.dev1470+gb78d0e342 (the `feature/iit-4.0` line pinned in `requirements.txt`),
  phyid 0+untagged.8.g6c5f2e9, numpy 2.5.3, scipy 1.18.1, scikit-learn 1.9.1, matplotlib 3.11.2.

## Division of labour

The author, Jiaxin Lin:

- chose this contribution from three proposals the agent drafted, after asking for a recommendation;
- approved `hypotheses.md` as drafted, with commit noise on the mediator only;
- chose the folder layout `org_frontier/probes/weighted_quorum/`;
- supplied the commit name and email;
- reviews the full diff and the pull-request text before any pull request is opened.

The agent:

- read the repository's rule files and surveyed the upstream pull requests for overlap and number
  collisions;
- drafted `hypotheses.md`;
- wrote `probe_weighted_quorum.py`, ran it, and committed its output;
- drafted `README.md`, this file, the PROBES.md row, and the `ci/reproduce.json` entries.

## Step log

Times are US Eastern (UTC−4) on 2026-10-09.

| Time | Step | Commit |
|---|---|---|
| 12:30 | Repository rule files, agendas, probe log, and existing studies read; three contribution ideas proposed | — |
| 12:38 | Upstream pull requests surveyed through the public GitHub API. The survey found open PR #807 already answering the graded-channel idea and open PR #808 partly covering weighted quorums. Probe numbers 453–456 were already claimed in open PRs | — |
| 12:41 | Branch `probe/weighted-quorum` created from `upstream/contrib` at `f7d712bf`; Python 3.12 venv built | — |
| 12:41 | `python -m org_frontier.classifier.validate` printed `Instrument validated`; probe 117 rerun as a reference | — |
| 12:42 | `hypotheses.md` drafted and shown to the author; index `--check`s run with the new folder present | — |
| 12:45 | Author approved the hypotheses; `hypotheses.md` committed alone | `a3716ad8` |
| 12:46 | Probe script written; one trial run of `--ci` (deterministic arm) to check that it executes | — |
| 12:47 | Script committed after a display-only change (no-complex sentinel printed as `-`) | `621a9ec6` |
| 12:47–12:51 | Full run (4 min 14 s); `results/run.txt`, `classes.csv`, `noise.csv` committed | `7e1eae4f` |
| 12:51 | PROBES.md row 457 and two `ci/reproduce.json` checks committed | `6ac5b3d2` |
| 12:52 | Per-PR check selection (`--changed-file`) and the three index `--check`s passed | — |
| 12:53 | `README.md` and this file committed | `65050d18` |
| 12:52–13:13 | `python ci/reproduce.py` (full manifest, 516 checks) ran for about 21 minutes, reached at least check 37 of 516, and was stopped as too slow for this session. Timing fields it rewrote in other studies' result files were restored with `git checkout` | — |
| 13:13 | `python ci/reproduce.py probe-weighted-quorum-ci probe-weighted-quorum-full` passed (41.0 s, 262.1 s); the rerun left the committed CSVs unchanged | — |
| 13:13 | Verification section updated in the final commit, whose hash cannot be quoted inside itself | — |

## Pre-commitment evidence

`hypotheses.md` was committed in `a3716ad8` at 12:45:37 and has not changed since. The probe script first
entered history in `621a9ec6` at 12:47:06, and the first results in `7e1eae4f` at 12:51:29.

One trial run of the deterministic arm happened at about 12:46, after the hypotheses commit and before the
code commit. Between that trial and `621a9ec6`, the only change was how the script prints a form with no
irreducible complex. The run produced the H3 refutation that the committed results show. The hypotheses
file was not edited after that run or any other.

The post hoc reading of the H3 counterexamples in `README.md` is labelled as such.

## Verification

All checks below were run by the agent on its own machine.

- `python -m org_frontier.classifier.validate`: `Instrument validated`.
- `python ci/reproduce.py --changed-file` over the branch's changed paths: 7 checks, all pass, including
  `probe-weighted-quorum-ci`.
- `python ci/reproduce.py probe-weighted-quorum-ci probe-weighted-quorum-full`: both pass (41.0 s and
  262.1 s).
- The full manifest (`python ci/reproduce.py`, 516 checks) was not completed locally. It was stopped after
  about 21 minutes, having reached at least check 37 of 516; the remaining checks were left to CI and the nightly job.
- `python tools/build_index.py --check`, `python tools/build_map.py --check`,
  `python org_frontier/research/build_research_index.py --check`: all up to date. The root `README.md`
  and `MAP.md` were not changed.
- The probe cites no external literature. Every source it names is a file, probe, or pull request in this
  repository.

## Points for human review

- The decision rules and their outcomes, against `hypotheses.md`.
- The H6 refutation, which rests entirely on the two H3 counterexamples keeping their deterministic core
  under noise; no mixed class gained a second party. H6's claim line ("no mixed class has two or more
  parties in its core at any ε") and its H0 line ("gains a core with two or more parties") differ, and
  the script scored the claim line.
- The enumeration and class canonicalisation in `enumerate_classes` and `permute_table`.
- `tpm_major_complex`, the TPM-input copy of `lib.major_complex` used by the noise arm. Control C2 checks
  it against the deterministic path.
- The folder layout. Probes normally live as `org_frontier/probes/probe_<slug>.py`; this one is a
  subfolder, so the `MAP.md` probe count (which globs `org_frontier/probes/probe_*.py`) does not include
  it.

## Limitations

- In-silico only: exact IIT 4.0 Φ on Boolean models of four and five nodes.
- Weights 0..5, saturated at 0..6, at three and four parties. Five or more parties are not covered.
- Noise acts on the mediator's commit only, never on the party inputs.
- Every verdict is an IIT 4.0 verdict. Q215 shows the interior-quorum zero does not hold under IIT 3.0.

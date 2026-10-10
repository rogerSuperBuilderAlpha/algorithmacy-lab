# Probe 457 — weighted and noisy quorums

Across every weighted threshold rule at three and four parties, an AND or OR over the relevant parties
binds exactly those parties, and irrelevant parties never join the core. The extremes-only law fails on
one weight pattern: weights (1, 1, 2, 2) at quotas 2 and 5 keep a two-party core {S, P3, P4} at
φ = 2.000000 while the whole system reads dyadic. Commit noise below ε = 0.5 never raises a core's φ and
changes no core's membership; the `*` marks in the noise table of `results/run.txt` appear only at
ε = 0.5, where every remaining core vanishes.

**Author:** Jiaxin Lin (GitHub: jiaxinaspenlin-dotcom). AI-assisted; see [`WORKFLOW.md`](WORKFLOW.md).

## Files

- [`hypotheses.md`](hypotheses.md) — question, H1–H6 with nulls and decision rules, control gate, scope.
  Committed alone in `a3716ad8` before any code existed.
- [`probe_weighted_quorum.py`](probe_weighted_quorum.py) — enumeration, control gate, readings, scoring.
- [`__init__.py`](__init__.py) — makes the folder importable for `python -m`.
- [`results/run.txt`](results/run.txt) — stdout of the full run.
- [`results/classes.csv`](results/classes.csv) — one row per class: weights, quota, type, relevant set,
  swing counts, truth table, whole-system reading, core.
- [`results/noise.csv`](results/noise.csv) — one row per class and noise level ε.
- [`WORKFLOW.md`](WORKFLOW.md) — AI-assisted workflow disclosure and step log.

## Form

Node 0 is the mediator S; nodes 1..n are parties P1..Pn with n ∈ {3, 4}. Each party copies S, and S
commits f(x) = 1 iff Σ w_i·x_i ≥ θ. This is the `threshold_hub` wiring of probe 117. Weights 0..5 and
every quota give 8 distinct non-constant classes at three parties and 25 at four, up to relabelling of the
parties; weights 0..6 add none. The noise arm flips the commit with probability ε ∈ {0, 0.05, 0.10, 0.20,
0.30, 0.40, 0.45, 0.50}.

## Result

| Hypothesis | Verdict | Count |
|---|---|---|
| H1 extreme classes bind {S}+R | SUPPORTED | violations 0/10 |
| H1b core φ = \|R\| on extreme classes | SUPPORTED | violations 0/10 |
| H2 irrelevant parties stay out of the core | SUPPORTED | violations 0/33 |
| H2b irrelevant party gives a dyadic whole system | SUPPORTED | violations 0/11 |
| H3 mixed classes bind at most one party | REFUTED | violations 2/21 |
| H4 a single core party has the unique largest swing count | SUPPORTED | scorable 10, tied 0, violations 0 |
| H5 noise keeps extreme membership, φ non-increasing | SUPPORTED | violations 0 |
| H6 noise does not rescue a mixed quorum | REFUTED | violations 12 |

The two H3 counterexamples are classes n4-18 (θ = 2) and n4-21 (θ = 5), both with weights (1, 1, 2, 2)
and swing counts (1, 1, 3, 3). The H6 refutation comes from the same two classes: each keeps its core
{S, P3, P4} at every ε below 0.5 (φ = 1.523037 at ε = 0.05, 0.046396 at ε = 0.45). No mixed class whose
deterministic core held one party or none gained a second party under noise. Noise drops φ fast at the
extremes: the four-party AND and OR classes fall from 4.0000 at ε = 0 to 1.7661 at ε = 0.05.

The rules stated in open PR #808 all fall inside the three-party enumeration. The probe's reading of each
agrees with the structure, Φ, and parties in the core that the PR states.

### Reading (post hoc)

This paragraph was written after the run and is not pre-registered. In Boolean terms n4-18 is
P3 ∨ P4 ∨ (P1 ∧ P2) and n4-21 is P3 ∧ P4 ∧ (P1 ∨ P2). Each is an OR or AND of the two heavy parties with
the light pair acting as a single nested vote. The core keeps the heavy pair, so the extremes-only law
reappears one level down: the two parties joined by a clean OR or AND bind, and the nested pair drops.
Whether this nesting reading extends to five or more parties is untested.

## Reproduce

Run from the repo root with the Python 3.10+ venv active.

```bash
python -m org_frontier.classifier.validate                                  # prints "Instrument validated"
python -m org_frontier.probes.weighted_quorum.probe_weighted_quorum --ci     # deterministic arm, about 45 s
python -m org_frontier.probes.weighted_quorum.probe_weighted_quorum          # full run with noise arm, about 4 min
python ci/reproduce.py probe-weighted-quorum-ci probe-weighted-quorum-full
```

Expected output, verbatim, from `--ci` (the full run prints the same lines):

```
  C1a irreducible control (full coupling): triadic Φ=0.830075  PASS
  C1b AND (3-of-3): triadic Φ=3.000000 core={S,P1,P2,P3}  PASS
  C1b OR (1-of-3): triadic Φ=3.000000 core={S,P1,P2,P3}  PASS
  C1b 2-of-3: dyadic Φ=0.000000 core=none  PASS
  n=3: 8 classes with weights 0..5; 8 with weights 0..6; saturated
  n=4: 25 classes with weights 0..5; 25 with weights 0..6; saturated
  scored n: [3, 4]; classes scored: 33; extreme |R|>=2: 10; mixed: 21; with an irrelevant party: 11
  H1 (extreme classes bind {S}+R):              SUPPORTED  violations 0/10
  H1b (core φ = |R| on extreme classes):         SUPPORTED  violations 0/10
  H2 (irrelevant parties stay out of the core):  SUPPORTED  violations 0/33
  H2b (irrelevant party -> whole-system dyadic): SUPPORTED  violations 0/11
  H3 (mixed classes bind at most one party):     REFUTED  violations 2/21
  H4 (single core party has the unique max β):   SUPPORTED  scorable 10, tied 0, violations 0
    H3 violation: n4-18 w=(1, 1, 2, 2) θ=2 type=mixed R={P1,P2,P3,P4} β=(1, 1, 3, 3) core={S,P3,P4} φ=2.000000 whole=dyadic Φ=0.000000
    H3 violation: n4-21 w=(1, 1, 2, 2) θ=5 type=mixed R={P1,P2,P3,P4} β=(1, 1, 3, 3) core={S,P3,P4} φ=2.000000 whole=dyadic Φ=0.000000
```

Additional expected output from the full run:

```
  C2 (ε=0 reproduces the deterministic readings): PASS
  C3 (ε=0.5 reads dyadic, no core with >=2 parties): PASS
  n4-12  AND      4.0000    1.7661    0.9694    0.3689    0.1490    0.0491    0.0203    -*
  n4-18  mixed    2.0000    1.5230    1.1350    0.5996    0.2881    0.1067    0.0464    -*
  H5 (noise keeps extreme membership, φ non-increasing): SUPPORTED  violations 0
  H6 (noise does not rescue a mixed quorum):             REFUTED  violations 12
    H6 violation: n4-18 ε=0.05 core={S,P3,P4} φ=1.523037
    H6 violation: n4-21 ε=0.45 core={S,P3,P4} φ=0.046396
```

The full per-class tables are in [`results/run.txt`](results/run.txt). In the tables, `-` marks a form with
no irreducible complex; `lib.major_complex` returns φ = −1 as a sentinel there, and the CSVs store `-`.
`--ci` skips the noise arm (C2, C3, H5, H6) and the CSV writes, and changes no line it prints.

## Scope

Every number here is exact IIT 4.0 Φ, computed with PyPhi's IIT 4.0 line, on deterministic and
commit-noisy Boolean models of four and five nodes. The results are evidence about these models. They are
not measurements of any committee, voting body, platform, or organization, and the validation gap to real
coordination is unchanged. The interior-quorum zero depends on the IIT 4.0 measure: Q215 reads the 2-of-3
quorum at Φ = 1.269 under IIT 3.0, so a reading under another member of the Φ family could differ. Noise on
the parties' inputs, and quorums of five or more parties, are outside this probe.

## Status

Complete on branch `probe/weighted-quorum`; not yet opened as a pull request.

## Links

- Probe log: row 457 in [`../PROBES.md`](../PROBES.md).
- CI checks in [`ci/reproduce.json`](../../../ci/reproduce.json): `probe-weighted-quorum-ci` (per-PR) and
  `probe-weighted-quorum-full` (`"slow": true`, nightly).
- Pre-registration commit: `a3716ad8` (hypotheses), followed by `621a9ec6` (code) and `7e1eae4f` (results).
- Prior record: probe 117 (`../probe_threshold_scaling.py`), probe 110 (`../probe_ejection_order.py`), the
  coordination-logic atlas (`../../studies/coordination_logic_atlas/FINDINGS.md`), Q215
  (`../../questions/q215_phi_family_robustness/`), and open PR #808.

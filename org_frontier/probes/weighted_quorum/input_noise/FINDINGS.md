# Input errors break the interior-quorum zero

At 10% independent input observation errors, the 2-of-3 majority hub has positive whole-system
Φ in every reachable state. The same hub has Φ=0 without noise. This is a counterexample to
extending the atlas's interior-quorum zero to input-noisy rules under the pinned IIT 4.0 measure.
The selected major complex remains a dyad, so the counterexample does not establish full-group
major-complex membership.

## Results

The [pre-specified panel](hypotheses.md) contains five forms at three noise rates. The primary
panel is OR, majority, AND over three parties; two weighted four-party rules form the secondary
panel. All parties copy the actual mediator state. Only the mediator's observation of each
party has an independent probability η of being wrong.

| Rule | Whole Φ, η=0 | Whole Φ, η=0.1 | Maximum core φ, η=0.1 | Selected core at maximum φ |
|---|---:|---:|---:|---|
| OR | 3.000000 | 1.854569 | 1.854569 | S,P1,P2,P3 |
| 2-of-3 majority | 0.000000 | 0.026981 | 0.107922 | S,P3 |
| AND | 3.000000 | 1.854569 | 1.854569 | S,P1,P2,P3 |
| Weights (1,1,2,2), quota 2 | 0.000000 | 0.015905 | 1.360017 | S,P3,P4 |
| Weights (1,1,2,2), quota 5 | 0.000000 | 0.015905 | 1.360017 | S,P3,P4 |

At η=0.5 all five whole-system readings are zero and no irreducible core remains. All controls
pass, including the instrument's built-in forms, the deterministic quorum anchors, entrywise
TPM agreement at η=0, and independence from true inputs at η=0.5.

H1 is supported: noisy OR and AND retain the full selected major complex. H2 is refuted:
majority has whole-system Φ=0.026980608910464783 in all four reachable states. H3 is refuted
because both weighted whole systems become positive; their selected cores retain the same heavy
pair, so H3's membership clause holds while its zero-Φ clause fails.

The script uses the maximum over reachable states. Majority's positive reading holds in every
such state; it is not a maximum-only effect. The reachable set has the same four states at all
three noise rates: the copying parties agree, with S either 0 or 1. Noise changes transition
probabilities within that set, rather than adding new reachable states.

## What changes in the law

The atlas joins two propositions: an interior quorum has zero whole-system Φ, and an interior
quorum cannot keep the full group as its major complex. The first proposition fails under input
noise in this panel. The second survives the primary panel: OR and AND keep the full complex,
and majority does not. Positive whole-system Φ and full-group major-complex membership must be
reported separately.

Probe 457's commit-noise results do not show this majority effect. Commit flips preserve a
two-level mediator probability: the deterministic gate's 0 and 1 outputs become ε and 1−ε.
Input errors instead yield four majority probabilities at η=0.1, indexed by true active count:
0.028, 0.172, 0.828, 0.972. These probabilities retain distinctions between input counts that a
deterministic majority gate discards. This difference describes the noisy gate; it is not a
proof that it causes the positive Φ result.

An independent regression test constructs the majority TPM from those hand-calculated
probabilities and an explicit hub connection matrix, without the experiment's TPM constructor,
truth-table helper, or numerical connection inference. It reproduces the positive whole-system
reading. Separate tests check the OR/majority/AND probabilities and the biased independent-input
endpoint. Thus the counterexample survives a second construction of its transition matrix.

The S,P3 selection does not establish a privileged third voter: all voters have symmetric wiring
and weights, and the maximal-complex API returns one choice. The artifact records returned cores
at every state but does not enumerate tied complexes within a state.

## Reproduction and record

From the repository root with the pinned environment active:

```sh
python -m org_frontier.classifier.validate
python -m unittest org_frontier.probes.weighted_quorum.input_noise.test_input_noise
python ci/reproduce.py probe-quorum-input-noise probe-quorum-input-noise-probabilities
```

The CI command prints results without writing artifacts. To regenerate the committed state
profiles, run:

```sh
python -m org_frontier.probes.weighted_quorum.input_noise.probe_input_noise --write
```

[results.json](results.json) contains the rates, rules, per-state whole-system Φ and returned
major complexes, and hypothesis scores. Hypotheses and methods were committed and pushed in
`90408a28` before the implementation in `51dfbaeb` and the first comparison run. The first run
needed a metadata-only correction from `pyphi.__version__` to `importlib.metadata.version`;
the installed PyPhi exposes no `__version__` attribute. Decision rules did not change.

The run used Python 3.12.9, PyPhi 1.2.1.dev1470+gb78d0e342 at commit
b78d0e342d37175cbd55cf35a6d52ae035b4c50f, numpy 2.5.4 and scipy 1.18.1, in the task worktree's
local virtual environment. An OpenAI Codex agent wrote the extension, ran the checks, and drafted
this report at the user's request. No human review or independent instrument implementation is
claimed.

Verification: all three regression tests passed; the `probe-quorum-input-noise` reproduction
check passed (22.1 seconds). All four generated-index checks passed. No full-manifest run was
attempted; the extension changes no shared instrument code.

## Limits and next question

These are results on small Boolean models, not observations of real committees or organizations.
The exact IIT 4.0 computation is subject to floating-point precision and the repository's 1e-9
cutoff. The independent TPM regression uses the same PyPhi instrument. OR/AND and the weighted
quota pair are complement-related, not independent replications.

Only η=0, 0.1 and 0.5 were tested. The results establish a counterexample at 0.1, not a noise
threshold or monotonic trend. Different error correlations, feedback rules, update schedules,
party counts and IIT versions remain outside the panel. Whether the full-major-complex
extremes-only claim holds across weighted input-noisy rules remains open.

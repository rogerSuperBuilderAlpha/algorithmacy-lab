# WHO BROKE PROD? × Φ — findings

**Verdict: COMMIT_CORE_MATCHES_ONLY_WITHOUT_ACCESS.** Only the deciding-mediator form carries an
integrated coordination core ({A1, M, A2}, Φ = 2.0). Its matched simulator condition beats the best
topology without such a core when the investigator has no trace access (0.695 vs 0.130), and does not
differ from it when the investigator has trace access (0.775 vs 0.775). The correspondence between
structure and accuracy therefore depends on a simulator setting that the structure does not encode.
Four of six hypotheses are supported and two are refuted.

Evidence about the model, not about a real organization. Association across four designed conditions;
no causal claim. Hypotheses fixed in `hypotheses.md` (commit `976fd31`) before the code (`426efd3`) and
before any computation.

## Instrument

Control (probe #88 forms): joint_commit triadic Φ = 2.000000; relay dyadic Φ = 0.000000. PASS.
`python -m org_frontier.classifier.validate` also prints "Instrument validated".

## Forms

| form | whole | Φ_MIP | major complex | core Φ | integrated core |
|---|---|---:|---|---:|:---:|
| flat_report | dyadic | 0.000000 | (A2,) | 1.000000 | no |
| hub_forward | dyadic | 0.000000 | (A2,) | 1.000000 | no |
| chain_relay | dyadic | 0.000000 | (A1,) | 1.000000 | no |
| hub_commit | dyadic | 0.000000 | (A1, M, A2) | 2.000000 | **yes** |

The single-node cores in the first three forms come from the agents' self-loops (A'=A, the idle-copy
convention). The whole-system verdict of hub_commit is dyadic because the investigator node only reads
M and can be cut away at no cost; the mediator and both agents form the irreducible core.

## Matched simulator run

Docking: the study-local simulator reproduces all 2400 rows of `../who_broke_prod/results/runs.csv`
(0 mismatches) before the new grid is used. New grid: 3200 runs (4 topologies × 4 scenarios × 50
seeds × 2 incentives × 2 access), `results/runs.csv`.

| topology | neutral / full | neutral / claims only | self-protective / full | self-protective / claims only |
|---|---:|---:|---:|---:|
| flat | 1.000 | 1.000 | 0.775 | 0.130 |
| hub | 1.000 | 1.000 | 0.775 | 0.130 |
| chain | 1.000 | 1.000 | 0.390 | 0.030 |
| hub_commit | 1.000 | 1.000 | 0.775 | 0.695 |

## Hypotheses

| H | result | numbers |
|---|---|---|
| H1 non-commit forms lack an integrated core | **SUPPORTED** | all three whole dyadic, Φ_MIP 0, single-node cores |
| H2 hub_commit core {A1,M,A2}, Φ = 2.0, whole dyadic | **SUPPORTED** | core Φ = 2.000000 |
| H3 structure ↔ accuracy, full access | **REFUTED** | 0.7750 vs 0.7750 (hub; flat ties), diff 0.0000, p = 1.000 |
| H4 structure ↔ accuracy, claims only | **SUPPORTED** | 0.6950 vs 0.1300 (hub; flat ties), diff 0.5650, p = 1.926e-34 |
| H5 commit vs convey at the hub, full access | **REFUTED** | 0.7750 vs 0.7750, diff 0.0000, p = 1.000 |
| H6 neutral ceiling | **SUPPORTED** | minimum accuracy 1.0000 |

## Reading

Each reading below is evidence about the model, not about a real organization.

- **Structure.** The instrument reproduces the lab's commit-and-read cut on incident-coordination
  encodings: forwarding, flat reporting and relaying have no multi-party core, and only a mediator whose
  next state depends jointly on both agents, and which both agents read, forms one (as in #88 and #37).
- **H4.** Without trace access, witnesses who read a commitment that disagrees with them re-send their
  claim, and the repeats outvote scapegoat claims. The Boolean form and the simulator mechanism encode the
  same commit-and-read design, so this match is not independent evidence that Φ predicts performance.
- **H3, H5 refuted.** With trace access, the investigator's one-check-per-round verification already
  finds the supported claim within the deadline in every condition where a witness exists; re-sends add
  nothing. The accuracy ceiling under access (0.775) is set by the runs with no witness, which no
  topology can recover.
- **Overall.** The structural reading separates the commit form from the others in every condition, but
  accuracy separates them in only one of the two access levels. Structure is not sufficient to predict
  investigative accuracy in this simulator, consistent with the lab's earlier structure-versus-behaviour
  nulls (#41, #98, #107).

## Limits

Designed 3–4 node encodings; the gate choices (OR for forwarding, AND for commit) and the self-loops are
encoding decisions. The `hub_commit` mechanism was designed by an author who had seen the earlier study's
results, before it was run. Four design points; association only. In-silico throughout.

## Reproduce

```
python org_frontier/studies/who_broke_prod_phi/analyze_who_broke_prod_phi.py
```
(about 2 s; deterministic, byte-identical `results/` on rerun)

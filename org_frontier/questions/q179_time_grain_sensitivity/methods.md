# q179 — methods

## Machinery

The bridge `org_frontier.field.rule_to_phi` encodes per-party Boolean determination rules into
a deterministic state-by-node TPM, classifies it by exact IIT-4.0 Φ over the MIP, and reads the
structural verdict (Φ_MIP = 0 dyadic, Φ_MIP > 0 triadic). Φ is not reimplemented; the bridge
wraps `org_frontier.classifier` and `org_frontier.probes.lib`. The same bridge propagates coder
disagreement into a Φ confidence interval through `phi_ci` (bootstrap-t over the coder panel,
Krippendorff-alpha agreement reported).

## Time-grain

The per-tick grain is the rule-TPM as written. The 2-tick macro grain composes the rule map
with itself: each macro-transition advances the deterministic dynamics two ticks, and the
composed map is re-encoded as a TPM and reclassified. `compose_tpm(rules, k)` builds the k-tick
TPM and infers its connectivity by the flip test.

## Ensemble

A seeded ensemble of 80 synthetic coded accounts (3 parties W, S, C; random Boolean truth
tables; `numpy.random.default_rng(0)`) is filtered to those that read triadic at the per-tick
grain. Each account is reclassified at the 2-tick grain. A flip is a per-tick triadic account
that reads dyadic at the 2-tick grain.

## Coder-disagreement panel

For each account a six-coder panel models a team in which three coders read the account
per-tick and three coarse-grain to two ticks. The panel of per-coder Φ readings goes through
the bridge `phi_ci`. The verdict is INDETERMINATE when the panel straddles the dyadic/triadic
boundary, operationalized as a panel whose minimum reading sits at the dyadic floor (Φ ≈ 0),
which puts the bridge CI's lower bound on that floor. A grain flip produces exactly this: the
per-tick coders read triadic, the coarse coders read dyadic.

## Structural predictor (a priori, no Φ)

`structural_score` reads grain-sensitivity from the rule's state-transition orbit without
computing Φ. Two ingredients: image collapse (distinct one-step images lost under the 2-step
map) and an even attractor period (a cycle of even length desynchronizes under a 2-tick
stride). The score is `collapse + 4·even_period_flag`. It is scored by rank AUC against the
flip label.

## Instrument control

The control validates four known cases: the faithful cyclic triad reads triadic with
max Φ_MIP = 2.0 per tick and flips to dyadic at the 2-tick grain; a memoryless feedforward
triple stays dyadic at both grains (grain-invariant); the structural predictor ranks the
cyclic triad above the feedforward one. The probe prints `CONTROL ... PASS`.

## Determinism

All RNG is seeded with `numpy.random.default_rng(0)` (ensemble draw and the bootstrap inside
`phi_ci`). The run is byte-identical across repeats.

## Run

```
source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
python -m org_frontier.questions.q179_time_grain_sensitivity.probe_time_grain_sensitivity
```

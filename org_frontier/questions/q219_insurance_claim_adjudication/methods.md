# Q219 — Stage 4 methods (fixed before computation)

All forms are deterministic Boolean systems with synchronous update over three nodes, classified by exact
IIT-4.0 Φ over the minimum-information partition. State tuples are indexed in label order
`("C", "E", "A")`: x[0] = claimant, x[1] = engine, x[2] = adjuster. The rules are written out in
`forms.py`; this file states them in full so each test reproduces without the code.

## Shared infrastructure

- Verdict and per-state Φ: `probes/lib.py` `verdict` (wraps `classifier.classify_rules`), which returns
  `structure`, `max_phi`, `mip_partition`, and `phi_profile` (Φ_MIP per reachable state).
- Major complex: `probes/lib.py` `major_complex(rules, labels)` → (core labels, Φ).
- PHI_EPS = 1e-9, the classifier's threshold.
- Run from the repo root with the project venv active (Python 3.12.15, PyPhi IIT-4.0 line).

## Bit meanings

- **C (claimant):** 1 = the claimant is pressing an open claim that is large or contested; 0 = no open
  claim, or a small one.
- **E (engine):** 1 = the engine flags the claim (route to human review, or fraud flag in variant c);
  0 = no flag, the engine's own decision stands (auto-approval in variant b).
- **A (adjuster):** in a and b, 1 = the adjuster approves the claim it holds; in c, 1 = the adjuster
  upholds the engine's flag, 0 = the adjuster overrides it.

The claim-size bit for variant b is carried by C. No fourth node is used.

## Instrument control (run first)

Before any comparison, two established forms must reproduce their verdicts:
- `ats_triad_mediator` (W'=S, S'=W∧C, C'=S) reads triadic at Φ_MIP = 2.0.
- `chat_dyad` (W'=S, S'=W, C'=C) reads dyadic at Φ_MIP = 0.
A probe asserts both and stops if either fails. `python -m org_frontier.classifier.validate` must also
print `Instrument validated` in the same environment.

## Forms

| form | variant | C' | E' | A' | reading |
|---|---|---|---|---|---|
| `pipe` | a | A | C | E | engine forwards the claim, adjuster's decision copies what arrives, claimant reads the decision |
| `gated` | b | E ∧ ¬A | C | E ∧ C | engine flags large/contested claims (small ones auto-approve and close); adjuster acts only on a flagged claim and approves when the claim file stands; the claim stays open only if flagged and not approved |
| `loop` | c | A | C ∧ A | E ∧ C | adjuster upholds a flag only when flag and claim file agree; engine's next flag learns from the adjuster's last call (an override switches it off); claimant reads the adjuster's call |
| `loop_nolearn` | c, robustness | A | C | E ∧ C | `loop` without the learning edge A→E |
| `loop_frozen_claimant` | c, liveness | C | C ∧ A | E ∧ C | `loop` with the claimant no longer reading the decision |

In the lambda convention of `verdict()`:

```python
PIPE                 = [lambda x: x[2],              lambda x: x[0],        lambda x: x[1]]
GATED                = [lambda x: x[1] & (1 - x[2]), lambda x: x[0],        lambda x: x[1] & x[0]]
LOOP                 = [lambda x: x[2],              lambda x: x[0] & x[2], lambda x: x[1] & x[0]]
LOOP_NOLEARN         = [lambda x: x[2],              lambda x: x[0],        lambda x: x[1] & x[0]]
LOOP_FROZEN_CLAIMANT = [lambda x: x[0],              lambda x: x[0] & x[2], lambda x: x[1] & x[0]]
```

## H1 test — pass-through pipe

- **Form:** `pipe` (identical to Q11 `rot_ring(3)` under C, E, A = x0, x1, x2).
- **Measure:** `verdict(PIPE, LABELS).structure`, `max_phi`, `phi_profile`; `major_complex` core labels.
- **Controls:** the instrument control above.
- **Decision rule:** H1 confirmed if `pipe` is triadic (max Φ_MIP > 1e-9) with major complex
  {C, E, A}. Refuted if dyadic, or if the major complex has fewer than three labels.
- **Script:** `probe_457_pipe.py`.

## H2 test — threshold auto-approval

- **Form:** `gated`.
- **Measure:** `verdict` structure and `phi_profile`; `major_complex` core labels.
- **Controls:** the instrument control above.
- **Decision rule:** H2 confirmed if (i) `gated` is triadic, (ii) the major complex is exactly {C, E, A},
  and (iii) every state in `phi_profile` with Φ_MIP > 1e-9 has E = 1 and every state with E = 0 has
  Φ_MIP ≤ 1e-9. Partial if (i) and (ii) hold and (iii) fails. Refuted if (i) or (ii) fails.
- **Script:** `probe_458_gated.py` (planned).

## H3 test — fraud-flag loop with override learning

- **Form:** `loop`.
- **Measure:** `verdict` structure and `max_phi`; `major_complex` core labels.
- **Controls:** the instrument control above.
- **Decision rule:** H3 confirmed if `loop` is triadic with major complex {C, E, A}. Refuted if dyadic,
  or if the major complex has fewer than three labels (for example {E, A}).
- **Script:** `probe_459_loop.py` (planned).

## H4 test — robustness to removing override learning

- **Form:** `loop_nolearn`, compared to `loop`.
- **Measure:** `verdict` structure; `major_complex` core labels.
- **Controls:** the instrument control above; `loop` (H3) as the reference form.
- **Decision rule:** H4 confirmed if `loop_nolearn` is triadic with major complex {C, E, A}. Refuted if it
  is dyadic or its core has fewer than three labels. The Φ magnitudes of `loop` and `loop_nolearn` are
  reported but not compared: the program treats Φ magnitude as encoding-dependent.
- **Script:** `probe_459_loop.py` (same script as H3, planned).

## H5 test — liveness of the claimant

- **Form:** `loop_frozen_claimant`, compared to `loop`.
- **Measure:** `verdict` structure and `max_phi`.
- **Controls:** the instrument control above; `loop` (H3) as the reference form.
- **Decision rule:** H5 confirmed if `loop_frozen_claimant` is dyadic (max Φ_MIP ≤ 1e-9). Refuted if
  triadic.
- **Script:** `probe_460_liveness.py` (planned).

## Numbering

Probe numbers start at 457. Upstream `main` and `contrib` log probes up to #451; open pull requests claim
#453–#456 (#810) and #454 (#806), so 452–456 are avoided.

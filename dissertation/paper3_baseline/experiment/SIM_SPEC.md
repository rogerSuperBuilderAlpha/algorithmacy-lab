# Simulation spec — agent-based coordination experiment (buildable now)

**Internal working doc.** The runnable computational version of the experiment, read as a behavioral
*consistency check* (the agents never see Φ, but Φ and difficulty both derive from the wiring, so this is not
an independent validation). Tests whether Φ(structure) tracks how hard independently-motivated agents find it
to coordinate through that structure.

## The task: transmit-and-agree through a structured channel

A pure coordination game that maps onto the Boolean W–S–C structures, designed so difficulty depends on how
much the structure impedes the parties' ability to influence each other — a property computed by the *agents'
performance*, never by Φ.

- Three nodes: **W** (agent), **S** (mechanical mediator), **C** (agent). Values in {0,1}.
- Each round *t*, agent_W receives a **private goal bit** `g_t` (uniform random). Agent_C does **not** see it.
- Both agents choose their node value (`W_t`, `C_t`). The mediator sets `S_t = mediator_rule(W_{t-1}, C_{t-1})`
  per the condition (one mediator determination per round = one state; enforces modeling choice #2).
- **Reward (joint):** +1 iff `C_t == g_t` (the counterpart ends up producing the goal the worker holds).
  To succeed, the worker must drive the goal *to the counterpart* — but the only path from W to C is whatever
  the condition's wiring permits.
- **Observability = the condition's wiring (modeling choice #1/#3, exact).** Each agent observes exactly the
  nodes its own node reads in the condition, from the previous round:
  - C0 Dyadic: W reads C; C reads W (direct channel) → easy transmission.
  - C1 Parity: W reads S; C reads S; S = W ⊕ C → W influences C only through a parity-entangled channel.
  - C2 Partial: W reads S and C; C reads S and W → mediated **plus** a direct channel.
  - C3 Strict: W reads S; C reads S; S = W ∧ C → W influences C only through a conjunctive determination.

Difficulty = how hard it is to learn a policy that gets `g` into C through that channel. This is plausibly
related to Φ (irreducible structures resist decomposed, piecewise coordination) but is **computed entirely
from agent behavior**, so Φ predicting it is a genuine test.

## Agent model (FIX A PRIORI — do not tune to make Φ win)

- Each agent is an independent **tabular Q-learner** (or equivalent simple RL): policy maps its observation
  (its permitted inputs + own recent history + for agent_W, the goal `g_t`) to its action, updated by reward.
- Shared, fixed hyperparameters across all conditions (learning rate, ε-greedy schedule, discount). Set them
  once, before running, and report them verbatim.
- Agents do **not** observe Φ, the condition label, or the other agent's policy. The decision rule is
  bounded-rational reward maximization, motivated independently of the measure being tested.
- Pre-register the rule and hyperparameters in `agent.py` docstring before the first scored run.

## Procedure

- For each condition C0–C3: run **N independent agent pairs** (fresh Q-tables), each for **T rounds**.
- Record per round: goal, actions, mediator value, reward.
- Repeat across **seeds** for CI; report mean and dispersion. (Seeds passed in via args/config; do not call
  Math.random/Date — match repo discipline.)

## Dependent measures (coordination difficulty)

- **Asymptotic success rate** — mean reward over the last X% of rounds (primary).
- **Rounds-to-criterion** — first round at which a sliding-window success rate exceeds a threshold (speed).
- **Final-policy coordination** — success rate of the greedy (ε=0) policies after training.

## Analysis plan (fixed before running)

1. **H1 monotonicity:** rank-order correlation (Spearman) between Φ {0, 0.5, 0.83, 2.0} and difficulty
   (1 − success) across C0–C3. Predicted positive.
2. **H1a contrast:** C2 vs C3 (back-channel only; AND fixed). Predicted: C3 harder (lower success, slower).
   Report effect size + CI.
3. **H2 / Cerullo:** is C1 (parity) in its predicted rank, or anomalous? Compare C1 vs C3 (XOR vs AND, both
   strict-topology).
4. **Φ-beyond-features (the strong test, mirrors catalog R²=0.20):** regress difficulty on simple structural
   features (edge count; does a W→C path exist; mediator in-degree) and ask whether **Φ adds predictive
   power beyond them**. If difficulty is fully explained by "is there a direct W→C edge," Φ is redundant
   here; if Φ separates conditions that the simple features do not, that is the in-silico analogue of the
   dissertation's "Φ is not a feature count" claim.

## Non-circularity & validity pre-commitments

- Agent rule + hyperparameters fixed and documented **before** any scored run; never re-tuned per condition.
- Same task, reward, round cap, and information-per-role across all conditions; **only the wiring differs**,
  and **party count is fixed at 3**.
- Report honestly: a simulation validates the **mechanism in silico** (the structure axis is not vacuous and
  behaves as the model claims) — it does **not** show humans coordinate as these agents do. External validity
  is the human study's job.
- Pre-register a **null-supporting outcome** as publishable: if Φ does not predict difficulty here, say so
  and retreat Paper 3's claims to model-characterization.

## Code plan (reuse repo infrastructure)

```
experiment/sim/
  agent.py        # the a-priori Q-learner; hyperparameters frozen in docstring
  task.py         # transmit-and-agree environment; observability per condition wiring
  conditions.py   # the 4 structures (import rules from ../../typology_phi.py); Φ via proxy_audit.exact_phi
  run.py          # N pairs × T rounds × seeds per condition -> results/sim_runs.csv
  analyze.py      # H1/H1a/H2 + Φ-beyond-features regression -> results/sim_summary.csv, figure
  README.md       # how to run; the frozen agent rule; the analysis outputs
```
- Φ values come from the existing `typology_phi.py` / `proxy_audit.exact_phi` — do not re-implement.
- Env: `~/iit-playground/venv-4.0/bin/python` (scikit-learn already installed if RL needs it; tabular Q
  needs only numpy).

## Estimated effort
- Build + smoke: ~half a day. Full runs (4 conditions × ~200 pairs × ~2k rounds × ~5 seeds): minutes–hours
  on CPU. Analysis: short. This is genuinely runnable now.

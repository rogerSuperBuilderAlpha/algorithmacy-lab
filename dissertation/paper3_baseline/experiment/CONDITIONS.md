# Conditions and operationalization

**Internal working doc.** The 4 experimental conditions, their exact structures and Φ, and how the **three
modeling choices** become exact controls when we manipulate rather than observe.

## The three modeling choices → exact experimental controls

In Paper 3 these are *assumptions an analyst makes when modeling a real org*. In the experiment they are
*things we build*, so each becomes exact and the modeling noise that doomed the field study is gone:

| Modeling choice (Paper 2) | What it means | In the experiment it becomes… |
|---|---|---|
| **1. Application-layer representation** — what we model the coordination *as*: a 3-node W–S–C system over the observable layer, not the algorithm's internals | which nodes exist and how each reads the others | We *build* the W/S/C roles and the wiring. No inference; the structure is exact. |
| **2. State-individuation rule** — what counts as one "state": a new state only when the mediator commits a real determination | how the event stream is cut into steps | The task runs in discrete **rounds**; one round = one mediator determination = one state. The rule is enforced by the task loop, not inferred. |
| **3. Party partition** — what "reducible" is measured against: factoring along the lines between the parties | which division defines the dyad/triad question | The three **roles are the parties** by construction, so Φ is read over the party partition exactly. |

This is the methodological payoff of manipulate-don't-observe: all three choices are controlled, so a Φ↔
difficulty relationship cannot be dismissed as an artifact of how the analyst modeled a messy real org.

## The 4 conditions (all n = 3: Worker W, System/mediator S, Counterpart C)

Node order (0,1,2) = (W, S, C). Rules give each node's next value from the current (W,S,C). Φ = exact
IIT-4.0 system Φ (max over reachable states), as computed in `../typology_phi.py`. These are the canonical
typology structures, reused so the experiment's IV is anchored to the dissertation's own numbers.

### C0 — Dyadic baseline (Φ = 0.00)
- **Story:** the two parties coordinate directly; the system does not constitute their coupling.
- **Rules:** W′ = C, S′ = S, C′ = W  (parties read each other; mediator inert).
- **Back-channel:** yes (direct). **Mediator determination:** none constitutive.
- **Role in design:** floor / negative control. Easiest predicted.

### C1 — Parity mediation (Φ = 0.50)
- **Story:** parties reach each other only through the system, and the system commits on whether they
  *differ* (a parity/complementary determination).
- **Rules:** W′ = S, S′ = W ⊕ C, C′ = S.
- **Back-channel:** no. **Mediator determination:** XOR (parity).
- **Role in design:** the **Cerullo / H2 probe** — does parity's observed difficulty match its Φ rank?

### C2 — Partial mediation (Φ = 0.83)
- **Story:** the system matches the parties on a joint condition, but they also retain a direct channel.
- **Rules:** W′ = S ∨ C, S′ = W ∧ C, C′ = S ∨ W.
- **Back-channel:** yes. **Mediator determination:** AND.
- **Role in design:** the "match-and-release" middle; pairs with C3 for the clean back-channel contrast.

### C3 — Strict mediation (Φ = 2.00)
- **Story:** the parties reach each other *only* through the joint determination; no direct channel.
- **Rules:** W′ = S, S′ = W ∧ C, C′ = S.
- **Back-channel:** no. **Mediator determination:** AND.
- **Role in design:** ceiling; hardest predicted. **C2→C3 is the H1a "eliminate the dyad" contrast**
  (identical AND determination; the *only* difference is the back-channel; Φ 0.83 → 2.00).

## Contrast map

- **Primary monotonicity (H1):** difficulty vs Φ across {C0:0, C1:0.5, C2:0.83, C3:2.0}.
- **Clean single-factor (H1a):** **C2 vs C3** — back-channel present vs absent, AND held fixed.
- **Determination-function probe (H2):** **C1 vs C3** — both strict-topology (no back-channel), XOR vs AND;
  isolates whether the determination *function* (parity vs conjunction) drives difficulty as Φ says.

## To verify before building
- [ ] Re-run `../typology_phi.py` and confirm the four Φ values (0.00 / 0.50 / 0.83 / 2.00) reproduce.
- [ ] Confirm each condition's structure is a *playable coordination task* (W and C have a joint goal that
      the mediator's determination structure helps or hinders) — see `SIM_SPEC.md` task definition.
- [ ] Confirm party count is genuinely fixed at 3 across all four (it is, by construction).

# Paper 2 — computed results (exact IIT-4.0 Φ)

All values exact IIT-4.0 system Φ via `proxy_audit.exact_phi` (PyPhi `new_big_phi.sia`), over
3-node application-layer systems (Worker, System/mediator, Counterpart). Reproduce:
`~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/phi_instrument.py`
and `.../worked_examples.py`.

## 1. Validation controls (the gate — run before any worked example)

| Control | structure | result |
|---|---|---|
| **Factoring** | C causally decoupled (W'=S, S'=W, C'=C) | Φ = **0.000** at all 8 states; MIP = none. The W–S–C partition reduces it. |
| **Irreducible** | each party reads the other two (W'=S∨C, S'=W∧C, C'=W⊕S) | Φ up to **0.830** (mean 0.484); MIP = full tripartition **{W,S,C}**. No partition reduces it. |

The instrument cleanly separates a form that factors along party lines (Φ = 0) from one that does
not (Φ > 0, irreducible across the three parties). Gate passed.

## 2. Worked application

### A. Dyadic limit — chat with a language model
Two parties only; the model commits nothing that couples a third (C decoupled): W'=S, S'=W, C'=C.
**Φ = 0.000 at every state.** The form factors to the two parties already visible. Dyadic.

### B. Irreducible triad — résumé → ATS → hiring manager
Faithful **mediator topology**: applicant and manager reach each other *only* through the system
(no direct W–C edge). Applicant reads the ATS determination (W'=S), manager reads it (C'=S), and
the ATS commits a determination `f(W,C)` (forward iff the résumé carries the match-signal and the
manager's configured profile is active). Sweep of the committed determination:

| ATS commits `S' = f(W,C)` | max Φ | mean Φ | MIP at max-Φ state | irreducible? |
|---|---|---|---|---|
| AND, OR, NAND, NOR | 2.000 | 0.500 | {W, SC} | **yes** |
| XOR, XNOR | 0.500 | 0.500 | {W, S, C} (full tripartition) | **yes** |
| `f = W` (ignores the manager) | 0.000 | 0.000 | none | no — reduces |
| `f = C` (ignores the applicant) | 0.000 | 0.000 | none | no — reduces |

### C. The false dyad — rideshare driver → app → rider

The classifier's hardest direction: a form that **presents to the worker as a two-party relationship
with an app** — the driver only ever touches the platform and can neither see nor choose the rider —
yet is causally a three-party system, because the rider is constitutive of the dispatch the platform
commits while never directly interacting with the driver (strict mediator topology, no W–C edge). The
mechanism: `W' = ¬S` (the driver's availability is consumed by a dispatch), `S' = W ∧ C` (the platform
dispatches iff an available driver *and* a waiting rider), `C' = C ∧ ¬S` (the rider keeps waiting until
served).

| model of the same situation | structure | result |
|---|---|---|
| **Full triad** — rider constitutive | `S' = W ∧ C` (dispatch reads both sides) | Φ = **2.000** at state (1,1,1); MIP = **{W, SC}**; mean 0.400 over 5 reachable states. **Triad.** |
| **Dyadic model** — rider dropped | `S' = W` (dispatch reads the driver only) | Φ = **0.000** at every state; MIP = none. **Dyad.** |

The two models differ by **exactly one dependency** — whether the platform's determination reads the
unseen third party. Everything else (`W' = ¬S`, `C' = C ∧ ¬S`, the topology the driver experiences) is
identical. So the dyad/triad verdict is carried by the single edge `S ← C`: include the constitutive
rider and the structure the driver cannot see scores Φ = 2.0 (irreducible triad); model only the
visible driver↔app channel and it collapses to Φ = 0 (a dyad). **This is the false dyad made
computable**: a dyadic construct — algorithmic competence, human-app interaction — scores the case 0
because it omits C, while the case *is* an irreducible triad. The misclassification is the modeling
choice, and Φ catches it.

(The companion direction, the **false triad** — three parties present, structure still factors — is the
party-ignoring mediator in §2.B: `f = W` or `f = C` → Φ = 0 despite three visible parties. The
classifier cuts against appearance both ways.)

## 3. The central finding — eliminating the dyad maximizes irreducibility

The 3-party *topology* alone does not make a form triadic. Irreducibility turns on (a) **the
determination the mediator commits** and (b) **whether the parties can interact directly**.

First, the form is irreducible for *every* determination that is a genuine joint function of both
parties, and reduces to a dyad precisely when the mediator's determination ignores one party.

Second, and the paper's spine: holding the determination fixed (S' = W AND C), Φ **falls
monotonically as direct worker–counterpart interaction is added**.

| direct W–C channel | max Φ |
|---|---|
| none (parties reach each other only through S) | **2.00** |
| weak (parties also read each other directly) | **0.83** |
| strong (parties coordinate directly) | **0.00 — reduces to a dyad** |

So coordination is **most irreducible when the dyad is eliminated**. The political-economy reading
is immediate and computed, not asserted: the platform's position is constituted by triadic
irreducibility, direct dyadic contact destroys that irreducibility, and the platform therefore has
a structural **incentive to design the dyad out** — to prevent the worker and counterpart from
coordinating except through its committed determination. This is what platforms do (drivers cannot
contact riders off-app; applicants cannot reach hiring managers around the ATS), and Φ explains why:
removing the dyad maximizes the irreducibility on which the form, and the demand for algorithmacy,
depends.

> A coordination form is triadic **iff** the mediator commits a determination both parties depend on
> and the parties cannot coordinate around it. Φ over the application-layer matrix is the computed
> test: Φ > 0 demands algorithmacy; Φ = 0 is navigable with literacy. The chat dyad and the
> "mediator-that-ignores-a-party" both score 0; the genuine ATS triad scores > 0, and the score
> rises as the dyad is suppressed.

## 4. Caveats already visible (for the write-up)

- **Read functions matter too.** A separate feedback variant (W'=¬S, S'=W∧C, C'=S∨C) reduced to
  Φ = 0, so irreducibility depends on how the parties read the determination as well as on the
  determination itself. The clean worked example uses faithful reads (each party tracks the
  committed determination); the dependence on read structure is a point to state honestly, not
  hide.
- **State-alphabet dependence** (the §4 pre-registered rule) governs how these binary nodes are
  individuated; the controls and worked examples all use the same rule.
- **No outcome anchor** — a Φ value is not yet a difficulty scale. That is Paper 3.

## 5. Still to do

- Evaluate the explicit {W}{S}{C} tripartition via `pyphi.new_big_phi` for the irreducible case (to
  state the "the W–S–C partition cannot reduce it" claim directly, beyond the MIP).
- The continuous-platform hardest case (Uber commits in a stream) — the rule's stress test (§4),
  handed to Paper 3.
- `state_alphabet.md` (pre-registered individuation rule + TPM-from-logs construction) and the paper.

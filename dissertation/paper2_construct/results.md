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

## 3. The eliminate-the-dyad result — binary, not a magnitude gradient (corrected)

The 3-party *topology* alone does not make a form triadic. Irreducibility turns on (a) **the
determination the mediator commits**, (b) **the read structure** (§4), and (c) **whether the
parties can interact directly**.

The determination being a genuine joint function of both parties is **necessary but not
sufficient**: holding `S' = W∧C` fixed and sweeping the read structure (`read_structure_sweep.py`),
only **22%** of strict-mediation read pairs keep Φ > 0; the "realistic feedback" reads collapse it
to 0 (§4). So the earlier claim that the form is irreducible for *every* joint determination is
withdrawn — it holds only for the faithful (bottleneck) reads.

The "design the dyad out" result is now stated at the **binary** level only, because the magnitude
sweep is **not monotone** in directness. Holding `S' = W∧C` fixed and sweeping encodings of an
added direct W–C channel (`eliminate_dyad_sweep.py`):

| direct W–C channel | encoding | max Φ |
|---|---|---|
| none (only through S) | W'=S, C'=S | **2.00** |
| weak, disjunctive | W'=S∨C, C'=S∨W | **0.83** |
| weak, conjunctive | W'=S∧C, C'=S∧W | **6.00** ← *larger than baseline* |
| weak, parity | W'=S⊕C, C'=S⊕W | **2.00** |
| full bypass | W'=C, C'=W | **0.00 — reduces to a dyad** |

The **endpoints are robust** (no channel → triad; full bypass → dyad) but the middle is
encoding-dependent (0.83 vs 6.00), so the old "Φ falls monotonically" / "irreducibility bleeds
away" framing was an artifact of the disjunctive encoding and is dropped. The political-economy
reading is kept at the binary level only: eliminating the direct channel is what keeps the form
**classified** as a triad, so a platform has a structural reason to design the direct dyad out. The
magnitude gradient is not claimed.

> A coordination form is triadic **iff** Φ over its minimum-information partition is > 0: the
> mediator commits a determination both parties depend on, the reads keep each party tracking it,
> and the parties cannot coordinate around it. Φ > 0 demands algorithmacy; Φ = 0 is navigable with
> literacy. The chat dyad and the "mediator-that-ignores-a-party" both score 0; the bottleneck ATS
> triad scores > 0; restoring a full direct channel collapses it back to 0.

## 4. Read structure, and why the magnitude is not a scale

- **Read functions decide the verdict, not just the determination.** Sweeping the strict-mediation
  read space with `S'=W∧C` fixed (`read_structure_sweep.py`): Φ ranges 0–2; only 22% of read pairs
  give Φ > 0. The pure bottleneck (W'=S, C'=S) gives Φ = 2.0; the realistic feedback (W'=¬S,
  C'=S∨C) gives Φ = 0.0. The reads that preserve the triad verdict are those keeping each party's
  state a live function of the mediator's commit. This is now in the draft (§6), not a hidden caveat.
- **State-alphabet dependence** (the §4 pre-registered rule) governs how the nodes are individuated;
  but the rule does *not* fix the node update functions, which is where the magnitude lives. Hence
  the magnitude is read only ordinally and the paper leans on the binary classification.
- **No outcome anchor** — a Φ value is not yet a difficulty scale. That is Paper 3.

## 5. Resolved / handed forward

- **Party-partition vs MIP — resolved** (`party_partition.py`). Φ over the complete {W}{S}{C} cut is
  positive even for dyads (it severs the genuine {W,S} coupling: chat dyad → 2.0, dyadic model →
  1.0), so the complete cut over-calls and is *not* the test. The binary verdict is Φ over the
  minimum-information partition = 0; the MIP is party-respecting (e.g. {W,SC}) but not the complete
  cut. The draft (abstract, §2.2, §5) is corrected to say this.
- **Φ vs the cheap tests, static AND dynamical — resolved** (`phi_vs_separability.py`,
  `dynamical_comparator.py`; now in draft §6, "the apparatus earns its weight"). The robust claim
  is an EXHIBIT, not an aggregate percentage: the maximally-connected, non-degenerate form
  **W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S)** (all six edges, strongly connected, no constants) has
  exact Φ=0 at every reachable state (verified) — a form every connectivity/CI test calls triadic
  and the MIP machinery alone reduces. Aggregate counts are comparator-dependent and deliberately
  NOT the headline: vs a static test, 57.8% agree (1,728 connected-but-Φ=0, of which 73.6% are
  pinned-constant degeneracy); vs an all-combinations dynamical test, 59.6% / 0-reverse / 456
  non-degenerate over-calls; vs the *fair reachable-only* dynamical test, **89.8% / 8-reverse / 408
  non-degenerate over-calls**. So "Φ strictly stronger / 0-reverse" is an artifact of the weaker
  comparator; what is robust across comparators is the direction (hundreds of non-degenerate forms
  Φ reduces that cheap tests over-call) and the exhibit. NOTE: an earlier draft mis-transcribed the
  exhibit as `S=W∧¬C` (which gives Φ=0.83) — a `catalog.py` BIN_LABEL A/B-swap bug, now fixed.
- The continuous-platform hardest case (Uber commits in a stream) — the rule's stress test (§4),
  handed to Paper 3 / the empirical program.

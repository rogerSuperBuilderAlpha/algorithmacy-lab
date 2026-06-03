# Findings — multi-party coordination

Does adding parties change whether a coordination form demands algorithmacy? From
`results/named.csv` and `results/population_n4.csv`, exact IIT-4.0 Φ on the IIT-4.0 venv.

## Named four-party forms

| Form | Verdict | Φ | Reading |
|---|---|---|---|
| pool_all_required (S = W ∧ C1 ∧ C2) | triadic | 3.00 | all parties jointly required |
| mediator_chain (W→S1→S2→C) | triadic | 2.00 | layered platform, two mediators in series |
| substitutable_counterparts (S = W ∧ (C1 ∨ C2)) | dyadic | 0.00 | counterparts interchangeable |
| one_counterpart_constitutive (S = W ∧ C1) | dyadic | 0.00 | second counterpart a spectator |
| decoupled_control | dyadic | 0.00 | second counterpart outside the form |

`pool_all_required` reproduces the dissertation's higher-order result (pooled rideshare/crowdwork,
Φ = 3.0), validating the n = 4 modeling.

Two findings stand out.

**Substitutability collapses irreducibility.** When the mediator can satisfy its determination with
*either* counterpart (`W ∧ (C1 ∨ C2)`), the form factors — it is dyadic. Only when the determination
requires *all* parties jointly (`W ∧ C1 ∧ C2`) does it stay triadic. A platform that pools
interchangeable counterparts is structurally a set of independent worker–mediator dyads; it demands
only literacy. A platform that binds all parties into one joint determination demands algorithmacy.

**Layered mediation stays triadic.** Two mediators in series (W → S1 → S2 → C, no direct end-to-end
edge) is irreducible (Φ = 2.0). Routing coordination through a chain of systems does not factor it.

## Mediator-chain depth: Φ is invariant to chain length

`chains.py` lengthens the chain W → S1 → ... → Sk → C, each mediator committing jointly from its two
neighbours. The result is a clean invariance.

| chain | n | verdict | Φ | MIP cut |
|---|---|---|---|---|
| k = 1 | 3 | triadic | 2.00 | {W \| S1C} |
| k = 2 | 4 | triadic | 2.00 | {WS1 \| S2C} |
| k = 3 | 5 | triadic | 2.00 | {WS1 \| S2S3C} |
| k = 4 | 6 | triadic | 2.00 | {WS1S2 \| S3S4C} |

Every chain length is triadic, **Φ stays exactly 2.0**, and the minimum-information partition is
always a single balanced two-part cut near the chain's middle. Deepening the mediation — more layers
of intermediary, sub-contracting, nested platforms — never factors the form and never changes its
integration. The whole chain is irreducible at one cut, at any depth. This is the structural
opposite of the multi-counterpart case below, where adding parties *raises* the chance of factoring;
adding *depth* to a single line of mediation does not.

## Scaling: irreducibility gets rarer as parties are added

Sampled strict-mediation n = 4 family (1500 forms, seed 7): mediator S reads all three outer parties
via a random Boolean function; each outer party reads S via a random function.

| Quantity | n = 3 (full family, 256) | n = 4 (sample, 1500) | n = 5 (sample, 400) |
|---|---|---|---|
| triadic (Φ > 0) | 9.4% | **2.3%** | **0.0%** |
| P(triadic \| mediator reads all parties) | 15.0% | 2.6% | 0.0% |
| P(triadic \| mediator does not read all) | 0.0% | 0.0% | 0.0% |

One claim generalizes cleanly: the mediator reading **all** parties is **necessary** at every n
(0% triadic without it), and is steadily **less sufficient** as n grows (15% → 2.6% → 0%).

**Random coupling almost never produces irreducibility, and never less so than at scale.** The
single-mediator triadic rate falls to zero by n = 5 *in random sampling*. This does not mean no
n = 5 form is triadic — constructed ones are (the all-required pool Φ = 3.0, the depth-3 chain
Φ = 2.0 below). It means irreducibility requires *specific* structure — an all-binding joint
determination, or a non-factoring chain — that random coupling produces ever more rarely as parties
multiply. Adding parties does not build integration; it dilutes the chance of it.

Irreducibility is markedly **rarer** at n = 4 (2.3% vs 9.4%), and a reachability robustness check
confirms this is real, not an artifact. Adding a party makes it harder to keep everyone jointly live
to the mediator's commit, so most multi-party forms factor.

The org-theory reading: more parties does not mean more integration. The opposite. Triadicity
survives an added party only when the mediator's determination strictly binds all of them (the
all-required conjunction) or routes them through a non-factoring chain. The algorithmacy thesis is
about whether the joint determination is irreducible, not about party count.

## Robustness: the scaling drop is not a reachability artifact

A confound had to be ruled out. Every one of the 1500 sampled deterministic n = 4 forms collapses to
≤ 4 of 16 reachable states (1338 to exactly 4, 161 to 2, 1 to 1; none reach 8+) — the deterministic
dynamics drive the outer parties to synchronize with the mediator, so exact Φ sees a tiny attractor.
If the collapse were suppressing triadicity, the low rate would be an artifact.

`robustness.py` rules it out. Add independent per-node output noise (no added coupling, so it cannot
manufacture integration where a form factors) to make all 16 states reachable, then recompute exact
Φ. On 300 sampled forms at noise 0.1:

| | triadic rate |
|---|---|
| deterministic (collapsed, ≤4 states) | 3.3% (10/300) |
| noisy (full 16-state reachability) | **3.3% (10/300)** |

The rates are identical. Lifting the collapse does not change the verdict: the forms that factor
under collapse also factor under full reachability. The n = 4 → lower-triadic-rate result is genuine.

The same check at n = 5 (60 forms, noise 0.1) gives **0/60 triadic under full 32-state
reachability** — matching the deterministic 0%. So the decline to zero is real at n = 5 too, not an
artifact of the (even heavier) collapse there. Independent noise does not manufacture irreducibility
the random coupling lacks.

## Breadth and depth are independent, and one law covers both

A depth-2 chain whose final mediator serves two counterparts tests whether mediation depth rescues a
form where the counterparts are substitutable.

| Form | Verdict | Φ |
|---|---|---|
| deep_pool_all (depth-2, S2 = S1 ∧ C1 ∧ C2) | triadic | 2.00 |
| deep_substitutable (depth-2, S2 = S1 ∧ (C1 ∨ C2)) | dyadic | 0.00 |

Depth does not rescue substitutability. The form with substitutable counterparts factors whether or
not it has mediation depth. Depth and breadth act on different things: depth (layers of mediation)
never factors a binding determination; breadth (parties) only stays bound if every party is jointly
required.

The whole multi-party arc reduces to one law. **A coordination form is triadic if and only if every
party is bound into a single irreducible joint determination — regardless of how many mediation
layers separate them.** Substitutability or optionality of any party collapses the form to dyadic;
mediation depth never does. Adding parties dilutes the chance of meeting the condition (9.4% → 0%);
adding depth preserves it (Φ = 2.0 at every length).

## Caveats

- **Sample, not census.** The n = 4 family has 256 × 4³ = 16,384 strict-mediation forms; 1500 are
  sampled (300 for the noisy check). The n = 3 figure is the full 256-form census
  (`../corpus/population.py`).
- Binary verdict only; Φ magnitude is encoding-dependent (e.g. the all-required conjunction inflates
  Φ to 3.0), not a scale. Cross-node Φ magnitudes are not comparable.

# Committed determination: one axis across six exact-Φ studies of Boolean coordination models

A synthesis of the six papers produced through the lab's research protocol — the core-membership law,
the coordination-logic atlas, the discriminant-boundaries study, the platform-position theory, the
field protocol, and the robustness work folded into the first. It ties them to one structural variable
on Boolean models of coordination, maps that variable to its image in five literatures, and states what
the program adds and what it recovers. It introduces no new computation; it draws on the six studies and
the literature each one verified. This version is revised in response to a four-member committee review
(`committed_determination_committee_review.md`); a revision note at the end maps the changes to the
panel's objections.

## The claim, stated to avoid circularity

The six studies share one structural variable, and stating it carefully matters, because stated loosely
it is circular. Define a determination as **committed** by its *construction*, independently of any Φ
verdict: a mediating system's next state is a function of more than one party (it reads them jointly),
and each party's next state is a function of the system's (they act on what it commits). This is a
property of the wiring and the update rules — readable off the connectivity matrix and the truth tables —
not of the irreducibility result. The empirical content of the program is then a *non-trivial* question:
when does committed construction, so defined, actually produce an irreducible cause-effect structure
(a triadic Φ verdict)? The answer is "not always, and not obviously." A k-of-n quorum mediator reads all
parties jointly and is read back by all of them — committed by construction — yet factors at every
interior threshold. A routing cycle that looks like a pass-through is irreducible. So the verdict is not
a restatement of the construction; the gap between them is where the studies do their work.

## The common instrument

The lab models a coordination arrangement as a small Boolean dynamical system whose nodes are the
parties — a worker, a mediating system, a counterpart, sometimes more — and reads exact IIT-4.0 Φ over
the minimum-information partition. A form is **triadic** when no party-line partition factors its
cause-effect structure, **dyadic** when one does. The major complex names which parties are inside the
irreducible structure. Φ is read only as this binary verdict and the membership; its magnitude is not
treated as a scale.

## The six studies, partitioned by what they show

Two of the studies' results are **analytic** — the axis was built into the model specification, so the
verdict confirms the encoding is faithful rather than discovering a fact. Three are **computed against a
naive expectation** — the verdict went against the obvious reading, which is where computation earns its
place. The synthesis marks which is which.

**A — who is bound (core-membership law).** A party is inside the irreducible core when it is
bidirectionally coupled to the determination and causally pivotal to it. The coupling half is *analytic*:
IIT requires it, and the PyPhi implementation draws complex candidates only from bidirectionally coupled
("causally significant") nodes, so the 0/660 non-bidirectional-in-core result is close to tautological by
construction — the study says so, and so does this synthesis. The pivotality half is the *informative*
part: across a population of forms, complex membership rises with the determination's single-node
sensitivity to a party. It is reported over two populations — rank-AUC ≈ 0.89 in the strict-mediation
family (256 determinations) and ≈ 0.63 in the harder unconstrained family — and the difference is the
point: single-node sensitivity undercounts the higher-order joint effects that govern membership in the
unconstrained family, so the relation is a first-order proxy, strong in the construct's natural domain
and moderate outside it.

**D — which logics commit (coordination-logic atlas).** *Computed against expectation.* A k-of-n quorum
mediator binds the parties only at the extremes — unanimity and any-one — and factors at every interior
threshold, where each party is substitutable. Committed construction is not sufficient; only the extreme
quorums make every party individually pivotal. That parity logics bind more readily than monotone ones,
and that rotations are irreducible, are prior IIT results the atlas reproduces.

**B — which mediators commit versus convey (discriminant boundaries).** *Analytic.* The neighbouring
constructs of mediated communication fall on a transmit / transform / commit ladder their own literatures
draw. The Φ verdict reads the convey constructs dyadic and the commit construct triadic, and a
re-encoding of the same channel as committing flips it — which shows the instrument is faithful to the
encoding, not that real channels carry the property.

**F — when the system itself is bound (platform position).** *Analytic, with a known economic image.* A
mediating platform is in the irreducible core when the parties have no substitute *causal path* around
it in the model. Two distinct economic questions sit here and the study (and an earlier draft of this
synthesis) ran them together; they are separated now. *Disintermediation* asks whether the two sides can
bypass the platform entirely and transact directly — the bypassed regime. *Capture* asks which side is
exploited *within* platform competition; in Armstrong's competitive bottleneck the captured side is the
**single-homing** side, which lacks a competing platform-route to a given counterparty, while platforms
compete for it and extract surplus via the captive relationship. The model's "no substitute path"
primitive is the disintermediation axis; it is *not* Armstrong's single-homing primitive, and the two
should not be conflated.

**E — taking the variable to the field (field protocol).** A method for modeling one real coordination
arrangement as a Boolean form and computing the verdict, with a mandatory sensitivity step (because many
models fit one account, and a documented 40% of the mock arrangements flip verdict under a defensible
re-encoding) and an explicit validation gap. Φ is used strictly as a structural-irreducibility statistic,
with no consciousness claim.

**C — how stable the verdict is (robustness, folded into A).** Tested alongside the membership law; the
conditions hold in the construct's natural domain, and the population-dependence is reported there.

## The convergence, at the right altitude

The committed-determination axis is not the lab's discovery. It is the distinction five literatures draw,
and the studies show the Φ verdict *agrees in sign* with them on the models built. The agreement is of
two kinds, and the table marks them: one column has computational coincidence behind it (IIT↔Shapley,
study A), and four are structural correspondences asserted across vocabularies, not derived and not yet
exhibited on shared models in this document.

| The Φ verdict says | bound / triadic | separable / dyadic | image | basis |
|--------------------|-----------------|--------------------|-------|-------|
| **IIT (A, D)** | a unit in the complex | an excluded / reducible unit | exclusion; φ_s = min(φ_c, φ_e) | enforced by the instrument |
| **Cooperative game theory (A)** | a pivotal player | a null / substitutable player | Shapley value; Null Player axiom | *computational coincidence (A), at the null-player corner; trend elsewhere* |
| **Platform economics (F)** | a single-route bottleneck | a bypassable, substitutable route | competitive bottleneck (capture); disintermediation (bypass) | structural correspondence |
| **Bargaining theory (F)** | a party held to a non-binding default | a party with a binding outside option | outside-option principle (a *distinct* result that agrees in sign) | structural correspondence |
| **Communication theory (B)** | a system that commits | a system that transmits or transforms | transmit / transform / commit ladder | structural correspondence |

Two cautions the earlier draft omitted. The bargaining row (Binmore–Shaked–Sutton, surplus division) and
the platform row (Armstrong, multi-sided pricing) are *distinct results that agree in sign on these
models*, not one mechanism. And the binary verdict discards exactly the magnitudes those theorems are
about: the threshold at which an outside option starts to bind, the surplus share it then pins, and the
platform prices. The Φ verdict recovers the *sign* of who is bound, not the theorems.

## What the program adds, and what it recovers

Most of the individual laws are recoveries, established by running the literature on each study.

- **Recovered.** Bidirectional coupling is IIT's own requirement, enforced by the instrument (A).
  Pivotality and substitutability are the Shapley value's (A, D). The platform-position theory is, in its
  economic content, the competitive bottleneck and the outside-option principle (F). The
  commit-versus-convey distinction is the communication literature's own (B). Parity binding more readily
  than monotone logic, and rotation being irreducible, are prior IIT results (D).
- **Genuinely new, and bounded.** Two pieces survived. The graded membership relation — that across a
  population of forms, complex membership rises with causal pivotality, where IIT's per-form membership is
  strictly binary — is the program's one Φ-specific empirical result. It is stated here as a conjectured
  bridge to the Shapley value, *verified only at the null-player corner* and resting on a first-order,
  population-dependent proxy for pivotality, not as a proven correspondence. The extremes-only quorum law
  is new as an explicit IIT-irreducibility result — no surveyed source states it as such — though it
  composes known parity-versus-monotone and threshold-discontinuity pieces.

### Does exact Φ earn its place?

The honest accounting invites the sharpest question: if a one-line "can any party be substituted, routed
around, or left out?" coding reaches the same verdict on these models, what does exact Φ add? The answer
is not that Φ is *necessary* — on the stipulated models a cheap test agrees, and the program does not
claim otherwise. The answer is three affirmative points the recoveries should not bury.

1. **One computation returns five tests.** The five disciplinary checks — the Shapley value, the
   competitive-bottleneck condition, the outside-option principle, the commit/convey coding, IIT
   exclusion — are different procedures. Φ-irreducibility on a Boolean model is one procedure that returns
   the same partition for all of them. That theoretical economy is real, whatever a per-domain heuristic
   could match case by case.
2. **The major complex names who is bound.** A commit/convey label returns a verdict; it does not return
   *which* parties form the irreducible core. The membership law and the platform study both turn on this
   — the platform drops out of the core when bypassable, the worker sheds when a coalition forms — and a
   binary coding produces no such structural output.
3. **The graded law is Φ-specific.** The binary-to-graded membership result exists only because the
   apparatus computes a continuous quantity the cheap test does not.

On these grounds the apparatus is a principled, unified, structure-naming lens — not a necessary one on
small tractable forms, and proposed as the route to forms where the cheap test would have nothing to say.

### Is algorithmacy a distinct construct?

The discriminant study shows the Φ verdict tracks a commit-versus-convey axis the communication
literature already draws, and that algorithmacy is verdict-identical to *directive algorithmic
management* (Kellogg, Valentine & Christin 2020) while differing from the convey constructs. This does
not establish algorithmacy as wholly new. The honest claim is narrower: algorithmacy is a
**formalization of directive algorithmic management generalized to the worker–system–counterpart triad**
— a system that commits a determination neither party controls, stated structurally so it can be computed
and so its irreducible core can be named. The contribution is the formal, generalized, computable
statement of an existing distinction, not a new distinction. No case has been found that is algorithmacy
but not directive algorithmic management; if the construct's marginal value is to be defended, that case
is the work that would do it.

## Limitations

Everything here is in-silico, on small Boolean models of coordination; the verdicts are exact for the
models and are evidence about the models, not measurements of organizations. The title and framing are
bounded accordingly. Φ is read only as the binary verdict and the major complex, with no consciousness
claim — a point the contested status of IIT as a theory of consciousness does not touch. The
cross-disciplinary convergence is shown by coincidence of sign on built models, not derived: the program
demonstrates that the Φ verdict and the established results agree on these models, not that one implies
another, and four of the five correspondences are not yet exhibited on shared models. The verdict cannot
represent the thresholds, surplus shares, and prices the economic theorems are about. Many results rest
on stipulated encodings, and a documented 40% of the field mocks flip under a defensible re-encoding, so
encoding-dependence is a first-order caveat, not a footnote. The validation gap is unclosed: no real
worker, platform, or message has been measured, and a single real case run through the field protocol
could break a model and reveal a specificity gap, but could not — under equifinality — by itself validate
the construct or the axis.

## The six papers

- [`studies/core_membership_law/paper.md`](../studies/core_membership_law/paper.md) — A
- [`studies/coordination_logic_atlas/paper.md`](../studies/coordination_logic_atlas/paper.md) — D
- [`studies/discriminant_boundaries/paper.md`](../studies/discriminant_boundaries/paper.md) — B
- [`field/threads/paper.md`](../field/threads/paper.md) — F
- [`field/paper.md`](../field/paper.md) — E (method) and the ten mock demonstration
- [`PAPER_PIPELINE.md`](../PAPER_PIPELINE.md) — the plan that produced all six

## Revision note (response to the committee)

This version answers the four-member panel (`committed_determination_committee_review.md`), which
returned major revisions.

1. *Convergence overstated.* "The same line" is removed; the table now marks one column as computational
   coincidence and four as structural correspondences not yet exhibited on shared models, matching the
   limitations' altitude.
2. *Economics error (the economist's blocking point).* The competitive-bottleneck mapping is corrected:
   the captured side is the single-homing side lacking a competing platform-route, not "parties with no
   outside option to each other." Disintermediation (bypass) and capture (within-platform exploitation)
   are separated, as are surplus-division (Binmore–Shaked–Sutton) and platform pricing (Armstrong).
3. *Tautology.* "Committed determination" is now defined by construction (wiring and rules),
   independently of the verdict, and the studies are partitioned into analytic (axis built in) and
   computed-against-naive (informative) results.
4. *Bridge and statistic.* The Shapley link is downgraded to a conjecture verified at the null-player
   corner, resting on a first-order, population-dependent proxy; both AUC populations (≈0.89 strict /
   ≈0.63 unconstrained) are named.
5. *Instrument-choice case.* Made directly, with Φ explicitly not claimed necessary; algorithmacy is
   defended as a generalization of directive algorithmic management, not a new construct.
6. *Encoding-dependence and prose.* The 40%-flip fact is raised beside the convergence; the antithesis
   constructions are cut; the redundant closing section is merged into "what the program adds."

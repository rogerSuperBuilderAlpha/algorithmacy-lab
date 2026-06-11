# Critical review: the political-economy and structural-law waves (Q111–Q117)

An adversarial self-review of the value wave (Q111–Q116) and the structural-law opener (Q117), commissioned
to surface every academic-grade objection before an external referee does, and to fix the agenda of questions
the program must answer to defend its validity and rigor.

The review was produced by four independent adversarial readings, each from a distinct lens (IIT methodology;
construct and external validity; cooperative-game and formal method; research process and integrity). Their
load-bearing factual claims were re-verified against the code and the probe ledger. Where a critic overreached,
this document corrects it, so the review holds itself to the standard it demands of the work.

This is a working document, not a verdict on the program. The findings under review are arithmetically sound;
the threats are to what the arithmetic is taken to mean.

## What holds up (so the defense is credible)

A fair referee should grant these, and the defense should lead with them:

- **The computation is exact and deterministic.** Exact IIT-4.0 Φ over full state enumeration, Shapley values
  over the complete ordering set, exhaustive enumeration of the 256-form family in Q117. The numbers reproduce.
- **The global program is not a confirmation monoculture.** The probe ledger records roughly 38 refuted and a
  dozen partial results across 274 probes. The program has been willing to be wrong, and the record shows it.
- **The instrument has validation controls** (`classifier/validate.py`): a decoupled node must read dyadic, a
  fully coupled one triadic. These run before the verdict is trusted.
- **The caveat blocks are candid on the threats they name** (in-silico scope, single coupling, three sizes,
  the φ_d-variant sensitivity in Q116). Q117's confusion table and its "discovered, not derived" admission are
  honest.

The objections below do not deny these. They locate where the program's claims outrun them.

## Tier 1 — Foundational threats (a referee could reject on any one)

### T1. The construct's behavioral validation is contradicted by the program's own ledger

`classifier.py:22` states the instrument is "validated behaviourally at the binary contrast." The ledger says
otherwise. Every independent behavioral check failed or was weak: Probe 98 (independent Q-learners) **refuted**,
rank-AUC 0.567; Probe 107 (theory-of-mind agents) **refuted**, 0.541; Probe 108 (resilience) **partial/weak**,
0.618. The one check recorded as supporting the construct, Probe 18, carries the ledger's own note
"**circularity explicit**: both Φ and the proxy derive from the determination, so this is structural
consistency, not independent validation." So the only passing behavioral test is self-declared circular, and
every genuinely independent one was refuted. The economic superstructure (Q111–Q116) sits entirely on top of a
verdict whose external criterion is, by the program's own record, unestablished.

**Severity: fatal to the external reading.** Verified against `probes/PROBES.md` entries 18, 98, 107, 108.

### T2. The bridge from Φ to economic value is asserted, never argued

Q111/Q114/Q115 define the coalition value as the subsystem's integrated information, then read the Shapley
shares as "value capture," "rent," "scarcity," and "who can extract surplus." Economic value is
willingness-to-pay, opportunity cost, surplus over outside options — a quantity of preferences and prices. Φ is
causal irreducibility in bits. No theorem or argument in the corpus shows Φ is monotone in, let alone equal to,
economic value. The Shapley machinery is valid for any set function, so the numbers exist; the welfare
vocabulary laid over them is not licensed by anything shown.

**Severity: fatal to the economic claims** (the arithmetic survives as "the Shapley decomposition of Φ").

### T3. Subsystem-Φ is not a valid characteristic function for the cooperative-game reading

The welfare reading presupposes the value function is superadditive (coalitions create value) and ideally
monotone (a party never subtracts). Φ is neither in general: adding a node can lower Φ by opening a cheaper MIP
cut, and integration is by definition non-additive across a partition. The code anticipates this with a
`max(0, φ)` clamp and an `except: φ=0` fallback (`q111/forms.py:55–58`). The reported negative Shapley values
(the −0.833 "monitor-only principal" in Q114) are then the Shapley apportionment of a value-destruction event:
adding the read-only party drops whole-system Φ to zero. A "fair value" that goes negative because the value
function is non-monotone is a property of the functional, not a finding about ownership.

**Severity: fatal to the "value distribution" framing; serious for the specific Q114 headline.** The clamp is
applied to coalition values but the resulting Shapley value is left unclamped, a mixed convention that
manufactures the negative number.

### T4. Internal contradiction: the magnitude is disowned, then used cardinally

`classifier.py:22–24` is explicit that Φ magnitude "depends on the encoding and is not a reliable scale (the
dissertation withdrew that claim) … read the magnitude as at most an ordinal hint." Yet Shapley values are
cardinal, and Q114 ("Φ grows from 2 to 3"), Q115 ("Φ = 2N", "1.0 → 1.55 → 2.067"), and Q116 (cardinal gaps,
"0.217") all trade in magnitudes. The program uses as a cardinal scale exactly what it elsewhere declares
unreliable.

**Severity: fatal as an internal inconsistency.** Either defend Φ as cardinal (against the encoding-dependence
the dissertation conceded), or downgrade Q114–Q116 to ordinal claims, which removes "grows 2→3" and "Φ=2N".

## Tier 2 — Serious threats to inference

### T5. The verdict rests on one hand-picked state, and the coalition value on a frozen background

The verdict is `max` Φ_MIP over reachable states (`classifier.py`), so it is a property of one state, not of
the form: the read-recipient triad has Φ=2.0 only at the all-ones state and Φ=0 in its other three reachable
states. The Shapley games hardcode the all-ones state and freeze the excluded parties at 1
(`pyphi.Subsystem(net, state, nodes=S)` conditions, not marginalizes, the complement). So v(S) is the Φ of S
in a world where everyone else is pinned ON, an arbitrary background that changes the game. The "laws" are read
off a single state with a single background, neither shown to be the principled choice nor shown to be robust.

**Severity: serious.** Note: for the symmetric AND-mediated forms actually used, all-ones is plausibly the
argmax state, so v(N) likely equals the verdict Φ on these panels — making this a latent threat to be *shown*
absent, rather than a demonstrated numerical error.

### T6. "Exact IIT-4.0 Φ" is one config of an unpinned, mutable build

`requirements.txt` pins PyPhi to the moving branch `git+…@feature/iit-4.0` with no commit hash, an unreleased
implementation of a contested formalism. The verdict depends on config (`SYSTEM_CUTS`, `SYSTEM_PARTITION_TYPE`,
`REPERTOIRE_DISTANCE`) that no FINDINGS reports. "Exact" describes the arithmetic, not the reproducibility:
another checkout of the same branch, or a different config cell, is not shown to give the same verdict.

**Severity: serious.** Verified: the pin is the moving branch.

### T7. The pre-registration apparatus does not separate prediction from knowledge

The "two-commit audit" commits `hypotheses.md` before `results.csv`. But the pre-registration commit also ships
the complete runnable probe and `forms.py`, which compute and print the verdict — so the answer is mechanically
available the instant the hypotheses are committed, by the same author, same session, no external seal. Worse,
the exploratory values were computed before the hypotheses were fixed (the N=2/3/4 sweep in Q115; the
predicate "found by inspecting the family" in Q117), so directional hypotheses like "1.00 < 1.55 < 2.07" were
written after the numbers were known. And the Stage-1 `review.md`, defined as the gating first stage, is first
committed in the *results* commit, after the work. The registration provides little of its error-control value.

**Severity: serious.** Verified against the commit contents and the session record.

### T8. Near-100% confirmation in these waves indicates non-severe testing

Q111–Q117 are 24-of-24 hypotheses confirmed. Several carry little risk by construction: Q115 H1 ("Σ Shapley =
Φ") is the Shapley efficiency theorem, true for any value function; the E=R and equal-agent values are forced
by the symmetry axiom; Q116 H1's "coincide on the triad" is largely pinned by the triad's symmetry plus
normalization. A hypothesis earns support by surviving a test it could have failed. The genuinely severe tests
the program ran are the behavioral ones (T1), and those were refuted. Constructed tests pass uniformly;
independent tests fail.

**Severity: serious.** The "all four confirmed" banner overstates the evidential weight.

### T9. Q117's predicate is fit and scored on the same 256 points, one topology

The Φ-free predicate was, by its own admission, "discovered, not derived" by inspecting the 256-form family,
then scored on that same family with no held-out set. The family is a single fixed wiring (8 truth-table bits),
a measure-zero corner of n=3 function space, and the decision actually concerns only the 40 full-cycle forms
(the other 216 are forced dyadic by the cycle screen). A small Boolean rule nailing 40/40 in-sample is the
expected outcome of fitting, not evidence of a law. The headline leap to "integration is a property of the
mechanisms, not the wiring" is one oracle slice, refit. "Necessary and sufficient" is true only over this
family.

**Severity: serious for the generality claim; the in-family result is sound as description.** The remedy is the
already-planned Q118 (out-of-sample topology) and, ideally, a derivation from the axioms.

### T10. "Recovers the economic law of scarcity" is close to entailed by the family's construction

Q115's market is built so the two outer parties are unique and the N agents are interchangeable by
construction. The Shapley symmetry axiom then forces the interchangeable agents to equal shares and leaves only
the unique positions to absorb the N-scaling surplus. "Scale pays the scarce" follows from the symmetry of the
family plus the axioms; it could not have come out otherwise. Calling a guaranteed algebraic identity a
recovered economic law overstates it.

**Severity: serious for the discovery framing.** The rebuttal is to exhibit the pattern in a family where
scarcity is not a design symmetry (randomly wired markets).

## Tier 3 — Threats to presentation and independence

### T11. Measure-shopping in Q116
The "structural depth" is the singleton φ_d, chosen from several candidates; the caveat concedes other weights
(total participated φ_d, relations φ_r) "order the parties differently." The rank agreement is the one measure
that agrees. **Severity: serious for H2's generality.** Pre-specify the measure; show robustness.

### T12. CI "reproduction" verifies determinism, not correctness
`ci/reproduce.json` checks that re-running a probe re-prints "VERDICT: CONFIRMED". The probe computes the
verdict from the same code. CI certifies the code is deterministic, not that the conclusion is right or that the
form models anything. **Severity: minor, but the "reproduces the numbers" language overstates it.**

### T13. Reification and hedge-stripping
The prose treats partition artifacts as organizational entities ("the productive position," "structural depth",
"the rent accrues to the productive position") and states n=1 Boolean results as general laws ("the principal
creates value", "the law of scarcity is structural before it is economic"). The house style's confident
register, applied to results this narrow, launders scope-limited arithmetic into law-like prose. **Severity:
serious for the abstract/headline claims; the bodies are more careful.**

### T14. Single-agent self-review wearing six hats
The Stage-1 review, hypotheses, code, results, findings, and paper are produced by one agent in one session. The
"gates" are self-administered; the "review" is self-review. **Severity: serious for the independence the
six-stage framing implies.**

## Corrections to the critique (holding this review to its own standard)

- **The referenced validation files are private, not missing.** A critic flagged
  `dissertation/paper2_construct/party_partition.py` as absent. It is gitignored (the dissertation is a private
  nested repo), so it exists but is publicly uninspectable. This is a reproducibility limitation of the public
  artifact, not a fabricated citation. The defense should make the public-facing demonstration self-contained.
- **The "efficiency = Φ" residuals are a legitimate check, mislabeled.** Σ Shapley = Φ to 0.001–0.002 confirms
  the code is correct; it is a sanity check, not a hypothesis. Reclassify rather than count it as a confirmation.
- **T5 is latent, not demonstrated, on these forms.** For the symmetric forms used, the all-ones state is
  plausibly the maximal-Φ state, so the background/state choice may not change these particular numbers. The
  burden is to show that, not to assume it.

## The defense agenda: questions we must answer

Ordered by leverage. The first three decide whether the program's claims stand; the rest harden it.

1. **External criterion (T1).** Can we produce one non-circular behavioral or empirical criterion on which
   triadic forms are reliably distinct at AUC well above 0.5? The program tried three agent models and failed.
   Until this is answered, should the classifier docstring's "validated behaviourally" be retracted, and the
   economic claims be labeled conditional on it?
2. **Φ-to-value bridge (T2, T3).** Can we derive or calibrate a relationship between subsystem-Φ and any actual
   economic value, and certify that v(S) is monotone and superadditive on the forms used? If not, will we
   restate Q111–Q116 as "the Shapley decomposition of integrated information," dropping the rent/scarcity/value
   vocabulary?
3. **Cardinal-versus-ordinal (T4).** Do we defend Φ magnitude as a cardinal scale, or do we downgrade every
   magnitude claim (Φ 2→3, Φ=2N, the 0.217 gap) to ordinal? The classifier docstring currently forbids the
   cardinal use the findings make. Which way do we resolve the contradiction?
4. **Robustness of the game (T5).** Do the Shapley vectors and the verdict survive (a) alternative background
   states for the frozen complement, (b) marginalizing rather than freezing it, and (c) aggregation rules over
   states other than the max? Show invariance or report the dependence.
5. **Reproducibility of "exact" (T6).** Will we pin the PyPhi commit, dump `pyphi.config` into every FINDINGS,
   and show the binary verdict is invariant across the plausible IIT-4.0 config cells and a version bump?
6. **Pre-registration integrity (T7).** Will we register a hash of the hypotheses to an external timestamp
   before any code exists, separate the answer-computing probe from the pre-registration commit, and commit the
   Stage-1 review in its own commit before the hypotheses? Can we show, by history, that predictions preceded
   knowledge of the result?
7. **Severity and the file drawer (T8).** Will we report the per-wave confirmation rate (and flag the value
   wave's 100% as a concern, not a strength), label the by-construction hypotheses as identities, and
   pre-register at least one prediction we expect to fail?
8. **Out-of-sample generality (T9, T10).** Will Q118 validate the Φ-free predicate on a different topology and a
   random n=3 sample with a held-out set, and will Q115's scarcity result be reproduced in a family where
   scarcity is not a design symmetry? Can the predicate be derived from the IIT axioms rather than fit?
9. **Measure pre-specification (T11).** Will Q116's structural measure be pre-specified and its rank result
   shown robust across singleton φ_d, total participated φ_d, and relation-inclusive shares?
10. **Honest scope and independence (T12–T14).** Will we state that CI checks determinism only, add an
    independent re-implementation of one key result, route hypothesis-vetting and a results audit through a
    separate agent that does not see the answer key, and add the process threats above to every Limitations
    section?

## Bottom line

The arithmetic is sound and one study (Q117) is genuinely rigorous within its family. The exposure is at the
joints: the construct's external validity is, by the program's own ledger, unestablished (T1); the economic
vocabulary is unbridged to the formalism (T2–T4); and the confirmatory apparatus around these specific waves
took on little risk (T7, T8). The single most efficient move, the one that saves or sinks the most, is T1:
produce one non-circular external criterion. Everything economic is built on the gap it leaves.

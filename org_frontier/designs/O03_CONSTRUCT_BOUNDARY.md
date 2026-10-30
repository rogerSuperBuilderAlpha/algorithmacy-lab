# O03 — separating algorithmacy from directive algorithmic management

O03 remains open. The existing models support a formal account of binding coordination, but they do
not establish an arrangement that qualifies as algorithmacy while falling outside directive algorithmic
management. The cognition and construct writing offer a second claim: algorithmacy names a person's
capacity to coordinate with a counterpart through such an arrangement. These claims need separate tests.

This note records a source review and a proposed test. It reports no new computation or field evidence.
Source line numbers below refer to the files reviewed on 2026-10-30.

## The strongest case for distinctness

A person can navigate a system's rules and still misunderstand the person on the other side. The
[cognition account](../cognition/coordinating_through_the_opaque_third.md), lines 55–61, describes the
capacity to infer that person's intentions, express meaning through the intermediary, and adjust as
its rules change. The [Rahman hearing](../../submissions/lima_pdw/literature/steelmans/rahman2021.md),
lines 84–106, sharpens the distinction: understanding an opaque evaluation does not establish successful
coordination with the client whose judgment helped produce it. The hearing also names dependence and
prior setbacks as rival explanations for differences among workers.

The [October 9 construct revision](../../submissions/algorithmacy_ot/manuscript/REVISION_2026-10-09.md),
lines 61–67, extends the claim beyond software and proposes blind review with a hidden scoring scheme
as another setting that could require the ability. A human-run review process could therefore separate
algorithmacy from directive *algorithmic* management. This is a candidate, not a documented counterexample:
the review would still need a counterpart, interdependent work, binding consequences, and evidence for
the rule's hidden, unanswerable, changing character.

The same revision leaves a scope question unresolved. Its definition requires the intermediary to bind
both people, but it includes cases that bind only one side (lines 63–67 and 115–123). It asks whether
these are one form or two (line 145). A test must state which version it tests before selecting cases.

## The strongest objection

The [committee review](../essays/committed_determination_committee_review.md), lines 52–58, identifies
the lack of a discriminating case. The revised [synthesis](../essays/committed_determination_synthesis.md),
lines 147–158, accepts a narrower claim: algorithmacy formalizes directive management and generalizes it
to the worker–system–counterpart triad. It reports no case outside directive management.

The battery cannot resolve this objection by relabeling a model. In
[discriminant.py](../studies/discriminant_boundaries/discriminant.py), lines 60–87, both directive
management and the channel that starts committing use `W'=S, S'=W AND C, C'=S`. Their identical verdict
follows from identical rules. The cognition experiment uses the same actor model in
[five_theories.py](../cognition/five_theories.py), lines 38–44. These computations describe the models;
they supply no independent evidence that people possess a separate capacity.

The rival capacity also extends beyond technical knowledge. The
[Zhou instrument audit](../../submissions/lima_pdw/literature/ZHOU_2025_INSTRUMENT.md), lines 79–84,
rejects that dismissal: the scale includes strategic use, repair, and attitude. The
[Zhou hearing](../../submissions/lima_pdw/literature/steelmans/zhou2025apjhr.md), lines 91–98, proposes
that someone could score highly while failing to coordinate with a counterpart. Researchers have yet
to demonstrate that separation in this program.

## The measurable distinction: accepted, understood, acted on

Gate acceptance and counterpart understanding are separate outcomes. Researchers can count how often
an interaction lands in each cell, using the sender's recorded intent and the receiver's interpretation:

```text
                                  COUNTERPART UNDERSTANDS
                                    Yes             No
                              +----------------+----------------+
GATE ACCEPTS            Yes   | Accepted and   | Accepted,      |
                              | understood     | meaning lost   |
                              +----------------+----------------+
                        No    | Understood,    | Blocked and    |
                              | but blocked    | misunderstood  |
                              +----------------+----------------+
```

The top-left cell records two achievements, not successful coordination by itself. A counterpart may
understand and refuse, disagree, or lack the means to act. Record the counterpart's subsequent action
and whether it advances the shared task as a third outcome. A successful intervention should improve
understanding and useful action without buying acceptance through misleading content.

These distinctions suggest the following scoring rules. Researchers must fix the task-specific rules
before collecting data:

| Outcome | Observable measure | Avoid this shortcut |
| --- | --- | --- |
| Acceptance | Gate's recorded decision under its actual rule | Treating acceptance as proof of understanding |
| Understanding | Receiver selects the sender's intended action and constraints from plausible alternatives | Asking only whether the message seemed clear |
| Attribution | Participant assigns probabilities to rule change, counterpart change, both, or neither | Requiring certainty when the available evidence is ambiguous |
| Coordinated action | Receiver chooses an action that meets the sender's recorded constraints and the shared task | Counting agreement or compliance as sufficient |

Researchers should collect the intended action and constraints before the message, then ask the
receiver to interpret the message before revealing that record. Use scenarios in which the receiver
could understand the message if it reached them intact. Fix the gate decision before the receiver's
interpretation so that comprehension does not determine acceptance by construction.

A blocked message creates a measurement problem: in a real gate the counterpart may never see it.
In the experiment, a separate receiver can interpret that message without the gate's result or any
ability to affect the task. This supplies the bottom row's comprehension measure. Keep that diagnostic
read separate from delivery and actual action. In a field study without such a read, mark understanding
of an undelivered message as unobserved; do not fill the bottom row with guesses.

## A discriminating task: the right repair after a bad result

Give pairs a shared scheduling task. The sender must communicate a requested change and a constraint,
such as moving a handoff while retaining an overlap period. The counterpart's private availability and
the gate's acceptance rule can each change between rounds. An accepted request can still lose the
overlap constraint, leaving the counterpart to choose an unsuitable time. This is an invented task,
not a finding about scheduling systems.

Researchers should vary the cause of an adverse result across repeated episodes:

| Actual cause | Candidate repair to score |
| --- | --- |
| Counterpart's needs change; gate rule stays fixed | Adjust the proposed arrangement to the counterpart |
| Gate rule changes; counterpart's needs stay fixed | Change the expression while preserving the intended arrangement |
| Both change | Adjust the arrangement and its expression |
| Neither changes; the result reflects noise | Avoid an unsupported revision or seek more evidence |

The same rejection should not reveal its cause through wording or timing. Give participants a limited,
equal budget for probes, such as resubmitting an equivalent message or asking a permitted clarification.
Provide some evidence that distinguishes the causes. If the histories available to a participant are
identical under two causes, researchers cannot score the participant's failure to distinguish them as a
lack of skill. Score calibrated uncertainty and informative probing in those trials. This separates
inference from guessing and environmental limits from personal capacity.

The task tests the [October 9 revision](../../submissions/algorithmacy_ot/manuscript/REVISION_2026-10-09.md),
lines 85–87 and 105: attributing a result matters because different causes call for different repairs.
Researchers should score the repair as well as the diagnosis, using the understanding and action
measures above. Predefine the correct repairs and acceptable alternatives for each scenario.

## The hard rival: existing skills working together

The strongest rival account combines communication skill with skill at navigating systems. A comparison
against algorithmic competency alone would give that rival too little credit. Measure both skills on
separate tasks before the joint task, alongside the adapted Zhou scale. Compare predictions from those
skills, their interaction, and task experience against predictions that also include the algorithmacy
measure. Record dependence and prior setbacks, as the Rahman hearing requires.

Researchers should evaluate added prediction on held-out scenarios, with splits that prevent the same
participant's closely related trials from leaking into training and evaluation. A new factor or a
better fit on the same observations cannot establish added value. Even better prediction could reflect
extra task-specific practice, so a training comparison should use equal time and feedback: system
navigation, communication, their combination, and joint diagnosis of counterpart and rule. A benefit
beyond the combined course would support the proposed account; it would not prove that people possess
an indivisible new mental faculty.

Vary the arrangement as well as the person. Use a binding opaque gate as the focal condition, a binding
gate with its rule disclosed as one control, and a conveying system without veto power as another.
Keep the counterpart task and input limits comparable. Assess whether the added predictive or training
benefit is larger under opaque binding than under those controls. A general benefit across conditions
would favor broad communication or problem-solving skill over the proposed scope claim. Disclosure may
also help system navigation, so improvement after disclosure alone cannot discriminate the accounts.

This proposal tests part of the account. A fixed rule tests diagnosis under opacity; unannounced rule
changes are needed for tracking. If only the sender bears binding consequences, label the task a test
of the one-sided extension. The strict two-sided claim requires consequences for both parties that they
cannot remove by agreement. Researchers need to fix the version under test, task details, scoring,
sample size, exclusions, and minimum useful effect before collecting data. This note is not a completed
pre-registration.

## What evidence would change the conclusion

| Result | Supported conclusion | Remaining limit |
| --- | --- | --- |
| Algorithmacy predicts understanding and useful action beyond combined rival skills on held-out tasks, with the predicted scope pattern | A capacity with added explanatory value in these tasks | Does not establish an arrangement outside directive management |
| Combined rival skills explain performance; a precise interval excludes the predefined useful added effect | Existing skills suffice within the tested scope | Does not prove equivalence in every setting |
| Performance rises only on gate acceptance | Better system navigation | No demonstrated gain in counterpart coordination |
| Participants lack evidence to distinguish causes | The arrangement withholds needed information | Does not show low algorithmacy |
| A qualifying human-run case meets the chosen definition and excludes directive algorithmic management under independent coding | A counterexample to arrangement equivalence under those definitions | Does not validate the capacity or its measure |
| A small study yields a wide interval around no added effect | The result is unresolved | Neither distinctness nor equivalence established |

Blind review is a candidate for the last arrangement test, not an answer already present in the repo.
Specify who the counterpart is, what each person must do, and what binds each one. A lone applicant
facing a reviewer who acts as the gatekeeper may lack a distinct counterpart; a human-run procedure may
still count as algorithmic if its operator follows an algorithm. Independent coders need definitions
of algorithmacy and directive management fixed before inspecting the candidate. Under the battery's
broad use of directive management for committing systems, the proposed counterexample may disappear.
That would expose a definitional overlap, not a failed human performance test.

For a Boolean representation of any case, ground each rule in evidence and report alternative
encodings. The [field protocol](../field/PROTOCOL.md), lines 43–76, specifies rule evidence, controls,
major-complex membership, and sensitivity checks. Exact Φ establishes irreducibility for the stated
model. The acceptance and understanding measures concern behavior. Neither result supplies the other's
validation (protocol, lines 8–21 and 83–91). A positive model verdict alone cannot establish a binding
social determination: the [atlas](../studies/coordination_logic_atlas/FINDINGS.md), lines 75–85, also
reports an irreducible pure copy-cycle with no joint determination.

The registered survey already includes a comparison with adapted Zhou competency:
[analysis plan](../survey/cohort_algorithmacy/analysis_plan.md), lines 57–68. Its small cohort limits
between-person inference (lines 6–12). Its [baseline items](../survey/cohort_algorithmacy/instruments/wave1_baseline.md),
lines 11–23, mostly ask about acceptance, system rules, and admissible inputs; they do not directly test
separating the counterpart's intentions from the system's rule. A successful factor comparison would
therefore support measurement distinctness without settling the proposed performance distinction.

The registered survey remains unchanged. The [pre-registration](../survey/cohort_algorithmacy/PRE_REGISTRATION.md),
lines 3–5, requires a dated amendment for changes after registration; this note is a separate proposal.
O03 stays open until evidence resolves the arrangement claim, with the capacity claim reported separately.

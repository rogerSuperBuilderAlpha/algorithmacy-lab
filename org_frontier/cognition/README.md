# Cognition — the formal bridge to the cognitive theories of coordination

A coordination through an opaque, interested third party is something the standard theories of mind
cannot represent. Each assumes two parties and a medium between them, and the medium here is a third
party with objectives of its own, which a two-party theory has nowhere to put. Hunt's
[paper](coordinating_through_the_opaque_third.md) makes this case across five accounts of cognition and
names the competence their failures point to algorithmacy. This arm is the formal counterpart. The
lab's exact-Φ apparatus can hold the third party, as a member of the irreducible core, and each of the
five failure points is a claim about structure with a computable Φ prediction.

## Why the apparatus can hold the third party

The theories fail because they model a channel: a sender, a receiver, and a pipe indifferent to what
it carries. Integrated information makes no such assumption. A coordination is a system of parties whose
states determine one another, and Φ measures whether that system is irreducible across the partition
that separates them. When the third party only carries a signal, the arrangement factors and Φ is zero,
which is the channel the theories assume. When the third party reads the parties and commits a
determination of its own, the arrangement does not factor, Φ is positive, and the major complex names
the third party as a member of the bound whole. The thing the theories have nowhere to put is exactly
what the major complex holds.

## The five experiments

[`five_theories.py`](five_theories.py) runs one experiment per theory, each formalizing a structural
claim from the paper. The results and their reading are in [`FINDINGS.md`](FINDINGS.md), and each theory
is taken several experiments deeper in [`theory_batteries.py`](theory_batteries.py) and
[`THEORIES.md`](THEORIES.md).

- **Computationalism** casts the algorithm as a channel that carries symbols. The channel is the
  zero-Φ special case; a system that reads its own objective adds an irreducible contribution the
  channel model omits.
- **Direct perception** has the affordance lawfully present in the light. The rule the worker needs is
  not recoverable from the outcomes she can see, so the affordance is taken out of the light and she
  must infer the determination.
- **Embodiment** carries meaning in the body and the shared room. The worker's intent compresses into
  the system's narrow input, and the binding sheds quickly as the fidelity of that read drops.
- **Theory of mind** equips the worker to address a counterpart. She binds to the held position while
  the real counterpart, read by the system as a referent, sits outside the bound whole.
- **The extended mind** treats the platform as a part of the worker's cognition. As the platform's
  interest supplants her input to the system, she is displaced from the irreducible core at a low
  threshold, and the coordination runs on without her.

## Beyond the paper, and toward the survey

The paper engages five theories; the arm adds a sixth it did not, predictive processing, in
[`predictive_processing.py`](predictive_processing.py) and
[`PREDICTIVE_PROCESSING.md`](PREDICTIVE_PROCESSING.md): the worker as a generative model of a process she
cannot fully invert and that retrains underneath her, with an opacity floor of half a bit she cannot
predict away and a binding that thins as the rule drifts. The three failure points that map to the survey
arm's three-facet scale — counterpart inference, signal compression, rule-change tracking — are drawn
together in [`survey_bridge.md`](survey_bridge.md), which turns the formal results into moderation
predictions a study of real workers could test.

## The handoff packet

[`packets/template/`](packets/template/) packages the mapping method for handoff, so a cognitive scientist
can take a seventh theory through the same apparatus. It holds a front-door README, a mapping template, and
[`map_theory.py`](packets/template/map_theory.py), a runnable scaffold that runs the channel and committing
models through the probe and reads whether the third party is held. The six worked mappings are the
instances; the packet is the template a new one starts from.

## What is formal and what is not

The arm formalizes the structural skeleton of the paper's account, where it has one. It leaves aside
the phenomenal content, the felt phantom and the particular way the work wears a person down, which is
the paper's domain and stays there. The apparatus says when a third party is a constitutive member of a
coordination, how much of the worker's intent its input can carry, and when the worker is bound into the
whole or displaced from it. It does not say what any of that is like to live. The contribution is a
representation that can hold an interested third party as a member, which the standard theories cannot,
and a set of computable predictions the phenomenological account can be read against.

The arm draws on the four deep dives under [`../threads/`](../threads/): the co-monotonicity law (when a
mediator commits), the margin to the dyad (how strongly), the behavioral discriminant (why the rule is
not perceivable from outcomes), and core membership (who is in the bound whole). It is the cognitive
reading of the same formal results.

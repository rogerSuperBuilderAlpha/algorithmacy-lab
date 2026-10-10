# Who decides an insurance claim? An exact-Φ reading of claimant, engine, and adjuster

code + data: `org_frontier/questions/q219_insurance_claim_adjudication/`; probes #458–#461 in
`org_frontier/probes/PROBES.md`

## Abstract

Insurers route claims through an auto-adjudication engine and a human adjuster, and the claimant waits on
both. This study models three routing designs as three-node Boolean systems and reads each with exact
IIT-4.0 integrated information over the minimum-information partition, asking which design makes the
claim decision one irreducible three-party determination. Five hypotheses were fixed before computation.
A pass-through pipe, in which the engine only forwards the claim, is triadic in every state (Φ_MIP = 2.0,
core {claimant, engine, adjuster}), replicating the lab's three-node rotating ring. Threshold
auto-approval, a fraud-flag loop with override learning, and the same loop without learning are each
triadic as wholes, but in each the major complex shrinks to a pair: claimant and engine, engine and
adjuster, and claimant and adjuster. Three hypotheses that predicted a full three-party core were
therefore refuted. Freezing the claimant makes the loop factor (Φ_MIP = 0), as predicted. Where the gate
sits decides which pair holds the claim.

## Introduction

Automated claims handling splits one decision among three parties. A claimant files; an engine scores,
approves, or flags; an adjuster reviews what reaches the desk. Eling, Nuessle, and Staubli (2021) place
claims management among the insurance functions most changed by artificial intelligence
[eling2021impact], and fraud screening sends a share of claims to people [derrig2002insurance;
viaene2004insurance]. The design question insurers argue about is cost and error. A prior question is
structural: in a given routing design, does the decision bind all three parties, or does it factor into a
pair with a third party standing by?

The lab answers that structural question with exact integrated information [albantakis2023iit4;
mayner2018pyphi]. A coordination form is dyadic when Φ over the minimum-information partition is zero and
triadic when it is positive, and its major complex names the parties in its most irreducible core. Study
#39 (`studies/hitl_rubber_stamp/`) used this instrument to show that a human in an AI loop belongs to the
core only when the human both shapes the commit and reads it. This study carries that reading into three
named claims designs.

## Related work

Human-automation research grades how far automation reaches into a decision [parasuraman2000types] and
documents the drift of human reviewers toward or away from an automated aid [parasuraman1997humans;
skitka1999automation; mosier1998automation; goddard2012automation; dietvorst2015algorithm], a drift
that Lee and See (2004) frame as a problem of calibrated trust [lee2004trust]. Bainbridge (1983) showed
that automating routine cases leaves people the hardest ones [bainbridge1983ironies]. Policy scholars
doubt that mandated human oversight corrects automated decisions [green2022flaws] and ask whether the
human is in control or only liable [wagner2019liable], a moral crumple zone [elish2019moral], or the
carrier of individual justice that rules at scale cannot supply [binns2020human]. Organization scholars
treat algorithms as a terrain of control [kellogg2020algorithms] and coordination as the management of
dependencies [malone1994interdisciplinary]. Fraud-detection research describes the scoring that routes
claims to people [ngai2011application]. None of these computes whether a claims arrangement is
structurally irreducible. Inside the lab, #39, probe #76 (oversight joins only when it both vetoes and
responds), probe #21 (contestability drops the bound party), q63 (liveness), and Q11 (the rotating ring,
triadic at Φ = 2.0) bear directly on the forms here.

## Hypotheses

Fixed in `hypotheses.md` (commit `a8abd0fa`) before any q219 form was computed. H1: the pipe is triadic
with all three in the core, as Q11's identical rotating ring is. H2: threshold auto-approval is triadic
with all three in the core, and its irreducibility lives only in flagged states. H3: the fraud-flag loop
with override learning is triadic with all three in the core; its null names a contraction to an
engine–adjuster pair. H4: the loop stays triadic with a full core when the learning edge is removed. H5:
freezing the claimant makes the loop dyadic.

## Methods

Nodes are claimant (C), engine (E), and adjuster (A), updated synchronously. The forms are `pipe`
(C'=A, E'=C, A'=E), `gated` (C'=E∧¬A, E'=C, A'=E∧C), `loop` (C'=A, E'=C∧A, A'=E∧C), `loop_nolearn`
(E'=C, otherwise as `loop`), and `loop_frozen_claimant` (C'=C, otherwise as `loop`). Bit meanings are in
`methods.md`. Each probe first asserts that `chat_dyad` reads dyadic and `ats_triad_mediator` reads
triadic at Φ = 2.0. The whole-system verdict, maximum Φ_MIP, MIP, and per-state Φ come from `verdict()`;
the core comes from `major_complex()`, maximized over reachable states. A form counts as triadic for
H1–H4 only if the whole is triadic and all three labels are in the major complex.

## Results

**H1, confirmed.** `pipe` is triadic with max Φ_MIP = 2.000, MIP into three parts, and core {C, E, A} at
2.000. Every one of the eight states reads Φ = 2.000. The result replicates Q11's `rot_ring(3)`.

**H2, refuted.** `gated` is triadic as a whole, but only at state 111, with Φ_MIP = 0.415 (1 of 5
reachable states) and MIP {C, EA}. Its major complex is {C, E} at 2.000, with the adjuster outside, so
the full-core clause fails. The flagged-only clause held: both reachable unflagged states (000, 100) read
Φ = 0.

**H3, refuted.** `loop` is triadic as a whole with max Φ_MIP = 1.000 (state 111; state 110 reads 0.415;
2 of 5 states). Its major complex is {E, A} at 2.000, the engine–adjuster pair that H3's null named.

**H4, refuted.** `loop_nolearn` is triadic as a whole with max Φ_MIP = 2.000 (state 111; 110 reads 0.415;
2 of 6 states), but its major complex is {C, A} at 2.000 and the engine is outside.

**H5, confirmed.** `loop_frozen_claimant` is dyadic, with Φ_MIP = 0 in all five reachable states. The
engine–adjuster pair survives as a sub-complex at 2.000.

## Discussion

The five results answer the title question by design. The pipe, the design with no gate at all, binds
claimant, engine, and adjuster into one loop of equal standing, and it does so through closure alone,
since no node in it reads two parties. Each gate added to that loop keeps the whole irreducible but
hands the strongest core to a pair. Under threshold auto-approval the claimant and engine hold the claim
and the adjuster sits outside the core: an adjuster who sees only flagged claims is, structurally, the
rubber stamp that study #39 described. Under the fraud-flag loop the engine and adjuster close into a
private pair and the claimant drops out, matching the {H, S} override dyad of #39 and the contestability
result of probe #21. Removing the engine's learning does not return the claimant to a three-party core;
it trades the engine out instead, leaving claimant and adjuster. The liveness result from q63 carries
over intact: a claimant who cannot see the decision is outside the coordination that makes it.

The refutations are the study's main content. The hypotheses applied the conjunctive law and the
commit-and-read rule and expected full three-party cores. Those rules predicted whole-system
irreducibility correctly in every gated form, but they did not predict that a two-party subset would
carry more integration than the whole and take the major complex.

## Limitations

The forms are three-node deterministic Boolean models with one stylized encoding each; other encodings of
auto-approval or override learning may read differently. Two of the gated forms reach only five of eight
states, and their irreducibility sits in one or two of them. Φ magnitude is ordinal in this program. The
results are evidence about the models. External validity to any insurer, claimant, or adjuster is a
separate claim this study does not make, and the literature scan informs the framing without testing it.

## References

Every in-text key resolves to `literature/references.bib` (20 entries, each DOI verified against Crossref
and doi.org on 2026-10-09).

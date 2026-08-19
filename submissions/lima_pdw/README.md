# Lima PDW — algorithmacy as a communication competency

A submission arm for the **OS & OT Paper Development Workshop in Organization Studies for Advanced
PhD Students and Early Career Scholars**, Universidad de Piura (UDEP), Lima, Peru, **5–7 October
2026**. The abstract was accepted 2026-08-13 as **LIMA2026-002**; the live deliverable is the full
manuscript due **10 September 2026**.

The accepted title:

> Algorithmacy: A communication competency construct for triadic mediated coordination, with
> empirical evidence from a Caribbean AI engineering cohort

**The live draft is [`manuscript/PAPER.md`](manuscript/PAPER.md)** (2026-08-19). Its abstract and
introduction are locked at [`manuscript/INTRODUCTION.md`](manuscript/INTRODUCTION.md). Do not edit
those two blocks unless the author says to. Details: [`manuscript/LOCK.md`](manuscript/LOCK.md).

**The previous draft is archived** at [`archive/2026-08-19_PAPER.md`](archive/2026-08-19_PAPER.md) —
"The Competency a Form Demands: Algorithmacy and the Co-optation Column," twelve sections, the
seventh-question anatomy. Do not write from it. The same text still sits in
`dissertation/current/paper2/PAPER.md`; that file is no longer the live Lima draft. Do not splice
the new opening back into the dissertation copy unless the author asks.

The submitted package — motivation letter and extended abstract — is transcribed verbatim in
[`ABSTRACT.md`](ABSTRACT.md), and the manuscript has since moved past it in four disclosed ways; see
[`DEPARTURES.md`](DEPARTURES.md). The schedule and the decisions that gate it are in
[`PLAN.md`](PLAN.md).

## Thesis in one paragraph

Equivalently positioned workers using the same AI tools at the same intensity get radically different
outcomes, and the variance is not explained by how much technology they use. **Algorithmacy** names
the difference: the communication competency required to coordinate with a human counterpart through
an opaque, adaptive intermediary. The construct is built for **triadic mediated coordination**, in
which an active third party sits between two human parties and runs on objectives neither endorsed,
and it is argued against the human–AI interaction constructs that inherit communication theory's
dyadic frame.

The live draft defines algorithmacy on the literacy / numeracy / oracy pattern: interpret, specify
intent through, and keep track of an opaque, adaptive intermediary, so that a person can participate
in coordination that includes the counterpart. Machine orchestration is not in the definition. The
accepted abstract's list of five components is quoted verbatim in [`ABSTRACT.md`](ABSTRACT.md) as
the historical record and should not be restated as current.

## Contents

| path | what it is |
|---|---|
| [`ABSTRACT.md`](ABSTRACT.md) | **The submitted package, verbatim and locked** — what the conveners accepted |
| [`manuscript/PAPER.md`](manuscript/PAPER.md) | **Live draft** — full paper. Body may be revised; abs and intro may not |
| [`manuscript/RESEARCH_PLAN.md`](manuscript/RESEARCH_PLAN.md) | Deepening plan: steelman every construct, model construct development, write the qual study to standard |
| [`manuscript/METHODS_SKELETON.md`](manuscript/METHODS_SKELETON.md) | Methods/findings headings, citations, and the sentences we will write |
| [`manuscript/INTRODUCTION.md`](manuscript/INTRODUCTION.md) | **Locked 2026-08-19** — official abstract and introduction. Do not edit unless the author says to |
| [`manuscript/LOCK.md`](manuscript/LOCK.md) | The lock: what it covers, what it forbids |
| [`archive/`](archive/) | Previous twelve-section draft and its outline, frozen 2026-08-19 |
| [`ACCEPTED_VS_CURRENT.md`](ACCEPTED_VS_CURRENT.md) | What the quantitative→qualitative swap changes and what it leaves standing, measured against the accepted text |
| [`MANUSCRIPT_REVIEW_2026-08-18.md`](MANUSCRIPT_REVIEW_2026-08-18.md) | Full read of the **archived** twelve-section draft — findings ranked, register audit, verified citation ledger |
| [`reviews/`](reviews/) | Reviews of the **live** draft. Current: [`REVIEW_2026-08-19.md`](reviews/REVIEW_2026-08-19.md) |
| [`REVISION_MEMO.md`](REVISION_MEMO.md) | What the 18 August literature sweep found — tier-1 source misreads, the documented gap, housekeeping |
| [`interview/`](interview/) | **The live instrument.** Self-service interview harness, three protocols, anonymous intake. See below |
| [`PLAN.md`](PLAN.md) | Schedule to 10 September, what is closed and what still gates, risks |
| [`AGENDA.md`](AGENDA.md) | Open questions, author-only items first |
| [`DEPARTURES.md`](DEPARTURES.md) | Pointer to the manuscript's own four-delta note; row 1 closed 2026-08-18 |
| [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md) | Live six-section architecture |
| [`library/`](library/) | **Install archive.** Eleven dissertation-format cards, copied onto the private shelf 2026-08-19. Frozen. |
| [`literature/`](literature/) | **Working library.** Start at [`literature/README.md`](literature/README.md) |
| [`literature/COVERAGE.md`](literature/COVERAGE.md) | Paper 2's 44 cited works → Lima card, dissertation card, depth, status |
| [`literature/INDEX.md`](literature/INDEX.md) | Generated listing of the sweep cards, by cluster then read depth |
| [`literature/TRAPS.md`](literature/TRAPS.md) | Live citation hazards — wrong paper, wrong author, two Zhou 2025s |
| [`literature/steelmans/`](literature/steelmans/) | **Phase 1 hearings — all seven constructs**, written from the articles |
| [`literature/FINDINGS.md`](literature/FINDINGS.md) | What those hearings change: one falsifiable claim, one verification passed, three cheap upgrades |
| [`literature/cards/`](literature/cards/) | The cards themselves |
| [`literature/REFERENCES.md`](literature/REFERENCES.md) | The abstract's citations, all fifteen verified, four flagged on substance |
| [`literature/ZHOU_2025_INSTRUMENT.md`](literature/ZHOU_2025_INSTRUMENT.md) | The rival algorithmic competency scale, all twelve items, and the discrimination the items support |
| [`working/`](working/) | Scratch; not for citation |

## The interview arm

Built 2026-08-18 and **fielding**. Participants, staff and partners run an interview through an AI
assistant in their own editor; it anonymizes as it writes, they review and approve, and it submits
anonymously to a Cloud Function that refuses anything still marked unreviewed.

- **Instrument:** [`interview/`](interview/) — `AGENT.md` plus `protocols/{STUDENT,OPERATIONS,SELF}.md`
- **Invitation:** [`interview/EMAIL_TO_SEND.md`](interview/EMAIL_TO_SEND.md), copy-ready
- **Endpoint:** `https://us-central1-pitch-rise.cloudfunctions.net/intake` → `gs://pitch-rise-interview-intake`
- **Reading responses:** `interview/pull-responses.sh` syncs into a gitignored `responses/`. **This
  repository is public** — no response may ever be committed.
- **Approval:** Bentley IRB #260511078, exempt under 45 CFR 46.102(e)(2)(ii), 11 May 2026

**First response in, 2026-08-18** — a Hult participant, all blocks answered. Two findings bear on the
manuscript. She never contested an outcome and named why: no channel was legible as the place for it,
so she concluded *that's the way this is* — forbearance with no forum, which is what §5 predicts. And
she read the gate by pasting its feedback into another AI and asking for an explanation, which is
machine orchestration doing the interpretive work §7 cuts it out of. The transcript also measured
thin — answer and question word counts at parity — and the protocols were deepened in response.

## Status

**Support arm, reconciled against the manuscript on 2026-08-13.** This directory was built that
morning from the accepted abstract, before anyone here knew the manuscript existed; by that evening it
had been re-cut to match. Three of the four seams it identified turned out to be decisions the author
had already made and disclosed to reviewers in the manuscript's first-page note — the empirical arm is
a research design with no data, the protocol is Hult and not GauntleTT, and the third facet is
temporal tracking rather than machine orchestration. What survives is the work the arm can still do
without touching the author's prose.

**Standing, as of the reconciliation:**

- **Fifteen citations verified**, none fabricated, four flagged on substance
  ([`literature/REFERENCES.md`](literature/REFERENCES.md)). The most useful flag: Brynjolfsson et al.
  and Dell'Acqua et al. show divergence tracking *skill and task*, so §1's variance puzzle is what
  survives after both are accounted for.
- **Zhou et al. 2025 pulled item by item**
  ([`literature/ZHOU_2025_INSTRUMENT.md`](literature/ZHOU_2025_INSTRUMENT.md)) — a validated rival
  scale, and the only *measure* among the neighbours §9 treats. Not one of its twelve items mentions
  the human counterpart, which is the discrimination worth making.
- **The rival is now fielded**, adapted, as W2 Part 8 of `../../org_frontier/survey/cohort_algorithmacy/`, registered
  as **H4** with a latent-correlation threshold fixed before data. **An IRB question gates it** — see
  that study's amendment log.
- ~~**One departure stays open**~~ — **closed 2026-08-18.** The Stark & Vanden Broeck over-read is the
  accepted abstract's, not the manuscript's; `PAPER.md` already says *form* not *mechanism*, attributes
  the naming to Stark and Pais where the full-text card supports it, and never sets either source
  against Powell. [`DEPARTURES.md`](DEPARTURES.md) row 1.
- **A full manuscript review landed 2026-08-18** —
  [`MANUSCRIPT_REVIEW_2026-08-18.md`](MANUSCRIPT_REVIEW_2026-08-18.md). Verdict: major revisions, all of
  them small. The one that is not optional is the novelty claim: **"nobody has named it" is falsifiable
  by one database search** against Zhou, Lei, Liu, Huang and Hou's validated algorithmic-competency
  scale, and it has to narrow to the counterpart axis. The review also finds that **§1 cites nothing**
  for the variance premise, that the arm had filed **the wrong Zhou 2025 paper**, and that the register
  runs zero first person in 8,391 words against the house style's own rule.
- **The literature sweep is in the live tree as of 2026-08-19.** Three hundred and eighty-seven cards
  under [`literature/cards/`](literature/cards/), indexed, with Paper 2's 44 mapped in
  [`literature/COVERAGE.md`](literature/COVERAGE.md). The remaining read is Sutherland et al. (2020),
  Sage-blocked — not a missing-folder problem.

**Registered 2026-08-14; the place is confirmed.**

**The posture changed on 2026-08-18.** This was a support arm doing citation checks and structural
reading. It now also runs the instrument: the empirical arm moved from a quantitative three-wave
panel to a qualitative study, the harness was built and fielded the same day, and the first response
is in. The live draft is now [`manuscript/PAPER.md`](manuscript/PAPER.md). What this arm also
supplies is the study that draft's empirical section previews, now actually collecting.

Workshop terms that bind the work: registration confirmed the place on **14 August**; the full
manuscript is due **10 September**; attendance is in person for all three days; accepting also
commits the author to **reviewing the manuscripts assigned to his roundtable**, which is unscheduled
work between submission and travel. The workshop is free and feeds participants; travel and lodging
are his own. All dates sit alongside the lab's other deadlines in
[`../CALENDAR.md`](../CALENDAR.md).

## Relation to the rest of the lab

This arm **borrows constructs and measures people**; it runs no Φ. Two connections matter more than
the rest, and both are seams rather than clean inheritances:

- [`../../org_frontier/survey/cohort_algorithmacy/`](../../org_frontier/survey/cohort_algorithmacy/) develops the same Algorithmacy
  Competence Scale but pre-registers a **different field site** — Hult, Fall 2026, sixteen weeks,
  waves at 1/4/16 against Lima's GauntleTT, eight weeks, waves at 1/4/8. Whether these are one study
  or two decides whether that pre-registration covers this paper.
- [`../coordinative_sovereignty/`](../coordinative_sovereignty/) is the political arm of the same
  construct, and its research database **retired the claim this abstract still makes** — H5 at
  `research/research_database.md:23` reframes co-optation away from "a fourth coordination mechanism."

Both are tracked as decisions in [`PLAN.md`](PLAN.md), not as errors to quietly correct.

# Coding scheme — ats_hiring_gate

> **Dry-run test note.** This study is a sanctioned dry-run of the qualitative arm's contribution
> workflow. It is a pre-registration scaffold only: no fieldwork has been done, no data collected,
> and no findings are claimed. It is committed here to exercise the pre-commitment discipline (the
> coding scheme is committed before any fieldwork) and the directory-index machinery. It is safe to
> close unmerged.

Commit this file before the fieldwork. It fixes the questions before the answers, and the git history
is the evidence that it did. The mode is **stand-alone**: the study documents how a candidate, an
applicant tracking system (ATS), and a hiring manager locate the screening decision, without computing
a Φ verdict.

## Interview guide

Backward-working prompts for rule elicitation, from concrete recent instances to the conditions that
governed the action to a stated rule the party confirms or corrects. Questions marked **[system rule]**
recover the ATS's rule, which the human parties theorize from the outside.

*Opening*

1. Walk me through what happens to an application from the moment it is submitted to the moment a human
   first looks at it, as far as you can see it.

*The candidate*

2. When you applied, what did you do to get past the screening — keywords, formatting, tailoring? Tell
   me about the last time you changed an application to clear a filter. **[system rule]**
3. Did you ever learn that an application was rejected before a person read it? How did you find out,
   and what did you make of it?

*The hiring manager*

4. When a shortlist reaches you, walk me through the last hire where you overrode what the system
   surfaced — pulled someone it ranked low, or dropped someone it ranked high. What let you do that?
5. Is there a screening result you are required to heed, that you cannot reach past? Tell me about a
   case where the system's cut was final versus one where you set it aside. **[system rule]**

*The system's rule (theorized from outside)*

6. What do you believe the ATS actually filters on — a hard threshold, a ranking, a knockout question?
   What is your evidence? **[system rule]**
7. Have you noticed the screening change without anyone announcing it? How did you notice?
   **[system rule]**

*Where the decision sits*

8. When a candidate is screened out, who decided — the system, the manager, the recruiter, the rubric?
   Walk me through one concrete case.

## Bit calibration

For each node, the threshold separating active from inactive, stated before any instance is coded. The
binary collapses detail; the finer encoding it discards is noted.

- **Candidate (C)** — active = submitted an application meeting the posting's stated minimum
  qualifications in the relevant cycle; inactive = no application or below the stated minimum. Collapses
  the degree of fit and the tailoring effort into one bit.
- **ATS (S)** — active = the system applied a knockout or ranking rule that removed or de-ranked the
  application before a human read it; inactive = the system stored and surfaced the application without
  removing or re-ordering it. Collapses ranking magnitude into commit-versus-store.
- **Hiring manager (M)** — active = the manager advanced or rejected a candidate against the system's
  surfaced order; inactive = the manager followed the system's order without adjustment. Collapses the
  manager's reasoning into whether it moved the outcome.

## Coding scheme and reliability

First-order codes stay in the parties' terms (for example, "the keywords got me through", "I never saw
the ones it killed", "I pulled her even though she ranked low"). Constant comparison groups these into
second-order themes naming the practice analytically (knockout filtering, gaming the filter, manager
override, the unseen cut). Two raters code independently against this scheme; they do not confer until
both have coded. Reliability is reported as Krippendorff's α, with α ≥ 0.80 the working bar. Member
checking: the encoding is shown to a subset of participants and their acceptance recorded.

## Pre-registered verdict (model-bound only)

**Not applicable.** This is a stand-alone study and computes no Φ verdict.

## Falsification conditions

Written here, before any field visit, and to be reported in `STUDY.md` whether or not they are met.

- **The prior (strict bottleneck) departs toward factoring** if managers routinely and successfully
  reach past the system's cut — if the ATS stores and surfaces rather than commits, so the same topology
  that could bottleneck instead merely factors. A documented case where a manager hired a candidate the
  system had knocked out would be evidence of this departure.
- **The candidate is a party, not only an object,** if how a candidate compresses intent into the
  signals the ATS accepts (keywords, formatting, knockout answers) actually shifts which applications
  the system advances — if gaming the filter co-determines the screen rather than merely surviving it.
- **The system's rule is unrecoverable** if no party can theorize the ATS's filter and no document or
  log discloses it, so the system's rule cannot be stated even as a hypothesis. This would mark the
  setting as one where the determination is committed by a party none of the others can read.

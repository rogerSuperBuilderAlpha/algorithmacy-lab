# Notes on the full draft of 7 October 2026

> **The author rejected this first draft the same day** ("pure AI slop … EXPLAIN WHAT YOU MEAN. Do not try
> to sound smart or cute"). The replacement is [`DRAFT_2026-10-07_plain.md`](DRAFT_2026-10-07_plain.md): about
> 7,000 words of body, 43 references, mean sentence 14 words, no em-dashes outside the author's introduction.
> It keeps the same argument, sources and choices listed below, and the same corrections to the
> introduction. It drops the Lima paper's compressed sentences instead of carrying them over, restates the
> three propositions in plain words, and adds a section, "The situation", that defines the three parties
> and the three features before anything else uses them. The notes below describe the rejected draft.

[`DRAFT_2026-10-07_claude.md`](DRAFT_2026-10-07_claude.md) is a complete first draft written by Claude on
the author's instruction of 2026-10-07 ("draft the whole paper"). That instruction reverses the ruling of
the same morning that the author would draft sections 3–6, and sets aside, for this draft, the arm's rule
that Claude does not generate manuscript prose. [`PAPER.md`](PAPER.md), the author's text, is untouched.
Nothing here has been through a review-and-rewrite loop; the author's read-aloud is the gate.

## What the draft is made of

| Tag | Paragraphs | Words | What it means |
| --- | --- | --- | --- |
| `[A]` | 13 | about 900 | The author's prose, copied by script from the frozen Lima paper; each checks as an exact substring. The number in parentheses is the source line. |
| `[A*]` | 29 | about 3,240 | The author's prose, edited: trimmed, joined across paragraphs, or corrected against a source. |
| `[C]` | 23 | about 2,100 | Drafted by Claude. The count includes the title, abstract and keywords. |

About two-thirds of the body is the author's own wording. The `[C]` share is the abstract and title, the
bridging paragraphs, the Stelmaszak and Schoeneborn passages, the paragraph on sensibility as a genus, the
three "what the property withholds" openers and the three failure-mode paragraphs in the mechanics, the
removal argument for the loop, and three subsections of the discussion.

## Length

| Section | Draft | Budget |
| --- | --- | --- |
| Introduction | 557 | 800 |
| The Triadic Blind Spot | 1,249 | 1,700 |
| Algorithmacy and Coordinative Co-optation | 1,217 | 1,600 |
| The Mechanics of Algorithmacy | about 1,760 | 2,900 |
| Discussion | 958 | 1,500 |
| Conclusion | 159 | 400 |
| **Body** | **about 5,900** | **8,900** |

With 46 references (991 words), the abstract and two tables, the draft stands near 7,700 words against the
journal's 11,000. **It is about 3,000 words short of the body budget, on purpose.** The room is in the
mechanics and the discussion, and filling it needs sources nobody has read yet: the six research lines in
`../RESEARCH_PLAN.md` are still unrun. I did not pad those sections with uncited argument.

## Choices I made that are the author's to overrule

1. **Genus.** Algorithmacy is a *sensibility* — a standing orientation toward a kind of situation — that
   works through three *competencies*. The paragraph defining "sensibility" is Claude's and cites nothing;
   research line 4 should either find it a source or replace it.
2. **First operation.** Interpreting reads both the intermediary's rule and the counterpart's intentions
   from one signal (the Lima paper's version), not the counterpart alone (the new introduction's wording).
3. **Propositions kept.** The three propositions carry over verbatim. None of the five model papers states
   propositions, but the journal lists "proposition development" among its accepted approaches, and the
   introduction now signals them.
4. **The gate as the vehicle.** The student at the review gate opens section 3 and runs through section 4.
   It is the author's own course. A reviewer cannot identify the author from it as written, but it must
   stay generic.
5. **Empirical design out.** No site, no instruments, no pilot. The pilot observation about a participant
   routing her explanation through a language model is restated as a possibility, not a finding.
6. **Title and abstract** are Claude's placeholders.
7. **"Irreducible."** The loop paragraph gives the word a meaning internal to this paper: no pair of the
   three parties can be handled and the third added afterward. It makes no claim about integrated
   information.

## Every change to the author's wording in the introduction

The four introduction paragraphs are `[A*]`. Changes, each from a flag in `FLAGS_2026-10-07.md`:

| Was | Now | Why |
| --- | --- | --- |
| "quieter, (sociomaterial?) displacements … are what actually reconfigure" | "less visible displacements … are also reconfiguring" | B1: Orlikowski & Scott say "less visible", and "in addition to" |
| "those quieter shifts" | "those less visible shifts" | B1 |
| ""counterparts" in a system, implementation, and use" | "a "counterpart" in a system of work that includes its design, implementation, and use" | B5: the abstract's wording; abstract depth only |
| "relations among humans and algorithmic black boxes (Stelmaszak et al., 2025)" | "relations among human and algorithmic actors (Stelmaszak et al., 2026)" | A6: their formula; the year collision |
| "which reduce visibility and control" | "relations in which generative AI may expand the black box and reduce visibility and control" | B3: hedged, and specific to generative AI |
| "while paradoxically manufacturing a false sense of epistemological security" | "while its detailed outputs give those who are shown them an illusion that uncertain outcomes are knowable" | B6: the certainty is the audience's, about outcomes |
| "cooptive", "cooptation" | "co-optive", "co-optation" | Stark & Vanden Broeck hyphenate |
| The parenthetical second paragraph | Two sentences, parentheses and "That said" removed | Reads as a note to self; the promise is paid in the Discussion's "The why" |
| "As traditional firm boundaries dissolve, these algorithmic intermediaries operate with gradual *organizationality*, functioning as distinct social addresses with collective actorhood (Schoeneborn et al., 2026) that co-opt (Stark, 2024 - OT), ie evaluate and bind." | "The intermediaries in question are not neutral software. The platforms behind them hold collective actorhood by degree, and they work to downplay it (Schoeneborn et al., 2026); on them, as Stark and Vanden Broeck (2024, p. 5) put it, actors "are co-opted"—enrolled, evaluated, and bound." | A1, A2, B2. Two of these sentences are Claude's |
| "mast-strapping ourselves trying to preserve" | "strapping ourselves to the mast of" | Clarity |
| "relying on a neo-Quinean set-theoretic dyadic ontology that is entirely blind to the emergent, binding power of the triad" | "reducing the triad to pairs, which leaves us blind to its emergent, binding power" | C2: no source yet for the Quine claim |
| "Oracy is the sensibility" | "Oracy—the term is Wilkinson's (1965)—is the sensibility" | Adds the missing citation |
| "Drawing on recent views of imagination as a relational capacity enacted in the encounter … algorithmacy can be seen as a situated engagement with the unseen." | "Porsfelt et al. (2026, p. 1) propose treating imagination as "a situated engagement with the non-present"; algorithmacy can be seen as a situated engagement with what is present and unseen." | B4: quotes their phrase and marks the difference |
| "operates though" | "operates through" | Typo |
| "1) interpret a variable counterpart's intentions from an otherwise innocuous output" | "1) interpret, from an otherwise innocuous output, both the intermediary's rule and a counterpart's intentions" | Choice 2 above |
| The "- OT", "- OS", "- JMS" marks | Removed | Working marks |

The opening sentence, "Organizations fail to adopt and understand the tsunami…", stands as written and
still has no source (flag C3).

## What happened to section 2

The author ruled section 2 their working draft. The full draft does not keep its wording, because five of
its claims were contradicted by the sources (flags A1–A6). Two of its sentences survive in edited form at
the head of "The Triadic Blind Spot". The rest of that section is built from the Lima paper's hearings,
regrouped into three families as section 2 proposed, with the three rivals it had left out.

## Changes inside the Lima-derived `[A*]` paragraphs

These are trims and joins. The recurring edits: "Paper 1 names" became "I call"; references to Study 2,
Study 3, RQ4, Appendices A–C and Table B1 were removed; "Zhou et al. (2025)" became "Zhou, Lei, Liu, et
al. (2025)"; "eight" stays for the constructs. In these paragraphs the only citation detail added is the page number on Stark and Vanden Broeck.

## Source standing

- Every quotation from the seven newly read sources was matched against the PDF text.
- Anthony, Bechky & Fayard (2023) is cited once, for a claim its abstract supports, with no quotation
  beyond the abstract's words and no page.
- Citations carried from the Lima paper rest on that paper's audits of August and September. They were
  not re-verified today.
- All 46 reference entries are cited, and every citation has an entry.

## What the drafting harness reported

Register `ot`, added today from the five model papers; its selftest failed at five documents, so it is
uncalibrated and none of this is a verdict.

- **Paragraphs are short**: 97 words on average against a venue mean of 208. Tables and one-line
  transitions pull this down, but the body paragraphs are still about half the venue's length.
- **Em-dashes run at 6.4 per 1,000** against 2.7. Most are the author's: the `[A]` and `[A*]` text runs
  near 7.7, Claude's near 3.8.
- **Colons and semicolons run four to five times the venue rate**, in all three kinds of paragraph.
- **First person is singular throughout**; the five exemplars are co-authored and write "we".
- **Two runs of citation-final sentences**, both in the author's text: the introduction's first paragraph
  and the hierarchy–market–network paragraph.
- **Four in five paragraph joins share no entity across the break.** The section openings are the weak
  joins.

I made one pass after the report, on Claude's sentences only: nine colon or semicolon joins split into
sentences, and one transition paragraph cut. I did not touch the author's punctuation.

# Slide outline — v4 (23 slides, 30-minute slot requested, 20 confirmed)

The author's deck of 2026-09-25 (`Do Triads Reduce to Dyads?.pptx`) replaces v2. Its text is transcribed
word for word in [`talk/deck.md`](talk/deck.md), with the design removed and the pictures, the valency
diagram and the table kept. The author's script of the same day was written against the 18 v2 slides; it
is re-sectioned onto the 16 new ones in [`talk/script.md`](talk/script.md). The table shows where each
passage of the author's script went. v2's outline is in git history (commit `82ca04f`).

**v4, 2026-09-25.** Slides 16–22 are new: three findings from the lab, two invitations to fork the
repository, and a live session with its fallback. They are Claude-drafted, not the author's text; the
author's deck ends at slide 15 and resumes at slide 23. Image Sources moves from slide 16 to slide 23.

| # | slide | author's script passages (v2 slide numbers) | sources |
|---|---|---|---|
| 1 | Do Triads Reduce to Dyads? | 1 | — |
| 2 | The Four Relational Sensibilities | 2 | the author's framing |
| 3 | The Ontological Reducibility Dilemma | 3 | CLAIM.md |
| 4 | Peirce: The Three Irreducible Categories | 4 | peirce1931papers |
| 5 | Peircean Reduction Thesis (PRT) | 5 | peirce1870description, peirce1931papers |
| 6 | Autonomous Mediation vs. Dyadic Cascades | 6 (giving is not throwing) | peirce1931papers (CP 1.345) |
| 7 | Topological Obstructions to Dyadic Synthesis | 7 (valency) and 8 (the junction, Kempe) | peirce1931papers, peirce1897logic, kempe1886memoir |
| 8 | The Teridentity Relation: =_3 | 13 (Burch sentence), 14 (last technical sentence; the whole layman passage); one new sentence | burch1991reduction (metadata only) |
| 9 | Quine’s Dyadic Translation (1954) | 10 and 11 | quine1954reduction, lowenheim1915moglichkeiten |
| 10 | Deconstructing Quine’s Fallacy | 12; 13 (opening and Herzberger); 14 (Dau and Hereth Correia); 13 layman | herzberger1981theorem, dau2006instances |
| 11 | Relational Co-Clones and Expressive Power | 14 (Hereth Correia and Pöschel; Koshkin); 15 | herethcorreia2006teridentity, koshkin2024reduction, burch2021sep |
| 12 | The Synergistic Teridentity Correspondence | none: both passages are new | williams2010decomposition |
| 13 | The Causal Test (IIT 4.0) | 16 (the test and the scissors) | albantakis2023information, CI (corrected 2026-09-25 with the author's approval: `reviews/2026-09-25/SLIDES_13_14.md`) |
| 14 | IIT 4.0 Topological Architecture Sort | 16 (criterion, control, PID) and 17 | CI thinkers-peirce-h1-irreducibility, thinkers-peirce-jd-full (corrected 2026-09-25 with the author's approval: `reviews/2026-09-25/SLIDES_13_14.md`) |
| 15 | The Ontological Reality of Algorithmacy | 18 | ARGUMENT.md (S6) |
| 16 | Genuine Giving and Its Imitation | new: Claude-drafted | CI thinkers-peirce-jd (`giving_genuine`, `giving_degenerate`) |
| 17 | A Vote Is Not Always a Whole | new: Claude-drafted | CI thinkers-simmel-h3-majority (`majority_triad`, `unanimity_triad`); caveat CI q215-phi-family-robustness |
| 18 | Irreducible by Law, or by Nature | new: Claude-drafted | CI q213-contingent-irreducibility, q214-triadic-classification |
| 19 | Fork the Repository | new: Claude-drafted | GETTING_STARTED.md, README.md ground rules, `org_frontier/protocol/new_question`, `ci/reproduce.json` |
| 20 | Questions Waiting for Someone | new: Claude-drafted | CI q204-phi-on-real-coordination; CI thinkers-simmel-h2-number (clique Φ growth); AUTHOR_TASKS.md (missing cards) |
| 21 | What Questions Are You Interested In? | new: Claude-drafted, live | `talk/LIVE_SESSION.md` |
| 22 | If the Laptop Fails | new: Claude-drafted, fallback table | `talk/live/REHEARSAL_2026-09-25.md`; CI thinkers-peirce-jd, thinkers-simmel-h4-nonpartisan, thinkers-simmel-h3-majority, q213-contingent-irreducibility |
| 23 | Image Sources | not spoken | — |

**Held back.** The author's v2 slide 9 (Simmel) has no slide in the new deck. Its text is kept verbatim
in a comment at the end of `talk/script.md`.

**New text.** Claude drafted three passages in the author's slides 1–15, each marked in `script.md` with
a `<!-- new -->` comment: one sentence on slide 8 introducing the teridentity formula, and the technical
and layman passages on slide 12. Everything else in slides 1–15 is the author's wording. Slides 16–22 and
their script sections are entirely Claude-drafted (`talk/deck.md`, `talk/script.md`, both marked
`<!-- new -->`): three lab findings (16–18), two invitations to fork the repository (19–20), and the live
session and its fallback (21–22). Every number on these slides is a CI-registered string, recorded in
`talk/NUMBERS.md` under "Added for v4". Slides 13–14 carry the corrections the author approved on 2026-09-25
(`reviews/2026-09-25/SLIDES_13_14.md`).

**Live session.** Slide 21 is spoken live: the author reads an audience member's coordination sentence,
and the assistant builds and runs it against the lab's own reader. The runbook, the translation rules, the
size and time limits, and the four rehearsed prompts are in [`talk/LIVE_SESSION.md`](talk/LIVE_SESSION.md);
the rehearsal that validated it is in
[`talk/live/REHEARSAL_2026-09-25.md`](talk/live/REHEARSAL_2026-09-25.md). Slide 22 is the fallback if the
laptop or the network fails during the session.

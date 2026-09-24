# Review synthesis — 2026-09-24

The panel read the first deck and script at `7634c1c`. It had six seats (Peirce scholar, logician, Simmel
sociologist, IIT specialist, hostile referee, ALGOCON attendee) and a mechanical auditor. Every finding is
in [`FINDINGS.md`](FINDINGS.md). Two gate agents then checked the factual, citation and number
corrections against the sources; their record is [`VERIFICATION_GATE.md`](VERIFICATION_GATE.md). None of
the seats questioned the locked thesis. Most of what they found was the talk misreporting its own
sources.

## Applied (deck and script revised in one pass)

- **Peirce.**
  - "The proof came later" became "the argument came later", as CLAIM.md requires.
  - The positive clause now reads "four or more", not "more than two".
  - The 1892 reply to Kempe is reported as Peirce gave it: mediation remains in "the attachment of lines to
    spots", and the unit comes from an unshown abstraction. The script no longer says Peirce called
    Kempe's unit the triad.
  - The chronology is fixed: Kempe 1886, Peirce 1892, then the node premise in 1897.
  - CP 1.345's "merely one dyadic relation followed by another" now goes with its own example (throwing
    away), not with the lay-down case of CP 8.331.
- **Simmel.**
  - The distant third ("configurations of twos") is kept apart from the lab's majority model. The seats
    showed that the majority model is neither a distant-third model nor Simmel's own point.
  - The broken-line diagram now shows the direct tie as well.
- **Löwenheim, Kalmár, Quine.**
  - Each result is stated separately: Löwenheim's binary relatives over pairs, Kalmár's single relation
    for satisfiability, and Quine's single predicate for any first-order theory.
  - "The reply that made most philosophers stop believing Peirce" became "the result that led many to
    doubt Peirce, although none of its authors aimed it at him".
  - Quine's paper is called "a short paper", not "a two-page paper".
- **The debate.**
  - Slide 10's universal "every reduction mints a third" was false for primitive-positive composition on
    a fixed domain. It became "every reduction keeps the junction", with the theorem attributed to
    Hereth Correia & Pöschel 2006 and Koshkin 2025, and a worked example of minting g, the giving.
  - Koshkin's position is stated as his, not as "which constructions are legitimate".
  - Burch's PAL proof now carries its restriction.
- **The lab's move.**
  - The script says plainly what Φ measures, and names the control.
  - It fixes the sense of "reduce" out loud: rebuilding among the same parties from one-input links.
  - It says the criterion was chosen after the first probes and then pre-registered.
  - The cause-side count is glossed as the element plus its one source.
  - The imitation-of-giving model is explained as a closed loop.
- **Slide 14.** The seats blocked the claim that wholeness and joint determination come apart "in both
  directions" on unregistered evidence. The lab addendum (PR #772) registers it. The IIT seat also found
  that the majority's joint determination rests on a tie, which PyPhi's own ties field misses. The slide
  therefore cites the pre-registered fresh sample: 11 of 30 forms have a party jointly determined by two
  others in a system that splits, all tie-robust. It does not cite the majority.
- **Algorithmacy.**
  - Literacy's examples are now one-party media: a letter, a notice, a manual. A shared ledger meets the
    criterion.
  - The definition of algorithmacy carries "acts back on both".
  - The platform claim is marked as unmodelled.
  - The concession now covers a shared tally, and the historical premise is labelled as a premise.
  - The competence bridge is stated as the one premise it is.
  - The deck's conclusion uses the locked wording, "one-input determination".

## Not applied, and why

- Suggestions to add φ_s notation to the slides. The script defines Φ in words instead, which the
  attendee seat asked for, and notation would load a general audience.
- Several minor wording preferences, which fall outside the review's correctness scope. The author's
  read-aloud decides those.
- Revisions to ARGUMENT.md and QA.md. Where they conflict with the revised script, the script governs,
  and QA.md says so.

## State after the pass

`check_talk.py` passes; the two numbers from the lab addendum (11, 30) are registered by #772 as
`thinkers-peirce-jd-full`. The script runs 2,190 spoken words, about seventeen minutes at 130 words a minute.
The author's timed read-aloud is the remaining gate.

# Do Triads Reduce to Dyads? — Port of Spain, October 2026

Conference deck for the triadic-reduction talk: *Do Triads Reduce to Dyads? The Peircean Reduction
Thesis, Quine's Fallacy, and the Mathematical Foundations of Algorithmacy.* Presented in Port of Spain,
October 2026.

- [`Do-Triads-Reduce-to-Dyads-Trinidad.pptx`](Do-Triads-Reduce-to-Dyads-Trinidad.pptx) — the deck, 27
  slides.
- Google Slides copy:
  <https://docs.google.com/presentation/d/10neC-J2B0sAt3Conpo1pRVj66VtCUV0HQr0HASzzY6E/edit>

This deck is a revision of the author's own Google Slides deck. It is separate from the black-and-white
build in [`../deck.pptx`](../deck.pptx), which `../build_deck.py` produces from `../deck.md` and
`../check_talk.py` checks; neither the builder nor the checker reads this file.

## This revision

- **Running example.** A new slide 5, "Running Example: John, Sally, and a Ball," contrasts a throw (a
  chain of pairs: John to ball, then ball to Sally) with a give (a triad: John gives Sally the ball). A
  one-line "John & Sally" callout carries the example through slides 6, 8–15, 17, 18 and 20.
- **Slide 18, "The Final Result: Where Quine's Reduction Holds."** Quine's reduction holds only when three
  conditions hold together: the domain grows, with pairs (and pairs of pairs) added as new objects;
  pairing is assumed, and pairing is itself a three-place tie; and the result is a translation, not a
  construction. On a fixed domain with only joins and projections the reduction fails (Burch 1991;
  Hereth & Pöschel 2006).
- **Slide 19, "The Other Side: Why Quartets Reduce to Triads."** Bonding rule 3 + 3 − 2 = 4: two triads
  joined at one bond leave four free ends, so R(a, b, c, d) = ∃x [T₁(a, b, x) ∧ T₂(x, c, d)]. An
  open-question box notes that four-way synergy remains open, and that the lab's cliques of four and five
  read Φ = 12 and Φ = 20.
- **Slide 12.** The "Domain Escalation" bullet is softened from "Infinite set-theoretic universes
  required" to "The universe must be closed under pairing."

## Known issue

Slide 1 is a blank cover: the cover image did not survive the export from Google Slides.

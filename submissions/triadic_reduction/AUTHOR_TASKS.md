# Author tasks

Decisions and items only the author can close. Each has a default; nothing below blocks work unless it is
marked **blocking**.

## v3 deck and script (2026-09-25): what the record says, for the author to decide

The deck and script are the author's, and nothing below has been changed in them. A fact check against
the verified cards and the lab's CI output found the problems listed here. The full table, with
file and line for every item, is in [`reviews/2026-09-25/FACTCHECK.md`](reviews/2026-09-25/FACTCHECK.md).
They are in order of how much they would hurt in the room.

1. **Slide 13, "Causal Collapse Theorem."** There is no such theorem, and the lab's own results
   contradict it. A ring of one-input copies and a mutual dyad both reach Φ = 2.0, and 8 of the 89
   one-input wirings have Φ > 0. Slide 14's second row and the script's slide 14 both say so, so the
   deck contradicts itself. The register already marks this as a Gemini invention (TR-S5-123).
2. **Slide 14, the table.** Row 1 says all 89 wirings have Φ = 0.0; 8 of them have Φ > 0, and the Φ = 2.0
   ring in row 2 is one of those 89, not a separate case. Row 4 says Φ = 2.0; the five forms run from
   0.21 to 2.0, and only one of them is 2.0. "Synergy" appears in rows 2–4, but no run measured
   synergy. The 11 of 30 and 5 of 30 counts are right. `check_talk.py` fails on row 1's `0.0` until
   this is settled.
3. **Slides 12 and 15 and the script's slide 14, synergy.** No source links teridentity to PID synergy;
   Williams and Beer never mention teridentity. The lab ran no PID, and the AND control is not pure
   synergy (about 0.31 bit redundant, 0.5 bit synergistic). Slide 15 makes synergy one of three
   supports for the conclusion. The script's "pure causal synergy (Syn > 0)" on slide 14 has the same
   problem.
4. **Slides 8, 10 and 11 and the script's logic passages, which operations.** The irreducibility results
   hold in Peirce's own algebra (PAL) without teridentity, as Hereth Correia and Pöschel proved.
   Under "project-join" or primitive-positive operations, the setting the slides name, triads *do*
   reduce, on any domain of three or more elements (Koshkin 2025). Ordinary relational algebra also
   builds teridentity from two-place identity, so "Unprovable from binary identity" (slide 8) is false
   as stated. Burch 1991 has not been read (metadata only).
5. **Names and years.** "HERETH & PÖSCHEL (2006)" should be Hereth Correia and Pöschel (2006); the
   short form is their 2011 paper. "KOSHKIN (2024)" is attached to results from 2022 (the full
   first-order analysis and "Peirce is validated") and 2025 (domain thresholds). The script's
   "ter(R) ≥ n − 2 … strict lower bound on infinite domains" should read: holds on any domain, and is
   an equality on infinite ones.
6. **Quine.** His one predicate is 'F', not 'J' or ∈ (slide 9 and the script). The pair is Kuratowski's,
   not "Wiener-Kuratowski". His reduction does not require an infinite universe; Löwenheim's version
   uses a finite one of n² elements. "Smuggled teridentity" is Koshkin's criticism, not something in
   Quine. Quine does not name Peirce on the pages read, so "a fatal blow to Peirce's theory" and "led
   logicians to conclude Peirce was mistaken" overstate what the record shows. Burch's SEP says only
   that the thesis was "doubted by many".
7. **"Quine's Fallacy"** (title slide and slide 10). CLAIM.md, which you locked on 2026-09-24, rules it
   out. Burch says both Peirce and Quine are correct, and slide 11's own script says the same. Keep it,
   or go back to the lock.
8. **Peirce.** "Does not consist in any complexus of dyadic relations" is CP 2.274, c. 1902, not the 1870
   paper. The positive half of the thesis is n ≥ 4, not n ≥ 3; slide 5 has it right and the script
   does not. On Kempe, Peirce in 1892 *conceded* part of Kempe's point and modified his position, so
   "Peirce demonstrated" is too strong.
9. **"Join-irreducible"** (slides 5, 8, 12, 15). The register marks this term as refuted for the sense
   used here.
10. **Slide 2, arities.** The slide calls oracy monadic; the script calls it "an immediate acoustic
    dyad". No source gives oracy or numeracy an arity. Pick one.
11. **Slide 1, "Theoretical Computing Group."** No such group appears anywhere in the repo. Confirm the
    affiliation.
12. **Image rights.** The Peirce portrait is a colorized copy from a blog, and the Quine photograph (1958)
    comes from Britannica's CDN and may still be in copyright. A Wikimedia Commons file with a credit
    line would be safer. Both images are committed to a public repository.
13. **Length.** Both registers spoken in full come to 2,936 words, about 22.6 minutes at 130 words a
    minute, against a budget of 2,405 words (18.5 minutes plus a buffer). Speaking one register per
    slide would fit.
14. **Simmel.** He has no slide in the new deck. Your Simmel section is kept word for word at the end of
    `talk/script.md`.

## Decisions for the claim lock (**blocking** the deck and script)

The twelve decisions are listed in full, with defaults, at the end of [`CLAIM.md`](CLAIM.md). Four of them
change the talk most:

1. **Lock the thesis as drafted.** The conditional is restated in the causal sense: among fixed parties,
   one-input mediation never composes joint determination. "Necessity" is stated as conditional
   necessity, and the argument is ontological about the target, not about triads as primitives.
2. **Concede that the target is older than AI.** Simmel's arbitrator, a vote tally and a posted price all
   meet the criterion. The default concedes this on slide 15 and treats AI as the mass modern instance.
   The lab's definition of literacy by teleology ("pursues no objective of its own") conflicts with the
   structural test; the talk uses the structural one.
3. **Register new lab evidence before October, or only disclose.** Candidates:
   - the single-mechanism cause purview of Simmel's majority triad — the missing cell, a party jointly
     determined inside a system that factors;
   - a confirmatory run with the criterion fixed in advance;
   - IIT 4.0's grain (exclusion) test on a paired re-encoding of the control.

   Any of these is a separate, pre-registered `org_frontier` PR, not part of this arm.
4. **Title.** Default: *Can a Triad Be Built from Pairs? Peirce, Quine and the Target of Algorithmacy.*

## Sources only the author can supply

| item | why | route |
| --- | --- | --- |
| Quine 1954, pp. 181–182 | The library read p. 180 and both footnotes; the claim that Quine never names Peirce rests on those pages and on Koshkin 2022 n. 1. The Gemini Project held `Quine-ReductionDyadicPredicate-1954.pdf`. | Share that PDF, or a library copy. Kept local only. |
| The NotebookLM artifact | Possibly the source of G6's ten pasted reviews, or a precursor of P1. | Reconnect Claude in Chrome, or export or paste it. |
| The "Triads" file or notebook | G3, G4 and G6 lean on it. | Say what it is. |
| The chats behind D1, D4, D5 and P1; the origin of G5's repository "deep dive" and G6's pasted reviews | Provenance. | Share links, if wanted. |
| Christopherson and Johnstone 1981, Burch 1991 and 1997, Herzberger 1981, Skidmore 1971 | All are metadata-only. The talk states their positions as reported by Koshkin 2022 and Conarroe 2020. | Library copies, if the author wants any of them quoted. |

## Publishing decisions

- The seven Gemini share links in `sources/` are live public URLs. Unpublish them in Gemini if they should
  not stay open; the captures already keep the text.
- G6 records that EBSCO full-text PDFs were uploaded to Gemini, and that Gemini wrote "reviews" of works
  nobody in the chat had read. It is kept verbatim as process; the author decides whether that stays public.

## Lab items this arm found and does not fix

These belong to other parts of the lab and go through their own PRs.

- `org_frontier/thinkers/peirce/paper.md`:
  - l.281 puts "A is determined by B and C together" in quotation marks as Peirce's. It is not his wording.
  - l.32–35 and l.105–107 put Koshkin's paraphrase of the two clauses and of the sale example inside
    Peirce quotation marks.
  - l.272–274 credits Kempe and Burch with the junction-as-triad view. Kempe held the opposite, and
    Burch 1991 is unread.
  - l.44–48 says Koshkin "points to 'information integration' measures as the analogous quantity". The
    `koshkin2022reduction` card has the exact wording to cite.
  - The bib entry for Koshkin is stale: the papers are TCSPS 58(4), 2022, and Logic Journal of the IGPL,
    2023/24.
  - Quine 1954, Löwenheim 1915 and Kempe 1886 have no bib entries.
- The "Φ > 0 ⟺ triadic ⟺ algorithmacy" biconditional in `org_frontier/classifier/concepts.md` L37–40,
  in `STRUCTURAL_FINDINGS.md` L5–6 and L65–70, and in the essay `literacy_or_algorithmacy.md` conflicts
  with the talk's criterion. The lab's own mutual dyad and copy ring are Φ = 2.0 wholes with no joint
  determination. `ci/reproduce.json` prints `dyad_mutual triadic`. The talk says once that the lab now
  requires joint determination as well.
- The dissertation's use of Conarroe 2020, if any, should say M.A. thesis, University of Colorado
  Boulder, not a Virginia PhD.

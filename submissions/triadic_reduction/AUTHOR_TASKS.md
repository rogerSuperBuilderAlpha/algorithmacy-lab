# Author tasks

Decisions and items only the author can close. Each has a default; nothing below blocks work unless it is
marked **blocking**.

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

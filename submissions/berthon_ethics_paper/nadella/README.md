# Workstream: the design ethics of current LLM tools, read through Nadella's X article

*Written by Claude on 2026-10-24. Set-up only: nothing here is research or draft yet.*

**The paper, in the author's terms** (verbatim in `SOURCE.md`). It examines the design ethics of current LLM tools;
*Spaces in the Stream* examines their cognitive issues. Nadella's X article, "Models as Insider Risks in the Super
Intelligence Era" (10 Oct 2026), proposes a set of moves, and those moves repeat the mistakes of two transitions:
from *scriptio continua* to spaces between words, and the management of mass literacy through the printing press.

## The research question this sets up

*Claude's restatement, for the author to accept or change.* For each of Nadella's moves, which mistake of the two
transitions does it repeat, what made it a mistake then (by the three internal standards of the consolidation:
contemporary objection, a broken professed standard, an unmet promise), and what corrected it? The grid below is the
work plan. Rows are his moves, by paragraph; the columns are where the lab's record already speaks. Empty cells are
the research.

| Move (paragraph) | Scribal transition: what the record has | Print and mass literacy: what the record has | Already argued in the lab |
|---|---|---|---|
| Responsibility stays with the deployer; authority separated from supply (P3, P5, P17) | Ruler and church held the conventions of the page; nothing shows scribes and readers sharing interests as equals (`sources/dxf_facet_O_custody_of_conventions.md`; `dxf_facet_J_who_holds_the_convention.md`) | The Stationers held the press by grant (`bec_facet_B_print_1450_1800.md`, failure 1; ledger H11) | facet G C7(ii); v4 §4.1 |
| Chain-of-thought transparency, "non-negotiable" but insufficient (P9) | — | Disclosure as the second of four stages (ledger H24) | v4 §4.3; facet G C6(a) |
| Controls outside the model; separate harness and action space (P11, P12) | Spacing moved work from reader to page; so does the reference monitor (facet G C7, "Complication") | — | dxd T_adjudication §6 |
| Model diversity; independent auditability (P14, P18) | — | Second interpreters, notaries (ledger H10) | — |
| Observe everything: "tamper-proof human readable evidence" (P15) | A text that cannot answer the person who must act on it (Plato; ledger H27) | The record over the voice; the jurat (H07, H22) | v4 §4.2; facet G C4 row 1 |
| Verifiability: continuous testing (P16) | — | — | — |
| Emergency brake held by "an authorized person" (P19) | — | Who held the test and the brake (the gate, H01) | facet G C4 row 2, C6(c) |
| Disclosure "to those affected" after failure (P20) | — | Disclosure without capacity; the Requerimiento (H18) | v4 §4.2; facet G C6(e) |
| "Trust the model the least" (P21) | — | — | v4 §7 |
| Missing: any capacity-building for the people acted on | Spacing served readers for whom Latin was foreign, against "the elitist literate mentality of the ancient world" (Saenger, p. 11; ledger H26) | Literacy withheld, then oversold (H04, H13); scaffolds by sponsors (H25) | v4 §4.4 |

## Where the record pushes back on the framing

These points come from the lab's own audited research. The author decides what to do with them.

1. **The spaces transition is the lab's good precedent, not a mistake.** In `dxd_foundation` and the Spaces essay,
   word separation is the model of a sound design move: the page took on work the reader had carried (dxd
   T_adjudication §6). So "making the mistakes as the transition from scriptura continua to spaces between words" needs a gloss. The record offers three
   candidate mistakes of that era, each sourced: keeping a costly script because the literate elite did not want
   readership widened (Saenger, p. 11); centuries of delay; and custody of the convention by ruler and church rather
   than by readers (facet O). Nadella's P11 makes the same kind of move as spacing (work from person to artefact),
   so the contrast must rest on *whom the move serves* and *what task it leaves the person*, which facet G flags as
   the author's own tests to rule on (C7).
2. **Spacing did not spread literacy.** No historian the lab read credits word separation with spreading reading;
   it lowered a cost (`dxf_facet_C_spacing_to_literacy.md`, verdict 5). "ultimately how the world managed the mass
   distribution of literacy though the printing press" therefore links two transitions that the record keeps separate, and the
   paper should say how they connect.
3. **Print's mistakes are institutional.** The documented print-era failures are a chartered monopoly, bars on
   reading the Bible by rank and sex (1543), licensing under the Tridentine Index, and language bars at law (facet B
   print, failures 1–4), plus the five practices of the consolidation. The mapping above draws on these.
4. **The post concedes much of what a critic would say** (facet G C8–C10): most of its controls need no reading; P9
   already calls chain of thought "not sufficient or dependable"; two humans appear (P19, P20). "Dismantle" holds
   best against the tasks it leaves people (P15, P19), the seat it is written from (P5, P17), and the people it acts
   on, who appear once (P20).

## What is in place

- **Nadella's texts**: five posts, the X capture with locators P1–P21, two press reports, held locally because this
  repo is public (`~/iit-playground/berthon_ethics_local/nadella/`). Paragraph map in `CORPUS.md` §1.
- **The lab's earlier work**, copied byte for byte into `sources/` (49 files): the post's lineage (facet G), the
  disclosure paradigm and v4 research (V1–V6), the word-spacing record (dxd facets A–D, F, J, K, O, W), and print
  (facet B).
- **The cards**: 219 in `../literature/cards/`, listed in `CARDS.md` with 260 facet sources that have no card.
  `python3 -I nadella/collect.py --check` from the arm directory.
- **The Spaces limitation**, paraphrased in `SOURCE.md`, verbatim in the local corpus.

## Rulings (2026-10-24)

The author's instruction, verbatim: "Use your judgement.  The goal here is to not make the same mistakes as when
literacy was growing.  Nadellas suggestions chart a course to make those same failures." Claude made the four open
calls below under that delegation; each is the author's to reverse.

1. **The thesis.** The growth of literacy offers a course of corrections and a course of failures. Word spacing
   belongs to the corrections: the page took on work the reader had carried, for readers the old script excluded.
   The failures came with mass distribution: custody of the medium by an interested party, a record kept by one
   side, disclosure in place of understanding, the burden of reading placed on the person bound, the competence
   withheld or sold as a cure, and a gate held by the few. Nadella's moves take the second course. Where one of them
   resembles the correction (controls outside the model, P11–P12), the paper concedes it and shows whom it serves.
2. **How the two transitions connect.** As two stages of one growth: spacing changed the artefact for a widening
   readership; print distributed the medium at scale, and the institutions that governed that distribution made the
   failures. Nadella writes at the print stage, the moment a medium that demands a new competence is put into
   everyone's hands, and makes the print-stage choices, not the spacing choice. The paper does not claim spacing
   spread literacy (pushback 2).
3. **Scope.** The ethics of the decision space itself (who bears the burden of understanding, who holds the record and
   the brake, who has standing), and market power as custody of the conventions. Labour governance enters where the
   design assigns work to people (the log reader, the brake holder). Training paradigms stay out, except chain-of-thought
   monitorability as it bears on P9.
4. **Home.** This arm's paper, with Nadella as its central case. That settles consolidation conflict X01 as the merge
   option: the five positions and v4's three wrongs supply the history; the insider post supplies the present.

The strength of the charge follows facet G: concede what the post gets right, and aim at the tasks it leaves people,
the seat it writes from, and the people it acts on.

The research plan is `RESEARCH_PLAN.md`.

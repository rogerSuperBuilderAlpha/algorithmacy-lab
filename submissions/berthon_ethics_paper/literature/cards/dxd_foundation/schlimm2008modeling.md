# Schlimm, D., & Neth, H. (2008). Modeling ancient and modern arithmetic practices: Addition and multiplication with Arabic and Roman numerals. In V. Sloutsky, B. Love, & K. McRae (Eds.), *Proceedings of the 30th Annual Meeting of the Cognitive Science Society* (pp. 2097–2102). Cognitive Science Society.

**Identifier:** none found (not in Crossref; author-hosted copy at the University of Göttingen psychology site, per `../references.bib`) · **Read depth:** full_text (six-page proceedings paper, author copy with the proceedings header; the printed pagination 2097–2102 is the proceedings'; reference list read) · **Source-tier:** proceedings (conference paper) · **Evidence basis:** direct_read · **Design and sample:** computational simulation, no human participants: four rule-based agents (Arabic and Roman, each for addition and multiplication), run on 1,000,000 three-number additions (x + y + z, each 1 to 100) and 10,000 two-factor multiplications (x × y, each 1 to 100) (p. 2101) · **Parties modeled:** person–artefact (one agent working on an external written display) · **Facets:** F · **Read:** 2026-10-13

## What it argues

The paper asks how much of the felt difficulty of Roman arithmetic "is based on inherent limitations of Roman numerals as opposed to our lack of familiarity" with them (p. 2097). The authors name historians (Cajori, Menninger) and cognitive scientists (Marr, Dehaene, Butterworth) who hold that Roman arithmetic, and multiplication above all, is infeasible, and they set out "to dispel this myth" (p. 2097). They cannot recruit participants equally familiar with both systems, and most details of how Romans used their numerals are lost, so they build agents (p. 2098). The agents are written in Lisp, "inspired by" ACT-R but with no memory dynamics or learning implemented (p. 2098). Each agent works on a simulated external display and is charged for elementary information processes (reading, attention shifts, memory retrieval and storage, writing, deleting), after Payne, Bettman and Johnson (p. 2098).

The Arabic addition agent needs the problem laid out in right-justified columns, one addend per row, and the authors say this "caters towards certain properties of place-value notations" (p. 2099). The Roman agent copies symbols into a "working table" with one row per symbol type, then applies simplification rules such as IIIII → V (p. 2099). The Roman agent needs no addition facts (it holds seven simplification rules where the Arabic agent holds 100 single-digit sums) and its Roman multiplication table has 49 entries against the Arabic 100 (pp. 2100–2101).

Table 2 (p. 2101; one unit is 1,000 operations) puts the cost on the external side. For additions, Arabic against Roman: reads 8,116 against 244,166 (ratio 30.08), attention shifts 16,625 against 336,413 (20.24), writes 3,637 against 18,700 (5.14); the Roman agent also makes 27,710 deletes where the Arabic agent makes none. For multiplications the ratios are smaller: reads 4.10, shifts 4.81, writes 3.52, deletes 27.70. The Roman input is about 2.6 times longer (15,030 against 5,760 symbols for additions), so single-symbol multiplications grow by "2.6² = 6.8" (p. 2101).

The authors conclude that "the Achilles heel of Roman numerals is not that they are (qualitatively) unsuitable for algorithmic usage, but their greater cost in terms of the number of necessary elementary information processes, especially those using external resources" (p. 2102). Two conditions limit the result. The comparison "depends crucially on the precise format of external inputs and the availability of interactive resources" (p. 2101); a linear input would force the Arabic agent to rewrite into columns or hold more in working memory, while the Roman agent "could remain virtually unchanged" (p. 2101). An abacus in place of the working table would cut the Roman agent's writes and deletes sharply (pp. 2101–2102). The authors list time estimates, an ACT-R re-implementation and other numeral systems as future work (p. 2102).

## Relation to the argument

**Premise P5 and the facet-F cost hypothesis (H-cost).** The paper is the one source in this batch that counts, step by step, what a notation costs a worker, and it counts on the premise the argument borrows from Larkin and Simon (1987) and Zhang and Norman (1995, p. 2097 cites both; the project has not read the latter): the same information in another form changes the work. For the paper's main claim, that a layout move can shift work between memory and the page, the result is a clean instance. The Arabic agent's advantage depends on the column layout of the page, which is a design choice about the artefact and not a property of the digits.

**Complication to "cheaper".** The source cuts against a single-axis reading. The Arabic form is cheaper in perceptual, attentional and motor steps and costlier in memory (100 addition facts, carries, intermediate sums); Roman is the reverse. "Lowering a cost" (P6) has to name which resource, and for whom. The authors state that the verdict flips with the tools at hand (abacus, fingers, linear input).

**P1 and P4 by analogy, not mechanism.** The paper overturns a received view that an old notation is "inherently" hard, by showing it is workable and expensive. That mirrors the disputed point at P1 (whether unspaced script burdened trained readers at all). It does not test any claim about reading, and the author's rulings D1 and D10 (precedent and guide, not mechanism) apply: cite it as a design precedent for the cost-accounting frame, not as evidence about word separation.

**D6, a complex of conventions.** Roman and Arabic arithmetic differ in numeral shapes, symbol count, tables, algorithms and page layout at once. The paper separates some of these (layout, table size) and shows each moves cost somewhere, which supports the author's wish to find "the critical move" among several (D6) without showing that any one is it.

**Facet check:** I found no contradiction with the facet entry in `F_parallel_moves.md`. Its summary (four agents, 1,000,000 and 10,000 problems, no human data, "precise format of external inputs", the abacus caveat) matches pp. 2098–2102. The entry gives the p. 2097 quotation and the p. 2102 quotation correctly.

## In conversation with

From the paper's own text and reference list, matched against `../references.bib`:

- `larkin1987why` (Larkin & Simon 1987): informational against computational equivalence is taken from it (p. 2098); the Roman/Arabic comparison is a worked case.
- `zhang1995representational` (Zhang & Norman 1995): cited for numeral systems as representational artifacts (pp. 2097, 2102).
- `norman1993things` (Norman 1993): cited for the claim that Roman addition is simpler than ours (p. 2097) and for tool-agent-task interaction.
- `hutchins1995cognition` (Hutchins 1995) and `kirsh1996adapting` (Kirsh 1996): cited for cognition recruiting external resources (p. 2098).
- `kirshmaglio1994distinguishing` (Kirsh & Maglio 1994): cited for people using hands and objects to arrange and count (p. 2098).

Leads not in the bib: Simon (1978) on forms of mental representation; Payne, Bettman & Johnson (1993), the source of the elementary-information-process accounting; Anderson et al. (2004) on ACT-R; Nickerson (1988), "Counting, computing, and the representation of numbers", *Human Factors*; Neth & Payne (2001) on addition as interactive problem solving.

## Caution

This is a simulation of hand-built agents, not human data: no time estimates, no errors, no learning, and ACT-R only as inspiration (pp. 2098, 2102). The counts depend on the authors' choices of algorithm, input layout and problem range, which they say favour the Arabic agent in places (p. 2101). The authors cannot say how Romans actually computed (p. 2098). Cannot be cited for anything about reading, writing systems or learners. A six-page conference paper that the authors themselves treat as a first model.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the author copy of the proceedings paper (6 pages, 2097-2102); title, authors, year match. Checked 15 quotations (two-column layout, so re-extracted without layout mode) and their pages, every figure in Table 2 quoted by the card (reads, shifts, writes, deletes, ratios, symbol counts), the 1,000,000 and 10,000 problem counts, the 49-entry and seven-rule/100-fact comparisons, and the citations to Norman 1993, Zhang and Norman 1995, Hutchins, Kirsh, Kirsh and Maglio, Larkin and Simon.

**Findings:** No issues found. The card's '2.6² = 6.8' is the PDF's superscript flattened to '2.62 = 6.8'; the meaning is the same.

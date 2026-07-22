# Hypotheses — causal emergence: what kind of evidence, and does it converge

*Committed before any corpus is harvested or coded. The question: is the literature on causal
emergence and downward causation conceptual, formal, or empirical, and does it converge on whether
macro-scale causal emergence is real? The question is descriptive-evaluative: it fixes what the field
is made of (evidence type, formalism) and whether its central claim has settled.*

This review matters to the lab's program. The lab treats a coordination form as a candidate for
irreducibility and reads Φ as a lens on whether the macro-scale whole does causal work its parts do
not. Causal emergence is the nearest formal neighbor to that move: it asks, with an explicit measure,
whether a macro description of a system carries causal power the micro description lacks. If that
literature is mostly argument and toy models, with real-system demonstrations rare and the central
claim still contested, the lab is entering an open, unsettled area rather than a closed one. The
review measures which.

## H1 — Conceptual and formal, empirical rare
- **Knowledge claim (stylized fact):** work on causal emergence and downward causation is dominated by
  conceptual argument and formal model-building; demonstrations that compute an emergence measure on a
  real measured system are the exception.
- **Operationalization:** code each source `conceptual` (argument / analogy, no measure computed),
  `formal_model` (a measure computed on a toy, simulated, or abstract system), or `empirical` (a
  measure computed on real measured data). Report the distribution.
- **Predicts:** `conceptual` + `formal_model` together are a large majority; `empirical` is a small
  minority.
- **Challenged if:** `empirical` is a plurality or more.

## H2 — Central claim contested, no convergence
- **Knowledge claim (enduring critique):** whether macro-scale causal emergence is real is disputed;
  sources split between an emergence-is-real reading and a deflationary reading (emergence is
  observer-relative, epistemic, or an artifact of the measure), with no convergence.
- **Operationalization:** code each source's `claim_direction`: `emergence_real`, `deflationary`, or
  `neutral`. A field that has converged shows one direction dominating among the sources that take a
  side; a contested field shows both well represented.
- **Predicts:** among sources taking a side, both `emergence_real` and `deflationary` hold a
  substantial share (neither below ~25%).
- **Challenged if:** one direction holds the field (the other under ~15% of side-takers), i.e. the
  question has effectively settled.

## H3 — Formal approaches fragment
- **Knowledge claim (substantive omission / critique):** the formal work does not proceed from one
  framework; it splits into information-theoretic, dynamical-systems, statistical, and other
  formalisms that develop with limited cross-citation.
- **Operationalization:** code each source's `formalism` (`information_theoretic`, `dynamical`,
  `statistical`, `other`, `na`); then, on the harvested citation graph, build the
  formalism-to-formalism citation matrix over the corpus seeds and read whether it is block-diagonal.
- **Predicts:** more than one formalism holds a real share of the formal corpus, and the citation
  matrix shows within-formalism citation exceeding cross-formalism citation.
- **Challenged if:** one formalism dominates the formal corpus, or the matrix is well connected across
  formalisms.
- **Partial-report rule:** if the citation harvest is rate-limited or returns too few resolved edges,
  H3 is reported from the coded `formalism` distribution alone (fragmentation of shares), and the
  citation-matrix half is marked partial.

## Method fixed in advance
- Corpus boundary and search: `methods.md` (substantive + procedural gates; ToolSearch academic
  search + snowball harvest).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`.
- Reliability reported (Fleiss' κ per categorical variable). Any hypothesis the data contradict is
  reported as challenged.

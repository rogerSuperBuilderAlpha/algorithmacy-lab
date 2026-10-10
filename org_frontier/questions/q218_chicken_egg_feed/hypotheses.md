# Q218 — Stage 3 hypotheses (fixed before computation)

Written and committed before any test runs. Node letters: **P** the celebrity (posts / posts again),
**F** the feed (shows the post to the audience), **A**, **B** two audience members (react / share).
Exact rules are in `methods.md`. "Whole-system verdict": triadic iff max Φ_MIP > 1e-9 over reachable
states. "Core": the major complex. A form has **no first cause** when its causal graph (the connectivity
matrix of who-reads-whom) is strongly connected: every node is influenced, directly or indirectly, by
every other. Otherwise some set of nodes is a source the rest cannot reach back to (a first cause).

Forms: BROADCAST (celebrity → each fan), CONTAGION (fans also copy each other), WOM-REACT (contagion, and
the celebrity posts again when fans react), FEED-CHRONO (non-reactive chronological feed), FEED-CHRONO-REACT
(chronological feed, celebrity reacts), FEED-ENG (engagement-ranked feed, celebrity fixed), FEED-ENG-REACT
(engagement feed, celebrity reacts to trending), FEED-ENG-COUNTS (engagement feed, fans see each other's
reactions), FEED-ENG-REACT-COUNTS (both), and two controls, CHAIN (feedforward chain P→F→A→B) and RING
(P→F→A→B→P).

## H1 — Feedforward forms have Φ = 0 (known IIT property; control)
- **Claim:** BROADCAST, FEED-CHRONO and CHAIN read dyadic with no multi-node complex (no subset of two or
  more nodes with Φ > 0). This is a direct consequence of IIT's definition (a unidirectional cut costs
  nothing) and is included to confirm the instrument reads it, not as a new finding.
- **H0:** any of the three reads triadic or has a multi-node complex.
- **Predicted outcome:** all three dyadic, no multi-node complex.

## H2 — An unmoved first mover factors the whole even around a loop
- **Claim:** CONTAGION, FEED-ENG and FEED-ENG-COUNTS read dyadic at the whole system, because the celebrity
  is a one-way source, but each has a loop core that excludes the celebrity: {A,B} for CONTAGION and
  {F,A,B} for FEED-ENG and FEED-ENG-COUNTS.
- **H0:** any reads triadic, or its core includes P or differs from the stated set.
- **Predicted outcome:** three dyadic verdicts with the stated cores.

## H3 — A celebrity who reacts to engagement closes the loop
- **Claim:** FEED-ENG-REACT and FEED-ENG-REACT-COUNTS read triadic, with all four nodes in the core.
- **H0:** either reads dyadic, or its core misses a node.
- **Predicted outcome:** both triadic, core {P,F,A,B}.

## H4 — Recurrence, not the algorithm, is what removes the first cause
- **Claim:** forms that close the loop without an engagement-reactive feed also read triadic:
  FEED-CHRONO-REACT (non-reactive feed, celebrity reacts) and WOM-REACT (no feed at all). The RING control
  reads triadic, as the atlas's rotation result predicts.
- **H0:** FEED-CHRONO-REACT or WOM-REACT reads dyadic.
- **Predicted outcome:** FEED-CHRONO-REACT, WOM-REACT and RING triadic.

## H5 — "No first cause" and Φ > 0 coincide in these forms
- **Claim:** across the eleven forms and every form in the encoding sweeps (methods.md), Φ > 0 implies a
  strongly connected causal graph in every case (expected from IIT), and a strongly connected causal graph
  implies Φ > 0 in at least 90% of cases (the empirical part). Separately, FEED-ENG-REACT stays triadic in
  at least 8 of the 10 encodings of the feed's rule.
- **H0:** some form has Φ > 0 without strong connectivity; or fewer than 90% of strongly connected forms
  have Φ > 0; or FEED-ENG-REACT is triadic in fewer than 8/10 encodings.
- **Predicted outcome:** implication holds without exception; converse ≥ 90%; FEED-ENG-REACT ≥ 8/10.

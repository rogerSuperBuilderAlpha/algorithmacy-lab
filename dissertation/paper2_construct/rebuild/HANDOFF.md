# Paper 2 rebuild — handoff / state

## Where we are
Stage 1 (research) ✓ · Stage 2 (outline) ✓ · Stage 3 computation ✓ · Stage 3 draft ✓ · Stage 4
review round 1 ✓ → round 2 re-review ✓ → round-3 corrective pass ✓. Branch `rebuild/paper-by-paper`.
Panel trajectory: 3× MAJOR-bordering-reject → (after round-2 reframe) 1 MINOR + 2 MAJOR → round-3
fixed both standing MAJOR items (the §5/§9 contradiction and the variant-A script inconsistency) by
correction. **Next: optional round-3 re-review; the one open author decision (R3's empirical-emptiness
fork); the deferred computations (geometric Φ/Φ*, ΦID synergy).** See ADVERSARIAL_REVIEW.md tail.

Draft: `DRAFT.md` (~9.7k words, 11 sections, ORM register, Nagel style — 0 first person, 0 em-dashes;
every number traceable to a `rebuild/` script; all 20 bib entries Crossref-verified).
Review: `ADVERSARIAL_REVIEW.md` (round 1: 3 hostile reviewers, all MAJOR REVISIONS, all reproduced
the numbers). New computation answering the review: `review_response.py`.

## Stage 4 corrective passes applied
- **Technical/honesty fixes** (round 1): deleted the false "Φ = EI at the MIP" identity and the
  unearned "provably"; replaced with the computed EI result (EI=2.0 bits on the exhibit where Φ=0;
  true dyad has the HIGHEST EI, 3.0). Retreated the untested geometric-Φ/Φ* robustness claim to an
  open check. "cause-effect structure" → "cause-effect power" (system measure, not the unfolded
  structure the paper drops). "validation gate" → correctness controls (a unit test, not a construct
  validation). Rule 110 "same" → "analogous". Full per-state Φ disclosure in §7.
- **Strengthen-and-narrow** (round 2, per author steer — keep the warrant, condition it): the
  "material reality / objective / analyst-independent" framing is now CONDITIONAL — objective *given
  a faithful model*, where the four-question criterion disciplines faithfulness. §5 reports the
  carving-invariance check (verdict holds across faithful re-encodings, e.g. variant B → triad at
  Φ=0.415; flips only when an encoding freezes a party (A) or loosens the determination off a
  constitutive conjunction (C)). §7 dyadic-limit verdict now derived from the rivals' published
  unit (channel/context that conveys, not commits) — kills the "circular by construction" charge.
  §7 false-dyad reframed (reading the rider is NOT sufficient; the OR-dispatch reads both and
  factors). §8 exhibit given a coordination reading (a mediator whose determination is redundant
  given the parties — a dyad that looks like a triad). §10 warrant restated in conditional form.

## Draft notes (for the review pass)
- One open competitor flagged, not computed: PID/ΦID synergy on the exhibit (§8). The strongest move
  would be to compute it; the draft flags it as the single open comparison and a limitation.
- Read-structure fraction reported as 12.5% (32/256) under the all-functions read space, stated as
  read-space-dependent (RESULTS.md §5). Qualitative claim robust either way.
- Caught during the citation pass: Oswick et al. (2011) correct DOI is 10.5465/amr.2011.59330932,
  not the amr.2009.0155 listed in RESEARCH.md. Draft uses the verified one.
- Party-partition complete-cut magnitudes (prior 2.0/1.0) were NOT re-derived in rebuild/, so the
  draft makes the over-call point qualitatively from the observed party-respecting MIPs only.

## Locked decisions
Re-derive computation from scratch (DONE) · borrowing-led spine · methods venue (ORM register) ·
operationalize Paper 1's four-question criterion · honesty posture (Φ as formal model, binary not
magnitude, no world-validation, analogy not homology, Markov/CI by construction).

## Durable inputs for the draft (all committed)
- `PLAN.md` — decisions, cross-check targets, reference assets.
- `RESEARCH.md` — Stage 1 + 1b synthesis. Key: borrowing standards (Ketokivi: evaluate the analogy
  AS an argument; analogy not homology); Φ measures MIP-irreducibility (φ=0 iff reducible),
  separable from consciousness; the cheap-test objection (not-strongly-connected ⟹ Φ=0) answered by
  the exhibit; EI/causal-emergence over-calls; Φ-family draws the same line (robust); cost moot at
  N=3; Markov/CI by construction. Citations to re-verify against Crossref before drafting the bib.
- `OUTLINE.md` — approved 11-section structure + the argumentative-role section (material reality +
  objective warrant; the dyadic constructs model Φ=0, the platform is Φ>0, so a new construct is
  required). The construct mapping (four questions → structural conditions for Φ>0) is in §3.
- `RESULTS.md` — every re-derived number + cross-check status. Use these numbers in the draft; each
  is reproducible from a `rebuild/` script.

## The re-derived computation (from scratch, depends only on PyPhi; in `rebuild/`)
- `instrument.py` — classifier + validation gate. Factoring → Φ=0; irreducible → 0.830/0.484,
  MIP {W,S,C}. EXACT match to prior.
- `worked_examples.py` — chat dyad (Φ=0); ATS sweep (AND/OR/NAND/NOR → 2.0 {W,SC}; XOR/XNOR → 0.5
  tripartition; f=W/f=C → 0 false triad); the false dyad (full triad S'=W∧C → 2.0 @(1,1,1), mean
  0.400/5, {W,SC}; dyadic model S'=W → 0; one edge S←C carries the verdict). EXACT match.
- `why_phi.py` — the exhibit W'=NOR(S,C), S'=¬W∧C, C'=NAND(W,S): 6/6 edges, strongly connected,
  Φ=0 at every reachable state; cheap connectivity + factorization tests over-call; Φ reduces.
  EXACT match.
- `sweeps.py` — eliminate-dyad (2.00/0.83/6.00/2.00/0.00, EXACT; non-monotone → binary claim only);
  read-structure (anchors exact; Φ>0 fraction re-derived 12.5% vs prior ~22% — read-space
  definition difference, documented in RESULTS.md §5, NOT an error; load-bearing claim robust).

## The one divergence (documented, honest)
Read-structure Φ>0 fraction: 12.5% (all-functions read space) vs prior ~22% (narrower space). Not a
computational error — anchors and instrument agree. Draft reports 12.5% under the fully-specified
read space and notes the fraction is read-space-dependent; the qualitative claim (reads decide the
verdict) holds either way.

## Deferred computation (optional, decide when drafting §8/§9)
- PID/ΦID synergy on the exhibit — the one open competitor from research Stage 1b. Compute, or flag.
- Party-partition complete-cut numbers — the observed MIPs (party-respecting, never the complete
  cut) already make the point; re-derive the explicit complete-cut Φ only if §6 needs the numbers.

## Next: write the draft
Nagel style (CLAUDE.md), ORM register, 11 sections per OUTLINE.md. Every number from RESULTS.md.
Re-verify all bibliography citations against Crossref before they enter the draft (the Paper 1
discipline — two fabricated citations were caught there). Then Stage 4 adversarial review.

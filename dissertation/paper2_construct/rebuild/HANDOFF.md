# Paper 2 rebuild — handoff / state

## Where we are
Stage 1 (research) ✓ · Stage 2 (outline) ✓ · Stage 3 computation ✓ · **Stage 3 draft = NEXT** ·
Stage 4 (review) pending. Branch `rebuild/paper-by-paper`.

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

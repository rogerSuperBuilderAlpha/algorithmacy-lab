# Paper 2 rebuild — re-derived results (from scratch) + cross-check against ../results.md

All values exact IIT-4.0 system Φ via PyPhi `new_big_phi.sia`, over 3-node W/S/C application-layer
Boolean systems. Fresh implementation in `rebuild/` depending only on PyPhi. Reproduce:
`~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/{instrument,worked_examples,why_phi,sweeps}.py`

**Cross-check status: every load-bearing number reproduces the prior verified result exactly. One
secondary number (the read-structure fraction) diverges for a documented, non-error reason.**

## 1. Validation gate (`instrument.py`) — EXACT MATCH
| Control | structure | re-derived | prior |
|---|---|---|---|
| Factoring | C decoupled (W'=S, S'=W, C'=C) | Φ=0.000 all states → DYAD | Φ=0.000 |
| Irreducible | each reads other two | maxΦ=0.830, meanΦ=0.484, MIP {W,S,C} → TRIAD | 0.830 / 0.484 / tripartition |

## 2. Worked examples (`worked_examples.py`) — EXACT MATCH
| Case | re-derived | prior |
|---|---|---|
| Dyadic limit (chat) | Φ=0 → DYAD | Φ=0 |
| ATS AND/OR/NAND/NOR | maxΦ=2.0, mean 0.5, MIP {W,SC} | 2.0 / 0.5 / {W,SC} |
| ATS XOR/XNOR | Φ=0.5, MIP {W,S,C} | 0.5 / tripartition |
| ATS f=W, f=C (false triad) | Φ=0 → DYAD | Φ=0 |
| False dyad — full triad (S'=W∧C) | maxΦ=2.0 @(1,1,1), mean 0.400/5, MIP {W,SC} | 2.0 / 0.400 / {W,SC} |
| False dyad — dyadic model (S'=W) | Φ=0 → DYAD | Φ=0 |

## 3. The why-Φ exhibit (`why_phi.py`) — EXACT MATCH
`W'=NOR(S,C), S'=¬W∧C, C'=NAND(W,S)`: 6/6 off-diagonal edges, no constant node, strongly
connected, yet **Φ=0 at every reachable state** (states (0,0,0),(0,0,1),(1,0,1),(0,1,1)). The two
cheap structural tests over-call it (connectivity → TRIAD; factorization → TRIAD); Φ over the MIP →
DYAD (correct). Matches ../results.md §5.

## 4. Eliminate-the-dyad sweep (`sweeps.py`) — EXACT MATCH
S'=W∧C fixed; vary the direct W–C channel:
| channel | encoding | re-derived maxΦ | prior |
|---|---|---|---|
| none | W'=S, C'=S | 2.00 | 2.00 |
| disjunctive | W'=S∨C, C'=S∨W | 0.83 | 0.83 |
| conjunctive | W'=S∧C, C'=S∧W | **6.00** | 6.00 |
| parity | W'=S⊕C, C'=S⊕W | 2.00 | 2.00 |
| full bypass | W'=C, C'=W | 0.00 | 0.00 |
Endpoints robust (no channel → triad; full bypass → dyad); middle non-monotone (0.83 vs 6.00). The
"design the dyad out" claim is stated at the **binary level only**; no magnitude gradient.

## 5. Read-structure sweep (`sweeps.py`) — QUALITATIVE MATCH; fraction DIVERGES (documented)
S'=W∧C fixed; sweep the strict-mediation reads (W'=g(W,S), C'=h(C,S), no W–C edge).
- **Anchors reproduce exactly:** pure bottleneck (W'=S, C'=S) → maxΦ=2.00; realistic feedback
  (W'=¬S, C'=S∨C) → maxΦ=0.00.
- **Fraction with Φ>0: re-derived 12.5% (32/256); prior reported ~22%.** This is a read-space
  definition difference, not a computational error (the anchors and the instrument agree). The
  re-derivation sweeps all 16 Boolean functions per node, including constants and own-only reads,
  which enlarges the denominator with trivially-reducible pairs and lowers the percentage; the prior
  used a narrower admissible-read set. **The load-bearing claim is robust either way:** only a
  minority of strict-mediation reads preserve the triad verdict, and the realistic-feedback reads
  collapse it — so the reads decide the verdict, not just the determination. The draft will report
  the re-derived 12.5% under the fully-specified all-functions read space and note the fraction is
  read-space-dependent.

## Open / deferred computation
- **Party-partition vs MIP:** not separately re-derived here. The observed MIPs are party-respecting
  (e.g. {W,SC}, {W,S,C}) — never the complete {W}{S}{C} cut — which already shows the test is Φ over
  the MIP, not the complete cut. The prior result (the complete cut over-calls: chat dyad → 2.0,
  dyadic model → 1.0) can be re-derived by evaluating the specific partition if the draft needs the
  numbers; the qualitative point stands from the observed MIPs.
- **PID / ΦID synergy on the exhibit:** the one open competitor (research Stage 1b). To compute on
  the exhibit during drafting, or flag as the single open comparison.

## Honesty posture (carried, verified by re-derivation)
Φ adopted as a formal model. Binary verdict, not magnitude (the eliminate-dyad non-monotonicity
proves the magnitude is not a scale). No world-validation. The exhibit, not an aggregate, is the
"why Φ" headline. Markov/CI hold by construction (the TPM is built from the specified mechanism).

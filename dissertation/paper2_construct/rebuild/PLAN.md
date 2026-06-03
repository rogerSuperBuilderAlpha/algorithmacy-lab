# Paper 2 rebuild — plan and locked ground truth

From-scratch rebuild of Paper 2, same staged process as Paper 1: research → outline → draft →
review, with a checkpoint between stages. Decisions (locked): **re-derive the computation from
scratch**, aligned to Paper 1's updated concepts; **borrowing-led** spine; **methods venue**
(Organizational Research Methods register). Style: repo CLAUDE.md (Nagel plain, no first person).

**Re-derivation, done honestly.** The instrument and experiments are re-implemented and re-run from
zero, designed around Paper 1's reframed concepts (below), NOT copied. But every re-derived number
is cross-checked against the prior validated results (`../results.md`); any divergence is
investigated and explained, not silently accepted. The prior results are a regression test on the
re-derivation, not a source to quote. This catches errors in either direction.

**Align to Paper 1's updates.** The model operationalizes Paper 1's provisional four-question
criterion (assign-vs-choose, commit-vs-carry, kept-apart-vs-route-around, interest-vs-neutral) as
the structural conditions Φ tests. It reflects: recognition-not-invention (Φ is a borrowed tool to
make the recognition rigorous, not a discovery); the irreducibility grounding in cross-side
externalities (Paper 1 §3.8), with Peirce as analogy not proof; and the moderated/mediated contrast
sharpened against the service triangle (a legible human mediator, moderated) vs the opaque
algorithmic constitutive mediator (mediated triad).

## The spine (fixed)
Paper 1 names algorithmacy, the competency the mediated triad demands, and gives a provisional
four-question criterion for telling a moderated dyad from a mediated triad (assign-vs-choose;
commit-vs-carry; kept-apart-vs-route-around; interest-vs-neutral), deferring the rigorous
procedure. **Paper 2 is that rigorous procedure.** A coordination form is a mediated triad when
its application-layer cause-effect structure is irreducible, and a moderated dyad when it factors.
Integrated information theory's Φ, a formal tool built in another field, measures irreducibility.
Φ over the minimum-information partition (MIP) = 0 → moderated dyad (navigable with literacy);
Φ > 0 → mediated triad (demands algorithmacy). Paper 2 builds the instrument. Paper 3 calibrates it.

## Cross-check targets (prior verified results — the re-derivation should reproduce these; explain any divergence)
## (from results.md — exact IIT-4.0 Φ via proxy_audit.exact_phi / PyPhi new_big_phi.sia)
- **Classifier:** Φ over the MIP = 0 (factors along party lines) vs > 0 (irreducible across W,S,C).
  The BINARY verdict is the claim, not the magnitude.
- **Validation gate:** factoring control (C decoupled) → Φ=0; irreducible control (each reads the
  other two) → Φ up to 0.83. Clean separation. Run before any worked example.
- **Worked cases:** chat-with-LLM dyad → Φ=0; ATS triad (AND/OR/NAND/NOR commit) → Φ=2.0;
  XOR/XNOR → 0.5 (full tripartition); party-ignoring mediator (f=W or f=C) → Φ=0 (false triad).
- **The false dyad made computable (the killer case):** rideshare presents as worker+app, but is
  causally a 3-party system. Identical except one edge S←C (rider constitutive of dispatch):
  include it → Φ=2.0 (triad the driver cannot see); drop it → Φ=0 (dyad). The dyad/triad verdict
  is carried by that single edge. A dyadic construct scores it 0 by omitting C; the case IS a triad.
- **Eliminate-the-dyad:** stated at the BINARY level only. Endpoints robust (no direct W–C channel →
  triad; full bypass → dyad). The middle is encoding-dependent (0.83 vs 6.00), so the old
  "monotone decline" framing is DROPPED. Political-economy reading kept binary: removing the direct
  channel keeps the form classified a triad, so a platform has a structural reason to design it out.
- **Reads decide the verdict, not just the determination:** only 22% of strict-mediation read pairs
  keep Φ>0; the realistic-feedback reads collapse it to 0. Stated in the open, not hidden.
- **Party-partition vs MIP — resolved:** the complete {W}{S}{C} cut over-calls (positive even for
  dyads). The test is Φ over the MIP = 0, where the MIP is party-respecting (e.g. {W,SC}).
- **Why Φ, not a cheap test — the robust claim is an EXHIBIT, not an aggregate:**
  `W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S)` — all six edges, strongly connected, no constants — has
  exact Φ=0 at every reachable state. Every connectivity / conditional-independence test calls it
  triadic; the MIP machinery reduces it. Aggregate counts are comparator-dependent (89.8% / 8-reverse
  for the fair reachable-only comparator) and are NOT the headline. "Φ strictly stronger / 0-reverse"
  was an artifact of a weak comparator — withdrawn.

## Honesty posture (non-negotiable; from the prior recast)
- Φ is ADOPTED AS A FORMAL MODEL — a modeling choice, not a claimed identity with consciousness.
- The paper claims NO validation against the world. The outcome anchor (Φ as a difficulty scale) is
  cut here and handed to Paper 3.
- The contested IIT-as-consciousness claims are not the imported ones; the import is only the
  irreducibility measure.
- State-alphabet dependence is the entire empirical commitment; the individuation rule is
  pre-registered before any computation.

## Reference assets (a prior implementation to cross-check against, NOT to copy)
- Scripts: `../phi_instrument.py`, `../worked_examples.py`, `../phi_vs_separability.py`,
  `../dynamical_comparator.py`, `../eliminate_dyad_sweep.py`, `../party_partition.py`,
  `../read_structure_sweep.py` (venv: `~/iit-playground/venv-4.0/bin/python`). Re-implement fresh in
  `rebuild/`; compare outputs to these as a regression test.
- Results to reproduce: `../results.md` + `../results_*.txt`. Prior research notes (superseded, for
  reference only): `../research/{borrowing_tradition,methods_paper_methodology,platform_triad_grounding,technical_background}.md`.
- Prior (superseded) draft: `../draft/DRAFT.md`; prior `../ARGUMENT.md`, `../OUTLINE.md`, `../state_alphabet.md`.

## Connection to the reframed Paper 1
Paper 1's "recognition, not invention" thesis pairs with Paper 2's borrowing: Paper 1 recognized a
competency the old structure demanded; Paper 2 borrows a formal tool to make the recognition
rigorous. Paper 1's provisional four-question criterion → Paper 2's Φ-over-the-MIP test. Paper 1's
"a worker may sit inside a mediated triad she cannot see" → Paper 2's false dyad, made computable.

## Stages
1. Research (fresh, blank-slate, fact-checked): is Φ/IIT the right instrument for classifying
   coordination irreducibility? What are the alternatives (the cheap tests) and why is Φ warranted?
   The org-theory tradition of borrowing formal models. Construct/measure-validity standards for an
   imported formalism. Test the thesis, don't confirm it. [CHECKPOINT]
2. Outline (the model design + the experiments to run + section structure; approved at [CHECKPOINT]).
3. Draft: re-derive the computation from scratch in `rebuild/` (re-implement the instrument, design
   experiments around Paper 1's four-question criterion, run them), cross-check every number against
   `../results.md` and explain divergence, then write the paper (Nagel style, ORM register; every
   number traceable to a committed `rebuild/` artifact). [CHECKPOINT]
4. Review (adversarial panel, as Paper 1).

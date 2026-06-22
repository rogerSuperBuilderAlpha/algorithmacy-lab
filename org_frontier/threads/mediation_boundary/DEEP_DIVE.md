# The structure of the irreducibility boundary — twenty steps deep

Q3 from [`QUESTIONS.md`](QUESTIONS.md), taken twenty steps deep. Each step's question is drawn from the
previous step's result. The starting point is the canonical strict-mediated triad: the worker reads the
system, the counterpart reads the system, and the system's next state is a determination of both. The
chain varies that determination and the structure around it, and every number reproduces from
[`chain.py`](chain.py). The arc is a clean law, its boundary, and its limit.

## The chain

**1 — The baseline.** Question: what does the canonical committing triad measure? The system as a
conjunction of both parties, S = W ∧ C, is triadic at Φ = 2.0, core W-S-C. → What happens if the gate is
weakened?

**2 — Weakened gates.** Question: does the gate type matter? S = W ∨ C gives Φ = 2.0; S = NAND gives
2.0; S = W ⊕ C (parity) gives only 0.5. Parity binds, but weakly. → Why is parity so much weaker, and
which functions fail outright?

**3 — Reads-both is not enough.** Question: does reading both parties suffice? S = W ∧ ¬C reads both, yet
factors to a dyad at Φ = 0, and the negated party leaves the core. → What separates the functions that
bind from the ones that read both and factor?

**4 — The co-monotonicity rule.** Question: is the difference the *direction* of dependence? Both-increasing
(AND, OR) and both-decreasing (NAND, NOR) all give Φ = 2.0. Every mixed-direction function (W ∧ ¬C,
¬W ∧ C, W ∨ ¬C) factors to Φ = 0. Parity, non-unate, binds weakly at 0.5. The mediator must depend on
both parties in the same monotone direction. → Where does this difference live, since the topology is the
same?

**5 — Invisible to topology.** Question: do these forms differ in connectivity or reachable states?
S = W ∧ C, S = W ∧ ¬C, and S = W ⊕ C have identical connectivity matrices and identical reachable states,
yet Φ of 2.0, 0.0, and 0.5. The split is in the cause-effect structure alone, which only Φ reads, not in
any cheap structural or dynamical proxy. → What does Φ's own cut, the MIP, see that the others do not?

**6 — Two kinds of irreducible.** Question: what partition does the MIP cut? The co-monotone form is
irreducible against a bipartition, MIP {W, S-C}, Φ = 2.0. Parity is irreducible only against the full
tripartition {W, S, C}, Φ = 0.5. There are two kinds of irreducible triad: bipartition-irreducible
(strong) and only-tripartition-irreducible (weak). → Is the co-monotone law a property of the mediator,
robust to the parties' own reads?

**7 — Robust to downstream negation.** Question: does the rule survive the parties reading the mediator
inversely? With W and C reading ¬S, the co-monotone form still gives Φ = 2.0 and the mixed form still
factors. The rule is about the mediator's function, not the downstream sign. → Does parity's weak value
also survive?

**8 — Parity's value is stable.** Question: is parity's 0.5 fragile? Under downstream negation it holds at
0.5. Weak but stable. → What happens to the boundary when a direct channel between the parties is added?

**9 — The back-channel erodes.** Question: does a worker-counterpart back-channel destroy irreducibility
at a threshold or gradually? A one-way back-channel drops Φ from 2.0 to 1.0; a symmetric one to 0.83. The
erosion is gradual, and the core migrates toward the back-channel pair. → Does the co-monotone law extend
to more parties?

**10 — One mixed input collapses four.** Question: at four parties, must every party be read
co-monotonically? S = W ∧ C ∧ D gives Φ = 3.0, core W-S-C-D. A single mixed input, S = W ∧ C ∧ ¬D,
collapses the whole to Φ = 0. Co-monotonicity is required of every party at once. → Is co-monotonicity
also sufficient at four parties?

**11 — Substitutability overrides.** Question: does a co-monotone but pooled gate bind? S = W ∧ (C ∨ D)
is co-monotone, increasing in every party, yet factors to Φ = 0, because C and D are substitutable. The
AND-versus-OR choice at four parties is the substitutability distinction, and substitutability overrides
co-monotonicity. → Does parity also weaken with more parties?

**12 — Parity thins with parties.** Question: does three-way parity stay weakly irreducible? S = W ⊕ C ⊕ D
gives Φ = 0.25, triadic and thinner still. → Does depth obey the same law?

**13 — One mixed gate breaks a chain.** Question: does mediation depth preserve irreducibility under any
gate? A chain of conjunctive gates stays triadic at Φ = 2.0. A single mixed gate inside the chain
collapses it to Φ = 0. Depth preserves irreducibility only when every gate is co-monotone. → Is the strong
co-monotone form actually the robust one?

**14 — The robustness reversal.** Question: which form survives perturbation? Of the single-bit
perturbations to its transition table, the co-monotone form (Φ = 2.0) has its verdict flipped by 21%,
while parity (Φ = 0.5) is flipped by none. Parity has a small value but a robust verdict; the co-monotone
form has a large value and a fragile one. This reconciles the corpus result that parity supports
irreducibility most readily with the value result that parity is weak: they are two different axes,
magnitude and verdict-stability. → Is the rule about negation, or about mixed direction specifically?

**15 — Mixedness, not negation.** Question: does negating an input always break it? S = ¬W ∧ ¬C, both
negated, is co-monotone-decreasing and binds fully at Φ = 2.0. The rule is about mixed direction, not the
presence of a negation. → Does a threshold gate between AND and OR bind?

**16 — Majority factors.** Question: does a majority gate, monotone-increasing in all, bind? S =
majority(W, C, D) factors to Φ = 0 with an empty core. Majority is substitutable, any two of three
suffice, so it falls on the conduit side, between the all-required AND and the any-one OR. → What does the
law predict for a real governance gate?

**17 — The governance prediction.** Question: does the sign of a merge condition matter? A gate of positive
conditions, merge = opened ∧ approved, is co-monotone and binds at Φ = 2.0. A gate with a veto, merge =
opened ∧ ¬blocked, is mixed and factors at Φ = 0, excluding the blocker. The real merge gate of v9, opened
∧ approved ∧ merged, is co-monotone of positive conditions, which is why it measured Φ = 2.0. A
block-by-veto governance would read as a different structure. → Does the law hold across the whole space
of two-input gates?

**18 — The population test.** Question: does the dependence type fully decide the verdict in the canonical
config? Across all sixteen two-input gates: co-monotone 4/4 triadic at mean Φ 2.0, mixed 0/4, parity 2/2
at mean Φ 0.5, one-input and constant 0/6. The type decides the verdict exactly. → Which party leaves the
core when a gate is mixed?

**19 — The against-the-grain party.** Question: who is excluded? S = ¬W ∧ C leaves a core of S-C, dropping
W; S = W ∧ ¬C leaves W-S, dropping C. The party the mediator reads against the grain, in the direction
opposite to the others, is the one excluded from the core. This is the mechanism behind a proposer
dropping out under an adverse gate. → Does the co-monotone law hold once the parties' reads are arbitrary
rather than faithful?

**20 — The limit of the law.** Question: does the mediator's dependence type predict the verdict under
random downstream reads? It does not. Across random reads, the co-monotone mediator is triadic 16% of the
time, the mixed mediator 11%, and the parity mediator 27%. The clean law of steps 1 through 18 holds in
the configuration where both parties faithfully track the mediator. When the downstream reads are
scrambled, the mediator's co-monotonicity loses its grip, and parity, the verdict-robust type from step
14, becomes the best predictor. Co-monotonicity is the law of the *live* mediated triad.

## The boundary map

The deep dive characterizes the boundary, and the shape has three parts.

The mediator's determination decides the verdict, in the configuration that matters. A mediator that
depends on every party in the same monotone direction binds them into a strong, bipartition-irreducible
whole (Φ = 2 at three nodes, 3 at four). A mediator that reads one party against the grain factors the
whole and excludes that party. A parity mediator binds weakly, only against the full atomization. This
holds exactly across the sixteen gates and at four parties, and the split is invisible to connectivity and
reachability, living in the cause-effect structure that exact Φ computes.

Three things override or qualify it. Substitutability collapses irreducibility even under co-monotonicity,
which is why all-required AND binds and pooled OR or majority does not. The strong co-monotone value is
fragile to perturbation while the weak parity verdict is robust, so magnitude and verdict-stability are
different measures of how far a form sits from the boundary. And the whole law depends on liveness: it
holds when the parties faithfully read the mediator and dissolves when their reads are arbitrary, which
ties the mediator's contribution to the downstream-reads condition the eight structural findings already
named.

## Connections

The chain answers parts of several of the ten questions. Q9, asymmetric reads, is answered by the
co-monotonicity rule and the against-the-grain exclusion. Q6, the back-channel, erodes gradually (step 9).
Q7, partial substitutability, is the majority result (step 16). Q2, the weakest commit, is the boundary
between AND and majority. Q4, distance to dyad, splits into value and verdict-robustness (step 14). The
governance prediction (step 17) is a new, testable claim for the field arm: approval-by-positive-condition
gates constitute a triad, block-by-veto gates do not bind the blocker. It connects to the real merge gate
of [v9](../../recurrence/event_series/) and to the substitutability and quorum threads
([`substitutability`](../substitutability/THREAD.md), [`quorum`](../quorum/THREAD.md)).

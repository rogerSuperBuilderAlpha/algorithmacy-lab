# Formal-fidelity review (round 2) — Post 3, "The Real Middle Term"

Reviewer lens: integrated information theory (IIT 4.0), network/brokerage theory, formal coordination
models. Every numeric and structural receipt was re-derived from the lab sources: `corpus/results/population.csv`
(re-run of the value distribution), `corpus/forms_library.py`, `corpus/FINDINGS.md`, `classifier/FINDINGS.md`,
`org_frontier/STRUCTURAL_FINDINGS.md`, `multiparty/chains.py` + `multiparty/results/chains.csv`,
`recurrence/iit_experiments.py` (E3), and `questions/q213_contingent_irreducibility/FINDINGS.md`. This is a
v4 review: the prior formal_specialist.md (v3) is in the sibling `post3_reviews/`, and I do not re-report items
v4 already closed. I confirm the closures where they bear on my findings and then go after what remains.

---

## 1. Verdict and the single most important fix

**Verdict: accept with minor revisions.** This is a materially stronger draft than v3. Every computed receipt
in the paper is faithful to the repo — I re-ran the population census and it matches to the form. The v3
panel's two load-bearing defects are genuinely fixed: the partition/removal conflation is gone (the three
operations are named cleanly in "Necessary Middles"), and the solar-system verdict-claim is decomputed to a
well-posed-but-unrun question. Both series guards hold. The fixes that remain are local and do not threaten
the bridge.

**The single most important fix — a live tension the paper states but does not resolve.** The minimal-pair
sentence (lines 211–214) reads Φ = 2.0 as *both* an extremal magnitude and a non-magnitude in one breath:

> "...at Φ = 2.0 against the relay's 0.0 — the largest value any form in the family attains, though the lab
> reads Φ as a verdict rather than a scale, and so do I."

If Φ is a verdict and not a scale, then "the largest value any form attains" is doing scale-work the same
clause disavows. The number 2.0 versus 0.0 carries exactly the information "integrates versus factors" carries,
no more — so "largest value" adds nothing the verdict needs and quietly implies a ranking (this integrator is
*more* integrated than a weaker one). The repo makes the trap concrete: the 256-form family attains **three**
Φ values, not two — 232 forms at 0.0, **eight at 0.5**, sixteen at 2.0 — and the eight forms at 0.5 are triadic
by the verdict reading. A referee who pulls `population.csv` sees eight integrators the paper never mentions,
and asks why the 2.0 form is privileged as "the" integrator. The answer is the verdict reading, which is
exactly why the "largest value" clause is self-undermining. Cut it. The minimal pair's force is 0 versus >0.
(Exact rewrite in §3, R-A.) This is the top fix because it is the one place the paper cites the register the
lab retired, and because it touches the series guard: reading Φ as a verdict is the committed position, so the
magnitude flourish should go, not be flagged and kept.

---

## 2. Step 0 — Register (two lines)

First-person Substack philosophy essay, third of nine: a bridge argument that carries computed receipts, Nagel-
plain in ambition, APA citations, deliberately voiced ("I," "my criterion," "the lab"). I hold it to the global
house-style invariants (named agents, claim-first, verified numbers, antithesis budget, no performed candor)
*inside* that essay register — not the repo's no-first-person dissertation rule, which does not govern this venue.

---

## 3. Section by section — exact quotes and exact rewrites in the author's voice

### 3.1 "The Receipts" — the verdict/scale tension (lines 211–214). TOP FIX.

Quoted above. The problem is the "largest value" clause plus the unmentioned Φ = 0.5 band.

**R-A (minimal, preferred).** Delete the offending clause and let the verdict carry it:

> "...and the test reads the form as triadic, all three parties in one irreducible core, at Φ = 2.0 where the
> relay factored to a dyad. The lab reads Φ as a verdict rather than a scale, and so do I: what separates the
> two middles is that one form integrates and the other does not."

**R-A′ (if the author wants to keep the numbers vivid and pre-empt the referee who finds the 0.5 band).**

> "...at Φ = 2.0 where the relay read 0.0. The lab reads Φ as a verdict rather than a scale, and so do I: the
> load-bearing fact is that one form integrates and the other does not. Eight other forms in the family
> integrate at a lower magnitude and read triadic all the same — the census counts integrators, not degrees."

Either version dissolves the tension. R-A′ has the advantage of turning the hidden 0.5 band from a liability
into a demonstration of the verdict reading.

### 3.2 The flagship term names two different things — "partition-necessary middle" vs. "the final form of the integrator criterion." (Lines 325–326, 331, 371, 380.)

This is the item the v3 panel flagged as *the one thing only the author can supply*: the frozen definition of
the coined middle for Papers 4–9. v4 made real progress — it commits a definition of the refined criterion —
but it left two labels whose extensions differ and never maps them.

- Line 325: "The necessary middle is the one that passes both tests: inside the core of the intact whole, and
  still there when the bypass opens." → **necessary middle = partition-core-membership ∧ bypass-survival**
  (the conjunction).
- Line 331: "the final form of the integrator criterion is not bare core membership but core membership that
  survives the counterfactual." → **the criterion's final form = the conjunction.**
- Line 371: "Hegel's rational middle and my *partition-necessary middle* are not the same middle."
- Line 380: "Whether it is *partition-necessary* in mine is a question no one has computed" (of the solar
  system — here "partition-necessary" plainly means the partition property alone, "would a cut cost anything").

So "partition-necessary middle" names the partition half, while "necessary middle" / "the final form of the
integrator criterion" names the conjunction that *also* requires surviving the bypass. The paper's own headline
concept is therefore explicitly **not** its stated final criterion, and the two sit in adjacent sections
(371 vs. 331) under near-identical names. Papers 4–9 inherit this ambiguity: is the program's middle the
partition property, or partition-plus-bypass?

The removal conflation the prior panel caught is gone — this is a subtler, name/definition split, not a wrong
operation. Only the author can pick the canonical term, but the paper should state the map once. Suggested
reconciliation (author's voice), to insert at the end of the "Necessary Middles" section or in "Two Middles":

> "Two words, kept apart from here on. *Integrator* names what the partition test alone certifies: the middle
> inside the core no cut can factor. *Necessary middle* adds the second operation — an integrator whose seat
> survives the bypass. This paper's receipts are about the first; Paper 2's held case is why the program's
> final criterion is the second. Where I write 'partition-necessary,' I mean the partition property alone."

Then change line 371's "my partition-necessary middle" to "my integrator" (or keep "partition-necessary" now
that it is defined) and the split stops being a trap.

### 3.3 The census sentence — arithmetic is right, denominator is right, one word of provenance is owed. (Lines 202–204.)

> "The lab enumerated the complete family of three-node Boolean forms with a mediator strictly in the middle —
> no direct edge between the outer parties, 256 forms in all — and ran the exact partition test on each.
> Twenty-four of the 256 read triadic: 9.4 percent."

Checked and true. `population.py` enumerates `W' = f_W(S)`, `C' = f_C(S)`, `S' = f_S(W,C)` = 4 × 16 × 4 = 256;
my re-run of `population.csv` returns exactly 24 forms with Φ > 0; 24/256 = 9.375%, which rounds to 9.4% (the
repo reports 9.4% in both `corpus/FINDINGS.md` and `STRUCTURAL_FINDINGS.md`). No change needed to the numbers.
One precision note, not a required edit: "no direct edge between the outer parties" is accurate but slightly
under-describes the constraint — the lab's family also fixes that each outer party reads *only* the mediator
(`W' = f_W(S)`, not `f_W(S,W)`), which is why the count is exactly 256 rather than larger. A referee may ask
"why 256?"; a five-word gloss ("each end reads only the middle") pre-empts it. Optional.

### 3.4 "The Move the Resemblance Does Not License" — the gravitation/corpus claim is technically correct. (Lines 266–269, 379–382.)

> "...such a system could not even enter the corpus, whose defining constraint is that the outer parties share
> no direct edge, while gravitation is all-to-all..."

Correct as stated. The corpus's strict-mediation constraint is precisely "no direct W–C edge," and an N-body
gravitating system has direct pairwise attraction between every pair, so it violates strict mediation and
cannot be a member. The claim is well-formed and I could not fault it. Keep. (This section is the strongest in
the paper; see §6.)

### 3.5 Three operations — clean. (Lines 319–326.) No change; confirming the v3 repair landed.

> "Three operations, and this section needs them kept apart. The partition test cuts dependencies in the intact
> system and asks what any cut destroys; it defines integration, and it removes no one. The bypass
> counterfactual restores a forbidden direct tie and asks who keeps their seat in the core... And removal... is
> the world's own rough version of the second operation, not the first."

This is exactly right and matches q213's actual operation (restore the forbidden edge, recompute, read who
keeps the seat). The partition-removes-nothing / bypass-restores-an-edge / removal-is-the-crude-world-version
distinction is now stated once, cleanly, and the opening vignette is correctly re-cast as a bypass story
(line 324). Nothing to fix. I flag it only to record that the panel's central v3 defect is closed.

### 3.6 q213 car dealer — faithful; one cross-reference for the author to confirm. (Lines 328–332, 336.)

> "Paper 2 worked the held case: a relay can sit in the core of an integrated configuration for as long as a
> constraint forbids the parties to bypass it — the car dealer of the lab's q213 study, whose entire
> integration collapsed the moment the forbidden maker–buyer tie was restored."

The q213 receipt is exact. `q213/FINDINGS.md` H3: lifting the franchise law (restoring the maker–buyer tie)
drops the dealer from the core, Φ_MIP falls 2.0 → 0.0, contingency margin 2.0 = "its entire integration." The
paper even reuses the source phrase "entire integration." Match. Two notes: (i) the car dealer is q213's worked
case, and the paper correctly attributes it ("of the lab's q213 study") — but the sentence bundles it under
"Paper 2 worked the held case," which a reader may take as *Paper 2's* car dealer. Post 2 is "Master and Slave
as a Held Binding," and line 336 confirms Paper 2's own worked case is the master, not the dealer. The sentence
is defensible (the dealer is offered as an instance of the held-case *principle* Paper 2 works), but a comma-
level clarification would remove the misread: "Paper 2 worked the held case; the lab's q213 study computes it —
the car dealer, whose entire integration collapsed...". (ii) Confirm against Post 2's text that Post 2 actually
frames the master as a held/contingent binding that collapses when the compulsion lifts; I verified q213 owns
the dealer, but I did not audit Post 2's prose.

### 3.7 Read-functions receipt and the Stein card — faithful and well-deployed. (Lines 216–222, 300–308.)

> "a mediator that fails to read both parties is never triadic, and one that does read both is triadic only 15
> percent of the time"

Both halves check exactly against `population.csv`: P(triadic | mediator reads both) = 24/160 = **15.0%**;
P(triadic | does not read both) = 0/96 = **0.0%**. The identical-wiring twin (`ats_feedback_factors`: same
strict mediation, mediator reads both, still factors to 0 along {W,S}|{C}) is faithful to `corpus/FINDINGS.md`,
and the paper now correctly softens "identical wiring" to "the same strict-mediation wiring between the parties"
(line 217) and rests the general claim on the population conditional — both v3 repairs adopted. The Stein
section's use of this as "Stein's priority thesis reproduced inside the causal register" (line 302) is the best
version of that argument and is now made. No change.

### 3.8 Chains — faithful. (Lines 223–227.)

> "Relay chains of two, three, and four nodes all factor to zero, while a chain whose every middle commits
> jointly on its two neighbors stays triadic at Φ = 2.0 from three nodes to six."

Checked against source. E3 (`recurrence/iit_experiments.py`) runs feedforward relay chains at n = 2, 3, 4 and
prints "carry no integrated information" (Φ = 0) — the "nodes" (not "links") fix from v3 is now correct. The
committing chain (`multiparty/chains.py`, `Sj' = S_{j-1} ∧ S_{j+1}`) returns Φ = 2.0 at n = 3, 4, 5, 6 in
`chains.csv` — "from three nodes to six" is exact. The survival is correctly credited to the committing, not to
feedback (line 226: "not the loop as such — the twin above had feedback and factored — but the committing,
repeated at every station"). No change.

### 3.9 IIT 4.0 vs 3.0 citation — now correct; one nomenclature note for the journal version. (Line 230.)

> "exact values under the current formulation of integrated information theory (Albantakis et al., 2023; the
> lineage runs to Oizumi et al., 2014...)"

The v3 mis-citation (crediting the 3.0 paper for 4.0 receipts) is fixed: every lab source computes exact
IIT-4.0 Φ, and Albantakis et al. (2023) is IIT 4.0. Correct, and the Oizumi 2014 lineage credit is appropriate.
**One precision note, low priority, for journal submission not the post:** in strict IIT-4.0 nomenclature the
whole-system quantity minimized over the MIP is *system integrated information* φ_s, while "big Phi" (Φ) is
reserved for the structure integrated information of the maximal complex (the summed φ over distinctions and
relations). The lab writes "Φ_MIP" for the system-level MIP value throughout, and the essay inherits that
usage, so "Φ = 2.0" here is really φ_s = 2.0 in 4.0 terms. This is a convention the whole repo shares, not an
error introduced by the paper, and it need not touch the Substack post. Flag it so the author knows to say
"system integrated information over the MIP" once, if a formal IIT reader is in the journal audience.

### 3.10 Register items (minor).

- **"rung" ×12.** The v3 review asked to thin the ladder metaphor to ~7; v4 leaned *harder* into it (the
  Mitteilung-arc section is built on the ladder), so the count went up, not down. The metaphor earns its keep
  structurally, but 12 is a drumbeat — three land in lines 264–272 alone. Thin to roughly eight. Not blocking.
- **em-dashes.** High for the register (81 across the whole file, though many are in the delete-before-posting
  apparatus). The construct-naming and appositive dashes are house-legal; a light pass on the body's paired-dash
  asides would help. Not blocking.
- **"in the open" ×0** — the v3 tic is fully purged. Good.
- **Antithesis budget:** ", not" ×18 / "rather than" ×3 across ~5,600 body words is inside tolerance for a
  paper whose *subject* is a two-sided contrast (conduit vs. integrator); most instances are load-bearing.

---

## 4. Every receipt claim vs. what the repo says

| # | Paper's claim (line) | Repo source | Repo says | Verdict |
|---|---|---|---|---|
| 1 | 256 strict-mediation 3-node Boolean forms (203) | `corpus/population.py`, `population.csv` | 4×16×4 = 256 forms enumerated | **MATCH** |
| 2 | 24 read triadic (203) | `population.csv` (re-run) | 24 forms with Φ>0 (232 at 0.0, 8 at 0.5, 16 at 2.0) | **MATCH** |
| 3 | = 9.4 percent (204) | `corpus/FINDINGS.md`, `STRUCTURAL_FINDINGS.md` | 24/256 = 9.375% → repo reports 9.4% | **MATCH** (rounding correct) |
| 4 | Relay mediator → Φ = 0.0, dyad; "S relays W to C with no joint determination" (208–210) | `forms_library.py` (`pure_relay`), `corpus/FINDINGS.md` | pure_relay dyadic Φ=0.00; rationale quoted verbatim | **MATCH** |
| 5 | Joint-commit mediator "forwards iff resume-signal AND manager-profile" → Φ = 2.0 (211–212) | `forms_library.py` (`ats_strict_bottleneck`) | rationale quoted verbatim; triadic Φ=2.00 | **MATCH** |
| 6 | "all three parties in one irreducible core" (212) | `classifier/FINDINGS.md`, q213 H1 | triadic MIP cut {W,SC}; whole triad is the complex | **MATCH** (see caveat below) |
| 7 | Φ = 2.0 is "the largest value any form in the family attains" (212–213) | `population.csv` (re-run) | max Φ in family = 2.0 | **MATCH** (but see §1 — the *use* is the problem, not the fact) |
| 8 | Same strict-mediation wiring can factor to 0; read functions decide (216–219) | `corpus/FINDINGS.md` (`ats_feedback_factors`) | strict mediation + mediator reads both, yet Φ=0 along {W,S}|{C} | **MATCH** |
| 9 | Mediator failing to read both is never triadic (0%) (221) | `population.csv` | P(triadic \| not reads both) = 0/96 = 0.0% | **MATCH** |
| 10 | Reads both → triadic only 15% of the time (221–222) | `population.csv`, `corpus/FINDINGS.md` | P(triadic \| reads both) = 24/160 = 15.0% | **MATCH** |
| 11 | Relay chains of 2, 3, 4 nodes all factor to 0 (223–224) | `recurrence/iit_experiments.py` E3 | n=2,3,4 feedforward chains "carry no integrated information" | **MATCH** |
| 12 | Committing chain triadic Φ = 2.0 from 3 to 6 nodes (224–226) | `multiparty/chains.py`, `chains.csv` | n=3,4,5,6 all triadic Φ=2.000000 | **MATCH** |
| 13 | Survival credited to committing, not feedback (226) | `multiparty/chains.py` (`Sj'=S_{j-1}∧S_{j+1}`), `STRUCTURAL_FINDINGS` #6 | each mediator commits jointly on both neighbours | **MATCH** |
| 14 | q213 car dealer: integration collapses when forbidden maker–buyer tie restored (328–332) | `q213/FINDINGS.md` H3 | Φ_MIP 2.0→0.0, dealer leaves core, margin 2.0 = "entire integration" | **MATCH** |
| 15 | Gravitation is all-to-all → solar system can't enter the corpus (267–268) | `corpus/population.py` (strict-mediation = no W–C edge) | corpus requires no direct outer edge; N-body is all-to-all | **MATCH** (technically correct) |

**No mismatches. No receipt was "not found."** Every number the paper prints is in the repo, and I re-derived
the census (item 2, the one number a v3 could not fully pin) directly from `population.csv`.

Two fidelity caveats, neither a defect in the paper:
- **Item 6:** whole-system Φ_MIP > 0 and major-complex membership are formally distinct computations that can
  dissociate (`STRUCTURAL_FINDINGS` #8). For `ats_strict_bottleneck` they coincide (all three in the core), so
  "all three in one irreducible core" holds — and the phrase is the lab's own verdict language. No change; noting
  the language is the essay's, not a separate proof.
- **Item 4:** `pure_relay` is a "first-pass" form in `corpus/FINDINGS.md` (not yet validated against the
  dissertation's worked cases), though its Φ = 0.00 is exact and independently reproduced by E3's three-node
  relay. The paper's minimal pair pairs it with the fully-validated `ats_strict_bottleneck`. Exposure is near-
  zero; the sourcing note already records this. No prose change needed.

---

## 5. Findings, ranked

1. **Verdict/scale tension, stated but unresolved (lines 211–214).** "The largest value any form attains" does
   scale-work the same clause disavows, and the unmentioned Φ = 0.5 band makes the trap real. Cut the clause;
   let the verdict carry the pair. §3.1, R-A/R-A′. *Top fix.*
2. **Flagship-term split: "partition-necessary middle" ≠ "the final form of the integrator criterion" (lines
   325–331 vs. 371/380).** The paper's headline concept names the partition half while its stated final
   criterion is the partition∧bypass conjunction, under near-identical labels. Map the two once, in the author's
   own voice. This is the item Papers 4–9 inherit; only the author can freeze it. §3.2.
3. **q213 attribution micro-ambiguity (lines 328–332).** The car dealer is correctly credited to q213 but
   bundled under "Paper 2 worked the held case," inviting a misread. One comma-level clarification; confirm the
   Post 2 cross-reference. §3.6.
4. **"rung" ×12 drumbeat.** Thin to ~8. §3.10.
5. **256 denominator gloss (optional) and IIT-4.0 φ_s vs Φ nomenclature (journal only).** Both are precision
   pre-empts, neither is an error. §3.3, §3.9.

Guards: **both hold.** No anticipation leak survives (the only "anticipated" in the body is the disclaimer,
line 365; the v3 leaks at the intro are fixed to "drew it" / "in another vocabulary"). No instrument-demotion
language anywhere (no "calculator / decorative / hollow / unnecessary / merely"); the Stein section grants
boundaries while keeping the instrument's work "real work" (line 314) and "thin and decidable is what makes it
an instrument" (line 262). Clean.

---

## 6. Biggest strength, and the one thing only the author can supply

**Strength.** "The Move the Resemblance Does Not License" remains the best section in the series, and v4 tightened
it: it states exactly what Sans establishes (the objective syllogism is a real structure of wholes), exactly what
he does not (that the reality is a *causal* structure a partition test measures), takes the remaining step in the
author's own name, and now prices the corpus limit honestly — a gravitating system "could not even enter the
corpus" because strict mediation forbids the all-to-all edges. Almost no bridge paper in this genre budgets its
own collapse this precisely. The receipts section is the first place in the nine posts where the claim to computed
ground is actually cashed, and it is cashed cleanly: real numbers, verbatim rule-glosses that check against the
code, the in-silico caveat carried through.

**The one thing only the author can supply.** The canonical, frozen name-and-definition for the program's middle,
resolved against finding #2. v4 committed the *criterion's* final form (core membership that survives the bypass)
but left the coined term "partition-necessary middle" naming only the partition half. Papers 4–9 will quote
whichever sentence this post freezes: does the program's flagship middle mean "an integrator" (partition-core
membership, this paper's receipts) or "a necessary middle" (partition ∧ bypass-survival, Paper 2's refinement)?
No reviewer can choose it — it is a commitment about what the program's criterion *is*, not a fact about what the
code computes. The code offers both components exactly; the author picks which one the word carries, and says so
once, here.

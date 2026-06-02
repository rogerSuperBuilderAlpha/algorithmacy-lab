# Dissertation Committee Review — Three Members

You are convening a doctoral dissertation committee for Roger Hunt III (Bentley University),
"The Transition to Algorithmacy: A Construct and a Formal Model of Triadic Algorithmic
Coordination." You will embody THREE committee members in turn, each reading the whole
dissertation but reviewing through their own lens, then a Chair synthesis. Be harsh, specific,
and fair: the goal is a defensible verdict, not encouragement.

## What to read (in this order)
Read everything before writing anything. Paths are relative to the `dissertation/` directory.
- Framing: `FRONT_MATTER.md` (title/abstract), `INTRODUCTION.md`, `CONCLUSION.md`, `BACK_MATTER.md`
- Paper 1 (construct): `paper1_review/DRAFT.md`
- Paper 2 (Φ model): `paper2_construct/draft/DRAFT.md`, plus `results.md` and the scripts
  `phi_instrument.py`, `worked_examples.py`, `eliminate_dyad_sweep.py`, `party_partition.py`,
  `read_structure_sweep.py`, `phi_vs_separability.py`
- Paper 3 (population/experiment): `paper3_baseline/draft/DRAFT.md`, `results.md`,
  `experiment/RESULTS.md`, and the scripts `simulated_orgs.py`, `analyze_simulated.py`,
  `typology_phi.py`, `typology_sensitivity.py`, `experiment/sim/coordination_sim.py`
Where a numeric claim is load-bearing, VERIFY it against the committed script/CSV output (run it
if you can, under `~/iit-playground/venv-4.0/bin/python`); do not take the prose on trust.

## The three members

### Member 1 — Dr. Elena Vance, Professor of Organizational Communication (construct theory)
Lens: Suddaby/Podsakoff construct-clarity tradition. She owns Paper 1.
Hammers: Is the dyad/triad distinction real and load-bearing, or rhetorical? Does "algorithmacy"
earn its place against algorithm sensemaking, AI literacy, HMC, Zhou's algorithmic competency, or
is it a relabel? Are the foreclosed constructs represented at full strength or strawmanned? Is the
integrative-review method reproducible? Does the opening empirical puzzle actually support the
claim, or is a citation being over-read? Is the structure→competency inference argued or assumed?
Lets slide: heavy formalism she can't evaluate (defers to Member 2). Kills on: a construct that
cannot be shown distinct from its nearest neighbor.

### Member 2 — Dr. Marcus Reinhardt, Professor of Computational Neuroscience (IIT / formal modeling)
Lens: built and critiqued integrated-information measures; reads PyPhi fluently. He owns Papers 2–3's machinery.
Hammers: Is the Φ-equals-triadicity transplant a homology or a shared English word ("irreducible")?
What survives the move — intrinsic existence, the MIP, the cause-effect structure — and what is
stripped? Crucially: does importing all of IIT-4.0 do ANY work a conditional-independence /
factorization test wouldn't? Is the state-individuation rule principled or gerrymandered, and does
the code actually compute what the prose claims? Are the "surprising" worked cases genuine outputs
or reverse-engineered TPMs? Is the magnitude interpretable, and is the paper consistent about
disclaiming it while leaning on it?
Lets slide: organizational vocabulary. Kills on: the apparatus being decorative, or the code not
matching the claims.

### Member 3 — Dr. Priya Anand, Professor of Research Methods (computational social science / measurement validation)
Lens: simulation methodology, validation, statistics. She owns research design and dissertation-level integration.
Hammers: Are the 86 "organizations" a discovery or a tautology (predictors = generator's own loop
variables)? Is the agent experiment genuinely informative or a triviality ("we removed a channel,
coordination got harder")? Is it circular — do Φ and difficulty share a generator? Is the OLS
identified, with standard errors? Are reported numbers backed by committed data? At the dissertation
level: the title promises a *competency* but the papers measure a *form property* — is there a
bait-and-switch? What has actually been shown about the real world, and is "we built a formal model
and named its limits" enough for a PhD? Is the hedging intellectual honesty or a shield for work not
done?
Lets slide: nothing about rigor. Kills on: zero contact with real outcomes dressed as validation.

## Output (per member, then Chair)
For EACH member, in their own voice:
1. **Verdict** (2–3 sentences).
2. **Most serious problems**, ranked, each with: a short quote, its location (file + section), a
   severity (fatal / major / minor), and why. Verify any number you cite.
3. **What is genuinely good** (be fair — name real strengths).
4. **Required revisions**, concrete and ordered.

Then **Chair synthesis**:
- Where the three agree and where they conflict (name the conflicts; do not average them away).
- The single greatest threat to the dissertation, and whether it is fixable.
- The hardest questions the candidate will face at defense.
- A recommendation: **pass / minor revisions / major revisions / fail**, with the conditions for
  moving up one level.

## Rules
- Quote the actual text; cite file and section so claims are checkable.
- Verify load-bearing numbers against the committed scripts/CSVs; flag any that don't reconcile.
- No rubber-stamping and no false harshness — every criticism must be specific and actionable.
- Each member reasons independently; do not let one member's view homogenize the others.

---

## Notes on use
- **As three parallel agents** (closest to a real committee, and what surfaces the strongest
  findings): give each agent only its own member's section plus the "What to read" and "Rules"
  blocks, then run a fourth pass for the Chair synthesis over the three outputs. The independence is
  the point — a single model role-playing all three tends to converge them.
- **The "verify the numbers" instruction is load-bearing.** The sharpest findings (e.g. an
  encoding-dependent Φ result, a rank-deficient OLS, a non-reproducible effect size) tend to come
  out only when the reviewer *runs the code* rather than trusting the prose. Keep that clause.
- To stress-test the revised drafts rather than the originals, point this at the
  `revision/committee-response` branch — the numbers there reconcile, so the committee's attack
  moves to the remaining soft spots (the demand-vs-capacity framing, the absence of real-world
  validation, whether the binary Φ verdict is worth the IIT apparatus).

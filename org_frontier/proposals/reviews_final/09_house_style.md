# House-style audit — final pre-submission pass

**Manuscript:** "When is a combination a configuration?" (Organization Theory, configurational special section)
**Basis:** `~/.claude/writing-style.md` (house style), full read of `final_manuscript.md`. Body word count (abstract through the closing paragraph, excluding references): **8,545 words**.

## 1. Verdict

**MINOR PASS.** The prose is close to the house standard — named agents, concrete anchors, honest hedges, real rhythm variation — but four mechanical tells survive: an epigram drumbeat at paragraph ends, a repetition cluster around "exactly computed," zero first person in a venue whose exemplars use it, and ~640 words of compressible material. One session of targeted cuts fixes all four.

## 2. Counts dashboard

| Check | Count | Assessment |
|---|---|---|
| Agentless passives / abstract-noun subjects | **3 hard, ~4 soft** | Excellent for 8.5k words; the 3 hard ones are quoted below |
| Antithesis density | "rather than" ×22 + contrastive ", not " ×~17 ≈ **39 / 8,545 ≈ 4.6 per 1,000** | Under the ceiling of 5, but barely — and clustered in §§5–6, where local density exceeds it. Thin by ~8 |
| Self-narrating rigor | "exactly" ×19; the computation-as-agent formula ("The computation says otherwise / reads it irreducible / still factors / honors the ordering") ×5 | A real tic. State the exactness policy once in §2 and strip the per-instance badges |
| Em-dashes | **45** (~5.3 per 1,000) | Mostly the sanctioned uses (coinage, expansion, qualification-then-reveal). ~4 lazy paired bolt-ins to cut; do not zero the rest |
| Epigram-landing uniformity | ~**22 of ~34** body paragraphs end on a polished quotable turn (~65%) | The single biggest slop signal. Flatten 5–7; the cure is plainness, not more polish |
| Verbatim formula repeats | "aggregate of smaller ones" ×3; "separates the criterion from the network surrogate" ×2 (verbatim); "this essay" ×10; "the call (for this section)" ×6; the models-not-world hedge ×3 | Vary or consolidate; strings quoted in §3 below |
| Filler transitions / empty closers | **0** filler transitions (no furthermore/moreover/additionally/"important to note"); ~2 pointer-closers ("...and section 5 builds on exactly this") | Clean. Pointer-closers are functional, leave them |
| Hedging quality | Strong: "Its phenomenological ambition is contested"; "the exercise disciplines the distinction rather than testing it"; "This is a translation, not an independent confirmation" | Flat, specific, never ritual. Only flaw: the same models-are-models hedge is run three times (§2 twice, §7 once) — keep §7's full version, shorten the others |
| First person | " we " ×**0**, " I " ×**0** | A register failure for this venue. House style: "Impersonal third-person throughout is the single biggest source of the robotic feel." The Stark & Vanden Broeck exemplar (this exact journal) writes "we contend" |
| Register fit (Organization Theory) | Otherwise strong | Essayistic, concrete, citation-dense with short punctures; the table in §6 and the worked model in §3 suit the venue's theory-essay genre |

## 3. Worst five, with paste-ready rewrites

**(1) Agentless passive on an abstract-noun subject — §2 specification note.**
> "Integrated information has been formalized more than once (IIT 3.0, Oizumi et al., 2014; IIT 4.0, Albantakis et al., 2023), the variants can disagree on a given model..."

Rewrite:
> "Tononi's group has formalized integrated information more than once (IIT 3.0, Oizumi et al., 2014; IIT 4.0, Albantakis et al., 2023); the variants can disagree on a given model..."

**(2) Agentless passive hiding the authors' own work — same paragraph.**
> "...and the dependence on the measure was tested rather than assumed."

Rewrite (also breaks the first-person drought exactly where the exemplars do — the analytic move):
> "...and we tested the dependence on the measure rather than assuming it."

**(3) Agentless passive in the limits section — §7.**
> "The verdicts are exact for the models and are evidence about the models; no organization has been measured..."

Rewrite:
> "The verdicts are exact for the models and are evidence about the models; we have measured no organization..."

**(4) Verbatim formula repeat — §3, third and fifth results open on the same string.**
> "A third result separates the criterion from the network surrogate specifically." / "A fifth result separates the criterion from the network surrogate at its limit."

Rewrite the fifth (or better, merge — see cut candidate C below):
> "**Density without constitution: maximal wiring.** The network surrogate fails even at its limit. Consider a three-party arrangement with all six directed couplings active..."

**(5) The paper-as-agent standing in for the author — "this essay" ×10, "I/we" ×0.**
> "This essay supplies that within-case criterion, borrowed from an unexpected neighbour, and develops three concepts configurational scholarship has stated only informally..."

Rewrite:
> "I supply that within-case criterion here, borrowing it from an unexpected neighbour, and develop three concepts configurational scholarship has stated only informally..."

Then carry "I/we" through the roadmap ("In section 3 I state the criterion...") and the two rewrites above. Three to five first-person moves total is enough; do not convert every "the essay."

**Also flag (epigram drumbeat, one worked example).** Landing lines to flatten — each is good alone; together they are the drumbeat: "Connection is not constitution. A whole that reads everyone can still be an aggregate, if it could have read anyone." / "Surface description misleads in both directions: the busy quorum factors, the idle-looking cycle binds." / "Spectators never belong, however well placed." / "Same position, opposite constitution, and only the counterfactual tells them apart." / "The plain counterfactual signs the verdict; the calculus locates it." / "The models small enough to compute turn out to be large enough to think with." Pick 5–7 and end plainly instead. Example — replace "Surface description misleads in both directions: the busy quorum factors, the idle-looking cycle binds." with:
> "Surface description misleads in both directions here: the quorum looked configured and was not, and the cycle looked like a relay and was."

Keep the final line of the paper ("...told from the heaps") and "A rotation binds." — those have earned their place.

## 4. Cut candidates (target ≈ 640 words)

**A. §2 specification note (the "One specification note..." paragraph): cut ~180 of ~300 words.** The IIT 3.0 replication detail (which three factorings fail to replicate and why) belongs in the online supplement the paper already advertises. Keep: the one-operationalization sentence, "a constitution criterion needs zeros," the binds/factors robustness scoping, and the Davis–Eisenhardt sentence. Least loss in the paper; the supplement gains a natural section.

**B. §4 Shapley paragraph ("The graded law can be stated in a second notation..."): cut ~120 of ~240.** Keep the honest scoping ("a translation, not an independent confirmation") and the priced example (mediator two-thirds, each party a sixth). Cut the axiom machinery (worth function definition, Null Player transfer) — the table in §6 already carries the game-theoretic row.

**C. §3 fifth result (maximal wiring): cut ~70 of ~120 by merging into the third result (synchronization).** Both make the same point against the network surrogate; a merged "Wiring without constitution" entry with two exhibits kills the verbatim repeat (worst-five #4) for free.

**D. §5 "verbal siblings" paragraph (Williamson / essential facilities / leakage): cut ~90 of ~225.** One sentence per sibling suffices; the paragraph's two real contributions (cost-relativized counterfactual; whole-partition vs. element-by-element test) stay.

**E. §5 "Five design moves" paragraph: cut ~100 of ~165.** Five compressed moves in one paragraph is a list wearing prose. Keep two (owner-tilt hollowing the core; opening the direct channel evicting the platform), which are the two the argument reuses.

**F. §6 closing paragraph (Kimsey / Emirbayer / Tsoukas affinities): cut ~80 of ~180.** Tsoukas is already placed at the end of §3; one sentence each for Kimsey and Emirbayer preserves the citations the venue expects without the ceremonial tour.

Running total: **~640 words**, bringing the body to ~7,900 without touching any load-bearing result.

## 5. Do not touch

- **The worked strict-mediation model in §3** ("Take three elements... Now cut it.") — the house's concrete-anchor rule executed perfectly, including the short-sentence puncture.
- **The Thompson paragraph** ("The nearest ancestor of these results deserves his credit by name") — named agent, active verbs, generous and precise; the best paragraph in the paper.
- **The quorum caveat** ("Φ of zero... does not condemn the design; it classifies it. The criterion measures constitution, not merit") — exactly the flat, specific hedging the style demands.
- **The encoding-as-power paragraph in §7** ("a platform that gets its coordination encoded as pairwise contracts has factored itself out of accountability for the whole, before any computation runs") — the paper's sharpest new sentence; leave verbatim.
- **The Obstfeld derivation** ("The orientation the literature most admires is, carried to completion, self-liquidating") — a genuine payoff, not decoration.
- **The em-dash coinages** ("necessary against contingent irreducibility," "the minimum-information partition — the cut that does the least damage") — sanctioned uses; do not sweep them up in a dash purge.
- **The honest-catalog hedge in §5** ("coded by the same hands that knew the outcomes... disciplines the distinction rather than testing it") and the final line ("...told from the heaps").
- **The §6 table** — it compresses what prose would bloat.

## 6. Bottom line

This reads like the dissertation corpus, not like Claude: agents are named, hedges are flat, every abstraction touches an escrow agent or a car dealer, and there is not one "furthermore" in 8,545 words. What remains is over-optimization, not under-writing — too many paragraphs auditioning their last line, a rigor badge ("exactly computed") pinned on every result instead of stated once, an antithesis rate touching the ceiling, and an author who never says "I" in a journal whose exemplars do. Apply the five rewrites, flatten five to seven landing lines, thin "rather than / , not" by about eight instances in §§5–6, and take the ~640-word cut. That is an afternoon's work, and after it the read-aloud gate — the author's, not a checker's — is the only gate left.

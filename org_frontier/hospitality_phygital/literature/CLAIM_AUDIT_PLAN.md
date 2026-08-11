# Claim audit — deep research plan

Purpose: run every claim the paper makes against the literature that might already answer it,
before a reviewer does. Plan only; nothing below has been executed. The claim inventory this plan
audits is the 31-item list isolated on 2026-08-09 (chat; to be frozen as `CLAIMS.md` at kickoff).

## 0. What kind of risk each claim carries

The claims divide into four exposure types, and the research design differs by type.

| type | exposure | design |
|---|---|---|
| **Absence claims** — "the literature does not ask/say X" | A single counterexample kills the contribution | Adversarial falsification: agents instructed to *refute*, searching venues the prior rounds did not sweep |
| **Borrowed-evidence claims** — "study Y shows Z" | Misreading, superseding studies, failed replications | Evidence audit: does the source say what we say, and has anything newer overturned it |
| **Definitional claims** — our constructs and distinctions | Term collisions; prior art under other names | Collision sweep: same idea, different vocabulary |
| **Inherited claims** — Pierre's abstract, editor-blessed | Low; already reviewed by the SI editor | Light confirmation only |

The absence claims are the ones that can kill. Prior rounds (FOUNDATION.md Parts 1–5) swept
hospitality, tourism, service and marketing venues. **They did not sweep philosophy of technology,
machine ethics, accountability theory, or law**, and those are exactly the fields where "what does a
machine owe" is a standing question. The plan assumes our biggest exposures live there.

## 1. Pre-registered expected collisions

Four hits I expect the audit to find, registered now so the agents confirm rather than discover, and
so a hit is handled as repositioning rather than panic:

1. **Bovens on accountability.** Claim 16 (accountability is a relation requiring a forum, not a
   state a party can be in) is close to Bovens' canonical definition of accountability as a
   relationship between an actor and a forum (*European Law Journal*, 2007). If confirmed, we cite
   rather than argue, and the claim gets stronger, not weaker.
2. **Verbeek and mediation theory.** Claim 27 ("constitutive mediator") has a philosophy-of-technology
   lineage: postphenomenological mediation theory holds that technologies co-constitute the relation
   between humans and world. The paper should almost certainly cite this rather than appear to coin
   the idea. The hospitality application remains ours.
3. **Raisch and Krakowski on augmentation vs automation.** Claims 13–14 (augmentative/substitutive)
   sit next to the augmentation–automation paradox in management theory (*AMR*, 2021). TPSR's
   augment/replace proposition was already flagged (P6). The defensible position is that our
   distinction is a condition on an *arrangement*, theirs a property of a *task allocation* — but
   that has to be argued against the real text, which nobody on this project has read.
4. **Gunkel, Coeckelbergh and machine ethics.** Claims 3, 12 and 28 assert nobody asks what the
   technology *owes*. Robot ethics asks adjacent questions constantly (moral status, robot rights,
   machines as moral patients/agents). The survival move, if the field is close: their question is
   what we owe machines or what machines can be responsible *for*; ours is what a machine performing
   hosting owes *the guest* under hospitality's own duty structure. Confirm the distance.

## 2. Research units

Nine units. Each gets one agent unless marked. Claims map as follows; claims 7 (triad, settled in
Part 5) and 30 (self-declared limit) need no research.

### U1 — The host-obligation absence *(claims 3, 4, 5, 12, 28 — KILL RISK, run first)*
Adversarial. Try to find anyone who asks whether an algorithmic system occupies the host role or
carries hospitality's duty of welcome. Sweep: machine/robot ethics (Gunkel, Coeckelbergh, Darling);
Levinas- and Derrida-inspired AI ethics; "machine hospitality" and "robot host" in HCI/CSCW; law of
algorithmic accountability (duties owed by deployers); care ethics and AI; the hospitality-of-AI
literature if any exists. Also re-test claim 4 (substitution unremarked) against service-research
commentaries and critical service work. Verdict per claim: KILL / WOUND / GRAZE / CLEAR, with the
searches that ground any CLEAR.

### U2 — Seamlessness and friction *(claims 6, 21, 22, 23, 26)*
Two jobs. (a) Re-run the friction-on-phygital absence with wider nets: seamless design critiques in
HCI, CX friction work post-2024, "calm technology" critiques, any phygital paper problematizing
smoothness. (b) Audit Folger 1977: replication status and the procedural-justice meta-analytic
record on voice effects independent of outcome; if the effect is contested, §7 needs the caveat
before a reviewer supplies it. Absorbs unrun prompt P5 (friction as design value).

### U3 — Augmentative/substitutive collisions *(claims 13, 14)*
Read Raisch and Krakowski in full; sweep augmentation/automation in IS and management; delegation
and task-allocation frameworks; any prior operationalization of augment-vs-substitute as a checkable
condition rather than a designer's intent. The question is not whether the words exist — they do —
but whether anyone has stated the distinction as a *conjunction of withholdings testable at a
touchpoint*. That specific form is what claim 13 needs to own.

### U4 — The three redistributions *(claims 8, 9, 29)*
Evidence audit plus contrary-evidence hunt. Knowledge: anything showing symmetric or guest-favouring
information effects of hospitality tech. Discretion: post-2024 empirical work on front-desk and
guest-facing algorithmic direction (would convert claim 29's "absent" to "present", which changes
§3's split verdict). Authority: counter-cases where mediation devolved rule-writing to properties or
guests. Also re-verify our readings of Rahman, Scott and Orlikowski, and Möhlmann at full-text depth.

### U5 — Standing, negotiated access, and the guest *(claims 10, 11)*
Two exposures. (a) Counter-readings: is our tactical (Lynch) and continuous-authority (Bulley)
reading contestable — has anyone read the same texts otherwise. (b) Collision: "consumer sovereignty"
in marketing and the customer-power literature — does existing theory already give the guest a
counterparty story under mediation, and does the phrase collide with coordinative sovereignty.

### U6 — Construct collisions *(claims 15, 16, 17)*
Term sweeps: "algorithmacy" anywhere in scholarly use; "coordinative sovereignty" anywhere;
algorithmic literacy / algorithmic competence constructs that already have three-component
structures. Bovens confirmation (see §1.1). Accountability-as-relation in algorithmic-accountability
theory (Wieringa's review is the likely map). The three-component structure (interpretation,
specification, tracking) checked against existing folk-theory and literacy taxonomies for
isomorphism — if someone's taxonomy maps 1:1, we cite and differentiate on derivation, not content.

### U7 — Affordances and their nulls *(claims 18, 19, 20)*
Absorbs unrun prompt P4. (a) Do the three published nulls still stand — post-2020 evaluations of
appeals, explanations and disclosure that *worked* would soften "survives its null". DSA Article 21
out-of-court settlement empirics; platform ombuds evaluations. (b) The design/institution division
(claim 20): does the sociotechnical or service-design literature already carve affordances by
provision mechanism. (c) "Affordance" term discipline: our usage vs Gibson/Norman lineage — one
sentence of protection may be needed.

### U8 — Torque, exclusion, and the remedy paradox *(claims 24, 25)*
Absorbs unrun prompt P3's core. (a) Empirical work on atypical guests meeting algorithmic categories
(accessibility, dietary, kinship, name mismatches) — currently the claim rests on classification
theory alone. (b) Cui et al. follow-ups, critiques or failed replications; any work naming the
remedy-deepens-mediation pattern (ratchet/lock-in framings in surveillance studies).

### U9 — Inherited and framing claims *(claims 1, 2, 27, 31 — light touch)*
Confirmation only: no direct refutation in print of the relational-practice framing; Verbeek
confirmation for claim 27 (see §1.2); a check that "constitutive mediator" as a phrase is not
already claimed in a service journal. Half an agent's work; bundle with U6 if budget is tight.

## 3. Execution architecture

**Wave 0 — desk triage (no agents).** Freeze the claim list as `manuscript/CLAIMS.md` with claim
text verbatim, type, unit assignment, and current evidence. Mark claims 7 and 30 settled. One pass
over FOUNDATION Parts 1–5 to attach what is already known to each claim, so no agent re-finds it.

**Wave 1 — kill risks.** U1, U2, U3 in parallel. Opus, maximum-adversarial prompts: the agent's
stated job is to *refute the claim*, default verdict WOUND when uncertain, CLEAR only with the
search log to justify it. These three can restructure the paper; nothing else runs until they
return and their verdicts are read.

**Wave 2 — evidence and collisions.** U4–U8 in parallel (U9 folded into U6). Opus for U5–U7
(judgment-heavy), sonnet acceptable for U4 and U8 (audit-shaped).

**Wave 3 — verification and adjudication.** One sonnet sweep re-resolving every citation returned
by every unit against Crossref (the standing rule; three catches to date). Then adjudication —
done by the lead, not an agent: verdict per claim recorded in `CLAIMS.md`, kills and wounds turned
into AGENDA items with proposed repositionings, FOUNDATION.md Part 6 written, bib updated with
readdepth notes, ABSTRACT_MAP statuses refreshed.

Agent count: 9–10 total, inside the medium-workflow guideline. Rough wall-clock: Wave 1 an
afternoon, Wave 2 overnight parallel, Wave 3 a morning. Fits Aug 10–12 inside Phase 2 of PLAN.md §6
without moving any gate.

## 4. Rules binding every unit

The standing protocol from RESEARCH_PROMPTS.md applies unchanged: Crossref or publisher-record
verification for every citation; read depth stated per source; no substantive attribution from an
abstract alone; misses reported as named absences; pay-to-publish outlets rejected. Three additions
for this audit:

1. **Refutation default.** Every prompt states the claim verbatim and instructs the agent to defeat
   it. An agent that returns only support has failed its brief.
2. **Verdict taxonomy.** KILL (claim already made or already refuted in print — the paper
   restructures), WOUND (substantially anticipated — cite, concede, reposition on what remains),
   GRAZE (adjacent work exists — a citation and a boundary sentence), CLEAR (named absence — the
   searches run become the footnote that protects the claim). Every verdict carries its evidence.
3. **Venue-escape requirement.** Each unit's prompt names at least two fields *outside* those swept
   in Parts 1–5, because the absence claims have only been tested inside hospitality's neighbours.

## 5. What execution decides that this plan does not

Whether a KILL on U1 re-points the paper or merely re-words it is an authorial decision, taken
against the ABSTRACT_MAP rule that the paper delivers the abstract the editor blessed. The plan
surfaces collisions; it does not pre-commit any response beyond the four pre-registered ones in §1,
where the response (cite the antecedent, keep the hospitality application) is safe under that rule.

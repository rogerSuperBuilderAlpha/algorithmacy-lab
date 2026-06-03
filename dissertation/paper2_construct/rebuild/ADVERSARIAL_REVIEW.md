# Paper 2 — adversarial committee review and adjudication (Stage 4, round 1)

Three hostile reviewers read the draft (`DRAFT.md`) independently against the committed scripts:
a measurement / construct-validity methodologist (R1), an integrated-information / complexity
expert (R2), and a senior organization theorist / platform-work skeptic (R3). All three
**reproduced every load-bearing number exactly** by running the `rebuild/` scripts in
`venv-4.0`. All three returned the same verdict: **MAJOR REVISIONS, bordering reject.**

The reviews converge hard. The arithmetic is not in doubt. The claims built on it are. This file
synthesizes the findings, then adjudicates each against new computation in `review_response.py`,
which settles several of the charges with numbers instead of rhetoric.

## The verdicts
- R1 (methodologist): MAJOR, bordering reject on the warrant claim.
- R2 (IIT expert): MAJOR. Engine correct; three §8 technical claims wrong/overstated; binary fragile.
- R3 (org theorist): MAJOR, bordering reject. Warrant circular; formalism in search of a problem.

## The new computation that adjudicates the charges (`review_response.py`)
1. **Per-state Φ profiles.** The binary rule is "Φ>0 at some reachable state." The worked triads
   are thin: ATS-AND carries Φ>0 at **1 of 4** reachable states; the false-dyad triad at **1 of 5**;
   the conjunctive channel at **1 of 5** (the lone Φ=6.0 state). Only the irreducible control is
   thick (**5 of 6**). In every thin case the carrying state is the all-on state, where both parties
   are simultaneously live. **R2's "single-state fragility" charge is correct.**
2. **Rideshare carving-invariance.** Re-encoding the same rideshare mechanism under four defensible
   alternatives: baseline → TRIAD; driver re-arms from both sides (W'=¬S∨¬C) → **TRIAD** (maxΦ=0.415);
   rider decoupled from dispatch timing (C'=C) → **DYAD**; looser OR match rule (S'=W∨C) → **DYAD**.
   Two of four flip. **R1/R3's "not analyst-independent" charge is partly correct** — with a real
   structure underneath it (below).
3. **Effective information on the exhibit.** EI = **2.0 bits** on the exhibit where Φ=0, and the
   *true dyad* (factoring control) has the *highest* EI of all (**3.0 bits**), the true triad 2.5.
   EI does not track the dyad/triad line. **R2's charge that the EI claim was asserted not computed
   is correct, and the computation now backs the underlying point** (EI over-calls) while killing the
   false identity the draft used to state it.

---

## A. Charges that are REAL and must be fixed (confirmed by computation or plainly correct)

### A1. The "material reality / objective / analyst-independent" framing is over-claimed (R1, R3; confirmed)
All three reviewers name this the central problem, and the carving computation confirms it. The
verdict is not invariant to defensible re-encodings (2 of 4 rideshare variants flip). "Objective
structural fact, not a matter of framing" (§1, §10) and "analyst-independent" (§10) claim more than
a model whose every input is an analyst's choice can deliver. **This is real.** The fix is not to
gut the claim. It is to state precisely what IS invariant. The verdict is determined by the
mechanism, and it is invariant across carvings that preserve the four-question criterion (a
constitutive joint determination over two live parties, no route-around). It flips exactly when a
re-encoding violates the criterion — by freezing a party into a constant (variant A makes the rider
inert) or by loosening the determination off a constitutive conjunction (variant C, an OR-dispatch
that fires on one side alone). That boundary is principled and reportable. The honest claim is
**conditional objectivity**: given a mechanism that meets the criterion, the dyad/triad verdict is a
structural fact, not a framing; and the criterion disciplines which encodings count as faithful. The
draft must make the conditional explicit and stop asserting unconditional analyst-independence.

### A2. The binary verdict is single-state in the worked triads (R2; confirmed)
The triad verdicts for ATS and the false dyad rest on the all-on state alone (1/4, 1/5). **This is
real.** It is not fatal, because the carrying state is interpretable — irreducibility appears exactly
when both parties are simultaneously live and the mediator must jointly resolve them, which is the
moment the triad exists. But the draft hides it by reporting only maxΦ and meanΦ. Fix: report the
full per-state Φ profile for every worked triad (now in `review_response.py`), and argue why
"Φ>0 at the state where both parties are live" is the right rule rather than a fragility. State
plainly that on this rule a single constitutive state suffices, by design.

### A3. §8 contains a false identity and an unearned "provably" (R2; confirmed)
"Φ in this lineage is effective information evaluated at the minimum-information partition" is
**false** for the IIT-4.0 system measure. EI is a determinism-minus-degeneracy quantity over a
max-entropy intervention; system-Φ is an intrinsic information distance minimized over the MIP. They
are not one functional differing by a partition step. "Effective information provably over-calls" was
asserted without computing EI. **Both real.** Fix: delete the identity. Replace it with the computed
result — EI = 2.0 bits on the Φ=0 exhibit, and the true dyad has the highest EI (3.0), so EI has no
partition step and cannot detect the factoring. The point survives; the false statement of it does not.

### A4. "Cause-effect structure factors" conflates the system measure with the unfolded Φ-structure (R2; correct)
§2 says the paper imports only the system measure and drops the cause-effect-structure / exclusion /
maximization apparatus. Then §3 and §6 say "the cause-effect structure factors," which is IIT's term
for the unfolded object the paper says it dropped. **Real terminological error.** Fix: say "the
system's intrinsic cause-effect *power* factors" or "the system's transition probabilities factor
over some partition," and reserve "cause-effect structure" for the machinery left behind.

### A5. The "geometric Φ / Φ* draw the same line" robustness claim is untested (R2; correct)
The draft asserts the partition-based family agrees on the line and that the IIT-4.0 choice "could
not flip a dyad to a triad," with citations but no computation. R2 notes these measures use different
baselines and normalizations and are known to disagree at the boundary, which is exactly where the
controls and the exhibit sit. **Real overreach.** Fix: retreat to the defensible claim. The IIT-4.0
system measure is the one adopted; it is a partition-minimizing measure; whether geometric Φ and Φ*
agree on the zero-set for boundary cases is not established here and is left open. Do not claim
tested robustness that was not tested.

### A6. The "validation gate" is a unit test, not a validation (R1, R3; correct)
Two controls the author built to factor / not-factor, which the instrument then agrees with, test
that the code computes Φ correctly. They do not validate the construct. **Real.** Fix: call it a
correctness check or a unit test, and drop any implication that passing it validates the dyad/triad
mapping against anything external. The construct mapping is argued (§3), not validated, and the draft
should say so in the same breath.

### A7. Rule 110 equivalence is asserted, not shown; exhibit entangled with reachability (R2; partly real)
"The same phenomenon appears in the Rule 110 example" claims a shared mechanism the draft does not
demonstrate. **Real as stated.** Fix: downgrade to "an analogous phenomenon." On reachability: half
the exhibit's state space is unreachable, and the draft never argues the reachable-only convention is
right for the organizational claim rather than a PyPhi default. Add one sentence defending it (a
coordination form's verdict should rest on states it can actually occupy).

## B. Charges that are PARTLY real — answerable, with a real point underneath

### B1. The warrant in §10 is "circular by construction" (R1, R3; partly real)
The charge: the rivals' Φ=0 and the platform's Φ>0 are both stipulated by the author's encodings, so
§10 computes the assertion rather than demonstrating it. There is a real gap and a real answer. The
gap: the draft never derives the rival constructs' Φ=0 status from their *published*
operationalizations. It models "chat" as a decoupled dyad and reports that a decoupled dyad factors.
A defender of the rival could reject the encoding. **Fix (real work):** for at least one rival
construct, derive the encoding from what that literature actually claims its unit is (e.g., CMC
competence's channel-with-context model puts the third element in the *context* the two parties read,
which is precisely a node that does not commit a joint determination — that is *why* it factors), so
the Φ=0 verdict follows from the construct's own commitments, not a sympathetic caricature. The
answer is available because Paper 1 already argues the rivals are channel/dyad models; Paper 2 must
show the encoding follows from that, not from convenience. What is NOT conceded: the criterion in §3
constrains the encoding, so it is not a free choice. The mapping is refereeable, and the paper should
invite the referee rather than hide the step.

### B2. The rideshare centerpiece is "a tautology — you added the edge that encodes the rider, then reported it matters" (R3; partly real)
True that placing S'=W∧C and then finding the rider matters is not surprising. But the charge misses
what the instrument adds, and the computation shows it. Reading both parties is **not** sufficient for
Φ>0. The exhibit reads both at every node and factors. The OR-dispatch (variant C) reads both and
factors. So "the author added an edge that reads the rider" does not by itself produce the triad
verdict, which means the verdict is not a restatement of edge-placement. **Fix:** reframe the false
dyad around exactly this. The finding is not "an edge that reads the rider makes the rider matter."
It is that a *constitutive conjunction* over two live parties fails to factor while a *disjunction*
over the same two parties factors, and inspection of the edge does not tell you which. That is work
the truth table does not do by eye, and it is the answer to B3 as well.

### B3. "Φ doesn't earn its keep — every real case is settled by reading the update function" (R3; partly real, and answerable)
The sharpest single objection. The residual zone where Φ beats the cheap tests (strongly-connected-
yet-reducible) is the exhibit, which the draft presents as an abstract automaton corresponding to no
coordination form. **Fix (real work, high value):** give the exhibit a coordination reading. It is a
mediator whose determination is redundant given the parties' own states — a third party that appears
constitutive (reads both, all six edges) but whose determination adds nothing the parties do not
already fix between them. That is a *real* platform pattern: the mediator that looks like it
constitutes the match but is actually predictable from the two sides, so the coordination reduces to
the pair despite the apparatus. That is the false triad's hard case, the structural sibling of the
false dyad, and it is exactly where reading the update function by eye fails (the OR-dispatch and the
exhibit both "read both" yet factor). Connect the exhibit to that reading and Φ earns its keep on a
case the paper cares about, not only on a cellular automaton.

### B4. PID/ΦID synergy left uncomputed (all three; real gap, deferred)
All three flag the one comparison the draft itself calls open. It is the nearest live competitor to
"why Φ specifically." **Decision:** computing a defensible ΦID synergy measure is non-trivial and
risks a wrong number. The honest interim move is to be more forthcoming that this is the single
unclosed comparison and to commit it to the revision, not to bury it as a limitation. If it is to be
computed, it should be validated against a known case before it enters the paper. Flagged, not faked.

## C. Reviewer overreach / points to hold the line on

- **"Formalism in search of a problem / venue mismatch" (R3).** Overstated once B3 is fixed. With the
  exhibit given a coordination reading, the methods contribution is the decision procedure plus the
  demonstration that inspection over-calls on a real pattern. That is an ORM-appropriate methods
  contribution. The interpretive novelty (irreducibility = triadicity) is the point of a borrowing
  paper, not a defect. Hold the line, but only after B3 is done.
- **"Markov/CI is vacuous because deterministic" (R2 minor).** Correct that CI is trivially satisfied,
  but the draft's claim is exactly that it holds by construction in the formal model and binds only in
  the empirical extension. That division is right. Adopt R2's wording (CI is met by the modeling
  choice, not a meaningful check passed) and keep the point.
- **"Retire the warrant entirely" (implied by R1/R3).** Do not. The Paper 1 posture holds: keep the
  construct and the warrant, tell the story, make the argument stronger. The warrant survives in its
  conditional form (A1) and is strengthened by B1 and B3, not abandoned.

## D. Disposition — what the corrective pass does

**Unambiguous fixes (apply now, no judgment call):** A2 (per-state profiles), A3 (EI: delete identity,
insert computed result), A4 (terminology), A5 (retreat the family-robustness claim), A6 (unit test),
A7 (Rule 110 "analogous"; defend reachable-only), and disclose the carving result (A1's data) and the
12.5%-vs-22% read-space dependence in the open.

**Strategic reframe (needs the author's steer, mirrors the Paper 1 decision):** A1 + B1 + B2 + B3 —
how far to tighten "material reality / objective / non-circular" to the defensible **conditional**
claim, versus a deeper reframe. Recommended, consistent with the Paper 1 "strengthen, don't retreat"
posture: keep the warrant in conditional form, derive at least one rival encoding from its published
operationalization (B1), reframe the false dyad around constitutive-conjunction-vs-disjunction (B2),
and give the exhibit a coordination reading so Φ earns its keep on a real pattern (B3). This is the
Paper-1-grade corrective round, and it is the next stage.

**Deferred computation (commit, do not fake):** B4 (ΦID synergy), and optionally geometric Φ / Φ* on
the controls + exhibit to convert A5 from a retreat into a tested claim.

---

# Stage 4, round 2 (re-review of the revised draft) + round-3 corrective pass

The revised draft went back through the same three roles. **The panel moved from unanimous
MAJOR-bordering-reject to one MINOR + two MAJOR.**

- **R2 (IIT expert): MINOR REVISIONS** (moved off MAJOR). All three technical errors fixed (EI
  identity deleted and replaced with the computed result; cause-effect power vs structure; geometric-Φ
  retreat). Single-state fragility resolved and independently noise-robust. Remaining asks were
  disclosure, not correction: disclose the exhibit reachable set (the all-on state is unreachable),
  add a noise-robustness line, add worked-case EI rows. R2: "the paper is close."
- **R1 (methodologist): MAJOR** (moved off bordering-reject). Accepted the conditional warrant, the
  unit-test relabel, the rival-encoding derivation as improved. **Found a real internal contradiction:**
  §5's "flips exactly when the criterion breaks" is refuted by §9's 12.5% — the four-question criterion
  is necessary, not sufficient, because the worker/counterpart reads are a second free choice it does
  not discipline, and criterion-satisfying reads can flip the centerpiece.
- **R3 (org theorist): MAJOR** (moved off bordering-reject). Granted the conditional warrant is honest
  (not motte-and-bailey) and the EI computation is the strongest new work. Two standing objections:
  (a) the §5 carving check is undercut by its own script comment, which called variant A "defensible"
  while the prose treated it as an unfaithful flip; (b) Φ still earns its keep on no *documented*
  coordination form — the exhibit's only real-world anchor is Rule 110, a cellular automaton.

## Round-3 corrective pass (applied)
New computation (`review_response.py` §§4–7) grounded every fix:
- **§5/§9 reconciliation (R1, the gate):** confirmed two criterion-satisfying reads (`C'=C∨¬S`,
  `C'=S∨C`, both keep `S'=W∧C`, no W–C edge) still flip to Φ=0. §5, §1, §10, and the abstract were
  rewritten to the honest claim: the criterion is **necessary not sufficient**; a faithful model needs
  the criterion met AND the reads declared; the objectivity is bounded to "given a fully specified,
  declared mechanism," and a different declaration can give a different verdict in the open. This
  weakens the warrant, honestly.
- **Variant-A script comment (R3):** corrected. `C'=C` is a frozen node, not the defensible
  "rider persists until served" (that is the baseline `C'=C∧¬S`); the comment now says so, removing the
  contradiction R3 caught.
- **R2 disclosures:** §7 notes the carrying state is noise-robust (Φ at the all-on state 2.0 → 1.53 at
  10% noise); §8 discloses the exhibit reachable set and that `(1,1,1)` is unreachable, symmetric with
  §7's thin-triad disclosure; §8 adds the worked-case EI inversion (false-dyad dyadic 2.5 > triad 2.16;
  ATS triad 1.81, the lowest).
- **Exhibit "common pattern" overreach (R3):** softened. The draft no longer claims the pattern is
  common; it states the claim is not made and that naming a documented platform of this shape is open.

## Standing after round 3
The §5 contradiction (R1's gate) and the variant-A inconsistency (R3) are fixed by correction, not
spin. The remaining open item is **R3's deepest objection**: Φ's unique zone (strongly-connected-yet-
reducible) has no *documented* platform instance in the paper. Two honest options, an author decision:
(a) concede the zone may be empirically thin and scope the contribution to the binary verdict plus the
discipline against inspection-based over-calling (the exhibit as a cautionary stress-test, which the
softened §8 already leans toward); or (b) search the platform-work literature for a cited case in that
zone. Deferred computations still open and committed: geometric Φ/Φ* family-robustness, ΦID synergy.

---

# Stage 4, round 3 (re-review of the round-3 draft) + copy-edit pass

The round-3 draft (with the §5/§9 reconciliation, the variant-A fix, R2's disclosures, and the
literature integration) went back through all three roles. **Verdict trajectory across three rounds:
3× MAJOR-bordering-reject → 1 MINOR + 2 MAJOR → ACCEPT + 2 MINOR.** No reviewer remains at MAJOR.

- **R2 (IIT expert): ACCEPT.** All three disclosures landed and reproduce; the EI implementation is
  the correct Hoel construction; no round-3 edit regressed a technical claim. Only non-blocking note:
  "realistic perturbation" → "perturbation" (the noise model is a toy).
- **R1 (methodologist): MINOR.** The §5/§9 contradiction is gone at the sentence level across all five
  loci (abstract, §1, §5, §9, §10); the bounded warrant survives the necessary-not-sufficient concession
  because it rests on construct-proliferation (rivals factor, platform does not), not on
  verdict-uniqueness; the paper does not over-correct. Asks: name the read-faithfulness as the open
  discipline in §5; de-hedge the abstract. "Resolve and this is ready to ACCEPT."
- **R3 (org theorist): MINOR.** Off MAJOR. The §5/script contradiction is fixed; the operator-choice
  tautology is conceded and correctly bounded; Φ-earns-its-keep is narrowed — the exhibit now has a
  documented organizational kin (fauxtomation, route-around), no longer only Rule 110 — but the
  cheap-test-defeating zone remains empirically unoccupied, which is acceptable to defer for a methods
  paper IF stated in §10 in those exact terms. Asks: state the empty-zone limit in §10; disjoin the
  §9 route-around axis from the exhibit's conditional-redundancy zone.

## Copy-edit pass (applied; all reviewer-requested, no judgment calls)
- §7: "realistic perturbation" → "perturbation," with a note that the mixing is a crude noise model
  (R2).
- §9: added a sentence disjoining the channel-opens axis (Öborn/Maffie) from the exhibit's
  conditional-redundancy zone, so a reader cannot slide from "route-around documented" to "Φ's unique
  zone documented" (R3).
- §5: named the read-faithfulness as the method's thinnest joint and an open discipline — the reads
  are disciplined by case-argument, not by a rule as tight as the alphabet's (R1, R3).
- §10: added the specific limit — the strongly-connected-yet-reducible zone where Φ uniquely beats the
  cheap tests is the one with no documented platform instance; the unique-necessity claim rests there
  on a constructed exhibit plus conceptual kin, and confirming a real instance is Paper 3's (R3).
- Abstract: de-hedged the bounded-objectivity pile-up (R1).

## Standing
Panel at ACCEPT + 2 MINOR, with the MINOR items now addressed in copy-edit. Genuine remaining loose
ends, all flagged in-draft as future work, none blocking: (1) compute a ΦID/PID synergy measure on the
exhibit (the most plausible cheap rival that might also fire in Φ's unique zone — the obvious next
computation); (2) geometric Φ / Φ* zero-set agreement on the controls + exhibit; (3) the empirical
confirmation of the exhibit's zone, which is Paper 3's measurement task.

---

# Stage 4, round 4 (re-review of the round-3 draft) + adjudication

The round-3 draft went back through the same three roles a fourth time: a measurement /
construct-validity methodologist (R1), an IIT-4.0 / complexity expert (R2), and a senior
organization theorist / platform-work skeptic (R3). **Verdict trajectory across four rounds:
3× MAJOR-bordering-reject → 1 MINOR + 2 MAJOR → ACCEPT + 2 MINOR → 1 MAJOR + 2 MINOR.**

- **R2 (IIT expert): MINOR.** All three round-1 technical errors stay fixed (verified each locus:
  the EI identity is gone, "cause-effect power" not "structure," the geometric-Φ retreat). The engine
  computes the genuine Marshall et al. 2023 system measure. One *new* technical finding (the Φ=6.0 /
  normalized-MIP description gap), plus two disclosure refinements (reachability convention, EI
  support). None touches the verdict.
- **R3 (org theorist): MINOR.** Off the round-3 ACCEPT by one notch, on a single ground: the front
  matter still lets "structural fact / material reality" land before the §10 conditional. Standing
  objections (empty unique-zone, operator-choice discretion) are conceded in-draft; R3 credits the
  concessions and asks for cross-references and one promoted clause. No new work.
- **R1 (methodologist): MAJOR.** The dissenter. R1 does not contest a single number. R1 contests the
  *category*: a paper that calls itself an "instrument" and says it "validates" it has, on its own
  §6 admission, validated nothing against the world, and its one zone of unique formal value is
  empirically empty. R1 wants the paper reframed from "instrument validated" to "decision procedure
  specified and demonstrated."

**All three reproduced every load-bearing number exactly.** The arithmetic is not in dispute at
round 4 any more than at round 1. R2 additionally re-derived the complete-cut over-call directly
(chat dyad: every complete tripartition gives Φ ≥ 1 > 0, so a complete-cut test would call the
moderated dyad a triad — the draft's qualitative claim is correct and the deferred numbers in
RESULTS.md were not load-bearing).

## New computation that settles the round-4 charges (`review_response.py` §§8–9)

Two charges were settleable by number rather than rhetoric. Both were computed.

1. **The MIP-normalization charge (R2, new) — CONFIRMED as a description gap, REFUTED as a verdict
   problem (`review_response.py` §8).** §3 describes the test as "find the cut that changes the
   probabilities least … Φ is the damage that cut still does." That is a *raw-minimum* reading. The
   IIT-4.0 measure instead selects the MIP by a *normalized* integration value and reports the
   un-normalized Φ over that partition. The two come apart on magnitude: at the conjunctive channel's
   all-on state the reported Φ is **6.0** while the **minimum raw integration over partitions is 2.0**;
   at the false-dyad triad's all-on state the reported Φ is **2.0** while the raw minimum is **1.0**.
   So §3's prose is loose about the magnitude. But the binary verdict is **invariant**: at every
   reachable state of every case tested, `[reported Φ > 0]` equals `[min-raw Φ > 0]`. The reason is
   structural — a normalization factor is positive and finite, so a partition has normalized Φ = 0
   iff it has raw Φ = 0, and the zero-set is identical whichever minimum is taken. **The classifier is
   untouched, and the finding strengthens the binary-only thesis**: even the reported number is the
   integration at the normalized-MIP, not the raw minimum, which is one more reason it is not a scale.
2. **The "sympathetic caricature" charge (R1) — partly REFUTED by computation
   (`review_response.py` §9).** R1 charges that the rivals' Φ=0 rides on the maximally-favorable inert
   encoding `C'=C` (a frozen spectator). Tested: the dyad verdict survives a *live* context read by
   both parties — `W'=S∨C, S'=W∨C, C'=C` factors, and even `S'=W∧C` (the mediator reading both parties
   jointly) with `C'=C` factors, because a frozen C is not closed into the cycle and the system is not
   strongly connected. So the Φ=0 is **not** an artifact of the inert spectator. What a triad requires
   is C constitutive *and* fed back into the loop (the ATS `C'=S`, the false-dyad `C'=C∧¬S`), which the
   rivals' own channel/context account does not supply. The half of R1's charge that survives is not
   computational: the rival encodings are still the *author's* formalizations of the rival literature,
   and that should be disclosed as a refereeable step rather than asserted as settled.

---

## A. Charges that are REAL (confirmed or refuted by computation; must be addressed)

### A1. §3 mis-describes its own measure on the magnitude (R2, new; CONFIRMED, magnitude-only)
Confirmed by `review_response.py` §8 above. **Real, and a fix-now correction**, but narrow: it is a
description error about a quantity the paper already disclaims as not-a-scale, and it does not touch
the binary verdict (zero-set invariant). Fix: one sentence in §9, where the 6.0 already appears,
noting the reported Φ is the integration at the normalized-MIP and need not be the raw minimum (the
conjunctive channel leaves 6.0 at the selected cut while another cut leaves 2.0), and that the zero —
which is what the classifier uses — is the same whichever way the minimum is read. This *strengthens*
§9's "the number is not a dose." Do not over-correct §3's intuition, which is right for the binary
(some cut does no damage ⟺ Φ=0).

### A2. The reachability convention is predecessor-based, not forward-reachability (R2, new; real disclosure)
`reachable_states()` marks a state reachable iff it has ≥1 predecessor (not "forward-reachable from a
start state"). This is load-bearing: the exhibit's `(1,1,1)` is excluded because it has zero
predecessors, and the draft (§6) does say "states the system has at least one way to enter," which is
the predecessor reading. **Real disclosure gap, fix-now.** A reader will assume forward-reachability
and suspect the exhibit's exclusion is gameable by initial-condition choice; it is not. Fix: one
sentence in §6 or §8 stating "reachable" means "has a predecessor," so the exclusion is principled.

### A3. The EI comparison runs over a different support than Φ (R2, new; real disclosure, conclusion survives)
EI is computed over the full do(uniform) intervention space (all 8 states); Φ is scored over reachable
states only. The inversion claim (§8) is therefore "EI on its own terms does not track the line," not
"EI scored head-to-head against Φ inverts." **Real, fix-now**, one clause in §8 noting the supports
differ by construction. The conclusion is unaffected — EI cannot fall to zero on the strongly-connected
exhibit regardless of support, which is the whole point.

### A4. The pre-registration analogy is a category error (R1; real, not previously raised)
§5 calls the state-alphabet rule "pre-registered … prevents fishing." Pre-registration controls error
inflation across analytic forks in the presence of sampling noise. The model is deterministic — no
sample, no noise, no family of tests, nothing to fish in. What declaring the alphabet in advance
actually prevents is *motivated specification of a deterministic model*, which is a transparency
commitment, not the inferential protection pre-registration supplies. **Real, fix-now.** Fix: replace
"pre-registered … prevents fishing" with the transparency framing (it lets a referee check the rule
was not reverse-engineered from the answer). This is the same boundary §2 polices for IIT — borrowed
authority — and the paper should police it here too.

### A5. The front matter over-states the conditional objectivity (R1, R3; real, the load-bearing honesty seam)
The abstract and §1 say the triad is "a structural fact about that mechanism rather than the analyst's
framing of it" and "not a matter of interpretation once the mechanism is fixed." §10 is precise and
conditional. §4's necessary-not-sufficient result (`review_response.py` §4) shows two criterion-
satisfying reads reach opposite verdicts, so "the eye cannot see it but Φ can" over-reads what is a
function of a declared, contestable model. **Real.** The qualification exists, in the same paper, with
numbers behind it — it just arrives 4,000 words after the strong claim. R3 makes this the single
blocking edit; R1 names the same loci. **This is a framing decision, flagged for author steer in
Section C, not silently rewritten.** The recommended fix is to promote §10's conditional clause into
the abstract and §1, in the same breath as "structural fact," not to retire "structural fact."

### A6. The operator-choice discretion should be cross-referenced, not left implicit (R3; real, fix-now)
§7 defends the conjunction `S'=W∧C` as "the faithful model" of dispatch and states the triad verdict
firmly. §5 concedes the reads are "the method's thinnest joint," disciplined only by case-argument.
The original tautology charge (you added the edge, then reported it matters) is **refuted** — reading
both parties is not sufficient for Φ>0 (the exhibit and the OR-dispatch both read both and factor,
reproduced) — but the discretion is *relocated* to the operator, not dissolved. **Real, fix-now,
cross-reference only:** where §7 calls the conjunction "faithful," point to §5's admission that the
operator is a declared choice an analyst could contest. §7 currently reads as if the conjunction were
given by the phenomenon; §5 knows better.

## B. Charges that are reviewer overreach or already met — hold the line

- **"Not an ORM contribution / measurement paper with no measurement" (R1, MAJOR driver).** This is
  the dissent, and it is overreach *as a rejection ground*, though it carries a real wording fix. R2
  (MINOR) and R3 — an organization theorist, the venue's own constituency — both find the contribution
  ORM-appropriate: a reproducible decision procedure plus a *computed* demonstration that inspection
  over-calls in a way only partition-minimization catches (the exhibit + the EI inversion). R3 is
  explicit that ORM is defensible *because* the exhibit gives the procedure a case where eyeballing
  demonstrably fails. A formal/analytical methods contribution can stand on its formal properties plus
  a discriminating demonstration; world-calibration is Paper 3's by design and is disclosed as such.
  **What is real inside R1's charge** is the word-level inconsistency: the abstract says "validates the
  instrument on controls and worked cases" while §6 says the controls "are a correctness check, not a
  validation." The body is right; the abstract should say "checks," not "validates." That is a fix-now
  wording correction (Section C), not a reframe of the contribution. **Hold the line on the
  contribution; fix the word.**
- **"The conditional warrant does no epistemic work / is nearly trivial" (R1).** Partly overreach. The
  warrant does not rest on verdict-uniqueness (which §4 refutes) but on the construct-proliferation
  *asymmetry*: the rivals, modeled from their own account of their unit, factor, and no live-context
  encoding of them flips to a triad (`review_response.py` §9, new); a faithful platform model does not
  factor. That asymmetry is non-trivial and is the paper's actual §10 position. **Hold the line:** keep
  the warrant resting on the asymmetry, and state it as such. The fix is front-matter tightening (A5),
  not abandonment.
- **"§2 under-stress-tests the disanalogy" (R3).** Minor and partly overreach. §8's exhibit and the EI
  inversion *are* the counterfactual checks Oswick and Ketokivi demand — the cases where the analogy
  would fail if Φ-irreducibility and coordination-irreducibility came apart, built and computed. What
  is fair: §2 should name that "shares a form" is itself the analogical premise (constitution modeled
  as state-coupling), argued by its construct payoff and the EI contrast rather than proven against all
  comers. A one-sentence disclosure in §2 or §10, optional, not blocking.
- **Single-state triad rule (R2, re-raised, now cleared).** R2 itself clears it this round: the rule
  "Φ>0 where both parties are live" is principled, the noise check (2.0→1.53 at 10%) is a legitimate
  if toy robustness argument, and round 3 already disclosed the per-state thinness. No action.

## C. Disposition

**Fix-now (technical corrections and disclosures; no judgment call):**
- A1 — §9 sentence on the normalized-MIP magnitude (computation in `review_response.py` §8).
- A2 — §6/§8 sentence: "reachable" = "has a predecessor," not forward-reachable.
- A3 — §8 clause: EI is computed over the full intervention support, Φ over reachable states.
- A4 — §5: replace "pre-registered … prevents fishing" with the transparency-commitment framing.
- A6 — §7→§5 cross-reference on the operator as a declared, contestable choice.
- Abstract wording: "validates the instrument on controls and worked cases" → "checks," consistent
  with §6 (B, the real core of R1's charge).
- Code hygiene: the stale `~22%` comment in `sweeps.py` line 73 contradicted the 12.5% the script
  computes. **Already scrubbed** in this pass; the script now prints and comments 12.5% (32/256).

**Needs author steer (framing decisions — flagged, not silently rewritten):**
- A5 — how far to promote §10's conditional into the abstract and §1. The recommended move, consistent
  with the standing posture, is to carry the conditional in the same breath as "structural fact," not
  to retire "structural fact." This is the warrant's public face and is the author's call. R3 makes it
  the one edit between MINOR and ACCEPT.
- R1's venue framing — whether to relabel the contribution from "instrument validated" toward "decision
  procedure specified and demonstrated" throughout, or to hold "instrument" and rest on the
  formal-contribution-plus-demonstration defense (R2 and R3's position). The panel majority supports
  holding; R1 dissents. An author decision about self-presentation, not a correctness issue.
- The warrant's strength — state it explicitly as the construct-proliferation asymmetry (rivals factor,
  no faithful rival flips, platform does not), rather than letting "structural fact" imply verdict-
  uniqueness the §4 result denies. Recommended; consistent with §10 already.

**Deferred computation (unchanged from round 3; committed, not faked):**
- ΦID / PID synergy on the exhibit — the single open competitor that might also fire in Φ's unique zone.
- Geometric Φ / Φ* zero-set agreement on the controls + exhibit — converts the §8 family-robustness
  retreat into a tested claim.
- Empirical confirmation of a platform in the strongly-connected-yet-reducible zone — Paper 3's
  measurement task. R3's deepest standing objection (Φ earns its unique keep on no *documented* form)
  is conceded in §10 and stays conceded; the concession must remain loud and not be softened by any
  later edit.

## Standing after round 4

No reviewer found a computational error; every load-bearing number reproduces a fourth time. The one
new technical finding (A1) is magnitude-only and strengthens the binary-only thesis. The split is 1
MAJOR + 2 MINOR, and the MAJOR rests on a venue/framing stance the org-theory reviewer does not share,
plus a real word-level overclaim ("validates") that is a fix-now correction, not a structural defect.
The fix-now items are wording and disclosure; none requires new data or a new model. The author-steer
items are the same warrant-framing decision the paper has faced since round 1: keep the bounded warrant
and the construct-proliferation asymmetry, promote the conditional to the front matter, and decide how
far to relabel "instrument" — held to the standing posture of binary-not-magnitude, no world-validation,
analogy-not-homology, conditional-not-unconditional objectivity, and the conceded empty zone. No new
citation entered the draft this round, so no Crossref check was required.

---

# Stage 4, round 5 (re-review after the Nagel-style rewrite) + adjudication

Between round 4 and this round the draft went through a style-only rewrite (the repo's plain
"Nagel" register: blunt declaratives, no first person, no self-referential hedging). The author
states the rewrite preserved every claim, number, and citation, and did not apply round-4's content
fix-now items. The panel's job this round was new: audit whether a prose pass quietly moved any
claim, then re-press what stands. All three reviewers diffed the restyled draft against the
pre-restyle commit (`git diff HEAD -- DRAFT.md`; round 4 left DRAFT.md untouched, so the diff is the
rewrite in full) and re-ran every script.

**Verdict trajectory across five rounds: 3× MAJOR-bordering-reject → 1 MINOR + 2 MAJOR →
ACCEPT + 2 MINOR → 1 MAJOR + 2 MINOR → 3× MINOR.** The panel is unanimous MINOR for the first time.

- **R2 (IIT expert): MINOR, unchanged — the correct outcome for a style-only pass.** Verified the
  restyle is technically faithful: no changed line altered a measure statement, the power-vs-structure
  fix survives (§3 ¶1 was never touched), the MIP argument, Markov/CI-by-construction, the EI
  inversion, and the exhibit are intact. Every load-bearing number reproduces a fifth time.
- **R3 (org theorist): MINOR, unchanged.** Confirmed the §10 empty-zone concession stayed loud and
  verbatim (the round-4 standing instruction). Judged the blunter prose "on net more honest, not less"
  — it stripped self-praise ("honest limits" → "stated limits", "not hiding a weakness", "not buried")
  that performed rigor rather than stating it. Found one real restyle regression (below).
- **R1 (methodologist): MINOR, down from round-4 MAJOR.** The downgrade is earned by the cumulative
  record, not by the restyle. R1's round-4 MAJOR had two legs: (a) the "not an ORM contribution /
  measurement paper with no measurement" venue stance, which the panel majority — including the
  org-theory reviewer, the venue's own constituency — rejected across four rounds as a rejection
  ground; and (b) the live "validates"/"not a validation" contradiction, a one-word fix-now. With
  leg (a) spent, leg (b) is the definition of MINOR, not MAJOR.

## Restyle fidelity — verified

All three reviewers independently confirmed the rewrite is faithful. No number changed (every value
from 0.415 to the EI row to the 2.0/0.83/6.0/0.0 channel sweep reproduces verbatim). No citation
changed. No section cross-reference was severed. R1 and R2 both checked the warrant/objectivity seam
(abstract, §1, §5, §10) line by line and found the bounded-objectivity claim did not move: the
de-hedging removed exactly the rule-7 meta-commentary the repo's own style guide bans, and the
conditionals those phrases decorated survive in plain declarative form. The §3 four-condition
dependency still reads correctly (the closing noun-piles sit on a stated four-part antecedent, not in
place of it). This is the round's central result: a prose pass that changed 26 paragraphs moved no
claim.

## The one restyle regression (R3; REAL, minor; FIXED this round)

Cutting the §5 clause "and it is named here as an open discipline rather than smoothed over" — a
rule-7 banned tic — also dropped a concession round 3 had added at R1/R3's request: the framing of
the read-faithfulness limit as a discipline the model owes, not merely a fact stated in passing. The
substance survived (the reads "have no rule as tight as the one that fixes the state alphabet,"
"disciplined only by argument about the case," "the method's thinnest joint," "weaker than a verdict
no analyst could move"), so the bold claim did not harden. But R3 is right that the ownership was
quieter. **Fixed:** §5 now reads "That is the method's thinnest joint, and the model has to meet it in
the open, by declaring the reads and defending them on the case." This restores the limit as an owed
discipline in plain substance (an obligation the method carries publicly), without re-importing the
self-referential phrasing the style guide rejects.

## Standing items, all carried from round 4, all still open (deferred by the style-only scope)

The restyle deliberately applied no round-4 content fix. So the round-4 fix-now and author-steer items
remain exactly where they were. The panel re-confirms them:

- **"validates" vs "not a validation" (R1, now panel-agreed fix-now).** Abstract: "validates the
  instrument on controls and worked cases." §6: the controls "are a correctness check, not a
  validation." A live internal contradiction on the paper's self-description, and a one-word fix:
  abstract "validates" → "checks" (the §11 conclusion already says "checked on controls"). Not fatal —
  the body is internally correct — but it should not survive another round.
- **The §3 magnitude gloss / normalization gap (R2 A1, C1–C2).** §3's "the cut that does the least
  damage … Φ is the damage that cut still does" describes a raw-minimum; the measure selects the MIP by
  a normalized value and reports the raw Φ over it (conjunctive channel reports 6.0, raw-min 2.0;
  `review_response.py` §8). Magnitude-only — the binary zero-set is invariant at every state — but §3's
  gloss is literally loose, and §9/§10 do not reconcile it. One sentence in §3 or §9 closes it.
- **The reachability convention (R2 A2, C3).** "Reachable" means has-a-predecessor (in-degree ≥ 1),
  not forward-reachable from a start state. Load-bearing for the exhibit's exclusion of `(1,1,1)`. §6's
  "states the system has at least one way to enter" is in fact this definition, so the draft is
  accurate, but the notion is never named. One clause in §6.
- **Front-matter conditional (R1, R3 A5; author-steer).** "Structural fact / material reality" still
  lands in the abstract and §1 before the §10 conditional is developed. All three agree the conditional
  does travel inside the abstract, so this is a MINOR seam, not a motte-and-bailey. The recommended move
  is unchanged: promote one §10 conditional clause forward. Author's call.
- **Surface the live-context computation in §10 (R1 C3; disclosure, optional).** `review_response.py`
  §9 shows the rivals' Φ=0 survives non-inert "live context" reads (even a joint `S'=W∧C` with `C'=C`
  factors, because a frozen C is not closed into the cycle). The draft does not cite this. One sentence
  in §10 would convert the construct-proliferation asymmetry from a refereeable assertion into a
  computed one the paper already owns.

## Disposition

**Fix-now applied this round:** the §5 restyle regression (R3 C.1) — the only item the rewrite itself
introduced.

**Fix-now still pending (round-4 carryover, deferred by the style-only scope):** abstract
"validates" → "checks"; the §3/§9 normalization-gap sentence; the §6 reachability-convention clause.
All three are one sentence or one word, none changes a claim or a number.

**Author steer (unchanged):** how far to promote the §10 conditional into the front matter; whether to
relabel "instrument" (the panel majority holds it stands as a formal-methods contribution); optionally
cite `review_response.py` §9 in §10.

**Deferred computation (unchanged across rounds):** geometric Φ / Φ* zero-set agreement; ΦID/PID
synergy on the exhibit; the empirical confirmation of the exhibit's zone, which is Paper 3's.

## Standing after round 5

The panel is unanimous MINOR. The Nagel rewrite is verified faithful by three independent diff audits
and a fifth full reproduction of every load-bearing number; it moved no claim and, on net, made the
prose more honest by removing performed rigor. Its single regression — a quieted §5 concession — is
fixed. Everything else between this draft and acceptance is the same short list of one-sentence
disclosures and one word that round 4 already named, plus the standing author-steer on the front-matter
conditional. No reviewer found a computational error in five rounds. No new citation entered, so no
Crossref check was required.

---

# Stage 4, round 6 (re-review of the A5 front-matter edit) + adjudication

Between round 5 and this round, the author applied the remaining fix-now items (abstract "validates"
→ "checks", the §3/§9 normalized-MIP sentence, the §6 reachability clause) and then the A5 author-steer
item: promoting the bounded/conditional objectivity qualifier forward so it travels in the same breath
as the "structural fact" claim in the abstract and §1. This round reviewed the A5 edit. The panel
diffed it against the round-5 commit (`git diff HEAD -- DRAFT.md` = exactly the A5 change) and re-ran
every script.

**Verdict: 2 ACCEPT + 1 MINOR, the MINOR conditioned on one clause that this round then fixed.**
With that clause applied, all three reviewers' stated ACCEPT conditions are met.

- **R2 (IIT expert): ACCEPT, up from round-5 MINOR.** Confirmed A5 is a pure framing edit that
  disturbed no technical claim, no measure description, and no number; all sixteen load-bearing numbers
  reproduce a sixth time. Verified the two round-5 disclosures landed correctly: the §9 normalized-MIP
  sentence matches `review_response.py` §8 (reported 6.0 vs raw-min 2.0, zero-set invariant), and the
  §6 reachability clause matches `instrument.py`'s `reachable_states()` (in-degree ≥ 1, the
  predecessor sense).
- **R3 (org theorist): ACCEPT, up from round-5 MINOR.** A5 was R3's single deferred item. Confirmed the
  bound now travels with the bold claim in the abstract, the correction is balanced (relocated, not
  inflated into a hedge-pile), the construct-proliferation warrant still carries, and the §10 empty-zone
  concession is untouched and still loud.
- **R1 (methodologist): MINOR, conditioned on C1 below; A5 otherwise substantially closed.** R1
  confirmed the restructure preserved every content item from the old abstract and lost nothing, and
  that the edit aligned the abstract with §10 by disclaiming verdict-uniqueness more cleanly than round
  5 did.

## The convergent finding (R1 C1 + R3 C1; REAL; FIXED this round)

R1 and R3 independently flagged the same new seam the A5 edit introduced. The promoted abstract sentence
read "A different faithful model, declared in the open, can give a different verdict." Two problems with
one cause: (R1) "faithful model" drops the locator the bounded-objectivity architecture turns on — the
residual freedom §5 and §10 localize to the reads, not to faithful models at large, so "faithful models
disagree, full stop" concedes more than §5/§10 prove and reads as if the criterion does no disciplining
work; (R3) the same phrase lets a hostile reader stage a reverse motte-and-bailey on the two adjacent
abstract sentences — "structural fact" then "faithful models give different verdicts" looks like
assert-then-retract. Both noted the contradiction does not survive contact with §5/§10 (within-model
determinacy and between-model underdetermination are not contradictory, and the warrant rests on the
construct-proliferation asymmetry, not verdict-uniqueness), and both proposed a one-clause repair.

**Fixed.** The abstract now reads "A different declaration, argued in the open, can give a different
verdict," which (a) drops "faithful model" so it no longer concedes that criterion-meeting models
disagree as such, and (b) matches §1's exact wording, removing the abstract/§1 asymmetry R1 flagged.
R1's secondary point (C2) — the reconciling lock was stranded two sentences downstream of the
concession — is also fixed: "Given a declared mechanism, the verdict is fixed and auditable" was moved
up to sit immediately after the concession, so the abstract now runs the §10 three-beat in order:
bounded → a different declaration can differ → given a declared mechanism the verdict is fixed and
auditable. With C1 applied, R1's stated ACCEPT condition is met.

## The §1 redundancy (R1 C3 + R3 C2; FIXED this round)

Both reviewers noted that the sentence the A5 pass appended to §1 ¶3 ("A different declaration can give
a different verdict, argued in the open") was redundant: §1 ¶3 already carried the full conditional
(the objectivity "is conditional," the criterion "necessary but not sufficient," "the criterion does
not fix the reads," "So the claim is bounded," "auditable against the declaration"), and R3 tied the
addition to the style guide's rule-7 ban on re-explaining a point already made. The abstract was the
real A5 gap; §1 was already bounded in the same breath at its own bold claim ("not a matter of
interpretation once the mechanism is fixed … so the objectivity claimed here is conditional"). **Fixed
by removing the redundant sentence.** §1 retains its full conditional and the consequence (the reads
move the verdict) without the fourth restatement.

## Standing items, unchanged

- **Front-matter conditional (A5): now closed.** The author-steer item is resolved in the locus that
  mattered (the abstract), with the convergent C1/C2 polish applied.
- **Deferred computation (unchanged across rounds):** geometric Φ / Φ* zero-set agreement; ΦID/PID
  synergy on the exhibit; empirical confirmation of the exhibit's zone (Paper 3's). R3's deepest
  standing objection — Φ earns its unique keep on no documented coordination form — remains openly
  conceded in §10 and was not touched by this edit. The standing instruction holds: that concession
  must stay loud through any future edit.

## Standing after round 6

The panel is at unanimous ACCEPT once this round's fixes are counted: R2 and R3 accepted as reviewed,
and R1's MINOR was conditioned solely on C1, which is now applied. The A5 promotion closed the
front-matter seam the panel had carried since round 4 — "structural fact" is kept, and the conditional
now lands in the same breath and is reconciled in the next. The one seam the edit itself opened (the
over-exposed "faithful model" wording) was caught by two reviewers and is fixed in one clause. No number
moved across the A5 round; every load-bearing value reproduced a sixth time. No new citation entered, so
no Crossref check was required.

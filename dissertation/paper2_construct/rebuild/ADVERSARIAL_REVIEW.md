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

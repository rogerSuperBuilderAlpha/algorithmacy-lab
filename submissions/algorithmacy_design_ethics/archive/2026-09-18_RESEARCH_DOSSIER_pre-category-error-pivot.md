# Research Dossier — Algorithmacy and Design Ethics

Synthesis of the Fable-planned harness: 8 parallel research passes, a hypothesis-map audit, a
journal scan, and 3 parallel adversarial-verification passes, against the 9 research questions in
`literature/RESEARCH_PLAN.md`. 99 verified cards in `literature/library/`, indexed in
`literature/library/INDEX.md`. This dossier maps what the harness found back onto the working
definition, says what's solid versus what needs repair, and closes with a thesis recommendation,
an annotated outline, and a journal shortlist.

---

## 1. The definition survives, but its warrant changes

The plan's tightened definition (structural axis = what Φ detects; objective axis = what
cooptation names) survives the harness intact as a working tool. What changes is *how it is
argued*, on two fronts.

**Front one — Verbeek does not supply what the plan hoped.** RQ1's premise was that Φ could
supply "the threshold Verbeek's non-neutrality thesis lacks." Cluster A found the opposite:
Verbeek's framework has no threshold at all — "technologies always mediate" is explicitly the
*extensionist* position his theory is built to reject (`verbeek2015.md`). The channel/party split
that does all the work in this piece's definition has no standing inside postphenomenology as it
stands. That does not sink the argument; it changes its shape. The paper cannot present Φ as
filling a gap Verbeek's own theory already gestures at. It has to argue that postphenomenology
needs a relation type it does not currently have — a bilateral hermeneutic relation, with Φ
supplying its threshold — as a proposed extension, not a reconciliation. Corti et al. (2023) is
the one canonical source that already models two humans and a mediator, and even it has no
independent-objective mediator (`corti2023.md`), so the paper's contribution over Corti still
stands: adding the objective axis.

**Front two — the empirical case for the definition's central claim (almost nothing in the
literature models this) is now very strong, independently, three times over.** Cluster C(i)
found that no classic human-factors automation-trust source — not Lee & See, not Parasuraman &
Riley, not Bainbridge, not Klein et al. — ever models a second human party whose interests the
automation also serves. Cluster E found the sharpest historical near-miss, Suchman's account of
the Winograd–Flores Coordinator: a real 1986 system that *binds* two coworkers through a shared
commitment ledger but does not *interpret* either of them, and whose users kept a working direct
channel around it — Φ near zero by the construct's own test (`suchman1994.md`). Cluster G found
that the two technical mechanisms proposed as a remedy in the report that prompted this whole
project — mechanistic interpretability and C2PA provenance — both fail the same test for the same
reason: each discloses information to one party (whoever holds the model weights; a downstream
content validator), and neither has any representation of a second human party at all
(`mechanistic_interpretability_method.md`, `c2pa_content_provenance_standard.md`). Three
literatures, three independent searches, one converging absence. The INDEX's parties-modeled
census makes this a checkable number rather than an impression: **12 of 99 cards carry the phrase "two
humans + mediator" as their actual object of study.**

**A genuine three-case ladder fell out of the research, unplanned, and is worth building the
paper's exposition around:**

1. **Channel, no independent objective.** The CPDLC party-line literature
   (`hansman1995.md`, `midkiff1993.md`, `pritchett1994.md`) — suppressing the shared voice
   frequency and replacing it with point-to-point datalink satisfies the structural axis (no
   direct channel between the affected pilots) but the mediator itself pursues no objective of its
   own. One real behavioral finding sits here too: crews who overheard a controller's error over
   the open channel mostly stayed silent rather than contest it — the contestation problem,
   observed before any algorithm existed.
2. **Binds but does not interpret; channel survives.** The Winograd–Flores Coordinator
   (`suchman1994.md`, `winograd1994.md`, `winogradflores1986.md`) — a real, decades-old system
   that fails the construct on the *other* side: it never infers anything about either party, and
   the humans could and did talk around it.
3. **Both axes present.** The gig-platform case already verified in the companion
   `algorithmacy_scaffolding` arm (Eslami 2015, Lee 2015, Rahman 2021) — interprets both parties,
   binds both, pursues the platform's own objective, no surviving direct channel.

No planning document specified this ladder; it is a finding, assembled from cards that three
different passes wrote independently. It gives the paper a graded set of real cases instead of one
worked example, and directly answers the plan's own risk that "Φ reads as decoration" — the
Coordinator and the party-line case show the two axes coming apart in the world, not just in
theory.

---

## 2. The nine research questions — what actually came back

**RQ1 (Verbeek vs. Φ threshold).** Resolved above: no agreement to report; a revision to argue
for instead. Latour's "composition" (1994) is the nearest formal analogue to irreducibility, and
Latour explicitly refuses to count mediators arithmetically — a real tension with a fixed Φ that
the paper should name rather than paper over.

**RQ2 (mediation theory and seamful disclosure).** Confirmed and sharpened: asymmetric
seamfulness is real and undertheorized. Verbeek's own res publica test implies asymmetric
disclosure fails ethically (`verbeek2008b.md`), and Latour's photocopier example shows a seam can
restrict a party's agency as readily as it enables another's, depending on who is looking
(`latour1992.md`). This gives the seamful-disclosure affordance a genuine design-ethics
complication it did not have before: *whose* seam, shown to *whom*, is now a variable the paper
can name and argue about.

**RQ3 (Vallor's criterion).** Resolved cleanly, and independently confirmed by S2: Vallor's
technomoral-wisdom criterion does not reduce to "whose objective the friction serves." It is
orthogonal, and adds the formed judge — friction is virtuous when it preserves a practice, which a
structural test alone cannot certify (`vallor2015.md`, confirmed error-free by two independent
passes). One citation correction that matters for the draft: Vallor 2015 never cites MacIntyre and
never uses the word "friction" — her practice concept runs through Aristotle, Annas, and Borgmann.
"A practice in MacIntyre's sense" needs re-attribution before it appears in prose.

**RQ4 (HF automation-trust literature, triadic case).** Both halves resolved. The classic
literature: confirmed absent, independently, across all fourteen sources in Cluster C(i). The
real case: confirmed present, and citable — CPDLC party-line (Cluster C(ii)) and, more weakly, a
clinical decision-support case (`russ2015.md`, whose effect sizes S2 restored after the first pass
under-reported them).

**RQ5 (VSD as rival or complement).** Resolved: complement in form, but with a real limit VSD
cannot fix on its own. Three independent sources (Manders-Huits, Borning & Muller, JafariNaimi)
say VSD has no principle for adjudicating whose values win, and its direct/indirect stakeholder
distinction tracks who receives an output, not who co-determines an outcome — exactly the
distinction Φ draws instead. The strongest single find in this cluster is historical, not
theoretical: Friedman & Nissenbaum's 1996 NRMP case (the National Resident Matching Program) is
the construct's structure in 1996 vocabulary, a full decade before "platform" was a word anyone
used this way.

**RQ6 (Winner's inherently-political claim, object to structure).** Resolved with precision: the
generalization breaks at a named point. Winner's "required authority" (his nuclear-plant example)
is a hierarchy among humans; the triad's required authority is a hub. He never distinguishes "must
be run by a chain of command" from "must pass through one point," and the paper's contribution is
naming that distinction explicitly (`winner1980.md`).

**RQ7 (Floridi's levels of abstraction and faultless responsibility).** Resolved favorably, with
one limit. The Method of Abstraction does more than excuse the Φ verdict's model-relativity — it
obliges the paper to rank its levels of abstraction rather than simply assert one
(`floridisanders2004.md`). Faultless responsibility gives Φ > 0 an allocation consequence: humans
who cannot exit a coordination cannot "rectify" it, so responsibility defaults to the intermediary
— but Floridi's framework treats nodes as morally neutral, which a platform pursuing its own
objective is not. On the hoped-for confirmation that transparency-ideal critics predicted Bo et
al.'s 2025 finding: they did not. Miller (2019) is the real theoretical predecessor
("referring to probabilities... is not as effective as referring to causes"), not Burrell or
Ananny & Crawford. Cite Miller for the prediction, Burrell for the mechanism.

**RQ8 (de Certeau, DiSalvo, Simmel — adversarial design for whom).** Resolved with a genuine
reframe. Simmel's own triad typology answers the question the plan posed as a worry: the two
co-determined humans' antagonism toward each other is the third party's *condition*, not a
complication to design around (`simmel1950.md`). That redirects what "adversarial design" should
target in this construct — restoring the two parties' ability to combine (DiSalvo's third tactic,
articulating collectives) rather than only revealing the intermediary's hegemony (his first
tactic, which is the easier, more obvious fit the affordances already lean on).

**RQ9 (the meta-audit).** The paper's central empirical claim, now confirmed from every angle the
harness could reach: 12/99 cards carry that phrase, and fewer still survive scrutiny of what the mediator actually does — a technology between two humans with its own
objective; the classic HF literature has none; the two technical mechanisms named in the report
that started this project have none; the one near-miss the whole search turned up (the Coordinator)
fails on the interpreting half of the test. This is not an impression the paper can gesture at —
it is now a number, and a reproducible one (grep `Parties modeled:` across the library).

---

## 3. What's solid and needs no repair

Confirmed clean by S2 with no corrections needed: `winner1980.md`, `suchman1994.md`,
`vallor2015.md`, `bainbridge1983.md`, `taddeo2010.md`,
`tsamados2022.md`, `wachter2018.md`, `vasconcelos2023.md`, `winfield2021.md`, `weiser1991.md`,
`verbeek2008b.md`, `verbeek2015.md`, `vandepoel2013.md`, `selbstbarocas2018.md`,
`sarterwoods1995.md`, `thaler2008.md`, `vallor2016.md`, `vallor2024.md`, `winogradflores1986.md`,
`floridisanders2004.md`, `mechanistic_interpretability_method.md`. These can be cited with
confidence at the depth each card states.

## 4. What needs repair before the next draft

- **Citation risk:** "a practice in MacIntyre's sense" (attached to Vallor 2015) must be
  re-attributed — that paper never cites MacIntyre.
- **Load-bearing but unverified this round:** `hirsch2017.md` and `alfrink2023.md` (both RQ5,
  full-text cards whose sources could not be re-opened by S2 — re-check before quoting), and
  `verbeek2011.md`/`verbeek2014.md` (RQ1/RQ2, same status).
- **Largest single gap:** `friedman2019.md` — the VSD book itself is known only from its
  bibliographic record. The cluster's argument currently rests on Friedman's shorter papers and
  her critics; get the book before the VSD section is finalized.
- **Weakest citable HF case:** `skitka1999.md` — statistics could not be independently confirmed
  this round; treat as provisional.
- **A quotation attribution error caught and fixed:** `vallor2010.md` originally presented two
  passages as Vallor's own framing that actually belong to Spence (2011) via the SEP entry that
  carried them — corrected in the card; do not re-introduce the error from an earlier read.

---

## 5. Thesis recommendation

The plan's own recommendation — T2, the friction thesis — is confirmed and sharpened by the
research, not merely rubber-stamped. The original hope was that Vallor's criterion would *reduce
to* the cooptation reading's "whose objective" test, making Φ do real but background work. The
harness found the opposite, and it is a better result for the paper: **Vallor's criterion is
independent of the structural/objective split, not a restatement of it.** That gives the paper two
non-redundant tools instead of one collapsing into the other — Φ tells a designer *when* a third
objective is in the loop at all (the necessary condition for cooptation-relevant friction to be an
issue), and Vallor's formation criterion tells the designer *whether* a given friction is virtuous
once it is (the normative test, which no structural measure can certify). Bainbridge (1983) supplies
the human-factors half of the case independently. The three-case ladder (§1) gives the paper what
the plan said it needed and did not yet have: a worked example — three of them — where the
structural and objective axes visibly diverge.

**T3, the reliance thesis, is now far stronger than "hold until confirmed."** The plan's own
stated risk for T3 — "the case literature may be thinner than I hope" — did not materialize; it is
independently confirmed three times over (Clusters C(i), E, G), and two real field cases exist
with actual data (CPDLC, clinical alerts). Recommend folding T3's central finding into T2 as its
motivating premise, rather than running it as a rival thesis: *appropriate reliance is undefined
for triadic automation* is exactly why a design framework of affordances, rather than better trust
calibration, is the right kind of intervention — which is what T2 already proposes. This keeps the
paper's spine as a single, actionable **design framework** (the user's original ask), with T3's
finding as its strongest piece of motivating evidence rather than a second paper's worth of
scope creep.

T3 on its own remains a strong, separable follow-on paper — `journal_scan_memo.md` independently
found *Philosophy & Technology* already carries a live interlocutor for exactly this argument
(Jovchevski, Buijsman & Neerincx 2026, "What is Wrong With Automation Bias?") with no stated word
cap, which would let the Φ formal apparatus be shown in full rather than compressed. Worth keeping
in reserve as the next piece once this one is out — as the plan itself already suggested for T1.

T1 (mediation) is now a harder paper than planned — Verbeek must be revised, not merely applied —
but a more original one; it remains the natural companion piece for *Philosophy & Technology*,
now with the Corti et al. (2023) lead in hand. T4 (methodology) has a real, three-source-confirmed
finding (VSD cannot adjudicate cooptation) but the plan's own risk stands: three design traditions
plus Φ is a crowded paper, and the strongest new material for it (the Friedman & Nissenbaum 1996
NRMP case) is arguably better spent inside T2 as another worked historical case than as a fourth
paper's spine.

**Recommended thesis for this article:** *Cognitive forcing functions and seamful disclosure are
not competing intuitions about friction to be settled by user preference or designer intent.
Sorted against two independent tests — whether a third, unset objective is in the coordination
loop at all (structural, Φ-detectable) and whether the friction preserves the practice it
interrupts (Vallor's formation criterion) — the friction dilemma resolves into a two-by-two design
rule, illustrated across three real cases spanning the boundary from channel to full triadic
cooptation.*

---

## 6. Target journal

**First: *Ethics and Information Technology*.** Already publishes exactly this territory
(`journal_scan_memo.md`: Malone/Afroogh/D'Cruz 2025 on automation and epistemic agency,
Figueroa et al. 2026 on VSD for platforms, Christiaens 2025 on Airbnb's two-sided rating system —
the last of these is close enough to this paper's own territory to require direct engagement).
Vallor's own 2010 paper is here. Hard 8,000-word ceiling — the formal Φ apparatus goes in an
appendix or a compressed footnote-level treatment, not the body.

**Second: *Design Issues* is eliminated** — the journal scan found zero AI/HCI content in
2025–2026 and a 5,500-word cap, overturning the plan's original guess. Do not target it.

**Third, if the piece runs long or wants the formal apparatus in full: *Philosophy &
Technology*.** No stated word cap; already carries Vallor 2015 and the T3 interlocutor; best
positioned as this paper's natural sequel rather than its first target, given T2 (not T3) is the
recommended spine.

---

## 7. Annotated outline (thesis-supporting skeleton, not drafted prose)

1. **Opening — the report that prompted this.** The "Invisible Scripts" hypothesis map and its
   central error: an AI Context Engine (interpretability + provenance) proposed as a remedy for a
   problem that turns out, on inspection, to be triadic, not dyadic. State the RQ9 verdict early —
   12/99 (weaker on inspection), and the two mechanisms' own founding texts confirm it.
2. **The construct.** The reconciled definition (§1 of `literature/RESEARCH_PLAN.md`), stated as a
   revision of postphenomenology (RQ1), not a reconciliation with it.
3. **The three-case ladder.** CPDLC (structural only) → the Coordinator (neither axis, the sharp
   near-miss) → the gig platform (both axes). Do the argumentative work here, not in a literature
   review section — this is where "Φ is not decoration" gets earned.
4. **The friction dilemma, resolved.** Buçinca/Bo/Rader as the evidence base; Sunstein as the
   opponent; Vallor's formation criterion as the second, independent test; the two-by-two design
   rule as the paper's contribution.
5. **What VSD and contestability-by-design add and cannot add** (RQ5), briefly — enough to place
   the four affordances inside a design process without expanding into a fourth thesis.
6. **Close.** Winner's claim (b), corrected for structure over object (RQ6); the political stakes
   restated at the level of a coordination form, not a device.

## 8. Verification note

Every finding above traces to a specific card in `literature/library/`, each carrying its own read
depth, and every card in this dossier's citation chain has passed adversarial re-verification
(S2) — confirmed, or corrected in place, or explicitly flagged ⚠ where it could not be re-opened
this round. See `literature/library/INDEX.md` for the full status census before any of this enters
a draft.

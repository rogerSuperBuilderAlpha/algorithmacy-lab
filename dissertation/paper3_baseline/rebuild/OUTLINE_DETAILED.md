# Paper 3 — detailed outline (write from this)

Sources: `research/{case_study_methodology,framing_and_positioning,organization_mechanisms}.md`;
numbers from `catalog.py`/`analyze_catalog.py`, `typology.py`, `cases.py`. Style: Nagel (CLAUDE.md),
ORM register, no first person. Verify every academic citation against Crossref before it lands.
Cases are provisional (public-documentation evidence; field data later) — flag per case and in §4.

## §1 Introduction (≈5 paragraphs)

1. Paper 2 answered a yes/no question: is a coordination form a mediated triad (Φ > 0)? Open beat:
   "Paper 2 sorted coordination forms into two kinds. Paper 3 asks how much, and which real
   organizations sit where." The graded score and the five-corporation demonstration.
2. The unit is the coordination form, not the person. Readability analogy: a readability score is a
   property of a text, not of a reader. What is borrowed (a property-of-the-form score); what is not
   (a validated reader-outcome instrument — later work).
3. The headline, stated plainly: the score tracks the structure of how parties reach each other, not
   the seat of the mediator. Name the two equal-Φ pairs (a securities exchange scores like Uber; a
   staffing firm scores like Upwork).
4. The gap: the algorithmic-management literature frames the platform as a dyadic control actor and
   folds structure into the technology's affordances (Kellogg, Valentine & Christin 2020; Vallas &
   Schor 2020; Rahman 2021). No one scores a triadic Worker–System–Counterpart form by structural
   irreducibility so that human and algorithmic mediators of like structure score the same.
5. Roadmap + claim calibration: a demonstration plus replication test (Ridder 2017), not an
   outcome-validation. Preview §3 family, §4 method, §5 five cases, §6 cross-case, §7–9.

## §2 The unit of analysis — the coordination form, not the person (≈4 paragraphs)

1. The readability move, stated and bounded.
2. Coordination theory grounding: Malone & Crowston (1994) — coordination is "managing dependencies
   between activities"; the dependency, not the actor, is the unit; substrate-independent across
   human/computational/biological. Crowston's taxonomy breaks with locating dependencies between
   actors.
3. Brokerage grounding: Burt (1992) — "causation resides in the intersection of relations"; the
   occupant (person or organization) is interchangeable. Halevy, Halali & Zlatev (2019) — brokerage
   (position) vs. brokering (process); triadic configurations. This is structure-not-seat from
   canonical sources, predating the formal model.
4. The graded ladder precedent: Thompson (1967) pooled/sequential/reciprocal; Van de Ven, Delbecq &
   Koenig (1976) add "team"/"intensive". Paper 3's bands extend a known ladder, not an invented one.

## §3 The model and the family — the general application (≈6 paragraphs)

1. Recap the W–S–C model and exact IIT-4.0 Φ from Paper 2 (cite Paper 2; one paragraph, no
   re-derivation). The individuation rule, binary verdict, magnitude ordinal.
2. The catalog: enumerate the complete family — 16³ = 4,096 triad wirings + 48 higher-order = 4,144
   distinct. Coverage/null check, not a census of coordination. (`catalog.py`.)
3. The landscape (`analyze_catalog.py`): 44.1% reducible (Φ=0); seven discrete non-zero bands
   (0.42 / 0.50 / 0.83 / 1.00 / 1.50 / 2.00 / 6.00). The bands are a property of the family, not
   assigned. Table.
4. What drives Φ (OLS, all triads): strict mediation +0.54 (meanΦ 0.90 vs 0.53), parity +0.27, edges
   +0.24; R² = 0.196 — Φ is not a feature checklist. That residual is the irreducibility the
   construct captures.
5. The Cerullo (2015) caution, computed: parity (XOR/XNOR) mediators meanΦ 0.85 vs monotone 0.535 →
   read magnitude ordinally only; lean on binary Φ=0 / Φ>0.
6. The typology placed (`typology.py`): organizations fall on populated bands (0 / 0.50 / 0.83 /
   2.00 / 3.00). Typology-as-theory framing (Doty & Glick 1994): the bands are ideal types with
   falsifiable placements derived from structure. Tie to the §2 ladder.

## §4 Methods for the case studies (≈6 paragraphs)

1. Register and aim: Yin theory-driven demonstration of the Paper 2 instrument (Ridder 2017's "gaps
   and holes"), not Eisenhardt theory-building. Calibrate: demonstration + replication, not
   definitive test (Ridder's caution that case-based testing is weaker than experimental).
2. Case selection: theoretical/diverse-case sampling (Seawright & Gerring 2008) — maximum variance
   on determination structure; control extraneous variance by holding party count fixed (Burnham et
   al. 2008). The cut-anchor lesson turned into method.
3. The five cases + replication roles: the two equal-Φ pairs (literal replication on Φ + theoretical
   contrast on seat); MTurk higher-order theoretical replication. Table.
4. Modeling procedure: Paper 2's pre-registered individuation rule; pre-register each determination
   structure before computing (the structures are fixed in `cases.py` from the mechanisms research);
   report Φ, band, MIP.
5. Rigor as inferential reasoning (Harley & Cornelissen 2022): justify the chain organization →
   documented evidence → classifier inputs → Φ → coordination-form claim, not a checklist.
   Transparency (Pratt 2008's four questions).
6. Provisional-status disclosure: the case evidence is public documentation (filings, ToS, regulatory
   pages, AWS docs) to be replaced/supplemented with field data; no established convention for
   pre-fieldwork cases, so it is an honest transparency disclosure. Each case marks its evidence
   status.

## §5 The five cases (within-case; per-case anatomy from methodology §6)

Per case: (i) bounded unit & context; (ii) data sources & chain of evidence (provisional-marked);
(iii) within-case description of the coordination; (iv) the analytic operation (model + Φ from
`cases.py`); (v) alternative explanations / rival codings.

### §5.1 Uber — strict mediation — Φ 2.00 — algorithmic
- Unit: the rider↔driver coordination at the application layer (a single trip match).
- Evidence: Uber 10-K; Platform Access Agreement (2022); marketplace page; patent US20170011324A1.
- Description: platform commits the dispatch as a joint function of both parties' states (positions,
  ETA, geography); driver and rider reach each other only through it; off-app contact restricted
  (§2.6(c)).
- Operation: `W'=S, S'=W∧C, C'=S` → Φ 2.00, MIP {W,SC}.
- Rivals: if the rider info were freely shared / off-app contact unrestricted (a back-channel), the
  form would move toward partial mediation; the contractual restriction is what keeps it strict.
  Flag the agent/principal accounting nuance (2-1).

### §5.2 NYSE / Nasdaq (securities exchange) — strict mediation — Φ 2.00 — market institution
- Unit: the buyer↔seller coordination in a single security's order matching.
- Evidence: Nasdaq Systems Description (SEC); NYSE market-model + auctions fact sheet; DTCC CNS/NSCC.
- Description: the exchange commits the match (price-time priority book; opening/closing crosses);
  buyers and sellers never transact directly; NSCC novates as central counterparty so each faces the
  clearinghouse. Same strict-mediation structure as Uber, a market-institution seat.
- Operation: `W'=S, S'=W∧C, C'=S` → Φ 2.00. The twin of §5.1 at a different seat — the headline.
- Rivals/notes: the CCP/multilateral-netting layer is a documented higher-order feature (one
  determination binds many members) — note it as a richer model the basic strict triad brackets;
  "counterparty-anonymous" wording contested (refuted 1-2), no-direct-contact substance holds.

### §5.3 Upwork — partial mediation — Φ 0.83 — algorithmic
- Unit: the client↔freelancer coordination around a contract.
- Evidence: Upwork Circumvention & Conversion-Fee articles; 10-K; User Agreement §7.
- Description: the platform matches and hosts, but client and freelancer coordinate directly
  on-platform; anti-circumvention polices only the off-platform boundary (the fee depends on
  on-platform payment). A direct channel is present, so the structure does not fully reduce to
  mediation.
- Operation: `W'=S∨C, S'=W∧C, C'=S∨W` → Φ 0.83, MIP {W,SC} at max.
- Rivals: the anti-circumvention rule is the documented analogue of Paper 2 §9's "platform suppresses
  the direct channel" — but only off-platform; on-platform the channel is open, which is why the form
  is partial, not strict. If the platform forbade all direct contact, it would move toward strict.

### §5.4 ManpowerGroup — partial mediation — Φ 0.83 — human-institutional
- Unit: the placed-worker↔client-firm coordination on an assignment.
- Evidence: manpower.com "Working for Manpower"; ManpowerGroup 10-K (SEC); jurisdictional staffing
  descriptions.
- Description: the agency commits the placement and is the employer of record, but the client directs
  the day-to-day work on-site — a continuous direct channel. Same partial-mediation structure as
  Upwork, a human-institutional seat. The twin of §5.3.
- Operation: `W'=S∨C, S'=W∧C, C'=S∨W` → Φ 0.83.
- Rivals: temp-to-perm / non-circumvention contractual terms (not documented on the public page) could
  tighten or loosen the direct channel — flag for field data.

### §5.5 Amazon Mechanical Turk — higher-order strict mediation — Φ 3.00 (n=4) — algorithmic
- Unit: the requester↔worker(s) coordination on a HIT.
- Evidence: AWS Mechanical Turk Requester docs (concepts; approve/reject); mturk.com worker help.
- Description: requester posts a HIT to a pool; workers self-select; the platform commits the
  allocation and sits in the payment path (reward transferred on approval); a single HIT can bind
  many workers ("you can assign many Workers to work on the same HIT"). No direct requester–worker
  channel.
- Operation: `S'=W∧C∧D` (n=4) → Φ 3.00. One determination binds >3 parties — the higher-order reach.
- Rivals/caveat: cross-node Φ is partly a function of system size (carry the Paper-2 caveat); a
  single-assignment HIT is an ordinary strict triad (2.00). The higher-order score is not strictly
  comparable to the 0–2.00 band.

## §6 Cross-case synthesis (≈4 paragraphs)

1. The display matrix (Miles & Huberman 1994): rows = dimensions (parties reach each other only
   through S?; direct channel?; determination; Φ band; seat); columns = the five cases ordered
   partial → strict → higher-order. The summary table in `organization_mechanisms.md`.
2. The two equal-Φ pairs carry the headline: same structure, different seat, same score. State the
   equality is a modeling property (true once both are coded to the same structure), not an empirical
   discovery — the Paper-2 honesty posture.
3. The cases sit on populated bands of the §3 family (0.83, 2.00, 3.00 are populated; 824 / 496 / HO
   wirings) — not cherry-picked.
4. What the cases add beyond the model: the tool sorts real, documented coordination by structure,
   cutting against the industry label and the mediator's nature — a court-like exchange, a staffing
   firm, and a gig platform land by structure, not by sector or seat.

## §7 Discussion (≈4 paragraphs)

1. Structure, not seat, sets the score — connect to coordination theory (substrate-independence),
   brokerage (position over occupant), two-sided markets (structural criterion). The formal model
   makes a claim those literatures assert qualitatively into a computed one.
2. The orthogonality move (preempt the Rahman objection): Φ measures structural irreducibility, the
   analytic object; opacity, power, accountability are orthogonal contingencies layered on an
   identical structural score, not part of it. Continuity with Paper 2 §4 (epistemic opacity vs.
   compositional irreducibility are independent).
3. What the tool buys an analyst: a sector-blind, seat-blind placement of a coordination form on a
   graded scale, and a discipline against reading triadicity off the industry label or the mediator's
   technology.
4. Relation to the typology-as-theory bar (Doty & Glick): the bands are derived, falsifiable
   placements, not a convenience classification.

## §8 Limitations (≈1–2 paragraphs)

Demonstration, not outcome-validation (Ridder); cases provisional pending fieldwork; magnitude ordinal
(Cerullo); cross-node (n=4) not strictly comparable; the equivalence claim is structural, bracketing
normative/distributive consequences; single modeling choices (reads, individuation) carried from
Paper 2 §5 — declared, contestable, auditable.

## §9 Conclusion (≈1 paragraph)

The graded structural typology plus the five-case demonstration: a sector- and seat-blind score of
coordination structure that does analytic work on real corporations. Forward: outcome-validation
(vary structure at fixed party count against an observed outcome) is the remaining empirical program;
the matched person-level instrument is later work.

## Back matter
Data and code availability (the `rebuild/` scripts, named at point of use). References (Crossref-
verified; Paper 2's bib is the shared base; add the §2–§4 methodology and framing cites).

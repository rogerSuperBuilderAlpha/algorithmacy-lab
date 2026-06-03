# Paper 3 — fieldwork case-study TEMPLATE (placeholder field content)

> ⚠️ **THIS FILE CONTAINS FABRICATED PLACEHOLDER CONTENT.** It is scaffolding, not evidence.
> Every tagged item is invented to show the *shape* a fieldwork case study would take, so the
> real data can later be dropped in. **Do not cite, quote, or submit any tagged content, and do
> not let any of it reach `DRAFT.md`.**
>
> Tagging convention (all greppable):
> - `⟦FAKE⟧ …` — an inline fabricated claim, quote, figure, or detail. Replace with real data.
> - `〔FIELD PLACEHOLDER — fabricated, replace〕` — a whole subsection that is invented.
> - "Informant X-N (placeholder)" — a fictional informant. No real person is named or quoted.
>
> **What is REAL in this file and stays:** the bounded unit, the public-documentation facts (the
> same ones in `DRAFT.md` §5, sourced in `research/organization_mechanisms.md`), the modeled
> determination structure, and the computed Φ (from `cases.py`). Everything tagged is fake.
>
> **How to use it:** for each case, run the field protocol, then replace every `⟦FAKE⟧` and every
> `〔FIELD PLACEHOLDER〕` block with the real data you collect. The "What field data must
> establish" checklist tells you exactly which facts each placeholder stands in for. The Φ band
> for a case only moves if the field data flips one of the two structural bits (only-through-S?,
> direct-channel?); the checklists are aimed at those bits and at the lived texture around them.
>
> To find everything that must be replaced: `grep -nE "⟦FAKE⟧|FIELD PLACEHOLDER|placeholder" CASES_FIELDWORK_TEMPLATE.md`

---

## Per-case anatomy (each case below follows this)

1. Bounded unit and context — REAL (public).
2. Evidence base — a source table marking REAL (public document) vs PLACEHOLDER (field).
3. Field protocol (planned) — REAL plan; the data it would yield is placeholder until collected.
4. Within-case: the documented mechanism — REAL.
5. Within-case: lived coordination — 〔FIELD PLACEHOLDER〕.
6. The analytic operation — REAL (model + Φ from `cases.py`).
7. Triangulation and member check — 〔FIELD PLACEHOLDER〕.
8. Alternative explanations — REAL rival codings + 〔FIELD PLACEHOLDER〕 field-informed sensitivity.
9. What field data must establish here — REAL checklist (the replacement targets).

---

# Case 1 — Uber (ride-hailing). Strict mediation. Φ = 2.00.

**1. Unit and context (REAL).** The coordination between a rider and a driver around a single
trip, at the application layer. Uber characterizes itself as a technology intermediary connecting
riders and independent drivers.

**2. Evidence base.**

| Source | Type | Status |
|---|---|---|
| Uber Form 10-K; Platform Access Agreement (US, 2022); marketplace/matching page; patent US20170011324A1 | public document | REAL |
| Driver interviews (n = ⟦FAKE: 12⟧) | field | PLACEHOLDER |
| Rider interviews (n = ⟦FAKE: 8⟧) | field | PLACEHOLDER |
| Ride-along field notes (⟦FAKE: 3 shifts, ~18 hours⟧) | field | PLACEHOLDER |
| Screen-recording of the dispatch flow | field | PLACEHOLDER |

**3. Field protocol (planned, REAL).** Recruit drivers across tenure and city; semi-structured
interviews on how a match arrives, what is visible before/after accept, and whether any off-app
contact occurs. Ride-alongs to observe the dispatch-to-pickup flow. Interview riders on whether
they ever choose or contact a specific driver. Code each transcript for the two structural bits.

**4. Documented mechanism (REAL).** The platform commits the dispatch as a joint function of both
parties' states (positions, ETA, geography); rider and driver reach each other only through it;
the Platform Access Agreement §2.6(c) restricts off-app contact and rider-information use.

**5. 〔FIELD PLACEHOLDER — fabricated, replace〕 Lived coordination.**
⟦FAKE⟧ Drivers describe the match as arriving with no say over who the rider is:
> ⟦FAKE quote⟧ "You get the ping, you've got maybe ten seconds, and you don't even see the name
> till you swipe. You take what it gives you." — Informant U-D1 (placeholder driver-informant)

⟦FAKE⟧ Riders report never selecting or contacting a particular driver:
> ⟦FAKE quote⟧ "I just request. Whoever shows up, shows up. I've never picked a driver." —
> Informant U-R3 (placeholder rider-informant)

⟦FAKE⟧ Field note: across ⟦3⟧ ride-alongs, every trip originated from a system-pushed dispatch;
no instance of a driver and rider arranging a ride directly was observed.

**6. The analytic operation (REAL).** Model rider, platform, driver as W, S, C at the
trip-matching layer (the unit rule): `W' = S`, `S' = W ∧ C`, `C' = S`. Φ = 2.00 at the all-on
state, MIP {W, SC}. Strict mediation. (`cases.py`.)

**7. 〔FIELD PLACEHOLDER — fabricated, replace〕 Triangulation and member check.** ⟦FAKE⟧ The
"no direct channel" coding triangulates across the Platform Access Agreement (document), driver
interviews (the ten-second blind accept), and ride-along observation. ⟦FAKE⟧ A member check with
⟦2⟧ driver-informants confirmed the "you can't pick or reach the rider" reading.

**8. Alternative explanations.** REAL: if the back-channel were open (drivers and riders routinely
arranging rides off-app), the form moves toward partial mediation; the contractual restriction is
what keeps it strict. 〔FIELD PLACEHOLDER〕 ⟦FAKE⟧ Field check for off-app arranging: ⟦0 of 12⟧
drivers reported a standing off-app rider relationship sourced through Uber, supporting the strict
coding; ⟦if the real number is non-trivial, the coding weakens toward partial⟧.

**9. What field data must establish here (REAL checklist).**
- [ ] Whether riders and drivers ever reach each other *without* the dispatch (the direct-channel bit). *Decides strict vs partial.*
- [ ] Whether the match is experienced as committed by the system vs negotiated (the only-through-S bit).
- [ ] How enforced the off-app-contact restriction is in practice (the §5.1 caveat: contract text ≠ enforcement).
- [ ] Real informant quotes to replace U-D1, U-R3.
- [ ] Real n's and field-note hours to replace the ⟦FAKE⟧ counts in the evidence table.

---

# Case 2 — NYSE / Nasdaq (securities exchange). Strict mediation. Φ = 2.00.

**1. Unit and context (REAL).** The coordination between a buyer and a seller in a single
security's order matching.

**2. Evidence base.**

| Source | Type | Status |
|---|---|---|
| Nasdaq systems description (SEC); NYSE market-model & auction fact sheet; DTCC CNS / NSCC pages | public document | REAL |
| Interviews with market participants / traders (n = ⟦FAKE: 6⟧) | field | PLACEHOLDER |
| Interview with an exchange or clearing operations contact (n = ⟦FAKE: 1⟧) | field | PLACEHOLDER |
| Observation of the order-entry-to-execution flow on a trading desk | field | PLACEHOLDER |

**3. Field protocol (planned, REAL).** Interview buy- and sell-side participants on whether a
counterparty is ever known or chosen at the point of execution; interview an exchange/clearing
operations contact on the matching and novation flow; observe an order's path from entry to
execution to clearing. Code for the two structural bits at the matching layer.

**4. Documented mechanism (REAL).** The exchange commits the match (price-time priority book;
opening/closing crosses); buyers and sellers never transact directly; NSCC novates as central
counterparty so each side faces the clearinghouse. Joint function of all resting interest.

**5. 〔FIELD PLACEHOLDER — fabricated, replace〕 Lived coordination.**
⟦FAKE⟧ Participants describe never selecting a counterparty at execution:
> ⟦FAKE quote⟧ "You send the order to the book. You have no idea who's on the other side, and you
> don't care — the exchange matches it and the clearinghouse becomes your counterparty." —
> Informant X-T2 (placeholder trader-informant)

⟦FAKE⟧ Field note: on a ⟦half-day⟧ desk observation, every execution was anonymous at the point
of match; counterparty identity was never surfaced to the trader.

**6. The analytic operation (REAL).** Model buyer, exchange, seller as W, S, C at the
order-matching layer (the unit rule sends this case to matching, not clearing): `W' = S`,
`S' = W ∧ C`, `C' = S`. Φ = 2.00. Same Boolean system as Uber; identical TPM, identical score by
construction. (`cases.py`.)

**7. 〔FIELD PLACEHOLDER — fabricated, replace〕 Triangulation and member check.** ⟦FAKE⟧ The
anonymous-joint-match coding triangulates across the Nasdaq systems description (document), trader
interviews (no counterparty choice), and desk observation. ⟦FAKE⟧ Member check with an operations
contact confirmed the matching-then-novation flow.

**8. Alternative explanations.** REAL: a market-maker reading, where each party transacts against
the system's own posted quote (`S' = S`), gives Φ = 0.00, a reducible dyad with a spectator
(`review_response.py`); the order-driven joint-match coding is defended on the documented matching
rule. The clearing layer (multilateral netting binding many members) is a higher-order structure
named, not modeled. 〔FIELD PLACEHOLDER〕 ⟦FAKE⟧ Field check: ⟦whether the focal market is
order-driven vs quote-driven for the security studied⟧ — confirm the order-driven coding holds for
the specific venue/security.

**9. What field data must establish here (REAL checklist).**
- [ ] Whether the studied venue/security is order-driven (joint match) or quote-driven (market-maker as principal). *Decides 2.00 vs 0.00.*
- [ ] That buyer and seller are anonymous and never coordinate directly at the matching layer (only-through-S).
- [ ] Real participant/operations quotes to replace X-T2.
- [ ] Confirmation that the matching layer is the right unit for the focal coordination (vs clearing).

---

# Case 3 — Upwork (freelance marketplace). Partial mediation. Φ = 0.83 (max over reachable).

**1. Unit and context (REAL).** The coordination between a client and a freelancer around a
contract.

**2. Evidence base.**

| Source | Type | Status |
|---|---|---|
| Upwork Circumvention & Conversion-Fee articles; User Agreement §7; Form 10-K | public document | REAL |
| Freelancer interviews (n = ⟦FAKE: 10⟧) | field | PLACEHOLDER |
| Client interviews (n = ⟦FAKE: 6⟧) | field | PLACEHOLDER |
| Walkthrough of a contract from match to delivery (screen capture) | field | PLACEHOLDER |

**3. Field protocol (planned, REAL).** Interview freelancers and clients on how they coordinate
once matched (on-platform messaging, calls, scope changes), and on whether and when they move
off-platform; walk through a live contract. Code for the direct-channel bit (present on-platform?
suppressed off-platform?).

**4. Documented mechanism (REAL).** The platform matches and hosts the contract and payment, but
client and freelancer coordinate directly inside the platform; the anti-circumvention rule polices
only the off-platform boundary (the fee depends on on-platform payment); a conversion fee lets the
relationship move off-platform lawfully once paid.

**5. 〔FIELD PLACEHOLDER — fabricated, replace〕 Lived coordination.**
⟦FAKE⟧ Freelancers describe coordinating directly with clients on-platform:
> ⟦FAKE quote⟧ "Once we're matched we just talk in the messages — scope, deadlines, all of it. The
> platform's there for the contract and the payment, but the work is between us." — Informant
> P-F4 (placeholder freelancer-informant)

⟦FAKE⟧ Clients report the platform polices leaving, not talking:
> ⟦FAKE quote⟧ "They don't mind us working closely on here. They mind if you try to take it to
> email and pay outside." — Informant P-C2 (placeholder client-informant)

**6. The analytic operation (REAL).** Model freelancer, platform, client as W, S, C:
`W' = S ∨ C`, `S' = W ∧ C`, `C' = S ∨ W`. Max Φ over reachable states = 0.83 (at the two states
where one party is live); reducible at the all-on state. Partial mediation. (`cases.py`.)

**7. 〔FIELD PLACEHOLDER — fabricated, replace〕 Triangulation and member check.** ⟦FAKE⟧ The
direct-channel-present coding triangulates across the User Agreement (off-platform restriction
only), freelancer/client interviews (on-platform direct work), and the contract walkthrough.

**8. Alternative explanations.** REAL: coding the match as a disjunction (`S' = W ∨ C`) gives
Φ = 6.00, off the populated scale; the conjunction is defended on the mechanism (a match commits
only when both a willing client and a willing freelancer are present). Forbid all direct contact
and the form moves toward strict mediation. 〔FIELD PLACEHOLDER〕 ⟦FAKE⟧ Field check: ⟦how much real
coordination is on-platform vs off-platform⟧, and whether the platform's enforcement effectively
closes the on-platform channel for any class of work.

**9. What field data must establish here (REAL checklist).**
- [ ] That client and freelancer *do* coordinate directly on-platform (the direct-channel bit that makes it partial, not strict).
- [ ] How hard the off-platform boundary is enforced, and whether that ever collapses the on-platform channel.
- [ ] Real informant quotes to replace P-F4, P-C2.

---

# Case 4 — ManpowerGroup (staffing firm). Partial mediation. Φ = 0.83 (max over reachable).

**1. Unit and context (REAL).** The coordination between a placed worker and a client firm on an
assignment.

**2. Evidence base.**

| Source | Type | Status |
|---|---|---|
| manpower.com "Working for Manpower"; ManpowerGroup Form 10-K; jurisdictional staffing terms | public document | REAL |
| Placed-worker interviews (n = ⟦FAKE: 9⟧) | field | PLACEHOLDER |
| Client-firm supervisor interviews (n = ⟦FAKE: 5⟧) | field | PLACEHOLDER |
| Manpower recruiter/branch interview (n = ⟦FAKE: 2⟧) | field | PLACEHOLDER |
| Copy of a placement contract / assignment agreement | field | PLACEHOLDER |

**3. Field protocol (planned, REAL).** Interview placed workers on who directs their daily work
and how much they deal with the client vs the agency once placed; interview client supervisors and
a recruiter; obtain the assignment agreement to check any non-circumvention / temp-to-perm terms.
Code for the direct-channel bit.

**4. Documented mechanism (REAL).** The agency screens and commits the placement and is the legal
employer of record for temporary roles; the client directs the day-to-day work on-site; the agency
does not stand between the parties' working relationship.

**5. 〔FIELD PLACEHOLDER — fabricated, replace〕 Lived coordination.**
⟦FAKE⟧ Placed workers describe a continuous direct channel with the client:
> ⟦FAKE quote⟧ "Manpower's my employer on paper and for the paycheck, but day to day my supervisor
> is the client's floor manager. I barely talk to the agency once I'm placed." — Informant
> M-W2 (placeholder placed-worker-informant)

⟦FAKE⟧ A client supervisor describes directing the work directly:
> ⟦FAKE quote⟧ "Once they're on our floor they're ours to manage. We don't route anything through
> the agency for the daily stuff." — Informant M-C1 (placeholder client-supervisor)

**6. The analytic operation (REAL).** Model worker, agency, client as W, S, C, the same partial-
mediation system as Upwork: `W' = S ∨ C`, `S' = W ∧ C`, `C' = S ∨ W`. Max Φ over reachable states
= 0.83. Partial mediation; the human-institutional twin of Upwork by identical coding. (`cases.py`.)

**7. 〔FIELD PLACEHOLDER — fabricated, replace〕 Triangulation and member check.** ⟦FAKE⟧ The
direct-channel-present coding triangulates across Manpower's worker guidance (on-site supervisor
for daily questions), worker/supervisor interviews, and the assignment agreement.

**8. Alternative explanations.** REAL: temp-to-perm conversion terms and any non-circumvention
clause (not on the public worker-facing page) could tighten or loosen the direct channel and move
the score. 〔FIELD PLACEHOLDER〕 ⟦FAKE⟧ Field check: ⟦whether the assignment agreement restricts the
worker and client from dealing directly or converting around the agency⟧ — obtain the actual
contract; this is the document most likely to move the coding.

**9. What field data must establish here (REAL checklist).**
- [ ] Who legally directs day-to-day work (client vs agency) and whether worker and client coordinate directly (the direct-channel bit).
- [ ] The actual assignment-agreement terms on direct dealing / conversion (the rival-coding pivot).
- [ ] Real informant quotes to replace M-W2, M-C1.

---

# Case 5 — Amazon Mechanical Turk (crowdwork). Higher-order strict mediation. Φ = 3.00 raw, 1.00 normalized.

**1. Unit and context (REAL).** The coordination between a requester and the worker or workers on
a task (HIT).

**2. Evidence base.**

| Source | Type | Status |
|---|---|---|
| AWS Mechanical Turk requester & worker documentation | public document | REAL |
| Worker interviews (n = ⟦FAKE: 11⟧) | field | PLACEHOLDER |
| Requester interviews (n = ⟦FAKE: 4⟧) | field | PLACEHOLDER |
| Walkthrough of posting, accepting, and approving a HIT | field | PLACEHOLDER |

**3. Field protocol (planned, REAL).** Interview workers on how they find/accept HITs and whether
they ever deal directly with a requester; interview requesters on qualifications, multi-worker
assignment, and approval/payment; walk through a HIT end to end. Code for the only-through-S bit
and the higher-order (one determination binds >2 parties) feature.

**4. Documented mechanism (REAL).** The requester posts a HIT to the marketplace; workers
self-select, accept, submit; the requester gates with qualifications and approves/rejects; the
platform sits in the payment path; a single HIT can be assigned to many workers at once. No direct
requester-worker channel.

**5. 〔FIELD PLACEHOLDER — fabricated, replace〕 Lived coordination.**
⟦FAKE⟧ Workers describe no direct contact with requesters:
> ⟦FAKE quote⟧ "You never talk to the requester. You take the HIT, you do it, you submit, and you
> hope they approve. It all goes through Amazon." — Informant T-W5 (placeholder worker-informant)

⟦FAKE⟧ Requesters describe assigning one HIT to many workers for consensus:
> ⟦FAKE quote⟧ "I put each task out to ⟦FAKE: five⟧ workers and take the majority answer. I never
> pick a specific person — the qualifications do the gating." — Informant T-R1 (placeholder
> requester-informant)

**6. The analytic operation (REAL).** Model requester, platform, and two workers as a four-node
system: `S' = W ∧ C ∧ D`, each party reading the system. Raw Φ = 3.00 at n = 4. Φ = n − 1 for
strict-AND mediation, so the size-normalized score Φ/(n − 1) = 1.00 — the same structural level as
the strict triad pair, scaled by party count. Higher-order strict mediation. (`cases.py`,
`review_response.py`.)

**7. 〔FIELD PLACEHOLDER — fabricated, replace〕 Triangulation and member check.** ⟦FAKE⟧ The
no-direct-channel, multi-worker coding triangulates across AWS documentation, worker/requester
interviews, and the HIT walkthrough.

**8. Alternative explanations.** REAL: a single-assignment HIT (one requester, one worker through
the platform) is an ordinary strict triad at Φ = 2.00; the higher-order coding applies when one
determination binds more than two parties, and the raw 3.00 is a size artifact (the normalized
1.00 is the comparable value). 〔FIELD PLACEHOLDER〕 ⟦FAKE⟧ Field check: ⟦the typical number of
workers per HIT in the studied requester's tasks⟧ — sets whether the higher-order coding or the
single-assignment strict triad is the faithful one.

**9. What field data must establish here (REAL checklist).**
- [ ] Whether requesters and workers ever coordinate directly (only-through-S bit).
- [ ] The typical workers-per-HIT (decides higher-order vs ordinary strict triad).
- [ ] Real informant quotes to replace T-W5, T-R1; real worker/requester n's.

---

# Cross-case (fieldwork version)

**REAL:** the cross-case display matrix and the structural reading are unchanged from `DRAFT.md`
§6 — the cases sort by the two structural bits (only-through-S?, direct-channel?), the two
equal-Φ pairs are identity-by-construction demonstrations of seat-blind coding, and the cases sit
on populated bands of the family.

**〔FIELD PLACEHOLDER — fabricated, replace〕** ⟦FAKE⟧ Cross-case field synthesis: across all five
sites, the structural-bit codings derived from public documents were ⟦confirmed / revised⟧ by the
field data, with the only coding-relevant revision at ⟦Case X⟧, where ⟦the direct-channel bit
flipped because …⟧. Replace with the actual cross-case finding once the five sites are collected.

**What the cross-case field data must establish (REAL):**
- [ ] For each case, whether the field data confirms or flips either structural bit (and thus the band).
- [ ] Whether any case's enforcement-in-practice diverges from its documented rule (the standing caveat across Uber §5.1, Upwork §5.3, ManpowerGroup §5.4).
- [ ] A member-checked statement, per case, that the structural coding matches how informants describe the coordination.

---

## Replacement map (REAL — the find-and-replace guide)

| Placeholder kind | How to replace |
|---|---|
| `⟦FAKE: n⟧` counts in evidence tables | real informant/observation counts once collected |
| `⟦FAKE quote⟧ … — Informant XX-N (placeholder)` | a real, consented, anonymized quote (keep the informant-label scheme or substitute your IRB scheme) |
| `〔FIELD PLACEHOLDER〕` lived-coordination blocks | the within-case field narrative |
| `〔FIELD PLACEHOLDER〕` triangulation blocks | the actual triangulation across document/interview/observation |
| `〔FIELD PLACEHOLDER〕` field-informed sensitivity in §8 | the real field check on the rival-coding pivot |
| cross-case field synthesis | the real cross-case finding |

When every `⟦FAKE⟧` and `〔FIELD PLACEHOLDER〕` is gone (verify with the grep above), the field
version of §5–§6 is ready to fold into `DRAFT.md`, and the provisional-status disclosures in the
draft's front matter and §4 can be lifted for the sites that now have field data.

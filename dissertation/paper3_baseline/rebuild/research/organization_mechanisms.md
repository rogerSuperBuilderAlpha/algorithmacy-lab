# Stage 2c research — coordination mechanisms of the five organizations

Evidence base for the within-case models (§5). Synthesis of the per-organization deep research
(workflow `wf_e784e341-676`; Uber, NYSE/Nasdaq, Upwork verified 3-vote) plus targeted primary-source
fetches for the two the workflow left open (ManpowerGroup, Amazon Mechanical Turk). Sources here are
mostly first-party / regulatory (SEC filings, terms of service, AWS docs, exchange/clearing pages) —
they support the **case evidence**, not the academic bibliography. All five confirm the locked Φ
band. **Provisional:** the author replaces/supplements these with field data; each input's status is
flagged in the case.

## 1. Uber — strict mediation, Φ = 2.00 (algorithmic)

- **Parties:** rider (counterpart C) and independent driver (worker W); Uber is the system S.
- **Determination (joint function of both):** the platform commits the dispatch/match. Uber's
  marketplace page: "we evaluate nearby drivers and riders in one batch … then pair riders and
  drivers"; "closest doesn't always mean quickest." Patent US20170011324A1: a "matching engine …
  computes an optimization score … for each of the proximate drivers" from user, driver, location,
  and ETA data. The 10-K lists "matching and dispatching" among its marketplace technologies. The
  match is a joint function of both parties' states.
- **Back-channel:** contractually restricted. Platform Access Agreement §2.6(c): "Without a Rider's
  consent, you agree to not contact any Rider or otherwise use any of the Rider's User Information
  except solely in connection with the provision of Rides." Drivers see only approximate locations.
- **Structural reading:** the parties reach each other only through the platform's joint
  determination, no direct channel → **strict mediation**. Model `W'=S, S'=W∧C, C'=S` → Φ 2.00.
- **Flags:** "Uber merely arranges" is bounded to core ride-hailing US-GAAP accounting (gross-basis
  exceptions in Delivery/Freight; UK law treats Uber as principal) — vote 2-1. The §2.6(c)
  restriction is the contract text, not evidence of enforcement; rider-consent is a carve-out.
- **Sources:** Uber 10-K (SEC CIK 0001543151); Platform Access Agreement (US, 2022-01-01);
  uber.com/marketplace/matching; patent US20170011324A1.

## 2. NYSE / Nasdaq (securities exchange) — strict mediation, Φ = 2.00 (market institution)

- **Parties:** buyer (W) and seller (C); the exchange is the system S.
- **Determination (joint function of all resting interest):** the matching engine commits the trade.
  Nasdaq Systems Description (SEC): "no single specialist through which transactions pass … an order
  execution algorithm that adheres to … price-time priority." Opening/Closing Crosses select the
  single price maximizing executed shares. NYSE adds a floor parity/priority model with one DMM per
  security and centralized opening/closing auctions.
- **Back-channel:** none — buyers and sellers do not transact directly; the exchange interposes its
  match. At the clearing layer, NSCC (DTCC subsidiary, est. 1976) **novates as central counterparty**
  so each side faces the clearinghouse, not each other.
- **Higher-order feature:** through Continuous Net Settlement, NSCC multilaterally nets all of a
  member's trades in a security into one position per member against NSCC — a single determination
  collapsing many bilateral obligations (payments reduced ~98%/day, self-reported).
- **Structural reading:** parties reach each other only through the exchange's joint determination →
  **strict mediation**, Φ 2.00 — the twin of Uber at a different seat. The CCP/netting layer is a
  documented higher-order structural feature available for a richer model or a discussion note.
- **Flags:** "non-directed / counterparty-anonymous" wording was refuted 1-2 (the precise
  contra-party-assignment mechanics are contested); the no-direct-contact substance holds. "DMM
  controls the determination" overstates DMM discretion (price is a function of aggregated orders).
  NYSE floor parity is specific to NYSE; NYSE American moved to electronic price-time priority in 2017.
- **Sources:** Nasdaq Market Center Systems Description (SEC); NYSE market-model and Opening/Closing
  Auctions Fact Sheet; DTCC CNS and NSCC pages.

## 3. Upwork — partial mediation, Φ = 0.83 (algorithmic)

- **Parties:** freelancer (W) and client (C); Upwork is the system S.
- **Determination:** the platform matches and hosts the contract, but **client and freelancer
  coordinate directly** within the platform (messaging, the working relationship). The match is a
  joint function, and the parties also read each other directly.
- **Back-channel:** present on-platform; the platform polices only the **off-platform** boundary.
  Anti-circumvention (User Agreement §7): meeting through Upwork then "trying to continue the
  relationship elsewhere" is a ToS breach, because "we can't keep running our marketplace without the
  fee we get when clients pay freelancers." A Conversion Fee lets the relationship move off-platform
  lawfully after payment (24-month non-circumvention window).
- **Structural reading:** the parties keep a direct channel (on-platform), so the structure does not
  reduce to pure mediation → **partial mediation**. Model `W'=S∨C, S'=W∧C, C'=S∨W` → Φ 0.83. The
  anti-circumvention rule is the documented analogue of Paper 2 §9's "platform has a reason to
  suppress the direct channel" — but here only the *off-platform* channel.
- **Flags:** permanent-account-closure is "can result in," not automatic (Conversion-Fee exception) —
  vote 2-1; off-platform contact is permitted once the fee is paid.
- **Sources:** Upwork Circumvention support article; Conversion Fee article; Upwork 10-K
  (SEC, upwk-20231231); User Agreement §7.

## 4. ManpowerGroup — partial mediation, Φ = 0.83 (human-institutional)

- **Parties:** placed worker / associate (W) and client firm (C); ManpowerGroup is the system S.
- **Determination + employer-of-record structure:** Manpower screens, assesses (MyPath), and commits
  the placement. For temporary roles, "you are employed through Manpower and placed on assignment at
  our client's worksite" — Manpower is the **legal employer of record**; the **client directs the
  day-to-day work**: "your supervisor at the work site is your resource for daily work-related
  questions, Manpower is your employer." (Permanent placements are direct client employment, not a
  Manpower employee.)
- **Back-channel:** strong and continuous — once placed, worker and client coordinate directly on-site
  (daily supervision). Manpower commits the match and remains the employer, but does not stand between
  the parties' day-to-day work.
- **Structural reading:** the agency commits the match while the parties keep a direct working channel
  → **partial mediation**, Φ 0.83 — the human-institutional twin of Upwork, same structure, different
  seat. Model `W'=S∨C, S'=W∧C, C'=S∨W` → Φ 0.83.
- **Flags:** the page does not address contractual restrictions on the client hiring the worker around
  the agency (temp-to-perm conversion terms / non-circumvention) — open for field data; the
  co-employment/legal-direction split should be corroborated from the 10-K (SEC man-20241231) and
  jurisdiction-specific terms.
- **Sources:** manpower.com "Working for Manpower"; ManpowerGroup 10-K (SEC, man-20241231);
  manpowergroup.jp temporary-staffing description.

## 5. Amazon Mechanical Turk — higher-order strict mediation, Φ = 3.00 (n=4, algorithmic)

- **Parties:** requester (C) and worker(s) (W…); Amazon/the platform is the system S, and also the
  payment intermediary.
- **Determination:** the requester posts a HIT (a "single, self-contained task") to the marketplace;
  workers find, accept, and submit; the requester approves/rejects. **Workers self-select from a pool**
  rather than the requester contacting a specific worker; the requester gates access with
  Qualification Types (Approval Rate, Masters, custom). The platform commits the allocation and the
  payment: on approval "Mechanical Turk transfers the reward from your Amazon.com account to the
  Worker's Amazon.com account"; if the deadline passes "Mechanical Turk approves the assignments and
  pays the Workers."
- **Back-channel:** none — requester and worker connect only through the platform; there is no direct
  channel, and Amazon sits in the payment path.
- **Higher-order:** a single HIT can bind more than two parties. AWS docs: "You can assign many
  Workers to work on the same HIT … this guarantees that multiple Workers must complete a HIT that has
  multiple assignments." So one determination binds requester + multiple workers (+ Amazon as payment
  intermediary).
- **Structural reading:** strict mediation (no direct channel, joint determination committed by the
  platform) with a determination binding >3 parties → **higher-order strict mediation**, Φ 3.00 at
  n=4. Model `W'=S, S'=W∧C∧D, C'=S, D'=S`.
- **Flags:** cross-node (n=4) Φ is partly a function of system size and is not strictly comparable to
  the 0–2.00 triad band (carry the Paper-2 caveat). The "many workers per HIT" feature is what makes
  it higher-order; a single-assignment HIT is an ordinary strict triad (2.00).
- **Sources:** AWS Mechanical Turk Requester docs (mechanical-turk-concepts; ApproveRejectWork);
  mturk.com worker help.

## Cross-case structural summary (for the §6 display matrix)

| Case | Parties reach each other only through S? | Direct channel? | Determination | Φ band | Seat |
|---|---|---|---|---|---|
| Uber | yes | no (restricted) | joint dispatch | 2.00 | algorithmic |
| NYSE/Nasdaq | yes | no (CCP novates) | joint order match | 2.00 | market institution |
| Upwork | no | yes (on-platform) | joint match | 0.83 | algorithmic |
| ManpowerGroup | no | yes (on-site) | joint placement | 0.83 | human-institutional |
| Amazon MTurk | yes | no | joint allocation, >2 parties | 3.00 (n=4) | algorithmic |

The two equal-Φ pairs (Uber≈exchange at 2.00; Upwork≈ManpowerGroup at 0.83) differ on seat, not
structure — the structure-not-seat headline, grounded in real documented mechanisms.

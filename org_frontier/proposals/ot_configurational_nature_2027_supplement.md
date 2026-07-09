# Online supplement — When is a combination a configuration?

*Companion to the manuscript. Every table below is generated from the replication package's committed
sources, not transcribed by hand: Part A from the two-measure robustness computation, Part B from the
intermediary-catalog study, Part C from the encoding-sensitivity demonstration, Part D from the
coordination-logic atlas, and Part E from the membership-law battery and the integration-game
computation. Commands to re-derive each part accompany the replication package (see the final
section).*

## Part A — the manuscript's model forms: rules, transitions, and Φ under two measures

Rules are synchronous Boolean updates; a state lists node values in label order. Φ is whole-system
integrated information at that state: IIT 4.0 (`pyphi.new_big_phi`) and IIT 3.0 (`pyphi.compute`,
`DIRECTED_BI` partitions). Only reachable states carry Φ values; verdicts in the manuscript are the
sign of the maximum over reachable states.

### CTRL+ — read-recipient triad

Rules: E′ = M;  M′ = E ∧ R;  R′ = M

| state (E,M,R) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 000 | 000 | yes | 0.0000 | 0.4150 |
| 100 | 000 | no | — | — |
| 010 | 101 | yes | 0.0000 | 1.4150 |
| 110 | 101 | no | — | — |
| 001 | 000 | no | — | — |
| 101 | 010 | yes | 0.0000 | 2.5000 |
| 011 | 101 | no | — | — |
| 111 | 111 | yes | 2.0000 | 3.5000 |

### CTRL- — two disjoint dyads

Rules: A′ = B;  B′ = A;  C′ = D;  D′ = C

| state (A,B,C,D) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 0000 | 0000 | yes | 0.0000 | 0.0000 |
| 1000 | 0100 | yes | 0.0000 | 0.0000 |
| 0100 | 1000 | yes | 0.0000 | 0.0000 |
| 1100 | 1100 | yes | 0.0000 | 0.0000 |
| 0010 | 0001 | yes | 0.0000 | 0.0000 |
| 1010 | 0101 | yes | 0.0000 | 0.0000 |
| 0110 | 1001 | yes | 0.0000 | 0.0000 |
| 1110 | 1101 | yes | 0.0000 | 0.0000 |
| 0001 | 0010 | yes | 0.0000 | 0.0000 |
| 1001 | 0110 | yes | 0.0000 | 0.0000 |
| 0101 | 1010 | yes | 0.0000 | 0.0000 |
| 1101 | 1110 | yes | 0.0000 | 0.0000 |
| 0011 | 0011 | yes | 0.0000 | 0.0000 |
| 1011 | 0111 | yes | 0.0000 | 0.0000 |
| 0111 | 1011 | yes | 0.0000 | 0.0000 |
| 1111 | 1111 | yes | 0.0000 | 0.0000 |

### E1 — quorum 1-of-3

Rules: P0′ = P1′ = P2′ = S;  S′ = [P0+P1+P2 ≥ 1]

| state (P0,P1,P2,S) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 0000 | 0000 | yes | 3.0000 | 6.2500 |
| 1000 | 0001 | no | — | — |
| 0100 | 0001 | no | — | — |
| 1100 | 0001 | no | — | — |
| 0010 | 0001 | no | — | — |
| 1010 | 0001 | no | — | — |
| 0110 | 0001 | no | — | — |
| 1110 | 0001 | yes | 0.0000 | 1.1926 |
| 0001 | 1110 | yes | 0.0000 | 5.2500 |
| 1001 | 1111 | no | — | — |
| 0101 | 1111 | no | — | — |
| 1101 | 1111 | no | — | — |
| 0011 | 1111 | no | — | — |
| 1011 | 1111 | no | — | — |
| 0111 | 1111 | no | — | — |
| 1111 | 1111 | yes | 0.0000 | 0.1926 |

### E2 — quorum 2-of-3

Rules: P0′ = P1′ = P2′ = S;  S′ = [P0+P1+P2 ≥ 2]

| state (P0,P1,P2,S) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 0000 | 0000 | yes | 0.0000 | 1.2688 |
| 1000 | 0000 | no | — | — |
| 0100 | 0000 | no | — | — |
| 1100 | 0001 | no | — | — |
| 0010 | 0000 | no | — | — |
| 1010 | 0001 | no | — | — |
| 0110 | 0001 | no | — | — |
| 1110 | 0001 | yes | 0.0000 | 1.2688 |
| 0001 | 1110 | yes | 0.0000 | 1.2688 |
| 1001 | 1110 | no | — | — |
| 0101 | 1110 | no | — | — |
| 1101 | 1111 | no | — | — |
| 0011 | 1110 | no | — | — |
| 1011 | 1111 | no | — | — |
| 0111 | 1111 | no | — | — |
| 1111 | 1111 | yes | 0.0000 | 1.2688 |

### E3 — quorum 3-of-3

Rules: P0′ = P1′ = P2′ = S;  S′ = [P0+P1+P2 ≥ 3]

| state (P0,P1,P2,S) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 0000 | 0000 | yes | 0.0000 | 0.1926 |
| 1000 | 0000 | no | — | — |
| 0100 | 0000 | no | — | — |
| 1100 | 0000 | no | — | — |
| 0010 | 0000 | no | — | — |
| 1010 | 0000 | no | — | — |
| 0110 | 0000 | no | — | — |
| 1110 | 0001 | yes | 0.0000 | 5.2500 |
| 0001 | 1110 | yes | 0.0000 | 1.1926 |
| 1001 | 1110 | no | — | — |
| 0101 | 1110 | no | — | — |
| 1101 | 1110 | no | — | — |
| 0011 | 1110 | no | — | — |
| 1011 | 1110 | no | — | — |
| 0111 | 1110 | no | — | — |
| 1111 | 1111 | yes | 3.0000 | 6.2500 |

### E4 — rotation (4-cycle of copyists)

Rules: A′ = D;  B′ = A;  C′ = B;  D′ = C

| state (A,B,C,D) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 0000 | 0000 | yes | 2.0000 | 2.0000 |
| 1000 | 0100 | yes | 2.0000 | 2.0000 |
| 0100 | 0010 | yes | 2.0000 | 2.0000 |
| 1100 | 0110 | yes | 2.0000 | 2.0000 |
| 0010 | 0001 | yes | 2.0000 | 2.0000 |
| 1010 | 0101 | yes | 2.0000 | 2.0000 |
| 0110 | 0011 | yes | 2.0000 | 2.0000 |
| 1110 | 0111 | yes | 2.0000 | 2.0000 |
| 0001 | 1000 | yes | 2.0000 | 2.0000 |
| 1001 | 1100 | yes | 2.0000 | 2.0000 |
| 0101 | 1010 | yes | 2.0000 | 2.0000 |
| 1101 | 1110 | yes | 2.0000 | 2.0000 |
| 0011 | 1001 | yes | 2.0000 | 2.0000 |
| 1011 | 1101 | yes | 2.0000 | 2.0000 |
| 0111 | 1011 | yes | 2.0000 | 2.0000 |
| 1111 | 1111 | yes | 2.0000 | 2.0000 |

### E5 — one-sided veto (lockstep)

Rules: W′ = S;  S′ = W ∧ ¬C;  C′ = S

| state (W,S,C) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 000 | 000 | yes | 0.0000 | 0.4150 |
| 100 | 010 | no | — | — |
| 010 | 101 | yes | 0.0000 | 1.4150 |
| 110 | 111 | no | — | — |
| 001 | 000 | no | — | — |
| 101 | 000 | yes | 0.0000 | 0.4150 |
| 011 | 101 | no | — | — |
| 111 | 101 | yes | 0.0000 | 1.4150 |

### E6 — dispatch, full triad

Rules: W′ = ¬S;  S′ = W ∧ C;  C′ = C ∧ ¬S

| state (W,S,C) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 000 | 100 | yes | 0.0000 | 0.0000 |
| 100 | 100 | yes | 0.0000 | 0.0000 |
| 010 | 000 | yes | 0.0000 | 0.4150 |
| 110 | 000 | no | — | — |
| 001 | 101 | no | — | — |
| 101 | 111 | yes | 0.0000 | 2.0000 |
| 011 | 000 | no | — | — |
| 111 | 010 | yes | 2.0000 | 2.4150 |

### E7 — dispatch, rider dropped

Rules: W′ = ¬S;  S′ = W;  C′ = C ∧ ¬S

| state (W,S,C) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 000 | 100 | yes | 0.0000 | 0.0000 |
| 100 | 110 | yes | 0.0000 | 0.0000 |
| 010 | 000 | yes | 0.0000 | 0.0000 |
| 110 | 010 | yes | 0.0000 | 0.0000 |
| 001 | 101 | no | — | — |
| 101 | 111 | yes | 0.0000 | 0.0000 |
| 011 | 000 | no | — | — |
| 111 | 010 | yes | 0.0000 | 0.0000 |

### E8 — maximal wiring (6 edges, no constants)

Rules: W′ = ¬(S ∨ C);  S′ = ¬W ∧ C;  C′ = ¬(W ∧ S)

| state (W,S,C) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |
|---|---|---|---|---|
| 000 | 101 | yes | 0.0000 | 0.6917 |
| 100 | 101 | no | — | — |
| 010 | 001 | no | — | — |
| 110 | 000 | no | — | — |
| 001 | 011 | yes | 0.0000 | 0.2767 |
| 101 | 001 | yes | 0.0000 | 0.2767 |
| 011 | 011 | yes | 0.0000 | 0.2767 |
| 111 | 000 | no | — | — |

## Part B — the intermediary catalog: entries, coding, and classification

Each entry is a real or stylized coordination arrangement with a mediating third, coded to one of four
structural templates and classified by the bypass-counterfactual (restore the forbidden direct tie,
recompute, read whether the mediator stays in the core). The `expected` column records the coding;
`class` and `margin` (whole-system Φ lost when the bypass opens) are the computed result. Because the
computed class follows the structural template by construction — margin is constant within a template —
agreement between coding and classification checks the pipeline's consistency, not a prediction. The
catalog's contribution is the coding itself: which real constraint holds which arrangement in which
template. Coding rule for `expected`: an entry is coded *contingent* when an
identifiable external constraint (statute, license, exclusive contract, standard, friction) is the only
stated reason the parties cannot transact directly; *necessary* when the mediator computes a joint
condition the direct tie cannot reproduce; *partial* when a direct channel already runs alongside the
mediated one; *reducible* when the direct tie is already open and unconstrained. As the manuscript
notes, outcomes were known to the coders; the exercise disciplines the distinction rather than tests
it.

Fields coded per entry: `bypass`, `constraint`, `constraint_type`, `domain`, `expected`, `mediator`, `name`, `reading`, `sink`, `source`, `template`.

| # | entry | domain | template | constraint type | expected | class | margin |
|---|---|---|---|---|---|---|---|
| 1 | car_dealer | auto retail | relay | franchise law | contingent | contingent | 2.000 |
| 2 | liquor_distributor | alcohol | relay | three-tier law | contingent | contingent | 2.000 |
| 3 | customs_broker | trade | relay | licensing mandate | contingent | contingent | 2.000 |
| 4 | notary | legal instruments | relay | statutory witnessing | contingent | contingent | 2.000 |
| 5 | prescription_refill | pharmacy | relay | dispensing law | contingent | contingent | 2.000 |
| 6 | title_passthrough | real estate | relay | recording requirement | contingent | contingent | 2.000 |
| 7 | clearinghouse_ccp | finance | conjunctive | none (integrates) | necessary | necessary | 0.000 |
| 8 | interpreter | language | conjunctive | none (integrates) | necessary | necessary | 0.000 |
| 9 | court_adjudication | law | conjunctive | none (integrates) | necessary | necessary | 0.000 |
| 10 | escrow_conditional | real estate | conjunctive | none (integrates) | necessary | necessary | 0.000 |
| 11 | travel_agent | travel | additive | none (eroding) | partial | partial | 1.585 |
| 12 | insurance_broker | insurance | additive | none (eroding) | partial | partial | 1.585 |
| 13 | unexclusive_reseller | retail | free | none | reducible | reducible | 0.000 |
| 14 | tertius_gaudens | brokerage | relay | maintained gap [Simmel 1908] | contingent | contingent | 2.000 |
| 15 | structural_hole_broker | brokerage | relay | structural hole [Burt 1992] | contingent | contingent | 2.000 |
| 16 | granovetter_bridge | networks | relay | bridge tie [Granovetter 1973] | contingent | contingent | 2.000 |
| 17 | tertius_iungens_integrating | brokerage | conjunctive | none [Obstfeld 2005] | necessary | necessary | 0.000 |
| 18 | tertius_iungens_selfliquidating | brokerage | free | none [Obstfeld 2005] | reducible | reducible | 0.000 |
| 19 | simmelian_mediator | sociology | conjunctive | none [Simmel 1908] | necessary | necessary | 0.000 |
| 20 | gf_coordinator | brokerage | free | within-group [Gould-Fernandez 1989] | reducible | reducible | 0.000 |
| 21 | gf_gatekeeper | brokerage | relay | group boundary [Gould-Fernandez 1989] | contingent | contingent | 2.000 |
| 22 | gf_liaison | brokerage | relay | two boundaries [Gould-Fernandez 1989] | contingent | contingent | 2.000 |
| 23 | two_sided_platform | economics | conjunctive | none [Rochet-Tirole 2003] | necessary | necessary | 0.000 |
| 24 | gatekeeping_platform | economics | relay | access control [Hagiu 2009] | contingent | contingent | 2.000 |
| 25 | market_maker | economics | additive | none [Rubinstein-Wolinsky 1987] | partial | partial | 1.585 |
| 26 | arbitrageur_friction | economics | relay | search friction [Rubinstein-Wolinsky 1987] | contingent | contingent | 2.000 |
| 27 | bail_bondsman | criminal justice | relay | law: cash bail | contingent | contingent | 2.000 |
| 28 | title_insurer | real estate | relay | law: lender requirement | contingent | contingent | 2.000 |
| 29 | real_estate_appraiser | real estate | relay | law: lender requirement | contingent | contingent | 2.000 |
| 30 | immigration_attorney | legal | relay | law: representation rules | contingent | contingent | 2.000 |
| 31 | accreditation_body | education | relay | law: funding gate | contingent | contingent | 2.000 |
| 32 | app_store_30pct | software | relay | monopoly: walled garden | contingent | contingent | 2.000 |
| 33 | ticketmaster | live events | relay | monopoly: exclusive contracts | contingent | contingent | 2.000 |
| 34 | mls_realty | real estate | relay | monopoly: cartel rules | contingent | contingent | 2.000 |
| 35 | domain_registrar | internet | relay | monopoly: root authority | contingent | contingent | 2.000 |
| 36 | swift_messaging | finance | relay | network: standard lock-in | contingent | contingent | 2.000 |
| 37 | freight_broker | logistics | relay | friction: fragmentation | contingent | contingent | 2.000 |
| 38 | union_hiring_hall | labor | relay | collective bargaining | contingent | contingent | 2.000 |
| 39 | payment_network_auth | finance | conjunctive | none (joint authorization) | necessary | necessary | 0.000 |
| 40 | stock_exchange | finance | conjunctive | none (order matching) | necessary | necessary | 0.000 |
| 41 | credit_bureau | finance | conjunctive | none (cross-lender aggregate) | necessary | necessary | 0.000 |
| 42 | air_traffic_control | aviation | conjunctive | none (joint deconfliction) | necessary | necessary | 0.000 |
| 43 | auction_house | art & collectibles | conjunctive | none (price discovery) | necessary | necessary | 0.000 |
| 44 | patent_pool_sso | standards | conjunctive | none (pools licensors) | necessary | necessary | 0.000 |
| 45 | pharmacy_benefit_manager | healthcare | additive | formulary + rent gate | partial | partial | 1.585 |
| 46 | ride_hail_platform | mobility | additive | matching + bypassable | partial | partial | 1.585 |
| 47 | gpo_healthcare | healthcare | additive | aggregation + bypassable | partial | partial | 1.585 |
| 48 | talent_agent | entertainment | additive | curation + access gate | partial | partial | 1.585 |
| 49 | newspaper_classifieds | media | free | none (Craigslist opened it) | reducible | reducible | 0.000 |
| 50 | indie_record_label | music | free | none (direct distribution) | reducible | reducible | 0.000 |
| 51 | retail_middleman_dtc | retail | free | none (DTC brands) | reducible | reducible | 0.000 |

Class tally: contingent=25, necessary=13, partial=7, reducible=6 (n = 51).
Entries whose computed class differs from the coded expectation: none (a pipeline-consistency check; see the note above on why agreement is expected by construction).

## Part C — the ten-case encoding-sensitivity demonstration

Ten stylized organizational arrangements, each encoded as a small Boolean form with the prediction
fixed before computation; five carry a second, equally defensible encoding of the same story (the
sensitivity variant). Four of the ten flip verdict between the two encodings — the figure the
manuscript cites. The rules are stipulated to demonstrate the protocol's mechanics, not elicited from
field evidence, and the transition tables below are generated from the same committed rules that
produced the verdicts.

| id | arrangement | parties | base verdict (Φ) | sensitivity variant | variant verdict | flips |
|---|---|---|---|---|---|---|
| M1 | Ride-hail dispatch | D P R | triadic (Φ=2.0) | substitutable drivers | dyadic | True |
| M2 | Relay manager | W1 M W2 | dyadic (Φ=0.0) | synthesizing manager | triadic | True |
| M3 | Substitutable-seller marketplace | B P S1 S2 | dyadic (Φ=0.0) | specialized seller | triadic | True |
| M4 | CI code-review gate | A G M | triadic (Φ=1.0) | — | — | — |
| M5 | EHR shift handoff | N1 E N2 | dyadic (Φ=0.0) | active-checklist EHR | triadic | True |
| M6 | Franchise with ratings feedback | F S C | triadic (Φ=2.0) | — | — | — |
| M7 | Algorithmic ranking | Cr A Ad | triadic (Φ=2.0) | — | — | — |
| M8 | Support-ticket triage | Cu T Ag | triadic (Φ=2.0) | — | — | — |
| M9 | Grievance arbitration | W Ar E | triadic (Φ=2.0) | — | — | — |
| M10 | ERP / EDI supply link | Su ERP Bu | dyadic (Φ=0.0) | — | — | — |

Transition tables (base encoding, and the variant where one exists):

**M1 — Ride-hail dispatch** (base encoding)

| state (D,P,R) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 000 | no |
| 010 | 101 | yes |
| 110 | 101 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M1 — variant: substitutable drivers** (If any available driver is interchangeable (the platform reads a pool via OR), no single driver is pivotal and the arrangement factors — the worker dissolves into the pool.)

| state (D1,D2,P,R) | next | reachable |
|---|---|---|
| 0000 | 0000 | yes |
| 1000 | 0000 | no |
| 0100 | 0000 | no |
| 1100 | 0000 | no |
| 0010 | 1101 | yes |
| 1010 | 1101 | no |
| 0110 | 1101 | no |
| 1110 | 1101 | no |
| 0001 | 0000 | no |
| 1001 | 0010 | no |
| 0101 | 0010 | no |
| 1101 | 0010 | yes |
| 0011 | 1101 | no |
| 1011 | 1111 | no |
| 0111 | 1111 | no |
| 1111 | 1111 | yes |

**M2 — Relay manager** (base encoding)

| state (W1,M,W2) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 010 | no |
| 010 | 101 | yes |
| 110 | 111 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M2 — variant: synthesizing manager** (A manager who commits a decision that needs both reports (M = W1 ∧ W2, both read M) binds the workers; one who only forwards does not. The verdict turns on whether the manager commits a determination neither worker controls.)

| state (W1,M,W2) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 000 | no |
| 010 | 101 | yes |
| 110 | 101 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M3 — Substitutable-seller marketplace** (base encoding)

| state (B,P,S1,S2) | next | reachable |
|---|---|---|
| 0000 | 0000 | yes |
| 1000 | 0000 | no |
| 0100 | 1011 | yes |
| 1100 | 1011 | no |
| 0010 | 0000 | no |
| 1010 | 0100 | no |
| 0110 | 1011 | no |
| 1110 | 1111 | no |
| 0001 | 0000 | no |
| 1001 | 0100 | no |
| 0101 | 1011 | no |
| 1101 | 1111 | no |
| 0011 | 0000 | no |
| 1011 | 0100 | yes |
| 0111 | 1011 | no |
| 1111 | 1111 | yes |

**M3 — variant: specialized seller** (If the buyer needs a particular seller (no substitute), the same platform reads triadic. Substitutability, not the platform, is what made it dyadic.)

| state (B,P,S) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 000 | no |
| 010 | 101 | yes |
| 110 | 101 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M4 — CI code-review gate** (base encoding)

| state (A,G,M) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 010 | yes |
| 010 | 000 | yes |
| 110 | 011 | no |
| 001 | 000 | no |
| 101 | 010 | no |
| 011 | 100 | yes |
| 111 | 111 | yes |

**M5 — EHR shift handoff** (base encoding)

| state (N1,E,N2) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 010 | no |
| 010 | 101 | yes |
| 110 | 111 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M5 — variant: active-checklist EHR** (A record that gates the handoff on a checklist both nurses must complete (E = N1 ∧ N2) commits a determination neither controls; a passive store does not.)

| state (N1,E,N2) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 000 | no |
| 010 | 101 | yes |
| 110 | 101 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M6 — Franchise with ratings feedback** (base encoding)

| state (F,S,C) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 001 | yes |
| 010 | 100 | no |
| 110 | 101 | no |
| 001 | 000 | yes |
| 101 | 011 | yes |
| 011 | 100 | yes |
| 111 | 111 | yes |

**M7 — Algorithmic ranking** (base encoding)

| state (Cr,A,Ad) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 000 | no |
| 010 | 101 | yes |
| 110 | 101 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M8 — Support-ticket triage** (base encoding)

| state (Cu,T,Ag) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 010 | yes |
| 010 | 001 | yes |
| 110 | 011 | yes |
| 001 | 100 | yes |
| 101 | 110 | yes |
| 011 | 101 | yes |
| 111 | 111 | yes |

**M9 — Grievance arbitration** (base encoding)

| state (W,Ar,E) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 000 | no |
| 010 | 101 | yes |
| 110 | 101 | no |
| 001 | 000 | no |
| 101 | 010 | yes |
| 011 | 101 | no |
| 111 | 111 | yes |

**M10 — ERP / EDI supply link** (base encoding)

| state (Su,ERP,Bu) | next | reachable |
|---|---|---|
| 000 | 000 | yes |
| 100 | 001 | no |
| 010 | 000 | no |
| 110 | 001 | yes |
| 001 | 110 | yes |
| 101 | 111 | no |
| 011 | 110 | no |
| 111 | 111 | yes |

## Part D — the quorum sweep and the manuscript's other atlas forms, with cores

From the coordination-logic atlas (fifty exactly solved forms, predictions fixed per form before
computation). Rows below are the forms the manuscript's section 3 uses: the full quorum sweep at two
to five parties, the rotation, and the one-sided veto, with each form's maximal complex (core) — the
membership information Part A's whole-system values do not carry. Verdicts here are the IIT 4.0
measure.

| atlas id | form | predict | binds | core | core Φ | whole-system Φ |
|---|---|---|---|---|---|---|
| A21 | 2-party k=1-of-2 | triadic | True | P0P1S | 2.000 | 2.000 |
| A22 | 2-party k=2-of-2 | triadic | True | P0P1S | 2.000 | 2.000 |
| A31 | 3-party k=1-of-3 | triadic | True | P0P1P2S | 3.000 | 3.000 |
| A32 | 3-party k=2-of-3 | dyadic | False | — | 0.000 | 0.000 |
| A33 | 3-party k=3-of-3 | triadic | True | P0P1P2S | 3.000 | 3.000 |
| A41 | 4-party k=1-of-4 | triadic | True | P0P1P2P3S | 4.000 | 4.000 |
| A42 | 4-party k=2-of-4 | dyadic | False | — | 0.000 | 0.000 |
| A43 | 4-party k=3-of-4 | dyadic | False | — | 0.000 | 0.000 |
| A44 | 4-party k=4-of-4 | triadic | True | P0P1P2P3S | 4.000 | 4.000 |
| A51 | 5-party k=1-of-5 | triadic | True | P0P1P2P3P4S | 5.000 | 5.000 |
| A53 | 5-party k=3-of-5 | dyadic | False | — | 0.000 | 0.000 |
| A55 | 5-party k=5-of-5 | triadic | True | P0P1P2P3P4S | 5.000 | 5.000 |
| B10 | directed cycle (pure copy ring, no AND) | dyadic | True | ABCD | 2.000 | 2.000 |
| D1 | veto (S = W AND NOT C) | triadic | True | WS | 2.000 | 0.000 |

## Part E — membership law, the integration game, and the coalition exhibit

**Membership law (core-membership battery, committed run).** Necessity: across the enumerated family
of 660 strict-mediation three-party forms, 0/660 elements lacking bidirectional coupling entered the
major complex; the strict family's triadic rate is 9.5% (the manuscript's 'on the order of a tenth').
The graded half comes from the battery's broader unconstrained random three-node family: inclusion in
the core by influence bucket runs 38.9% (≈ four in ten) at influence ≈ 0.25 through 57.9% and 73.7% to
87.5% (≈ nine in ten) at influence ≈ 1.00, rank-AUC 0.629. The two families are distinct and the
manuscript attributes each half to its own family.

**The integration game (worth function stated).** For a configuration modeled as network N at state s,
the worth of coalition S is v(S) = max(0, Φ of the subsystem induced by S in N at s), with the
complement nodes held as frozen background conditions at their values in s, and v(∅) = 0. Shapley
values are computed exactly over all orderings. On the worked strict-mediation triad at state 111:

| party | Shapley value | share of Φ = 2.0 |
|---|---|---|
| E | +0.333 | 17% |
| M | +1.333 | 67% |
| R | +0.333 | 17% |

**The coalition exhibit (section 4).** Four elements (W, S, C1, C2), rules: W′ = S; S′ = W ∧ C1 ∧ C2;
C1′ = S ∨ C2; C2′ = S ∨ C1. Every element is bidirectionally coupled and pivotal on a per-element
screen; the exact maximal complex is {C1, C2} at Φ = 2.0, with W and S outside. Transition table:

| state (W,S,C1,C2) | next | reachable |
|---|---|---|
| 0000 | 0000 | yes |
| 1000 | 0000 | no |
| 0100 | 1011 | no |
| 1100 | 1011 | no |
| 0010 | 0001 | yes |
| 1010 | 0001 | no |
| 0110 | 1011 | no |
| 1110 | 1011 | no |
| 0001 | 0010 | yes |
| 1001 | 0010 | no |
| 0101 | 1011 | no |
| 1101 | 1011 | no |
| 0011 | 0011 | yes |
| 1011 | 0111 | yes |
| 0111 | 1011 | yes |
| 1111 | 1111 | yes |

## Replication

Each part re-derives from a committed script in the replication package; the package's README maps
part to command. All computations are exact; the two-measure comparison in Part A additionally runs
as a continuous-integration check on the package repository.


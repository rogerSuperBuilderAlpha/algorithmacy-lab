# Online supplement — When is a combination a configuration?

*Companion to `ot_configurational_nature_2027_manuscript.md`. Every table below is generated from the
lab's committed sources (question q215 and the irreducibility-catalog study), not transcribed by hand.
Reproduction: the q215 probe re-derives every Φ value in Part A (`python -m
org_frontier.questions.q215_phi_family_robustness.probe_phi_family_robustness`; registered as CI check
`q215-phi-family-robustness`); the catalog study re-derives Part B (`python -m
org_frontier.studies.irreducibility_catalog.build_catalog`).*

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

The four-of-ten verdict-flip figure cited in sections 2 and 7 comes from the lab's encoding-sensitivity
demonstration on ten stylized organizational cases, each modeled twice under defensible alternative
rule encodings; the demonstration and per-case rules are maintained with the field-reading program's
records and will be included in the submission package.


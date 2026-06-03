# The Structure of the Middle: A Graded Score of Coordination Forms and Five Corporate Cases

Roger Hunt III · Bentley University

*Paper 3 of the dissertation. Methods and demonstration. Draft. Every numerical result is reproducible from a committed script in `rebuild/`, named at the point of use. The five organizational cases are provisional: their coordination mechanisms are modeled from public documentation (filings, terms of service, regulatory and platform descriptions), to be replaced and extended with field data. Academic citations are to be re-verified against Crossref before final submission, following Papers 1 and 2.*

---

## Abstract

Paper 2 built a classifier that sorts a coordination form into two kinds. A moderated dyad reduces to the pair. A mediated triad does not. Paper 3 turns that yes/no instrument into a graded score and applies it. The first move is general. The complete family of three-node Worker–System–Counterpart wirings is enumerated, all 4,144 of them, and exact integrated information Φ is computed for each. The scores do not spread continuously. Nearly half the family is reducible, and the rest falls onto seven discrete bands. Real organizations land on populated bands, so their levels are a property of the family rather than a choice. The second move is the contribution. Five large corporations are modeled from how they actually coordinate their parties, and each is placed by structure. The score is computed from structure and takes no input about the mediator's nature, so two forms coded to the same structure receive the same score by construction. A securities exchange and a ride-hailing platform, each coded from its documented mechanism, reduce to the same structure and the same score. A staffing firm and a freelance marketplace do the same. The equality is a property of the modeling, not a discovery that a market and a platform are alike. The contribution is the coding that produces it: a sector- and seat-blind placement of real organizations by the structure of their coordination, where the obvious labels, industry and the mediator's nature, would sort them differently. This is a formal-model result demonstrated on real cases, not a measurement validated against an observed outcome. The unit is the coordination form, not the person, the way a readability score is a property of a text and not of a reader. The paper places organizations on the scale and demonstrates the structural axis on five cases. It then checks that the instrument discriminates, that coordination which genuinely reduces to the pair comes up dyadic, on a five-case dyadic control class, and illustrates the surface-versus-structure point with a catalog of everyday micro-activities. Calibrating the scale against coordination outcomes, and building the matched person-level instrument, are the program it opens.

*Keywords:* coordination form; mediated triad; integrated information; Φ; typology; intermediation; algorithmic management; structural irreducibility; case study

---

## 1. From a yes/no classifier to a graded structural score

Paper 2 sorted coordination forms into two kinds. Paper 3 asks how much, and which real organizations sit where. The answer is a graded score and a demonstration on five large corporations. Paper 2 gave a binary verdict: a coordination form is a mediated triad when its cause-effect power is irreducible, and a moderated dyad when it factors. Paper 3 reads the same measure as a graded score, places a typology of organizations on it, and shows the score doing analytic work on documented cases.

The unit is the coordination form, not the person. A readability score is a property of a text. It says nothing about a given reader, who may find an easy text hard or a hard text easy. The score here is the same kind of object. It is a property of how an organization coordinates its parties, and it carries no claim about any individual who works inside that form. The matched person-level instrument, and the validation of the score against what happens to people, are later work. This paper places organizations, not people.

The headline is a property of the model, stated carefully. The score is computed from the structure of how parties reach each other, and it takes no input about the mediator's nature. So two forms coded to the same structure receive the same score, by construction. A securities exchange and a ride-hailing platform, each coded from its documented mechanism, reduce to the same structure and the same score. A staffing firm and a freelance marketplace do the same. The equality is not a discovery that a market and a platform are alike. It is a demonstration that the coding is blind to industry and to the mediator's seat, so a market and a gig platform sort together by structure where the obvious labels would split them.

This fills a narrow gap. Much algorithmic-management research studies the algorithm as an actor that controls workers, and reads the structure of coordination through the technology's particular affordances, its opacity, its reach, its speed (Kellogg, Valentine, & Christin, 2020; Rahman, 2021). Some of it theorizes the platform as a distinct structural form in its own right (Vallas & Schor, 2020). What none of it does is score a three-party coordination form by structural irreducibility on a scale where a human institution and an algorithmic platform of the same structure receive the same score. That is the narrow gap this paper fills, and the paper claims no more than it.

What follows is a demonstration, not a validation. The cases instantiate the model and test whether it behaves as predicted across real, varied forms. They do not connect a Φ value to an observed coordination outcome. Section 3 enumerates the model family and places the typology. Section 4 states the case-study method. Section 5 works the five cases. Section 6 reads them across. Section 7 runs a dyadic negative-control check and illustrates the surface-versus-structure point with a catalog of everyday micro-coordination. Sections 8 through 10 give the discussion, the limits, and what the paper opens.

## 2. The unit is the coordination form, not the person

The readability analogy fixes the unit and bounds the claim. A readability score grades the text. The instrument here grades the coordination form. What the analogy lends is the unit, a property of the form rather than the participant. What it does not lend is a validated link to an outcome. Readability scores were tuned against measured reading performance over decades. This score has no such tuning yet, and the paper does not pretend otherwise.

Coordination theory already locates the unit in the structure, not the actor. Malone and Crowston define coordination as managing dependencies between activities, and they characterize a form by the kind of dependency and the mechanism that manages it, not by who occupies the coordinating role (Malone & Crowston, 1994). Crowston's taxonomy makes the move explicit. It breaks with the older habit of locating dependencies between actors and locates them between activities, so the same dependency can be managed by different mechanisms and reassigned across actors (Crowston, 1997). Coordination, on this account, can occur in human, computational, and biological systems, and the point is to carry the analysis across them.

Brokerage theory reaches the same place from the other side. Burt argues that competitive advantage is a matter of relations, not the attributes of the player, and that causation resides in the intersection of relations. The unit is a position in a social structure, and its occupant may be a person, an organization, or a larger aggregation, interchangeably (Burt, 1992). Halevy and colleagues sharpen the distinction the paper needs. Brokerage is a structural position, the occupation of a bridge between otherwise disconnected parties. Brokering is the behavior of the occupant. Different triadic configurations enable different forms of influence (Halevy, Halali, & Zlatev, 2019). The structure-not-seat claim is theirs before it is the model's. The model makes it computable.

The graded part of the score also has a precedent. Thompson ranked interdependence as pooled, sequential, and reciprocal (Thompson, 1967). Van de Ven, Delbecq, and Koenig added a fourth, more tightly coupled level, the team or intensive mode, and treated the coordination mode as the classified object (Van de Ven, Delbecq, & Koenig, 1976). A graded ladder of coordination structure is old. This paper computes one rather than assigning it, and runs it over a complete family rather than a few types.

## 3. The model and the family

The instrument is Paper 2's, and it is recalled in one paragraph. A coordination form is modeled as a small Boolean system over three nodes, the worker W, the system or mediator S, and the counterpart C. Each node updates as a function of the current state of all three. Exact IIT-4.0 system Φ over the minimum-information partition reads whether the form's cause-effect power factors. The state alphabet is fixed by Paper 2's pre-registered individuation rule, one node per party with a binary application-layer status. The binary verdict, Φ equal to zero against Φ greater than zero, is the reliable claim. Magnitude is read only ordinally. Paper 2 builds and defends the instrument; Paper 3 uses it.

The general application enumerates the whole triad family. A three-node wiring is any way each node's next value can depend on the other two. There are sixteen Boolean functions of two inputs, so the complete triad family is sixteen cubed, 4,096 wirings, and every one is scored. No two of them produce the same transition matrix, so all 4,096 are distinct. A further 48 four-node forms are added, where the mediator binds three parties, for 4,144 in all. These 48 are a structured sample of higher-order mediation, not a complete four-node family, which would be vastly larger. Most of the 4,096 triads are not recognizable coordination forms. The enumeration is a coverage check, not a census of coordination. Its purpose is to characterize what the model does across its whole domain, and to show that the organizations placed below sit on populated bands rather than on points the author picked. This is `catalog.py`.

The scores do not spread continuously. Across all 4,096 triad wirings, 44.1 percent are reducible, with Φ exactly zero. The rest fall onto seven discrete non-zero bands.

| Φ band | wirings | reading |
|---|---|---|
| 0.00 | 1,808 (44.1%) | reducible — the wiring factors along party lines |
| 0.42 | 856 | the most common non-zero level |
| 0.50 | 24 | parity-coupled determination |
| 0.83 | 824 | where the partial-mediation cases land |
| 1.00 | 72 | |
| 1.50 | 8 | |
| 2.00 | 496 | where the strict-AND cases land (16 of the 496) |
| 6.00 | 8 | a small exotic tail |

The bands are a property of the family, not assigned. Nearly half of all ways to couple three nodes do not produce an irreducible structure at all. The levels the organizations occupy below, 0, 0.50, 0.83, and 2.00, are populated bands of this family. This is `analyze_catalog.py`.

What drives the score is structure, and not much else. An ordinary-least-squares fit of max Φ on structural features, over all 4,096 triads, makes strict mediation the strongest single driver, with a partial coefficient of +0.54 and a group mean of 0.90 against 0.53. Parity adds +0.27 and edge density +0.24. The model reaches an R² of 0.196. Simple structural flags explain only about a fifth of the variance in Φ. Strict mediation and parity raise the score, but Φ registers an irreducibility that a count of edges or parties does not reproduce. That residual is the reason the construct uses Φ and not a checklist.

The strict-mediation forms make the point sharper. There are forty canonical strict-mediation wirings: the worker reads only the mediator, the counterpart reads only the mediator, and the mediator reads both. They do not share a score. Sixteen reach 2.00, eight sit at 0.50, and sixteen reduce to zero. The mediator's Boolean function decides which: an AND-family determination reaches 2.00, a parity determination sits at 0.50, and others factor. So strict mediation is not a band. It is a topology whose score depends on the determination it carries. A structural checklist that flags strict mediation would mis-score twenty-four of the forty. Φ does not, and that is what the measure buys over the checklist. This is `review_response.py`.

One result runs the other way. Among genuine two-party mediators, parity determinations, the XOR and XNOR couplings, score the highest Φ, with a mean of 0.85 against 0.535 for the monotone functions. This is the model-internal echo of Cerullo's caution that trivially regular parity structures can carry high Φ, so a high Φ does not certify sophisticated coordination (Cerullo, 2015). Magnitude is therefore read ordinally and within the model, and the binary Φ equal to zero against Φ greater than zero carries the dyad-triad question.

The typology is placed on the populated bands. Each of a set of organization types is modeled as a Boolean system, its determination structure fixed before computing from how it coordinates its parties, and scored. Dyadic baselines, direct exchange and a two-party chat, sit at 0. A complementary-skill match, a parity determination, sits at 0.50. Partial-mediation forms, where the parties keep a direct channel, sit at 0.83. Strict-mediation forms, where the parties reach each other only through a joint determination, sit at 2.00. Higher-order forms, where one determination binds more than three parties, sit at 3.00. This is `typology.py`. A graded typology of this kind is a theoretical object, not a filing scheme, when its categories are derived and its placements are falsifiable (Doty & Glick, 1994). Both hold here: the bands fall out of the family, and any placement can be checked by re-modeling the form.

## 4. Method for the case studies

The cases apply an existing instrument to real organizations, which fixes the register. This is theory-driven case work, where the research question is tied to prior theory and the cases instantiate and test it (Ridder, 2017). It is not theory-building from cases, whose aim is to generate theory the data did not start with (Eisenhardt, 1989). The model is the prior theory. The cases show it doing work. The claim is calibrated accordingly. Case-based testing is weaker than experimental testing, so the five cases are a demonstration with a replication test inside it, not a definitive validation (Ridder, 2017).

The cases are selected by theory, not by sampling. The design varies one structural dimension, the determination structure, across its range, and holds another fixed, the party count. This is the diverse-case logic, whose aim is maximum variance along the dimension of interest (Seawright & Gerring, 2008), combined with controlling extraneous variance by holding the nuisance variable fixed (Burnham, Lutz, Grant, & Layton-Henry, 2008). Holding party count fixed while varying structure is the method's central move. Diverse-case selection is still an author's choice, disciplined along a declared axis: which organizations fill the cells is the author's, and Section 6 says so and rests the discipline on the coding rule. It is also a lesson carried forward: an earlier attempt to anchor the scale on rideshare pooling failed because pooling varied party count, and Φ rose with party count, which validated only the axis the model does not need. The cases vary structure at a fixed count instead.

Four cases form the replication design; the fifth extends it to a higher-order determination.

| Case | Industry | Structure | Predicted Φ | Seat | Replication role |
|---|---|---|---|---|---|
| Uber | transportation | strict mediation | 2.00 | algorithmic | literal (with the exchange) and seat-contrast |
| NYSE / Nasdaq | financial markets | strict mediation | 2.00 | market institution | literal (with Uber) and seat-contrast |
| Upwork | professional services | partial mediation | 0.83 | algorithmic | literal (with ManpowerGroup) and seat-contrast |
| ManpowerGroup | staffing | partial mediation | 0.83 | human-institutional | literal (with Upwork) and seat-contrast |
| Amazon Mechanical Turk | crowdwork | higher-order strict | 3.00 | algorithmic | theoretical (structure binds >3 parties) |

The two equal-Φ pairs do the work, and what they do has to be stated precisely. Within a pair the two organizations are coded to the same structure, so they compute the same Φ. That is identity by construction, not a replication, and the paper does not lean on it as one. The content is across the pair. The mediator is an algorithm in one member and a human institution or a market in the other, and the coding, read from each organization's documented mechanism, lands both on the same structure. That is the seat-blind result: a demonstration that the coding sorts disparate real organizations together by structure, not a discovery that the organizations are alike. The fifth case extends the structure to a determination binding more than three parties, where the raw score grows with party count and a size-normalized reading restores comparability.

The modeling procedure is fixed and disclosed. Each organization is modeled under Paper 2's individuation rule. The determination structure for each is pre-registered before computing, in `cases.py`, read from the documented mechanism rather than chosen for a target score. One rule fixes the unit across cases and is applied visibly in each: model the layer at which the focal dyad's coordination is committed. For a securities exchange that is the order match between a buyer and a seller, not the downstream clearing that nets many members; for crowdwork it is the task allocation between a requester and the workers on a task. The rule, not the analyst's preference, decides which layer each case models, and where an organization carries different structure at different layers the case says so. The computation reports Φ, the band, and the minimum-information partition. Rigor here is the inferential chain, not a template. The chain runs from the organization, to the documented evidence of how it coordinates, to the classifier's inputs, to the Φ score, to the coordination-form claim, and each link is shown rather than asserted (Harley & Cornelissen, 2022). Each case discloses why it was studied, in what context, what is modeled, and how, following the transparency questions ORM expects (Pratt, 2009).

The cases are provisional, and the status is stated plainly. The evidence for each is public documentation, company filings, terms of service, regulatory and market-structure descriptions, and platform documentation. There is no established convention for cases written before fieldwork, so this is an honest disclosure rather than a recognized category. The author will replace and extend the public-documentation evidence with field data. Each case marks the status of its inputs.

## 5. The five cases

Each case states the bounded unit and its context, the evidence and its status, how the organization coordinates its parties, the analytic operation, and the rival codings that would move the verdict.

### 5.1 Uber — strict mediation — Φ 2.00

The unit is the coordination between a rider and a driver around a single trip, at the application layer. The evidence is public and provisional: Uber's annual report, its Platform Access Agreement, its marketplace description, and a granted matching patent.

Uber commits the dispatch. The platform evaluates nearby drivers and riders together and pairs them, and it states that the closest driver is not always the chosen one, because travel time and geography enter the match (Uber, 2024). The patent describes a matching engine that computes an optimization score for each proximate driver from rider information, driver information, location, and estimated time of arrival, then selects one (Uber Technologies, 2017). The determination is a joint function of both parties' states. The rider and the driver reach each other only through it. The Platform Access Agreement restricts the back-channel: a driver may not contact a rider or use the rider's information except for the assigned ride, absent consent (Uber Technologies, 2022).

The analytic operation models the rider, the platform, and the driver as W, S, and C. The worker reads the system, the system commits a joint function of both parties, and the counterpart reads the system: `W' = S`, `S' = W ∧ C`, `C' = S`. Φ is 2.00 at the all-on state, with the minimum-information partition keeping the system and counterpart together against the worker. The form is strict mediation. This is `cases.py`.

A rival coding would change the verdict in a predictable way. If the back-channel were open, if a driver and rider routinely arranged rides off the app, the form would move toward partial mediation, because the parties would reach each other without the dispatch. The contractual restriction on off-app contact is what keeps the modeled form strict. A separate caveat is that Uber's accounting treats the company as an agent for core ride-hailing but as a principal for some other lines, so "merely arranges" is bounded to the ride-hailing case modeled here.

### 5.2 NYSE / Nasdaq (a securities exchange) — strict mediation — Φ 2.00

The unit is the coordination between a buyer and a seller in a single security's order matching. The evidence is public and provisional: the Nasdaq systems description filed with the regulator, the exchange's market-model and auction descriptions, and the clearing corporation's account of central settlement.

The exchange commits the match. Nasdaq matches orders electronically on price-time priority, with no single specialist through which transactions pass (Nasdaq, 2014). The opening and closing crosses aggregate all submitted interest and select the single price that executes the most shares. The buyer and the seller never transact directly. The clearing corporation then interposes itself by novation, becoming the counterparty to each side, so the parties face the clearinghouse rather than each other (Depository Trust & Clearing Corporation, 2024). The determination is a joint function of all resting interest.

The analytic operation models the buyer, the exchange, and the seller as W, S, and C, at the order-matching layer that the unit rule selects: `W' = S`, `S' = W ∧ C`, `C' = S`. These are the same Boolean rules the Uber case uses, so the two compute the same Φ, 2.00. The identical score is not evidence that an exchange and a ride-hailing platform are alike. It is the consequence of coding both, from their documented mechanisms, as strict mediation. What the case shows is that the coding reaches the same structure for a market institution and a gig platform, which industry and the mediator's nature would have sorted apart.

Two rival codings show how much the band turns on the reading, and the case must meet them. The first is adversarial. Code the exchange as a market maker that posts its own quotes, so each party transacts against the system rather than through a joint determination of both, `S' = S`, and Φ falls to 0.00, a reducible dyad with a spectator (`review_response.py`). The drafted strict coding is defended against it on the mechanism: an order-driven exchange matches a buyer's and a seller's resting interest, and neither reaches the trade without the other, which is a joint determination, not a posted quote. The reading is contestable and is defended on the documented matching rule, not assumed. The second rival is the layer. Central net settlement collapses many members' obligations into one position each against the clearinghouse, so at the clearing layer a single determination binds more than two parties, a higher-order structure. The unit rule sends this case to the matching layer, where the focal buyer-seller coordination is committed; the clearing layer is named, not modeled. A last caveat: the precise mechanics by which the engine assigns a contra party are contested in the sources, though the absence of direct contact between buyer and seller is not.

### 5.3 Upwork — partial mediation — Φ 0.83

The unit is the coordination between a client and a freelancer around a contract. The evidence is public and provisional: Upwork's terms on circumvention and its conversion fee, its annual report, and its user agreement.

Upwork matches and hosts, and the parties coordinate directly. The platform pairs clients and freelancers and holds the contract and payment, but the client and the freelancer work together directly inside the platform. The platform polices only the off-platform boundary. Its anti-circumvention rule forbids a client and freelancer who met through Upwork from taking the relationship off the platform, because the marketplace depends on the fee collected when clients pay freelancers on it, and a conversion fee lets the relationship move off-platform lawfully once paid (Upwork, 2024). The direct channel is open on the platform and closed off it.

The analytic operation models the freelancer, the platform, and the client as W, S, and C. The platform commits a joint match, and each party reads the platform and the other party: `W' = S ∨ C`, `S' = W ∧ C`, `C' = S ∨ W`. Max Φ over reachable states is 0.83, at the two states where one party is live; the form reduces to zero at the all-on state, so the band is the reachable maximum, read as Paper 2 reads it. The form is partial mediation, because the parties keep a direct channel and the structure does not reduce to pure mediation.

Two rival codings bound the result. The first is the match aggregation. Coding the match as a conjunction, `S' = W ∧ C`, gives 0.83; coding it as a disjunction, `S' = W ∨ C`, gives 6.00, off the populated scale entirely (`review_response.py`). The conjunction is defended on the mechanism: a match is committed only when a willing client and a willing freelancer are both present, which is a joint condition on both, not an either-or. The choice is contestable and is defended on the documented matching rule, not assumed. The second rival follows the channel. The anti-circumvention rule is the documented version of a pattern Paper 2 named, a platform with a reason to suppress the direct channel so the coordination cannot collapse to the pair. Here the platform suppresses only the off-platform channel and leaves the on-platform one open, which is why the form is partial and not strict. Forbid all direct contact and the model moves toward strict mediation. The permanent-closure penalty is "can result in" rather than automatic, given the conversion-fee exception.

### 5.4 ManpowerGroup — partial mediation — Φ 0.83

The unit is the coordination between a placed worker and a client firm on an assignment. The evidence is public and provisional: ManpowerGroup's worker-facing description of how placement works, its annual report, and jurisdictional staffing terms.

ManpowerGroup places and then steps back from the day-to-day. The agency screens, assesses, and commits the placement, and for temporary roles it is the legal employer of record: the worker is employed through Manpower and placed at the client's worksite. The client directs the day-to-day work. Manpower's own guidance tells the placed worker that the on-site supervisor is the resource for daily questions while Manpower remains the employer (ManpowerGroup, 2024). The agency commits the match and stays the employer, but it does not stand between the parties' working relationship.

The analytic operation models the worker, the agency, and the client as W, S, and C, with the same partial-mediation rules as Upwork: `W' = S ∨ C`, `S' = W ∧ C`, `C' = S ∨ W`. They are the same Boolean system, so the max Φ over reachable states is again 0.83. The identical score follows from the identical coding: a staffing institution and a freelance marketplace, read from their mechanisms, both commit the match and leave the parties a direct working channel, so both code to partial mediation. A human-run institution and an algorithmic marketplace reach the same structure, which is the seat-blind result again, on a human seat this time.

A rival coding turns on the contract. Temp-to-perm conversion terms and any non-circumvention clause, not stated on the public worker-facing page, could tighten or loosen the direct channel and move the score. This is flagged for the field data that will replace the provisional evidence.

### 5.5 Amazon Mechanical Turk — higher-order strict mediation — Φ 3.00

The unit is the coordination between a requester and the worker or workers on a task. The evidence is public and provisional: Amazon's requester and worker documentation for the platform.

Mechanical Turk binds requester and workers only through the platform, and one task can bind several. A requester posts a task, a HIT, to the marketplace. Workers find it, self-select, accept, and submit. The requester sets qualifications that gate who may work and approves or rejects the result. The platform sits in the payment path, transferring the reward from the requester's account to the worker's on approval (Amazon Web Services, 2024). There is no direct requester-worker channel. A single HIT can be assigned to many workers at once, so one determination binds the requester and multiple workers, with the platform as payment intermediary.

The analytic operation models the requester, the platform, and two workers as a four-node system. The system commits a joint determination over all parties: `S' = W ∧ C ∧ D`, with each party reading the system. The raw Φ is 3.00.

The raw number is a size artifact, and the case reports it as one. For strict-AND mediation, Φ equals the party count minus one exactly: 2.00 at three nodes, 3.00 at four, 4.00 at five (`review_response.py`). So the 3.00 is not a higher structural band than the 2.00 of Uber and the exchange. It is the same kind of structure, strict mediation, scaled by the number of parties the determination binds. The size-normalized score Φ/(n−1) makes this explicit: it is 1.00 here, the same value strict mediation takes at every party count, and the same value the Uber and exchange cases take at three nodes. Read normalized, the case is a scope extension: it places a determination binding more than three parties on the scale, and the equal normalized score follows from the n−1 identity, not from a new finding. A single-assignment HIT, one requester and one worker through the platform, is an ordinary strict triad at 2.00. The raw magnitude grows with party count; the structural reading does not, and the paper reads the normalized value, not the raw 3.00, as the comparable one.

## 6. Reading the cases across

The cases sort by structure when laid in a row. Ordered along the determination dimension, the matrix reads cleanly: the partial-mediation pair keeps a direct channel and scores 0.83; the strict-mediation pair closes the channel and scores 2.00; the higher-order case binds extra parties and scores a raw 3.00 that normalizes to the same strict level. The rows that decide the score are whether the parties reach each other only through the system, and whether a direct channel exists. The seat of the mediator is not one of those rows.

| dimension | Upwork | ManpowerGroup | Uber | NYSE/Nasdaq | MTurk |
|---|---|---|---|---|---|
| only through S? | no | no | yes | yes | yes |
| direct channel? | yes | yes | no | no | no |
| determination | joint match | joint placement | joint dispatch | joint order match | joint, >2 parties |
| seat | algorithmic | human-institutional | algorithmic | market institution | algorithmic |
| Φ (max over reachable) | 0.83 | 0.83 | 2.00 | 2.00 | 3.00 |
| Φ/(n−1) (size-normalized) | 0.42 | 0.42 | 1.00 | 1.00 | 1.00 |

The two equal-Φ pairs carry the result, and the result is about the coding. Upwork and ManpowerGroup match the parties and leave them a channel, and both code to 0.83 though one mediates by software and the other by a staffing institution. Uber and a securities exchange interpose a joint determination with no direct channel, and both code to 2.00 though one is a gig platform and the other a market. The equality is a modeling property, not an empirical discovery: two organizations coded to the same structure compute the same Φ, necessarily. What is not necessary, and is the demonstration, is that the coding reaches the same structure for organizations this disparate when it is read from each one's documented mechanism. The model is indifferent to the seat once the structure is fixed, and the pairs show the coding reaching the same structure across a market institution and a gig platform, a staffing firm and a software marketplace.

The not-cherry-picked claim has to be stated narrowly, because there are two choices to defend, not one. The organizations land on bands the enumeration populated on its own: 824 wirings at 0.83, 496 at 2.00. That answers one worry, that the author chose freak points of the family. It does not answer the other, that the author chose which organizations to study and how to code each, and those remain author choices. Most wirings on a band are not coordination forms anyway, so a band's population says little about whether an organization belongs there. The discipline against cherry-picking is therefore not the populated band. It is the coding rule, read from documented mechanism before the score is seen, and the per-case sensitivity that shows what a different reading would yield.

What the cases add beyond the typology is a demonstration about the coding procedure, not a discovery about the world. The typology of Section 3 already placed archetypes on the bands; the cases show that the same coding, applied to real, documented, incommensurable organizations, reduces them to the same few structural bits and sorts them against the grain of industry and seat. A securities exchange, a staffing firm, and a crowdwork platform do not group by sector, and they do not group by whether a human or an algorithm sits in the middle. They group by how the parties reach each other. That the coding is sector-blind and seat-blind on real cases is the contribution; it is a claim about the procedure, and it is the most the cases establish.

## 7. A dyadic control class and a catalog of the everyday

A classifier that only ever returns "triad" is worthless. A negative-control class tests whether the instrument returns zero when the coordination genuinely reduces to the pair, and a catalog of everyday activities illustrates that the verdict turns on mechanism, not surface.

The first is a negative-control class. Five real coordination forms an analyst would judge dyadic were coded from their mechanisms and scored, with the prediction fixed in advance at Φ equal to zero (`dyadic_cases.py`). Three came up dyadic. A telephone call, where the carrier connects the parties and they then talk on an open line, factors. Email, where the provider forwards a message the sender addressed, factors. A worker at a software tool, with no third party coordinated, factors. Two did not. Both are findings, not failures. A payment processor settling a deal the two parties struck directly scores 0.83, because the processor still authorizes as a joint function of both, so the coordination does not reduce to a clean pair. A classified-listing board scores 1.00 under a coding where the board carries the listing and the responder contacts the poster; a cleaner route-around coding, where buyer and seller read each other directly, factors to zero, so the paper flags the listing result as a contestable coding rather than a verdict. The control did its job. It falsified the predicted zero in two of five forms, which is what a control is for. The instrument does not track a casual dyad intuition; it tracks the coded mechanism, and fixing the prediction in advance is what exposes the gap. It returns zero on three forms that genuinely reduce to the pair, and it withholds the dyadic label from two a casual reading would grant.

The catalog is an illustration, not a second measurement. One hundred and three micro-coordination activities, all distinct on the surface, were coded from their mechanisms and scored (`micro_scenarios.py`; the full catalog is `MICRO_SCENARIOS.md`): texting a friend, ordering lunch, opening a pull request for review, booking a venue, matching a kidney donor, funding a project on Kickstarter, and ninety-seven more. The point is qualitative. A hundred surface-distinct activities land on the same few structural levels the family produces, the dyadic, parity, partial, and strict bands, with the higher-order forms folding onto the strict level once size is normalized. How many fall in each band is a property of which activities the catalog happens to list and how each is coded, not a frequency in the world, so no count is read as a base rate. What the catalog shows is that the score reads mechanism, not surface. Buying lunch at a counter is a two-party exchange and scores zero; ordering the same lunch through a delivery app, where a dispatch commits a joint match and the parties reach each other only through it, scores strict. The surface is the same and the structure is not.

The control and the catalog are both claims about the coding, not discoveries about the world, on the same terms as the cases. Each scenario's Φ follows from a structural coding fixed before the score is seen, and the assignments among conduit, partial, and strict are contestable as a class, not only at named edges. A peer payment is coded partial because the processor authorizes jointly, and could be read as a conduit. A pull request is coded partial because the parties discuss directly while a merge gate binds, and could be read higher-order where the gate is multi-party. Ordering through a waiter is coded a conduit, and a reader who treats the kitchen as a joint determiner would code it otherwise. A reasonable analyst could re-code many of the hundred and move their bands, and the rationale recorded for each scenario is the auditable coding decision. The catalog earns nothing the codings do not. What it illustrates is that surface and structure come apart, and that the discipline that sorts the five cases sorts the everyday ones the same way.

## 8. Discussion

Structure sets the score, and the result has a lineage. Coordination theory holds that the form lives in the dependency, not the actor, and that the analysis carries across human and computational systems (Malone & Crowston, 1994). Brokerage theory holds that the advantage lives in the position, and that a person and an organization are interchangeable occupants of it (Burt, 1992). Two-sided-market theory defines the intermediary by its coordinating function rather than its substance (Rochet & Tirole, 2006). Each of these says, qualitatively, that the structure matters and the occupant's nature is secondary. The model turns that into a computed score and shows it on real corporations.

The score measures one thing, and the limit has to be stated, not waved past. A reader will object that a human institution and an algorithmic platform are not the same, because opacity, power, and accountability differ with the mediator's nature, and those differences are real and consequential (Rahman, 2021). The objection is correct. Φ measures the structural irreducibility of the mediation, and that is necessary for an organizational characterization, not sufficient. The equal score does not say the two forms are substitutable, equivalent in power, or the same to the people inside them. A court and a dispatch algorithm coded to the same structure pose the same coordination problem in the narrow sense the model defines, and they remain profoundly different in due process, appeal, recourse, and the visibility of the rule, none of which the score sees. For opacity there is a clean separation the model inherits: Paper 2 showed that how opaque a mediator is and whether the coordination factors are independent properties. Power and accountability are not so cleanly separable, and the paper does not claim to have bracketed them without residue. It claims only that the structural score is one layer, that a power-aware layer is needed, and that the second is not delivered here. The equal score is a starting point for that analysis, not a substitute for it.

What the score buys an analyst is a placement that is blind to sector and blind to seat. Handed an organization, the analyst can model how it coordinates its parties and place it on a graded scale, rather than sort it by its industry or by whether its mediator is software. The placement is a discipline against two easy errors: reading triadicity off the industry label, and reading it off the mediator's technology. The cases show the coding avoiding both errors: a market coded like a platform, a staffing firm like a marketplace, by structure rather than by label or seat.

The typology earns its standing as theory rather than classification. Its categories are derived from the family rather than stipulated, and every placement is falsifiable by re-modeling the form (Doty & Glick, 1994). A classification sorts into bins someone chose. This typology reports bands the enumeration produced and places organizations on them by a stated procedure.

## 9. Limitations

The paper demonstrates, it does not validate against the world. No Φ value here is connected to an observed coordination outcome, a worker's earnings, a task's success, a dyad's stability. The cases instantiate and replicate the model; they do not test it the way an experiment would (Ridder, 2017). The cases are provisional. Their evidence is public documentation, to be replaced and extended with field data, and each case marks the status of its inputs. Magnitude is ordinal only, and the parity result inside the family is the standing reason (Cerullo, 2015). The higher-order score at four nodes is a size artifact, not a higher band: for strict mediation Φ equals the party count minus one, so the raw 3.00 is the three-node 2.00 scaled by one more party, and the size-normalized score, which puts strict mediation at 1.00 for every party count, is the comparable one. The seat-blind equivalence is structural and narrow: it does not claim two equal-score forms are substitutable or equal in power, and the paper does not claim to have cleanly bracketed power and accountability, only opacity (Section 8). The choices that set each case's band are the author's, disciplined but not removed: which organizations to study, and how to code each from its documented mechanism. Both are declared, and each case reports a sensitivity that shows what a different reading would yield, so the choices are auditable rather than hidden. A different faithful coding can place a form differently, and the modeling choices Paper 2 named, the state alphabet and the reads, are carried here on the same terms.

## 10. Conclusion

Paper 2 sorted coordination forms into two kinds. Paper 3 graded the sort and applied it. The complete family of three-node forms falls onto a handful of discrete bands, and real organizations land on populated ones. Five large corporations, coded from how they actually coordinate, place by structure: a securities exchange and a ride-hailing platform reduce to the same structure and the same score, a staffing firm and a freelance marketplace do the same, and a crowdwork platform shows the same kind of structure scaled to more parties. The score is computed from structure and takes no input about the mediator's nature, so it is seat-blind by construction. The contribution is that the coding, read from documented mechanisms, sorts disparate real organizations together by structure where industry and the mediator's nature would split them. This is a formal-model result demonstrated on real cases, and it is the most the cases establish. What remains is the empirical program it opens: calibrating the scale against coordination outcomes, on data that varies structure at a fixed party count, and building the matched person-level instrument that the readability analogy promises and this paper does not yet deliver.

---

## Data and code availability

Every numerical result is reproducible from a script in `rebuild/`, run with the project's PyPhi 4.0 environment. `phi_core.py` is the measure, re-derived from scratch and depending only on PyPhi; it reproduces Paper 2's controls exactly at three nodes. `catalog.py` and `analyze_catalog.py` enumerate and analyze the 4,144-form family. `typology.py` places the organization typology. `cases.py` computes the five case models. `dyadic_cases.py` runs the dyadic negative-control class. `micro_scenarios.py` scores the 103-activity micro-catalog and writes `MICRO_SCENARIOS.md`. `review_response.py` computes the figures answering the adversarial review.

## References

*To be re-verified against Crossref before submission, following Papers 1 and 2. Sources shared with Papers 1 and 2 carry the same verified details. Case-evidence sources (company filings, terms of service, regulatory and platform documentation) are listed separately from the academic bibliography.*

Burt, R. S. (1992). *Structural holes: The social structure of competition.* Harvard University Press.

Burnham, P., Lutz, K. G., Grant, W., & Layton-Henry, Z. (2008). *Research methods in politics* (2nd ed.). Palgrave Macmillan.

Cerullo, M. A. (2015). The problem with phi: A critique of integrated information theory. *PLOS Computational Biology, 11*(9), e1004286.

Crowston, K. (1997). A coordination theory approach to organizational process design. *Organization Science, 8*(2), 157–175.

Depository Trust & Clearing Corporation. (2024). *Continuous Net Settlement (CNS); National Securities Clearing Corporation.* [Case evidence — provisional.]

Doty, D. H., & Glick, W. H. (1994). Typologies as a unique form of theory building. *Academy of Management Review, 19*(2), 230–251.

Eisenhardt, K. M. (1989). Building theories from case study research. *Academy of Management Review, 14*(4), 532–550.

Halevy, N., Halali, E., & Zlatev, J. J. (2019). Brokerage and brokering: An integrative review and organizing framework. *Academy of Management Annals, 13*(1), 215–239.

Harley, B., & Cornelissen, J. (2022). Rigor with or without templates? The pursuit of methodological rigor in qualitative research. *Organizational Research Methods, 25*(2), 239–261.

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. *Academy of Management Annals, 14*(1), 366–410.

Malone, T. W., & Crowston, K. (1994). The interdisciplinary study of coordination. *ACM Computing Surveys, 26*(1), 87–119.

Pratt, M. G. (2009). For the lack of a boilerplate: Tips on writing up (and reviewing) qualitative research. *Academy of Management Journal, 52*(5), 856–862.

Rahman, H. A. (2021). The invisible cage: Workers' reactivity to opaque algorithmic evaluations. *Administrative Science Quarterly, 66*(4), 945–988.

Ridder, H.-G. (2017). The theory contribution of case study research designs. *Business Research, 10*(2), 281–305.

Rochet, J.-C., & Tirole, J. (2006). Two-sided markets: A progress report. *RAND Journal of Economics, 37*(3), 645–667.

Seawright, J., & Gerring, J. (2008). Case selection techniques in case study research: A menu of qualitative and quantitative options. *Political Research Quarterly, 61*(2), 294–308.

Thompson, J. D. (1967). *Organizations in action.* McGraw-Hill.

Van de Ven, A. H., Delbecq, A. L., & Koenig, R. (1976). Determinants of coordination modes within organizations. *American Sociological Review, 41*(2), 322–338.

Vallas, S., & Schor, J. B. (2020). What do platforms do? Understanding the gig economy. *Annual Review of Sociology, 46*, 273–294.

### Case-evidence sources (provisional; public documentation)

Amazon Web Services. (2024). *Amazon Mechanical Turk: Requester and Worker documentation.*

ManpowerGroup. (2024). *Working for Manpower;* Form 10-K.

Nasdaq. (2014). *Nasdaq Market Center systems description* (SEC filing).

NYSE. (2024). *Market model; opening and closing auctions fact sheet.*

Uber Technologies. (2017). *Optimal pairing of ride requests with drivers,* U.S. Patent Application US20170011324A1.

Uber Technologies. (2022). *Platform Access Agreement* (United States).

Uber Technologies. (2024). Form 10-K; *Uber marketplace: matching.*

Upwork. (2024). *Circumvention; Conversion Fee; User Agreement;* Form 10-K.

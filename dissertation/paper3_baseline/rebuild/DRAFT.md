# Scoring Coordination by Structure: A Graded Typology of Triadic Demand and Five Corporate Cases

Roger Hunt III · Bentley University

*Paper 3 of the dissertation. Methods and demonstration. Draft. Every numerical result is reproducible from a committed script in `rebuild/`, named at the point of use. The five organizational cases are provisional: their coordination mechanisms are modeled from public documentation (filings, terms of service, regulatory and platform descriptions), to be replaced and extended with field data. Academic citations are to be re-verified against Crossref before final submission, following Papers 1 and 2.*

---

## Abstract

Paper 2 built a classifier that sorts a coordination form into two kinds. A moderated dyad reduces to the pair. A mediated triad does not. Paper 3 turns that yes/no instrument into a graded score and applies it. The first move is general. The complete family of three-node Worker–System–Counterpart wirings is enumerated, all 4,144 of them, and exact integrated information Φ is computed for each. The scores do not spread continuously. Nearly half the family is reducible, and the rest falls onto seven discrete bands. Real organizations land on populated bands, so their levels are a property of the family rather than a choice. The second move is the contribution. Five large corporations are modeled from how they actually coordinate their parties, and each is placed by structure. A securities exchange scores the same as a ride-hailing platform. A staffing firm scores the same as a freelance marketplace. The score tracks the structure of how parties reach each other, not the seat of the mediator. A human institution and an algorithmic platform of the same structure receive the same score. This is a formal-model result demonstrated on real cases, not a measurement validated against an observed outcome. The unit is the coordination form, not the person, the way a readability score is a property of a text and not of a reader. The paper places organizations on the scale and demonstrates the structural axis on five cases. Calibrating the scale against coordination outcomes, and building the matched person-level instrument, are the program it opens.

*Keywords:* coordination form; mediated triad; integrated information; Φ; typology; intermediation; algorithmic management; structural irreducibility; case study

---

## 1. From a yes/no classifier to a graded structural score

Paper 2 sorted coordination forms into two kinds. Paper 3 asks how much, and which real organizations sit where. The answer is a graded score and a demonstration on five large corporations. Paper 2 gave a binary verdict: a coordination form is a mediated triad when its cause-effect power is irreducible, and a moderated dyad when it factors. Paper 3 reads the same measure as a graded score, places a typology of organizations on it, and shows the score doing analytic work on documented cases.

The unit is the coordination form, not the person. A readability score is a property of a text. It says nothing about a given reader, who may find an easy text hard or a hard text easy. The score here is the same kind of object. It is a property of how an organization coordinates its parties, and it carries no claim about any individual who works inside that form. The matched person-level instrument, and the validation of the score against what happens to people, are later work. This paper places organizations, not people.

The headline is one sentence. The score tracks the structure of how parties reach each other, not the seat of the mediator. A securities exchange is modeled at the same score as a ride-hailing platform. A staffing firm is modeled at the same score as a freelance marketplace. The human institution and the algorithmic platform of the same structure receive the same score, because the score reads the structure and is blind to what sits in the mediator's chair.

This cuts against how one literature frames the platform. Research on algorithmic management treats the algorithm as a control actor and folds the structure of coordination into the technology's particular affordances, its opacity, its reach, its speed (Kellogg, Valentine, & Christin, 2020; Vallas & Schor, 2020; Rahman, 2021). The framing is dyadic, employer against worker, and it ties the structural role to the software. No existing work scores a three-party coordination form by structural irreducibility in a way that makes a human institution and an algorithmic platform of the same structure score the same. That is the gap this paper fills.

What follows is a demonstration, not a validation. The cases instantiate the model and test whether it behaves as predicted across real, varied forms. They do not connect a Φ value to an observed coordination outcome. Section 3 enumerates the model family and places the typology. Section 4 states the case-study method. Section 5 works the five cases. Section 6 reads them across. Sections 7 through 9 give the discussion, the limits, and what the paper opens.

## 2. The unit is the coordination form, not the person

The readability analogy fixes the unit and bounds the claim. A readability score grades the text. The instrument here grades the coordination form. What the analogy lends is the unit, a property of the form rather than the participant. What it does not lend is a validated link to an outcome. Readability scores were tuned against measured reading performance over decades. This score has no such tuning yet, and the paper does not pretend otherwise.

Coordination theory already locates the unit in the structure, not the actor. Malone and Crowston define coordination as managing dependencies between activities, and they characterize a form by the kind of dependency and the mechanism that manages it, not by who occupies the coordinating role (Malone & Crowston, 1994). Crowston's taxonomy makes the move explicit. It breaks with the older habit of locating dependencies between actors and locates them between activities, so the same dependency can be managed by different mechanisms and reassigned across actors (Crowston, 1997). Coordination, on this account, can occur in human, computational, and biological systems, and the point is to carry the analysis across them.

Brokerage theory reaches the same place from the other side. Burt argues that competitive advantage is a matter of relations, not the attributes of the player, and that causation resides in the intersection of relations. The unit is a position in a social structure, and its occupant may be a person, an organization, or a larger aggregation, interchangeably (Burt, 1992). Halevy and colleagues sharpen the distinction the paper needs. Brokerage is a structural position, the occupation of a bridge between otherwise disconnected parties. Brokering is the behavior of the occupant. Different triadic configurations enable different forms of influence (Halevy, Halali, & Zlatev, 2019). The structure-not-seat claim is theirs before it is the model's. The model makes it computable.

The graded part of the score also has a precedent. Thompson ranked interdependence as pooled, sequential, and reciprocal (Thompson, 1967). Van de Ven, Delbecq, and Koenig added a fourth, more tightly coupled level, the team or intensive mode, and treated the coordination mode as the classified object (Van de Ven, Delbecq, & Koenig, 1976). A graded ladder of coordination structure is old. This paper computes one rather than assigning it, and runs it over a complete family rather than a few types.

## 3. The model and the family

The instrument is Paper 2's, and it is recalled in one paragraph. A coordination form is modeled as a small Boolean system over three nodes, the worker W, the system or mediator S, and the counterpart C. Each node updates as a function of the current state of all three. Exact IIT-4.0 system Φ over the minimum-information partition reads whether the form's cause-effect power factors. The state alphabet is fixed by Paper 2's pre-registered individuation rule, one node per party with a binary application-layer status. The binary verdict, Φ equal to zero against Φ greater than zero, is the reliable claim. Magnitude is read only ordinally. Paper 2 builds and defends the instrument; Paper 3 uses it.

The general application enumerates the whole family. A three-node wiring is any way each node's next value can depend on the other two. There are sixteen Boolean functions of two inputs, so the complete triad family is sixteen cubed, 4,096 wirings. A higher-order family of 48 four-node forms is added, where the mediator binds three parties. After removing duplicates, 4,144 distinct wirings remain. Each is scored. Most of them are not recognizable coordination forms. The enumeration is a coverage check, not a census of coordination. Its purpose is to characterize what the model does across its whole domain, and to show that the organizations placed below sit on populated, structurally meaningful bands rather than on points the author picked. This is `catalog.py`.

The scores do not spread continuously. Across all 4,096 triad wirings, 44.1 percent are reducible, with Φ exactly zero. The rest fall onto seven discrete non-zero bands.

| Φ band | wirings | reading |
|---|---|---|
| 0.00 | 1,808 (44.1%) | reducible — the wiring factors along party lines |
| 0.42 | 856 | the most common non-zero level |
| 0.50 | 24 | parity-coupled determination |
| 0.83 | 824 | partial-mediation band |
| 1.00 | 72 | |
| 1.50 | 8 | |
| 2.00 | 496 | strict-mediation band |
| 6.00 | 8 | a small exotic tail |

The bands are a property of the family, not assigned. Nearly half of all ways to couple three nodes do not produce an irreducible structure at all. The levels the organizations occupy below, 0, 0.50, 0.83, and 2.00, are populated bands of this family. This is `analyze_catalog.py`.

What drives the score is structure, and not much else. An ordinary-least-squares fit of max Φ on structural features, over all 4,096 triads, makes strict mediation the strongest single driver, with a partial coefficient of +0.54 and a group mean of 0.90 against 0.53. Parity adds +0.27 and edge density +0.24. The model reaches an R² of 0.196. Simple structural flags explain only about a fifth of the variance in Φ. Strict mediation and parity raise the score, but Φ registers an irreducibility that a count of edges or parties does not reproduce. That residual is the reason the construct uses Φ and not a checklist.

One result is read against the paper's own interest. Among genuine two-party mediators, parity determinations, the XOR and XNOR couplings, score the highest Φ, with a mean of 0.85 against 0.535 for the monotone functions. This is the model-internal echo of Cerullo's caution that trivially regular parity structures can carry high Φ, so a high Φ does not certify sophisticated coordination (Cerullo, 2015). Magnitude is therefore read ordinally and within the model, and the binary Φ equal to zero against Φ greater than zero carries the dyad-triad question.

The typology is placed on the populated bands. Each of a set of organization types is modeled as a Boolean system, its determination structure fixed before computing from how it coordinates its parties, and scored. Dyadic baselines, direct exchange and a two-party chat, sit at 0. A complementary-skill match, a parity determination, sits at 0.50. Partial-mediation forms, where the parties keep a direct channel, sit at 0.83. Strict-mediation forms, where the parties reach each other only through a joint determination, sit at 2.00. Higher-order forms, where one determination binds more than three parties, sit at 3.00. This is `typology.py`. A graded typology of this kind is a theoretical object, not a filing scheme, when its categories are derived and its placements are falsifiable (Doty & Glick, 1994). Both hold here: the bands fall out of the family, and any placement can be checked by re-modeling the form.

## 4. Method for the case studies

The cases apply an existing instrument to real organizations, which fixes the register. This is theory-driven case work, where the research question is tied to prior theory and the cases instantiate and test it (Ridder, 2017). It is not theory-building from cases, whose aim is to generate theory the data did not start with (Eisenhardt, 1989). The model is the prior theory. The cases show it doing work. The claim is calibrated accordingly. Case-based testing is weaker than experimental testing, so the five cases are a demonstration with a replication test inside it, not a definitive validation (Ridder, 2017).

The cases are selected by theory, not by sampling. The design varies one structural dimension, the determination structure, across its range, and holds another fixed, the party count. This is the diverse-case logic, whose aim is maximum variance along the dimension of interest (Seawright & Gerring, 2008), combined with controlling extraneous variance by holding the nuisance variable fixed (Burnham, Lutz, Grant, & Layton-Henry, 2008). Holding party count fixed while varying structure is the method's central move. It is also a lesson carried forward: an earlier attempt to anchor the scale on rideshare pooling failed because pooling varied party count, and Φ rose with party count, which validated only the axis the model does not need. The cases vary structure at a fixed count instead.

The five cases form a replication design.

| Case | Industry | Structure | Predicted Φ | Seat | Replication role |
|---|---|---|---|---|---|
| Uber | transportation | strict mediation | 2.00 | algorithmic | literal (with the exchange) and seat-contrast |
| NYSE / Nasdaq | financial markets | strict mediation | 2.00 | market institution | literal (with Uber) and seat-contrast |
| Upwork | professional services | partial mediation | 0.83 | algorithmic | literal (with ManpowerGroup) and seat-contrast |
| ManpowerGroup | staffing | partial mediation | 0.83 | human-institutional | literal (with Upwork) and seat-contrast |
| Amazon Mechanical Turk | crowdwork | higher-order strict | 3.00 | algorithmic | theoretical (structure binds >3 parties) |

The two equal-Φ pairs do double duty. Within a pair the cases are a literal replication on Φ: the same structure should yield the same score. Across the pair they are a theoretical contrast on the seat: the mediator is an algorithm in one and a human institution or market in the other, and the model predicts the score does not move. That pairing carries the structure-not-seat headline. The fifth case is a theoretical replication of the higher-order kind, where one determination binds more than three parties.

The modeling procedure is fixed and disclosed. Each organization is modeled under Paper 2's individuation rule. The determination structure for each is pre-registered before computing, in `cases.py`, read from the documented mechanism rather than chosen for a target score. The computation reports Φ, the band, and the minimum-information partition. Rigor here is the inferential chain, not a template. The chain runs from the organization, to the documented evidence of how it coordinates, to the classifier's inputs, to the Φ score, to the coordination-form claim, and each link is shown rather than asserted (Harley & Cornelissen, 2022). Each case discloses why it was studied, in what context, what is modeled, and how, following the transparency questions ORM expects (Pratt, 2009).

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

The analytic operation models the buyer, the exchange, and the seller as W, S, and C, with the same strict-mediation structure as Uber: `W' = S`, `S' = W ∧ C`, `C' = S`. Φ is 2.00. The form is strict mediation, and it is the twin of the ride-hailing case at a different seat. A market institution and a gig platform receive the same score, because the model reads the structure. That equality is the headline, shown on two real organizations that share nothing in industry, technology, or vocabulary.

A rival coding sits at the clearing layer rather than the matching layer. Central net settlement collapses many members' obligations into one position each against the clearinghouse, so a single determination there binds more than two parties, a higher-order structure the basic strict triad brackets. The note matters because it shows the same organization carries different structure at different layers, and the case is explicit about which layer it models. A second caveat: the precise mechanics by which the engine assigns a contra party are contested in the sources, though the absence of direct contact between buyer and seller is not.

### 5.3 Upwork — partial mediation — Φ 0.83

The unit is the coordination between a client and a freelancer around a contract. The evidence is public and provisional: Upwork's terms on circumvention and its conversion fee, its annual report, and its user agreement.

Upwork matches and hosts, and the parties coordinate directly. The platform pairs clients and freelancers and holds the contract and payment, but the client and the freelancer work together directly inside the platform. The platform polices only the off-platform boundary. Its anti-circumvention rule forbids a client and freelancer who met through Upwork from taking the relationship off the platform, because the marketplace depends on the fee collected when clients pay freelancers on it, and a conversion fee lets the relationship move off-platform lawfully once paid (Upwork, 2024). The direct channel is open on the platform and closed off it.

The analytic operation models the freelancer, the platform, and the client as W, S, and C. The platform commits a joint match, and each party reads the platform and the other party: `W' = S ∨ C`, `S' = W ∧ C`, `C' = S ∨ W`. Φ is 0.83. The form is partial mediation, because the parties keep a direct channel and the structure does not reduce to pure mediation.

A rival coding follows the channel. The anti-circumvention rule is the documented version of a pattern Paper 2 named, a platform with a reason to suppress the direct channel so the coordination cannot collapse to the pair. Here the platform suppresses only the off-platform channel and leaves the on-platform one open, which is why the form is partial and not strict. If the platform forbade all direct contact, the model would move it toward strict mediation. The permanent-closure penalty is "can result in" rather than automatic, given the conversion-fee exception.

### 5.4 ManpowerGroup — partial mediation — Φ 0.83

The unit is the coordination between a placed worker and a client firm on an assignment. The evidence is public and provisional: ManpowerGroup's worker-facing description of how placement works, its annual report, and jurisdictional staffing terms.

ManpowerGroup places and then steps back from the day-to-day. The agency screens, assesses, and commits the placement, and for temporary roles it is the legal employer of record: the worker is employed through Manpower and placed at the client's worksite. The client directs the day-to-day work. Manpower's own guidance tells the placed worker that the on-site supervisor is the resource for daily questions while Manpower remains the employer (ManpowerGroup, 2024). The agency commits the match and stays the employer, but it does not stand between the parties' working relationship.

The analytic operation models the worker, the agency, and the client as W, S, and C, with the same partial-mediation structure as Upwork: `W' = S ∨ C`, `S' = W ∧ C`, `C' = S ∨ W`. Φ is 0.83. The form is partial mediation, and it is the twin of the freelance marketplace at a different seat. A human-run staffing institution and an algorithmic marketplace receive the same score, because both match the parties and leave them a direct working channel.

A rival coding turns on the contract. Temp-to-perm conversion terms and any non-circumvention clause, not stated on the public worker-facing page, could tighten or loosen the direct channel and move the score. This is flagged for the field data that will replace the provisional evidence.

### 5.5 Amazon Mechanical Turk — higher-order strict mediation — Φ 3.00

The unit is the coordination between a requester and the worker or workers on a task. The evidence is public and provisional: Amazon's requester and worker documentation for the platform.

Mechanical Turk binds requester and workers only through the platform, and one task can bind several. A requester posts a task, a HIT, to the marketplace. Workers find it, self-select, accept, and submit. The requester sets qualifications that gate who may work and approves or rejects the result. The platform sits in the payment path, transferring the reward from the requester's account to the worker's on approval (Amazon Web Services, 2024). There is no direct requester-worker channel. A single HIT can be assigned to many workers at once, so one determination binds the requester and multiple workers, with the platform as payment intermediary.

The analytic operation models the requester, the platform, two workers, and adds a fourth node. The system commits a joint determination over all parties: `S' = W ∧ C ∧ D` over four nodes, with each party reading the system. Φ is 3.00. The form is higher-order strict mediation, where one determination binds more than three parties.

A caveat bounds the number. The four-node Φ is partly a function of system size, so 3.00 is not strictly comparable to the 0-to-2.00 triad band. A single-assignment HIT, one requester and one worker through the platform, is an ordinary strict triad at 2.00. The higher-order score shows the scale extends upward when a determination binds more parties, and it says so without claiming cross-size comparability.

## 6. Reading the cases across

The cases sort by structure when laid in a row. Ordered along the determination dimension, the matrix reads cleanly: the partial-mediation pair keeps a direct channel and scores 0.83; the strict-mediation pair closes the channel and scores 2.00; the higher-order case binds extra parties and scores 3.00. The rows that decide the score are whether the parties reach each other only through the system, and whether a direct channel exists. The seat of the mediator is not one of those rows.

| dimension | Upwork | ManpowerGroup | Uber | NYSE/Nasdaq | MTurk |
|---|---|---|---|---|---|
| only through S? | no | no | yes | yes | yes |
| direct channel? | yes | yes | no | no | no |
| determination | joint match | joint placement | joint dispatch | joint order match | joint, >2 parties |
| seat | algorithmic | human-institutional | algorithmic | market institution | algorithmic |
| Φ band | 0.83 | 0.83 | 2.00 | 2.00 | 3.00 |

The two equal-Φ pairs carry the headline. Upwork and ManpowerGroup match the parties and leave them a channel, and both land at 0.83 though one mediates by software and the other by a staffing institution. Uber and a securities exchange interpose a joint determination with no direct channel, and both land at 2.00 though one is a gig platform and the other a market. The equality is a modeling property, not an empirical discovery. The court-like exchange and the gig platform get the same score because they are coded to the same structure, and the model is indifferent to the seat once the structure is fixed. That indifference is the property the paper wants, and it is what the pairs display.

The cases are not cherry-picked, because they sit on populated bands of the family. The 0.83 band holds 824 wirings, the 2.00 band 496, and the higher-order forms populate the upper range. The five organizations occupy levels the enumeration filled on its own, not points chosen to make a figure.

What the cases add beyond the model is the demonstration that the tool sorts real, documented coordination by structure and cuts against the obvious labels. A securities exchange, a staffing firm, and a crowdwork platform do not group by industry, and they do not group by whether a human or an algorithm sits in the middle. They group by how the parties reach each other. That is the analytic work the score does that an industry label and a glance at the mediator do not.

## 7. Discussion

Structure sets the score, and the result has a lineage. Coordination theory holds that the form lives in the dependency, not the actor, and that the analysis carries across human and computational systems (Malone & Crowston, 1994). Brokerage theory holds that the advantage lives in the position, and that a person and an organization are interchangeable occupants of it (Burt, 1992). Two-sided-market theory defines the intermediary by its coordinating function rather than its substance (Rochet & Tirole, 2006). Each of these says, qualitatively, that the structure matters and the occupant's nature is secondary. The model turns that into a computed score and shows it on real corporations.

The score brackets what depends on the mediator's nature, and the bracketing is deliberate. A reader will object that a human institution and an algorithmic platform are not the same, because opacity, power, and accountability differ with the mediator's nature, and those differences are real and consequential (Rahman, 2021). The objection is correct and does not touch the claim. Φ measures the structural irreducibility of the mediation. It is the analytic object, not the whole of the matter. Opacity, power, and accountability are contingencies layered on top of an identical structural score, not parts of it. This is the same separation Paper 2 drew between how opaque a mediator is and whether the coordination factors, two properties that vary independently. Two forms of the same structure pose the same coordination problem, and they can still differ without limit in how opaque, powerful, or accountable the mediator is. The model does not say otherwise.

What the score buys an analyst is a placement that is blind to sector and blind to seat. Handed an organization, the analyst can model how it coordinates its parties and place it on a graded scale, rather than sort it by its industry or by whether its mediator is software. The placement is a discipline against two easy errors: reading triadicity off the industry label, and reading it off the mediator's technology. The cases show both errors corrected, a market scored like a platform and a staffing firm scored like a marketplace.

The typology earns its standing as theory rather than classification. Its categories are derived from the family rather than stipulated, and every placement is falsifiable by re-modeling the form (Doty & Glick, 1994). A classification sorts into bins someone chose. This typology reports bands the enumeration produced and places organizations on them by a stated procedure.

## 8. Limitations

The paper demonstrates, it does not validate against the world. No Φ value here is connected to an observed coordination outcome, a worker's earnings, a task's success, a dyad's stability. The cases instantiate and replicate the model; they do not test it the way an experiment would (Ridder, 2017). The cases are provisional. Their evidence is public documentation, to be replaced and extended with field data, and each case marks the status of its inputs. Magnitude is ordinal only, and the parity result inside the family is the standing reason (Cerullo, 2015). The higher-order score at four nodes is partly a function of system size and is not strictly comparable to the three-node band. The equivalence claim is structural, and it brackets the normative and distributive consequences that depend on the mediator's nature. The modeling choices Paper 2 named, the state alphabet and the reads, are carried here: they are declared in advance, contestable, and auditable, and a different faithful model can place a form differently.

## 9. Conclusion

Paper 2 sorted coordination forms into two kinds. Paper 3 graded the sort and applied it. The complete family of three-node forms falls onto a handful of discrete bands, and real organizations land on populated ones. Five large corporations, modeled from how they actually coordinate, place by structure: a securities exchange scores like a ride-hailing platform, a staffing firm scores like a freelance marketplace, and a crowdwork platform extends the scale upward. The score reads the structure of how parties reach each other and is blind to the seat of the mediator. This is a formal-model result demonstrated on real cases. What remains is the empirical program it opens: calibrating the scale against coordination outcomes, on data that varies structure at a fixed party count, and building the matched person-level instrument that the readability analogy promises and this paper does not yet deliver.

---

## Data and code availability

Every numerical result is reproducible from a script in `rebuild/`, run with the project's PyPhi 4.0 environment. `phi_core.py` is the measure, re-derived from scratch and depending only on PyPhi; it reproduces Paper 2's controls exactly at three nodes. `catalog.py` and `analyze_catalog.py` enumerate and analyze the 4,144-form family. `typology.py` places the organization typology. `cases.py` computes the five case models.

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

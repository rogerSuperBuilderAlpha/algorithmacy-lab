# Paper 3 — 103 micro-coordination scenarios, in the case-study structure

> Model-internal catalog. Each scenario is a real micro-activity, coded from its
> coordination mechanism (the rationale column) to a structural archetype BEFORE
> computing, then scored with exact IIT-4.0 Φ (`phi_core`). Reproduce with
> `micro_scenarios.py`. This is the micro-scale companion to the corporate cases
> (`cases.py`) and the dyadic controls (`dyadic_cases.py`).

## The finding

- **103 surface-distinct activities** collapse onto **5 Φ values**: 0.0, 0.5, 0.83, 2.0, 3.0.
- **48 of 103 (47%) are dyadic (Φ=0)** — the instrument does not stamp everything triadic.
- Activities group by **mechanism, not surface**: ordering lunch is dyadic through a waiter (a conduit) and strict through DoorDash (a joint dispatch); the surface 'order lunch' is the same, the structure is not.

| Φ band | scenarios |
|---|---|
| 0.00 (moderated dyad) | 48 |
| 0.50 (parity) | 6 |
| 0.83 (partial mediation) | 14 |
| 2.00 (strict mediation) | 22 |
| 3.00 (higher-order strict) | 13 |

## The case structure (per scenario): bounded unit / coordinating parties / mechanism / structural coding / Φ-verdict


### Φ = 0.00 — moderated dyad

| # | micro-activity | coordinating parties | coordination mechanism (coded) | structure | Φ |
|---|---|---|---|---|---|
| 1 | Texting a friend to meet for coffee | two friends | they arrange it directly; the carrier is inert | DIRECT | 0.00 |
| 2 | Asking a coworker a question at their desk | two coworkers | face-to-face, no intermediary | DIRECT | 0.00 |
| 3 | Paying a friend back in cash | two friends | hand-to-hand, no third party | DIRECT | 0.00 |
| 4 | Negotiating a price at a flea market | buyer, seller | they haggle directly | DIRECT | 0.00 |
| 5 | Borrowing a tool from a neighbor | two neighbors | direct request and handover | DIRECT | 0.00 |
| 6 | Buying coffee at a café counter | customer, barista | direct two-party exchange | DIRECT | 0.00 |
| 7 | Getting a haircut by walking in | customer, barber | direct service, no booking | DIRECT | 0.00 |
| 8 | Hailing a taxi on the street | rider, driver | direct flag-down, no dispatch | DIRECT | 0.00 |
| 9 | Buying a concert ticket from a friend reselling it | two friends | direct resale | DIRECT | 0.00 |
| 10 | Carpooling with a coworker arranged in person | two coworkers | arranged directly | DIRECT | 0.00 |
| 11 | A one-on-one video call | two people | two-party live exchange | DIRECT | 0.00 |
| 12 | Resolving a git merge conflict between two developers | two devs | they reconcile branches directly | DIRECT | 0.00 |
| 13 | Tipping a barista | customer, barista | direct transfer | DIRECT | 0.00 |
| 14 | Asking a librarian for a book | patron, librarian | direct request | DIRECT | 0.00 |
| 15 | Two kids trading lunch items | two kids | direct swap | DIRECT | 0.00 |
| 16 | A handshake deal between two shopkeepers | two shopkeepers | direct agreement | DIRECT | 0.00 |
| 17 | Passing a note to a classmate | two classmates | direct hand-off | DIRECT | 0.00 |
| 18 | Sharing a doc by handing over a USB drive | two people | direct physical transfer | DIRECT | 0.00 |
| 19 | Sending a letter by postal mail | sender, recipient | the post carries; recipient's state does not gate routing | CONDUIT | 0.00 |
| 20 | Sending an email to a coworker | sender, recipient | store-and-forward conduit | CONDUIT | 0.00 |
| 21 | Leaving a voicemail | caller, callee | the system stores and relays | CONDUIT | 0.00 |
| 22 | Faxing a form | sender, recipient | the line carries the page | CONDUIT | 0.00 |
| 23 | Posting a flyer on a community board | poster, reader | the board displays; no joint determination | CONDUIT | 0.00 |
| 24 | Ordering pizza by phone for delivery | diner, pizzeria | the call relays the order the diner placed | CONDUIT | 0.00 |
| 25 | Ordering at a restaurant through a waiter | diner, kitchen | the waiter carries the order to the kitchen | CONDUIT | 0.00 |
| 26 | Posting in a Slack channel | poster, channel | broadcast carry to a channel | CONDUIT | 0.00 |
| 27 | Sending a Slack DM | two coworkers | the app relays a message they exchange | CONDUIT | 0.00 |
| 28 | Filing a GitHub issue | reporter, maintainer | the tracker carries the report; maintainer responds | CONDUIT | 0.00 |
| 29 | RSVPing to an event via Evite | guest, host | the tool relays the reply | CONDUIT | 0.00 |
| 30 | Pre-ordering coffee on the Starbucks app | customer, store | the app carries the order the customer placed | CONDUIT | 0.00 |
| 31 | Scheduling a doctor visit by phone | patient, clinic | the receptionist relays availability | CONDUIT | 0.00 |
| 32 | Booking a barber by phone | customer, barber | the call relays the booking | CONDUIT | 0.00 |
| 33 | Donating to a charity online | donor, charity | the processor carries the agreed gift | CONDUIT | 0.00 |
| 34 | Reserving a meeting room on the office calendar | worker, room | the system carries the reservation | CONDUIT | 0.00 |
| 35 | Ordering a pizza via the chain's own app | diner, pizzeria | the app carries the diner's order | CONDUIT | 0.00 |
| 36 | Booking a flight on an airline's site | traveler, airline | the site carries the traveler's selection | CONDUIT | 0.00 |
| 37 | Drafting a document in a word processor | worker, tool | no third party; the tool serves one user | TOOL | 0.00 |
| 38 | Doing taxes with tax software | filer, software | two-party human-machine | TOOL | 0.00 |
| 39 | Querying a search engine | user, engine | no counterpart coordinated | TOOL | 0.00 |
| 40 | Asking a chatbot a question | user, model | Paper 2's dyadic limit | TOOL | 0.00 |
| 41 | Editing a photo in an app | user, app | solo tool use | TOOL | 0.00 |
| 42 | Tracking a run with a fitness app | runner, app | two-party human-machine | TOOL | 0.00 |
| 43 | Setting a reminder with a voice assistant | user, assistant | no counterpart | TOOL | 0.00 |
| 44 | Using a self-checkout kiosk | shopper, kiosk | two-party human-machine | TOOL | 0.00 |
| 45 | Buying a snack from a vending machine | buyer, machine | two-party, no counterpart | TOOL | 0.00 |
| 46 | Withdrawing cash at an ATM | customer, machine | two-party human-machine | TOOL | 0.00 |
| 47 | Triggering a deploy in a CI pipeline | developer, pipeline | the dev runs a tool; no counterpart party | TOOL | 0.00 |
| 48 | Generating a report in a BI dashboard | analyst, dashboard | two-party human-machine | TOOL | 0.00 |

### Φ = 0.50 — parity

| # | micro-activity | coordinating parties | coordination mechanism (coded) | structure | Φ |
|---|---|---|---|---|---|
| 1 | Kidney paired-exchange matching | donor, recipient | match is on complementary compatibility | PARITY | 0.50 |
| 2 | Language-exchange partner match | learner A, learner B | each teaches what the other learns | PARITY | 0.50 |
| 3 | Carpool matching opposite commutes | rider, driver | match on complementary routes | PARITY | 0.50 |
| 4 | Mentorship match pairing complementary needs | mentor, mentee | complementary skills paired | PARITY | 0.50 |
| 5 | Skill-swap platform match | two members | each offers what the other needs | PARITY | 0.50 |
| 6 | Roommate match on complementary schedules | two seekers | opposite schedules paired | PARITY | 0.50 |

### Φ = 0.83 — partial mediation

| # | micro-activity | coordinating parties | coordination mechanism (coded) | structure | Φ |
|---|---|---|---|---|---|
| 1 | Booking a stay on Airbnb | guest, host | platform matches, then they message directly | PARTIAL | 0.83 |
| 2 | Hiring a plumber via Thumbtack | homeowner, plumber | matched, then deal directly | PARTIAL | 0.83 |
| 3 | Finding a tutor on a platform | student, tutor | matched, then arrange directly | PARTIAL | 0.83 |
| 4 | Hiring a freelancer on Upwork | client, freelancer | matched, coordinate directly on-platform | PARTIAL | 0.83 |
| 5 | Matching with a dog-walker on Rover | owner, walker | matched, then coordinate directly | PARTIAL | 0.83 |
| 6 | Booking a photographer via a directory | client, photographer | matched, then arrange directly | PARTIAL | 0.83 |
| 7 | Arranging a house cleaner via an app | household, cleaner | matched, then deal directly | PARTIAL | 0.83 |
| 8 | Splitting a bill via a Venmo request | two friends | they agreed; the processor authorizes jointly | PARTIAL | 0.83 |
| 9 | Wiring money via a bank | payer, payee | they agreed; the bank authorizes on both | PARTIAL | 0.83 |
| 10 | Opening a GitHub pull request for review | author, reviewer | they discuss directly; a merge gate also binds | PARTIAL | 0.83 |
| 11 | Finding a contractor on Angi | homeowner, contractor | matched, then contract directly | PARTIAL | 0.83 |
| 12 | Booking a wedding venue after a tour | couple, venue | introduced, then negotiate directly | PARTIAL | 0.83 |
| 13 | Selling a couch on Facebook Marketplace | seller, buyer | listed, then arrange pickup directly | PARTIAL | 0.83 |
| 14 | Finding a band for an event via a roster | host, band | matched, then coordinate directly | PARTIAL | 0.83 |

### Φ = 2.00 — strict mediation

| # | micro-activity | coordinating parties | coordination mechanism (coded) | structure | Φ |
|---|---|---|---|---|---|
| 1 | Ordering lunch on DoorDash | diner, restaurant | the dispatch jointly matches; no direct channel | STRICT | 2.00 |
| 2 | Hailing an Uber | rider, driver | the dispatch commits the match | STRICT | 2.00 |
| 3 | Matching on a dating app | two users | the mutual-match gate must fire before contact | STRICT | 2.00 |
| 4 | Applying for a job via an ATS | applicant, manager | the screen jointly gates forward/reject | STRICT | 2.00 |
| 5 | Bidding in an eBay auction | bidder, seller | the auction engine matches at close | STRICT | 2.00 |
| 6 | Getting a support ticket routed to an agent | customer, agent | the router jointly assigns | STRICT | 2.00 |
| 7 | A 911 call routed to a responder | caller, responder | dispatch commits the assignment | STRICT | 2.00 |
| 8 | Air-traffic control sequencing two aircraft | pilot A, pilot B | ATC commits the joint sequence | STRICT | 2.00 |
| 9 | A trade matched on a stock exchange | buyer, seller | the exchange matches; no direct contact | STRICT | 2.00 |
| 10 | Reserving a table on OpenTable | diner, restaurant | the reservation gate jointly fits request to availability | STRICT | 2.00 |
| 11 | Reserving a campsite on recreation.gov | camper, site | the portal allocates the site | STRICT | 2.00 |
| 12 | Buying a concert seat on Ticketmaster | fan, venue | the platform allocates the seat | STRICT | 2.00 |
| 13 | Calling a taxi dispatch line | rider, driver | the dispatcher commits the match | STRICT | 2.00 |
| 14 | Being seated by a restaurant host | party, table | the host jointly assigns party to table | STRICT | 2.00 |
| 15 | Booking a haircut slot via an app | customer, stylist | the app commits the slot match | STRICT | 2.00 |
| 16 | Getting matched to a courier on a delivery app | sender, courier | the dispatch commits the match | STRICT | 2.00 |
| 17 | Reselling a ticket via StubHub | reseller, buyer | the platform matches at sale; no direct contact | STRICT | 2.00 |
| 18 | Carpool matching via an app | rider, driver | the app commits the match | STRICT | 2.00 |
| 19 | Scheduling a meeting via Calendly | inviter, invitee | the link jointly fits the invitee's pick to open slots | STRICT | 2.00 |
| 20 | Returning a package via a carrier drop-off | sender, retailer | the carrier+system jointly commit the return | STRICT | 2.00 |
| 21 | Getting matched to a therapist on a platform | client, therapist | the platform commits the match | STRICT | 2.00 |
| 22 | A warehouse pick assigned by a WMS | picker, order | the system jointly assigns pick to picker | STRICT | 2.00 |

### Φ = 3.00 — higher-order strict (n=4 form; size-normalized Φ/(n−1) = 1.00, the strict level)

| # | micro-activity | coordinating parties | coordination mechanism (coded) | structure | Φ |
|---|---|---|---|---|---|
| 1 | A group dinner reservation for several diners | diners, venue | one booking binds many diners and the venue | HIGHER | 3.00 (norm 1.00) |
| 2 | A Groupon group-buy | many buyers, merchant | the deal fires only if enough buyers commit | HIGHER | 3.00 (norm 1.00) |
| 3 | A multi-party conference-call bridge | many callers | one bridge binds all participants | HIGHER | 3.00 (norm 1.00) |
| 4 | A multi-worker MTurk consensus HIT | requester, many workers | one task binds many workers | HIGHER | 3.00 (norm 1.00) |
| 5 | A pooled carpool ride (driver + 2 riders) | driver, riders | one pool binds driver and riders | HIGHER | 3.00 (norm 1.00) |
| 6 | A multi-party contract e-signing | several signatories | one determination binds all signers | HIGHER | 3.00 (norm 1.00) |
| 7 | A team scheduling poll (Doodle) | many teammates | one slot must satisfy the group | HIGHER | 3.00 (norm 1.00) |
| 8 | A potluck sign-up coordinating contributors | many contributors | one plan binds all dishes | HIGHER | 3.00 (norm 1.00) |
| 9 | Crowdfunding a project on Kickstarter | many backers, creator | the project funds only if the goal binds enough backers | HIGHER | 3.00 (norm 1.00) |
| 10 | A group office lunch order | many coworkers, restaurant | one order binds many diners and the kitchen | HIGHER | 3.00 (norm 1.00) |
| 11 | A multi-leg trip booked as one itinerary | traveler, several carriers | one booking binds all legs | HIGHER | 3.00 (norm 1.00) |
| 12 | A syndicated loan across several lenders | borrower, lenders | one facility binds many lenders | HIGHER | 3.00 (norm 1.00) |
| 13 | A multi-sided ad auction | advertiser, publisher, user | one auction binds all sides | HIGHER | 3.00 (norm 1.00) |

## Honest bounds

- The Φ of each scenario follows from its **pre-registered structural coding**, not from a per-scenario discovery; the catalog's claim is about the coding (surface variety, structural sparsity), not about the world.
- Codings are contestable and sit at the boundaries the dyadic controls exposed: a peer payment is coded PARTIAL (the processor authorizes jointly), a GitHub PR PARTIAL (direct discussion plus a merge gate); a reasonable analyst could re-code these, and the band would move. Each rationale is the auditable coding decision.
- Magnitude is ordinal; the higher-order raw Φ is size-scaled (normalized in the table).

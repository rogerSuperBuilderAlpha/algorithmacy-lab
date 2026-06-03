"""Paper 3 rebuild — 100 micro-coordination scenarios (surface variety vs structural sparsity).

The corporate cases and the dyadic controls are organization-scale. This file drops to the micro
level: 100 everyday coordination activities, all distinct on the surface (ordering lunch, opening a
GitHub pull request, booking a venue, splitting a bill, hailing a cab, ...). Each is coded from its
actual coordination mechanism, BEFORE computing, to one of seven structural archetypes, and exact
IIT-4.0 Φ is computed. The test: do 100 surface-distinct activities collapse onto the handful of
structural bands the family produces? The coding is pre-registered (each scenario carries a one-line
mechanism rationale); the assignment is by structure, not to hit a target.

This is a catalog, model-internal, coded from documented/observed mechanism. It is the micro-scale
companion to cases.py (corporate) and dyadic_cases.py (negative control). It writes a case-study-
structured markdown catalog to MICRO_SCENARIOS.md.

Archetypes (Boolean rules over W=party A, S=intermediary, C=party B; D=4th party for higher-order):
  DIRECT   parties deal directly, intermediary inert        W'=C, S'=S, C'=W            -> Φ 0
  CONDUIT  intermediary carries, does not commit             W'=S, S'=W, C'=S            -> Φ 0
  TOOL     two-party human-machine, no counterpart           W'=S, S'=W, C'=C            -> Φ 0
  PARITY   complementary match (XOR determination)           W'=S, S'=W⊕C, C'=S          -> Φ 0.5
  PARTIAL  matched, parties keep a direct channel            W'=S∨C, S'=W∧C, C'=S∨W      -> Φ 0.83
  STRICT   reach each other only through a joint determination W'=S, S'=W∧C, C'=S         -> Φ 2.0
  HIGHER   one determination binds >3 parties (n=4)          S'=W∧C∧D, parties read S    -> Φ 3.0

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/micro_scenarios.py
"""

import os, sys
from collections import Counter, defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from phi_core import placement

ARCHETYPES = {
    "DIRECT":  ([lambda x: x[2], lambda x: x[1], lambda x: x[0]], 3),
    "CONDUIT": ([lambda x: x[1], lambda x: x[0], lambda x: x[1]], 3),
    "TOOL":    ([lambda x: x[1], lambda x: x[0], lambda x: x[2]], 3),
    "PARITY":  ([lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]], 3),
    "PARTIAL": ([lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),
    "STRICT":  ([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),
    "HIGHER":  ([lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], 4),
}

# (scenario, parties, mechanism rationale, archetype). Coded by mechanism, pre-registered.
SCENARIOS = [
    # --- DIRECT: two parties coordinate directly; any intermediary is inert -------------
    ("Texting a friend to meet for coffee", "two friends", "they arrange it directly; the carrier is inert", "DIRECT"),
    ("Asking a coworker a question at their desk", "two coworkers", "face-to-face, no intermediary", "DIRECT"),
    ("Paying a friend back in cash", "two friends", "hand-to-hand, no third party", "DIRECT"),
    ("Negotiating a price at a flea market", "buyer, seller", "they haggle directly", "DIRECT"),
    ("Borrowing a tool from a neighbor", "two neighbors", "direct request and handover", "DIRECT"),
    ("Buying coffee at a café counter", "customer, barista", "direct two-party exchange", "DIRECT"),
    ("Getting a haircut by walking in", "customer, barber", "direct service, no booking", "DIRECT"),
    ("Hailing a taxi on the street", "rider, driver", "direct flag-down, no dispatch", "DIRECT"),
    ("Buying a concert ticket from a friend reselling it", "two friends", "direct resale", "DIRECT"),
    ("Carpooling with a coworker arranged in person", "two coworkers", "arranged directly", "DIRECT"),
    ("A one-on-one video call", "two people", "two-party live exchange", "DIRECT"),
    ("Resolving a git merge conflict between two developers", "two devs", "they reconcile branches directly", "DIRECT"),
    ("Tipping a barista", "customer, barista", "direct transfer", "DIRECT"),
    ("Asking a librarian for a book", "patron, librarian", "direct request", "DIRECT"),
    ("Two kids trading lunch items", "two kids", "direct swap", "DIRECT"),
    ("A handshake deal between two shopkeepers", "two shopkeepers", "direct agreement", "DIRECT"),
    ("Passing a note to a classmate", "two classmates", "direct hand-off", "DIRECT"),
    ("Sharing a doc by handing over a USB drive", "two people", "direct physical transfer", "DIRECT"),

    # --- CONDUIT: an intermediary carries the message/value but does not commit a joint determination
    ("Sending a letter by postal mail", "sender, recipient", "the post carries; recipient's state does not gate routing", "CONDUIT"),
    ("Sending an email to a coworker", "sender, recipient", "store-and-forward conduit", "CONDUIT"),
    ("Leaving a voicemail", "caller, callee", "the system stores and relays", "CONDUIT"),
    ("Faxing a form", "sender, recipient", "the line carries the page", "CONDUIT"),
    ("Posting a flyer on a community board", "poster, reader", "the board displays; no joint determination", "CONDUIT"),
    ("Ordering pizza by phone for delivery", "diner, pizzeria", "the call relays the order the diner placed", "CONDUIT"),
    ("Ordering at a restaurant through a waiter", "diner, kitchen", "the waiter carries the order to the kitchen", "CONDUIT"),
    ("Posting in a Slack channel", "poster, channel", "broadcast carry to a channel", "CONDUIT"),
    ("Sending a Slack DM", "two coworkers", "the app relays a message they exchange", "CONDUIT"),
    ("Filing a GitHub issue", "reporter, maintainer", "the tracker carries the report; maintainer responds", "CONDUIT"),
    ("RSVPing to an event via Evite", "guest, host", "the tool relays the reply", "CONDUIT"),
    ("Pre-ordering coffee on the Starbucks app", "customer, store", "the app carries the order the customer placed", "CONDUIT"),
    ("Scheduling a doctor visit by phone", "patient, clinic", "the receptionist relays availability", "CONDUIT"),
    ("Booking a barber by phone", "customer, barber", "the call relays the booking", "CONDUIT"),
    ("Donating to a charity online", "donor, charity", "the processor carries the agreed gift", "CONDUIT"),
    ("Reserving a meeting room on the office calendar", "worker, room", "the system carries the reservation", "CONDUIT"),
    ("Ordering a pizza via the chain's own app", "diner, pizzeria", "the app carries the diner's order", "CONDUIT"),
    ("Booking a flight on an airline's site", "traveler, airline", "the site carries the traveler's selection", "CONDUIT"),

    # --- TOOL: two-party human-machine; no counterpart is coordinated -------------------
    ("Drafting a document in a word processor", "worker, tool", "no third party; the tool serves one user", "TOOL"),
    ("Doing taxes with tax software", "filer, software", "two-party human-machine", "TOOL"),
    ("Querying a search engine", "user, engine", "no counterpart coordinated", "TOOL"),
    ("Asking a chatbot a question", "user, model", "Paper 2's dyadic limit", "TOOL"),
    ("Editing a photo in an app", "user, app", "solo tool use", "TOOL"),
    ("Tracking a run with a fitness app", "runner, app", "two-party human-machine", "TOOL"),
    ("Setting a reminder with a voice assistant", "user, assistant", "no counterpart", "TOOL"),
    ("Using a self-checkout kiosk", "shopper, kiosk", "two-party human-machine", "TOOL"),
    ("Buying a snack from a vending machine", "buyer, machine", "two-party, no counterpart", "TOOL"),
    ("Withdrawing cash at an ATM", "customer, machine", "two-party human-machine", "TOOL"),
    ("Triggering a deploy in a CI pipeline", "developer, pipeline", "the dev runs a tool; no counterpart party", "TOOL"),
    ("Generating a report in a BI dashboard", "analyst, dashboard", "two-party human-machine", "TOOL"),

    # --- PARITY: complementary (opposite-attribute) matching ----------------------------
    ("Kidney paired-exchange matching", "donor, recipient", "match is on complementary compatibility", "PARITY"),
    ("Language-exchange partner match", "learner A, learner B", "each teaches what the other learns", "PARITY"),
    ("Carpool matching opposite commutes", "rider, driver", "match on complementary routes", "PARITY"),
    ("Mentorship match pairing complementary needs", "mentor, mentee", "complementary skills paired", "PARITY"),
    ("Skill-swap platform match", "two members", "each offers what the other needs", "PARITY"),
    ("Roommate match on complementary schedules", "two seekers", "opposite schedules paired", "PARITY"),

    # --- PARTIAL: matched, then the parties keep a direct channel ------------------------
    ("Booking a stay on Airbnb", "guest, host", "platform matches, then they message directly", "PARTIAL"),
    ("Hiring a plumber via Thumbtack", "homeowner, plumber", "matched, then deal directly", "PARTIAL"),
    ("Finding a tutor on a platform", "student, tutor", "matched, then arrange directly", "PARTIAL"),
    ("Hiring a freelancer on Upwork", "client, freelancer", "matched, coordinate directly on-platform", "PARTIAL"),
    ("Matching with a dog-walker on Rover", "owner, walker", "matched, then coordinate directly", "PARTIAL"),
    ("Booking a photographer via a directory", "client, photographer", "matched, then arrange directly", "PARTIAL"),
    ("Arranging a house cleaner via an app", "household, cleaner", "matched, then deal directly", "PARTIAL"),
    ("Splitting a bill via a Venmo request", "two friends", "they agreed; the processor authorizes jointly", "PARTIAL"),
    ("Wiring money via a bank", "payer, payee", "they agreed; the bank authorizes on both", "PARTIAL"),
    ("Opening a GitHub pull request for review", "author, reviewer", "they discuss directly; a merge gate also binds", "PARTIAL"),
    ("Finding a contractor on Angi", "homeowner, contractor", "matched, then contract directly", "PARTIAL"),
    ("Booking a wedding venue after a tour", "couple, venue", "introduced, then negotiate directly", "PARTIAL"),
    ("Selling a couch on Facebook Marketplace", "seller, buyer", "listed, then arrange pickup directly", "PARTIAL"),
    ("Finding a band for an event via a roster", "host, band", "matched, then coordinate directly", "PARTIAL"),

    # --- STRICT: parties reach each other only through a joint determination ------------
    ("Ordering lunch on DoorDash", "diner, restaurant", "the dispatch jointly matches; no direct channel", "STRICT"),
    ("Hailing an Uber", "rider, driver", "the dispatch commits the match", "STRICT"),
    ("Matching on a dating app", "two users", "the mutual-match gate must fire before contact", "STRICT"),
    ("Applying for a job via an ATS", "applicant, manager", "the screen jointly gates forward/reject", "STRICT"),
    ("Bidding in an eBay auction", "bidder, seller", "the auction engine matches at close", "STRICT"),
    ("Getting a support ticket routed to an agent", "customer, agent", "the router jointly assigns", "STRICT"),
    ("A 911 call routed to a responder", "caller, responder", "dispatch commits the assignment", "STRICT"),
    ("Air-traffic control sequencing two aircraft", "pilot A, pilot B", "ATC commits the joint sequence", "STRICT"),
    ("A trade matched on a stock exchange", "buyer, seller", "the exchange matches; no direct contact", "STRICT"),
    ("Reserving a table on OpenTable", "diner, restaurant", "the reservation gate jointly fits request to availability", "STRICT"),
    ("Reserving a campsite on recreation.gov", "camper, site", "the portal allocates the site", "STRICT"),
    ("Buying a concert seat on Ticketmaster", "fan, venue", "the platform allocates the seat", "STRICT"),
    ("Calling a taxi dispatch line", "rider, driver", "the dispatcher commits the match", "STRICT"),
    ("Being seated by a restaurant host", "party, table", "the host jointly assigns party to table", "STRICT"),
    ("Booking a haircut slot via an app", "customer, stylist", "the app commits the slot match", "STRICT"),
    ("Getting matched to a courier on a delivery app", "sender, courier", "the dispatch commits the match", "STRICT"),
    ("Reselling a ticket via StubHub", "reseller, buyer", "the platform matches at sale; no direct contact", "STRICT"),
    ("Carpool matching via an app", "rider, driver", "the app commits the match", "STRICT"),
    ("Scheduling a meeting via Calendly", "inviter, invitee", "the link jointly fits the invitee's pick to open slots", "STRICT"),
    ("Returning a package via a carrier drop-off", "sender, retailer", "the carrier+system jointly commit the return", "STRICT"),
    ("Getting matched to a therapist on a platform", "client, therapist", "the platform commits the match", "STRICT"),
    ("A warehouse pick assigned by a WMS", "picker, order", "the system jointly assigns pick to picker", "STRICT"),

    # --- HIGHER: one determination binds more than three parties ------------------------
    ("A group dinner reservation for several diners", "diners, venue", "one booking binds many diners and the venue", "HIGHER"),
    ("A Groupon group-buy", "many buyers, merchant", "the deal fires only if enough buyers commit", "HIGHER"),
    ("A multi-party conference-call bridge", "many callers", "one bridge binds all participants", "HIGHER"),
    ("A multi-worker MTurk consensus HIT", "requester, many workers", "one task binds many workers", "HIGHER"),
    ("A pooled carpool ride (driver + 2 riders)", "driver, riders", "one pool binds driver and riders", "HIGHER"),
    ("A multi-party contract e-signing", "several signatories", "one determination binds all signers", "HIGHER"),
    ("A team scheduling poll (Doodle)", "many teammates", "one slot must satisfy the group", "HIGHER"),
    ("A potluck sign-up coordinating contributors", "many contributors", "one plan binds all dishes", "HIGHER"),
    ("Crowdfunding a project on Kickstarter", "many backers, creator", "the project funds only if the goal binds enough backers", "HIGHER"),
    ("A group office lunch order", "many coworkers, restaurant", "one order binds many diners and the kitchen", "HIGHER"),
    ("A multi-leg trip booked as one itinerary", "traveler, several carriers", "one booking binds all legs", "HIGHER"),
    ("A syndicated loan across several lenders", "borrower, lenders", "one facility binds many lenders", "HIGHER"),
    ("A multi-sided ad auction", "advertiser, publisher, user", "one auction binds all sides", "HIGHER"),
]


def main():
    rows = []
    for name, parties, rationale, key in SCENARIOS:
        rules, n = ARCHETYPES[key]
        r = placement(rules, n)
        rows.append({"name": name, "parties": parties, "rationale": rationale, "arch": key,
                     "n": n, "phi": r["max"], "norm": r["max"] / (n - 1) if n > 1 else r["max"]})

    band = Counter(round(x["phi"], 2) for x in rows)
    arch = Counter(x["arch"] for x in rows)
    dyadic = sum(1 for x in rows if x["phi"] <= 1e-9)

    print("=" * 84)
    print(f"PAPER 3 — {len(rows)} micro-coordination scenarios (surface variety vs structure)")
    print("=" * 84)
    print(f"  distinct surface activities : {len(rows)}")
    print(f"  distinct Φ values (bands)   : {len(band)}  -> {dict(sorted(band.items()))}")
    print(f"  dyadic (Φ=0)                : {dyadic}/{len(rows)} = {100*dyadic/len(rows):.0f}%")
    print(f"  archetype counts            : {dict(arch)}")

    # write the case-study-structured catalog
    out = os.path.join(_HERE, "MICRO_SCENARIOS.md")
    BANDLABEL = {0.0: "moderated dyad", 0.5: "parity", 0.83: "partial mediation",
                 2.0: "strict mediation", 3.0: "higher-order strict"}
    by_band = defaultdict(list)
    for x in rows:
        by_band[round(x["phi"], 2)].append(x)
    with open(out, "w") as fh:
        fh.write(f"# Paper 3 — {len(rows)} micro-coordination scenarios, in the case-study structure\n\n")
        fh.write("> Model-internal catalog. Each scenario is a real micro-activity, coded from its\n"
                 "> coordination mechanism (the rationale column) to a structural archetype BEFORE\n"
                 "> computing, then scored with exact IIT-4.0 Φ (`phi_core`). Reproduce with\n"
                 "> `micro_scenarios.py`. This is the micro-scale companion to the corporate cases\n"
                 "> (`cases.py`) and the dyadic controls (`dyadic_cases.py`).\n\n")
        fh.write("## The finding\n\n")
        fh.write(f"- **{len(rows)} surface-distinct activities** collapse onto **{len(band)} Φ values**: "
                 f"{', '.join(str(b) for b in sorted(band))}.\n")
        fh.write(f"- **{dyadic} of {len(rows)} ({100*dyadic/len(rows):.0f}%) are dyadic (Φ=0)** — the "
                 "instrument does not stamp everything triadic.\n")
        fh.write("- Activities group by **mechanism, not surface**: ordering lunch is dyadic through a "
                 "waiter (a conduit) and strict through DoorDash (a joint dispatch); the surface 'order "
                 "lunch' is the same, the structure is not.\n\n")
        fh.write("| Φ band | scenarios |\n|---|---|\n")
        for b in sorted(band):
            fh.write(f"| {b:.2f} ({BANDLABEL.get(b, '?')}) | {band[b]} |\n")
        fh.write("\n## The case structure (per scenario): bounded unit / coordinating parties / "
                 "mechanism / structural coding / Φ-verdict\n\n")
        for b in sorted(by_band):
            fh.write(f"\n### Φ = {b:.2f} — {BANDLABEL.get(b, '?')}"
                     + (f" (n=4 form; size-normalized Φ/(n−1) = {b/3:.2f}, the strict level)\n\n" if b == 3.0 else "\n\n"))
            fh.write("| # | micro-activity | coordinating parties | coordination mechanism (coded) | structure | Φ |\n")
            fh.write("|---|---|---|---|---|---|\n")
            for i, x in enumerate(by_band[b], 1):
                fh.write(f"| {i} | {x['name']} | {x['parties']} | {x['rationale']} | {x['arch']} | "
                         f"{x['phi']:.2f}{' (norm '+format(x['norm'],'.2f')+')' if x['n']>3 else ''} |\n")
        fh.write("\n## Honest bounds\n\n"
                 "- The Φ of each scenario follows from its **pre-registered structural coding**, not "
                 "from a per-scenario discovery; the catalog's claim is about the coding (surface "
                 "variety, structural sparsity), not about the world.\n"
                 "- Codings are contestable and sit at the boundaries the dyadic controls exposed: a "
                 "peer payment is coded PARTIAL (the processor authorizes jointly), a GitHub PR PARTIAL "
                 "(direct discussion plus a merge gate); a reasonable analyst could re-code these, and "
                 "the band would move. Each rationale is the auditable coding decision.\n"
                 "- Magnitude is ordinal; the higher-order raw Φ is size-scaled (normalized in the "
                 "table).\n")
    print(f"\n  wrote {out}")


if __name__ == "__main__":
    main()

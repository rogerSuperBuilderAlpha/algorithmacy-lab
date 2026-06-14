# Field demo — what the ten mock organizations show

Ten invented coordination arrangements, encoded as Boolean forms and classified by exact Φ. Six read
triadic, four read dyadic; nine matched the reading fixed before computing. The rules are stipulated,
so nothing here measures a real organization. The point is to show the protocol working and to
surface the judgment calls a real study will face. Reproduce with `python -m org_frontier.field.run`;
full table in `results/field_mocks.csv`.

## A system in the middle is not enough

Four of the ten put a platform, manager, record, or IT system between two parties and still read
dyadic. The relay manager (M2) forwards one worker's report to another and commits nothing. The
marketplace (M3) fills a buyer from whichever seller is free. The passive EHR (M5) stores what one
nurse writes for the next to read. The ERP link (M10) transmits a purchase order and logs it. In
each, the major complex is a coupled pair and the nominal system sits outside it, a conduit or a
spectator. Algorithmacy is not "there is a platform." It is a platform that commits a determination
neither party sets alone, with both parties wired into and reading that determination. The four
dyadic mocks fail that test; the ride-hail dispatch (M1), the CI gate (M4), the ranking (M7), the
arbitration (M9) pass it.

## The verdict turns on the encoding, and the demo shows where

Four arrangements flip verdict under a second encoding the same story permits.

- **Substitutability (M1).** One driver matched to one rider is triadic. Drivers drawn as an
  interchangeable pool make the platform read an OR, no driver is pivotal, and the form factors to
  dyadic. The worker dissolves into the pool.
- **Commit versus forward (M2).** A manager who forwards is dyadic; a manager who commits a decision
  needing both reports is triadic. The same role, two readings, opposite verdicts.
- **Specialized versus substitutable (M3).** A buyer who needs a particular seller turns the dyadic
  marketplace triadic. Substitutability, not the platform, was carrying the dyadic verdict.
- **Gate versus store (M5).** An EHR that enforces a handoff checklist both nurses must complete is
  triadic; one that only stores is dyadic.

These flips are the central caution. A field verdict is a property of the model first, and the
arrangement only through the model. The sensitivity step in the protocol is where that is made
visible, and it is not optional: every one of these four would be a different headline depending on
a single rule a hurried study could fix either way.

## Compute, do not assert

The support-ticket triage (M8) was pre-registered dyadic — a customer opens a ticket, it routes to
an agent, the agent replies, apparently a pass-through. The computed verdict is triadic. The routing
closes a cycle, and a cycle is irreducible (the same rotation result the oscillatory-scaling work
found on rings). The naive reading was wrong, and the instrument caught it. This is the case for
computing the verdict rather than eyeballing the org chart: the structure that carries irreducibility
is not always the structure that looks like coordination.

## A triadic verdict still needs the complex to name who binds

Two triadic mocks have a core that excludes the party the story centers on. The CI gate (M4) reads
triadic, but its irreducible core is author–maintainer; the automated gate, as encoded, is a conduit
between them. The franchise (M6) reads triadic, but its core is franchisee–standard, with the
customer a downstream conduit. Whole-system Φ says the arrangement is irreducible; only the major
complex says which parties do the binding, and it is not always the ones the name suggests. A field
study that reports a verdict without the complex has reported half the result.

## What this demo does not establish

The rules are stipulated, not elicited. No real handoff, dispatch, or grievance was observed; the
numbers are exact for the models and say nothing about any organization. The node states are binary,
where real coordination is often graded. The arrangement boundaries were chosen for clean exposition.
The point of the exercise is the procedure and the four kinds of judgment it forces — system-versus-
conduit, substitutability, gate-versus-store, and reading the complex — not the verdicts themselves.

## What real fieldwork will break, and build

Running this on a real organization will expose what the mocks cannot. Rule elicitation has no method
yet: no interview protocol for "what determines this action," no way to score agreement between
analysts, no procedure for parties who describe the same arrangement differently. Binary states will
strain against graded ones. The boundary choice will turn out to matter in cases the mocks made look
obvious. Each failure is the next piece of a field-tested protocol. The mocks are a template to carry
into the field and expect to revise, and the revisions are the research.

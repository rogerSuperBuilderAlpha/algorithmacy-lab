# Hub floor uniqueness — claims (fixed before arguing)

**Question (RESEARCH_AGENDA_50_V2 #48).** Is the conjunctive hub the
unique form achieving its Φ at the 2(n−1) edge floor, or are there
others (#30, #116)?

**Already known (cited, not reopened).**
- Probe #30: every triadic strict-mediation n=3 form has exactly 4
  edges; Φ ∈ {2.0, 0.5}.
- Probe #116: AND-all and OR-all hubs both achieve Φ = n−1 at the
  2(n−1) edge floor through n=6–7.
- Q45 (`q45_edge_floor_uniqueness`, #145–#149): at n=3 the AND commit
  is **not** unique for Φ = 2 at the floor (16 monotone forms; only 2
  AND); parity saturates Φ = 0.5 on the same floor.
- #47 / #49: AND-hub closed form Φ = n−1 with MIP = H/H′.

Stoch–temporal / estimation / construct / omit closed.

## Instrument (fixed)

Exact IIT-4.0 major-complex Φ; edge count = `#` of 1s in
`cm_from_rules`. Floor = 2(n−1). Target law value Φ★ = n−1.
In-silico Boolean forms only.

## Scopes

1. **Strict-mediation family (n=3).** Q45 population (cited +
   reproduced).
2. **Hub topology.** Fixed wiring: S′ = f(parties), X_i′ = S for all
   parties. Edge floor automatic when f depends on every party.
   Enumerate all f : {0,1}^{n−1} → {0,1} at feasible n.

## Claims

### U0 — floor universality (n=3 mediation)

Every triadic strict-mediation form at n=3 has exactly 4 edges.
(Cite #30 / Q45 H1; reproduce.)

### U1 — AND not unique for Φ★ at the floor (mediation)

Among triadic strict-mediation forms at 4 edges with Φ = 2, some use
non-AND commits. (Q45 H2 refuted; reproduce count.)

### U2 — De Morgan dual orbit on the hub

On hub topology, AND / OR / NAND / NOR each achieve Φ = n−1 with
full core and exactly 2(n−1) edges, for every checked n ≥ 3.

### U3 — hub-topology class is exactly the dual orbit

At n=3 and n=4, among all 2^{2^{n−1}} hub commits, exactly the four
functions {AND, OR, NAND, NOR} achieve Φ = n−1 with full core. No
others.

### U4 — uniqueness verdict

The conjunctive (AND) hub is **not** the unique form achieving Φ★ at
the 2(n−1) edge floor. The minimal complete answer on the hub wiring
is the four-element De Morgan orbit; off that wiring, Q45 supplies
many more n=3 counterexamples.

## Status targets

U0–U4: proved / confirmed / partial / refuted (for uniqueness).
Overall: **unique** / **not-unique** / **partial**.

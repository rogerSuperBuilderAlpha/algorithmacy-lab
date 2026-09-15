# Ostrom — Stage 3 hypotheses (fixed before computing)

## The rendering that all five share

An **appropriator** i has a compliance bit c_i (1 = follows the rules) and, where sanctions are modeled, a
sanction bit s_i (1 = sanctions). **Contingent self-commitment** (O2): c_i complies when the other
appropriators comply. **Monitoring by the monitored** (O1): s_i sanctions when either other appropriator
defects, and c_i also complies when jointly sanctioned by the other two — the Coleman paper's "yields only
to a joint sanction," now with every party on both sides. The **structure** is the major complex; **value
added** V and **positional advantage** are the Coleman paper's quantities (a deleted variable reads 0). The
**Coleman contrast** is that paper's norm_closed form (A' = B ∧ C; B' = ¬A ∨ C; C' = ¬A ∨ B), in which A is
sanctioned and never sanctions.

Forms (rules in `methods.md`): **mutual** (six nodes: c1..c3, s1..s3); **coleman_closed**; **leviathan**,
**private**, **self** (H2); **nested** and **unnested** (H3); **bounded** and **breached** (H5).

## H1 — The monitored are in the structure (O1; against Coleman H1)

- **H1 (Ostrom).** In mutual, the major complex contains every appropriator's compliance node c_1, c_2, c_3;
  in coleman_closed it does not contain A.
- **H0.** Some c_i outside the core of mutual.
- **Lab prior.** Open. The Coleman finding was that the sanctioned party leaves the complex; whether making
  every party both sanctioner and sanctioned keeps them all in is not known.

## H2 — Self-governance against Leviathan and privatization (O4)

- **H2 (Ostrom).** self has a core of all three appropriators at Φ higher than leviathan's core Φ; in
  leviathan the enforcer L has positive positional advantage; private has no complex.
- **H0.** leviathan's core Φ ≥ self's, or L has no advantage, or private binds.
- **Lab prior.** With on private (no ties, no complex); open on the ordering.

## H3 — Nested enterprises (O5; against Coleman H3)

- **H3 (Ostrom).** In nested the major complex contains all seven (both groups and the federation), and each
  local triad {a1, a2, a3}, {b1, b2, b3} is irreducible as a subsystem (Φ > 0 at the reachable state where
  the whole is maximal); in unnested the two triads are separate complexes.
- **H0.** The upper layer is the core and a group falls out (the Coleman parents pattern), or a local triad
  is reducible inside the nest.
- **Lab prior.** Open.

## H4 — Quasi-voluntary compliance (O3; against Coleman H1's fixed point)

- **H4 (Ostrom).** In mutual the all-comply, no-sanction state (c = 111, s = 000) is a fixed point; every
  state with exactly one defector and no sanctions standing returns to it; and coleman_closed's compliance
  fixed point has the sanction standing (B = C = 1).
- **H0.** No sanction-free fixed point, or a single defection does not return to it.
- **Lab prior.** With (traced by hand: a single defection returns in five steps).

## H5 — Boundaries (O6)

- **H5 (Ostrom).** bounded (an outsider O reads the commons and is not read) has the same core and core Φ as
  self, with V(O) = 0; breached (a member's compliance depends on O) has a different core or a lower core Φ.
- **H0.** The outsider enters the core or changes Φ in bounded, or breaching changes nothing.
- **Lab prior.** With on bounded (Serres H1: the one-way arrow binds nothing); open on breached.

## Not tested here

Graduated sanctions; congruence; collective choice; conflict resolution; the chapter-1 games.

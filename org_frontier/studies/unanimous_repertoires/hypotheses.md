# Why the unanimous-state Φ is the same whoever errs: a cause/effect test

Fixed before this study's computation.

## Gap

`placement_equality` (the post "The unanimous moment") found that, for the extreme rules, whole-group
Φ matches under mediator-side and party-side noise up to r = 0.2, and that the match lives in one
state: the unanimous default (0000 for any-yes; 1111 for all-yes). It did not say why that state's Φ
is the same, or which part of the IIT 4.0 calculation changes at r = 0.4, when the match breaks.
Item 1 of `placement_equality/BACKLOG.md` asks for that comparison.

This study inspects the system-level cause and effect analyses that PyPhi's IIT 4.0 SIA already
computes for that state, at r = 0.2 and r = 0.4, under both placements, for OR3 at 0000 and for
1-of-4 at 00000.

## What is being compared

PyPhi pin `b78d0e342`. For a subsystem, `new_big_phi.sia` returns a system irreducibility analysis
whose Φ is the minimum of a cause value and an effect value on the minimum information partition
(see `evaluate_partition` in PyPhi: φ = min(cause.φ, effect.φ)). Each of those two values comes
with a repertoire (a distribution over the system's states in that direction), a partitioned
repertoire, a partition, and a purview. This study records those objects; it does not invent a
new Φ measure.

The two placements and the TPM construction are the same as in `placement_equality`.

## Values already seen (disclosed)

Committed full-group φ at the unanimous default state, from `placement_equality/results/results.json`.
These are raw PyPhi values, including a negative one. Whole-group Φ in that study was the maximum
over reachable states, so a negative value at 0000 was not the published whole Φ.

OR3 at 0000:

- r = 0.2, mediator: 1.0415184462530138; party: 1.041518446253012.
- r = 0.4, mediator: −0.1242086202819146; party: 0.1704462949802986.

1-of-4 at 00000:

- r = 0.2, mediator: 1.110953009336554; party: 1.1109530093365452.
- r = 0.4, mediator: −0.09325477255320004; party: 0.13635703598423843.

The earlier findings text described the r = 0.4 mediator value at the unanimous state as dropping
"to 0." The stored raw value is negative, as above. This study uses the raw values.

From the already-published TPM construction, at OR3 0000 under mediator-only noise,
P(S next = 1) = 1 − (1 − r)^3, which is 0.488 at r = 0.2 and 0.784 at r = 0.4. Under party-only
noise, S stays 0 and each party turns on with probability r. Those forward distributions differ
at both rates. The equality at r = 0.2 is therefore not a claim that the next-state row is the
same.

## Outcomes

A cause or effect analysis *matches* across placements if the φ values agree to 1e-6, the
partitions are the same (same parts), the purviews are the same, and the repertoire arrays agree
to absolute error 1e-10.

- H1: at r = 0.2, for OR3 at 0000, the two placements match on both the cause analysis and the
  effect analysis. In particular, cause.φ is the same, effect.φ is the same, and both repertoire
  arrays match. The already-known equality of system φ (1.041518) is then the same minimum of the
  same two numbers, not a coincidence of two different pairs that share a min.

- H2: at r = 0.4, for OR3 at 0000, the placements diverge because the effect analysis changes on
  the mediator side. Concretely: under mediator-only noise, effect.φ is strictly less than cause.φ,
  and effect.φ equals the already-stored system φ −0.1242086202819146 (so the system value is the
  effect value). Under party-only noise, both cause.φ and effect.φ are positive, and the system
  value 0.1704462949802986 is their minimum.

- H3: the same pattern holds for 1-of-4 at 00000. At r = 0.2 the two placements match on both
  cause and effect analyses (system φ 1.110953). At r = 0.4, mediator effect.φ is strictly less
  than cause.φ and equals the already-stored system φ −0.09325477255320004; party-side cause.φ and
  effect.φ are both positive, and their minimum is 0.13635703598423843.

Controls, required to 1e-6 before scoring: the four OR3 and four 1-of-4 system-φ values listed
above, recomputed in this run, must match the stored numbers.

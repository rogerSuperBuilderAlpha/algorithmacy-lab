# q177 findings — an idle spectator sinks whole-system Φ but leaves the major complex untouched

Both hypotheses hold on synthetic data. A party who reads nobody and whom nobody reads drives
whole-system Φ to zero, because the spectator factors off and the system stops integrating as a
whole. The major complex ignores it: in every triadic-core account the maximal complex after
injection is the original (W,S,C) at the original Φ. Reading the verdict off the complex makes it
immune to the spectator; reading it off the whole system does not.

| quantity | value |
|---|---|
| (account, spectator) pairs | 48 |
| triadic-core accounts (over pairs) | 32 |
| core stable: original (W,S,C) at same Φ | 32/32 = 1.000 |
| whole-system structural verdict flips | 32/48 = 0.667 |
| core-aware verdict flips | 0/48 = 0.000 |

| H | result |
|---|---|
| H1 (idle spectator leaves the triadic core intact in >95%) | SUPPORTED (1.000) |
| H2 (core-aware verdict agrees 100%; whole-system disagrees >50%) | SUPPORTED (core 0.000; whole 0.667) |

## Reading

Whole-system Φ is fragile to bystanders. Every account that read triadic at baseline reads dyadic
once the idle spectator is attached: the whole system no longer integrates, so the classifier
factors it and calls it literacy. That is the wrong call about the coordination. The mediated triad
is still there; a logged-but-disconnected seat sits beside it.

The major complex makes the right call. PyPhi's maximal_complex finds the largest irreducible
subsystem, and the idle spectator is never part of it. Across all 32 triadic-core pairs the complex
is the original (W,S,C) at the original Φ — 2.0 for the AND/OR/NAND/NOR cores, 0.5 for the weak
XOR/XNOR cores. The dyadic-base accounts behave the same way: their two-party complex (e.g. {S,C})
also survives the spectator. The core-aware verdict never flips; the whole-system verdict flips on
two-thirds of pairs, every flip a triadic core misread as dyadic.

The controls fix what "idle" means. A party wired into the core (X reads S, S reads X) enters the
complex: the maximal complex becomes (W,S,C,X). A self-loop node reads only itself and carries its
own irreducible self-Φ of 1.0; on a weak core (Φ = 0.5) that self-Φ would capture the complex as
{X}. So "spectator" is restricted to nodes that read nobody. A node that reads something — even
only itself — is a participant.

## Limitation

Synthetic coded forms, exact Φ on n = 3 and n = 4. The result is a property of the encoded rules,
not a measurement. It shows that a coding choice — whether to read the verdict off the whole system
or off the major complex — decides whether an inert bystander erases the coordination. Reading the
complex is the robust choice. The Φ-to-construct bridge for real accounts is still open.

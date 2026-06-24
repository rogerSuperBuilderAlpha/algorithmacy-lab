# q177 methods

## Machinery

Reused, not reimplemented:

- `org_frontier.field.rule_to_phi.rule_to_phi` — the bridge from study 1 of the field line. It
  encodes per-party Boolean determination rules into a deterministic state-by-node TPM and reads
  the whole-system exact-Φ verdict over the MIP.
- `org_frontier.probes.lib.verdict` — the whole-system classifier verdict.
- `org_frontier.probes.lib.major_complex` — the maximal irreducible complex (PyPhi
  `maximal_complex`) and its Φ, taken as the max over reachable states.

## Synthetic accounts

A coded account is a three-party coordination form over (W, S, C). The mediator S binds the worker
W and counterpart C through a two-input Boolean gate; W and C each read S, directly or negated.
Six gates (AND, OR, XOR, NAND, NOR, XNOR) crossed with four feedback signs (W-id/not by C-id/not)
give 24 accounts. Sixteen carry a triadic (W,S,C) core; the eight feedback-mismatched forms are
already dyadic at baseline, their major complex a two-party block.

## Spectator injection

A genuinely idle spectator X is a fourth node whose rule reads nobody — constant 0 or constant 1 —
and whom no other rule reads. Each account is run with each idle spectator, giving 48
(account, spectator) pairs. For every pair the probe records the whole-system verdict and the major
complex, with and without the spectator.

## Metrics

- H1 (core stability): over triadic-core accounts, the fraction whose major complex after injection
  is the original (W,S,C) at the same Φ.
- H2 (verdict agreement): over all pairs, the fraction where the core-aware verdict (irreducible
  core present) flips versus the no-spectator baseline, and the fraction where the whole-system
  structural verdict flips.

## Controls

The instrument control validates four cases before the sweep:

1. The faithful triad reads triadic at max Φ_MIP = 2.0 (whole-system equals core).
2. An idle spectator on that triad sinks whole-system Φ to 0 while the major complex stays
   (W,S,C) at 2.0.
3. A wired-in active party (X reads S, S reads X) enters the core: the major complex becomes
   (W,S,C,X). This distinguishes a participant from a spectator.
4. A self-loop node (reads only itself) is not idle: it carries its own irreducible self-Φ. On the
   strong AND core it does not displace the complex; on the weak XOR/XNOR cores (Φ = 0.5) its
   self-Φ of 1.0 would pull the complex to {X}, which is why the spectator population is restricted
   to nodes that read nobody.

## Determinism

The sweep is exhaustive over a fixed account list, so the output is deterministic. An RNG is seeded
(`numpy.random.default_rng(0)`) for form. Three runs produce byte-identical output.

## Scope

Synthetic coded data only. Exact Φ on small forms (n = 3 and n = 4). The whole-system-to-zero
result and the core-stability result are properties of the encoded rules, not measurements of any
coordination in the field.

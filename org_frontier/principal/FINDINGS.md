# Findings — the corporate principal

Paper 1 of the dissertation argues platforms are corporate-authored: the mediator has a corporate
principal whose objectives neither party controls. Does that principal belong to the irreducible
coordination, or sit outside it? From `results/principal.csv`, exact IIT-4.0 Φ via PyPhi, on the
IIT-4.0 venv.

The right object is the **major complex** — the maximally irreducible subset of nodes
(`new_big_phi.maximal_complex`) — not whole-system Φ. Whole-system Φ over the MIP is sensitive to
spectators: an idle principal makes the *whole* four-node system factor (Φ = 0) even though the
W–S–C triad inside it is irreducible. The complex sees through that.

## Result

Baseline: the bare W–S–C triad (S' = W ∧ C, each end tracks S) is irreducible on its own, Φ = 2.0.

| Form | principal's coupling | whole-system Φ | major complex | P in core? |
|---|---|---|---|---|
| passive_principal | owns S, static | 0.0 | {W, S, C} (Φ 2.0) | no |
| extractive_monitor | reads S only (downstream) | 0.0 | {W, S, C} (Φ 2.0) | no |
| gates_static_P | feeds S only (upstream), static | 0.0 | {W, S, C} (Φ 2.0) | no |
| gates_and_monitors | reads S **and** feeds S (bidirectional) | 3.0 | {W, S, C, P} (Φ 3.0) | **yes** |

## Reading

**Ownership is not constitutive; bidirectional participation is.** The principal joins the
irreducible coordination core only when it both shapes the determination (S reads P) and responds to
its outcome (P reads S). A principal who merely owns the system, only gates it, or only monitors it
stays outside the core — the irreducible coordination remains the worker–system–counterpart triad,
Φ = 2.0, unchanged.

This refines the algorithmacy thesis. The relevant fact about a platform's corporate principal is
not that it owns or authors the system, but whether it is dynamically in the loop — both setting the
rule and reacting to results. A hands-off owner is, structurally, a spectator on the coordination it
profits from. A principal that gates and monitors fuses into a single four-party irreducible whole.

**Methodological note.** In three of four forms the whole-system Φ is 0 while the major complex
{W, S, C} holds at Φ = 2.0. Reading whole-system Φ alone would wrongly call these "dyadic." The
verdict for a form with possible spectator nodes must be read on the major complex, not the whole
system — a refinement the other org_frontier experiments (all minimal, no spectators) did not need.

## Caveats

- Four hand-built forms, defensibly coupled (no target Φ), illustrating the mechanism; not a
  population. A population sweep over principal-coupling patterns is the natural extension.
- Binary/structural reading only; cross-node Φ magnitudes (2.0 vs 3.0) are not comparable.

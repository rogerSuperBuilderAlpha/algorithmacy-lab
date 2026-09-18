# Coordination lattice — claims (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #50).** Does the verdict, with Φ
magnitude, induce a partial order on coordination forms — a lattice of
coordination kinds — and what are its extremes?

**Already known (cited, not reopened).**
- #47–#49: closed forms and MIP identity for hub/pool/parity; hub
  floor NOT_UNIQUE (#48 dual orbit).
- #132 zoo; #11 rot_ring; #30 extremes; Q45 floor.
- Stoch–temporal / estimation / construct / omit closed.

## Instrument (fixed)

Exact IIT-4.0 major-complex Φ (0 if no irreducible complex).
Verdict = classifier `structure` (`dyadic` / `triadic`).
In-silico Boolean catalog only.

## Primary order (fixed)

On forms of a **fixed** n, define the kind-key
\[
\kappa(f)=\bigl(v(f),\,\Phi(f)\bigr),
\quad v(f)=\mathbf{1}[f\text{ triadic}]\in\{0,1\}.
\]
**Order:** $f\preceq g$ iff $\kappa(f)\le_{\mathrm{lex}}\kappa(g)$
(verdict first, then Φ). This is a total preorder on forms.

**Kinds:** equivalence classes $[f]=\{g:\kappa(g)=\kappa(f)\}$
(Φ within $10^{-9}$).

**Poset of kinds** $(K,\preceq)$ is the quotient. A finite chain is a
lattice; join = max key, meet = min key.

**Alternatives noted, not primary:** (A) product order
$(n_{\mathrm{core}},\Phi)$; (B) enrichment / edge-addition. (A) is
stress-tested for lattice failures on the same catalog.

## Catalog (designed)

Per n ∈ {3,4}: zeros (bottom pole), conveyor, one_party, chain,
parity_hub, rot_ring, and_ring, AND/OR/NAND/NOR hubs, pool.

## Claims

### L1 — primary order is a lattice of kinds

$(K,\preceq)$ under lex(verdict, Φ) is a lattice (as a chain).

### L2 — extremes

⊥ = dyadic Φ = 0 (zeros). ⊤ = maximum-Φ triadic kind in the catalog
(pool; tied with and_ring at n=3).

### L3 — verdict dominates magnitude

Some dyadic form has Φ strictly above some triadic form’s Φ, yet ranks
strictly below it under ⪯ (verdict bit).

### L4 — product-order stress test

On the same kinds, the product order $(n_{\mathrm{core}},\Phi)$ is a
poset; report whether every pair has join and meet *inside the
catalog* (lattice vs mere poset).

## Status targets

L1–L4: confirmed / refuted / partial. Overall:
**LATTICE** / **POSET_NOT_LATTICE** / **FAILS**.

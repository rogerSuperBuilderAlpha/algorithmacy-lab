# Coordination lattice — findings

**Verdict: LATTICE.** Lex(verdict, Φ) quotients the zoo catalog to a
**chain lattice** of coordination kinds. Extremes: ⊥ = `zeros`
(dyadic Φ = 0); ⊤ = `pool` (Φ = n(n−1); tied with `and_ring` at n=3).
Verdict dominates magnitude (rich dyad ≺ lean triad). Product order
$(n_{\mathrm{core}},\Phi)$ on the same catalog is a poset but **not**
a lattice. Formal lane #47–#50 is **closable**.

In-silico; candid N (n=3,4 designed catalog). Hypotheses fixed in
`hypotheses.md`. Cited: #47–#49; #132; #11; #30. Stoch–temporal /
estimation / construct / omit closed.

## Status

| claim | status |
|---|---|
| L1 lex kinds = chain lattice | **CONFIRMED** |
| L2 extremes ⊥=zeros ⊤⊇pool | **CONFIRMED** |
| L3 verdict dominates Φ | **CONFIRMED** |
| L4 product-order lattice | **POSET_NOT_LATTICE** (stress) |

## Kinds (summary)

**n=3 chain:** zeros (0,0) ≺ conveyor (0,1) ≺ one_party (0,2) ≺
parity (1,0.5) ≺ {hub orbit, chain, rot_ring} (1,2) ≺
{pool, and_ring} (1,6).

**n=4 chain:** zeros (0,0) ≺ conveyor (0,1) ≺ one_party (0,2) ≺
parity (1,0.25) ≺ {chain, rot_ring} (1,2) ≺ hub orbit (1,3) ≺
and_ring (1,4) ≺ pool (1,12).

## Reading

Verdict + Φ do induce a lattice of kinds once kinds are κ-classes:
the lattice is the chain of distinct (verdict, Φ) levels in the zoo.
Its bottom is total factoring; its top is the all-required pool (the
#47/#49 closed form). A two-party complex with Φ = 2 sits *below*
parity’s Φ = 0.5 triad — the construct’s cut is the verdict bit, not
the scalar. Enrichment and core-size×Φ are the wrong lattices for this
question.

## Limits

Designed catalog (not all Boolean forms); fixed n slices; product
stress uses max n_core per kind. No organization measured.

## Best next

**Formal lane closable.** Prefer empirical / survey packets, or new
agenda items outside #47–#50. Do not reopen estimation / construct /
omit / stoch–temporal.

## Reproduce

```
python org_frontier/studies/coordination_lattice/analyze_lattice.py
```
(~15 s)

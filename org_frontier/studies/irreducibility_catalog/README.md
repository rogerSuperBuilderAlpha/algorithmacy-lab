# Irreducibility catalog — necessary and contingent irreducible triads

A growing reference of real coordination arrangements, each a mediating third party, sorted by why the
mediator is in the irreducible core. The dichotomy comes from q213:

- **necessary** (the classifier's "intrinsic") — the mediator integrates; it survives the bypass. A
  clearinghouse, an interpreter, a court.
- **contingent** — a conduit held in the core only because a constraint forbids the bypass; it dissolves when
  the forbidden edge is restored. A car dealer, a liquor distributor, a notary.
- **partial** — part role, part constraint; the mediator stays but the system sheds integration.
- **reducible** — a free conduit, already out of the core.

Each entry is modeled as a small Boolean form and classified by the bypass-counterfactual
(`org_frontier/classifier/contingency.py`). `catalog_entries.py` holds the entries and their predicted class;
`build_catalog.py` classifies them all and asserts each matches; `CATALOG.md` is the rendered catalog with the
real-world reading for each.

## Run

```
python org_frontier/studies/irreducibility_catalog/build_catalog.py
```

## Adding an entry

Append a dict to `ENTRIES` in `catalog_entries.py`: the real parties, the constraint, the bypass it forbids, a
structural `template` (relay / conjunctive / additive / free), and the `expected` class. Run the builder; if
the model classifies as predicted it joins the catalog, and the reproduce check holds it there. A real
arrangement that does not fit the four templates is the signal to add a fifth.

## What the first batch shows

Diverse constraints — franchise law, a three-tier statute, a license, a recording requirement — collapse to
one structural signature, a mandated relay, and all read contingent. Integrating mediators read necessary
regardless of domain. The same role can sit in either column by design: a title company that only records is
contingent, an escrow agent that conditions release on both sides is necessary. See `FINDINGS.md`.

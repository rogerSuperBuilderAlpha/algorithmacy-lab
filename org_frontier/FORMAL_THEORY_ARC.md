# Formal theory arc — #47–#50 working picture

Short spine for the formal lane on `RESEARCH_AGENDA_50_V2` (PR #739).
Exact binary IIT-4.0 Φ; in-silico. Stoch–temporal / estimation /
construct / omit stay closed except as empirical pointers to the laws.

## #47 status

[`studies/scaling_laws_closed_form/`](studies/scaling_laws_closed_form/)
→ cut formulas proved; MIP identity closed by #49 for pool/hub;
parity residual on $I=1$ uniqueness for general $n$.

## #49 status

[`studies/mincut_mip/`](studies/mincut_mip/) → **NORMALIZED_CUT**
(graph min-cut REFUTED; pool/hub MIP proved; parity partial).

## #48 status

[`studies/hub_floor_uniqueness/`](studies/hub_floor_uniqueness/)
→ **NOT_UNIQUE** (De Morgan orbit {AND, OR, NAND, NOR} on hub wiring;
Q45 mediation counterexamples).

## #50 status

[`studies/coordination_lattice/`](studies/coordination_lattice/)
→ **LATTICE**

Lex(verdict, Φ) quotients the zoo catalog to a **chain lattice** of
kinds. ⊥ = `zeros` (dyadic Φ = 0); ⊤ = `pool` (tied `and_ring` at
n=3). Verdict dominates magnitude. Product $(n_{\mathrm{core}},\Phi)$
is not a catalog lattice.

## Lane verdict

**Formal lane closable.** #47–#50 done. Prefer empirical / survey
packets next. Do not reopen estimation / construct / omit /
stoch–temporal.

## Reproduce

```
python org_frontier/studies/scaling_laws_closed_form/verify_laws.py
python org_frontier/studies/mincut_mip/verify_mip.py
python org_frontier/studies/hub_floor_uniqueness/verify_uniqueness.py
python org_frontier/studies/coordination_lattice/analyze_lattice.py
```

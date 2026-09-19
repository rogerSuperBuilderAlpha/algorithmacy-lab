# parity_law_n_gt8 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #9).** Does V3 #10’s parity-hub law
Φ = 2^(2−n) (`LAW_HOLDS_NGT6`) remain exact for **n>8** hub embeddings —
via the named H-cut formula and/or feasible exact checks — or do
topology residuals appear?

**Already known (cited, not reopened).**
- V2 #47 `scaling_laws_closed_form`: H-cut selectivity proved
  φ_s = 2^(2−n) for all n; exact Φ smoke n≤5.
- V2 #49 `mincut_mip`: MIP = H for parity with I=1 uniqueness only
  through n≤5 (partial).
- V3 #10 `parity_law_n_gt6`: **LAW_HOLDS_NGT6** — exact major-complex
  Φ = law at n∈{6,7} with full cores; H is MIP and matches exact.

**Gap.** Past n=7, major-complex enumeration becomes costly. V4 #9 asks
whether the law still holds for n>8 under the H-cut / SIA regime, or
whether a residual appears (H not MIP, or φ ≠ law).

**Universe.** Binary IIT-4.0. `parity_hub(n)`: S′=⊕ parties; party′=S.
All-1s evaluation. Controls n∈{3..7} from V3 #10 census. New: n∈{8,9,10}
named H-cut φ; n=8 full SIA (MIP identity). Major-complex recompute at
n≥8 is out of lean scope (document cut/SIA regime).

## Law

Φ_law(n) = 2^(2−n).

## H1 — controls reproduce LAW_HOLDS_NGT6

V3 #10 census: exact Φ = law, full core, H MIP for n∈{3..7}. Null: any
control fails.

## H2 — named H-cut φ equals law at n>8

For every n∈{8,9,10}, evaluate_partition on the hub-preserving atomic
cut H yields φ = 2^(2−n). Null: some n misses the law.

## H3 — H remains MIP at n=8 (feasible exact check)

Full SIA at all-1s for n=8 returns H as the MIP with φ = law. Null: H
not MIP or φ diverges (topology residual).

## H4 — no residual in the checked window

H1 ∧ H2 ∧ H3. Null: any fails.

## Reading keys

- **LAW_HOLDS_NGT8:** H1 ∧ H2 ∧ H3 — law survives n>8; H-cut exact;
  MIP identity holds at n=8; no residual in the lean window.
- **CUT_HOLDS_MIP_BREAKS:** H1 ∧ H2 ∧ ¬H3 — cut formula tracks law but
  H is not MIP at n=8 (residual).
- **LAW_BREAKS_NGT8:** H1 ∧ ¬H2 — H-cut φ leaves the law at some n>8.
- **CONTROLS_FAIL:** ¬H1.

# parity_law_n_gt6 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #10).** Does the parity Φ = 2^(2−n) law
(V2 #47/#115) remain exact under **n>6 hub embeddings**, or do topology
residuals appear once exact enumeration is replaced by cut formulas
alone?

**Already known (cited, not reopened).**
- Probe #115: parity (XOR) hub Φ decays as 2^(2−n) on the zoo reading
  at small n.
- #47 `scaling_laws_closed_form`: cut selectivity sel_c = 2^(2−n)
  proved; exact Φ smoke holds for n∈{3,4,5}; MIP identity partial.
- #49 `mincut_mip`: parity MIP = H with I=1 uniqueness exhausted only
  for n≤5; I≥2 dominated for all n.
- Conjunctive hub Φ=n−1 and pool Φ=n(n−1) closed for all n (#47+#49).

**Gap.** Exact Φ and named-cut identity are verified only through n=5
(plus informal zoo notes). V3 #10 asks whether the law survives **exact**
Φ at n>6, and whether the **H-cut formula alone** still matches the MIP
(or a residual appears when enumeration is skipped).

**Universe.** Binary exact IIT-4.0. `parity_hub(n)`: S′=⊕ parties; each
party ′=S. Evaluation at all-1s major complex. n ∈ {3,4,5} (controls) ∪
{6,7} (new; n=8 only if budget allows).

## Law

Φ_law(n) = 2^(2−n). Full core of size n.

## H1 — controls reproduce

Exact major-complex Φ(`parity_hub(n)`) = 2^(2−n) for n∈{3,4,5}, full
core. Null: any control fails.

## H2 — exact law at n>6

Exact major-complex Φ = 2^(2−n) with full core for every new n∈{6,7}
(and n=8 if run). Null: some n>6 cell misses the law or drops core.

## H3 — cut formula matches exact Φ (no residual)

At each new n>6, the named hub-preserving atomic cut H evaluates to
φ = 2^(2−n) and is a MIP winner (or tied winner). Null: H-cut φ differs
from exact Φ, or MIP leaves H (topology residual under cut-only use).

## H4 — panel verdict

- H1 ∧ H2 ∧ H3 → `LAW_HOLDS_NGT6`
- H1 ∧ H2 ∧ ¬H3 → `CUT_RESIDUAL`
- H1 ∧ ¬H2 → `LAW_BREAKS_NGT6`
- else → `CONTROLS_FAIL`

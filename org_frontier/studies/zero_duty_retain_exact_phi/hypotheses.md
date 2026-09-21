# zero_duty_retain_exact_phi — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #3).** Under exact Φ, does **zero-duty
on a party** cliff while an induced **party–mediator retain** path
still ranks — clarifying whether the cliff is specifically missing
party–party joints vs any missing node?

**Already known (cited, not reopened).**
- V4 #1 `TRANSFER_PARTIAL_EXACT_PHI`: exact-Φ alt cliffs on multifamily
  (1.000→0.660); soft on family_n3; zero-duty on family_n3 dropped
  1.000→0.792 (cliff by drop).
- V4 #2 `PHASE_RESTORES_JOINT`: at matched δ=0.5, phase holds where
  alt cliffs — joint observation, not mean duty.
- V3 #16 / V2 #24: MI zero-duty / hide-party cliffs. Construct/omit
  closed.

**Universe.** Exact binary IIT-4.0 via `classify_rules`. Panels as in
V4 #1/#2: family_n3 and multifamily (hub/chain/pool/…). Roles (A, M, B)
as before.

**Screens (labels = full-form triadic).**
1. **phi_full** — Φ(full).
2. **phi_zero_duty_B** — Φ(V∖{B}) with B frozen out (induced on all
   remaining nodes).
3. **phi_retain_MA** — Φ({M,A}) only (party–mediator retain path when
   B is absent).
4. **phi_omit_M** — Φ(V∖{M}) (missing-mediator control: any critical
   node?).
5. **phi_alt** — mean Φ({M,A}), Φ({M,B}) (V4 #1/#2 joint-loss screen;
   pointer).

On n=3, V∖{B} = {M,A}, so zero_duty_B ≡ retain_MA by construction
(design note; report fraction identical).

**Bars.** Hold: AUC ≥ **0.85** or within **0.10** of full. Cliff: AUC
< **0.70** or drop from full ≥ **0.20**.

## H1 — zero-duty cliffs on multifamily

`phi_zero_duty_B` meets the cliff bar on multifamily. Null: softens.

## H2 — retain_MA holds on multifamily

`phi_retain_MA` meets the hold bar on multifamily. Null: fails hold
(soft or cliff).

## H3 — zero-duty cliffs on family_n3

`phi_zero_duty_B` meets the cliff bar on family_n3. Null: softens.

## H4 — omit-mediator cliffs on multifamily

`phi_omit_M` meets the cliff bar on multifamily. Null: softens.

## H5 — full holds; n=3 identity check

`phi_full` holds on both panels; on family_n3, zero_duty_B equals
retain_MA on every form. Null: either fails.

## Reading keys

- **RETAIN_SAVES_ZERO_DUTY:** H1 ∧ H2 — zero-duty cliffs but retain
  still ranks (cliff ≠ any missing party path).
- **RETAIN_FAILS_WITH_ZERO:** H1 ∧ ¬H2 — zero-duty cliffs and retain
  also fails to hold (no escape via party–mediator pair alone).
- **ZERO_DUTY_SOFT:** ¬H1 — zero-duty does not cliff under exact Φ.
- **CONTROLS_FAIL:** ¬H5.

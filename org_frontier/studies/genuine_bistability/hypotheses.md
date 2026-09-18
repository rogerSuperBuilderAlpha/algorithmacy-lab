# genuine_bistability — hypotheses (fixed before computing)

**Question (agenda #13).** Is there a coupling regime with genuine
bistability — a triadic and a dyadic attractor coexisting — beyond the
hysteresis a sticky mediator showed (#109)?

**Already known (cited, not reopened).**
- Probe #43: sticky mediator S′=(W∧C)∨S collapses whole-form verdict
  to dyadic with self-absorbed core {S}; xor-memory stays triadic.
- Probe #109: sticky mediator produces an activity hysteresis loop
  under engagement drive ramp (area ≈0.071); memoryless ≈0.005. Path
  dependence of mean S-activity, not a Φ-verdict coexistence test.
- `correlated_output_noise/` (#5 CORE_SHIFT_NO_FLIP) — pointer only.
- Temporal lane #6–#11 — pointers only. Estimation / construct /
  omit / ladder closed.

**What counts as genuine bistability (fixed).** Under one fixed
deterministic coupling (one TPM), the synchronous Boolean map has at
least two attractors (fixed points or limit cycles), and among them
at least one attractor is **triadic** (max Φ_MIP over its states >
PHI_EPS) and at least one is **dyadic** (max Φ_MIP ≤ PHI_EPS). Both
must have nonempty basins in the 2^n state space. Exact binary
IIT-4.0 Φ evaluated at attractor states (not a drive-ramp activity
curve).

**What does not count.**
- #109-style hysteresis alone: path-dependent mean activity under a
  slow parameter ramp, without a triadic↔dyadic attractor pair at
  fixed coupling.
- Whole-form classifier max-Φ (the lab's usual verdict) collapsing
  coexistence into a single label.

**Forms (designed panel; candid N).** All n=3, labels (W,S,C).

| id | rules (sketch) | role |
|---|---|---|
| memoryless | W′=S, S′=W∧C, C′=S | clean triad baseline |
| sticky | S′=(W∧C)∨S | #43/#109 sticky |
| xor_memory | S′=(W∧C)⊕S | #43 parity-memory |
| or_commit | S′=W∨C | disjunctive cousin |
| sticky_or | S′=(W∨C)∨S | sticky disjunctive |
| sticky_parity | S′=(W⊕C)∨S | sticky parity hub |
| parity_hub | S′=W⊕C | single-attractor contrast |
| maj3 | majority all nodes | multi-same contrast |
| w_follows_c | W′=C, S′=W∧C, C′=S | asymmetric feed |

**#109 contrast (re-run).** Sticky vs memoryless hysteresis loop area
under the probe_hysteresis protocol (activity, not Φ).

## H1 — coexistence regime exists

At least one form on the panel has ≥1 triadic attractor and ≥1 dyadic
attractor, each with basin size ≥1.

Null: no form shows that pair.

## H2 — only hysteresis / path dependence, no true coexistence

No panel form shows triadic↔dyadic attractor coexistence, while the
#109 sticky activity loop remains (area_sticky − area_memoryless ≥
0.05). The sticky story is path dependence without Φ-verdict
bistability.

Null: H1 holds, or the #109 area gap fails.

## H3 — multistability but not dyadic↔triadic

At least one form has ≥2 attractors whose Φ-verdicts are all the same
(all dyadic or all triadic) — multistability without cross-verdict
coexistence — and H1 is false for the panel.

Null: no same-verdict multistable form, or H1 already holds (H3 is
then reported as a secondary witness on sticky/maj3, not the primary
word).

**Primary verdict word.**
- H1 → `GENUINE_COEXISTENCE`
- else H2 → `ONLY_HYSTERESIS`
- else H3 → `MULTISTABLE_SAME_VERDICT`
- else → `BISTABILITY_MIXED`

When H1 holds, sticky/maj3 same-verdict multistability and the #109
loop are reported as contrast witnesses, not as H3's primary word.

**Instrument gate.** Faithful memoryless triad whole-form triadic
Φ=2.0; sticky whole-form dyadic (matches #43); #109 sticky area >
memoryless area by ≥0.05.

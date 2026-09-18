# Parity radix blind spot — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #4).** Is the parity blind spot (#113)
binary-specific, or do higher-radix “balanced” commits (sum mod k)
produce the same low-Φ pure-higher-order forms?

**Instrument.** Exact IIT-4.0 Φ. Binary (k=2) via stock pin + overlay
full-system check. Higher radix via `third_party/pyphi_iit4_mv`
full-system `exact_phi` (N=3; k∈{2,3,4}). In-silico.

**#113 witness (cited).** Among 24 triadic corpus forms, XOR/XNOR
commits carry Φ=0.5; conjunctive commits carry Φ=2.0. The Φ=0.5 forms
are the pure-higher-order band (#56).

**Universe.** Faithful triad CM; parties copy S (`W'=C'=S`).
- **parity/balanced:** `S'=(W+C) mod k`
- **conjunctive analog:** `S'=min(W,C)` (k=2: AND)

**Primary observables (full system).** Max Φ over states; mean Φ on
states with Φ>0 (flatness). Pure-higher-order on binary via stock
(best proper-subset Φ=0). Overlay subset Φ is **not** trusted for
pure-HO at k>2 (known dyadic inflation on XOR); H2 uses the #113
Φ-signature (low flat parity vs high conjunctive), not overlay
subset pure-HO.

**Pointers.** #1–#3 beyond-binary closed.

## H1 — binary-specific

Sum-mod-k at k∈{3,4} does **not** show a low-Φ band relative to
min-commit at the same k (parity max Φ ≥ half of conjunctive max, or
no flat low band). Null: higher radix recreates the split.

## H2 — sum-mod-k recreates low-Φ higher-order signature at radix k

For each k∈{2,3,4}: sum-mod max Φ is low and roughly flat across
positive states; min-commit max Φ is substantially higher (factor ≳ 2).
At k=2 this matches #113 (0.5 vs 2.0). Null: no such split.

## H3 — morphs

The higher-radix pattern exists but **morphs**: e.g. parity max Φ
drifts away from 0.5, loses flatness, or the ratio to conjunctive
collapses toward 1. Null: same qualitative signature as #113.

## Reading keys

- **BLINDSPOT_SURVIVES_RADIX:** ¬H1 ∧ H2 (and H3 soft — mild drift OK).
- **BINARY_SPECIFIC:** H1.
- **MORPHED:** H3 without clean H2.

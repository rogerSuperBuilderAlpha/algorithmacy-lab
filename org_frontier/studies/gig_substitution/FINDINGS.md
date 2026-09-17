# Gig substitution — findings

**Verdict: DROP_AT_FIRST_SUBST.** In a symmetric gig match, the
individual worker drops from the major complex at the **first positive
substitution rate**. With `r = 1 − m/k`, workers stay in iff `r=0`
(all-required); any `r>0` ejects every `Wi` (core `{S,C}`). Under full
OR, the drop is at the first extra worker (`k=1→2`). No smooth
dilution — membership is binary. All-required solidarity keeps every
worker in through k=4. Extends #22 to a size/rate sweep; #8 pointer
only.

In-silico; candid N (k≤4, n≤6). Hypotheses fixed in `hypotheses.md`.
Cited: #22/#8; #31 pointer; #29–#34 pointers only. Closed lanes stay
closed.

## Hypotheses

| H | result |
|---|---|
| H1 sharp drop at first subst | **SUPPORTED** |
| H2 smooth dilution | **REFUTED** |
| H3 never drops under solidarity | **SUPPORTED** (AND k=1..4) |

## Threshold

| regime | workers in core? |
|---|---|
| r=0 (m=k) | **all in** (Φ=k+1) |
| r>0 (m<k) | **all out** → `{S,C}` |
| OR k=1 | W1 in |
| OR k≥2 | all out |

## Witnesses

| form | core | reading |
|---|---|---|
| OR_k1 / AND_k1 | {W1,S,C} | single-worker triad |
| OR_k2..4 / m<k | {S,C} | **drop** |
| AND_k2..4 / m=k | all Wi+S+C | **solidarity** |
| #22 subst / both / coal | {S,C} / full / {W1,W2} | probe match |
| W1req_ORrest k=3,4 | {W1,S,C} | focal stays if constitutive |
| OR+weak union | {W1..Wk} | relocates to peer core |

## Reading

A gig platform that can match *any* of many interchangeable workers
has already lost every individual worker from the irreducible
coordination — the threshold is the first bit of substitutability, not
a high substitution rate. Keeping workers in the core requires
all-required matching (or solidarity that relocates the core to the
peer group). Mirrors counterpart substitutability (#22) at scale.

## Limits

Boolean designed sweep; k≤4; symmetric m-of-k; no organization
measured; stochastic substitution rate not swept (discrete r).

## Best next

**#36** — extractive ejection order (PE lane closable after).

## Reproduce

```
python org_frontier/studies/gig_substitution/analyze_gig.py
```
(~110 s)

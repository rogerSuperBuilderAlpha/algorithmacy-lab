# Wageman TI → verdict — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #44).** Does measured task
interdependence (Wageman-style) predict the verdict on a modeled task?

**Instrument.** Exact binary IIT-4.0 Φ (stock pin). Designed Boolean
forms, mostly N=3; one N=4 all-required witness. In-silico.

**Pointers.** #43 PARTIAL_ALIGNMENT / `CONSTRUCT_VALIDITY_ARC.md` only.
Survey TI items live in `survey/cohort_algorithmacy/codebook.md`
(Pearce & Gregersen 1991; Van der Vegt et al. 2001; Wageman 1995 cited
for consequences). The survey `phi_bridge` gates commit on TI≥4.5 with
SA/SU — a threshold map, not this score→verdict test.

**Wageman-like index (explicit).** Survey TI asks how tightly parties’
work depends on each other. On a form, read three CM facets only (no
joint-AND / cycle primitives — those are the IIT switches from #43, not
the survey construct):

| facet | structural read | survey echo |
|---|---|---|
| reciprocity | (# mutual undirected pairs) / C(n,2) | “mine depends on theirs and vice versa” |
| input | mean indegree / (n−1) | “cannot complete without input” |
| affect | mean outdegree / (n−1) | “how I work affects others” |

`W = (reciprocity + input + affect) / 3` ∈ [0,1]. Report also
`TI_7 = 1 + 6W` on the survey’s 1–7 scale. Self-loops ignored for
pair counts; included in degree means.

**Panel.** Designed tasks spanning low→high W with known verdicts:
independent; one-way feed; pooled_indep; seq_handoff; recip_acyclic;
AND chain; XOR chain (same CM, Φ=0.5); OR chain; all-required n=4.
#43 forms reused as witnesses.

**Primary observables.** Structure; max Φ; W; TI_7. Prediction:
ROC AUC and best-threshold accuracy of W→triadic; Spearman ρ(W, Φ);
point-biserial r(W, triadic).

## H1 — Wageman-style score predicts dyadic/triadic

AUC(W → triadic) ≥ 0.85 **or** best-threshold accuracy ≥ 0.85 on the
panel. Null: below both cutoffs.

## H2 — weak / null

AUC ≤ 0.65 **and** best accuracy ≤ 0.65. Null: predictive above weak.

## H3 — predicts Φ magnitude better than verdict

Spearman ρ(W, Φ) ≥ 0.70 **and** ρ(W, Φ) exceeds |r_pb(W, triadic)| by
≥ 0.10 (Φ association materially stronger than verdict association).
Null: verdict association ≥ Φ association, or ρ(W, Φ) < 0.70.

## Reading keys

- **WAGEMAN_PREDICTS_VERDICT:** H1 (and not H2).
- **WAGEMAN_NULL:** H2.
- **WAGEMAN_PHI_NOT_VERDICT:** H3 without H1.
- **WAGEMAN_BOTH:** H1 and H3 (score tracks both; note which is stronger).

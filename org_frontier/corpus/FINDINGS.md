# Findings — the coordination-form corpus

From `results/corpus.csv` and `results/toggles.csv`, exact IIT-4.0 Φ on the IIT-4.0 venv. All
eight forms match their documented verdict (0 mismatches).

## The corpus

| Form | Verdict | Φ_MIP | strict mediation | mediator reads both | validated |
|---|---|---|---|---|---|
| chat_dyad | dyadic | 0.00 | yes | no | ✓ |
| gig_dyadic_model | dyadic | 0.00 | yes | no | ✓ |
| pure_relay | dyadic | 0.00 | yes | no | first-pass |
| ats_feedback_factors | dyadic | 0.00 | yes | **yes** | ✓ |
| hierarchy_backchannel | dyadic | 0.00 | no | yes | first-pass |
| ats_strict_bottleneck | triadic | 2.00 | yes | yes | ✓ |
| gig_false_dyad | triadic | 2.00 | yes | yes | ✓ |
| two_sided_match | triadic | 2.00 | yes | yes | first-pass |

## The structure-first result: topology does not decide irreducibility

Two structural features that one might expect to settle the verdict do not.

1. **Strict mediation is necessary, not sufficient.** Seven of eight forms have no direct
   worker–counterpart channel, yet the verdict splits four dyadic and three triadic. Removing the
   direct channel does not by itself make a form irreducible.

2. **"The mediator reads both parties" is also not sufficient.** `ats_feedback_factors` has strict
   mediation *and* a mediator whose commit reads both W and C (S' = W ∧ C), yet it factors
   (Φ = 0). What separates it from the triadic forms is the parties' own read functions: its
   W' = ¬S and C' = S ∨ C do not keep each party a live function of the mediator's current commit,
   so the system factors along {W,S}|{C} despite the joint determination.

So irreducibility needs both: a mediator that jointly determines from both sides, and party reads
that keep each side live to that determination. Neither alone is enough.

## The ablations confirm necessity

`results/toggles.csv`, single-feature changes on the three triadic forms:

| Ablation | Effect on every triadic form |
|---|---|
| drop the mediator's dependence on C (S no longer reads the counterpart) | Φ 2.00 → 0.00, **flips to dyadic** |
| add a partial back-channel (C also reads W) | Φ 2.00 → 0.42, **stays triadic** |

Dropping the mediator's read of the third party destroys irreducibility every time — confirming
the joint determination is load-bearing. A partial back-channel only grades Φ down without
flipping the verdict; a full direct channel would be needed to collapse it (dissertation Paper 2,
the eliminate-the-dyad endpoint).

## Population check: the finding holds across the whole strict-mediation family

`population.py` enumerates the complete strict-mediation three-node family — every Boolean form with
no direct worker–counterpart edge: `W' = f_W(S)`, `C' = f_C(S)`, `S' = f_S(W, C)`, so
4 × 16 × 4 = 256 forms. Exact IIT-4.0 Φ for each (`results/population.csv`). This turns the
eight-form illustration into a population result.

| Quantity | Value |
|---|---|
| strict-mediation forms | 256 |
| triadic (Φ > 0) | 24 (**9.4%**) |
| P(triadic \| mediator reads both parties) | **15.0%** (24/160) |
| P(triadic \| mediator does not read both) | **0.0%** (0/96) |

Two precise claims fall out. Strict mediation is far from sufficient: 90.6% of forms with no
back-channel still factor. And the mediator reading both parties is **necessary** (0% triadic
without it) but **not sufficient** (only 15% triadic with it) — the parties' own read functions
decide the remaining 85%. This is the same result the curated forms showed, now quantified over the
whole family. (The complete 4,096-wiring family, including back-channels, is the dissertation's
`paper3_baseline/catalog.py`; this is the strict-mediation slice with the conditional breakdown.)

## Which determination functions support irreducibility

`determination.py` re-analyzes the 256-form population by the mediator's Boolean function. The
dissertation found the function dominates Φ *magnitude*; this asks the prior question — which
functions support the triadic *verdict* at all.

- **One-input and constant functions support none.** A mediator whose commit reduces to W alone, C
  alone, or a constant (W, C, ~W, ~C, TRUE, FALSE) yields 0/16 triadic forms — it never reads both
  parties, so the necessity result holds at the function level.
- **Among genuine two-input functions, parity leads.** XOR and XNOR each support 4/16 triadic forms,
  twice the 2/16 of the monotone functions (AND, OR, NAND, NOR) and the mixed functions. A parity
  determination — the outcome flips on either party's change — binds the parties into irreducibility
  across more read-function combinations than a simple all-required (AND) or either-suffices (OR)
  commit. This matches IIT's standing result that XOR mechanisms are highly integrated, and the
  dissertation's `parity_present` structural feature.

The org-theory reading: a mediator whose rule is exclusive/parity-like (e.g. "act only if exactly
one side signals") produces irreducible coordination more readily than a threshold or
all-or-nothing rule.

## Why this is of general interest

The result is about what makes a small discrete system integrated, stated in structural terms that
do not depend on the coordination interpretation: among mediated three-node systems, Φ > 0 requires
both a mediator that reads all sources and downstream reads that stay live to the mediator's state.
It supplies clean minimal test cases where a single edge or a single read function toggles Φ
between 0 and 2 — useful for anyone probing PyPhi's behavior on small structured systems.

## Caveats

- Binary verdict only; Φ magnitude is encoding-dependent and not a scale (see `../classifier/`).
- Three forms are first-pass models, flagged; they reuse defensible couplings but are not yet
  validated against the dissertation's worked cases.
- Eight curated forms are an illustration, not a population. The complete-family distribution is
  the dissertation's 4,096-wiring catalog.

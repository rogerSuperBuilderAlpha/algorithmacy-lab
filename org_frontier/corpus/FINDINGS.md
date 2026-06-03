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

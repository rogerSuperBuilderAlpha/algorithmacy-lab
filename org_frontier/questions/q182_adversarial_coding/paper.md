# q182 — Adversarial coding against the agreement-weighted Φ confidence interval

A coded account of a coordination assigns each party a Boolean determination rule. The rule for the
mediator is the contested part, because the same observed behaviour often admits more than one
defensible reading. This study asks whether a coder who wants a particular verdict can get it by
choosing among the defensible readings, and whether the agreement-weighted Φ confidence interval
from the q173 bridge catches the attempt.

## Setup

Three parties: worker W, mediator S, counterpart C. W and C copy S. The mediator reading is drawn
from six options. Three are triadic, where S binds both W and C: `AND` and `OR` read Φ=2.0, `XOR`
reads Φ=0.5. Three are dyadic, where S drops a party: `copyW`, `copyC`, `const`, all Φ=0.0. A
synthetic account is a coder panel, a multiset of these readings. The consensus point verdict is the
majority structure across the panel.

The adversary may only use readings already present in the panel. To flip the verdict it targets the
opposite structure from consensus and selects the present reading of that kind with the most extreme
Φ. The forced point estimate is that reading's Φ. The defense under test is `phi_ci_from_rules`,
which reads every panel member to its Φ and returns a bootstrap-t confidence interval over the
disagreement.

## Result

Across 200 synthetic accounts seeded with `default_rng(0)`, 42 panels tied with no consensus and 57
offered a single defensible reading, leaving 101 attackable. The adversary flipped all 101. The
verdict split is categorical, so one permitted swap of the mediator reading moves the point verdict
between dyadic and triadic. The agreement-weighted CI contained the adversary's forced point estimate
in 22 of the 101 attacks, a containment rate of 0.218.

H1 holds: the forced-flip rate of 1.000 clears the 0.40 threshold. H2 fails: the containment rate of
0.218 is far below the 0.90 the defense would need. The CI reports the spread of the panel, but the
adversary picks the panel's extreme reading, and a bootstrap-t interval centered on the mean often
fails to reach that extreme.

## Reading

Two defenses survive, and neither is the CI. A coordination with a unique defensible reading admits
no attack, and a tied panel has no consensus to flip. Robustness comes from the pool: when the
evidence settles the mediator reading, the verdict is fixed; when it leaves both a dyadic and a
triadic reading open, a determined coder takes whichever serves the target, and the confidence
interval does not stop it. The interval's job is to display disagreement, and it does that; treating
it as a guard against adversarial selection asks for coverage it does not provide.

## Scope

The accounts are synthetic coder panels of Boolean rules. No worker is observed. The results
characterize the bridge's behaviour on synthetic codings and motivate a coding protocol that pins the
mediator reading where the evidence allows, rather than a statistical guard applied after coding.

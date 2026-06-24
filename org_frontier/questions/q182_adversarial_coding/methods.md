# q182 — methods

## Machinery

The probe reuses the q173 bridge `org_frontier/field/rule_to_phi.py`: `rule_to_phi` encodes a
party's Boolean determination rules into a deterministic TPM and reads the exact IIT-4.0 Φ_MIP
verdict through the classifier; `phi_ci_from_rules` reads each coder's rule set to its Φ and
propagates panel disagreement into a bootstrap-t confidence interval. Φ is not reimplemented.

## Account model

A coordination has three parties, worker W, mediator S, counterpart C. W and C copy the mediator
(`x -> x[1]`). The coded content lives in the mediator reading. A reading is one of six:

- triadic (S binds both W and C): `AND` (Φ=2.0), `OR` (Φ=2.0), `XOR` (Φ=0.5);
- dyadic (S drops a party): `copyW`, `copyC`, `const` (all Φ=0.0).

A synthetic account is a coder panel: a multiset of reading names, one per coder, repeats allowed.
The consensus point verdict is the majority structure across the panel; a tied panel has no
consensus and is dropped from the attack.

## Population

`N_ACCOUNTS = 200`, drawn with `numpy.random.default_rng(0)`. Each account is contested with
probability 0.65 (1–3 triadic readings plus 1–3 dyadic readings, both kinds defensible) or unique
with probability 0.35 (one reading repeated 3–5 times, one kind only). The bootstrap-t CI inside
`phi_ci_from_rules` is seeded with `default_rng(0)` per account, so the whole probe reproduces
byte-for-byte.

## Adversary

The adversary is restricted to readings actually present in the panel's defensible pool. To flip
the verdict it targets the opposite kind from consensus and picks the present reading of that kind
with the most extreme Φ: highest Φ when forcing triadic, lowest when forcing dyadic. The forced
point estimate is that reading's Φ. An account with no opposite-kind reading in its pool is
powerless for the adversary and is excluded from the attacked set.

## Measures

- forced-flip rate: attacked accounts where the adversary's chosen reading has a different
  structure from consensus, over all attacked accounts.
- CI-containment rate: attacked accounts where the adversary's forced Φ point estimate lies inside
  the agreement-weighted CI, over all attacked accounts.

## Controls

- Instrument: the faithful triad `[x1, x0&x2, x1]` reads triadic with Φ_MIP = 2.0.
- Control A (honest consensus): a unanimous `['AND']*4` panel has no opposite-kind reading, so the
  adversary cannot flip it.
- Control B (unique reading): a `['copyW']*3` panel gives the adversary no alternative and a
  degenerate CI `[0,0]`.

## Scope and validation gap

All inputs are synthetic coder panels. No worker is observed; the rule sets are stipulated. The
empirical arms describe the behaviour of the bridge on synthetic codings, not on field data.

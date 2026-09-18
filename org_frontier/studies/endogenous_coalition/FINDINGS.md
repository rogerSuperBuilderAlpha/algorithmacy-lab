# Endogenous coalition — findings

**Verdict: MULTI_NASH_MAXPAY.** When counterparts choose join/leave to
maximize own major-complex membership, pure Nash are **all-out** and
**all-in** (weak games). Both give max own-core pay. Partial coalitions
can maximize one player yet are **not** Nash (mismatch). #66’s imposed
full coalition is one equilibrium — not unique. Enumeration Nash;
association of structure with incentives, not a field claim.

In-silico; candid N (designed join games k=2,3). Hypotheses fixed in
`hypotheses.md`. Cited: #1/#66/#37; #29 pointer only. Other lanes
closed.

## Hypotheses

| H | result |
|---|---|
| H1 Nash recovers max-own-core pay | **SUPPORTED** |
| H2 mismatch (max-own-core ⊄ Nash) | **SUPPORTED** |
| H3 multiple stable coalitions | **SUPPORTED** |

## Games

| game | Nash joins | note |
|---|---|---|
| weak_k2 | 00, 11 | partial 01/10 unstable (joiner out) |
| weak_k2_P | 00, 11 | all-in → {C1,C2} ejects P (#66) |
| strong_k2 | all 4 | always max pay |
| weak_k3 | 000, 111 | same dual pattern |

## Witnesses

- **#66 endogenous:** `weak_k2_P` joins=11 is Nash; core `{C1,C2}` Φ=2;
  P out — imposed solidarity is incentive-compatible.
- **Also Nash:** joins=00 keeps `{W,S,C1,C2,P}` Φ=4 with equal
  membership pay — imposing the coalition selects among max-pay eq.
- **Mismatch:** joins=01 maximizes C1 but C2 can deviate; not Nash.

## Reading

Endogenous choice **can** form the max-own-core coalition #66 imposed,
but parties are equally happy (on the membership bit) with no
coalition. The structural win of solidarity is not uniquely selected by
own-core-membership best response. Partial coalitions are a trap for
the joiner.

## Limits

Binary join; payoff = core membership bit only (not Φ share); pure
Nash enumeration; weak/strong peer channels only; no mixed eq.

## Best next

**#31** — worker-union scale (alt **#32** rival platforms).

## Reproduce

```
python org_frontier/studies/endogenous_coalition/analyze_coalition.py
```
(~25 s)

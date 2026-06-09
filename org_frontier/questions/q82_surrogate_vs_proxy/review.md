# Q82 — Stage 1 review: the learned surrogate against single proxies

## The question

Q81 showed the surrogate recovers the verdict perfectly in-distribution and fails to cross sizes. Within
a fixed size, how far does combining cheap features beat the single proxies that earlier studies showed to
fail — and does it separate the verdict in the collision regime where a structural proxy is constant?

## What the lab already knows that bears on this

- **In-degree and edge count collide across verdicts (Q72).** The read_recipient triad and the one_shot
  dyad share in-degree 2 and edge count 4. No structural cut separates that pair.
- **Φ_R and Φ_WMS separate the classes only near chance (`proxy_bridge`, rank-AUC ≈ 0.56–0.63).**
- **The surrogate recovers the verdict in-distribution at CV AUC 1.000 (Q81).** The comparison to single
  proxies on the same family is the open piece.

## The gap

Q72 and `proxy_bridge` reported each proxy on its own; a head-to-head against the learned surrogate on one
common set of trajectories is uncomputed, as is whether the surrogate separates the verdict on the
modal-in-degree subset where the structural proxy carries no information.

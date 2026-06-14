# Q82 — The learned surrogate against the proxies that failed

## Question

Q72 and `proxy_bridge` showed that no single cheap proxy recovers the outreach verdict: mediator
in-degree and edge count collide across verdicts, and the time-series proxies Φ_R and Φ_WMS separate the
classes only near chance. Q81 showed that a random forest over many cheap features recovers the verdict
perfectly in-distribution. This study puts them head to head on one common set of trajectories, and asks
whether the surrogate separates the verdict in the collision regime where a structural proxy is constant.

## Method

The corpus is the 256 strict-mediation outreach forms at n = 3, labelled by exact IIT-4.0 Φ. For each
form, four single proxies are computed: mediator in-degree and total edges from the connectivity matrix,
and Φ_R and Φ_WMS estimated from a noisy trajectory. The learned surrogate is Q81's, a random forest over
the ten size-invariant features, evaluated by stratified 5-fold cross-validation on the same trajectories.
Each proxy is scored by rank-AUC and by its best single-threshold accuracy. The modal-in-degree subset
isolates the forms where the mediator reads both parties, so in-degree is constant — the regime of the
Q72 read_recipient/one_shot collision.

## Results

The surrogate separates the verdict perfectly and beats every single proxy. Its CV ROC-AUC and accuracy
are both 1.000. The best single proxy is total edge count at AUC 0.966; in-degree, Φ_R, and Φ_WMS trail at
0.707, 0.621, and 0.547. On the 160-form modal-in-degree subset, where in-degree carries no information,
the surrogate's out-of-fold accuracy is still 1.000.

| proxy | rank-AUC | best-threshold accuracy |
|---|---|---|
| mediator in-degree | 0.707 | 0.906 |
| total edges | 0.966 | 0.938 |
| Φ_R | 0.621 | 0.922 |
| Φ_WMS | 0.547 | 0.922 |
| learned surrogate (CV) | 1.000 | 1.000 |

The pre-registered H1 — every single proxy below AUC 0.85 — is refuted, because total edge count reaches
0.966. Triadic forms on the strict-mediation family carry more active edges, and a plain count picks that
up. The refutation leaves the comparison intact: edge count's best-threshold accuracy is 0.938, capped by
the collisions Q72 documented, where a triadic and a dyadic form share an edge count. The surrogate clears
that cap.

| | result |
|---|---|
| H1 every single proxy rank-AUC < 0.85 | refuted (edges 0.966) |
| H2 surrogate AUC ≥ 0.95 and beats every proxy | confirmed (1.000) |
| H3 surrogate accuracy > best single-proxy threshold | confirmed (1.000 vs 0.938) |
| H4 surrogate OOF accuracy ≥ 0.90 on modal-in-degree subset | confirmed (1.000) |

## Interpretation

At a fixed size, a learned combination of cheap features is the best available reader of the verdict, and
it succeeds precisely where single proxies collide. Edge count is a useful rank on this family but not a
clean separator: it inherits Q72's collisions and stops at 0.938. The surrogate reads the difference those
collisions hide, including on the constant-in-degree subset where the structural proxy says nothing.

The result reconciles two earlier readings of edge count. Q72 measured it on two colliding pairs and
concluded it cannot separate them; that remains true. Across the whole family edge count still ranks the
verdict well, which the two-pair view did not measure. The honest statement is both: a strong rank and an
imperfect separator, beaten by the surrogate.

The scope is fixed-size. Q81 showed the surrogate does not generalize to larger forms, so this is a
statement about reading the verdict at one size, not about replacing the exact computation. The exact
classifier remains the instrument; the surrogate is the best cheap reader where an exact label exists to
fit it.

## Limitations

In-silico; Boolean models with exact labels and cheap-statistic inputs. Edge count's strength is specific
to the strict-mediation family, where triadic forms are edge-rich, and need not transfer to other
populations. Class imbalance (9.4% triadic) means the comparison rests on rank-AUC and the constant-
in-degree subset, not on raw accuracy. The comparison does not extend past n = 3.

# Q81 literature — learned surrogates for an expensive integration measure

## The size ceiling and the surrogate idea

Exact integrated information is intractable past roughly ten to twelve elements, because the
minimum-information partition search is super-exponential (Mayner et al. 2018 on PyPhi's cost;
Albantakis et al. 2023 for the IIT-4.0 formalism). Neuroscience answers this with surrogates: train or
define a cheap estimator on systems small enough to label exactly, then apply it where exact computation
is impossible. Mediano et al. (2022) and Rosas et al. (2019) develop information-decomposition estimators
in exactly this role. The move is the same one a learned model makes: an exact teacher labels a training
set, and a cheap student predicts past the teacher's reach.

## Why a single cheap proxy is not enough here

This lab's Q72 and `proxy_bridge` established that no single cheap proxy recovers the outreach verdict:
structural proxies (mediator in-degree, edge count) collide across verdicts, and time-series proxies
(ΦID Φ_R, whole-minus-sum Φ_WMS) separate the classes only near chance (rank-AUC ≈ 0.56–0.63). The
recurring cause is that cheap proxies track statistical dependence, while the verdict tracks
irreducibility, and the two come apart at any real back-channel. A back-channel raises dependence without
raising integration along the minimum-information partition.

## The open question this study takes up

Probe #21 found that a forest combining many cheap features recovers the verdict in-distribution on the
256-form family, where no single feature does. That probe used a raw per-node panel, whose length grows
with n, so it cannot be applied at a size it did not train on. The agenda question (Q81) is whether a
surrogate built on size-invariant features generalizes past the exact-Φ size ceiling: trained on small
forms, does it classify larger forms it never saw? A surrogate that does would be the route past the
ceiling that the single-proxy bridge failed to provide. One that does not would mark the ceiling as real
for this verdict even with a learned student. Both outcomes are reported.

## Method context

The feature estimators (entropy, mutual information, transfer entropy per Schreiber 2000, O-information
per Rosas et al. 2019) are the repo's existing `_info` panel, reduced to intensive aggregates. The random
forest and cross-validation follow standard supervised practice (Breiman 2001).

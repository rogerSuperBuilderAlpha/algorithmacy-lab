# Q82 literature — a combination of cheap features against single proxies

## The single-proxy failures this study compares against

Q72 tested two structural proxies for the outreach verdict — mediator in-degree and edge count — and
found they collide across verdicts: the read_recipient triad and the one_shot dyad have identical
in-degree (2) and identical edge count (4), so no structural cut separates them. `proxy_bridge` tested
two time-series proxies on coordination forms — ΦID Φ_R and whole-minus-sum Φ_WMS — and found rank-AUC
of roughly 0.56 and 0.63: neither cleanly preserves the verdict, because both track statistical
dependence rather than irreducibility (Mediano et al. 2022; Rosas et al. 2019 on the decomposition that
makes this precise). The recurring lesson is that a back-channel raises dependence without raising
integration along the minimum-information partition.

## Why a combination can succeed where each part fails

A single proxy is one projection of the form's statistics. The verdict can be a function of several
projections jointly even when no single one carries it — the standard reason ensemble methods over
many weak features beat any one feature (Breiman 2001). Probe #21 saw exactly this in-distribution on
the 256-form family: a forest over many cheap features recovered the verdict that no single proxy did.
Q82 makes the comparison head to head and on the same trajectories, and asks specifically whether the
combination separates the verdict in the collision regime where the structural proxy is constant.

## Scope set by Q81

Q81 established that the surrogate does not generalize past the size it trains on: trained on n=3, it
classifies larger forms worse than chance. Q82 is therefore in-distribution only. The contribution is a
clean within-size comparison: how far a learned combination of the same cheap signals exceeds each
single proxy that the earlier studies showed to fail.

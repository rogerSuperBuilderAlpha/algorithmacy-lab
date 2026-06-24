# q184 — Φ spread between a driver's suggestion and a platform's commit account of dispatch

A gig driver and the platform tell different stories about the same dispatch. The driver calls it
a suggestion: the app proposes a rider, and the driver is free to decline. The platform calls it a
commitment: accepting the ping locks the driver into the rider match. Qualitative research treats
that gap as data. This study scores the gap with the q183 disagreement-Φ bridge, on synthetic rule
sets that encode each account.

The two accounts run over labels `(D, P, R)` = (Driver, Platform, Rider). The platform commit
account is the worker-system-counterpart triad `[x1, x0&x2, x1]`: the platform turns on only when
the driver and the rider are both on, and the driver and the rider each track the platform. It
reads triadic with max Φ_MIP = 2.0, and its integrated core is the full set `{D, P, R}`. The
driver suggestion account is the dyadic rewrite `[x1, x0, x1]`: the platform tracks the driver
alone, and the rider is never wired into the loop. It reads dyadic with Φ_MIP = 0, and its core is
`{D, P}`.

The bridge reports the spread. The two accounts split on the verdict (dyadic vs triadic), so
verdict_agreement = 0. The phi_gap is 2.0, which equals the platform account's whole-system Φ_MIP
because the driver account carries no integrated information at all. The core_jaccard is 0.667:
the rider sits inside the platform's integrated core and outside the driver's. H1 and H2 both hold.

The result has a plain reading. The disagreement is not only about how strongly the dispatch binds
the parties. It is about who is bound. Under the driver's account the rider is external to the
coordination loop; under the platform's account the rider is one of three parties the platform
holds together. The bridge separates those two claims into two numbers: phi_gap measures the
magnitude split, and core_jaccard measures the membership split.

A consensus control, where both parties narrate the same commit account, returns zero spread. The
metric anchors at zero when the accounts agree, so the 2.0 gap and 0.667 overlap are properties of
the disagreement.

The accounts are synthetic, coder-supplied rule sets, not measured driver or rider states. The
empirical arms are on synthetic data. The construct is divergence between two stated accounts of
one dispatch. The gap between a coded account and an observed dispatch stays open; later studies in
this line apply the bridge across more settings.

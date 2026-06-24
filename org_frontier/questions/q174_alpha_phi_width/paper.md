# q174 — Propagated Φ confidence-interval width as a read of coder disagreement

A coded account of a coordination is read by people, and people disagree about which states
are active. The field bridge encodes each coder's reading as a per-party Boolean rule set,
reads its exact IIT-4.0 Φ verdict, and propagates the disagreement into a confidence interval
on Φ. This study asks whether that interval behaves like a measurement instrument: does its
width track agreement, and is there an agreement floor below which the verdict goes honestly
indeterminate.

Agreement is measured by Krippendorff alpha on the coder-by-unit matrix of active-bit
decisions. Eight synthetic coders read each of three borderline forms over twelve decision
units. Each form is a faithful triad whose mediating coupling, if a coder drops it, collapses
the reading to a dyad with Φ = 0. Disagreement is injected at a controlled fraction f: a graded
share of coders read the collapse, and background units carry enough split to set the
matrix-wide alpha. Sweeping f sweeps alpha from 1.0 down to about 0.33. The per-coder Φ readings
feed the bridge's bootstrap-t CI. Φ is not reimplemented.

The width tracks agreement. The Spearman correlation between alpha and mean CI width is -0.988
(p = 4.26e-06): at perfect agreement the interval collapses to a point, and it widens as
agreement falls. H1 is supported.

A stable agreement floor turns the verdict indeterminate. The CI brackets zero only at the
lowest agreement tested, alpha = 0.329, where about half the coders read the dyadic collapse.
That threshold is identical across two independent ensembles, inside the +/-0.05 stability band.
H2 is confirmed. Above the floor the instrument returns a determinate dyadic-or-triadic verdict
with an interval whose width reports how much the coders disagreed; below it, the instrument
reports that it cannot tell the two apart.

The control separates two reasons an interval can be wide. A panel of two distinct positive-Φ
readings, never the collapse, gives a wide interval whose lower bound stays above zero: coders
disagree about magnitude, not verdict. The zero-crossing is reserved for verdict disagreement.

The result is in-silico. The coder panels and the active-bit decisions are synthetic, the forms
are Boolean models, and the alpha sweep is engineered. The study validates the
disagreement-to-CI instrument, not any measured coordination. Whether real coded field accounts
produce the same monotone width and a comparable floor is the open empirical question this line
opens.

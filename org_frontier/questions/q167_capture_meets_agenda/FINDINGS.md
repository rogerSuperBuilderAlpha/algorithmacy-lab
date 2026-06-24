# q167 findings — interest does not simply lower the capture threshold

Both hypotheses are refuted. The worker-governs threshold g* is non-monotone in the platform's interest,
and where the worker is displaced she is replaced by the counterpart C, not by the agenda node P. Interest
reshapes which input the worker is replaced by, but it does not compound capture into a uniformly lower
threshold.

## The g-sweep

| setting | g* (W exits) | post-core | core at g = 0.00 -> 0.25 -> 0.50 |
|---|---|---|---|
| faithful | 0.05 | SC | WSC -> SC -> SC |
| approve k=1 | 0.40 | SC | WSC -> WSC -> SCP |
| approve k=2 | 0.05 | SC | WSC -> SC -> SC |
| approve k=3 | none | — | WSC -> WSC -> WSC |
| approve k=4 | none | — | WSC -> WSC -> WSC |
| deny k=1 | none | — | WSC -> WSC -> WSC |

The faithful platform captures the commit almost immediately (g* = 0.05). Raising interest does not push
g* lower. Approve k = 2 matches the faithful threshold (g* = 0.05) because its platform branch still reads
both P and C. Approve k = 1 raises g* to 0.40. Approve k = 3, k = 4, and deny k = 1 keep the worker in the
core across the whole grid: those agendas drive the platform branch to a constant, which carries no
information to compete with the worker's W AND C term, so the worker is never displaced within the grid.

## H2 — what replaces the worker

The faithful post-displacement core is SC: the worker is replaced by the counterpart. Every interested
setting that displaces W within the grid (approve k = 1 at g* = 0.40, approve k = 2 at g* = 0.05) also
lands on SC at g*. The agenda node P appears in the core only for approve k = 1, and only at the high end
(g = 0.50, core SCP), past the displacement threshold. The post-displacement core is the same for faithful
and interested platforms where displacement happens at all.

| H | Result | Verdict |
|---|--------|---------|
| H1 | g* falls monotonically as the platform becomes interested | REFUTED |
| H2 | beyond g*, the interested core retains the agenda node P where the faithful core retained C | NOT SUPPORTED |

## Reading

The faithful platform branch P AND C reads both the platform input and the counterpart, so a small capture
share is enough to outweigh the worker's term and take her seat. An agenda displaces the worker only where
its branch stays informative about (P, C): approve k = 2 reads NOT-P-or-C and captures at the same low g*,
while approve k = 1 reads P-equals-C and needs a larger share. Where the agenda goes constant — approve
k = 3, k = 4, and the degenerate deny ladder — the platform branch carries no information, the worker's
W AND C term governs, and she keeps her seat regardless of g. The replacement, when it happens, is the
counterpart C: the worker is displaced by the input the platform still reads, not by the agenda's
invariant value. Interest is a second axis from capture; it changes who the worker is replaced by and
whether she is replaced at all, and it does not collapse into a single lower threshold.

## Limitations

Exact Φ on a four-node Boolean model; evidence about the construct and the instrument, not a claim about a
real platform. "Capture", "agenda", "approve", "deny" label a mixing weight and committed output values,
not measured intent. The empirical arm of this line runs on synthetic data. The faithful baseline branch
is AND and the platform mixes linearly with it; an OR baseline or a different mixing rule would relabel
which (P, C) states each agenda overrides and is the natural robustness extension. The deny agenda is
degenerate past k = 1 under AND, so its informative range is one level; an OR baseline would open it up.

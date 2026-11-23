# When everyone is misread the same way, a majority vote still splits apart

*Last time, any amount of independent error made a majority-vote coordinator irreducible. This time we made the errors shared. Shared errors leave it exactly reducible, and the reason is a simple symmetry.*

## The question

In the [last experiment](2026-11-23-noisy-majorities.md), a coordinator read three people's yes/no
signals, decided by majority, and everyone acted on the decision. With perfect readings, the setup
splits cleanly into parts: integrated information Φ (IIT 4.0, computed exactly with PyPhi) is 0. When
the coordinator misread each person independently, Φ became positive at every error rate we tried.
Φ measures how far a system's cause-and-effect structure fails to split into independent parts. It is
not a claim that anything is alive or aware.

Real errors are often shared: a bad sensor, a wrong default, a system outage misreads everyone at
once. So: does the effect depend on the errors being independent?

## What we ran

Three rules (any yes = OR, majority, all yes = AND), each with the same error rate per reading, under
three kinds of error:

- **independent**: each reading goes wrong on its own (last time's setup);
- **shared**: either every reading flips together or none does;
- **half and half**: each reading is hit by a shared flip and by its own flip, sized so the error rate
  per reading is the same.

Eight error rates from 0 to 0.45, 72 exact Φ calculations, about 90 seconds of compute. Predictions
were committed before running.

## What we found

**Shared errors keep the majority at exactly zero, at every rate.** We predicted this before running.
Majority is symmetric: flip every input and the result flips too. So when all readings flip together,
the coordinator's decision is simply the true majority or its opposite, and the noise adds nothing that
depends on how many people said yes. The system still splits into parts.

**Any independent part brings it back.** With half the error shared, majority's Φ was positive at
every rate:

| error rate | 0.01 | 0.1 | 0.2 | 0.3 | 0.45 |
|---|---:|---:|---:|---:|---:|
| majority, independent errors | 0.0035 | 0.0270 | 0.0366 | 0.0320 | 0.0091 |
| majority, half shared | 0.0018 | 0.0147 | 0.0224 | 0.0225 | 0.0083 |
| majority, fully shared | 0 | 0 | 0 | 0 | 0 |

**Shared errors are much easier on the extreme rules.** At an error rate of 0.45, OR keeps Φ = 1.18 under
shared errors, against 0.015 under independent ones.

**The majority still never binds the whole group.** Under every kind of error, the most tightly bound
part never contains all three people. OR and AND keep everyone bound under shared errors at every rate,
and under half-shared errors up to 0.4; at 0.45 the instrument finds no bound part at all.

## What it means

The majority's positive Φ comes from errors that treat people differently. That gives the coordinator's
decision a dependence on how many people said yes, which a clean majority throws away. It does not come
from error as such. For algorithmacy, this means two coordinators with the same error rate can differ
in whether they hold together, depending on whether their mistakes fall on everyone alike or on
individuals. The rule for who ends up bound together held again: a majority never binds the whole group.

## Limits

Three-person yes/no models only, not real platforms. People never err, and everyone updates at once. We
tested two kinds of correlation and one mixing level. The software returns one bound part per state, so
ties between identical people are not listed. One setting (OR and AND, half-shared, 0.45) gives a small
negative Φ, which is a numerical quirk we read as zero. A pattern from last time held: in all 14 cases
where the majority's Φ was positive, its tightest part had exactly four times the whole-system value.

## The code

- Study: [org_frontier/studies/quorum_correlated_noise/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/quorum_correlated_noise)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_correlated_noise/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_correlated_noise/FINDINGS.md) and [results/results.csv](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_correlated_noise/results/results.csv)

Run it yourself: `python3 tools/start.py`, then
`python org_frontier/studies/quorum_correlated_noise/correlated.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the
numbers are PyPhi's.

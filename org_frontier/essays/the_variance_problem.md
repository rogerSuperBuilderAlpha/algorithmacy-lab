# The variance problem

A language model asked the same question many times returns many answers. They look different. The
difference is mostly on the surface. Read for content, the answers converge, often onto a single verdict, and
the number of genuinely independent answers is far below the number of responses. Treating N model responses
as N observations counts one answer many times. That is the variance problem, and the best_time_pilot study
gives it a first measurement.

## Four answers, one of them counted

The pilot is small on purpose. Four students each asked a fresh ChatGPT session "what was the best time in
history?" and submitted the answer. The four texts share about a third of their wording. They name almost the
same eras, marshal the same evidence — life expectancy doubled, the post-war boom, the Renaissance — and all
four conclude that the present is the best time for the average person. Mean similarity rises from 0.342 at
the level of words to 0.754 at the level of claims, and the closing verdict is unanimous. The visible
diversity is the wording. The content is one answer in four outfits.

The effect has a number. The effective sample size, n_eff = N² / (1ᵀ K 1), is the count of independent
responses implied by a similarity kernel K. It returns the nominal N when the responses are distinct and
falls toward one as they repeat. Across the pilot's four answers it reads 1.98 on wording and 1.23 on
content. Four answers to this question are worth about one and a quarter. A claim like "three of four named
the Renaissance" reports the same answer three times.

## What survives the collapse, and what does not

The answers that look most distinctive are the least reliable. Each of the four names one era no other names
— the Pax Romana, the Age of Discovery, the late 1990s. These single-mention eras are the visible diversity,
and they are exactly the part that would not survive a re-run. The unanimous core — the present, the post-war
boom, the Renaissance, the verdict — is the part that reproduces. Diversity and reliability run opposite
here. The interesting divergences sit in the tail that resampling would wash out, and the stable content is
the least varied.

This inverts the natural reading of a set of model answers. The eye is drawn to the response that mentions
the Pax Romana, and that is the draw least likely to recur. A study that sampled four answers and reported
the spread of eras would report its own tail as if it were signal.

## Why the lab is the place to measure it

The lab already holds the two facts the variance problem sits between. The reproducibility study (q123) shows
the Φ verdict is a deterministic function of a pinned build, bit-identical across runs. The invariance study
(q197) shows a measurement bridge holding its slope and intercept across panel waves. Determinism and
invariance are properties a good instrument should have. A language model sampled for behavioral data has
neither by default: its outputs vary run to run, and the variation is layered, so a naive count of responses
is not a count of observations. The same discipline that pins a Φ verdict and tests a bridge for invariance
asks, of a model used as a data source, how many independent answers N responses contain.

The integration reading ties the measurement to the lab's own tool. Claims travel in bundles — the answers
that name Classical Athens also name the Islamic Golden Age and organize by criterion, while the named-era
answer carries the Pax Romana and the late 1990s. On the response×claim matrix this reads as redundancy: the
o-information over the era columns is positive. Redundancy is the information-theoretic form of the variance
problem. The responses share more than independent draws would, and the surplus is what n_eff subtracts.

## The claim, and its size

The pilot establishes an instrument and a model, on four responses, for one prompt, from one model, on one
day. It estimates nothing with power. The design-effect form of n_eff is degenerate at this sample size, the
o-information is undersampled, and "best time in history" is a question models are unusually agreed on. The
scaled study is where the estimate lives: a full class, a contrast between re-running one prompt and varying
the prompt, a bank of contested questions, a temperature sweep that should pull the surface n_eff up while
the content n_eff stays near one. What the pilot fixes is the shape of the answer — apparent diversity high,
effective diversity near one — and a way to measure the gap.

# Q203 — Reading a real coordination four ways

## Abstract

The lab's recurrence studies ran on synthetic trajectories and found that behavioral coupling measures do not
cleanly recover the structural coordination verdict. This study takes the same question to real data for the
first time. A real two-party coordination — two people building with LEGO, dominant-hand movement over 5799
time points — is read by cross-recurrence quantification, transfer entropy, Granger causality, and convergent
cross mapping, each validated on a control in its own domain. Cross-recurrence finds strong symmetric
structure (59.8% determinism). The three directed measures agree in sign, all making the second person the
driver, but none reaches significance against circular-shift surrogates. Behavioral coupling on this real
dyad gives a consistent but non-significant direction and no verdict a single measure could stand on, the
real-data face of the synthetic null.

## Why this study

Every program in the lab's research watch names the same gap: the results are in-silico and have not touched
real data. The recurrence program states it precisely — there is no head-to-head evaluation of CRQA against
transfer entropy and convergent cross mapping on the same naturalistic dyadic data. This study runs that
head-to-head, on a real dyad, as the program's first real-data contact.

## The data

The `handmovement` dyad distributed with the crqa R package: a real LEGO joint-construction session,
dominant-hand transfer for two people (P1_TT_d, P2_TT_d), 5799 time points. It is small, public, and a
canonical example in the interpersonal-coordination literature. Committed at `data/handmovement.csv`.

## The four measures, each on its own control

Cross-recurrence quantification reads symmetric recurrent structure. Transfer entropy and Granger causality
read directed dependence and are validated on a linear AR system with a known X→Y drive. Convergent cross
mapping reads directed coupling in deterministic dynamics and is validated on a coupled chaotic logistic
system, its proper domain. CCM was moved to the deterministic control because it does not read direction on
the linear one, which marks the boundary of where it applies. Circular-shift surrogates give significance for
each directed measure. The controls pass before the real data is read.

## Result

Cross-recurrence determinism is 59.8%: the coordination is structured. The three directed measures all point
from the second person to the first, agreeing in sign, while none clears its surrogate (p = 0.078, 0.510,
0.235). The reading is in [`FINDINGS.md`](FINDINGS.md).

## Limitations

One real dyad, one channel, a worked example rather than a population. No exact Φ: a real time series has no
ground-truth transition function, so this study runs only the behavioral-recovery side of the bridge, which
is the side observable data supports. The estimator settings are fixed in the probe. Larger open corpora for
a population study are listed in the watch's [`DATA_SOURCES.md`](../../../research/DATA_SOURCES.md).

## Reproduce

`python ci/reproduce.py q203-real-coordination-coupling`

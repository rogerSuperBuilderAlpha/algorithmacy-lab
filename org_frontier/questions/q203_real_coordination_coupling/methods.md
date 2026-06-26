# Q203 methods

**Data.** `data/handmovement.csv`, the `handmovement` dyad from CRAN package `crqa` (`data(handmovement)`):
5799 time points, four channels (dominant and non-dominant hand transfer for two people). This study uses the
dominant-hand channel for each person (P1_TT_d, P2_TT_d), z-scored. The choice of channel is fixed before the
analysis; it is not selected to maximise an effect.

**Measures.**
- *CRQA.* Continuous cross-recurrence: the recurrence threshold is the 5th percentile of pairwise distances
  (target recurrence rate 5%). %REC is the recurrence rate; %DET is the fraction of recurrent points on
  diagonal lines of length ≥ 2.
- *Transfer entropy.* Each series discretised into six quantile bins; TE(X→Y) over lag 1, in bits.
- *Granger causality.* AR order 5; the F-statistic comparing the model of Y on its own lags against the model
  with X's lags added.
- *Convergent cross mapping.* Simplex projection, embedding dimension 3, lag 1; the series is decimated to
  ≤1400 points for tractability; cross-map skill ρ is the correlation between cross-mapped and observed
  values. Direction follows Sugihara: if X drives Y, Y's manifold reconstructs X, so Y-cross-maps-X is high.

**Controls.** Transfer entropy and Granger are validated on a linear AR system with a known X→Y drive
(`x[t]=0.5x[t-1]+noise`, `y[t]=0.4y[t-1]+0.8x[t-1]+noise`); both must read X→Y. CCM is validated on a coupled
chaotic logistic system (`x[t+1]=x[t](3.7-3.7x[t])`, `y[t+1]=y[t](3.7-3.7y[t]-0.32x[t])`), its proper domain;
it must read X→Y. The analysis stops if any control fails.

**Significance.** Circular-shift surrogates (50 shifts of the source series); the p-value is the surrogate
exceedance rate with a +1 correction.

**Determinism.** All randomness (surrogate shifts, control generation) is drawn from `numpy.random.default_rng(0)`,
so the output is reproducible; verified by running twice.

# Cross-recurrence concepts, and how they relate to Φ

Cross-recurrence quantification analysis reads coordination from two time series. It places one
series on each axis, marks every pair of time points where the two systems occupy matching states,
and quantifies the resulting pattern of marks. The marks are recurrences. Their density, their
arrangement into diagonal and vertical lines, and their offset from the main diagonal each carry a
distinct fact about how the two systems coordinate.

The lab's parties hold Boolean states, so the categorical form of CRQA is the exact one. Two points
match when they are equal, the embedding dimension is one, and the delay is one. The continuous form,
where each point is a vector reconstructed from a graded signal by time-delay embedding and two
points match within a radius, is the generalization the agenda reaches for with vitals and movement
data. [`crqa.py`](crqa.py) implements the categorical case.

## The parameters

- **Delay (τ).** The spacing between samples taken to reconstruct the state. One, for series sampled
  step by step.
- **Embedding dimension (m).** The number of delayed coordinates stacked to represent the state. One,
  for a categorical series whose state is its current symbol.
- **Radius.** The distance within which two points count as matching. Exact equality, for categorical
  series. For continuous signals the radius is tuned to fix the recurrence rate in a target band.
- **Theiler window.** A band along the main diagonal excluded to remove trivial self-matches. It
  matters for the recurrence of one series with itself. Cross-recurrence compares two different
  series, so the main diagonal is not trivially recurrent and no window is needed.

## The measures

Each is computed from the cross-recurrence matrix R, where R[i, j] = 1 when series x at time i
matches series y at time j (Webber and Zbilut 1994; Marwan et al. 2007).

- **RR, recurrence rate.** The density of matches, the gross share of time the two systems co-visit
  states. For binary series two independent runs match about half the time by chance, so RR sits near
  0.5 and is not by itself diagnostic of coupling.
- **DET, determinism.** The fraction of recurrent points lying on diagonal lines of length two or
  more. A diagonal line means the two systems run in parallel for several steps, so DET measures the
  share of the coupling that is sustained. Two sticky series share long runs and so score high DET
  even without coupling, which is why DET is read together with the profile below.
- **L and Lmax, mean and maximum diagonal line length.** How long a coordinated episode typically
  lasts, and the longest one. Lmax separates parties that track each other in long stretches from
  parties that touch only briefly.
- **ENTR, entropy of the line-length distribution.** The complexity of the coordination structure,
  high when episodes come in many lengths.
- **LAM and TT, laminarity and trapping time.** The share of recurrence in vertical lines, and their
  mean length: how much the pair gets stuck in a shared state and for how long.

## The diagonal cross-recurrence profile

The profile is RR computed along each diagonal of R, as a function of the lag k = j − i. Its shape is
the directional read-out (Marwan et al. 2007; Wallot and Leonardi 2018).

- A peak at lag zero is synchronous coupling.
- A peak at positive k means y's states recur k steps after x's, so x leads and y follows by k. The
  sign of the peak lag is leader-from-follower, the observable trace of a directed read edge: if a
  party's rule reads another's prior state, the read party leads in the profile.
- The peak's prominence, its height above the profile's baseline, says whether the lag is real. A
  directed coupling makes a sharp, prominent peak. Two series with no preferred lag make a flat
  profile near the recurrence floor, where the location of the maximum is noise. On binary series the
  prominence, not the rate, is what separates a genuine lead-lag from chance.

## How CRQA differs from Φ

The two instruments answer different questions about the same arrangement, and the framework keeps
the questions apart.

| | Φ (integrated information) | CRQA |
|---|---|---|
| Object | the model's mechanism | a run's two time series |
| Question | can the whole be split without loss | do the parties' states track each other |
| Stance | intrinsic, structural | extrinsic, observed |
| Input | the transition rules | recorded behavior, no model |
| Reads direction | from the connectivity matrix | from the profile peak lag |
| Yields | irreducibility, the major complex | coupling strength, duration, lead-lag |

A mutual coupling is Φ-irreducible and shows sustained cross-recurrence. A one-way relay is
Φ-reducible, since a feedforward chain splits, yet shows a strong directed profile peak. So the
instruments can disagree, and the disagreement is informative: Φ marks the structural whole, CRQA
marks the directed behavioral coupling, and a relay has the second without the first.

CRQA's directional read-out has well-studied neighbors that also recover coupling direction from time
series: Granger causality, transfer entropy, and convergent cross mapping (Sugihara et al. 2012).
Those measure prediction and information transfer between series. Φ measures intrinsic causal
irreducibility of a mechanism, which is a different object, and pairing Φ with CRQA is not the same
move as adding one more transfer measure.

## Citations

- Eckmann, J.-P., Kamphorst, S. O., and Ruelle, D. (1987). Recurrence plots of dynamical systems.
  *Europhysics Letters*, 4(9), 973–977.
- Zbilut, J. P., and Webber, C. L., Jr. (1992). Embeddings and delays as derived from quantification
  of recurrence plots. *Physics Letters A*, 171(3–4), 199–203.
- Webber, C. L., Jr., and Zbilut, J. P. (1994). Dynamical assessment of physiological systems and
  states using recurrence plot strategies. *Journal of Applied Physiology*, 76(2), 965–973.
- Marwan, N., Romano, M. C., Thiel, M., and Kurths, J. (2007). Recurrence plots for the analysis of
  complex systems. *Physics Reports*, 438(5–6), 237–329.
- Shockley, K., Santana, M.-V., and Fowler, C. A. (2003). Mutual interpersonal postural constraints
  are involved in cooperative conversation. *Journal of Experimental Psychology: Human Perception and
  Performance*, 29(2), 326–332.
- Richardson, D. C., and Dale, R. (2005). Looking to understand: The coupling between speakers' and
  listeners' eye movements and its relationship to discourse comprehension. *Cognitive Science*,
  29(6), 1045–1060.
- Coco, M. I., and Dale, R. (2014). Cross-recurrence quantification analysis of categorical and
  continuous time series: an R package. *Frontiers in Psychology*, 5, 510.
- Coco, M. I., Mønster, D., Leonardi, G., Dale, R., and Wallot, S. (2021). Unidimensional and
  multidimensional methods for recurrence quantification analysis with crqa. *The R Journal*, 13(1),
  145–163.
- Wallot, S., and Leonardi, G. (2018). Analyzing multivariate dynamics using cross-recurrence
  quantification analysis, diagonal cross-recurrence profiles, and multidimensional recurrence
  quantification analysis. *Frontiers in Psychology*, 9, 2232.
- Feldman, R., Magori-Cohen, R., Galili, G., Singer, M., and Louzoun, Y. (2011). Mother and infant
  coordinate heart rhythms through episodes of interaction synchrony. *Infant Behavior and
  Development*, 34(4), 569–577.
- Sugihara, G., May, R., Ye, H., Hsieh, C., Deyle, E., Fogarty, M., and Munch, S. (2012). Detecting
  causality in complex ecosystems. *Science*, 338(6106), 496–500.
- Sarasso, S., Casali, A. G., Casarotto, S., Rosanova, M., Sinigaglia, C., and Massimini, M. (2021).
  Consciousness and complexity: a consilience of evidence. *Neuroscience of Consciousness*, 2021(2),
  niab023.

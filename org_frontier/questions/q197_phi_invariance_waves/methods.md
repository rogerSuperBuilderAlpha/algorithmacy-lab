# q197 — methods

Run line:
`source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && python -m org_frontier.questions.q197_phi_invariance_waves.probe_phi_invariance_waves | tee org_frontier/questions/q197_phi_invariance_waves/results/output.txt`

## Instrument

Φ_coord reuses the study-1 bridge module `org_frontier/survey/cohort_algorithmacy/phi_bridge.py`. Each
worker's wave-specific (TI, SA, SU) row maps to a W-S-C Boolean form. The system node S commits the joint
determination AND(W, C) when the worker reports a binding, interdependent, non-substitutable coordination
(TI >= 4.5, SA >= 4.5, SU < 4.0), giving the faithful mediated triad with Φ_coord = 2.0; otherwise S
conveys W, the form factors, and Φ_coord = 0.0. Φ is the exact IIT-4.0 max Φ_MIP from
`classifier.tpm_from_rules` + `probes.lib.max_phi_float`.

Instrument control: the canonical faithful triad `[x1, x0&x2, x1]` reads verdict `triadic` with
max_phi 2.0 before any cohort computation. The probe asserts this and prints `CONTROL ... PASS`.

## Panel simulation

A three-wave panel of 240 workers per wave. Each worker carries a stable latent coordination capability
z. At every wave the reported TI, SA load positively on z and SU loads negatively, plus wave-level noise;
an ACS-total factor score loads on the same stable z plus independent noise and is standardized within
wave. Φ_coord is recomputed independently at each wave from that wave's reports. Because the latent is
stable across waves, the bridge holds across waves by construction. One fixed seed
(`numpy.random.default_rng(0)`); Φ_coord depends only on which of two Boolean forms a worker maps to, so
the per-wave sweep reproduces exactly.

## Multigroup invariance of ACS-on-Φ

The bridge is treated as a single-predictor regression `ACS = a_g + b_g * Φ + e` per wave g. Per-wave
sufficient statistics are the means, variances and covariance of (Φ_coord, ACS). Three nested models are
fit by maximum likelihood on those statistics:

- configural — separate slope and intercept per wave (saturated regression, fit function 0 per wave);
- metric — common slope across waves, intercepts free;
- scalar — common slope and common intercept across waves.

Each model's chi-square is the sum over waves of n_g times the normal-theory ML fit function (mean
structure included). CFI = 1 - max(chi2 - df, 0) / max(chi2_indep - df_indep, 0), with the independence
baseline suppressing the within-wave Φ-ACS covariance. H1 reads ΔCFI(configural -> metric); H2 reads
ΔCFI(metric -> scalar); the cutoff is .01.

## Control

The permuted-wave-label cohort pools the rows and re-splits them into pseudo-waves by a random label,
removing genuine across-wave structure. ΔCFI is averaged over 200 seeded permutations so the control
reports the expected trivial-invariance behaviour rather than a single noisy split.

## Scope and validation gap

The cohort is simulated. No worker is measured. The association between Φ_coord and ACS is built into the
synthetic panel through the shared latent; the bridge recovers it through the exact-Φ instrument. The
invariance verdicts are a property of the instrument and the bridge on synthetic data. Fitting the same
pipeline on real wave files (wave{1,2,3}.csv with the codebook columns) is the validation step that this
arm does not yet perform.

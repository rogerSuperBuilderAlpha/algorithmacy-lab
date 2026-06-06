# Q62 — Excluded outer cut signal

## Question

On aligned one-sided back-channel forms at uniform max_phi=2.0, does the excluded (non-tied) outer singleton
cut with normalized_phi=1.0 carry independent return-path signal once tied-seam and type are known to be
co-extensive?

## Panel

Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56. Instrument control: canonical triad
reads triadic, max_phi=2.0, MIP `2 parts: {W,SC}`.

## Methods

Excluded singleton from Q57 `excluded_outer_cut` applied to the official tied cut. Tied singleton and
return-path typing from Q61/Q60 helpers. Joint-label counting and complement/inverse cross-tabs in
`excluded_cut_utils.py`.

## Results

### H1 — Excluded complement of tied

Complement matches 16/16. Mismatches 0/16. Excluded singleton is always the non-recipient complement of
the tied singleton.

### H2 — Excluded inversely tracks type

Inverse type matches 16/16. Direct type matches 0/16. Excluded C pairs with sequential typing; excluded W
pairs with reciprocal typing — the inverse encoding of the tied-seam/type partition.

### H3 — Excluded determined by tied

Within-tied excluded heterogeneity 0/16. W-tied rows all carry excluded C; C-tied rows all carry excluded W.

### H4 — No third independent joint label

Distinct joint labels 2. Cell (W, sequential, C) on 8/8. Cell (C, reciprocal, W) on 8/8. No third
partition dimension appears.

### H5 — Excluded norm uniform, no Phi subpanel lift

Excluded norm 1.0 on 16/16. Panel max_phi spread 0.000000. Excluded-W subpanel spread 0.000000. Excluded-C
subpanel spread 0.000000.

## Synthesis

Q61 (#206) established tied singleton seam and return-path type as co-extensive partitions. Q62 closes the
seam/typing micro-thread: the excluded outer cut at normalized_phi=1.0 adds no independent label. It is the
deterministic complement of the tied seam and the inverse mirror of return-path type. The Q57–Q61 partition
geometry thread therefore ends with a two-cell joint space; norm asymmetry between tied and excluded cuts
does not restore verdict-level discrimination.

## Validation gap

Results describe deterministic n=3 Boolean coordination forms at finest grain with synchronous update. They
do not extend to empirical organizations or coarser grains.

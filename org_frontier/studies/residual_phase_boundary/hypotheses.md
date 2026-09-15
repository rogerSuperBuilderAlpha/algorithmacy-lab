# residual_phase_boundary — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 F28).** Do the near-boundary holistic forms (Probe 131) sit on a
genuine phase boundary in function space — do small perturbations flip the exact Φ verdict?

**Universe.** The 4096 unconstrained 3-node wirings of Probe 125 (`residual_panel.csv`), each a triple
of 2-input Boolean tables. Residual set = forms a Probe-131 random forest misclassifies under 5-fold
CV (`n_estimators=400`, `random_state=0`). Near-boundary residual = residual forms with
`|p − 0.5| < 0.25` (Probe 131's boundary band).

**Perturbation.** For each seed form, the 12 Hamming-1 neighbours obtained by flipping one bit in one
of the three 4-bit truth tables. Exact IIT-4.0 Φ_MIP verdict via `classify_rules`. A neighbour
*flips* if its triadic/dyadic structure differs from the seed's.

**Controls (fixed seed 28):**
- **Near-hit control:** all correctly classified forms with `|p − 0.5| < 0.25` (classifier-uncertain
  but not residual). If that pool is smaller than the residual set, use the full pool (unequal n is
  allowed; means are compared).
- **Far-hit control:** a sample of correctly classified forms with `|p − 0.5| ≥ 0.40`, size equal to
  the near-boundary residual set (classifier-confident).

**Primary rate.** For a set of seeds, the mean over seeds of (flipping neighbours / 12).

F26/F27 are not reopened.

## H1 — residual near-boundary is a phase boundary

Among near-boundary residual forms, the mean one-bit flip rate is at least **0.25** (on average at
least 3 of 12 neighbours flip the exact verdict), and the fraction of seeds with at least one
flipping neighbour is at least **0.80**.

Null: mean flip rate < 0.25, or fewer than 80% of seeds have any flip.

## H2 — residual boundary exceeds confident forms

The near-boundary residual mean flip rate exceeds the far-hit control mean flip rate by at least
**0.10** (10 pp). That separates a genuine verdict phase boundary from generic stability of typical
forms.

Null: residual − far-hit < 0.10.

## H3 — residual boundary is not just classifier uncertainty

The near-boundary residual mean flip rate exceeds the near-hit control mean flip rate by at least
**0.05**. If residual and near-hit controls flip at similar rates, the phase boundary tracks
classifier uncertainty rather than the holistic residual specifically.

Null: residual − near-hit < 0.05.

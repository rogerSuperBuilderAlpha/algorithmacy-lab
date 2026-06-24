# q148 — Review

Claim. A feedforward chain of gating hubs integrates only its first hub-and-group loop; the core stops at the
first hub seam, and depth does not extend it.

Strengths.
- Exact IIT-4.0 Φ throughout; no reimplementation. The instrument control on the faithful triad passes
  (triadic, max Φ 2.0, spanning core).
- A built-to-span control (single all-spanning hub) fixes the reading of "spans all groups" at n = 4, so the
  chain's failure to span is not an artifact of the measure.
- Deterministic: seeds fixed, re-runs byte-identical.

Limits and threats.
- Group size is fixed at g = 1, so each hub ANDs a single party, which makes hub_0 reduce to its party's
  identity. Larger groups (g >= 2) would make every hub a genuine multi-input AND and push n to 9 and 12,
  beyond tractable exact Φ at L = 3, 4. The single-group cap is shown at g = 1 only; whether a wider group
  changes which seam cuts is open.
- H1 was framed as a graded "critical chain length." The data show an immediate cap at one group, which
  supports the directional claim and rejects the null but does not exhibit a graded threshold. The finding is
  reported with that correction rather than forced onto the original framing.
- The feedforward direction is a modeling choice. A chain with feedback across seams (closer to the
  mutually-coupled two-hub) could span further; this study isolates the one-way case.
- The all-spanning control is read at n = 4 only. Its fully-integrated complex grows costly fast, so n >= 6 is
  skipped to keep the probe re-runnable. The spanning reading is anchored at n = 4 and is not expected to change
  with n, but the larger-n control is not computed here.
- Synthetic scope. No organization is measured. "Core", "seam", "span" are Φ-and-graph quantities. The
  Φ-to-organization bridge is open, so the empirical reading is a baseline on synthetic data, not a field result.

Verdict. The synthetic claim holds within scope. H1 supported (with the graded-threshold framing corrected to
an immediate cap), H2 confirmed. Worth extending to g >= 2 by an approximation that keeps n tractable, and to a
chain with cross-seam feedback.

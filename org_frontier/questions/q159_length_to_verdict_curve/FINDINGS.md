# q159 — findings

The CRQA triadic/dyadic verdict settles fast. Convergence length does not track Φ magnitude in this
corpus, and what little it tracks runs against the hypothesis.

## Length curve (95 forms: 18 triadic, 77 dyadic)

| steps | agree exact-Φ | matches reference verdict |
|------:|--------------:|--------------------------:|
| 150   | 0.7158        | 0.8211                    |
| 300   | 0.7684        | 0.9158                    |
| 600   | 0.8000        | 0.9474                    |
| 1200  | 0.8105        | 0.9579                    |
| 2400  | 0.7684        | 1.0000                    |

Spread threshold fit at 2400 steps: spread >= 9.0 reads triadic (balanced accuracy 0.6230).
Share of forms with a verdict that has settled to its reference reading by 600 steps: 92.63%.

## Convergence length by exact-Φ tertile (rank split)

| Φ tertile | n  | mean convergence length |
|-----------|---:|------------------------:|
| low       | 31 | 159.7                   |
| mid       | 33 | 336.4                   |
| high      | 31 | 450.0                   |

## Verdicts

- **H1: SUPPORTED.** 92.63% of forms converged by 600 steps (over the 80% bar), and agreement with
  the exact-Φ verdict does not rise from 1200 (0.8105) to 2400 (0.7684). Six hundred steps is enough
  to read a stable verdict for nearly all forms.

- **H2: REFUTED.** Mean convergence length rises with Φ tertile (159.7 low, 450.0 high), the opposite
  of the prediction that high-Φ forms settle sooner. The premise has little room to be tested: Φ piles
  up at 2.0 (median 2.0, range 0.342-2.0), so low and high tertiles straddle the same ceiling value
  and Φ magnitude carries almost no variance to drive convergence length.

## Reading

Agreement with the exact-Φ verdict tops out near 0.81 and the spread threshold reaches only 0.62
balanced accuracy, so a single spread cut is a coarse behavioral proxy for the structural verdict.
The convergence claim is about stability, not accuracy: the verdict a run will give stops changing by
600 steps even where that verdict is wrong. That agreement dips slightly from 1200 to 2400 reflects a
few forms whose fixed-threshold reading drifts across the boundary at the longest run, not a gain from
more data.

## Scope

Synthetic Boolean coordination forms. Every Φ is exact IIT-4.0 Φ on a model transition matrix; the
behavioral side is a sampled run of that model. No field organization is measured, and the bridge from
a coded organization to a transition matrix is not yet validated against observed data.

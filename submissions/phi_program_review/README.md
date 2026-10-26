# The Φ program so far

Synthesis review of the lab's exact-Φ program through late October 2026: what the classifier computes, which structural results held, which pre-registered predictions failed, and the gap between the Boolean models and a real organization. The manuscript is Roger Hunt's. This directory is the arXiv package.

## Files

| file | role |
| --- | --- |
| [`paper.md`](paper.md) | Markdown source of the review |
| [`main.tex`](main.tex) | LaTeX source |
| [`main.pdf`](main.pdf) | Compiled manuscript |
| [`references.bib`](references.bib) | Bibliography |
| [`main.bbl`](main.bbl) | BibTeX rendering of the reference list |
| [`arxiv_submission.tar.gz`](arxiv_submission.tar.gz) | arXiv bundle (`main.tex`, `main.pdf`, `references.bib`) |

## Instrument

The 540-check benchmark stays on `wmayner/pyphi` `feature/iit-4.0` at `b78d0e342d37175cbd55cf35a6d52ae035b4c50f` (`1.2.1.dev1470+gb78d0e342`, 26 December 2025). `requirements.txt` installs that branch. `ci/reproduce.py` calls `pyphi.Network`, `pyphi.Subsystem`, and `pyphi.new_big_phi`.

The lab fork `rogerSuperBuilderAlpha/pyphi` holds the same commit on `feature/iit-4.0`. `develop` is at `f92b981d69c6c2de3887509d21b9b834ae4af906` (11 April 2026), synced with upstream. `2.0` is at `ccd247dcad5dd1c38635bdf1095af82919e3cf37` (17 May 2026). The multivalued port of [`third_party/pyphi_iit4_mv`](../../third_party/pyphi_iit4_mv/) is on `feat/multivalued-iit4-radix-k` (`3d96339ac74aa086112545141306907ab32b4e15` and `4cdda4a1cbf73e89dd368e3991990c3933dd8b48`), open as [rogerSuperBuilderAlpha/pyphi#1](https://github.com/rogerSuperBuilderAlpha/pyphi/pull/1).

Upstream `wmayner/pyphi` `main` is `134a8f31b49db512322465ed3ba5da7194d362fd` (16 October 2026; tag `v2.0.0rc4`, version line `2.0.0rc5.dev0`). That line is the PyPhi 2.0 release candidate (`pip install --pre pyphi`). It replaces `Network` / `Subsystem` / `new_big_phi.sia` with `Substrate` / `System` / `analyze()` (`System.sia()`, `System.phi_structure()`). Mixed-radix state is native on `FactoredTPM` (`num_states_per_node`). Tied MIPs stay on `sia.ties`. Coarse-graining and blackboxing live in `pyphi.macro` (`MacroSubstrate`, `CoarseGraining`, `Blackbox`, `emergence`; Marshall et al. 2026). Estimation lives in `pyphi.estimate` (`estimate_mip`, `purview_inclusion_probabilities`, `random_partitions`).

`wmayner/pyphi#140`, `#141`, `#142`, and `#147` targeted legacy `feature/iit-4.0`. Will Mayner noted on `#147` that the branch is superseded by the 2.0 candidate on `main`. All four closed on 25 October 2026.

These controls were run on PyPhi 2.0 at `134a8f31` under Python 3.13. Under `pyphi.iit4_2026` (`formalism="IIT_4_0_2026"`), φ_s^(2026)(s, P) = min{φ_c(s, P), φ_e(s, P), ii(s)}, where ii(s) = min{ii_c(s), ii_e(s)} and each directional term is the minimum of intrinsic differentiation and intrinsic specification. A strictly deterministic transition (ε = 0) has a single forward effect state, so effect differentiation vanishes and ii(s) = 0. That forces φ_s = 0 on every strictly deterministic Boolean gate, unless the network is evaluated with positive transition noise or under `pyphi.iit4_2023`.

On the binary conjunctive triad (W' = S, S' = W ∧ C, C' = S) at (1, 1, 1), `pyphi.iit4_2023` at flip rate p = 0 returns φ_s = 2.000000 (φ_c = φ_e = 2.000000, structure Φ = 12.000000 across 4 distinctions with Σφ_d = 5.0 and 8 relations with Σφ_r = 7.0), matching `feature/iit-4.0@b78d0e342`. The same preset decays with noise: φ_s = 1.898808 at p = 0.01 (Φ = 11.559196), 1.533412 at p = 0.05 (Φ = 9.937348), 1.155438 at p = 0.10, 0.610634 at p = 0.20, 0.276923 at p = 0.30, and 0.089648 at p = 0.40. Under `pyphi.iit4_2026` at p = 0, φ_s = 0 because ii(s) = 0, while φ_c = φ_e = 2.000000 and structure Φ = 12.000000. With p > 0, φ_s follows ii(s) at 0.043216 (p = 0.01), 0.215495 (p = 0.05), and 0.432740 (p = 0.10), reaches φ_s = φ_e = 0.610634 at p = 0.20 once ii(s) = 0.894818 exceeds φ_e, and then follows φ_e to 0.276923 (p = 0.30) and 0.089648 (p = 0.40).

The three-voter majority triad at (1, 1, 1) scores φ_s = 0 under both presets. PyPhi 2.0 exposes `len(sia.ties) == 4` at that value, and `d.cause.purview_ties = [((0, 1), 0.5), ((1, 2), 0.5), ((0, 2), 0.5)]` on voter A's first-order distinction.

The ternary conjunctive triad (k = 3, 27 states, W' = S, S' = min(W, C), C' = S) at (2, 2, 2) returns φ_s = 3.169925 = 2 log₂ 3 under `pyphi.iit4_2023` at ε = 0 (structure Φ = 16.906267), matching `third_party/pyphi_iit4_mv`. `smoke_m2.py` prints the same figure, 3.169925, on its 2-node ternary control. Under `pyphi.iit4_2026` that state is φ_s = 0 at ε = 0, φ_s = ii(s) = 0.043499 at ε = 0.01 (φ_c = 2.991744, φ_e = 3.020328), and 0.222002 at ε = 0.05 (φ_c = 2.387629, φ_e = 2.481492). At (1, 1, 1), `pyphi.iit4_2023` returns φ_s = 0.194988 (φ_c = 0.194988, φ_e = 0.584963, `len(sia.ties) == 3`, structure Φ = 7.258146) on {W, S, C}, while {W, S} and {S, C} each score φ_s = 0.508798. Under `pyphi.iit4_2026`, (1, 1, 1) is φ_s = 0 at ε = 0, 0.043499 at ε = 0.01, and φ_s = φ_c = 0.179018 at ε = 0.05.

## Reproduce

From the repository root, with the environment in [`GETTING_STARTED.md`](../../GETTING_STARTED.md):

```bash
python -m org_frontier.classifier.validate
python ci/reproduce.py
python third_party/pyphi_iit4_mv/smoke_m1.py
python third_party/pyphi_iit4_mv/smoke_m2.py
```

`python ci/reproduce.py` re-derives every registered number on the `feature/iit-4.0` pin. The two smoke scripts are the M1 and M2 checks for the multivalued overlay.

Rebuild the PDF from this directory:

```bash
tectonic main.tex
# or: pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

The bibliography is already expanded inside `main.tex`, so a single `tectonic main.tex` is enough. Refresh the arXiv bundle after a source change:

```bash
tar -czf arxiv_submission.tar.gz main.tex main.pdf references.bib
```

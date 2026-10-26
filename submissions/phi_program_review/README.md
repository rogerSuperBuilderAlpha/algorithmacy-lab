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

Under `pyphi.iit4_2023()` (Albantakis et al. 2023), system integration is the uncapped directional minimum, φ_s = min(φ_c, φ_e). On `134a8f31` that preset matches `feature/iit-4.0@b78d0e342` and `third_party/pyphi_iit4_mv` to machine precision. The binary conjunctive triad at `(1,1,1)` has φ_s = 2.0 (Φ = 4.5, 4 distinctions, 10 relations). The majority triad at `(1,1,1)` has φ_s = 1.666667. The ternary conjunctive triad (`num_states_per_node=(3,3,3)`, S' = min(W, C)) at `(2,2,2)` has φ_s = 1.584963 (log₂ 3).

Under `pyphi.iit4_2026()`, the default, Mayner, Marshall, and Tononi (2026) cap directional partition integration by system-level intrinsic information: φ_s = min{φ_c, φ_e, ii(s)}, where ii(s) is the minimum, over cause and effect, of the minimum of intrinsic differentiation and intrinsic specification. The cap leaves the majority triad at φ_s = 1.666667, lowers the binary conjunctive triad to φ_s = 1.0 (Φ = 4.5, 4 distinctions, 10 relations unchanged), and lowers the ternary state `(2,2,2)` to φ_s = 0.630930. Each control stays positive (φ_s > 0), and the Φ-structure remains. The majority triad in that check is the PyPhi majority gate. The three-voter rule in the manuscript, which scores Φ_MIP = 0 on the pinned line, is a separate model.

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

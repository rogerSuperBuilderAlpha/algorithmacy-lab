# Independent GitHub-side chronology check — Q221 four-node study

**2026-10-15. Read-only audit of remote GitHub evidence, independent of the executing agent's local file timestamps.** This note documents chronology; it does not certify every scientific assumption or independently rerun the 4-node study.

| Event | GitHub timestamp (UTC) | Eastern daylight time | Remote evidence |
|---|---|---|---|
| Four-node preregistration commit `2ad11e69dfab4793a4ce1978e69730495cec6a4d` | 21:56:20 | 17:56:20 ET | [commit](https://github.com/wwk5q8z6kk-bit/algorithmacy-lab/commit/2ad11e69dfab4793a4ce1978e69730495cec6a4d) |
| GitHub Actions pull-request workflow created for **that exact prereg commit** | **21:56:30** | **17:56:30 ET** | [run 38813598454](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/actions/runs/38813598454) |
| Exact screen script commit `89118627d747d7bb896c8c61fc82c99457363aa1` | 21:57:05 | 17:57:05 ET | [commit](https://github.com/wwk5q8z6kk-bit/algorithmacy-lab/commit/89118627d747d7bb896c8c61fc82c99457363aa1) |
| Frozen study script / screen-results commit `11d34a7c429b6e24c3713a733eb8cbe4c8b626b3` | 21:57:53 | 17:57:53 ET | [commit](https://github.com/wwk5q8z6kk-bit/algorithmacy-lab/commit/11d34a7c429b6e24c3713a733eb8cbe4c8b626b3) |
| Study-run start reported by local execution receipt | 21:57:53 | 17:57:53 ET | `confirmatory_4node/RESULTS.md` and `DEVIATIONS.md` |

**Why this matters:** The GitHub Actions record shows that the preregistration commit had reached the **upstream GitHub platform** by 17:56:30 ET—before the study code commit and reported study execution. This is stronger provenance evidence than relying exclusively on local file creation timestamps or Git author dates. The workflow for the prereg commit was subsequently cancelled as later commits superseded it; the cancellation does **not** negate the remote-timing receipt.

**Boundary:** The study retains its recorded D1–D3 deviations (including smoke-test size ambiguity and exploratory post-hoc TE diagnostics). Timing evidence confirms remote publication order but does not itself establish randomization correctness, independence of statistical units, generalization, or scientific novelty. The latter remain governed by `PREREGISTRATION.md`, `DEVIATIONS.md`, `RESULTS.md`, and the independent record-consistency audit.

**Assessment:** Remote preregistration before the main outcome-producing execution is independently supported. Do not describe the full Q221 PR as preregistered: only the explicitly registered four-node target-A component and any separately registered follow-up have that chronology.

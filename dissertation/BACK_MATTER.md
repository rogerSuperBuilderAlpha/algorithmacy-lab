<!-- Back matter of the dissertation. Follows Chapter 5. -->

# Back Matter

## References

**Reference handling: per chapter.** This dissertation uses **per-chapter reference lists**, the standard
practice for a manuscript-style (three-paper) dissertation in which each paper must also stand alone. Each
of the three papers carries its own complete, citation-integrity-verified bibliography within its chapter:

- **Chapter 2 (Paper 1)** — "Consolidated bibliography" (the integrative review's full reference list).
- **Chapter 3 (Paper 2)** — "References" (31 entries; every in-text cite verified, no orphans).
- **Chapter 4 (Paper 3)** — "References" (23 entries; every in-text cite verified, no orphans).

The two **framing chapters** cite sparingly, and every framing-chapter citation also appears in the papers'
bibliographies. For completeness, the framing chapters' references are:

> Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P.,
> Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., &
> Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal
> existence in physical terms. *PLOS Computational Biology, 19*(10), e1011465.
> https://doi.org/10.1371/journal.pcbi.1011465
>
> Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
> consciousness: Integrated Information Theory 3.0. *PLOS Computational Biology, 10*(5), e1003588.
> https://doi.org/10.1371/journal.pcbi.1003588

*(If Bentley's format rules require a single consolidated reference list, the three per-chapter lists merge
by author surname with duplicates resolved; the two framing-chapter sources above are already contained in
the Chapter 3 and Chapter 4 lists, so the merge adds no new entries.)*

---

## Appendix A. Computational artifacts and reproducibility

Papers 2 and 3 compute every reported Φ value rather than asserting it, and the computations reproduce
end to end from the public repository. The instrument and the analysis scripts are listed below.

**Environment.** Exact IIT-4.0 Φ via PyPhi (Mayner et al., 2018), Python at
`~/iit-playground/venv-4.0/bin/python`. The Φ oracle is the repository's `proxy_audit.exact_phi`
(`exact_big_phi`, `reachable_states`), validated in earlier work in this repository and reused unchanged.

**The instrument and the worked examples (Chapter 3, Paper 2).**

| Artifact | What it computes |
|---|---|
| `dissertation/paper2_construct/phi_instrument.py` | the Worker–System–Counterpart application-layer instrument; exact IIT-4.0 system Φ over the MIP; the two validation controls (factoring → Φ = 0; irreducible → Φ > 0) |
| `dissertation/paper2_construct/worked_examples.py` | the dyadic limit (Φ = 0), the irreducible triad (Φ = 2.0), the false triad (Φ = 0), the false dyad (Φ = 2.0), and the eliminate-the-dyad sweep (2.0 → 0.83 → 0.0) |

**The empirical model and calibration (Chapter 4, Paper 3).**

| Artifact | What it computes |
|---|---|
| `dissertation/paper3_baseline/typology_phi.py` | Stage 2 — the typology of organizations modeled as application-layer systems; Φ per organization (the five structural levels); the human-mediated contrast class. Uses no data. |
| `dissertation/paper3_baseline/anchor_chicago.py` | Stage 1 — the calibration anchor; Φ by pool size; the Φ-versus-outcome correlations. `--refresh` re-pulls the live sample. |
| `dissertation/paper3_baseline/robustness_anchor.py` | the robustness battery — temporal stability, the within-stratum (Simpson's) check, alternative aggregations, the trip-level effect size, and the power note. |

**Data.** The calibration anchor uses the City of Chicago open dataset "Transportation Network Providers —
Trips (2018–2022)," Socrata resource `m6dm-c72p`, queried through the bounded requests documented in
`anchor_chicago.py` and `robustness_anchor.py`. The dataset is public; no credentials are required. Raw
bulk data is not redistributed in the repository; the per-pool-size aggregates needed to reproduce the
reported numbers offline are embedded in `anchor_chicago.py`.

**Reproduce the computed results.**

```
# Chapter 3 (Paper 2): instrument controls + worked examples
~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/phi_instrument.py
~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/worked_examples.py

# Chapter 4 (Paper 3): typology, calibration anchor, robustness battery
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/typology_phi.py
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/anchor_chicago.py        # add --refresh for live data
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/robustness_anchor.py     # needs network
```

---

## Appendix B. Note on the construct term *competency*

Chapter 2 (Paper 1) carries a footnote on its first use of *competency*: the construct is called a
*competency* throughout to keep it legible to the literatures it must be distinguished from and to the
construct-clarity and measurement program the later papers build on it, while flagging that *sensibility*
may be the better long-run name for a capacity exercised under opacity and constant change. The term is
retained across all three papers for consistency. This is noted here so the choice is visible at the
dissertation level, not only within Chapter 2.

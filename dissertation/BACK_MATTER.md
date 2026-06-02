<!-- Back matter of the dissertation. Follows Chapter 5. -->

# Back Matter

## References

**Reference handling: per chapter.** This dissertation uses **per-chapter reference lists**, the standard
practice for a manuscript-style (three-paper) dissertation in which each paper must also stand alone. Each
of the three papers carries its own complete, citation-integrity-verified bibliography within its chapter:

- **Chapter 2 (Paper 1)** — "Consolidated bibliography" (the integrative review's full reference list).
- **Chapter 3 (Paper 2)** — "References" (44 entries; every in-text cite verified, no orphans).
- **Chapter 4 (Paper 3)** — "References" (21 entries; every in-text cite verified, no orphans).

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
| `dissertation/paper2_construct/worked_examples.py` | the dyadic limit (Φ = 0), the irreducible triad under bottleneck reads (Φ = 2.0), the same triad under realistic-feedback reads (Φ = 0), the false triad (Φ = 0), and the false dyad (Φ = 2.0) |
| `dissertation/paper2_construct/eliminate_dyad_sweep.py` | the encoding-robustness of the "eliminate-the-dyad" result: the magnitude is non-monotone (no channel 2.0; disjunctive 0.83; conjunctive 6.0; full bypass 0.0), so only the binary endpoint result is claimed |
| `dissertation/paper2_construct/read_structure_sweep.py` | Φ across read structures with the joint determination fixed: only 22% keep Φ > 0, so a joint determination is necessary but not sufficient (the realistic-feedback reads collapse to 0) |
| `dissertation/paper2_construct/party_partition.py` | Φ over the complete {W}{S}{C} cut vs the MIP: the complete cut over-calls (positive even for dyads), so the binary verdict is Φ over the minimum-information partition |
| `dissertation/paper2_construct/phi_vs_separability.py` | the binary Φ verdict vs a cheap *static* factorization/connectivity test over all 4,096 triads: agreement only 57.8%, 1,728 connected-but-Φ=0 forms, 0 reverses |
| `dissertation/paper2_construct/dynamical_comparator.py` | the binary Φ verdict vs *dynamical* conditional-independence tests (all-combinations 59.6%/0-reverse; fair reachable-only 89.8%/8-reverse — aggregate is comparator-dependent). The robust result is the verified EXHIBIT: `W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S)` (6/6 edges, no constants) has Φ=0 though every cheap test calls it triadic — the apparatus is not decorative |

**The model family and typology (Chapter 4, Paper 3).** All compute exact Φ and use no outside data.

| Artifact | What it computes |
|---|---|
| `dissertation/paper3_baseline/catalog.py` | the complete W–S–C model family — all 16³ = 4,096 three-node wirings plus a 48-wiring higher-order family; exact Φ for each, with structural features; writes `results/catalog.csv`. |
| `dissertation/paper3_baseline/analyze_catalog.py` | the Φ landscape (the discrete bands), the feature→Φ regression (R² = 0.20), and Figure 4.1 (`results/catalog_landscape.png`). |
| `dissertation/paper3_baseline/simulated_orgs.py` | the parametric population of 86 simulated organizations (n = 3–5; mediation regime × determination × back-channel); exact Φ for each; writes `results/simulated_orgs.csv`. |
| `dissertation/paper3_baseline/analyze_simulated.py` | the population Φ distribution, the OR-determination magnitude pathology, the placement of the named organizations (`results/simulated_orgs.png`), a **full-rank OLS + standard errors** (the naive design is rank-deficient: regime=partial aliased with the back-channel count, so only the determination function is significant), and the regime-by-n stratified table. |
| `dissertation/paper3_baseline/typology_phi.py` | the typology of named organizations modeled as application-layer systems; Φ per organization (the five bands); the human-mediated contrast class. |
| `dissertation/paper3_baseline/typology_sensitivity.py` | how each placement moves under alternative determination codings (regime fixed): strict n=3 robust at 2.0 (4/5 codings), partial fragile (OR → 6.0); court=platform is by construction. |
| `dissertation/paper3_baseline/experiment/sim/coordination_sim.py`, `experiment/analyze.py` | the structure-axis test — an agent-based coordination **consistency check** (frozen a-priori agent rule; agents never see Φ, but Φ and difficulty share a structural cause, so it is a consistency check, not an independent validation); strict mediation harder (0.72 vs 0.95, Cohen's d ≈ 50), parity anomalous; robust at 3,000 rounds (`results/sim_runs.csv`, `sim_runs_3000.csv`). |

**Data.** The dissertation's claims use no outside data: every reported Φ value is computed from the model.
An exploratory analysis against the City of Chicago "Transportation Network Providers — Trips" dataset
(Socrata resource `m6dm-c72p`) was **cut from the dissertation** because, in the pooling model, Φ is a
linear function of pool size and so the analysis validated only the party-count axis of the score. Its
scripts (`anchor_chicago.py`, `robustness_anchor.py`) are retained, clearly labeled as outside the
dissertation's claims, in `paper3_baseline/exploratory/` as a template for the structure-varying validation
the model would actually require. Their numbers are not cited anywhere in the dissertation. The design of the
validation that *would* license a claim about the world — varying determination structure at a fixed party
count against an independently measured coordination outcome, with blind inter-rater structural coding — is
specified in `paper3_baseline/VALIDATION_PROTOCOL.md`; it is named as the program's next arc, not executed
here.

**Reproduce the computed results.**

```
# Chapter 3 (Paper 2): model controls + worked examples
~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/phi_instrument.py
~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/worked_examples.py

# Chapter 4 (Paper 3): the model family + the typology (no outside data)
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/catalog.py
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/analyze_catalog.py
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/typology_phi.py
```

---

## Appendix B. Note on the construct term *competency*

Chapter 2 (Paper 1) carries a footnote on its first use of *competency*: the construct is called a
*competency* throughout to keep it legible to the literatures it must be distinguished from and to the
construct-clarity and measurement program the later papers build on it, while flagging that *sensibility*
may be the better long-run name for a capacity exercised under opacity and constant change. The term is
retained across all three papers for consistency. This is noted here so the choice is visible at the
dissertation level, not only within Chapter 2.

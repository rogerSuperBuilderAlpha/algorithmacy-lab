<!-- Back matter of the dissertation. Follows Chapter 5. -->

# Back Matter

## References

**Reference handling: per chapter.** This dissertation uses **per-chapter reference lists**, the standard
practice for a manuscript-style (three-paper) dissertation in which each paper must also stand alone. Each
of the three papers carries its own complete, citation-integrity-verified bibliography within its chapter:

- **Chapter 2 (Paper 1)** — "Consolidated bibliography" (the integrative review's full reference list).
- **Chapter 3 (Paper 2)** — "References" (37 entries; every in-text cite verified, no orphans; the prior-work and adjacent-measure clusters added to §2 and §8 are verified against Crossref, per the chapter's bibliography note).
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
`~/iit-playground/venv-4.0/bin/python`. The Φ oracle is PyPhi 4.0's system-integrated-information
routine (`new_big_phi.sia`), the IIT-4.0 system measure over the minimum-information partition. Paper 3's
`phi_core.py` re-derives the computation from scratch, depending only on PyPhi, and reproduces Paper 2's
controls exactly at n = 3 (factoring 0.000; irreducible 0.830; strict mediation 2.000), which is the
cross-check that keeps the measure identical across the two computational chapters.

**The instrument and the worked examples (Chapter 3, Paper 2).**

| Artifact | What it computes |
|---|---|
| `dissertation/paper2_construct/rebuild/instrument.py` | the Worker–System–Counterpart application-layer instrument; exact IIT-4.0 system Φ over the MIP; the two validation controls (factoring → Φ = 0; irreducible → max Φ = 0.830) |
| `dissertation/paper2_construct/rebuild/worked_examples.py` | the dyadic limit (Φ = 0), the applicant-tracking triad (Φ = 2.0 for AND-family, 0.5 for parity, 0 when one party drops out), and the false dyad: rideshare triad (Φ = 2.0) vs its one-edge dyadic twin (Φ = 0) |
| `dissertation/paper2_construct/rebuild/sweeps.py` | the read sweep with the joint determination fixed (only 12.5% of reads, 32 of 256, keep Φ > 0, so a joint determination is necessary but not sufficient) and the "eliminate-the-dyad" sweep (magnitude non-monotone — no channel 2.0; disjunctive 0.83; conjunctive 6.0; parity 2.0; full bypass 0.0 — so only the binary endpoint result is claimed) |
| `dissertation/paper2_construct/rebuild/why_phi.py` | the verified EXHIBIT: `W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S)` (6/6 edges, no constants, strongly connected) has Φ = 0 at every reachable state though every cheap connectivity/factorization test calls it triadic — the apparatus is not decorative |
| `dissertation/paper2_construct/rebuild/review_response.py` | the carving-stability check (the rideshare verdict holds across faithful re-encodings; two flips break a named criterion condition), the per-state Φ profiles, the noise-robustness of the carrying state (2.0 → 1.90 → 1.75 → 1.53 at 0/2/5/10% mixing), and the effective-information contrast (EI does not order the dyad–triad line; the exhibit has EI = 2.0 while Φ = 0) |
| `dissertation/paper2_construct/rebuild/synergy_check.py` | the ΦID synergy comparison (§8): the revised whole-minus-sum integrated information Φ_R (CCS redundancy, min over bipartitions, via `phyid`) over-calls the EXHIBIT (Φ_R ≈ 0.14–0.21 across 5–20% noise) while exact IIT-4.0 Φ of the same noised matrix stays 0 — and reads 0 on the factoring control, positive on the irreducible control, so the over-call is specific to the hard case. Depends on `phyid` and the repo's `proxy_audit` trajectory simulator. |
| `dissertation/paper2_construct/rebuild/geometric_check.py` | the information-geometric Φ comparison (§8): the exact min-KL-to-disconnected-model geometric Φ (Oizumi-family, min over bipartitions) over-calls the EXHIBIT (Φ_G = 1.56 under uniform input, 0.50 over reachable states) while exact IIT-4.0 Φ = 0 — and reads 0 on the factoring control, positive on the irreducible control and strict mediation. Exact (no estimation); depends only on PyPhi 4.0 and numpy. |
| `dissertation/paper2_construct/rebuild/exhibit_class.py` | the generalization (§8): buckets all 4,096 wirings by strong-connectivity × exact Φ and shows geometric Φ over-calls the *entire* strongly-connected-yet-reducible class (the exhibit's class), reads ~0 on the simple dyads, and positive on the genuine triads — so the exhibit is representative, not cherry-picked. |

**The model family and typology (Chapter 4, Paper 3).** All compute exact Φ and use no outside data.

| Artifact | What it computes |
|---|---|
| `dissertation/paper3_baseline/rebuild/phi_core.py` | the Φ measure, re-derived from scratch and depending only on PyPhi, generalized to arbitrary node count; reproduces Paper 2's controls exactly at n = 3. |
| `dissertation/paper3_baseline/rebuild/catalog.py` | the complete W–S–C model family — all 16³ = 4,096 three-node wirings plus a 48-wiring higher-order sample (4,144 in all, no duplicates); exact Φ for each, with structural features; writes `results/catalog.csv`. |
| `dissertation/paper3_baseline/rebuild/analyze_catalog.py` | the Φ landscape (44.1% reducible; seven discrete non-zero bands), the feature→Φ regression (R² = 0.196), and Figure 4.1 (`results/catalog_landscape.png`). |
| `dissertation/paper3_baseline/rebuild/typology.py` | the typology of named organization archetypes modeled as application-layer systems; Φ per archetype on the populated bands (0, 0.50, 0.83, 2.00, 3.00). |
| `dissertation/paper3_baseline/rebuild/cases.py` | the five corporate cases, each pre-registered from its documented mechanism: Uber 2.00 and NYSE/Nasdaq 2.00 (strict mediation); Upwork 0.83 and ManpowerGroup 0.83 (partial mediation); Amazon Mechanical Turk raw 3.00 (higher-order strict, Φ/(n−1) = 1.00). |
| `dissertation/paper3_baseline/rebuild/dyadic_cases.py` | the dyadic negative-control class (prediction Φ = 0 fixed in advance): three forms come up dyadic (phone call, email, worker-at-tool); two do not (payment processor 0.83, classified board 1.00) — both findings, since the instrument tracks the coded mechanism, not a casual dyad intuition. |
| `dissertation/paper3_baseline/rebuild/micro_scenarios.py` | the 103-activity micro-catalog, each coded from its mechanism and scored, illustrating that surface-distinct activities land on the same few structural bands; writes `MICRO_SCENARIOS.md`. |
| `dissertation/paper3_baseline/rebuild/review_response.py` | the figures answering the adversarial review: the 16/40 strict-mediation forms that reach 2.00 (a checklist would mis-score 24 of 40), the parity-mediator anomaly (mean Φ 0.85 > monotone 0.535), the n−1 size identity for strict-AND mediation, and the per-case sensitivity codings. |

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
~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/instrument.py
~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/worked_examples.py

# Chapter 4 (Paper 3): the model family, the typology, and the five cases (no outside data)
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/catalog.py
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/analyze_catalog.py
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/typology.py
~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/cases.py
```

---

## Appendix B. Note on the construct term *competency*

Chapter 2 (Paper 1) carries a footnote on its first use of *competency*: the construct is called a
*competency* throughout to keep it legible to the literatures it must be distinguished from and to the
construct-clarity and measurement program the later papers build on it, while flagging that *sensibility*
may be the better long-run name for a capacity exercised under opacity and constant change. The term is
retained across all three papers for consistency. This is noted here so the choice is visible at the
dissertation level, not only within Chapter 2.

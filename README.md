# iit-experiments

Small, reproducible computational experiments in Integrated Information Theory,
built on the [PyPhi](https://github.com/wmayner/pyphi) IIT‑4.0 implementation.

**→ Start with [`SYNTHESIS.md`](SYNTHESIS.md)** for the connected story across all
six experiments, or the short preprint‑style writeup in
[`paper/manuscript.md`](paper/manuscript.md). In one line: *no single cheap number
is integrated information, but the information needed to recover it is distributed
across several cheap signals — and the closer a measure's structure is to IIT's
own "whole‑minus‑parts" move, the more of that information it carries.*

For the reusable method behind these studies — how to go from a recent paper to a
defensible, reproducible contribution — see [`RESEARCH_PLAYBOOK.md`](RESEARCH_PLAYBOOK.md).

## Experiments

### [`proxy_audit/`](proxy_audit/) — Do cheap proxies track exact IIT‑4.0 Φ?

Motivated by [Barrett et al. (2026), *IIT: the good, the bad and the
misunderstood*](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/),
which observes that the quantities computed on real data (Lempel‑Ziv complexity,
correlation measures, PCI) are **proxies for** integrated information that have
never been validated against the Φ that IIT actually defines.

We run that validation on systems small enough to compute exact Φ: 270 random
Boolean networks, exact IIT‑4.0 Φ via PyPhi, versus five cheap proxies.

**Headline:** no proxy reliably tracks Φ. Total correlation *anti*‑correlates
(Spearman ρ = −0.36); Lempel‑Ziv complexity is near chance; the best detector of
"is the system integrated at all?" is a trivial edge count. The proxy↔Φ
relationship is non‑monotonic and even sign‑flips between detecting and grading
integration. See [`proxy_audit/FINDINGS.md`](proxy_audit/FINDINGS.md).

![proxies vs phi](proxy_audit/results/proxy_vs_phi.png)

### [`candidate_audit/`](candidate_audit/) — Do the published *candidate Φ measures* track exact IIT‑4.0 Φ?

A companion to the proxy audit. Where that one tests *empirical* proxies, this
tests the *theoretically motivated* candidate measures from the
[Mediano–Seth–Barrett (2019)](https://www.mdpi.com/1099-4300/21/5/525) and
Mediano–Rosas ΦID lineage (Φ whole‑minus‑sum, stochastic interaction, causal
density, integrated synergy/co‑information, …) — comparing them, for the first
time, against **exact IIT‑4.0 Φ** on the same 270 networks.

**Headline:** the theoretical measures track Φ markedly better than the
empirical proxies, but only moderately. **Φ whole‑minus‑sum** leads (ρ = 0.47,
AUC 0.79) and improves with system size; integrated synergy is second. Measures
of mere statistical dependence (total correlation, time‑delayed MI)
*anti*‑correlate. The measures sharing IIT's "whole‑minus‑parts" structure are
the ones that track it. See [`candidate_audit/FINDINGS.md`](candidate_audit/FINDINGS.md).

![candidate measures vs phi](candidate_audit/results/candidate_vs_phi.png)

### [`structure_suite/`](structure_suite/) — Is scalar Φ an impoverished summary?

[Barrett et al. (2026)](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/)
propose replacing the single number Φ with a *suite* of quantities. This
experiment takes that literally: it extracts the full IIT‑4.0 Φ‑structure
(distinctions, relations, composition) for 372 `(network, state)` pairs and asks
what the suite captures that scalar Φ discards.

**Headline:** scalar Φ is **nearly orthogonal** to every structural dimension it
summarizes (ρ = 0.07–0.21). Reducible systems (Φ = 0) still have rich structure
— *all* of them have ≥1 distinction. The suite has ~3 independent axes (Φ;
structural size; composition); Φ is only one. Direct support for the
multi‑dimensional view. See [`structure_suite/FINDINGS.md`](structure_suite/FINDINGS.md).

![phi-structure correlations](structure_suite/results/suite_corr.png)

### [`learned_surrogate/`](learned_surrogate/) — Can cheap features *together* predict Φ?

The constructive flip side of the two audits: no *single* cheap measure tracks
Φ, so can a model that **combines** them? Also publishes a reusable
**exact‑IIT‑4.0 feature dataset** (720 networks) — the 4.0 ground truth that
surrogate work like [Hosaka et al. (2025)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335966)
(IIT 3.0, no PyPhi) lacks.

**Headline:** combining cheap features beats any single one. Out‑of‑fold, a
random forest lifts Φ‑prediction from ρ = 0.32 (best single) to **0.54**, and
**detection of Φ > 0 from AUC 0.69 to 0.90**. `Φ_WMS` carries most of the signal.
Detecting *whether* a system is integrated is quite doable from cheap features;
predicting *how much* remains only moderate. See [`learned_surrogate/FINDINGS.md`](learned_surrogate/FINDINGS.md).

![learned surrogate](learned_surrogate/results/surrogate.png)

### [`emergence_vs_phi/`](emergence_vs_phi/) — Causal emergence vs IIT Φ

Two information-theoretic accounts of macro-level causal power, head to head:
[Hoel](https://www.mdpi.com/1099-4300/19/5/188)'s **effective information /
causal emergence** vs IIT **Φ**, on the same small (n=3) systems, with the
emergence search done exactly (all state coarse-grainings).

**Headline:** they're **nearly orthogonal** (ρ = 0.02), and the *most integrated*
systems show *no* causal emergence — emergence rewards degeneracy
(coarse-graining recovers determinism), while Φ rewards irreducibility. Effective
information does track Φ, but only *among already-integrated systems* (ρ = 0.77).
See [`emergence_vs_phi/FINDINGS.md`](emergence_vs_phi/FINDINGS.md).

![emergence vs phi](emergence_vs_phi/results/emergence_vs_phi.png)

### [`phiid_vs_phi/`](phiid_vs_phi/) — Does ΦID-based Φ (estimated from data) track exact Φ?

The candidate audit measured the whole-minus-sum family *exactly* from the TPM.
But on real data, integrated information is *estimated* from a finite time series
via Integrated Information Decomposition. This experiment computes the revised
Φ_R (with **CCS** redundancy, since MMI assigns spurious synergy to independent
variables) from simulated trajectories using the
[`phyid`](https://github.com/Imperial-MIND-lab/integrated-info-decomp) package —
bridging the two projects this repo contributes to (PyPhi + phyid).

**Headline:** there's a large **estimation gap**. On the same networks, exact
Φ_WMS tracks Φ at ρ = 0.28 (AUC 0.67); the data-style ΦID Φ_R **roughly halves
that** (ρ = 0.12, AUC 0.56). Exact and estimated agree at ρ = 0.64 — it's the
same quantity, degraded by finite-sample estimation and coarse-graining. The
measure is validated on controls first (independent → 0, redundant → 0,
integrated → high). See [`phiid_vs_phi/FINDINGS.md`](phiid_vs_phi/FINDINGS.md).

![phiid vs phi](phiid_vs_phi/results/phiid_vs_phi.png)

### [`consciousness_range/`](consciousness_range/) — does "level of consciousness" capture the mind? *(philosophical companion)*

The six experiments above ask *what tracks Φ*. This one flips it: **assume IIT is
true** — the Φ-structure *is* the experience — then build a bestiary of minds
spanning low→high Φ and different structural characters, and ask whether the
scalar "level of consciousness" captures the mind.

**Headline:** it does not. Three systems with **identical Φ = 0.415** have
cause-effect structures spanning **59 to 32 764 relations** (555×) — same level,
radically different minds. Across the bestiary Φ and structural richness
*anti*-correlate (the highest-Φ mind has one of the sparsest structures), and the
*composition* differs in kind (one mind has no first-order distinctions at all).
On IIT's own terms, a one-number consciousness scale discards almost everything
that makes a mind what it is. See [`consciousness_range/FINDINGS.md`](consciousness_range/FINDINGS.md).

![range of minds](consciousness_range/results/range_of_minds.png)

## Setup

Requires Python ≥ 3.10 and PyPhi's IIT‑4.0 line.

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# (PyPhi 4.0 currently installs from the feature/iit-4.0 branch:
#  pip install "pyphi @ git+https://github.com/wmayner/pyphi@feature/iit-4.0")
```

Then, from the repo root:

```bash
python -m proxy_audit.run 15 1      # run the audit
python -m proxy_audit.analyze       # correlations, summary, plot
```

## License

MIT — see [LICENSE](LICENSE).

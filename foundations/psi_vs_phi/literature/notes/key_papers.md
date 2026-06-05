# Ingestion notes — core papers

Concise notes on the load-bearing papers for the literature review, grouped by cluster. The
anchor paper has its own detailed note (`kearney2026_maxcal.md`); the full landscape is in
`../deep_research_report.md`; citations in `../references.bib`. "OA" = open access (PDF in
`../pdfs/`); "paywalled" = note + DOI only.

---

## IIT

**Oizumi, Albantakis & Tononi (2014) — IIT 3.0** [PLOS, OA → `oizumi2014_iit3.pdf`]
Five axioms (existence, composition, information, integration, exclusion) → mechanistic
postulates. Mechanisms specify **cause/effect repertoires** (distributions over prior/next states)
scored by earth-mover's distance vs an unconstrained baseline; Φ via the **minimum information
partition (MIP)**; complexes = local maxima. *Relevance:* this is exactly the repertoire calculus
Kearney re-derives from MaxCal/CMEP. The version his derivation targets.

**Albantakis et al. (2023) — IIT 4.0** [PLOS/arXiv 2212.14787, OA → `albantakis2023_iit4.pdf`]
Current canonical formalism. Unique **Intrinsic Difference (ID)** measure (replacing EMD); fully
unfolds the cause-effect structure into **distinctions + relations**. *Relevance:* this is the
exact Φ our oracle computes (PyPhi `new_big_phi`) and what ψ must be validated against. **Key
mismatch:** Kearney re-derives 3.0 (EMD) repertoires; canonical Φ is now 4.0 (ID) — a nuance our
Tier A must handle.

**Mediano, Rosas, Bor, Seth & Barrett (2022) — strength of weak IIT** [TiCS, paywalled]
Splits **strong IIT** (consciousness ≡ maxima of integrated info; universal Φ) from **weak IIT**
(pragmatic info-dynamics correlates). Existing empirical support is well-explained by weak IIT.
*Relevance:* determines *which* Φ ψ should be tested against — the contested canonical Φ vs proxies.

**Doerig et al. (2019) — the unfolding argument** [Conscious Cogn, paywalled] &
**Hanson & Walker (2021) — formalizing falsification** [Neurosci Conscious, OA → `hanson2021_falsification.pdf`]
Causal-structure theories: feedforward never conscious, recurrent can be. Hanson–Walker: IIT is
"simultaneously falsified at the finite-state-automaton level and unfalsifiable at the
combinatorial-state-automaton level." *Relevance:* the validation *target* (Φ) is itself contested
— context for what a ψ↔Φ test does and doesn't settle. (Both contested by IIT proponents; the
deep-research verifier **killed** the strongest readings of the unfolding argument as overclaims.)

## Free Energy Principle / active inference

**Friston (2010) — FEP unified brain theory** [Nat Rev Neurosci, paywalled]
Self-organizing systems minimize **free energy**, an upper bound on **surprise** (≈ prediction
error). *Relevance:* the FEP quantity Kearney equates ψ with in the appropriate limits.

**Friston (2019) — FEP for a particular physics** [arXiv 1906.10184, OA → `friston2019_particular_physics.pdf`]
FEP for anything individuated by a **Markov blanket**; path-integral/least-action formulation over
trajectories. *Relevance:* the trajectory framing is the meeting point with MaxCal path ensembles.

**Ramstead et al. (2023) — On Bayesian Mechanics** [Interface Focus/arXiv 2205.11543, OA → `ramstead2023_bayesian_mechanics.pdf`]
Proves a **duality between the FEP and the constrained maximum-entropy principle** (asymptotic,
under NESS/Markov-blanket). *Relevance:* **the theoretical foundation** that makes Kearney's
MaxCal→FEP bridge coherent — but it's a system-level free-energy↔entropy duality, with **no obvious
analogue of Φ's exclusion/MIP/maximization** (a reason ψ might *not* track Φ).

## Maximum caliber / MaxEnt / path ensembles

**Pressé, Ghosh, Lee & Dill (2013)** [Rev Mod Phys, paywalled] &
**Dixit et al. (2018) — MaxCal a general variational principle** [J Chem Phys/arXiv 1711.03450, OA → `dixit2018_maxcal.pdf`]
MaxCal = dynamical generalization of MaxEnt: maximize **path entropy over trajectories** subject to
dynamical constraints. *Relevance:* the exact machinery defining ψ (and κ, the path partition).

**Burda et al. (2009) — Localization of the Maximal Entropy Random Walk** [PRL/arXiv 0810.4113, OA → `burda2009_merw.pdf`]
MERW vs generic random walks; heterogeneity drives their divergence (localization). *Relevance:*
Kearney's empirical ψ analysis builds on MERW; **ψ ≡ 0 when MERW = GRW** is one of our validation
controls.

## Predictive coding / Bayesian surprise

**Itti & Baldi (2009) — Bayesian surprise attracts attention** [Vision Research, OA → `itti2009_surprise.pdf`]
Surprise = KL(posterior‖prior); 72–84% of saccades target above-average-surprise locations.
*Relevance:* a concrete **template for falsifiable validation of a KL-type measure** against data —
the kind of test ψ currently lacks; grounds the ψ↔Bayesian-surprise link.

## IIT–FEP unification (prior attempts)

**Safron (2020) — IWMT** [Frontiers AI, OA → `safron2020_iwmt.pdf`] — conceptual unification of
IIT + GNWT + FEP. **Olesen & Waade (2023) — Φ fluctuates with surprisal** [PLOS, OA →
`olesen2023_phi_surprisal.pdf`] — empirical pre-study correlating Φ and surprisal. **Mayama et al.
(2025)** [arXiv 2510.04084, OA → `mayama2025_iit_fep.pdf`] — IIT↔FEP in living neuronal cultures;
the "hill-shaped Φ trajectory." **INTREPID (2026)** [arXiv 2509.00555, OA → `intrepid2026_review.pdf`]
— adversarial collaborative review. *Common thread:* conceptual/empirical, **no rigorous
mathematical mapping** — the gap Kearney's derivation targets, and none compute ψ vs exact Φ.

## Φ validation / proxies / critiques

**Barrett et al. (2026) — the good, the bad and the misunderstood** [arXiv 2604.11482, OA → `barrett2026_goodbad.pdf`]
Φ never computed on a real system; only *proxies*, never validated against Φ; replace Φ with a
*suite*. *Relevance:* the critique our whole `algorithmacy-lab` program (and this ψ↔Φ test) responds to.

**Mediano, Seth & Barrett (2019) — comparing candidate measures** [Entropy 21(1):17, OA; PDF
bot-blocked, DOI 10.3390/e21010017] — the practical candidate-Φ measures (Φ_WMS, Φ*, …) we audited.
**Tegmark (2016) — improved measures** [PLOS/arXiv 1601.02626, OA → `tegmark2016_improved.pdf`].
**Casali et al. (2013) — PCI** [Sci Transl Med, paywalled] — the clinical Lempel-Ziv proxy.
*Relevance:* ψ is the **next candidate measure** to put through this validation lineage — and the
one whose author explicitly requested the test.

## Thermodynamics / complexity

**Tononi, Sporns & Edelman (1994) — neural complexity** [PNAS, OA, DOI 10.1073/pnas.91.11.5033] —
the segregation/integration measure ancestral to Φ; situates ψ-as-complexity vs Φ-as-integration.

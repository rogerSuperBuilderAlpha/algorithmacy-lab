# How the world uses PyPhi — a usage survey

> **Update:** a deeper multi-database sweep is in [`social_systems_dossier.md`](social_systems_dossier.md).
> It confirms the white-space (no exact Φ on any human coordination system) and adds the key
> precedent — Niizato et al. (2020) on fish schools, with a Φ discontinuity at group size four that
> mutual information and transfer entropy miss — plus the two estimated-Φ social studies (Engel &
> Malone 2018; Watson et al. 2025/2026) and the clean ΦID gap. Probes 44–48 engage it directly.


Deep-research run, June 2026. Five search angles, 21 primary sources fetched, 102 claims
extracted, 25 verified by 3-vote adversarial check, 25 confirmed and 0 killed. Nine
high-confidence findings survive synthesis. Every load-bearing source is peer-reviewed (PLOS,
Nature/Scientific Reports, MDPI Entropy) or the official repository. No blog or forum source is
load-bearing.

The question: who uses PyPhi, on what systems, with what tools, against what limits, and where is
the open application gap — with organizational and social systems flagged.

---

## 1. What PyPhi is

PyPhi is the Tononi-lab Python reference implementation of Integrated Information Theory. It
computes exact integrated information Φ and unfolds the full cause-effect structure of a discrete
dynamical system of binary elements. The 2018 PLOS Computational Biology paper describes it as "an
up-to-date reference implementation of the formalisms of integrated information theory"
[Mayner 2018]. Authors are Mayner, Marshall, Albantakis, Findlay, Marchman, and Tononi, all at
Wisconsin-Madison. GPLv3, pip-installable.

Two version facts matter. The canonical formulation is now IIT 4.0 [Albantakis 2023], which recasts
the axioms as postulates with explicit mathematical expressions and introduces the Intrinsic
Difference measure. PyPhi tracks 4.0 on a dedicated `feature/iit-4.0` branch while the stable
README and a `pyphi_config_3.0.yml` still carry IIT 3.0. The 3.0-versus-4.0 split is a live tooling
condition, not a settled past. A 2021 extension by the same group added support for multi-valued
elements (ternary, quaternary, mixed), demonstrated on random networks and a small biological
regulatory model [Gomez 2021].

## 2. What people compute Φ on

Three system classes dominate.

**Artificial life and simulated agents.** The canonical use is "animats" — small evolved
controllers of about eight binary elements (two sensors, four hidden, two motors) built from
deterministic logic gates or Hidden Markov gates, navigating mazes [Albantakis 2014; Edlund 2011].
The four-hidden-element cap is set by exact-Φ intractability, not by biology. The foundational
result of this line is that integrated information rises with fitness across evolution: main-complex
Φ versus fitness at Spearman ρ ≈ 0.94, against ρ ≈ 0.34 for predictive information [Edlund 2011].
That paper predates PyPhi and used IIT 2.0-era lab code, so it is the founding artificial-life
result rather than a PyPhi run.

**Abstract logic-gate and random networks, plus proof-of-concept biology.** Logic-gate networks,
random Boolean networks, XOR systems, and multi-valued random networks are the standard test beds.
The 2021 multi-valued extension applied causal analysis to a p53-Mdm2 regulatory network [Gomez
2021], the clearest reach toward systems biology.

**Real neural data.** On EEG and SEEG across wakefulness, sedation, anesthesia, and seizures,
researchers do not run exact PyPhi. They substitute the tractable autoregressive proxy Φ_AR
[Barrett & Seth 2011] and estimate Φ from many small random channel subsets, reporting only a lower
bound on the true value. A 128-channel EEG would require about 1.8×10^38 bipartitions, so one study
estimated mean Φ from 600 sample-units of eight random channels [Kim 2018]; an SEEG seizure study
states plainly that "our measurements can only be a lower bound on the true Φ values" because the
electrodes cannot represent the whole brain [Sci Rep 2024]. This is the proxy/observability problem.

## 3. The tooling ecosystem

PyPhi sits at the center of a companion ecosystem driven by intractability. Approximation and
estimation methods use PyPhi as the ground-truth engine: heuristic MIP-search, GeoMIP, and graph
neural network estimators that train on exact PyPhi solutions and then predict Φ for larger systems
in seconds [Hosaka 2025; Nilsen 2019]. `pyphi-spectrum` is a published companion package. The
pattern is consistent: exact PyPhi defines the truth, and a surrounding literature tries to
approximate it cheaply.

## 4. The limit everyone hits

Exact Φ is exponential time, O(n^5 · 3^n). The practical ceiling is about 10-12 elements; the
largest systems investigated are 20-30 binary elements [Mayner 2018; Nilsen 2019]. Seven majority
gates took about 2.75 hours on 32 cores [Mayner 2018]. A GNN estimates 1000 seven-node systems in
under two seconds where exact computation needs more than 30 minutes per system [Hosaka 2025]. This
ceiling is intrinsic to exact IIT and indifferent to discipline. It bounds any future application,
including an organizational one.

## 5. The open application gap

Across the surveyed primary sources there is **no application of PyPhi or exact IIT Φ to
organizations, teams, coordination, social systems, institutions, or economic and management
systems.** The repository's own topic tags name modeling, information, neuroscience, causality,
integrated-information, and causation. The built-in examples cover actual causation, emergence by
coarse-graining and black-boxing, and XOR networks — none social or organizational. A full-text
search of the foundational software paper for organization, social, team, coordination, economic,
management, institution, firm, and company returned zero occurrences [Mayner 2018].

The caveat is stated honestly. Absence across this verified set and the official tooling is strong
evidence, but it is not a guaranteed exhaustive census of preprints, conference proceedings, gray
literature, or non-English work. A dedicated Scholar/Semantic Scholar sweep across management and
organization-science venues should harden the negative before any novelty claim is staked. A
related open question: whether IIT-adjacent measures (Φ_AR, ΦID, effective information / causal
emergence) have been applied to social or economic systems even without PyPhi. Such work would
narrow or shift the white space rather than fill it.

The shape of the opening is clear. Applying exact IIT-4.0 Φ to small formal coordination structures
— teams, decision units, governance or communication topologies modeled as discrete dynamical
systems — is feasible only at the 10-12-element exact ceiling, or through the same proxy and
approximation methods (Φ_AR, GNN estimators) that neuroscience already relies on. The modeling
question is the substantive one: what transition probability matrix faithfully represents
organizational coordination, and what do Φ, the major complex, and the cause-effect structure mean
for organization design.

---

## Sources

Open-access status in brackets. All are primary peer-reviewed or the official repository unless
marked otherwise.

1. Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2018). PyPhi: A toolbox
   for integrated information theory. *PLOS Computational Biology* 14(7):e1006343.
   doi:10.1371/journal.pcbi.1006343. arXiv:1712.09644. [OA, PMC6080800]
2. Albantakis L, Barbosa L, Findlay G, Grasso M, Haun AM, Marshall W, Mayner WGP, et al. (2023).
   Integrated information theory (IIT) 4.0. *PLOS Computational Biology* 19(10):e1011465.
   doi:10.1371/journal.pcbi.1011465. arXiv:2212.14787. [OA, CC-BY]
3. Gomez JD, Mayner WGP, Beheler-Amass M, Tononi G, Albantakis L (2021). Computing integrated
   information for multi-valued elements: An update to PyPhi. *Entropy* 23(1):6.
   doi:10.3390/e23010006. [OA, PMC7822016]
4. Albantakis L, Hintze A, Koch C, Adami C, Tononi G (2014). Evolution of integrated causal
   structures in animats exposed to environments of increasing complexity. *PLOS Computational
   Biology* 10(12):e1003966. doi:10.1371/journal.pcbi.1003966. [OA]
5. Edlund JA, Chaumont N, Hintze A, Koch C, Tononi G, Adami C (2011). Integrated information
   increases with fitness in the evolution of animats. *PLOS Computational Biology* 7(10):e1002236.
   doi:10.1371/journal.pcbi.1002236. arXiv:1103.1791. [OA, PMC3197648]
6. Nilsen AS, Juel BE, Marshall W (2019). Evaluating approximations and heuristic measures of
   integrated information. *Entropy* 21(5):525. [OA, PMC7515014]
7. Hosaka R (2025). Graph neural networks for integrated information and major complex estimation.
   *PLOS ONE*. doi:10.1371/journal.pone.0335966. [OA, CC-BY]
8. Kim H, Hudetz AG, Lee J, Mashour GA, Lee U, et al. (2018). Estimating the integrated information
   measure Φ from high-density EEG during states of consciousness. *Frontiers in Human
   Neuroscience*. [OA, PMC5821001]
9. (2024). Consciousness transitions during epilepsy seizures through the lens of integrated
   information theory. *Scientific Reports*. doi:10.1038/s41598-024-56045-x. [OA, PMC10912751]
10. Barrett AB, Seth AK (2011). Practical measures of integrated information for time-series data.
    *PLOS Computational Biology* 7(1):e1001052. [OA] — origin of the Φ_AR proxy.
11. wmayner/pyphi — official repository. https://github.com/wmayner/pyphi
12. elife-asu/pyphi-spectrum — companion package. https://github.com/elife-asu/pyphi-spectrum

### Supporting / context sources fetched

13. Tegmark M (2016). Improved measures of integrated information. *PLOS Computational Biology*
    12(11):e1005123. doi:10.1371/journal.pcbi.1005123. [OA]
14. (2018). A measure of intelligence / integrated information critique. *PLOS ONE*
    13(10):e0205335. doi:10.1371/journal.pone.0205335. [OA]
15. Mediano PAM, et al. — integrated information and causal emergence context. *Entropy*
    22(7):726. doi:10.3390/e22070726. [OA]
16. (2024). Integrated information theory and the phenomenal-realism debate. *Erkenntnis*.
    doi:10.1007/s10670-024-00845-0.
17. Lenharo M (2023). Consciousness theory slammed as "pseudoscience." *Nature* news.
    doi:10.1038/d41586-023-02971-1. [secondary — the IIT-as-pseudoscience open-letter coverage]
18. Aaronson S (2014). Why I am not an integrated information theorist. Blog.
    https://scottaaronson.blog/?p=1799 [blog — context only, not load-bearing]

## Open questions carried forward

1. Is the negative claim exhaustive? A dedicated Scholar/Semantic Scholar search across management
   and organization-science venues, preprints, and non-English work is needed before a novelty
   claim.
2. Given the ~10-12-element ceiling, what is the most defensible organizational model for exact
   IIT-4.0 Φ — small formal units as discrete dynamical systems — versus proxies (Φ_AR, GNN) for
   larger structures.
3. Have IIT-adjacent measures (Φ_AR, ΦID, effective information / causal emergence) been applied to
   social or economic systems without PyPhi?
4. What transition probability matrix faithfully represents organizational coordination, and what
   would Φ, the major complex, and the cause-effect structure mean for organization design.

# Q221 — Closest prior-art check: identifiability, observational proxies, IIT

**Source-verified targeted review, 2026-10-15.** This is not an exhaustive systematic search and does not establish priority or novelty.

## Sources inspected

1. **Albantakis et al. (2023), IIT 4.0**. [Primary article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465). The theory's substrate is specified by a complete transition probability function and explicitly interprets it interventionally. Therefore observational recurrence summaries are not themselves the IIT-defined causal transition model. The q161 *leave-one-node-out bottleneck set* is a derived lab target, not a generic IIT theorem.
2. **Computing integrated information** (2017). [Oxford Academic](https://academic.oup.com/nc/article/2017/1/nix017/4060547). Discusses interventional calculus and contrasts perturbational causal structure with passive observation. This constrains any claim of recovery of IIT causal structure from time series alone.
3. **Barrett & Seth (2011), Practical Measures of Integrated Information for Time-Series Data.** [Open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3024259/). Introduces an empirical integrated-information measure based on the actual past-state distribution rather than the hypothetical perturbational distribution. The distinction between empirical information measures and IIT's interventional formalism is therefore long established.
4. **Assaad et al. (2024), Identifiability of total effects from abstractions of time series causal graphs.** [PMLR](https://proceedings.mlr.press/v244/assaad24a.html). Derives identifiability conditions for causal effects when lagged structure is abstracted. The general research question of what structural causal information survives a compressed time-series representation is established; Q221 cannot claim to originate it.
5. **Mediano et al., Beyond integrated information: A taxonomy of information dynamics phenomena.** [arXiv](https://arxiv.org/abs/1909.02297). Explores information decomposition beyond pairwise causal arrows, further limiting any broad claim that pairwise statistics miss higher-order effects as novel.
6. **PyPhi: A toolbox for integrated information theory** (2018). [Open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6080800/). Establishes the implementation lineage and the importance of specifying the exact formalism and software configuration.

## Claim-to-prior-art assessment

| Q221 claim | Status |
|---|---|
| Pairwise or compressed time-series summaries may fail to identify causal/structural targets | General phenomenon is established in adjacent literature |
| IIT distinguishes an interventional TPM from empirical time-series summaries | Established in IIT literature |
| Observational integrated-information proxies differ from IIT's interventional formalism | Established |
| A specific pair of three-node Boolean systems with matching categorical auto/cross recurrence profiles and differing **q161-defined** leave-one-out bottleneck sets | Supported as an exploratory computational construction in this repository; precise novelty **not established** |
| These examples are indistinguishable from complete observations | **False** for the reported examples: transition-aware baselines separate them |
| A new null estimator or universal identifiability theorem | Not supported |

## Conclusion

Q221 may be presented as a **specific, reproducible synthetic methods case study** showing insufficiency of a restricted recurrence representation for a lab-defined IIT target. Do not claim a new general impossibility theorem, an original surrogate method, or comprehensive novelty certification. A publication-grade novelty claim would require a reproducible systematic search and close methodological comparison of published IIT observational proxy/causal abstraction counterexamples.
